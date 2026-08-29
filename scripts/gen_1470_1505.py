#!/usr/bin/env python3
"""Generate #1470–#1505 with derive/proof beats."""
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
    # 1470-1481
    (1470, "相対豊富対", "1470_rel_ample_pair", "RelAmplePair", "584_analysis_115", "box",
     ["相対豊富", "ファイバー正", "埋め込み"], ["定義", "判定"], [r"L-(K+D)", r"(L-(K+D))|_F>0"], r"(L-(K+D))|_F>0"),
    (1471, "相対ネフ対", "1471_rel_nef_pair", "RelNefPair", "584_analysis_115", "box",
     ["相対ネフ", "曲線交差", "ファイバー"], ["定義", "判定"], [r"(L.C)", r"(L.C)\ge 0"], r"(L.C)\ge 0"),
    (1472, "相対ビッグ対", "1472_rel_big_pair", "RelBigPair", "584_analysis_115", "box",
     ["相対ビッグ", "相対体積", "開錐"], ["体積", "判定"], [r"vol_{X/S}(L)", r"vol_{X/S}(L)>0"], r"vol_{X/S}(L)>0"),
    (1473, "NAdamSoftClip", "1473_nadamsoftclip", "NAdamSoftClip", "585_linear_115", "opt",
     ["NAdam軟クリップ", "ネステロフ", "二重制限"], ["核", "軟クリップ"], [r"m\leftarrow\beta m+(1-\beta)g", r"\theta\leftarrow\theta-\mathrm{clip}(\mathrm{soft}(\hat m))"], r"\theta\leftarrow\theta-\mathrm{clip}(\mathrm{soft}(\hat m))"),
    (1474, "NAdamHardClip", "1474_nadamhardclip", "NAdamHardClip", "585_linear_115", "opt",
     ["NAdam硬クリップ", "ネステロフ", "硬閾値"], ["核", "硬クリップ"], [r"m\leftarrow\beta m+(1-\beta)g", r"\theta\leftarrow\theta-\mathrm{hard}(\mathrm{clip}(\hat m))"], r"\theta\leftarrow\theta-\mathrm{hard}(\mathrm{clip}(\hat m))"),
    (1475, "NAdamSoftHard", "1475_nadamsofthard", "NAdamSoftHard", "585_linear_115", "opt",
     ["NAdam軟硬", "二段閾値", "更新"], ["軟", "硬"], [r"u\leftarrow\mathrm{soft}(\hat m)", r"u\leftarrow\mathrm{hard}(u)"], r"u\leftarrow\mathrm{hard}(\mathrm{soft}(\hat m))"),
    (1476, "内心類似中線比", "1476_in_symmedian_ratio", "InSymmedianRatio", "586_geometry_115", "tri",
     ["内心と類似中線", "角条件", "比"], ["配置", "比"], [r"I", r"\ell_s/\ell"], r"\ell_s/\ell"),
    (1477, "傍心類似中線比", "1477_ex_symmedian_ratio", "ExSymmedianRatio", "586_geometry_115", "tri",
     ["傍心と類似中線", "外角", "比"], ["配置", "比"], [r"I_a", r"\ell_s/\ell'"], r"\ell_s/\ell'"),
    (1478, "外心類似中線比", "1478_o_symmedian_ratio", "OSymmedianRatio", "586_geometry_115", "tri",
     ["外心と類似中線", "円周角", "比"], ["配置", "比"], [r"O", r"\ell_s/R"], r"\ell_s/R"),
    (1479, "ラデマッハ再訪", "1479_rademacher_revisit", "RademacherRevisit", "587_probability_113", "pts",
     ["ラデマッハ", "符号平均", "複雑度"], ["定義", "上界"], [r"\mathfrak{R}_n", r"\mathfrak{R}_n(\mathcal{F})\le C/\sqrt n"], r"\mathfrak{R}_n(\mathcal{F})\le C/\sqrt n"),
    (1480, "ガウス複雑度", "1480_gaussian_complexity", "GaussianComplexity", "587_probability_113", "pts",
     ["ガウス複雑度", "正規平均", "比較"], ["定義", "関係"], [r"G(\mathcal{F})", r"G(\mathcal{F})\asymp\mathfrak{R}(\mathcal{F})"], r"G(\mathcal{F})\asymp\mathfrak{R}(\mathcal{F})"),
    (1481, "ラグランジュ細分", "1481_lagrange_refine", "LagrangeRefine", "588_combinatorics_112", "nums",
     ["ラグランジュ数", "木の数え上げ", "細分"], ["定義", "細分"], [r"L_n", r"L(n,k)"], r"L(n,k)", [1, 1, 4, 26, 236]),
    # 1482-1493
    (1482, "純端末対", "1482_plt_pair", "PltPair", "589_analysis_116", "box",
     ["純端末対", "食い違い", "境界"], ["定義", "判定"], [r"a(E,X,D)", r"a(E,X,D)\ge -1"], r"a(E,X,D)\ge -1"),
    (1483, "純標準対", "1483_klt_pair", "KltPair", "589_analysis_116", "box",
     ["純標準対", "食い違い", "開条件"], ["定義", "判定"], [r"a(E,X,D)", r"a(E,X,D)>-1"], r"a(E,X,D)>-1"),
    (1484, "カノニカル対", "1484_canonical_pair", "CanonicalPair", "589_analysis_116", "box",
     ["カノニカル対", "食い違い非負", "閉条件"], ["定義", "判定"], [r"a(E,X,D)", r"a(E,X,D)\ge 0"], r"a(E,X,D)\ge 0"),
    (1485, "LARSSoftClip", "1485_larssoftclip", "LARSSoftClip", "590_linear_116", "opt",
     ["LARS軟クリップ", "層正規化", "二重"], ["核", "軟クリップ"], [r"\eta\leftarrow\|w\|/\|g\|", r"\eta\leftarrow\mathrm{clip}(\mathrm{soft}(\eta))"], r"\eta\leftarrow\mathrm{clip}(\mathrm{soft}(\eta))"),
    (1486, "LARSHardClip", "1486_larshardclip", "LARSHardClip", "590_linear_116", "opt",
     ["LARS硬クリップ", "層正規化", "硬閾"], ["核", "硬クリップ"], [r"\eta\leftarrow\|w\|/\|g\|", r"\eta\leftarrow\mathrm{hard}(\mathrm{clip}(\eta))"], r"\eta\leftarrow\mathrm{hard}(\mathrm{clip}(\eta))"),
    (1487, "LAMBSoftClip", "1487_lambsoftclip", "LAMBSoftClip", "590_linear_116", "opt",
     ["LAMB軟クリップ", "層信頼域", "二重"], ["核", "軟クリップ"], [r"r\leftarrow\|w\|/\|\hat u\|", r"r\leftarrow\mathrm{clip}(\mathrm{soft}(r))"], r"r\leftarrow\mathrm{clip}(\mathrm{soft}(r))"),
    (1488, "垂心類似中線比", "1488_h_symmedian_ratio", "HSymmedianRatio", "591_geometry_116", "tri",
     ["垂心と類似中線", "直交", "比"], ["配置", "比"], [r"H", r"\ell_s/\ell_H"], r"\ell_s/\ell_H"),
    (1489, "重心類似中線比", "1489_g_symmedian_ratio", "GSymmedianRatio", "591_geometry_116", "tri",
     ["重心と類似中線", "中線近傍", "比"], ["配置", "比"], [r"G", r"\ell_s/\ell_G"], r"\ell_s/\ell_G"),
    (1490, "九点類似中線比", "1490_n_symmedian_ratio", "NSymmedianRatio", "591_geometry_116", "tri",
     ["九点円と類似中線", "中点", "比"], ["配置", "比"], [r"N", r"\ell_s/\ell_N"], r"\ell_s/\ell_N"),
    (1491, "ダドリー積分", "1491_dudley_integral", "DudleyIntegral", "592_probability_114", "pts",
     ["ダドリー積分", "被覆積分", "上界"], ["定義", "上界"], [r"\int_0^\infty\sqrt{\log N(\epsilon)}\,d\epsilon", r"\mathbb{E}\sup X\le C\int\sqrt{\log N}"], r"\mathbb{E}\sup X\le C\int\sqrt{\log N}"),
    (1492, "経験被覆数", "1492_empirical_covering", "EmpiricalCovering", "592_probability_114", "pts",
     ["経験被覆", "データ依存", "サイズ"], ["定義", "サイズ"], [r"N_n(\epsilon)", r"N_n(\epsilon)\le N(\epsilon)"], r"N_n(\epsilon)\le N(\epsilon)"),
    (1493, "ナーラヤナ細分", "1493_narayana_refine", "NarayanaRefine", "593_combinatorics_113", "nums",
     ["ナーラヤナ", "カタラン細分", "峰数"], ["定義", "細分"], [r"N(n,k)", r"C_n=\sum_k N(n,k)"], r"N(n,k)", [1, 1, 3, 6, 15]),
    # 1494-1505
    (1494, "フリップ対", "1494_flip_pair", "FlipPair", "594_analysis_117", "box",
     ["フリップ対", "小収縮", "双有理"], ["定義", "変換"], [r"\phi^-", r"\phi^+:X^+\to Z"], r"X\dashrightarrow X^+"),
    (1495, "フロップ対", "1495_flop_pair", "FlopPair", "594_analysis_117", "box",
     ["フロップ対", "K自明", "双有理"], ["定義", "変換"], [r"K_X\cdot C=0", r"X\dashrightarrow X'"], r"X\dashrightarrow X'"),
    (1496, "収縮対", "1496_contraction_pair", "ContractionPair", "594_analysis_117", "box",
     ["収縮対", "極小モデル", "射"], ["定義", "射"], [r"\phi:X\to Y", r"\rho(X/Y)=1"], r"\rho(X/Y)=1"),
    (1497, "ApolloSoft", "1497_apollosoft", "ApolloSoft", "595_linear_117", "opt",
     ["Apollo軟閾", "準ニュートン", "平滑"], ["核", "軟閾"], [r"B\leftarrow B+uu^\top", r"u\leftarrow\mathrm{soft}(u)"], r"u\leftarrow\mathrm{soft}(u)"),
    (1498, "ApolloHard", "1498_apollohard", "ApolloHard", "595_linear_117", "opt",
     ["Apollo硬閾", "準ニュートン", "剪定"], ["核", "硬閾"], [r"B\leftarrow B+uu^\top", r"u\leftarrow\mathrm{hard}(u)"], r"u\leftarrow\mathrm{hard}(u)"),
    (1499, "ApolloClip", "1499_apolloclip", "ApolloClip", "595_linear_117", "opt",
     ["Apolloクリップ", "準ニュートン", "制限"], ["核", "クリップ"], [r"B\leftarrow B+uu^\top", r"u\leftarrow\mathrm{clip}(u)"], r"u\leftarrow\mathrm{clip}(u)"),
    (1500, "内心傍接円比", "1500_in_excircle_ratio", "InExcircleRatio", "596_geometry_117", "tri",
     ["内心と傍接円", "半径", "比"], ["配置", "比"], [r"r", r"r/r_a"], r"r/r_a"),
    (1501, "傍心傍接円比", "1501_ex_excircle_ratio", "ExExcircleRatio", "596_geometry_117", "tri",
     ["傍心と傍接円", "半径", "比"], ["配置", "比"], [r"r_a", r"r_a/r_b"], r"r_a/r_b"),
    (1502, "外心傍接円比", "1502_o_excircle_ratio", "OExcircleRatio", "596_geometry_117", "tri",
     ["外心と傍接円", "外接半径", "比"], ["配置", "比"], [r"R", r"R/r_a"], r"R/r_a"),
    (1503, "局所被覆数", "1503_local_covering", "LocalCovering", "597_probability_115", "pts",
     ["局所被覆", "半径球", "サイズ"], ["定義", "サイズ"], [r"N(B(f,r),\epsilon)", r"N_{\mathrm{loc}}(\epsilon)"], r"N_{\mathrm{loc}}(\epsilon)"),
    (1504, "一様エントロピー", "1504_uniform_entropy", "UniformEntropy", "597_probability_115", "pts",
     ["一様エントロピー", "対数被覆", "積分"], ["定義", "積分"], [r"H(\epsilon)", r"\int\sqrt{H(\epsilon)}\,d\epsilon"], r"\int\sqrt{H(\epsilon)}\,d\epsilon"),
    (1505, "フィボナッチ細分", "1505_fibonacci_refine", "FibonacciRefine", "598_combinatorics_114", "nums",
     ["フィボナッチ", "漸化式", "細分"], ["定義", "細分"], [r"F_n=F_{n-1}+F_{n-2}", r"F(n,k)"], r"F(n,k)", [1, 1, 2, 3, 5]),
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
    assert "VIDEOS_1470_1481" not in text

    def block(name, items):
        lines = [f"\n\n{name}: tuple[Video, ...] = ("]
        for num, title, path, cls in items:
            lines.append(f'    Video({num}, "{title}", "{path}", "{cls}"),')
        lines.append(")")
        return "\n".join(lines)

    cp.write_text(
        text.rstrip()
        + block("VIDEOS_1470_1481", created[:12])
        + block("VIDEOS_1482_1493", created[12:24])
        + block("VIDEOS_1494_1505", created[24:])
        + "\n",
        encoding="utf-8",
    )

    tp = ROOT / "tests/test_catalog.py"
    t = tp.read_text(encoding="utf-8")
    if "VIDEOS_1470_1481" not in t:
        t = t.replace(
            "VIDEOS_1458_1469 = _catalog.VIDEOS_1458_1469\n",
            "VIDEOS_1458_1469 = _catalog.VIDEOS_1458_1469\n"
            "VIDEOS_1470_1481 = _catalog.VIDEOS_1470_1481\n"
            "VIDEOS_1482_1493 = _catalog.VIDEOS_1482_1493\n"
            "VIDEOS_1494_1505 = _catalog.VIDEOS_1494_1505\n",
        )
        insert = """
    def test_numbers_are_1470_to_1481(self):
        nums = [v.number for v in VIDEOS_1470_1481]
        self.assertEqual(nums, list(range(1470, 1482)))


    def test_numbers_are_1482_to_1493(self):
        nums = [v.number for v in VIDEOS_1482_1493]
        self.assertEqual(nums, list(range(1482, 1494)))


    def test_numbers_are_1494_to_1505(self):
        nums = [v.number for v in VIDEOS_1494_1505]
        self.assertEqual(nums, list(range(1494, 1506)))

"""
        t = t.replace(
            "    def test_each_scene_file_defines_the_class(self):",
            insert + "    def test_each_scene_file_defines_the_class(self):",
        )
        t = t.replace(
            "            *VIDEOS_1458_1469,\n        ):",
            "            *VIDEOS_1458_1469,\n"
            "            *VIDEOS_1470_1481,\n"
            "            *VIDEOS_1482_1493,\n"
            "            *VIDEOS_1494_1505,\n"
            "        ):",
        )
        tp.write_text(t, encoding="utf-8")

    plan = ROOT / "project/math/PLAN.md"
    p = plan.read_text(encoding="utf-8")
    if "#1470" not in p:
        extra = "\n\n## 導出つき続き（#1470–#1481）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[:12]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#1482–#1493）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[12:24]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#1494–#1505）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[24:]:
            extra += f"| {num} | {title} | 実装 |\n"
        p = p.replace("## 1 本の作業フロー", extra + "\n## 1 本の作業フロー")
        plan.write_text(p, encoding="utf-8")

    print("created", created[0][0], "-", created[-1][0])


if __name__ == "__main__":
    main()
