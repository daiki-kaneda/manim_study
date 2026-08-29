#!/usr/bin/env python3
"""Generate #1650–#1685 with derive/proof beats."""
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
    (1650, "相対ログフロップ対", "1650_rel_log_flop", "RelLogFlop", "659_analysis_130", "box",
     ["相対ログフロップ", "K自明", "双有理"], ["定義", "変換"], [r"K_X\cdot C=0", r"X\dashrightarrow_S X'"], r"X\dashrightarrow_S X'"),
    (1651, "ログ極小モデル対", "1651_log_mmp_pair", "LogMmpPair", "659_analysis_130", "box",
     ["ログ極小モデル", "ネフ化", "終端"], ["手順", "結論"], [r"K+D", r"(K+D)\cdot C\ge 0"], r"(K+D)\cdot C\ge 0"),
    (1652, "相対ログ極小モデル対", "1652_rel_log_mmp", "RelLogMmp", "659_analysis_130", "box",
     ["相対ログ極小モデル", "相対ネフ化", "終端"], ["手順", "結論"], [r"K+D", r"(K+D)\cdot C\ge 0"], r"(K+D)\cdot C\ge 0"),
    (1653, "LionWSoftClip", "1653_lionwsoftclip", "LionWSoftClip", "660_linear_130", "opt",
     ["LionW軟クリップ", "減衰符号", "二重"], ["核", "軟クリップ"], [r"x\leftarrow x-\eta\mathrm{sign}(m)-\lambda x", r"u\leftarrow\mathrm{clip}(\mathrm{soft}(u))"], r"u\leftarrow\mathrm{clip}(\mathrm{soft}(u))"),
    (1654, "SophiaWSoftClip", "1654_sophiawsoftclip", "SophiaWSoftClip", "660_linear_130", "opt",
     ["SophiaW軟クリップ", "減衰二階", "二重"], ["核", "軟クリップ"], [r"\theta\leftarrow\theta-\eta m/\hat H-\lambda\theta", r"u\leftarrow\mathrm{clip}(\mathrm{soft}(u))"], r"u\leftarrow\mathrm{clip}(\mathrm{soft}(u))"),
    (1655, "AdaFactorHardClip", "1655_adafactorhardclip", "AdaFactorHardClip", "660_linear_130", "opt",
     ["AdaFactor硬クリップ", "因子化", "硬閾"], ["核", "硬クリップ"], [r"R_{ij}C_{ij}\approx G_{ij}^2", r"u\leftarrow\mathrm{hard}(\mathrm{clip}(u))"], r"u\leftarrow\mathrm{hard}(\mathrm{clip}(u))"),
    (1656, "内心フォイエルバッハ比", "1656_in_feuerbach_ratio", "InFeuerbachRatio", "661_geometry_130", "tri",
     ["内心とフォイエルバッハ", "九点円接点", "比"], ["配置", "比"], [r"I", r"d(I,N)/r"], r"d(I,N)/r"),
    (1657, "傍心フォイエルバッハ比", "1657_ex_feuerbach_ratio", "ExFeuerbachRatio", "661_geometry_130", "tri",
     ["傍心とフォイエルバッハ", "九点円接点", "比"], ["配置", "比"], [r"I_a", r"d(I_a,N)/r_a"], r"d(I_a,N)/r_a"),
    (1658, "外心フォイエルバッハ比", "1658_o_feuerbach_ratio", "OFeuerbachRatio", "661_geometry_130", "tri",
     ["外心とフォイエルバッハ", "九点円", "比"], ["配置", "比"], [r"O", r"ON/R"], r"ON/R"),
    (1659, "経験劣ガウス", "1659_empirical_subgauss", "EmpiricalSubgauss", "662_probability_128", "pts",
     ["経験劣ガウス", "データ尾部", "集中"], ["定義", "尾部"], [r"\psi_{2,n}", r"\mathbb{P}_n(|X|>t)\le 2e^{-t^2/K}"], r"\mathbb{P}_n(|X|>t)\le 2e^{-t^2/K}"),
    (1660, "局所チャイニング", "1660_local_chaining", "LocalChaining", "662_probability_128", "pts",
     ["局所チェイニング", "半径球", "階層"], ["構成", "上界"], [r"\gamma_2(B(f,r))", r"\mathbb{E}\sup_{B}X\le C\gamma_2"], r"\mathbb{E}\sup_{B}X\le C\gamma_2"),
    (1661, "根つき木細分", "1661_rooted_tree_refine", "RootedTreeRefine", "663_combinatorics_127", "nums",
     ["根つき木", "向き", "細分"], ["定義", "細分"], [r"n^{n-1}", r"R(n,k)"], r"R(n,k)", [1, 2, 9, 64, 625]),
    (1662, "ログ終端対", "1662_log_terminal_model", "LogTerminalModel", "664_analysis_131", "box",
     ["ログ終端", "終端モデル", "ネフ"], ["定義", "判定"], [r"a(E)>0", r"(K+D)\cdot C\ge 0"], r"(K+D)\cdot C\ge 0"),
    (1663, "相対ログ終端対", "1663_rel_log_terminal_model", "RelLogTerminalModel", "664_analysis_131", "box",
     ["相対ログ終端", "相対終端", "相対ネフ"], ["定義", "判定"], [r"a(E/S)>0", r"(K+D)\cdot C\ge 0"], r"(K+D)\cdot C\ge 0"),
    (1664, "ログ安定対", "1664_log_stable_pair", "LogStablePair", "664_analysis_131", "box",
     ["ログ安定", "半安定", "平坦族"], ["定義", "条件"], [r"(X,D)", r"K_X+D"], r"K_X+D"),
    (1665, "NAdamBoundHard", "1665_nadamboundhard", "NAdamBoundHard", "665_linear_131", "opt",
     ["NAdam境界硬閾", "ネステロフ", "剪定"], ["核", "硬境界"], [r"m\leftarrow\beta m+(1-\beta)g", r"\eta\leftarrow\mathrm{hard}(\eta)"], r"\eta\leftarrow\mathrm{hard}(\mathrm{clip}(\eta))"),
    (1666, "RMSBoundHard", "1666_rmsboundhard", "RMSBoundHard", "665_linear_131", "opt",
     ["RMS境界硬閾", "二乗平均", "剪定"], ["核", "硬境界"], [r"v\leftarrow\beta v+(1-\beta)g^2", r"\eta\leftarrow\mathrm{hard}(\eta)"], r"\eta\leftarrow\mathrm{hard}(\mathrm{clip}(\eta))"),
    (1667, "LookaheadSoftHard", "1667_lookaheadsofthard", "LookaheadSoftHard", "665_linear_131", "opt",
     ["Lookahead軟硬", "外側平均", "二段"], ["軟", "硬"], [r"u\leftarrow\mathrm{soft}(u)", r"u\leftarrow\mathrm{hard}(u)"], r"u\leftarrow\mathrm{hard}(\mathrm{soft}(u))"),
    (1668, "垂心フォイエルバッハ比", "1668_h_feuerbach_ratio", "HFeuerbachRatio", "666_geometry_131", "tri",
     ["垂心とフォイエルバッハ", "九点円", "比"], ["配置", "比"], [r"H", r"HN/R"], r"HN/R"),
    (1669, "重心フォイエルバッハ比", "1669_g_feuerbach_ratio", "GFeuerbachRatio", "666_geometry_131", "tri",
     ["重心とフォイエルバッハ", "九点円", "比"], ["配置", "比"], [r"G", r"GN/\ell"], r"GN/\ell"),
    (1670, "九点フォイエルバッハ比", "1670_n_feuerbach_ratio", "NFeuerbachRatio", "666_geometry_131", "tri",
     ["九点円フォイエルバッハ", "接点", "比"], ["配置", "比"], [r"N", r"R_N=R/2"], r"R_N=R/2"),
    (1671, "一様チャイニング", "1671_uniform_chaining", "UniformChaining", "667_probability_129", "pts",
     ["一様チェイニング", "全空間階層", "上界"], ["構成", "上界"], [r"\gamma_{2,u}", r"\mathbb{E}\sup X\le C\gamma_{2,u}"], r"\mathbb{E}\sup X\le C\gamma_{2,u}"),
    (1672, "スケールエントロピー", "1672_scale_entropy", "ScaleEntropy", "667_probability_129", "pts",
     ["スケールエントロピー", "半径依存", "対数"], ["定義", "依存"], [r"H_r(\epsilon)", r"H_r(\epsilon)\propto r^{\alpha}"], r"H_r(\epsilon)\propto r^{\alpha}"),
    (1673, "二分木細分", "1673_binary_tree_refine", "BinaryTreeRefine", "668_combinatorics_128", "nums",
     ["二分木", "左右", "細分"], ["定義", "細分"], [r"B_n", r"B(n,k)"], r"B(n,k)", [1, 1, 2, 5, 14]),
    (1674, "ログ半安定対", "1674_log_semistable_pair", "LogSemistablePair", "669_analysis_132", "box",
     ["ログ半安定", "簡約ファイバー", "平坦"], ["定義", "条件"], [r"(X,D)/S", r"(X_s,D_s)"], r"(X_s,D_s)"),
    (1675, "相対ログ安定対", "1675_rel_log_stable_pair", "RelLogStablePair", "669_analysis_132", "box",
     ["相対ログ安定", "相対豊富", "平坦族"], ["定義", "条件"], [r"K_X+D", r"(K_X+D)/S"], r"(K_X+D)/S"),
    (1676, "ログ簡約対", "1676_log_slc_pair", "LogSlcPair", "669_analysis_132", "box",
     ["ログ簡約", "半対数標準", "食い違い"], ["定義", "判定"], [r"a(E,X,D)", r"a(E,X,D)\ge -1"], r"a(E,X,D)\ge -1"),
    (1677, "SAMBoundHard", "1677_samboundhard", "SAMBoundHard", "670_linear_132", "opt",
     ["SAM境界硬閾", "鋭度", "剪定"], ["核", "硬境界"], [r"\epsilon\leftarrow\rho g/\|g\|", r"\rho\leftarrow\mathrm{hard}(\rho)"], r"\rho\leftarrow\mathrm{hard}(\mathrm{clip}(\rho))"),
    (1678, "ProdigyBoundHard", "1678_prodigyboundhard", "ProdigyBoundHard", "670_linear_132", "opt",
     ["Prodigy境界硬閾", "D推定", "剪定"], ["核", "硬境界"], [r"d\leftarrow\|g\|", r"\eta\leftarrow\mathrm{hard}(\eta)"], r"\eta\leftarrow\mathrm{hard}(\mathrm{clip}(\eta))"),
    (1679, "MuonWSoftClip", "1679_muonwsoftclip", "MuonWSoftClip", "670_linear_132", "opt",
     ["MuonW軟クリップ", "減衰直交", "二重"], ["核", "軟クリップ"], [r"U^\top U=I", r"U\leftarrow\mathrm{clip}(\mathrm{soft}(U))"], r"U\leftarrow\mathrm{clip}(\mathrm{soft}(U))"),
    (1680, "内心フォイエル接点比", "1680_in_feuerbach_touch", "InFeuerbachTouch", "671_geometry_132", "tri",
     ["内心接点比", "九点円", "比"], ["配置", "比"], [r"I", r"IT/r"], r"IT/r"),
    (1681, "傍心フォイエル接点比", "1681_ex_feuerbach_touch", "ExFeuerbachTouch", "671_geometry_132", "tri",
     ["傍心接点比", "九点円", "比"], ["配置", "比"], [r"I_a", r"I_aT/r_a"], r"I_aT/r_a"),
    (1682, "外心フォイエル接点比", "1682_o_feuerbach_touch", "OFeuerbachTouch", "671_geometry_132", "tri",
     ["外心接点比", "九点円", "比"], ["配置", "比"], [r"O", r"OT/R"], r"OT/R"),
    (1683, "半径敏感度", "1683_radius_sensitivity", "RadiusSensitivity", "672_probability_130", "pts",
     ["半径敏感度", "局所複雑度", "傾き"], ["定義", "傾き"], [r"\phi'(r)", r"\phi'(r)\propto r^{\alpha-1}"], r"\phi'(r)\propto r^{\alpha-1}"),
    (1684, "標本依存複雑度", "1684_sample_complexity", "SampleComplexity", "672_probability_130", "pts",
     ["標本依存複雑度", "データ依存", "上界"], ["定義", "上界"], [r"\mathfrak{C}_n", r"\mathfrak{C}_n\le C/\sqrt n"], r"\mathfrak{C}_n\le C/\sqrt n"),
    (1685, "順序木細分", "1685_ordered_tree_refine", "OrderedTreeRefine", "673_combinatorics_129", "nums",
     ["順序木", "平面順序", "細分"], ["定義", "細分"], [r"O_n", r"O(n,k)"], r"O(n,k)", [1, 1, 3, 11, 45]),
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
        path = f"project/math/{season}/{slug}/scene.py"
        code = mk(kind, cls, num, title, notes, dnotes, dtex, final, vals)
        folder = ROOT / "project/math" / season / slug
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "scene.py").write_text(code, encoding="utf-8")
        (folder / "storyboard.md").write_text(story(num, title), encoding="utf-8")
        ast.parse(code)
        created.append((num, title, path, cls))
        titles.add(title)

    cp = ROOT / "project/math/catalog.py"
    text = cp.read_text(encoding="utf-8")
    assert "VIDEOS_1650_1661" not in text

    def block(name, items):
        lines = [f"\n\n{name}: tuple[Video, ...] = ("]
        for num, title, path, cls in items:
            lines.append(f'    Video({num}, "{title}", "{path}", "{cls}"),')
        lines.append(")")
        return "\n".join(lines)

    cp.write_text(
        text.rstrip()
        + block("VIDEOS_1650_1661", created[:12])
        + block("VIDEOS_1662_1673", created[12:24])
        + block("VIDEOS_1674_1685", created[24:])
        + "\n",
        encoding="utf-8",
    )

    tp = ROOT / "tests/test_catalog.py"
    t = tp.read_text(encoding="utf-8")
    if "VIDEOS_1650_1661" not in t:
        t = t.replace(
            "VIDEOS_1638_1649 = _catalog.VIDEOS_1638_1649\n",
            "VIDEOS_1638_1649 = _catalog.VIDEOS_1638_1649\n"
            "VIDEOS_1650_1661 = _catalog.VIDEOS_1650_1661\n"
            "VIDEOS_1662_1673 = _catalog.VIDEOS_1662_1673\n"
            "VIDEOS_1674_1685 = _catalog.VIDEOS_1674_1685\n",
        )
        insert = """
    def test_numbers_are_1650_to_1661(self):
        nums = [v.number for v in VIDEOS_1650_1661]
        self.assertEqual(nums, list(range(1650, 1662)))


    def test_numbers_are_1662_to_1673(self):
        nums = [v.number for v in VIDEOS_1662_1673]
        self.assertEqual(nums, list(range(1662, 1674)))


    def test_numbers_are_1674_to_1685(self):
        nums = [v.number for v in VIDEOS_1674_1685]
        self.assertEqual(nums, list(range(1674, 1686)))

"""
        t = t.replace(
            "    def test_each_scene_file_defines_the_class(self):",
            insert + "    def test_each_scene_file_defines_the_class(self):",
        )
        t = t.replace(
            "            *VIDEOS_1638_1649,\n        ):",
            "            *VIDEOS_1638_1649,\n"
            "            *VIDEOS_1650_1661,\n"
            "            *VIDEOS_1662_1673,\n"
            "            *VIDEOS_1674_1685,\n"
            "        ):",
        )
        tp.write_text(t, encoding="utf-8")

    plan = ROOT / "project/math/PLAN.md"
    p = plan.read_text(encoding="utf-8")
    if "#1650" not in p:
        extra = "\n\n## 導出つき続き（#1650–#1661）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[:12]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#1662–#1673）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[12:24]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#1674–#1685）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[24:]:
            extra += f"| {num} | {title} | 実装 |\n"
        p = p.replace("## 1 本の作業フロー", extra + "\n## 1 本の作業フロー")
        plan.write_text(p, encoding="utf-8")

    print("created", created[0][0], "-", created[-1][0])


if __name__ == "__main__":
    main()
