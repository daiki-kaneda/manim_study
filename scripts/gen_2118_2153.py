#!/usr/bin/env python3
"""Generate #2118–#2153 with derive/proof beats."""
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
    (2118, "相対ログ随伴準平滑対", "2118_rel_log_adj_semismooth", "RelLogAdjSemismooth", "854_analysis_169", "box",
     ["相対ログ随伴準平滑", "相対準平滑", "ファイバー"], ["定義", "条件"], [r"a(E,X/S,D)>-1", r"(X/S,D)\ \mathrm{semismooth}"], r"(X/S,D)\ \mathrm{semismooth}"),
    (2119, "ログ随伴純粋対", "2119_log_adj_pure", "LogAdjPure", "854_analysis_169", "box",
     ["ログ随伴純粋", "純粋モデル", "対"], ["定義", "条件"], [r"a(E,X,D)\ge 0", r"(X,D)\ \mathrm{pure}"], r"(X,D)\ \mathrm{pure}"),
    (2120, "相対ログ随伴純粋対", "2120_rel_log_adj_pure", "RelLogAdjPure", "854_analysis_169", "box",
     ["相対ログ随伴純粋", "相対純粋", "ファイバー"], ["定義", "条件"], [r"a(E,X/S,D)\ge 0", r"(X/S,D)\ \mathrm{pure}"], r"(X/S,D)\ \mathrm{pure}"),
    (2121, "RMSBoundSoftHard", "2121_rmsboundsofthard", "RMSBoundSoftHard", "855_linear_169", "opt",
     ["RMS境界軟硬", "二乗平均", "枠二段"], ["軟", "硬"], [r"\eta\leftarrow\mathrm{soft}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{soft}(\mathrm{bound}(\eta)))"),
    (2122, "LookaheadClipHardBound", "2122_lookaheadcliphardbound", "LookaheadClipHardBound", "855_linear_169", "opt",
     ["Lookaheadクリップ硬境界", "外側平均", "枠二段"], ["クリップ", "硬"], [r"\eta\leftarrow\mathrm{clip}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{clip}(\eta))\in[L,U]"),
    (2123, "ProdigyClipSoftBound", "2123_prodigyclipsoftbound", "ProdigyClipSoftBound", "855_linear_169", "opt",
     ["Prodigyクリップ軟境界", "D推定", "枠二段"], ["クリップ", "軟"], [r"\eta\leftarrow\mathrm{clip}(\eta)", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{clip}(\eta))\in[L,U]"),
    (2124, "垂心類似九点中心弧比", "2124_h_sym_nine_center_arc", "HSymNineCenterArc", "856_geometry_169", "tri",
     ["垂心類似九点中心弧", "中心と弧", "比"], ["配置", "比"], [r"H", r"HN/\widehat{\ell}"], r"HN/\widehat{\ell}"),
    (2125, "重心類似九点中心弧比", "2125_g_sym_nine_center_arc", "GSymNineCenterArc", "856_geometry_169", "tri",
     ["重心類似九点中心弧", "中心と弧", "比"], ["配置", "比"], [r"G", r"GN/\widehat{\ell}"], r"GN/\widehat{\ell}"),
    (2126, "九点類似中心弧比", "2126_n_sym_nine_center_arc", "NSymNineCenterArc", "856_geometry_169", "tri",
     ["九点類似中心弧", "中心と弧", "比"], ["配置", "比"], [r"N", r"NN'/\widehat{\ell}"], r"NN'/\widehat{\ell}"),
    (2127, "局所データスケール被覆", "2127_local_data_scale_cov", "LocalDataScaleCov", "857_probability_167", "pts",
     ["局所データスケール被覆", "データ局所", "サイズ"], ["定義", "サイズ"], [r"N_n^{ds}(r,\epsilon)", r"N_n^{ds}\lesssim(r/\epsilon)^d"], r"N_n^{ds}\lesssim(r/\epsilon)^d"),
    (2128, "局所データスケールパッキング", "2128_local_data_scale_pack", "LocalDataScalePack", "857_probability_167", "pts",
     ["局所データスケールパッキング", "データ局所", "分離"], ["定義", "サイズ"], [r"M_n^{ds}(r,\epsilon)", r"M_n^{ds}\lesssim(r/\epsilon)^d"], r"M_n^{ds}\lesssim(r/\epsilon)^d"),
    (2129, "有向増加森細分", "2129_directed_inc_forest", "DirectedIncForest", "858_combinatorics_166", "nums",
     ["有向増加森", "有向増加", "細分"], ["定義", "細分"], [r"DIF_n", r"DIF(n,k)"], r"DIF(n,k)", [1, 2, 6, 24, 120]),
    (2130, "ログ随伴純正則対", "2130_log_adj_pure_regular", "LogAdjPureRegular", "859_analysis_170", "box",
     ["ログ随伴純正則", "純正則", "対"], ["定義", "条件"], [r"a(E,X,D)>0", r"(X,D)\ \mathrm{pure\ regular}"], r"(X,D)\ \mathrm{pure\ regular}"),
    (2131, "相対ログ随伴純正則対", "2131_rel_log_adj_pure_regular", "RelLogAdjPureRegular", "859_analysis_170", "box",
     ["相対ログ随伴純正則", "相対純正則", "ファイバー"], ["定義", "条件"], [r"a(E,X/S,D)>0", r"(X/S,D)\ \mathrm{pure\ regular}"], r"(X/S,D)\ \mathrm{pure\ regular}"),
    (2132, "ログ随伴純平滑対", "2132_log_adj_pure_smooth", "LogAdjPureSmooth", "859_analysis_170", "box",
     ["ログ随伴純平滑", "純平滑", "対"], ["定義", "条件"], [r"a(E,X,D)\gg 0", r"(X,D)\ \mathrm{pure\ smooth}"], r"(X,D)\ \mathrm{pure\ smooth}"),
    (2133, "ScheduleFreeClipSoftBound", "2133_schedulefreeclipsoftbound", "ScheduleFreeClipSoftBound", "860_linear_170", "opt",
     ["平均化クリップ軟境界", "スケジュール不要", "枠二段"], ["クリップ", "軟"], [r"\eta\leftarrow\mathrm{clip}(\eta)", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{clip}(\eta))\in[L,U]"),
    (2134, "AdamWClipSoftBound", "2134_adamwclipsoftbound", "AdamWClipSoftBound", "860_linear_170", "opt",
     ["AdamWクリップ軟境界", "減衰つき", "枠二段"], ["クリップ", "軟"], [r"\eta\leftarrow\mathrm{clip}(\eta)", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{clip}(\eta))\in[L,U]"),
    (2135, "LionBoundSoftHard", "2135_lionboundsofthard", "LionBoundSoftHard", "860_linear_170", "opt",
     ["Lion境界軟硬", "符号更新", "枠二段"], ["軟", "硬"], [r"\eta\leftarrow\mathrm{soft}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{soft}(\mathrm{bound}(\eta)))"),
    (2136, "内心九点弦半径比", "2136_in_nine_chord_radius", "InNineChordRadius", "861_geometry_170", "tri",
     ["内心九点弦半径", "弦と半径", "比"], ["配置", "比"], [r"I", r"\ell_9/r"], r"\ell_9/r"),
    (2137, "傍心九点弦半径比", "2137_ex_nine_chord_radius", "ExNineChordRadius", "861_geometry_170", "tri",
     ["傍心九点弦半径", "弦と半径", "比"], ["配置", "比"], [r"I_a", r"\ell_9/r_a"], r"\ell_9/r_a"),
    (2138, "外心九点弦半径比", "2138_o_nine_chord_radius", "ONineChordRadius", "861_geometry_170", "tri",
     ["外心九点弦半径", "弦と半径", "比"], ["配置", "比"], [r"O", r"\ell_9/R"], r"\ell_9/R"),
    (2139, "経験局所半径被覆", "2139_emp_local_radius_cov", "EmpLocalRadiusCov", "862_probability_168", "pts",
     ["経験局所半径被覆", "経験局所", "サイズ"], ["定義", "サイズ"], [r"N_n^{el}(r,\epsilon)", r"N_n^{el}\lesssim(r/\epsilon)^d"], r"N_n^{el}\lesssim(r/\epsilon)^d"),
    (2140, "経験局所半径パッキング", "2140_emp_local_radius_pack", "EmpLocalRadiusPack", "862_probability_168", "pts",
     ["経験局所半径パッキング", "経験局所", "分離"], ["定義", "サイズ"], [r"M_n^{el}(r,\epsilon)", r"M_n^{el}\lesssim(r/\epsilon)^d"], r"M_n^{el}\lesssim(r/\epsilon)^d"),
    (2141, "平面根つき増加森細分", "2141_planar_rooted_inc_forest", "PlanarRootedIncForest", "863_combinatorics_167", "nums",
     ["平面根つき増加森", "平面根", "細分"], ["定義", "細分"], [r"PRIF_n", r"PRIF(n,k)"], r"PRIF(n,k)", [1, 2, 5, 14, 42]),
    (2142, "相対ログ随伴純平滑対", "2142_rel_log_adj_pure_smooth", "RelLogAdjPureSmooth", "864_analysis_171", "box",
     ["相対ログ随伴純平滑", "相対純平滑", "ファイバー"], ["定義", "条件"], [r"a(E,X/S,D)\gg 0", r"(X/S,D)\ \mathrm{pure\ smooth}"], r"(X/S,D)\ \mathrm{pure\ smooth}"),
    (2143, "ログ随伴準終端対", "2143_log_adj_semiterminal", "LogAdjSemiterminal", "864_analysis_171", "box",
     ["ログ随伴準終端", "準終端", "対"], ["定義", "条件"], [r"a(E,X,D)>-1", r"(X,D)\ \mathrm{semiterminal}"], r"(X,D)\ \mathrm{semiterminal}"),
    (2144, "相対ログ随伴準終端対", "2144_rel_log_adj_semiterminal", "RelLogAdjSemiterminal", "864_analysis_171", "box",
     ["相対ログ随伴準終端", "相対準終端", "ファイバー"], ["定義", "条件"], [r"a(E,X/S,D)>-1", r"(X/S,D)\ \mathrm{semiterminal}"], r"(X/S,D)\ \mathrm{semiterminal}"),
    (2145, "SophiaBoundSoftHard", "2145_sophiaboundsofthard", "SophiaBoundSoftHard", "865_linear_171", "opt",
     ["Sophia境界軟硬", "二階情報", "枠二段"], ["軟", "硬"], [r"\eta\leftarrow\mathrm{soft}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{soft}(\mathrm{bound}(\eta)))"),
    (2146, "ApolloClipSoftBound", "2146_apolloclipsoftbound", "ApolloClipSoftBound", "865_linear_171", "opt",
     ["Apolloクリップ軟境界", "準ニュートン", "枠二段"], ["クリップ", "軟"], [r"\eta\leftarrow\mathrm{clip}(\eta)", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{clip}(\eta))\in[L,U]"),
    (2147, "MuonClipSoftBound", "2147_muonclipsoftbound", "MuonClipSoftBound", "865_linear_171", "opt",
     ["Muonクリップ軟境界", "直交更新", "枠二段"], ["クリップ", "軟"], [r"\eta\leftarrow\mathrm{clip}(\eta)", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{clip}(\eta))\in[L,U]"),
    (2148, "垂心九点弦半径比", "2148_h_nine_chord_radius", "HNineChordRadius", "866_geometry_171", "tri",
     ["垂心九点弦半径", "弦と半径", "比"], ["配置", "比"], [r"H", r"\ell_9/R"], r"\ell_9/R"),
    (2149, "重心九点弦半径比", "2149_g_nine_chord_radius", "GNineChordRadius", "866_geometry_171", "tri",
     ["重心九点弦半径", "弦と半径", "比"], ["配置", "比"], [r"G", r"\ell_9/\ell"], r"\ell_9/\ell"),
    (2150, "九点弦半径比", "2150_nine_chord_radius", "NineChordRadius", "866_geometry_171", "tri",
     ["九点弦半径", "弦と半径", "比"], ["配置", "比"], [r"N", r"\ell_9/R_N"], r"\ell_9/R_N"),
    (2151, "一様データスケール被覆", "2151_unif_data_scale_cov", "UnifDataScaleCov", "867_probability_169", "pts",
     ["一様データスケール被覆", "一様データ", "サイズ"], ["定義", "サイズ"], [r"N_n^{uds}(r,\epsilon)", r"N_n^{uds}\lesssim(r/\epsilon)^d"], r"N_n^{uds}\lesssim(r/\epsilon)^d"),
    (2152, "一様データスケールパッキング", "2152_unif_data_scale_pack", "UnifDataScalePack", "867_probability_169", "pts",
     ["一様データスケールパッキング", "一様データ", "分離"], ["定義", "サイズ"], [r"M_n^{uds}(r,\epsilon)", r"M_n^{uds}\lesssim(r/\epsilon)^d"], r"M_n^{uds}\lesssim(r/\epsilon)^d"),
    (2153, "増加林細分", "2153_inc_grove", "IncGrove", "868_combinatorics_168", "nums",
     ["増加林", "林細分", "細分"], ["定義", "細分"], [r"IG_n", r"IG(n,k)"], r"IG(n,k)", [1, 1, 2, 5, 14]),
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
    assert "VIDEOS_2118_2129" not in text

    def block(name, items):
        lines = [f"\n\n{name}: tuple[Video, ...] = ("]
        for num, title, path, cls in items:
            lines.append(f'    Video({num}, "{title}", "{path}", "{cls}"),')
        lines.append(")")
        return "\n".join(lines)

    cp.write_text(
        text.rstrip()
        + block("VIDEOS_2118_2129", created[:12])
        + block("VIDEOS_2130_2141", created[12:24])
        + block("VIDEOS_2142_2153", created[24:])
        + "\n",
        encoding="utf-8",
    )

    tp = ROOT / "tests/test_catalog.py"
    t = tp.read_text(encoding="utf-8")
    if "VIDEOS_2118_2129" not in t:
        t = t.replace(
            "VIDEOS_2106_2117 = _catalog.VIDEOS_2106_2117\n",
            "VIDEOS_2106_2117 = _catalog.VIDEOS_2106_2117\n"
            "VIDEOS_2118_2129 = _catalog.VIDEOS_2118_2129\n"
            "VIDEOS_2130_2141 = _catalog.VIDEOS_2130_2141\n"
            "VIDEOS_2142_2153 = _catalog.VIDEOS_2142_2153\n",
        )
        insert = """
    def test_numbers_are_2118_to_2129(self):
        nums = [v.number for v in VIDEOS_2118_2129]
        self.assertEqual(nums, list(range(2118, 2130)))


    def test_numbers_are_2130_to_2141(self):
        nums = [v.number for v in VIDEOS_2130_2141]
        self.assertEqual(nums, list(range(2130, 2142)))


    def test_numbers_are_2142_to_2153(self):
        nums = [v.number for v in VIDEOS_2142_2153]
        self.assertEqual(nums, list(range(2142, 2154)))

"""
        t = t.replace(
            "    def test_each_scene_file_defines_the_class(self):",
            insert + "    def test_each_scene_file_defines_the_class(self):",
        )
        t = t.replace(
            "            *VIDEOS_2106_2117,\n        ):",
            "            *VIDEOS_2106_2117,\n"
            "            *VIDEOS_2118_2129,\n"
            "            *VIDEOS_2130_2141,\n"
            "            *VIDEOS_2142_2153,\n"
            "        ):",
        )
        tp.write_text(t, encoding="utf-8")

    plan = ROOT / "project/math/PLAN.md"
    p = plan.read_text(encoding="utf-8")
    if "#2118" not in p:
        extra = "\n\n## 導出つき続き（#2118–#2129）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[:12]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#2130–#2141）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[12:24]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#2142–#2153）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[24:]:
            extra += f"| {num} | {title} | 実装 |\n"
        p = p.replace("## 1 本の作業フロー", extra + "\n## 1 本の作業フロー")
        plan.write_text(p, encoding="utf-8")

    print("created", created[0][0], "-", created[-1][0])


if __name__ == "__main__":
    main()
