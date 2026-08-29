#!/usr/bin/env python3
"""Generate #2190–#2225 with derive/proof beats."""
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
    (2190, "相対ログ随伴弱正則対", "2190_rel_log_adj_weak_regular", "RelLogAdjWeakRegular", "884_analysis_175", "box",
     ["相対ログ随伴弱正則", "相対弱正則", "ファイバー"], ["定義", "条件"], [r"a(E,X/S,D)\ge -1/2", r"(X/S,D)\ \mathrm{weak\ regular}"], r"(X/S,D)\ \mathrm{weak\ regular}"),
    (2191, "ログ随伴強平滑対", "2191_log_adj_strong_smooth", "LogAdjStrongSmooth", "884_analysis_175", "box",
     ["ログ随伴強平滑", "強平滑", "対"], ["定義", "条件"], [r"a(E,X,D)\gg 0", r"(X,D)\ \mathrm{strong\ smooth}"], r"(X,D)\ \mathrm{strong\ smooth}"),
    (2192, "相対ログ随伴強平滑対", "2192_rel_log_adj_strong_smooth", "RelLogAdjStrongSmooth", "884_analysis_175", "box",
     ["相対ログ随伴強平滑", "相対強平滑", "ファイバー"], ["定義", "条件"], [r"a(E,X/S,D)\gg 0", r"(X/S,D)\ \mathrm{strong\ smooth}"], r"(X/S,D)\ \mathrm{strong\ smooth}"),
    (2193, "RMSClipSoftBound", "2193_rmsclipsoftbound", "RMSClipSoftBound", "885_linear_175", "opt",
     ["RMSクリップ軟境界", "二乗平均", "枠二段"], ["クリップ", "軟"], [r"\eta\leftarrow\mathrm{clip}(\eta)", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{clip}(\eta))\in[L,U]"),
    (2194, "LookaheadClipSoftBound", "2194_lookaheadclipsoftbound", "LookaheadClipSoftBound", "885_linear_175", "opt",
     ["Lookaheadクリップ軟境界", "外側平均", "枠二段"], ["クリップ", "軟"], [r"\eta\leftarrow\mathrm{clip}(\eta)", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{clip}(\eta))\in[L,U]"),
    (2195, "ProdigyClipHardBound", "2195_prodigycliphardbound", "ProdigyClipHardBound", "885_linear_175", "opt",
     ["Prodigyクリップ硬境界", "D推定", "枠二段"], ["クリップ", "硬"], [r"\eta\leftarrow\mathrm{clip}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{clip}(\eta))\in[L,U]"),
    (2196, "垂心類似九点弦弧比", "2196_h_sym_nine_chord_arc", "HSymNineChordArc", "886_geometry_175", "tri",
     ["垂心類似九点弦弧", "弦と弧", "比"], ["配置", "比"], [r"H", r"\ell_9/\widehat{\ell}"], r"\ell_9/\widehat{\ell}"),
    (2197, "重心類似九点弦弧比", "2197_g_sym_nine_chord_arc", "GSymNineChordArc", "886_geometry_175", "tri",
     ["重心類似九点弦弧", "弦と弧", "比"], ["配置", "比"], [r"G", r"\ell_9/\widehat{\ell}"], r"\ell_9/\widehat{\ell}"),
    (2198, "九点類似弦弧比", "2198_n_sym_nine_chord_arc", "NSymNineChordArc", "886_geometry_175", "tri",
     ["九点類似弦弧", "弦と弧", "比"], ["配置", "比"], [r"N", r"\ell_9/\widehat{\ell}"], r"\ell_9/\widehat{\ell}"),
    (2199, "局所一様データ被覆", "2199_local_unif_data_cov", "LocalUnifDataCov", "887_probability_173", "pts",
     ["局所一様データ被覆", "一様データ", "サイズ"], ["定義", "サイズ"], [r"N_n^{lud}(r,\epsilon)", r"N_n^{lud}\lesssim(r/\epsilon)^d"], r"N_n^{lud}\lesssim(r/\epsilon)^d"),
    (2200, "局所一様データパッキング", "2200_local_unif_data_pack", "LocalUnifDataPack", "887_probability_173", "pts",
     ["局所一様データパッキング", "一様データ", "分離"], ["定義", "サイズ"], [r"M_n^{lud}(r,\epsilon)", r"M_n^{lud}\lesssim(r/\epsilon)^d"], r"M_n^{lud}\lesssim(r/\epsilon)^d"),
    (2201, "根つき増加林細分", "2201_rooted_inc_grove", "RootedIncGrove", "888_combinatorics_172", "nums",
     ["根つき増加林", "根つき林", "細分"], ["定義", "細分"], [r"RIG_n", r"RIG(n,k)"], r"RIG(n,k)", [1, 2, 5, 15, 52]),
    (2202, "ログ随伴弱平滑対", "2202_log_adj_weak_smooth", "LogAdjWeakSmooth", "889_analysis_176", "box",
     ["ログ随伴弱平滑", "弱平滑", "対"], ["定義", "条件"], [r"a(E,X,D)>-1", r"(X,D)\ \mathrm{weak\ smooth}"], r"(X,D)\ \mathrm{weak\ smooth}"),
    (2203, "相対ログ随伴弱平滑対", "2203_rel_log_adj_weak_smooth", "RelLogAdjWeakSmooth", "889_analysis_176", "box",
     ["相対ログ随伴弱平滑", "相対弱平滑", "ファイバー"], ["定義", "条件"], [r"a(E,X/S,D)>-1", r"(X/S,D)\ \mathrm{weak\ smooth}"], r"(X/S,D)\ \mathrm{weak\ smooth}"),
    (2204, "ログ随伴準標準対", "2204_log_adj_semiclassical", "LogAdjSemiclassical", "889_analysis_176", "box",
     ["ログ随伴準標準", "準標準", "対"], ["定義", "条件"], [r"a(E,X,D)\ge 0", r"(X,D)\ \mathrm{semiclassical}"], r"(X,D)\ \mathrm{semiclassical}"),
    (2205, "ScheduleFreeClipHardBound", "2205_schedulefreecliphardbound", "ScheduleFreeClipHardBound", "890_linear_176", "opt",
     ["平均化クリップ硬境界", "スケジュール不要", "枠二段"], ["クリップ", "硬"], [r"\eta\leftarrow\mathrm{clip}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{clip}(\eta))\in[L,U]"),
    (2206, "AdamWClipHardBound", "2206_adamwcliphardbound", "AdamWClipHardBound", "890_linear_176", "opt",
     ["AdamWクリップ硬境界", "減衰つき", "枠二段"], ["クリップ", "硬"], [r"\eta\leftarrow\mathrm{clip}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{clip}(\eta))\in[L,U]"),
    (2207, "LionHardSoftBound", "2207_lionhardsoftbound", "LionHardSoftBound", "890_linear_176", "opt",
     ["Lion硬軟境界", "符号更新", "枠二段"], ["硬", "軟"], [r"\eta\leftarrow\mathrm{hard}(\eta)", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{hard}(\mathrm{clip}(\eta)))"),
    (2208, "内心九点中心弧比", "2208_in_nine_center_arc", "InNineCenterArc", "891_geometry_176", "tri",
     ["内心九点中心弧", "中心と弧", "比"], ["配置", "比"], [r"I", r"IN/\widehat{\ell}"], r"IN/\widehat{\ell}"),
    (2209, "傍心九点中心弧比", "2209_ex_nine_center_arc", "ExNineCenterArc", "891_geometry_176", "tri",
     ["傍心九点中心弧", "中心と弧", "比"], ["配置", "比"], [r"I_a", r"I_aN/\widehat{\ell}"], r"I_aN/\widehat{\ell}"),
    (2210, "外心九点中心弧比", "2210_o_nine_center_arc", "ONineCenterArc", "891_geometry_176", "tri",
     ["外心九点中心弧", "中心と弧", "比"], ["配置", "比"], [r"O", r"ON/\widehat{\ell}"], r"ON/\widehat{\ell}"),
    (2211, "経験一様データ被覆", "2211_emp_unif_data_cov", "EmpUnifDataCov", "892_probability_174", "pts",
     ["経験一様データ被覆", "経験一様", "サイズ"], ["定義", "サイズ"], [r"N_n^{eud}(r,\epsilon)", r"N_n^{eud}\lesssim(r/\epsilon)^d"], r"N_n^{eud}\lesssim(r/\epsilon)^d"),
    (2212, "経験一様データパッキング", "2212_emp_unif_data_pack", "EmpUnifDataPack", "892_probability_174", "pts",
     ["経験一様データパッキング", "経験一様", "分離"], ["定義", "サイズ"], [r"M_n^{eud}(r,\epsilon)", r"M_n^{eud}\lesssim(r/\epsilon)^d"], r"M_n^{eud}\lesssim(r/\epsilon)^d"),
    (2213, "無根増加林細分", "2213_unrooted_inc_grove", "UnrootedIncGrove", "893_combinatorics_173", "nums",
     ["無根増加林", "無根林", "細分"], ["定義", "細分"], [r"UIG_n", r"UIG(n,k)"], r"UIG(n,k)", [1, 1, 2, 5, 14]),
    (2214, "相対ログ随伴準標準対", "2214_rel_log_adj_semiclassical", "RelLogAdjSemiclassical", "894_analysis_177", "box",
     ["相対ログ随伴準標準", "相対準標準", "ファイバー"], ["定義", "条件"], [r"a(E,X/S,D)\ge 0", r"(X/S,D)\ \mathrm{semiclassical}"], r"(X/S,D)\ \mathrm{semiclassical}"),
    (2215, "ログ随伴強標準対", "2215_log_adj_strong_canonical", "LogAdjStrongCanonical", "894_analysis_177", "box",
     ["ログ随伴強標準", "強標準", "対"], ["定義", "条件"], [r"a(E,X,D)>0", r"(X,D)\ \mathrm{strong\ canonical}"], r"(X,D)\ \mathrm{strong\ canonical}"),
    (2216, "相対ログ随伴強標準対", "2216_rel_log_adj_strong_canonical", "RelLogAdjStrongCanonical", "894_analysis_177", "box",
     ["相対ログ随伴強標準", "相対強標準", "ファイバー"], ["定義", "条件"], [r"a(E,X/S,D)>0", r"(X/S,D)\ \mathrm{strong\ canonical}"], r"(X/S,D)\ \mathrm{strong\ canonical}"),
    (2217, "SophiaHardSoftBound", "2217_sophiahardsoftbound", "SophiaHardSoftBound", "895_linear_177", "opt",
     ["Sophia硬軟境界", "二階情報", "枠二段"], ["硬", "軟"], [r"\eta\leftarrow\mathrm{hard}(\eta)", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{hard}(\mathrm{clip}(\eta)))"),
    (2218, "ApolloClipHardBound", "2218_apollocliphardbound", "ApolloClipHardBound", "895_linear_177", "opt",
     ["Apolloクリップ硬境界", "準ニュートン", "枠二段"], ["クリップ", "硬"], [r"\eta\leftarrow\mathrm{clip}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{clip}(\eta))\in[L,U]"),
    (2219, "MuonClipHardBound", "2219_muoncliphardbound", "MuonClipHardBound", "895_linear_177", "opt",
     ["Muonクリップ硬境界", "直交更新", "枠二段"], ["クリップ", "硬"], [r"\eta\leftarrow\mathrm{clip}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{clip}(\eta))\in[L,U]"),
    (2220, "垂心九点中心弧比", "2220_h_nine_center_arc", "HNineCenterArc", "896_geometry_177", "tri",
     ["垂心九点中心弧", "中心と弧", "比"], ["配置", "比"], [r"H", r"HN/\widehat{\ell}"], r"HN/\widehat{\ell}"),
    (2221, "重心九点中心弧比", "2221_g_nine_center_arc", "GNineCenterArc", "896_geometry_177", "tri",
     ["重心九点中心弧", "中心と弧", "比"], ["配置", "比"], [r"G", r"GN/\widehat{\ell}"], r"GN/\widehat{\ell}"),
    (2222, "九点中心弧比", "2222_nine_center_arc", "NineCenterArc", "896_geometry_177", "tri",
     ["九点中心弧", "中心と弧", "比"], ["配置", "比"], [r"N", r"NN'/\widehat{\ell}"], r"NN'/\widehat{\ell}"),
    (2223, "一様局所半径被覆", "2223_unif_local_radius_cov", "UnifLocalRadiusCov", "897_probability_175", "pts",
     ["一様局所半径被覆", "一様局所", "サイズ"], ["定義", "サイズ"], [r"N_n^{ulr}(r,\epsilon)", r"N_n^{ulr}\lesssim(r/\epsilon)^d"], r"N_n^{ulr}\lesssim(r/\epsilon)^d"),
    (2224, "一様局所半径パッキング", "2224_unif_local_radius_pack", "UnifLocalRadiusPack", "897_probability_175", "pts",
     ["一様局所半径パッキング", "一様局所", "分離"], ["定義", "サイズ"], [r"M_n^{ulr}(r,\epsilon)", r"M_n^{ulr}\lesssim(r/\epsilon)^d"], r"M_n^{ulr}\lesssim(r/\epsilon)^d"),
    (2225, "有向増加林細分", "2225_directed_inc_grove", "DirectedIncGrove", "898_combinatorics_174", "nums",
     ["有向増加林", "有向林", "細分"], ["定義", "細分"], [r"DIG_n", r"DIG(n,k)"], r"DIG(n,k)", [1, 2, 6, 22, 90]),

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
    assert "VIDEOS_2190_2201" not in text

    def block(name, items):
        lines = [f"\n\n{name}: tuple[Video, ...] = ("]
        for num, title, path, cls in items:
            lines.append(f'    Video({num}, "{title}", "{path}", "{cls}"),')
        lines.append(")")
        return "\n".join(lines)

    cp.write_text(
        text.rstrip()
        + block("VIDEOS_2190_2201", created[:12])
        + block("VIDEOS_2202_2213", created[12:24])
        + block("VIDEOS_2214_2225", created[24:])
        + "\n",
        encoding="utf-8",
    )

    tp = ROOT / "tests/test_catalog.py"
    t = tp.read_text(encoding="utf-8")
    if "VIDEOS_2190_2201" not in t:
        t = t.replace(
            "VIDEOS_2178_2189 = _catalog.VIDEOS_2178_2189\n",
            "VIDEOS_2178_2189 = _catalog.VIDEOS_2178_2189\n"
            "VIDEOS_2190_2201 = _catalog.VIDEOS_2190_2201\n"
            "VIDEOS_2202_2213 = _catalog.VIDEOS_2202_2213\n"
            "VIDEOS_2214_2225 = _catalog.VIDEOS_2214_2225\n",
        )
        insert = """
    def test_numbers_are_2190_to_2201(self):
        nums = [v.number for v in VIDEOS_2190_2201]
        self.assertEqual(nums, list(range(2190, 2202)))


    def test_numbers_are_2202_to_2213(self):
        nums = [v.number for v in VIDEOS_2202_2213]
        self.assertEqual(nums, list(range(2202, 2214)))


    def test_numbers_are_2214_to_2225(self):
        nums = [v.number for v in VIDEOS_2214_2225]
        self.assertEqual(nums, list(range(2214, 2226)))

"""
        t = t.replace(
            "    def test_each_scene_file_defines_the_class(self):",
            insert + "    def test_each_scene_file_defines_the_class(self):",
        )
        t = t.replace(
            "            *VIDEOS_2178_2189,\n        ):",
            "            *VIDEOS_2178_2189,\n"
            "            *VIDEOS_2190_2201,\n"
            "            *VIDEOS_2202_2213,\n"
            "            *VIDEOS_2214_2225,\n"
            "        ):",
        )
        tp.write_text(t, encoding="utf-8")

    plan = ROOT / "project/math/PLAN.md"
    p = plan.read_text(encoding="utf-8")
    if "#2190" not in p:
        extra = "\n\n## 導出つき続き（#2190–#2201）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[:12]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#2202–#2213）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[12:24]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#2214–#2225）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[24:]:
            extra += f"| {num} | {title} | 実装 |\n"
        p = p.replace("## 1 本の作業フロー", extra + "\n## 1 本の作業フロー")
        plan.write_text(p, encoding="utf-8")

    print("created", created[0][0], "-", created[-1][0])


if __name__ == "__main__":
    main()
