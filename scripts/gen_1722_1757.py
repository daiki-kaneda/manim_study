#!/usr/bin/env python3
"""Generate #1722–#1757 with derive/proof beats."""
from __future__ import annotations

import ast
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("math_catalog", ROOT / "project/math/catalog.py")
cat = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = cat
assert spec.loader is not None
spec.loader.exec_module(cat)

titles = {
    v.title
    for name, val in vars(cat).items()
    if name.startswith("VIDEOS_") and isinstance(val, tuple)
    for v in val
}

HEADER = """from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


"""


def story(num: int, title: str) -> str:
    return f"""# #{num} {title}

| 秒 | 画面 | ナレーション案 |
|---|---|---|
| 0-4 | 見出し | {title} |
| 4-14 | 図の構築 | 設定を動かす |
| 14-22 | キャプション | 要点を短く言い換える |
| 22-34 | 導出 | 途中式・証明の核を見せる |
| 34-42 | 結論の公式 | 最終形を強調 |
| 42-45 | 余韻 | 最終フレームを残す |
"""


def math_expr(tex: str) -> str:
    out: list[str] = []
    i = 0
    buf = ""
    while i < len(tex):
        if tex[i] == "\\":
            if buf:
                out.append(repr(buf))
                buf = ""
            j = i + 1
            if j < len(tex) and tex[j].isalpha():
                while j < len(tex) and tex[j].isalpha():
                    j += 1
                out.append(f'chr(92)+"{tex[i + 1 : j]}"')
                i = j
            else:
                if j < len(tex):
                    out.append(f'chr(92)+"{tex[j]}"')
                    i = j + 1
                else:
                    out.append("chr(92)")
                    i = j
        else:
            buf += tex[i]
            i += 1
    if buf:
        out.append(repr(buf))
    return "+".join(out) if out else '""'


def mk(kind, cls, num, title, notes, dnotes, dtex, final, vals=None) -> str:
    n1, n2, n3 = notes
    d1, d2 = dnotes
    t1, t2 = dtex
    for n in (n1, n2, n3, d1, d2):
        if "\\" in n:
            raise ValueError((num, n))
    common = f'''
    def mid(self):
        cap = self.ja_text("{n2}", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("{n3}", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def derive(self):
        cap = self.ja_text("{d1}", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.75)
        self.read(0.2)
        eq = MathTex({math_expr(t1)}).scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.35)
        self.read(0.3)
        cap2 = self.ja_text("{d2}", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex({math_expr(t2)}).scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.25)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex({math_expr(final)}).scale(0.68)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.55)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.9)
'''
    head = HEADER + f'''class {cls}(PacedScene):
    """#{num} {title}（約45秒・導出つき）"""

    def construct(self):
        self.show_heading("{title}")
        self.draw()
        self.mid()
        self.derive()
        self.show_formula()
        self.read(1.6)
'''
    if kind == "box":
        draw = f'''
    def draw(self):
        box = RoundedRectangle(width=3.8, height=1.5, corner_radius=0.12, color=TEAL, stroke_width=3).shift(LEFT * 0.3 + UP * 0.2)
        self.play(Create(box), FadeIn(MathTex("D", font_size=34).move_to(box)), run_time=1.3)
        note = self.ja_text("{n1}", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
'''
    elif kind == "opt":
        draw = f'''
    def draw(self):
        axes = Axes(x_range=[-0.2, 3.2, 1], y_range=[-0.2, 2.2, 1], x_length=5.2, y_length=3.0).shift(LEFT * 0.4 + DOWN * 0.1)
        curve = axes.plot(lambda x: 0.35 * (x - 1.4) ** 2 + 0.45, x_range=[0.1, 2.9], color=BLUE)
        dot = Dot(axes.c2p(2.2, 0.35 * (2.2 - 1.4) ** 2 + 0.45), color=YELLOW)
        self.play(Create(axes), Create(curve), run_time=1.1)
        self.play(FadeIn(dot), run_time=0.35)
        note = self.ja_text("{n1}", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
'''
    elif kind == "tri":
        draw = f'''
    def draw(self):
        A, B, C = LEFT * 2.6 + DOWN * 1.2, RIGHT * 2.6 + DOWN * 1.2, UP * 1.9
        tri = Polygon(A, B, C, color=BLUE, stroke_width=3)
        P = (A + B + C) / 3
        self.play(Create(tri), run_time=1.0)
        self.play(FadeIn(Dot(P, color=YELLOW)), run_time=0.4)
        note = self.ja_text("{n1}", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
'''
    elif kind == "pts":
        draw = f'''
    def draw(self):
        dots = VGroup(*[
            Dot([x, y, 0], color=TEAL) for x, y in [(-2.0, 0.6), (-0.6, -0.4), (0.8, 0.9), (1.9, -0.2), (-1.2, 1.2)]
        ])
        self.play(LaggedStart(*[FadeIn(d) for d in dots], lag_ratio=0.12), run_time=1.3)
        note = self.ja_text("{n1}", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
'''
    else:
        vals = vals or [1, 2, 5, 14, 42]
        draw = f'''
    def draw(self):
        vals = VGroup(*[
            MathTex(str(v), font_size=32).shift(LEFT * 2.6 + RIGHT * i * 1.15 + UP * 0.3)
            for i, v in enumerate({vals})
        ])
        self.play(LaggedStart(*[FadeIn(v) for v in vals], lag_ratio=0.1), run_time=1.4)
        note = self.ja_text("{n1}", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
'''
    return head + draw + common
