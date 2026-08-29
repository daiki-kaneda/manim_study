#!/usr/bin/env python3
"""Generate #2082–#2117 with derive/proof beats."""
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
    (2082, "ログ随伴標準対", "2082_log_adj_canonical", "LogAdjCanonical", "839_analysis_166", "box",
     ["ログ随伴標準", "標準モデル", "対"], ["定義", "条件"], [r"K+D\ \mathrm{nef}", r"(X,D)\ \mathrm{canonical}"], r"(X,D)\ \mathrm{canonical}"),
    (2083, "相対ログ随伴標準対", "2083_rel_log_adj_canonical", "RelLogAdjCanonical", "839_analysis_166", "box",
     ["相対ログ随伴標準", "相対標準", "ファイバー"], ["定義", "条件"], [r"K+D\ \mathrm{nef}/S", r"(X/S,D)\ \mathrm{canonical}"], r"(X/S,D)\ \mathrm{canonical}"),
    (2084, "ログ随伴正則対", "2084_log_adj_regular", "LogAdjRegular", "839_analysis_166", "box",
     ["ログ随伴正則", "正則モデル", "対"], ["定義", "条件"], [r"a(E,X,D)\ge 0", r"(X,D)\ \mathrm{regular}"], r"(X,D)\ \mathrm{regular}"),
    (2085, "RMSClipHardBound", "2085_rmscliphardbound", "RMSClipHardBound", "840_linear_166", "opt",
     ["RMSクリップ硬境界", "二乗平均", "枠二段"], ["クリップ", "硬"], [r"\eta\leftarrow\mathrm{clip}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{clip}(\eta))\in[L,U]"),
    (2086, "LookaheadSoftBoundHard", "2086_lookaheadsoftboundhard", "LookaheadSoftBoundHard", "840_linear_166", "opt",
     ["Lookahead軟境界硬", "外側平均", "枠二段"], ["軟", "硬"], [r"\eta\leftarrow\mathrm{soft}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{soft}(\mathrm{clip}(\eta)))"),
    (2087, "ProdigyHardSoftBound", "2087_prodigyhardsoftbound", "ProdigyHardSoftBound", "840_linear_166", "opt",
     ["Prodigy硬軟境界", "D推定", "枠二段"], ["硬", "軟"], [r"\eta\leftarrow\mathrm{hard}(\eta)", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{hard}(\mathrm{clip}(\eta)))"),
    (2088, "内心九点弧弦比", "2088_in_nine_arc_chord", "InNineArcChord", "841_geometry_166", "tri",
     ["内心九点弧弦", "弧と弦", "比"], ["配置", "比"], [r"I", r"\widehat{\ell}/\ell_9"], r"\widehat{\ell}/\ell_9"),
    (2089, "傍心九点弧弦比", "2089_ex_nine_arc_chord", "ExNineArcChord", "841_geometry_166", "tri",
     ["傍心九点弧弦", "弧と弦", "比"], ["配置", "比"], [r"I_a", r"\widehat{\ell}/\ell_9"], r"\widehat{\ell}/\ell_9"),
    (2090, "外心九点弧弦比", "2090_o_nine_arc_chord", "ONineArcChord", "841_geometry_166", "tri",
     ["外心九点弧弦", "弧と弦", "比"], ["配置", "比"], [r"O", r"\widehat{\ell}/\ell_9"], r"\widehat{\ell}/\ell_9"),
    (2091, "局所一様半径被覆", "2091_local_unif_radius_cov", "LocalUnifRadiusCov", "842_probability_164", "pts",
     ["局所一様半径被覆", "一様球", "サイズ"], ["定義", "サイズ"], [r"N_n^{u}(r,\epsilon)", r"N_n^{u}\lesssim(r/\epsilon)^d"], r"N_n^{u}\lesssim(r/\epsilon)^d"),
    (2092, "局所一様半径パッキング", "2092_local_unif_radius_pack", "LocalUnifRadiusPack", "842_probability_164", "pts",
     ["局所一様半径パッキング", "一様球", "分離"], ["定義", "サイズ"], [r"M_n^{u}(r,\epsilon)", r"M_n^{u}\lesssim(r/\epsilon)^d"], r"M_n^{u}\lesssim(r/\epsilon)^d"),
    (2093, "三分増加森細分", "2093_ternary_inc_forest", "TernaryIncForest", "843_combinatorics_163", "nums",
     ["三分増加森", "三分岐増加", "細分"], ["定義", "細分"], [r"TIF_n", r"TIF(n,k)"], r"TIF(n,k)", [1, 2, 7, 30, 143]),
    (2094, "相対ログ随伴正則対", "2094_rel_log_adj_regular", "RelLogAdjRegular", "844_analysis_167", "box",
     ["相対ログ随伴正則", "相対正則", "ファイバー"], ["定義", "条件"], [r"a(E,X/S,D)\ge 0", r"(X/S,D)\ \mathrm{regular}"], r"(X/S,D)\ \mathrm{regular}"),
    (2095, "ログ随伴平滑対", "2095_log_adj_smooth", "LogAdjSmooth", "844_analysis_167", "box",
     ["ログ随伴平滑", "平滑モデル", "対"], ["定義", "条件"], [r"a(E,X,D)>0", r"(X,D)\ \mathrm{smooth}"], r"(X,D)\ \mathrm{smooth}"),
    (2096, "相対ログ随伴平滑対", "2096_rel_log_adj_smooth", "RelLogAdjSmooth", "844_analysis_167", "box",
     ["相対ログ随伴平滑", "相対平滑", "ファイバー"], ["定義", "条件"], [r"a(E,X/S,D)>0", r"(X/S,D)\ \mathrm{smooth}"], r"(X/S,D)\ \mathrm{smooth}"),
    (2097, "ScheduleFreeHardSoftBound", "2097_schedulefreehardsoftbound", "ScheduleFreeHardSoftBound", "845_linear_167", "opt",
     ["平均化硬軟境界", "スケジュール不要", "枠二段"], ["硬", "軟"], [r"\eta\leftarrow\mathrm{hard}(\eta)", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{hard}(\mathrm{clip}(\eta)))"),
    (2098, "AdamWHardSoftBound", "2098_adamwhardsoftbound", "AdamWHardSoftBound", "845_linear_167", "opt",
     ["AdamW硬軟境界", "減衰つき", "枠二段"], ["硬", "軟"], [r"\eta\leftarrow\mathrm{hard}(\eta)", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{hard}(\mathrm{clip}(\eta)))"),
    (2099, "LionClipSoftBound", "2099_lionclipsoftbound", "LionClipSoftBound", "845_linear_167", "opt",
     ["Lionクリップ軟境界", "符号更新", "枠二段"], ["クリップ", "軟"], [r"\eta\leftarrow\mathrm{clip}(\eta)", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{clip}(\eta))\in[L,U]"),
    (2100, "垂心九点弧弦比", "2100_h_nine_arc_chord", "HNineArcChord", "846_geometry_167", "tri",
     ["垂心九点弧弦", "弧と弦", "比"], ["配置", "比"], [r"H", r"\widehat{\ell}/\ell_9"], r"\widehat{\ell}/\ell_9"),
    (2101, "重心九点弧弦比", "2101_g_nine_arc_chord", "GNineArcChord", "846_geometry_167", "tri",
     ["重心九点弧弦", "弧と弦", "比"], ["配置", "比"], [r"G", r"\widehat{\ell}/\ell_9"], r"\widehat{\ell}/\ell_9"),
    (2102, "九点弧弦比", "2102_nine_arc_chord", "NineArcChord", "846_geometry_167", "tri",
     ["九点弧弦", "弧と弦", "比"], ["配置", "比"], [r"N", r"\widehat{\ell}/\ell_9"], r"\widehat{\ell}/\ell_9"),
    (2103, "経験一様半径被覆", "2103_emp_unif_radius_cov", "EmpUnifRadiusCov", "847_probability_165", "pts",
     ["経験一様半径被覆", "経験一様", "サイズ"], ["定義", "サイズ"], [r"N_n^{eu}(r,\epsilon)", r"N_n^{eu}\lesssim(r/\epsilon)^d"], r"N_n^{eu}\lesssim(r/\epsilon)^d"),
    (2104, "経験一様半径パッキング", "2104_emp_unif_radius_pack", "EmpUnifRadiusPack", "847_probability_165", "pts",
     ["経験一様半径パッキング", "経験一様", "分離"], ["定義", "サイズ"], [r"M_n^{eu}(r,\epsilon)", r"M_n^{eu}\lesssim(r/\epsilon)^d"], r"M_n^{eu}\lesssim(r/\epsilon)^d"),
    (2105, "ラベル増加森細分", "2105_labeled_inc_forest", "LabeledIncForest", "848_combinatorics_164", "nums",
     ["ラベル増加森", "増加ラベル", "細分"], ["定義", "細分"], [r"LIF_n", r"LIF(n,k)"], r"LIF(n,k)", [1, 2, 8, 44, 296]),
    (2106, "ログ随伴準正則対", "2106_log_adj_semiregular", "LogAdjSemiregular", "849_analysis_168", "box",
     ["ログ随伴準正則", "準正則モデル", "対"], ["定義", "条件"], [r"a(E,X,D)\ge -1", r"(X,D)\ \mathrm{semiregular}"], r"(X,D)\ \mathrm{semiregular}"),
    (2107, "相対ログ随伴準正則対", "2107_rel_log_adj_semiregular", "RelLogAdjSemiregular", "849_analysis_168", "box",
     ["相対ログ随伴準正則", "相対準正則", "ファイバー"], ["定義", "条件"], [r"a(E,X/S,D)\ge -1", r"(X/S,D)\ \mathrm{semiregular}"], r"(X/S,D)\ \mathrm{semiregular}"),
    (2108, "ログ随伴準平滑対", "2108_log_adj_semismooth", "LogAdjSemismooth", "849_analysis_168", "box",
     ["ログ随伴準平滑", "準平滑モデル", "対"], ["定義", "条件"], [r"a(E,X,D)>-1", r"(X,D)\ \mathrm{semismooth}"], r"(X,D)\ \mathrm{semismooth}"),
    (2109, "SophiaClipSoftBound", "2109_sophiaclipsoftbound", "SophiaClipSoftBound", "850_linear_168", "opt",
     ["Sophiaクリップ軟境界", "二階情報", "枠二段"], ["クリップ", "軟"], [r"\eta\leftarrow\mathrm{clip}(\eta)", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{clip}(\eta))\in[L,U]"),
    (2110, "ApolloHardSoftBound", "2110_apollohardsoftbound", "ApolloHardSoftBound", "850_linear_168", "opt",
     ["Apollo硬軟境界", "準ニュートン", "枠二段"], ["硬", "軟"], [r"\eta\leftarrow\mathrm{hard}(\eta)", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{hard}(\mathrm{clip}(\eta)))"),
    (2111, "MuonBoundSoftHard", "2111_muonboundsofthard", "MuonBoundSoftHard", "850_linear_168", "opt",
     ["Muon境界軟硬", "直交更新", "枠二段"], ["軟", "硬"], [r"\eta\leftarrow\mathrm{soft}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{soft}(\mathrm{bound}(\eta)))"),
    (2112, "内心類似九点中心弧比", "2112_in_sym_nine_center_arc", "InSymNineCenterArc", "851_geometry_168", "tri",
     ["内心類似九点中心弧", "中心と弧", "比"], ["配置", "比"], [r"I", r"IN/\widehat{\ell}"], r"IN/\widehat{\ell}"),
    (2113, "傍心類似九点中心弧比", "2113_ex_sym_nine_center_arc", "ExSymNineCenterArc", "851_geometry_168", "tri",
     ["傍心類似九点中心弧", "中心と弧", "比"], ["配置", "比"], [r"I_a", r"I_aN/\widehat{\ell}"], r"I_aN/\widehat{\ell}"),
    (2114, "外心類似九点中心弧比", "2114_o_sym_nine_center_arc", "OSymNineCenterArc", "851_geometry_168", "tri",
     ["外心類似九点中心弧", "中心と弧", "比"], ["配置", "比"], [r"O", r"ON/\widehat{\ell}"], r"ON/\widehat{\ell}"),
    (2115, "一様経験半径被覆", "2115_unif_emp_radius_cov", "UnifEmpRadiusCov", "852_probability_166", "pts",
     ["一様経験半径被覆", "一様経験", "サイズ"], ["定義", "サイズ"], [r"N_n^{ue}(r,\epsilon)", r"N_n^{ue}\lesssim(r/\epsilon)^d"], r"N_n^{ue}\lesssim(r/\epsilon)^d"),
    (2116, "一様経験半径パッキング", "2116_unif_emp_radius_pack", "UnifEmpRadiusPack", "852_probability_166", "pts",
     ["一様経験半径パッキング", "一様経験", "分離"], ["定義", "サイズ"], [r"M_n^{ue}(r,\epsilon)", r"M_n^{ue}\lesssim(r/\epsilon)^d"], r"M_n^{ue}\lesssim(r/\epsilon)^d"),
    (2117, "無根増加森細分", "2117_unrooted_inc_forest", "UnrootedIncForest", "853_combinatorics_165", "nums",
     ["無根増加森", "無根増加", "細分"], ["定義", "細分"], [r"UIF_n", r"UIF(n,k)"], r"UIF(n,k)", [1, 1, 3, 12, 55]),
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
    assert "VIDEOS_2082_2093" not in text

    def block(name, items):
        lines = [f"\n\n{name}: tuple[Video, ...] = ("]
        for num, title, path, cls in items:
            lines.append(f'    Video({num}, "{title}", "{path}", "{cls}"),')
        lines.append(")")
        return "\n".join(lines)

    cp.write_text(
        text.rstrip()
        + block("VIDEOS_2082_2093", created[:12])
        + block("VIDEOS_2094_2105", created[12:24])
        + block("VIDEOS_2106_2117", created[24:])
        + "\n",
        encoding="utf-8",
    )

    tp = ROOT / "tests/test_catalog.py"
    t = tp.read_text(encoding="utf-8")
    if "VIDEOS_2082_2093" not in t:
        t = t.replace(
            "VIDEOS_2070_2081 = _catalog.VIDEOS_2070_2081\n",
            "VIDEOS_2070_2081 = _catalog.VIDEOS_2070_2081\n"
            "VIDEOS_2082_2093 = _catalog.VIDEOS_2082_2093\n"
            "VIDEOS_2094_2105 = _catalog.VIDEOS_2094_2105\n"
            "VIDEOS_2106_2117 = _catalog.VIDEOS_2106_2117\n",
        )
        insert = """
    def test_numbers_are_2082_to_2093(self):
        nums = [v.number for v in VIDEOS_2082_2093]
        self.assertEqual(nums, list(range(2082, 2094)))


    def test_numbers_are_2094_to_2105(self):
        nums = [v.number for v in VIDEOS_2094_2105]
        self.assertEqual(nums, list(range(2094, 2106)))


    def test_numbers_are_2106_to_2117(self):
        nums = [v.number for v in VIDEOS_2106_2117]
        self.assertEqual(nums, list(range(2106, 2118)))

"""
        t = t.replace(
            "    def test_each_scene_file_defines_the_class(self):",
            insert + "    def test_each_scene_file_defines_the_class(self):",
        )
        t = t.replace(
            "            *VIDEOS_2070_2081,\n        ):",
            "            *VIDEOS_2070_2081,\n"
            "            *VIDEOS_2082_2093,\n"
            "            *VIDEOS_2094_2105,\n"
            "            *VIDEOS_2106_2117,\n"
            "        ):",
        )
        tp.write_text(t, encoding="utf-8")

    plan = ROOT / "project/math/PLAN.md"
    p = plan.read_text(encoding="utf-8")
    if "#2082" not in p:
        extra = "\n\n## 導出つき続き（#2082–#2093）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[:12]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#2094–#2105）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[12:24]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#2106–#2117）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[24:]:
            extra += f"| {num} | {title} | 実装 |\n"
        p = p.replace("## 1 本の作業フロー", extra + "\n## 1 本の作業フロー")
        plan.write_text(p, encoding="utf-8")

    print("created", created[0][0], "-", created[-1][0])


if __name__ == "__main__":
    main()
