#!/usr/bin/env python3
"""Generate #2010–#2045 with derive/proof beats."""
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
    (2010, "ログ随伴体積対", "2010_log_adj_vol", "LogAdjVol", "809_analysis_160", "box",
     ["ログ随伴体積", "体積関数", "境界"], ["定義", "性質"], [r"vol(K+D)", r"vol(K+D)"], r"vol(K+D)"),
    (2011, "相対ログ随伴体積対", "2011_rel_log_adj_vol", "RelLogAdjVol", "809_analysis_160", "box",
     ["相対ログ随伴体積", "相対体積", "ファイバー"], ["定義", "性質"], [r"vol_{X/S}(K+D)", r"vol_{X/S}(K+D)"], r"vol_{X/S}(K+D)"),
    (2012, "ログ随伴数値次元対", "2012_log_adj_num_dim", "LogAdjNumDim", "809_analysis_160", "box",
     ["ログ随伴数値次元", "成長率", "κ"], ["定義", "値"], [r"\kappa_\sigma(K+D)", r"\kappa_\sigma\in\{0,\ldots,n\}"], r"\kappa_\sigma(K+D)"),
    (2013, "RMSHardBoundClip", "2013_rmshardboundclip", "RMSHardBoundClip", "810_linear_160", "opt",
     ["RMS硬境界クリップ", "二乗平均", "三重"], ["核", "硬境界"], [r"v\leftarrow\beta v+(1-\beta)g^2", r"\eta\leftarrow\mathrm{clip}(\mathrm{hard}(\eta))"], r"\eta\leftarrow\mathrm{clip}(\mathrm{hard}(\eta))\in[L,U]"),
    (2014, "LookaheadSoftBoundClip", "2014_lookaheadsoftboundclip", "LookaheadSoftBoundClip", "810_linear_160", "opt",
     ["Lookahead軟境界クリップ", "外側平均", "三重"], ["核", "軟境界"], [r"x\leftarrow x+\alpha(y-x)", r"\eta\leftarrow\mathrm{clip}(\mathrm{soft}(\eta))"], r"\eta\leftarrow\mathrm{clip}(\mathrm{soft}(\eta))\in[L,U]"),
    (2015, "ProdigyHardBoundClip", "2015_prodigyhardboundclip", "ProdigyHardBoundClip", "810_linear_160", "opt",
     ["Prodigy硬境界クリップ", "D推定", "三重"], ["核", "硬境界"], [r"d\leftarrow\|g\|", r"\eta\leftarrow\mathrm{clip}(\mathrm{hard}(\eta))"], r"\eta\leftarrow\mathrm{clip}(\mathrm{hard}(\eta))\in[L,U]"),
    (2016, "内心類似九点弧比", "2016_in_sym_nine_arc", "InSymNineArc", "811_geometry_160", "tri",
     ["内心類似九点弧", "九点円弧", "比"], ["配置", "比"], [r"I", r"\ell_{a,s}/r"], r"\ell_{a,s}/r"),
    (2017, "傍心類似九点弧比", "2017_ex_sym_nine_arc", "ExSymNineArc", "811_geometry_160", "tri",
     ["傍心類似九点弧", "九点円弧", "比"], ["配置", "比"], [r"I_a", r"\ell_{a,s}/r_a"], r"\ell_{a,s}/r_a"),
    (2018, "外心類似九点弧比", "2018_o_sym_nine_arc", "OSymNineArc", "811_geometry_160", "tri",
     ["外心類似九点弧", "九点円弧", "比"], ["配置", "比"], [r"O", r"\ell_{a,s}/R"], r"\ell_{a,s}/R"),
    (2019, "局所データ半径被覆", "2019_local_data_radius_cov", "LocalDataRadiusCov", "812_probability_158", "pts",
     ["局所データ半径被覆", "データ球", "サイズ"], ["定義", "サイズ"], [r"N_n(B,r,\epsilon)", r"N_n\lesssim(r/\epsilon)^d"], r"N_n\lesssim(r/\epsilon)^d"),
    (2020, "局所データ半径パッキング", "2020_local_data_radius_pack", "LocalDataRadiusPack", "812_probability_158", "pts",
     ["局所データ半径パッキング", "データ球", "分離"], ["定義", "サイズ"], [r"M_n(B,r,\epsilon)", r"M_n\lesssim(r/\epsilon)^d"], r"M_n\lesssim(r/\epsilon)^d"),
    (2021, "根つき増加森細分", "2021_rooted_inc_forest", "RootedIncForest", "813_combinatorics_157", "nums",
     ["根つき増加森", "根と増加", "細分"], ["定義", "細分"], [r"RIF_n", r"RIF(n,k)"], r"RIF(n,k)", [1, 2, 7, 38, 291]),
    (2022, "相対ログ随伴数値次元対", "2022_rel_log_adj_num_dim", "RelLogAdjNumDim", "814_analysis_161", "box",
     ["相対ログ随伴数値次元", "相対成長", "κ"], ["定義", "値"], [r"\kappa_\sigma(X/S,K+D)", r"\kappa_\sigma"], r"\kappa_\sigma(X/S,K+D)"),
    (2023, "ログ随伴飯高対", "2023_log_adj_iitaka", "LogAdjIitaka", "814_analysis_161", "box",
     ["ログ随伴飯高", "線形系像", "κ"], ["写像", "次元"], [r"\phi_{|m(K+D)|}", r"\kappa(X,K+D)"], r"\kappa(X,K+D)"),
    (2024, "相対ログ随伴飯高対", "2024_rel_log_adj_iitaka", "RelLogAdjIitaka", "814_analysis_161", "box",
     ["相対ログ随伴飯高", "相対線形系", "κ"], ["写像", "次元"], [r"\phi/S", r"\kappa(X/S,K+D)"], r"\kappa(X/S,K+D)"),
    (2025, "ScheduleFreeHardBoundClip", "2025_schedulefreehardboundclip", "ScheduleFreeHardBoundClip", "815_linear_161", "opt",
     ["平均化硬境界クリップ", "スケジュール不要", "三重"], ["核", "硬境界"], [r"z\leftarrow(1-c)z+cx", r"\eta\leftarrow\mathrm{clip}(\mathrm{hard}(\eta))"], r"\eta\leftarrow\mathrm{clip}(\mathrm{hard}(\eta))\in[L,U]"),
    (2026, "AdamWHardBoundClip", "2026_adamwhardboundclip", "AdamWHardBoundClip", "815_linear_161", "opt",
     ["AdamW硬境界クリップ", "減衰つき", "三重"], ["核", "硬境界"], [r"u\leftarrow\hat m/\sqrt{\hat v}", r"\eta\leftarrow\mathrm{clip}(\mathrm{hard}(\eta))"], r"\eta\leftarrow\mathrm{clip}(\mathrm{hard}(\eta))\in[L,U]"),
    (2027, "LionSoftBoundHard", "2027_lionsoftboundhard", "LionSoftBoundHard", "815_linear_161", "opt",
     ["Lion軟境界硬", "符号更新", "枠二段"], ["軟", "硬"], [r"\eta\leftarrow\mathrm{soft}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{soft}(\mathrm{clip}(\eta)))"),
    (2028, "垂心類似九点弧比", "2028_h_sym_nine_arc", "HSymNineArc", "816_geometry_161", "tri",
     ["垂心類似九点弧", "九点円弧", "比"], ["配置", "比"], [r"H", r"\ell_{a,s}/R"], r"\ell_{a,s}/R"),
    (2029, "重心類似九点弧比", "2029_g_sym_nine_arc", "GSymNineArc", "816_geometry_161", "tri",
     ["重心類似九点弧", "九点円弧", "比"], ["配置", "比"], [r"G", r"\ell_{a,s}/\ell"], r"\ell_{a,s}/\ell"),
    (2030, "九点類似弧比", "2030_n_sym_nine_arc", "NSymNineArc", "816_geometry_161", "tri",
     ["九点類似弧", "弧", "比"], ["配置", "比"], [r"N", r"\ell_{a,s}/R_N"], r"\ell_{a,s}/R_N"),
    (2031, "経験局所スケール被覆", "2031_emp_local_scale_cov", "EmpLocalScaleCov", "817_probability_159", "pts",
     ["経験局所スケール被覆", "データ局所", "サイズ"], ["定義", "サイズ"], [r"N_n(B,r,\epsilon)", r"N_n\lesssim(r/\epsilon)^d"], r"N_n\lesssim(r/\epsilon)^d"),
    (2032, "経験局所スケールパッキング", "2032_emp_local_scale_pack", "EmpLocalScalePack", "817_probability_159", "pts",
     ["経験局所スケールパッキング", "データ局所", "分離"], ["定義", "サイズ"], [r"M_n(B,r,\epsilon)", r"M_n\lesssim(r/\epsilon)^d"], r"M_n\lesssim(r/\epsilon)^d"),
    (2033, "ラベル増加木細分", "2033_labeled_inc_tree", "LabeledIncTree", "818_combinatorics_158", "nums",
     ["ラベル増加木", "増加ラベル", "細分"], ["定義", "細分"], [r"LI_n", r"LI(n,k)"], r"LI(n,k)", [1, 1, 3, 13, 71]),
    (2034, "ログ随伴フリップ対", "2034_log_adj_flip", "LogAdjFlip", "819_analysis_162", "box",
     ["ログ随伴フリップ", "小収縮", "双有理"], ["定義", "変換"], [r"\phi^-", r"X\dashrightarrow X^+"], r"X\dashrightarrow X^+"),
    (2035, "相対ログ随伴フリップ対", "2035_rel_log_adj_flip", "RelLogAdjFlip", "819_analysis_162", "box",
     ["相対ログ随伴フリップ", "相対小収縮", "ファイバー"], ["定義", "変換"], [r"\phi^-/S", r"X\dashrightarrow_S X^+"], r"X\dashrightarrow_S X^+"),
    (2036, "ログ随伴フロップ対", "2036_log_adj_flop", "LogAdjFlop", "819_analysis_162", "box",
     ["ログ随伴フロップ", "K自明", "双有理"], ["定義", "変換"], [r"(K+D)\cdot C=0", r"X\dashrightarrow X'"], r"X\dashrightarrow X'"),
    (2037, "SophiaSoftBoundHard", "2037_sophiasoftboundhard", "SophiaSoftBoundHard", "820_linear_162", "opt",
     ["Sophia軟境界硬", "二階情報", "枠二段"], ["軟", "硬"], [r"\eta\leftarrow\mathrm{soft}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{soft}(\mathrm{clip}(\eta)))"),
    (2038, "ApolloHardBoundClip", "2038_apollohardboundclip", "ApolloHardBoundClip", "820_linear_162", "opt",
     ["Apollo硬境界クリップ", "準ニュートン", "三重"], ["核", "硬境界"], [r"B\leftarrow B+uu^\top", r"\eta\leftarrow\mathrm{clip}(\mathrm{hard}(\eta))"], r"\eta\leftarrow\mathrm{clip}(\mathrm{hard}(\eta))\in[L,U]"),
    (2039, "MuonSoftBoundHard", "2039_muonsoftboundhard", "MuonSoftBoundHard", "820_linear_162", "opt",
     ["Muon軟境界硬", "直交更新", "枠二段"], ["軟", "硬"], [r"\eta\leftarrow\mathrm{soft}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{soft}(\mathrm{clip}(\eta)))"),
    (2040, "内心九点中心弦比", "2040_in_nine_center_chord", "InNineCenterChord", "821_geometry_162", "tri",
     ["内心九点中心弦", "中心と弦", "比"], ["配置", "比"], [r"I", r"IN/\ell_9"], r"IN/\ell_9"),
    (2041, "傍心九点中心弦比", "2041_ex_nine_center_chord", "ExNineCenterChord", "821_geometry_162", "tri",
     ["傍心九点中心弦", "中心と弦", "比"], ["配置", "比"], [r"I_a", r"I_aN/\ell_9"], r"I_aN/\ell_9"),
    (2042, "外心九点中心弦比", "2042_o_nine_center_chord", "ONineCenterChord", "821_geometry_162", "tri",
     ["外心九点中心弦", "中心と弦", "比"], ["配置", "比"], [r"O", r"ON/\ell_9"], r"ON/\ell_9"),
    (2043, "一様データ半径被覆", "2043_unif_data_radius_cov", "UnifDataRadiusCov", "822_probability_160", "pts",
     ["一様データ半径被覆", "一様データ", "サイズ"], ["定義", "サイズ"], [r"N_{n,u}(r,\epsilon)", r"N_{n,u}\lesssim(r/\epsilon)^d"], r"N_{n,u}\lesssim(r/\epsilon)^d"),
    (2044, "一様データ半径パッキング", "2044_unif_data_radius_pack", "UnifDataRadiusPack", "822_probability_160", "pts",
     ["一様データ半径パッキング", "一様データ", "分離"], ["定義", "サイズ"], [r"M_{n,u}(r,\epsilon)", r"M_{n,u}\lesssim(r/\epsilon)^d"], r"M_{n,u}\lesssim(r/\epsilon)^d"),
    (2045, "三分増加木細分", "2045_ternary_inc_tree", "TernaryIncTree", "823_combinatorics_159", "nums",
     ["三分増加木", "三分岐増加", "細分"], ["定義", "細分"], [r"TI_n", r"TI(n,k)"], r"TI(n,k)", [1, 1, 3, 12, 55]),
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
    assert "VIDEOS_2010_2021" not in text

    def block(name, items):
        lines = [f"\n\n{name}: tuple[Video, ...] = ("]
        for num, title, path, cls in items:
            lines.append(f'    Video({num}, "{title}", "{path}", "{cls}"),')
        lines.append(")")
        return "\n".join(lines)

    cp.write_text(
        text.rstrip()
        + block("VIDEOS_2010_2021", created[:12])
        + block("VIDEOS_2022_2033", created[12:24])
        + block("VIDEOS_2034_2045", created[24:])
        + "\n",
        encoding="utf-8",
    )

    tp = ROOT / "tests/test_catalog.py"
    t = tp.read_text(encoding="utf-8")
    if "VIDEOS_2010_2021" not in t:
        t = t.replace(
            "VIDEOS_1998_2009 = _catalog.VIDEOS_1998_2009\n",
            "VIDEOS_1998_2009 = _catalog.VIDEOS_1998_2009\n"
            "VIDEOS_2010_2021 = _catalog.VIDEOS_2010_2021\n"
            "VIDEOS_2022_2033 = _catalog.VIDEOS_2022_2033\n"
            "VIDEOS_2034_2045 = _catalog.VIDEOS_2034_2045\n",
        )
        insert = """
    def test_numbers_are_2010_to_2021(self):
        nums = [v.number for v in VIDEOS_2010_2021]
        self.assertEqual(nums, list(range(2010, 2022)))


    def test_numbers_are_2022_to_2033(self):
        nums = [v.number for v in VIDEOS_2022_2033]
        self.assertEqual(nums, list(range(2022, 2034)))


    def test_numbers_are_2034_to_2045(self):
        nums = [v.number for v in VIDEOS_2034_2045]
        self.assertEqual(nums, list(range(2034, 2046)))

"""
        t = t.replace(
            "    def test_each_scene_file_defines_the_class(self):",
            insert + "    def test_each_scene_file_defines_the_class(self):",
        )
        t = t.replace(
            "            *VIDEOS_1998_2009,\n        ):",
            "            *VIDEOS_1998_2009,\n"
            "            *VIDEOS_2010_2021,\n"
            "            *VIDEOS_2022_2033,\n"
            "            *VIDEOS_2034_2045,\n"
            "        ):",
        )
        tp.write_text(t, encoding="utf-8")

    plan = ROOT / "project/math/PLAN.md"
    p = plan.read_text(encoding="utf-8")
    if "#2010" not in p:
        extra = "\n\n## 導出つき続き（#2010–#2021）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[:12]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#2022–#2033）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[12:24]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#2034–#2045）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[24:]:
            extra += f"| {num} | {title} | 実装 |\n"
        p = p.replace("## 1 本の作業フロー", extra + "\n## 1 本の作業フロー")
        plan.write_text(p, encoding="utf-8")

    print("created", created[0][0], "-", created[-1][0])


if __name__ == "__main__":
    main()
