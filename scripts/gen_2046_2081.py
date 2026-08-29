#!/usr/bin/env python3
"""Generate #2046–#2081 with derive/proof beats."""
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
    (2046, "相対ログ随伴フロップ対", "2046_rel_log_adj_flop", "RelLogAdjFlop", "824_analysis_163", "box",
     ["相対ログ随伴フロップ", "相対K自明", "ファイバー"], ["定義", "変換"], [r"(K+D)\cdot C=0", r"X\dashrightarrow_S X'"], r"X\dashrightarrow_S X'"),
    (2047, "ログ随伴収縮対", "2047_log_adj_contraction", "LogAdjContraction", "824_analysis_163", "box",
     ["ログ随伴収縮", "例外因子", "双有理"], ["定義", "像"], [r"\mathrm{Exc}(\phi)", r"X\to X'"], r"X\to X'"),
    (2048, "相対ログ随伴収縮対", "2048_rel_log_adj_contraction", "RelLogAdjContraction", "824_analysis_163", "box",
     ["相対ログ随伴収縮", "相対例外", "ファイバー"], ["定義", "像"], [r"\mathrm{Exc}(\phi/S)", r"X\to_S X'"], r"X\to_S X'"),
    (2049, "RMSSoftBoundHard", "2049_rmssoftboundhard", "RMSSoftBoundHard", "825_linear_163", "opt",
     ["RMS軟境界硬", "二乗平均", "枠二段"], ["軟", "硬"], [r"\eta\leftarrow\mathrm{soft}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{soft}(\mathrm{clip}(\eta)))"),
    (2050, "LookaheadHardBoundClip", "2050_lookaheadhardboundclip", "LookaheadHardBoundClip", "825_linear_163", "opt",
     ["Lookahead硬境界クリップ", "外側平均", "三重"], ["核", "硬境界"], [r"x\leftarrow x+\alpha(y-x)", r"\eta\leftarrow\mathrm{clip}(\mathrm{hard}(\eta))"], r"\eta\leftarrow\mathrm{clip}(\mathrm{hard}(\eta))\in[L,U]"),
    (2051, "ProdigySoftBoundHard", "2051_prodigysoftboundhard", "ProdigySoftBoundHard", "825_linear_163", "opt",
     ["Prodigy軟境界硬", "D推定", "枠二段"], ["軟", "硬"], [r"\eta\leftarrow\mathrm{soft}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{soft}(\mathrm{clip}(\eta)))"),
    (2052, "垂心九点中心弦比", "2052_h_nine_center_chord", "HNineCenterChord", "826_geometry_163", "tri",
     ["垂心九点中心弦", "中心と弦", "比"], ["配置", "比"], [r"H", r"HN/\ell_9"], r"HN/\ell_9"),
    (2053, "重心九点中心弦比", "2053_g_nine_center_chord", "GNineCenterChord", "826_geometry_163", "tri",
     ["重心九点中心弦", "中心と弦", "比"], ["配置", "比"], [r"G", r"GN/\ell_9"], r"GN/\ell_9"),
    (2054, "九点中心弦比", "2054_nine_center_chord", "NineCenterChord", "826_geometry_163", "tri",
     ["九点中心弦", "中心と弦", "比"], ["配置", "比"], [r"N", r"NN'/\ell_9"], r"NN'/\ell_9"),
    (2055, "局所経験半径被覆", "2055_local_emp_radius_cov", "LocalEmpRadiusCov", "827_probability_161", "pts",
     ["局所経験半径被覆", "経験球", "サイズ"], ["定義", "サイズ"], [r"N_n^{\mathrm{emp}}(r,\epsilon)", r"N_n^{\mathrm{emp}}\lesssim(r/\epsilon)^d"], r"N_n^{\mathrm{emp}}\lesssim(r/\epsilon)^d"),
    (2056, "局所経験半径パッキング", "2056_local_emp_radius_pack", "LocalEmpRadiusPack", "827_probability_161", "pts",
     ["局所経験半径パッキング", "経験球", "分離"], ["定義", "サイズ"], [r"M_n^{\mathrm{emp}}(r,\epsilon)", r"M_n^{\mathrm{emp}}\lesssim(r/\epsilon)^d"], r"M_n^{\mathrm{emp}}\lesssim(r/\epsilon)^d"),
    (2057, "二分増加森細分", "2057_binary_inc_forest", "BinaryIncForest", "828_combinatorics_160", "nums",
     ["二分増加森", "二分岐増加", "細分"], ["定義", "細分"], [r"BIF_n", r"BIF(n,k)"], r"BIF(n,k)", [1, 2, 5, 16, 61]),
    (2058, "ログ随伴終端対", "2058_log_adj_terminal", "LogAdjTerminal", "829_analysis_164", "box",
     ["ログ随伴終端", "終端性", "対"], ["定義", "条件"], [r"(K+D)\cdot C\ge 0", r"(X,D)\ \mathrm{terminal}"], r"(X,D)\ \mathrm{terminal}"),
    (2059, "相対ログ随伴終端対", "2059_rel_log_adj_terminal", "RelLogAdjTerminal", "829_analysis_164", "box",
     ["相対ログ随伴終端", "相対終端", "ファイバー"], ["定義", "条件"], [r"(K+D)\cdot C\ge 0", r"(X/S,D)\ \mathrm{terminal}"], r"(X/S,D)\ \mathrm{terminal}"),
    (2060, "ログ随伴極小対", "2060_log_adj_minimal", "LogAdjMinimal", "829_analysis_164", "box",
     ["ログ随伴極小", "極小モデル", "対"], ["定義", "条件"], [r"(K+D)\cdot C\ge 0", r"(X,D)\ \mathrm{minimal}"], r"(X,D)\ \mathrm{minimal}"),
    (2061, "ScheduleFreeSoftBoundHard", "2061_schedulefreesoftboundhard", "ScheduleFreeSoftBoundHard", "830_linear_164", "opt",
     ["平均化軟境界硬", "スケジュール不要", "枠二段"], ["軟", "硬"], [r"\eta\leftarrow\mathrm{soft}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{soft}(\mathrm{clip}(\eta)))"),
    (2062, "AdamWSoftBoundHard", "2062_adamwsoftboundhard", "AdamWSoftBoundHard", "830_linear_164", "opt",
     ["AdamW軟境界硬", "減衰つき", "枠二段"], ["軟", "硬"], [r"\eta\leftarrow\mathrm{soft}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{soft}(\mathrm{clip}(\eta)))"),
    (2063, "LionHardBoundClip", "2063_lionhardboundclip", "LionHardBoundClip", "830_linear_164", "opt",
     ["Lion硬境界クリップ", "符号更新", "三重"], ["核", "硬境界"], [r"u\leftarrow\mathrm{sign}(m)", r"\eta\leftarrow\mathrm{clip}(\mathrm{hard}(\eta))"], r"\eta\leftarrow\mathrm{clip}(\mathrm{hard}(\eta))\in[L,U]"),
    (2064, "内心九点弦弧比", "2064_in_nine_chord_arc", "InNineChordArc", "831_geometry_164", "tri",
     ["内心九点弦弧", "弦と弧", "比"], ["配置", "比"], [r"I", r"\ell_9/\widehat{\ell}"], r"\ell_9/\widehat{\ell}"),
    (2065, "傍心九点弦弧比", "2065_ex_nine_chord_arc", "ExNineChordArc", "831_geometry_164", "tri",
     ["傍心九点弦弧", "弦と弧", "比"], ["配置", "比"], [r"I_a", r"\ell_9/\widehat{\ell}"], r"\ell_9/\widehat{\ell}"),
    (2066, "外心九点弦弧比", "2066_o_nine_chord_arc", "ONineChordArc", "831_geometry_164", "tri",
     ["外心九点弦弧", "弦と弧", "比"], ["配置", "比"], [r"O", r"\ell_9/\widehat{\ell}"], r"\ell_9/\widehat{\ell}"),
    (2067, "一様局所スケール被覆", "2067_unif_local_scale_cov", "UnifLocalScaleCov", "832_probability_162", "pts",
     ["一様局所スケール被覆", "一様局所", "サイズ"], ["定義", "サイズ"], [r"N_{n,u}(B,r,\epsilon)", r"N_{n,u}\lesssim(r/\epsilon)^d"], r"N_{n,u}\lesssim(r/\epsilon)^d"),
    (2068, "一様局所スケールパッキング", "2068_unif_local_scale_pack", "UnifLocalScalePack", "832_probability_162", "pts",
     ["一様局所スケールパッキング", "一様局所", "分離"], ["定義", "サイズ"], [r"M_{n,u}(B,r,\epsilon)", r"M_{n,u}\lesssim(r/\epsilon)^d"], r"M_{n,u}\lesssim(r/\epsilon)^d"),
    (2069, "根つきラベル増加木細分", "2069_rooted_labeled_inc_tree", "RootedLabeledIncTree", "833_combinatorics_161", "nums",
     ["根つきラベル増加木", "根とラベル", "細分"], ["定義", "細分"], [r"RLI_n", r"RLI(n,k)"], r"RLI(n,k)", [1, 1, 4, 20, 124]),
    (2070, "相対ログ随伴極小対", "2070_rel_log_adj_minimal", "RelLogAdjMinimal", "834_analysis_165", "box",
     ["相対ログ随伴極小", "相対極小", "ファイバー"], ["定義", "条件"], [r"(K+D)\cdot C\ge 0", r"(X/S,D)\ \mathrm{minimal}"], r"(X/S,D)\ \mathrm{minimal}"),
    (2071, "ログ随伴終局対", "2071_log_adj_final", "LogAdjFinal", "834_analysis_165", "box",
     ["ログ随伴終局", "終局モデル", "対"], ["定義", "条件"], [r"K+D\ \mathrm{nef}", r"(X,D)\ \mathrm{final}"], r"(X,D)\ \mathrm{final}"),
    (2072, "相対ログ随伴終局対", "2072_rel_log_adj_final", "RelLogAdjFinal", "834_analysis_165", "box",
     ["相対ログ随伴終局", "相対終局", "ファイバー"], ["定義", "条件"], [r"K+D\ \mathrm{nef}/S", r"(X/S,D)\ \mathrm{final}"], r"(X/S,D)\ \mathrm{final}"),
    (2073, "SophiaHardBoundClip", "2073_sophiahardboundclip", "SophiaHardBoundClip", "835_linear_165", "opt",
     ["Sophia硬境界クリップ", "二階情報", "三重"], ["核", "硬境界"], [r"h\leftarrow\beta h+(1-\beta)g^2", r"\eta\leftarrow\mathrm{clip}(\mathrm{hard}(\eta))"], r"\eta\leftarrow\mathrm{clip}(\mathrm{hard}(\eta))\in[L,U]"),
    (2074, "ApolloSoftBoundHard", "2074_apollosoftboundhard", "ApolloSoftBoundHard", "835_linear_165", "opt",
     ["Apollo軟境界硬", "準ニュートン", "枠二段"], ["軟", "硬"], [r"\eta\leftarrow\mathrm{soft}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{soft}(\mathrm{clip}(\eta)))"),
    (2075, "MuonHardSoftBound", "2075_muonhardsoftbound", "MuonHardSoftBound", "835_linear_165", "opt",
     ["Muon硬軟境界", "直交更新", "枠二段"], ["硬", "軟"], [r"\eta\leftarrow\mathrm{hard}(\eta)", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{hard}(\mathrm{clip}(\eta)))"),
    (2076, "垂心九点弦弧比", "2076_h_nine_chord_arc", "HNineChordArc", "836_geometry_165", "tri",
     ["垂心九点弦弧", "弦と弧", "比"], ["配置", "比"], [r"H", r"\ell_9/\widehat{\ell}"], r"\ell_9/\widehat{\ell}"),
    (2077, "重心九点弦弧比", "2077_g_nine_chord_arc", "GNineChordArc", "836_geometry_165", "tri",
     ["重心九点弦弧", "弦と弧", "比"], ["配置", "比"], [r"G", r"\ell_9/\widehat{\ell}"], r"\ell_9/\widehat{\ell}"),
    (2078, "九点弦弧比", "2078_nine_chord_arc", "NineChordArc", "836_geometry_165", "tri",
     ["九点弦弧", "弦と弧", "比"], ["配置", "比"], [r"N", r"\ell_9/\widehat{\ell}"], r"\ell_9/\widehat{\ell}"),
    (2079, "経験データ半径被覆", "2079_emp_data_radius_cov", "EmpDataRadiusCov", "837_probability_163", "pts",
     ["経験データ半径被覆", "経験データ", "サイズ"], ["定義", "サイズ"], [r"N_n^{\mathrm{data}}(r,\epsilon)", r"N_n^{\mathrm{data}}\lesssim(r/\epsilon)^d"], r"N_n^{\mathrm{data}}\lesssim(r/\epsilon)^d"),
    (2080, "経験データ半径パッキング", "2080_emp_data_radius_pack", "EmpDataRadiusPack", "837_probability_163", "pts",
     ["経験データ半径パッキング", "経験データ", "分離"], ["定義", "サイズ"], [r"M_n^{\mathrm{data}}(r,\epsilon)", r"M_n^{\mathrm{data}}\lesssim(r/\epsilon)^d"], r"M_n^{\mathrm{data}}\lesssim(r/\epsilon)^d"),
    (2081, "ケイリー増加森細分", "2081_cayley_inc_forest", "CayleyIncForest", "838_combinatorics_162", "nums",
     ["ケイリー増加森", "ラベル森", "細分"], ["定義", "細分"], [r"CIF_n", r"CIF(n,k)"], r"CIF(n,k)", [1, 3, 16, 125, 1296]),
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
    assert "VIDEOS_2046_2057" not in text

    def block(name, items):
        lines = [f"\n\n{name}: tuple[Video, ...] = ("]
        for num, title, path, cls in items:
            lines.append(f'    Video({num}, "{title}", "{path}", "{cls}"),')
        lines.append(")")
        return "\n".join(lines)

    cp.write_text(
        text.rstrip()
        + block("VIDEOS_2046_2057", created[:12])
        + block("VIDEOS_2058_2069", created[12:24])
        + block("VIDEOS_2070_2081", created[24:])
        + "\n",
        encoding="utf-8",
    )

    tp = ROOT / "tests/test_catalog.py"
    t = tp.read_text(encoding="utf-8")
    if "VIDEOS_2046_2057" not in t:
        t = t.replace(
            "VIDEOS_2034_2045 = _catalog.VIDEOS_2034_2045\n",
            "VIDEOS_2034_2045 = _catalog.VIDEOS_2034_2045\n"
            "VIDEOS_2046_2057 = _catalog.VIDEOS_2046_2057\n"
            "VIDEOS_2058_2069 = _catalog.VIDEOS_2058_2069\n"
            "VIDEOS_2070_2081 = _catalog.VIDEOS_2070_2081\n",
        )
        insert = """
    def test_numbers_are_2046_to_2057(self):
        nums = [v.number for v in VIDEOS_2046_2057]
        self.assertEqual(nums, list(range(2046, 2058)))


    def test_numbers_are_2058_to_2069(self):
        nums = [v.number for v in VIDEOS_2058_2069]
        self.assertEqual(nums, list(range(2058, 2070)))


    def test_numbers_are_2070_to_2081(self):
        nums = [v.number for v in VIDEOS_2070_2081]
        self.assertEqual(nums, list(range(2070, 2082)))

"""
        t = t.replace(
            "    def test_each_scene_file_defines_the_class(self):",
            insert + "    def test_each_scene_file_defines_the_class(self):",
        )
        t = t.replace(
            "            *VIDEOS_2034_2045,\n        ):",
            "            *VIDEOS_2034_2045,\n"
            "            *VIDEOS_2046_2057,\n"
            "            *VIDEOS_2058_2069,\n"
            "            *VIDEOS_2070_2081,\n"
            "        ):",
        )
        tp.write_text(t, encoding="utf-8")

    plan = ROOT / "project/math/PLAN.md"
    p = plan.read_text(encoding="utf-8")
    if "#2046" not in p:
        extra = "\n\n## 導出つき続き（#2046–#2057）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[:12]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#2058–#2069）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[12:24]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#2070–#2081）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[24:]:
            extra += f"| {num} | {title} | 実装 |\n"
        p = p.replace("## 1 本の作業フロー", extra + "\n## 1 本の作業フロー")
        plan.write_text(p, encoding="utf-8")

    print("created", created[0][0], "-", created[-1][0])


if __name__ == "__main__":
    main()