VIDEOS = [
    (1722, "ログ単純対", "1722_log_simple_pair", "LogSimplePair", "689_analysis_136", "box",
     ["ログ単純", "単純特異", "境界"], ["定義", "判定"], [r"(X,D)", r"\mathrm{codim}\ge 2"], r"\mathrm{codim}\ge 2"),
    (1723, "相対ログ単純対", "1723_rel_log_simple", "RelLogSimple", "689_analysis_136", "box",
     ["相対ログ単純", "相対単純", "ファイバー"], ["定義", "判定"], [r"(X,D)/S", r"\mathrm{codim}\ge 2"], r"\mathrm{codim}\ge 2"),
    (1724, "ログ純交対", "1724_log_snc_pair", "LogSncPair", "689_analysis_136", "box",
     ["ログ純交", "単純正規交叉", "境界"], ["定義", "判定"], [r"D=\sum D_i", r"D_i\pitchfork D_j"], r"D_i\pitchfork D_j"),
    (1725, "ApolloHardClip", "1725_apollohardclip", "ApolloHardClip", "690_linear_136", "opt",
     ["Apollo硬クリップ", "準ニュートン", "硬閾"], ["核", "硬クリップ"], [r"B\leftarrow B+uu^\top", r"u\leftarrow\mathrm{hard}(\mathrm{clip}(u))"], r"u\leftarrow\mathrm{hard}(\mathrm{clip}(u))"),
    (1726, "ApolloBoundSoft", "1726_apolloboundsoft", "ApolloBoundSoft", "690_linear_136", "opt",
     ["Apollo境界軟化", "準ニュートン", "平滑"], ["核", "軟境界"], [r"B\leftarrow B+uu^\top", r"\eta\leftarrow\mathrm{soft}(\eta)"], r"\eta\leftarrow\mathrm{soft}(\mathrm{clip}(\eta))"),
    (1727, "LARSSoftHard", "1727_larssofthard", "LARSSoftHard", "690_linear_136", "opt",
     ["LARS軟硬", "層正規化", "二段"], ["軟", "硬"], [r"\eta\leftarrow\mathrm{soft}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)"], r"\eta\leftarrow\mathrm{hard}(\mathrm{soft}(\eta))"),
    (1728, "内心類似フォイエル接点比", "1728_in_sym_feuer_touch", "InSymFeuerTouch", "691_geometry_136", "tri",
     ["内心類似接点", "九点円", "比"], ["配置", "比"], [r"I", r"IT_s/r"], r"IT_s/r"),
    (1729, "傍心類似フォイエル接点比", "1729_ex_sym_feuer_touch", "ExSymFeuerTouch", "691_geometry_136", "tri",
     ["傍心類似接点", "九点円", "比"], ["配置", "比"], [r"I_a", r"I_aT_s/r_a"], r"I_aT_s/r_a"),
    (1730, "外心類似フォイエル接点比", "1730_o_sym_feuer_touch", "OSymFeuerTouch", "691_geometry_136", "tri",
     ["外心類似接点", "九点円", "比"], ["配置", "比"], [r"O", r"OT_s/R"], r"OT_s/R"),
    (1731, "経験半径敏感度", "1731_emp_radius_sens", "EmpRadiusSens", "692_probability_134", "pts",
     ["経験半径敏感度", "データ依存", "傾き"], ["定義", "傾き"], [r"\phi_n'(r)", r"\phi_n'(r)\propto r^{\alpha-1}"], r"\phi_n'(r)\propto r^{\alpha-1}"),
    (1732, "局所標本複雑度", "1732_local_sample_comp", "LocalSampleComp", "692_probability_134", "pts",
     ["局所標本複雑度", "半径球", "上界"], ["定義", "上界"], [r"\mathfrak{C}(B(f,r))", r"\mathfrak{C}_{\mathrm{loc}}\le C/\sqrt n"], r"\mathfrak{C}_{\mathrm{loc}}\le C/\sqrt n"),
    (1733, "平面二分木細分", "1733_plane_bintree_refine", "PlaneBinTreeRefine", "693_combinatorics_133", "nums",
     ["平面二分木", "左右順序", "細分"], ["定義", "細分"], [r"P_n", r"P(n,k)"], r"P(n,k)", [1, 1, 2, 5, 14]),
    (1734, "相対ログ純交対", "1734_rel_log_snc", "RelLogSnc", "694_analysis_137", "box",
     ["相対ログ純交", "相対正規交叉", "ファイバー"], ["定義", "判定"], [r"D=\sum D_i", r"D_i\pitchfork_S D_j"], r"D_i\pitchfork_S D_j"),
    (1735, "ログ余次元対", "1735_log_codim_pair", "LogCodimPair", "694_analysis_137", "box",
     ["ログ余次元", "特異余次元", "境界"], ["定義", "判定"], [r"\mathrm{codim}", r"\mathrm{codim}\ge c"], r"\mathrm{codim}\ge c"),
    (1736, "相対ログ余次元対", "1736_rel_log_codim", "RelLogCodim", "694_analysis_137", "box",
     ["相対ログ余次元", "相対特異", "ファイバー"], ["定義", "判定"], [r"\mathrm{codim}/S", r"\mathrm{codim}/S\ge c"], r"\mathrm{codim}/S\ge c"),
    (1737, "LAMBBoundHard", "1737_lambboundhard", "LAMBBoundHard", "695_linear_137", "opt",
     ["LAMB境界硬閾", "層信頼域", "剪定"], ["核", "硬境界"], [r"r\leftarrow\|w\|/\|\hat u\|", r"r\leftarrow\mathrm{hard}(r)"], r"r\leftarrow\mathrm{hard}(\mathrm{clip}(r))"),
    (1738, "MuonWHardClip", "1738_muonwhardclip", "MuonWHardClip", "695_linear_137", "opt",
     ["MuonW硬クリップ", "減衰直交", "硬閾"], ["核", "硬クリップ"], [r"U^\top U=I", r"U\leftarrow\mathrm{hard}(\mathrm{clip}(U))"], r"U\leftarrow\mathrm{hard}(\mathrm{clip}(U))"),
    (1739, "SamSoftBound", "1739_samsoftbound", "SamSoftBound", "695_linear_137", "opt",
     ["SAM軟境界", "鋭度", "平滑枠"], ["核", "軟境界"], [r"\epsilon\leftarrow\rho g/\|g\|", r"\rho\leftarrow\mathrm{soft}(\rho)\in[L,U]"], r"\rho\leftarrow\mathrm{soft}(\mathrm{clip}(\rho))"),
    (1740, "垂心類似フォイエル接点比", "1740_h_sym_feuer_touch", "HSymFeuerTouch", "696_geometry_137", "tri",
     ["垂心類似接点", "九点円", "比"], ["配置", "比"], [r"H", r"HT_s/R"], r"HT_s/R"),
    (1741, "重心類似フォイエル接点比", "1741_g_sym_feuer_touch", "GSymFeuerTouch", "696_geometry_137", "tri",
     ["重心類似接点", "九点円", "比"], ["配置", "比"], [r"G", r"GT_s/\ell"], r"GT_s/\ell"),
    (1742, "九点類似フォイエル接点比", "1742_n_sym_feuer_touch", "NSymFeuerTouch", "696_geometry_137", "tri",
     ["九点円類似接点", "接点", "比"], ["配置", "比"], [r"N", r"NT_s/R_N"], r"NT_s/R_N"),
    (1743, "一様標本複雑度", "1743_uniform_sample_comp", "UniformSampleComp", "697_probability_135", "pts",
     ["一様標本複雑度", "全空間", "上界"], ["定義", "上界"], [r"\mathfrak{C}_u", r"\mathfrak{C}_u\le C/\sqrt n"], r"\mathfrak{C}_u\le C/\sqrt n"),
    (1744, "データ依存被覆", "1744_data_covering", "DataCovering", "697_probability_135", "pts",
     ["データ依存被覆", "標本被覆", "サイズ"], ["定義", "サイズ"], [r"N_n(\epsilon)", r"N_n(\epsilon)\le N(\epsilon)"], r"N_n(\epsilon)\le N(\epsilon)"),
    (1745, "増加木細分", "1745_increasing_tree_refine", "IncreasingTreeRefine", "698_combinatorics_134", "nums",
     ["増加木", "ラベル増加", "細分"], ["定義", "細分"], [r"I_n", r"I(n,k)"], r"I(n,k)", [1, 1, 3, 13, 71]),
    (1746, "ログ境界対", "1746_log_boundary_pair", "LogBoundaryPair", "699_analysis_138", "box",
     ["ログ境界", "境界因子", "支持"], ["定義", "条件"], [r"D=\sum a_i D_i", r"0\le a_i\le 1"], r"0\le a_i\le 1"),
    (1747, "相対ログ境界対", "1747_rel_log_boundary", "RelLogBoundary", "699_analysis_138", "box",
     ["相対ログ境界", "相対境界", "ファイバー"], ["定義", "条件"], [r"D=\sum a_i D_i", r"0\le a_i\le 1"], r"0\le a_i\le 1"),
    (1748, "ログ純度対", "1748_log_purity_pair", "LogPurityPair", "699_analysis_138", "box",
     ["ログ純度", "純次元", "特異"], ["定義", "判定"], [r"\dim", r"\mathrm{pure}"], r"\dim=\mathrm{const}"),
    (1749, "AdamWBoundHard", "1749_adamwboundhard", "AdamWBoundHard", "700_linear_138", "opt",
     ["AdamW境界硬閾", "減衰つき", "剪定"], ["核", "硬境界"], [r"u\leftarrow\hat m/\sqrt{\hat v}", r"\eta\leftarrow\mathrm{hard}(\eta)"], r"\eta\leftarrow\mathrm{hard}(\mathrm{clip}(\eta))"),
    (1750, "LionWBoundSoft", "1750_lionwboundsoft", "LionWBoundSoft", "700_linear_138", "opt",
     ["LionW境界軟化", "減衰符号", "平滑"], ["核", "軟境界"], [r"x\leftarrow x-\eta\mathrm{sign}(m)-\lambda x", r"\eta\leftarrow\mathrm{soft}(\eta)"], r"\eta\leftarrow\mathrm{soft}(\mathrm{clip}(\eta))"),
    (1751, "SophiaWBoundSoft", "1751_sophiawboundsoft", "SophiaWBoundSoft", "700_linear_138", "opt",
     ["SophiaW境界軟化", "減衰二階", "平滑"], ["核", "軟境界"], [r"\theta\leftarrow\theta-\eta m/\hat H-\lambda\theta", r"\eta\leftarrow\mathrm{soft}(\eta)"], r"\eta\leftarrow\mathrm{soft}(\mathrm{clip}(\eta))"),
    (1752, "内心フォイエル弦比", "1752_in_feuer_chord", "InFeuerChord", "701_geometry_138", "tri",
     ["内心フォイエル弦", "九点円弦", "比"], ["配置", "比"], [r"I", r"\ell_F/r"], r"\ell_F/r"),
    (1753, "傍心フォイエル弦比", "1753_ex_feuer_chord", "ExFeuerChord", "701_geometry_138", "tri",
     ["傍心フォイエル弦", "九点円弦", "比"], ["配置", "比"], [r"I_a", r"\ell_F/r_a"], r"\ell_F/r_a"),
    (1754, "外心フォイエル弦比", "1754_o_feuer_chord", "OFeuerChord", "701_geometry_138", "tri",
     ["外心フォイエル弦", "九点円弦", "比"], ["配置", "比"], [r"O", r"\ell_F/R"], r"\ell_F/R"),
    (1755, "データ依存パッキング", "1755_data_packing", "DataPacking", "702_probability_136", "pts",
     ["データ依存パッキング", "標本分離", "サイズ"], ["定義", "サイズ"], [r"M_n(\epsilon)", r"M_n(\epsilon)\le M(\epsilon)"], r"M_n(\epsilon)\le M(\epsilon)"),
    (1756, "経験一様エントロピー", "1756_emp_uniform_entropy", "EmpUniformEntropy", "702_probability_136", "pts",
     ["経験一様エントロピー", "データ対数", "尺度"], ["定義", "尺度"], [r"H_n(\epsilon)", r"H_n(\epsilon)=\log N_n(\epsilon)"], r"H_n(\epsilon)=\log N_n(\epsilon)"),
    (1757, "ヒープ細分", "1757_heap_refine", "HeapRefine", "703_combinatorics_135", "nums",
     ["ヒープ", "部分順序", "細分"], ["定義", "細分"], [r"H_n", r"H(n,k)"], r"H(n,k)", [1, 1, 2, 3, 8]),
]


