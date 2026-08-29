#!/usr/bin/env python3
"""Generate #2226–#2261 with derive/proof beats."""
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
    (2226, "ログ随伴弱標準対", "2226_log_adj_weak_canonical", "LogAdjWeakCanonical", "899_analysis_178", "box",
     ["ログ随伴弱標準", "弱標準", "対"], ["定義", "条件"], [r"a(E,X,D)\ge -1/2", r"(X,D)\ \mathrm{weak\ canonical}"], r"(X,D)\ \mathrm{weak\ canonical}"),
    (2227, "相対ログ随伴弱標準対", "2227_rel_log_adj_weak_canonical", "RelLogAdjWeakCanonical", "899_analysis_178", "box",
     ["相対ログ随伴弱標準", "相対弱標準", "ファイバー"], ["定義", "条件"], [r"a(E,X/S,D)\ge -1/2", r"(X/S,D)\ \mathrm{weak\ canonical}"], r"(X/S,D)\ \mathrm{weak\ canonical}"),
    (2228, "ログ随伴準極小対", "2228_log_adj_semiminimal", "LogAdjSemiminimal", "899_analysis_178", "box",
     ["ログ随伴準極小", "準極小", "対"], ["定義", "条件"], [r"(K+D)\cdot C\ge 0", r"(X,D)\ \mathrm{semiminimal}"], r"(X,D)\ \mathrm{semiminimal}"),
    (2229, "RMSBoundHardSoft", "2229_rmsboundhardsoft", "RMSBoundHardSoft", "900_linear_178", "opt",
     ["RMS境界硬軟", "二乗平均", "枠二段"], ["硬", "軟"], [r"\eta\leftarrow\mathrm{hard}(\eta)", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{hard}(\mathrm{bound}(\eta)))"),
    (2230, "LookaheadHardSoftBound", "2230_lookaheadhardsoftbound", "LookaheadHardSoftBound", "900_linear_178", "opt",
     ["Lookahead硬軟境界", "外側平均", "枠二段"], ["硬", "軟"], [r"\eta\leftarrow\mathrm{hard}(\eta)", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{hard}(\mathrm{clip}(\eta)))"),
    (2231, "ProdigySoftHardBound", "2231_prodigysofthardbound", "ProdigySoftHardBound", "900_linear_178", "opt",
     ["Prodigy軟硬境界", "D推定", "枠二段"], ["軟", "硬"], [r"\eta\leftarrow\mathrm{soft}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{soft}(\mathrm{clip}(\eta)))"),
    (2232, "内心類似九点弧弦比", "2232_in_sym_nine_arc_chord", "InSymNineArcChord", "901_geometry_178", "tri",
     ["内心類似九点弧弦", "弧と弦", "比"], ["配置", "比"], [r"I", r"\widehat{\ell}/\ell_9"], r"\widehat{\ell}/\ell_9"),
    (2233, "傍心類似九点弧弦比", "2233_ex_sym_nine_arc_chord", "ExSymNineArcChord", "901_geometry_178", "tri",
     ["傍心類似九点弧弦", "弧と弦", "比"], ["配置", "比"], [r"I_a", r"\widehat{\ell}/\ell_9"], r"\widehat{\ell}/\ell_9"),
    (2234, "外心類似九点弧弦比", "2234_o_sym_nine_arc_chord", "OSymNineArcChord", "901_geometry_178", "tri",
     ["外心類似九点弧弦", "弧と弦", "比"], ["配置", "比"], [r"O", r"\widehat{\ell}/\ell_9"], r"\widehat{\ell}/\ell_9"),
    (2235, "局所スケールデータ被覆", "2235_local_scale_data_cov", "LocalScaleDataCov", "902_probability_176", "pts",
     ["局所スケールデータ被覆", "スケールデータ", "サイズ"], ["定義", "サイズ"], [r"N_n^{lsd}(r,\epsilon)", r"N_n^{lsd}\lesssim(r/\epsilon)^d"], r"N_n^{lsd}\lesssim(r/\epsilon)^d"),
    (2236, "局所スケールデータパッキング", "2236_local_scale_data_pack", "LocalScaleDataPack", "902_probability_176", "pts",
     ["局所スケールデータパッキング", "スケールデータ", "分離"], ["定義", "サイズ"], [r"M_n^{lsd}(r,\epsilon)", r"M_n^{lsd}\lesssim(r/\epsilon)^d"], r"M_n^{lsd}\lesssim(r/\epsilon)^d"),
    (2237, "平面増加林細分", "2237_planar_inc_grove", "PlanarIncGrove", "903_combinatorics_175", "nums",
     ["平面増加林", "平面林", "細分"], ["定義", "細分"], [r"PIG_n", r"PIG(n,k)"], r"PIG(n,k)", [1, 2, 5, 14, 42]),
    (2238, "相対ログ随伴準極小対", "2238_rel_log_adj_semiminimal", "RelLogAdjSemiminimal", "904_analysis_179", "box",
     ["相対ログ随伴準極小", "相対準極小", "ファイバー"], ["定義", "条件"], [r"(K+D)\cdot C\ge 0", r"(X/S,D)\ \mathrm{semiminimal}"], r"(X/S,D)\ \mathrm{semiminimal}"),
    (2239, "ログ随伴準終局対", "2239_log_adj_semifinal", "LogAdjSemifinal", "904_analysis_179", "box",
     ["ログ随伴準終局", "準終局", "対"], ["定義", "条件"], [r"K+D\ \mathrm{nef}", r"(X,D)\ \mathrm{semifinal}"], r"(X,D)\ \mathrm{semifinal}"),
    (2240, "相対ログ随伴準終局対", "2240_rel_log_adj_semifinal", "RelLogAdjSemifinal", "904_analysis_179", "box",
     ["相対ログ随伴準終局", "相対準終局", "ファイバー"], ["定義", "条件"], [r"K+D\ \mathrm{nef}/S", r"(X/S,D)\ \mathrm{semifinal}"], r"(X/S,D)\ \mathrm{semifinal}"),
    (2241, "ScheduleFreeHardBoundSoft", "2241_schedulefreehardboundsoft", "ScheduleFreeHardBoundSoft", "905_linear_179", "opt",
     ["平均化硬境界軟", "スケジュール不要", "枠二段"], ["硬", "軟"], [r"\eta\leftarrow\mathrm{hard}(\eta)", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{hard}(\mathrm{bound}(\eta)))"),
    (2242, "AdamWHardBoundSoft", "2242_adamwhardboundsoft", "AdamWHardBoundSoft", "905_linear_179", "opt",
     ["AdamW硬境界軟", "減衰つき", "枠二段"], ["硬", "軟"], [r"\eta\leftarrow\mathrm{hard}(\eta)", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{hard}(\mathrm{bound}(\eta)))"),
    (2243, "LionSoftHardBound", "2243_lionsofthardbound", "LionSoftHardBound", "905_linear_179", "opt",
     ["Lion軟硬境界", "符号更新", "枠二段"], ["軟", "硬"], [r"\eta\leftarrow\mathrm{soft}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{soft}(\mathrm{clip}(\eta)))"),
    (2244, "垂心類似九点弧弦比", "2244_h_sym_nine_arc_chord", "HSymNineArcChord", "906_geometry_179", "tri",
     ["垂心類似九点弧弦", "弧と弦", "比"], ["配置", "比"], [r"H", r"\widehat{\ell}/\ell_9"], r"\widehat{\ell}/\ell_9"),
    (2245, "重心類似九点弧弦比", "2245_g_sym_nine_arc_chord", "GSymNineArcChord", "906_geometry_179", "tri",
     ["重心類似九点弧弦", "弧と弦", "比"], ["配置", "比"], [r"G", r"\widehat{\ell}/\ell_9"], r"\widehat{\ell}/\ell_9"),
    (2246, "九点類似弧弦比", "2246_n_sym_nine_arc_chord", "NSymNineArcChord", "906_geometry_179", "tri",
     ["九点類似弧弦", "弧と弦", "比"], ["配置", "比"], [r"N", r"\widehat{\ell}/\ell_9"], r"\widehat{\ell}/\ell_9"),
    (2247, "経験スケールデータ被覆", "2247_emp_scale_data_cov", "EmpScaleDataCov", "907_probability_177", "pts",
     ["経験スケールデータ被覆", "経験スケール", "サイズ"], ["定義", "サイズ"], [r"N_n^{esd}(r,\epsilon)", r"N_n^{esd}\lesssim(r/\epsilon)^d"], r"N_n^{esd}\lesssim(r/\epsilon)^d"),
    (2248, "経験スケールデータパッキング", "2248_emp_scale_data_pack", "EmpScaleDataPack", "907_probability_177", "pts",
     ["経験スケールデータパッキング", "経験スケール", "分離"], ["定義", "サイズ"], [r"M_n^{esd}(r,\epsilon)", r"M_n^{esd}\lesssim(r/\epsilon)^d"], r"M_n^{esd}\lesssim(r/\epsilon)^d"),
    (2249, "ケイリー増加林細分", "2249_cayley_inc_grove", "CayleyIncGrove", "908_combinatorics_176", "nums",
     ["ケイリー増加林", "ケイリー林", "細分"], ["定義", "細分"], [r"CIG_n", r"CIG(n,k)"], r"CIG(n,k)", [1, 3, 16, 125, 1296]),
    (2250, "ログ随伴準フリップ対", "2250_log_adj_semiflip", "LogAdjSemiflip", "909_analysis_180", "box",
     ["ログ随伴準フリップ", "準フリップ", "対"], ["定義", "変換"], [r"\phi^-_{\mathrm{semi}}", r"X\dashrightarrow X^+"], r"X\dashrightarrow X^+"),
    (2251, "相対ログ随伴準フリップ対", "2251_rel_log_adj_semiflip", "RelLogAdjSemiflip", "909_analysis_180", "box",
     ["相対ログ随伴準フリップ", "相対準フリップ", "ファイバー"], ["定義", "変換"], [r"\phi^-_{\mathrm{semi}}/S", r"X\dashrightarrow_S X^+"], r"X\dashrightarrow_S X^+"),
    (2252, "ログ随伴準フロップ対", "2252_log_adj_semiflop", "LogAdjSemiflop", "909_analysis_180", "box",
     ["ログ随伴準フロップ", "準フロップ", "対"], ["定義", "変換"], [r"(K+D)\cdot C=0", r"X\dashrightarrow X'"], r"X\dashrightarrow X'"),
    (2253, "SophiaSoftHardBound", "2253_sophiasofthardbound", "SophiaSoftHardBound", "910_linear_180", "opt",
     ["Sophia軟硬境界", "二階情報", "枠二段"], ["軟", "硬"], [r"\eta\leftarrow\mathrm{soft}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{soft}(\mathrm{clip}(\eta)))"),
    (2254, "ApolloHardBoundSoft", "2254_apollohardboundsoft", "ApolloHardBoundSoft", "910_linear_180", "opt",
     ["Apollo硬境界軟", "準ニュートン", "枠二段"], ["硬", "軟"], [r"\eta\leftarrow\mathrm{hard}(\eta)", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{hard}(\mathrm{bound}(\eta)))"),
    (2255, "MuonHardBoundSoft", "2255_muonhardboundsoft", "MuonHardBoundSoft", "910_linear_180", "opt",
     ["Muon硬境界軟", "直交更新", "枠二段"], ["硬", "軟"], [r"\eta\leftarrow\mathrm{hard}(\eta)", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{hard}(\mathrm{bound}(\eta)))"),
    (2256, "内心九点弧心比", "2256_in_nine_arc_center", "InNineArcCenter", "911_geometry_180", "tri",
     ["内心九点弧心", "弧と心", "比"], ["配置", "比"], [r"I", r"\widehat{\ell}/IN"], r"\widehat{\ell}/IN"),
    (2257, "傍心九点弧心比", "2257_ex_nine_arc_center", "ExNineArcCenter", "911_geometry_180", "tri",
     ["傍心九点弧心", "弧と心", "比"], ["配置", "比"], [r"I_a", r"\widehat{\ell}/I_aN"], r"\widehat{\ell}/I_aN"),
    (2258, "外心九点弧心比", "2258_o_nine_arc_center", "ONineArcCenter", "911_geometry_180", "tri",
     ["外心九点弧心", "弧と心", "比"], ["配置", "比"], [r"O", r"\widehat{\ell}/ON"], r"\widehat{\ell}/ON"),
    (2259, "一様スケールデータ被覆", "2259_unif_scale_data_cov", "UnifScaleDataCov", "912_probability_178", "pts",
     ["一様スケールデータ被覆", "一様スケール", "サイズ"], ["定義", "サイズ"], [r"N_n^{usd}(r,\epsilon)", r"N_n^{usd}\lesssim(r/\epsilon)^d"], r"N_n^{usd}\lesssim(r/\epsilon)^d"),
    (2260, "一様スケールデータパッキング", "2260_unif_scale_data_pack", "UnifScaleDataPack", "912_probability_178", "pts",
     ["一様スケールデータパッキング", "一様スケール", "分離"], ["定義", "サイズ"], [r"M_n^{usd}(r,\epsilon)", r"M_n^{usd}\lesssim(r/\epsilon)^d"], r"M_n^{usd}\lesssim(r/\epsilon)^d"),
    (2261, "増加林根細分", "2261_inc_grove_root", "IncGroveRoot", "913_combinatorics_177", "nums",
     ["増加林根", "根細分", "細分"], ["定義", "細分"], [r"IGR_n", r"IGR(n,k)"], r"IGR(n,k)", [1, 1, 3, 10, 35]),

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
    assert "VIDEOS_2226_2237" not in text

    def block(name, items):
        lines = [f"\n\n{name}: tuple[Video, ...] = ("]
        for num, title, path, cls in items:
            lines.append(f'    Video({num}, "{title}", "{path}", "{cls}"),')
        lines.append(")")
        return "\n".join(lines)

    cp.write_text(
        text.rstrip()
        + block("VIDEOS_2226_2237", created[:12])
        + block("VIDEOS_2238_2249", created[12:24])
        + block("VIDEOS_2250_2261", created[24:])
        + "\n",
        encoding="utf-8",
    )

    tp = ROOT / "tests/test_catalog.py"
    t = tp.read_text(encoding="utf-8")
    if "VIDEOS_2226_2237" not in t:
        t = t.replace(
            "VIDEOS_2214_2225 = _catalog.VIDEOS_2214_2225\n",
            "VIDEOS_2214_2225 = _catalog.VIDEOS_2214_2225\n"
            "VIDEOS_2226_2237 = _catalog.VIDEOS_2226_2237\n"
            "VIDEOS_2238_2249 = _catalog.VIDEOS_2238_2249\n"
            "VIDEOS_2250_2261 = _catalog.VIDEOS_2250_2261\n",
        )
        insert = """
    def test_numbers_are_2226_to_2237(self):
        nums = [v.number for v in VIDEOS_2226_2237]
        self.assertEqual(nums, list(range(2226, 2238)))


    def test_numbers_are_2238_to_2249(self):
        nums = [v.number for v in VIDEOS_2238_2249]
        self.assertEqual(nums, list(range(2238, 2250)))


    def test_numbers_are_2250_to_2261(self):
        nums = [v.number for v in VIDEOS_2250_2261]
        self.assertEqual(nums, list(range(2250, 2262)))

"""
        t = t.replace(
            "    def test_each_scene_file_defines_the_class(self):",
            insert + "    def test_each_scene_file_defines_the_class(self):",
        )
        t = t.replace(
            "            *VIDEOS_2214_2225,\n        ):",
            "            *VIDEOS_2214_2225,\n"
            "            *VIDEOS_2226_2237,\n"
            "            *VIDEOS_2238_2249,\n"
            "            *VIDEOS_2250_2261,\n"
            "        ):",
        )
        tp.write_text(t, encoding="utf-8")

    plan = ROOT / "project/math/PLAN.md"
    p = plan.read_text(encoding="utf-8")
    if "#2226" not in p:
        extra = "\n\n## 導出つき続き（#2226–#2237）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[:12]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#2238–#2249）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[12:24]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#2250–#2261）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[24:]:
            extra += f"| {num} | {title} | 実装 |\n"
        p = p.replace("## 1 本の作業フロー", extra + "\n## 1 本の作業フロー")
        plan.write_text(p, encoding="utf-8")

    print("created", created[0][0], "-", created[-1][0])


if __name__ == "__main__":
    main()
