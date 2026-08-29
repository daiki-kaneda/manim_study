#!/usr/bin/env python3
"""Generate #1758–#1793 with derive/proof beats."""
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
    (1758, "相対ログ純度対", "1758_rel_log_purity", "RelLogPurity", "704_analysis_139", "box",
     ["相対ログ純度", "相対純次元", "ファイバー"], ["定義", "判定"], [r"\dim/S", r"\dim/S=d"], r"\dim/S=d"),
    (1759, "ログクエンチ対", "1759_log_quench_pair", "LogQuenchPair", "704_analysis_139", "box",
     ["ログクエンチ", "食い違い急減", "境界"], ["定義", "判定"], [r"a(E)", r"a(E)\searrow"], r"a(E)\searrow"),
    (1760, "相対ログクエンチ対", "1760_rel_log_quench", "RelLogQuench", "704_analysis_139", "box",
     ["相対ログクエンチ", "相対急減", "ファイバー"], ["定義", "判定"], [r"a(E/S)", r"a(E/S)\searrow"], r"a(E/S)\searrow"),
    (1761, "LookaheadBoundSoft", "1761_lookaheadboundsoft", "LookaheadBoundSoft", "705_linear_139", "opt",
     ["Lookahead境界軟化", "外側平均", "平滑"], ["核", "軟境界"], [r"x\leftarrow x+\alpha(y-x)", r"\eta\leftarrow\mathrm{soft}(\eta)"], r"\eta\leftarrow\mathrm{soft}(\mathrm{clip}(\eta))"),
    (1762, "ProdigySoftBound", "1762_prodigysoftbound", "ProdigySoftBound", "705_linear_139", "opt",
     ["Prodigy軟境界", "D推定", "平滑枠"], ["核", "軟境界"], [r"d\leftarrow\|g\|", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{clip}(\eta))"),
    (1763, "ScheduleFreeBoundSoft", "1763_schedulefreeboundsoft", "ScheduleFreeBoundSoft", "705_linear_139", "opt",
     ["平均化境界軟化", "スケジュール不要", "平滑"], ["核", "軟境界"], [r"z\leftarrow (1-c)z+cx", r"\eta\leftarrow\mathrm{soft}(\eta)"], r"\eta\leftarrow\mathrm{soft}(\mathrm{clip}(\eta))"),
    (1764, "垂心フォイエル弦比", "1764_h_feuer_chord", "HFeuerChord", "706_geometry_139", "tri",
     ["垂心フォイエル弦", "九点円弦", "比"], ["配置", "比"], [r"H", r"\ell_F/R"], r"\ell_F/R"),
    (1765, "重心フォイエル弦比", "1765_g_feuer_chord", "GFeuerChord", "706_geometry_139", "tri",
     ["重心フォイエル弦", "九点円弦", "比"], ["配置", "比"], [r"G", r"\ell_F/\ell"], r"\ell_F/\ell"),
    (1766, "九点フォイエル弦比", "1766_n_feuer_chord", "NFeuerChord", "706_geometry_139", "tri",
     ["九点円フォイエル弦", "弦", "比"], ["配置", "比"], [r"N", r"\ell_F/R_N"], r"\ell_F/R_N"),
    (1767, "局所一様エントロピー", "1767_local_uniform_entropy", "LocalUniformEntropy", "707_probability_137", "pts",
     ["局所一様エントロピー", "半径球", "対数"], ["定義", "尺度"], [r"H_{\mathrm{loc}}(\epsilon)", r"H_{\mathrm{loc}}=\log N_{\mathrm{loc}}"], r"H_{\mathrm{loc}}=\log N_{\mathrm{loc}}"),
    (1768, "経験局所被覆", "1768_emp_local_covering", "EmpLocalCovering", "707_probability_137", "pts",
     ["経験局所被覆", "データ半径球", "サイズ"], ["定義", "サイズ"], [r"N_n(B(f,r),\epsilon)", r"N_{n,\mathrm{loc}}(\epsilon)"], r"N_{n,\mathrm{loc}}(\epsilon)"),
    (1769, "根つき森細分", "1769_rooted_forest_refine", "RootedForestRefine", "708_combinatorics_136", "nums",
     ["根つき森", "成分", "細分"], ["定義", "細分"], [r"RF_n", r"RF(n,k)"], r"RF(n,k)", [1, 2, 7, 38, 291]),
    (1770, "ログ支持対", "1770_log_support_pair", "LogSupportPair", "709_analysis_140", "box",
     ["ログ支持", "境界支持", "因子"], ["定義", "条件"], [r"\mathrm{Supp}(D)", r"\mathrm{Supp}(D)=\bigcup D_i"], r"\mathrm{Supp}(D)=\bigcup D_i"),
    (1771, "相対ログ支持対", "1771_rel_log_support", "RelLogSupport", "709_analysis_140", "box",
     ["相対ログ支持", "相対支持", "ファイバー"], ["定義", "条件"], [r"\mathrm{Supp}(D)/S", r"\mathrm{Supp}(D)=\bigcup D_i"], r"\mathrm{Supp}(D)=\bigcup D_i"),
    (1772, "ログ係数対", "1772_log_coeff_pair", "LogCoeffPair", "709_analysis_140", "box",
     ["ログ係数", "境界係数", "区間"], ["定義", "条件"], [r"a_i", r"0\le a_i\le 1"], r"0\le a_i\le 1"),
    (1773, "AdamWSoftBound", "1773_adamwsoftbound", "AdamWSoftBound", "710_linear_140", "opt",
     ["AdamW軟境界", "減衰つき", "平滑枠"], ["核", "軟境界"], [r"u\leftarrow\hat m/\sqrt{\hat v}", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{clip}(\eta))"),
    (1774, "LionHardBound", "1774_lionhardbound", "LionHardBound", "710_linear_140", "opt",
     ["Lion硬境界", "符号更新", "枠剪定"], ["核", "硬境界"], [r"x\leftarrow x-\eta\mathrm{sign}(m)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{clip}(\eta))"),
    (1775, "SophiaHardBound", "1775_sophiahardbound", "SophiaHardBound", "710_linear_140", "opt",
     ["Sophia硬境界", "二階情報", "枠剪定"], ["核", "硬境界"], [r"\theta\leftarrow\theta-\eta m/\hat H", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{clip}(\eta))"),
    (1776, "内心類似フォイエル弦比", "1776_in_sym_feuer_chord", "InSymFeuerChord", "711_geometry_140", "tri",
     ["内心類似弦", "九点円弦", "比"], ["配置", "比"], [r"I", r"\ell_{F,s}/r"], r"\ell_{F,s}/r"),
    (1777, "傍心類似フォイエル弦比", "1777_ex_sym_feuer_chord", "ExSymFeuerChord", "711_geometry_140", "tri",
     ["傍心類似弦", "九点円弦", "比"], ["配置", "比"], [r"I_a", r"\ell_{F,s}/r_a"], r"\ell_{F,s}/r_a"),
    (1778, "外心類似フォイエル弦比", "1778_o_sym_feuer_chord", "OSymFeuerChord", "711_geometry_140", "tri",
     ["外心類似弦", "九点円弦", "比"], ["配置", "比"], [r"O", r"\ell_{F,s}/R"], r"\ell_{F,s}/R"),
    (1779, "経験局所パッキング", "1779_emp_local_packing", "EmpLocalPacking", "712_probability_138", "pts",
     ["経験局所パッキング", "データ半径球", "分離"], ["定義", "サイズ"], [r"M_n(B(f,r),\epsilon)", r"M_{n,\mathrm{loc}}(\epsilon)"], r"M_{n,\mathrm{loc}}(\epsilon)"),
    (1780, "スケール標本複雑度", "1780_scale_sample_comp", "ScaleSampleComp", "712_probability_138", "pts",
     ["スケール標本複雑度", "半径依存", "上界"], ["定義", "依存"], [r"\mathfrak{C}(r)", r"\mathfrak{C}(r)\propto r^{\alpha}"], r"\mathfrak{C}(r)\propto r^{\alpha}"),
    (1781, "ラベル木細分", "1781_labeled_tree_refine", "LabeledTreeRefine", "713_combinatorics_137", "nums",
     ["ラベル木", "頂点ラベル", "細分"], ["定義", "細分"], [r"n^{n-2}", r"L(n,k)"], r"L(n,k)", [1, 1, 3, 16, 125]),
    (1782, "相対ログ係数対", "1782_rel_log_coeff", "RelLogCoeff", "714_analysis_141", "box",
     ["相対ログ係数", "相対境界係数", "区間"], ["定義", "条件"], [r"a_i", r"0\le a_i\le 1"], r"0\le a_i\le 1"),
    (1783, "ログ重み対", "1783_log_weight_pair", "LogWeightPair", "714_analysis_141", "box",
     ["ログ重み", "境界重み", "総和"], ["定義", "条件"], [r"w(D)", r"w(D)=\sum a_i"], r"w(D)=\sum a_i"),
    (1784, "相対ログ重み対", "1784_rel_log_weight", "RelLogWeight", "714_analysis_141", "box",
     ["相対ログ重み", "相対重み", "ファイバー"], ["定義", "条件"], [r"w(D/S)", r"w(D)=\sum a_i"], r"w(D)=\sum a_i"),
    (1785, "NAdamSoftHardBound", "1785_nadamsofthardbound", "NAdamSoftHardBound", "715_linear_141", "opt",
     ["NAdam軟硬境界", "ネステロフ", "枠二段"], ["軟", "硬"], [r"\eta\leftarrow\mathrm{soft}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{soft}(\mathrm{clip}(\eta)))"),
    (1786, "RMSHardBound", "1786_rmshardbound", "RMSHardBound", "715_linear_141", "opt",
     ["RMS硬境界", "二乗平均", "枠剪定"], ["核", "硬境界"], [r"v\leftarrow\beta v+(1-\beta)g^2", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{clip}(\eta))"),
    (1787, "LARSBoundSoft", "1787_larsboundsoft", "LARSBoundSoft", "715_linear_141", "opt",
     ["LARS境界軟化", "層正規化", "平滑"], ["核", "軟境界"], [r"\eta\leftarrow\|w\|/\|g\|", r"\eta\leftarrow\mathrm{soft}(\eta)"], r"\eta\leftarrow\mathrm{soft}(\mathrm{clip}(\eta))"),
    (1788, "垂心類似フォイエル弦比", "1788_h_sym_feuer_chord", "HSymFeuerChord", "716_geometry_141", "tri",
     ["垂心類似弦", "九点円弦", "比"], ["配置", "比"], [r"H", r"\ell_{F,s}/R"], r"\ell_{F,s}/R"),
    (1789, "重心類似フォイエル弦比", "1789_g_sym_feuer_chord", "GSymFeuerChord", "716_geometry_141", "tri",
     ["重心類似弦", "九点円弦", "比"], ["配置", "比"], [r"G", r"\ell_{F,s}/\ell"], r"\ell_{F,s}/\ell"),
    (1790, "九点類似フォイエル弦比", "1790_n_sym_feuer_chord", "NSymFeuerChord", "716_geometry_141", "tri",
     ["九点円類似弦", "弦", "比"], ["配置", "比"], [r"N", r"\ell_{F,s}/R_N"], r"\ell_{F,s}/R_N"),
    (1791, "半径被覆数", "1791_radius_covering", "RadiusCovering", "717_probability_139", "pts",
     ["半径被覆数", "球被覆", "サイズ"], ["定義", "サイズ"], [r"N(r,\epsilon)", r"N(r,\epsilon)\lesssim (r/\epsilon)^d"], r"N(r,\epsilon)\lesssim (r/\epsilon)^d"),
    (1792, "半径パッキング数", "1792_radius_packing", "RadiusPacking", "717_probability_139", "pts",
     ["半径パッキング数", "球分離", "サイズ"], ["定義", "サイズ"], [r"M(r,\epsilon)", r"M(r,\epsilon)\lesssim (r/\epsilon)^d"], r"M(r,\epsilon)\lesssim (r/\epsilon)^d"),
    (1793, "ケイリー細分", "1793_cayley_refine", "CayleyRefine", "718_combinatorics_138", "nums",
     ["ケイリー", "木の公式", "細分"], ["定義", "細分"], [r"n^{n-2}", r"Cay(n,k)"], r"Cay(n,k)", [1, 1, 3, 16, 125]),
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
        if num in (1770, 1771):
            clean_dtex = [r"\mathrm{Supp}(D)" if False else r"S(D)", r"S(D)=\bigcup D_i"]
            # avoid long English Supp - use S(D)
            clean_dtex = [r"S(D)", r"S(D)=\bigcup D_i"]
            clean_final = r"S(D)=\bigcup D_i"
        elif num == 1767:
            clean_dtex = [r"H_{\mathrm{loc}}(\epsilon)", r"H_{\mathrm{loc}}=\log N_{\mathrm{loc}}"]
            clean_final = r"H_{\mathrm{loc}}=\log N_{\mathrm{loc}}"
        elif num == 1768:
            clean_dtex = [r"N_n(B,\epsilon)", r"N_{n,\mathrm{loc}}(\epsilon)"]
            clean_final = r"N_{n,\mathrm{loc}}(\epsilon)"
        elif num == 1779:
            clean_dtex = [r"M_n(B,\epsilon)", r"M_{n,\mathrm{loc}}(\epsilon)"]
            clean_final = r"M_{n,\mathrm{loc}}(\epsilon)"
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
    assert "VIDEOS_1758_1769" not in text

    def block(name, items):
        lines = [f"\n\n{name}: tuple[Video, ...] = ("]
        for num, title, path, cls in items:
            lines.append(f'    Video({num}, "{title}", "{path}", "{cls}"),')
        lines.append(")")
        return "\n".join(lines)

    cp.write_text(
        text.rstrip()
        + block("VIDEOS_1758_1769", created[:12])
        + block("VIDEOS_1770_1781", created[12:24])
        + block("VIDEOS_1782_1793", created[24:])
        + "\n",
        encoding="utf-8",
    )

    tp = ROOT / "tests/test_catalog.py"
    t = tp.read_text(encoding="utf-8")
    if "VIDEOS_1758_1769" not in t:
        t = t.replace(
            "VIDEOS_1746_1757 = _catalog.VIDEOS_1746_1757\n",
            "VIDEOS_1746_1757 = _catalog.VIDEOS_1746_1757\n"
            "VIDEOS_1758_1769 = _catalog.VIDEOS_1758_1769\n"
            "VIDEOS_1770_1781 = _catalog.VIDEOS_1770_1781\n"
            "VIDEOS_1782_1793 = _catalog.VIDEOS_1782_1793\n",
        )
        insert = """
    def test_numbers_are_1758_to_1769(self):
        nums = [v.number for v in VIDEOS_1758_1769]
        self.assertEqual(nums, list(range(1758, 1770)))


    def test_numbers_are_1770_to_1781(self):
        nums = [v.number for v in VIDEOS_1770_1781]
        self.assertEqual(nums, list(range(1770, 1782)))


    def test_numbers_are_1782_to_1793(self):
        nums = [v.number for v in VIDEOS_1782_1793]
        self.assertEqual(nums, list(range(1782, 1794)))

"""
        t = t.replace(
            "    def test_each_scene_file_defines_the_class(self):",
            insert + "    def test_each_scene_file_defines_the_class(self):",
        )
        t = t.replace(
            "            *VIDEOS_1746_1757,\n        ):",
            "            *VIDEOS_1746_1757,\n"
            "            *VIDEOS_1758_1769,\n"
            "            *VIDEOS_1770_1781,\n"
            "            *VIDEOS_1782_1793,\n"
            "        ):",
        )
        tp.write_text(t, encoding="utf-8")

    plan = ROOT / "project/math/PLAN.md"
    p = plan.read_text(encoding="utf-8")
    if "#1758" not in p:
        extra = "\n\n## 導出つき続き（#1758–#1769）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[:12]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#1770–#1781）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[12:24]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#1782–#1793）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[24:]:
            extra += f"| {num} | {title} | 実装 |\n"
        p = p.replace("## 1 本の作業フロー", extra + "\n## 1 本の作業フロー")
        plan.write_text(p, encoding="utf-8")

    print("created", created[0][0], "-", created[-1][0])


if __name__ == "__main__":
    main()