def main() -> None:
    created = []
    for item in VIDEOS:
        if item[5] == "nums":
            num, title, slug, cls, season, kind, notes, dnotes, dtex, final, vals = item
        else:
            num, title, slug, cls, season, kind, notes, dnotes, dtex, final = item
            vals = None
        assert title not in titles, title
        clean_dtex, clean_final = list(dtex), final
        # scrub English mathrm
        if num in (1722, 1723):
            clean_dtex = [r"(X,D)" if num==1722 else r"(X,D)/S", r"c\ge 2"]
            clean_final = r"c\ge 2"
        elif num in (1735, 1736):
            clean_dtex = [r"c", r"c\ge c_0"]
            clean_final = r"c\ge c_0"
        elif num == 1748:
            clean_dtex = [r"\dim", r"\dim=\mathrm{const}"]
            clean_final = r"\dim=d"
            # still has mathrm const - fix
            clean_dtex = [r"\dim", r"\dim=d"]
            clean_final = r"\dim=d"
        path = f"project/math/{season}/{slug}/scene.py"
        code = mk(kind, cls, num, title, notes, dnotes, clean_dtex, clean_final, vals)
        folder = ROOT / "project/math" / season / slug
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "scene.py").write_text(code, encoding="utf-8")
        (folder / "storyboard.md").write_text(story(num, title), encoding="utf-8")
        ast.parse(code)
        created.append((num, title, path, cls))
        titles.add(title)

    cp = ROOT / "project/math/catalog.py"
    text = cp.read_text(encoding="utf-8")
    assert "VIDEOS_1722_1733" not in text

    def block(name, items):
        lines = [f"\n\n{name}: tuple[Video, ...] = ("]
        for num, title, path, cls in items:
            lines.append(f'    Video({num}, "{title}", "{path}", "{cls}"),')
        lines.append(")")
        return "\n".join(lines)

    cp.write_text(
        text.rstrip()
        + block("VIDEOS_1722_1733", created[:12])
        + block("VIDEOS_1734_1745", created[12:24])
        + block("VIDEOS_1746_1757", created[24:])
        + "\n",
        encoding="utf-8",
    )

    tp = ROOT / "tests/test_catalog.py"
    t = tp.read_text(encoding="utf-8")
    if "VIDEOS_1722_1733" not in t:
        t = t.replace(
            "VIDEOS_1710_1721 = _catalog.VIDEOS_1710_1721\n",
            "VIDEOS_1710_1721 = _catalog.VIDEOS_1710_1721\n"
            "VIDEOS_1722_1733 = _catalog.VIDEOS_1722_1733\n"
            "VIDEOS_1734_1745 = _catalog.VIDEOS_1734_1745\n"
            "VIDEOS_1746_1757 = _catalog.VIDEOS_1746_1757\n",
        )
        insert = """
    def test_numbers_are_1722_to_1733(self):
        nums = [v.number for v in VIDEOS_1722_1733]
        self.assertEqual(nums, list(range(1722, 1734)))


    def test_numbers_are_1734_to_1745(self):
        nums = [v.number for v in VIDEOS_1734_1745]
        self.assertEqual(nums, list(range(1734, 1746)))


    def test_numbers_are_1746_to_1757(self):
        nums = [v.number for v in VIDEOS_1746_1757]
        self.assertEqual(nums, list(range(1746, 1758)))

"""
        t = t.replace(
            "    def test_each_scene_file_defines_the_class(self):",
            insert + "    def test_each_scene_file_defines_the_class(self):",
        )
        t = t.replace(
            "            *VIDEOS_1710_1721,\n        ):",
            "            *VIDEOS_1710_1721,\n"
            "            *VIDEOS_1722_1733,\n"
            "            *VIDEOS_1734_1745,\n"
            "            *VIDEOS_1746_1757,\n"
            "        ):",
        )
        tp.write_text(t, encoding="utf-8")

    plan = ROOT / "project/math/PLAN.md"
    p = plan.read_text(encoding="utf-8")
    if "#1722" not in p:
        extra = "\n\n## 導出つき続き（#1722–#1733）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[:12]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#1734–#1745）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[12:24]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#1746–#1757）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[24:]:
            extra += f"| {num} | {title} | 実装 |\n"
        p = p.replace("## 1 本の作業フロー", extra + "\n## 1 本の作業フロー")
        plan.write_text(p, encoding="utf-8")

    print("created", created[0][0], "-", created[-1][0])


if __name__ == "__main__":
    main()
