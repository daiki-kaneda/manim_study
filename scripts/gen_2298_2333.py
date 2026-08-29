#!/usr/bin/env python3
"""Generate #2298–#2333 with derive/proof beats."""
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
    (2298, "ログ随伴準数値次元対", "2298_log_adj_seminum_dim", "LogAdjSeminumDim", "929_analysis_184", "box",
     ["ログ随伴準数値次元", "準数値次元", "κ"], ["定義", "値"], [r"\kappa_{\mathrm{semi}}(K+D)", r"\kappa_{\mathrm{semi}}\in\{0,\ldots,n\}"], r"\kappa_{\mathrm{semi}}(K+D)"),
    (2299, "相対ログ随伴準数値次元対", "2299_rel_log_adj_seminum_dim", "RelLogAdjSeminumDim", "929_analysis_184", "box",
     ["相対ログ随伴準数値次元", "相対準κ", "ファイバー"], ["定義", "値"], [r"\kappa_{\mathrm{semi}}(X/S,K+D)", r"\kappa_{\mathrm{semi}}"], r"\kappa_{\mathrm{semi}}(X/S,K+D)"),
    (2300, "ログ随伴準飯高対", "2300_log_adj_semiiitaka", "LogAdjSemiIitaka", "929_analysis_184", "box",
     ["ログ随伴準飯高", "準飯高写像", "κ"], ["写像", "次元"], [r"\phi^{\mathrm{semi}}_{|m(K+D)|}", r"\kappa_{\mathrm{semi}}(X,K+D)"], r"\kappa_{\mathrm{semi}}(X,K+D)"),
    (2301, "RMSHardBoundSoft", "2301_rmshardboundsoft", "RMSHardBoundSoft", "930_linear_184", "opt",
     ["RMS硬境界軟", "二乗平均", "枠二段"], ["硬", "軟"], [r"\eta\leftarrow\mathrm{hard}(\eta)", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{hard}(\mathrm{bound}(\eta)))"),
    (2302, "LookaheadBoundHardSoft", "2302_lookaheadboundhardsoft", "LookaheadBoundHardSoft", "930_linear_184", "opt",
     ["Lookahead境界硬軟", "外側平均", "枠二段"], ["硬", "軟"], [r"\eta\leftarrow\mathrm{hard}(\eta)", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{hard}(\mathrm{bound}(\eta)))"),
    (2303, "ProdigyHardBoundSoft", "2303_prodigyhardboundsoft", "ProdigyHardBoundSoft", "930_linear_184", "opt",
     ["Prodigy硬境界軟", "D推定", "枠二段"], ["硬", "軟"], [r"\eta\leftarrow\mathrm{hard}(\eta)", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{hard}(\mathrm{bound}(\eta)))"),
    (2304, "内心類似九点弧心比", "2304_in_sym_nine_arc_center", "InSymNineArcCenter", "931_geometry_184", "tri",
     ["内心類似九点弧心", "弧と心", "比"], ["配置", "比"], [r"I", r"\widehat{\ell}/IN"], r"\widehat{\ell}/IN"),
    (2305, "傍心類似九点弧心比", "2305_ex_sym_nine_arc_center", "ExSymNineArcCenter", "931_geometry_184", "tri",
     ["傍心類似九点弧心", "弧と心", "比"], ["配置", "比"], [r"I_a", r"\widehat{\ell}/I_aN"], r"\widehat{\ell}/I_aN"),
    (2306, "外心類似九点弧心比", "2306_o_sym_nine_arc_center", "OSymNineArcCenter", "931_geometry_184", "tri",
     ["外心類似九点弧心", "弧と心", "比"], ["配置", "比"], [r"O", r"\widehat{\ell}/ON"], r"\widehat{\ell}/ON"),
    (2307, "局所被覆データ半径", "2307_local_cov_data_radius", "LocalCovDataRadius", "932_probability_182", "pts",
     ["局所被覆データ半径", "被覆半径", "サイズ"], ["定義", "サイズ"], [r"r_n^{\mathrm{cov}}", r"N\lesssim(r/\epsilon)^d"], r"N\lesssim(r_n^{\mathrm{cov}}/\epsilon)^d"),
    (2308, "局所パッキングデータ半径", "2308_local_pack_data_radius", "LocalPackDataRadius", "932_probability_182", "pts",
     ["局所パッキングデータ半径", "パッキング半径", "分離"], ["定義", "サイズ"], [r"r_n^{\mathrm{pack}}", r"M\lesssim(r/\epsilon)^d"], r"M\lesssim(r_n^{\mathrm{pack}}/\epsilon)^d"),
    (2309, "根つき増加根林細分", "2309_rooted_inc_root_grove", "RootedIncRootGrove", "933_combinatorics_181", "nums",
     ["根つき増加根林", "根林", "細分"], ["定義", "細分"], [r"RIRG_n", r"RIRG(n,k)"], r"RIRG(n,k)", [1, 2, 5, 15, 52]),
    (2310, "相対ログ随伴準飯高対", "2310_rel_log_adj_semiiitaka", "RelLogAdjSemiIitaka", "934_analysis_185", "box",
     ["相対ログ随伴準飯高", "相対準飯高", "ファイバー"], ["写像", "次元"], [r"\phi^{\mathrm{semi}}/S", r"\kappa_{\mathrm{semi}}(X/S,K+D)"], r"\kappa_{\mathrm{semi}}(X/S,K+D)"),
    (2311, "ログ随伴準飯高次元対", "2311_log_adj_semiiitaka_dim", "LogAdjSemiIitakaDim", "934_analysis_185", "box",
     ["ログ随伴準飯高次元", "次元", "κ"], ["定義", "値"], [r"\dim\phi^{\mathrm{semi}}", r"\kappa_{\mathrm{semi}}"], r"\kappa_{\mathrm{semi}}=\dim\phi^{\mathrm{semi}}"),
    (2312, "相対ログ随伴準飯高次元対", "2312_rel_log_adj_semiiitaka_dim", "RelLogAdjSemiIitakaDim", "934_analysis_185", "box",
     ["相対ログ随伴準飯高次元", "相対次元", "κ"], ["定義", "値"], [r"\dim_S\phi^{\mathrm{semi}}", r"\kappa_{\mathrm{semi}}/S"], r"\kappa_{\mathrm{semi}}(X/S)=\dim_S\phi^{\mathrm{semi}}"),
    (2313, "ScheduleFreeBoundHardSoft", "2313_schedulefreeboundhardsoft", "ScheduleFreeBoundHardSoft", "935_linear_185", "opt",
     ["平均化境界硬軟", "スケジュール不要", "枠二段"], ["硬", "軟"], [r"\eta\leftarrow\mathrm{hard}(\eta)", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{hard}(\mathrm{bound}(\eta)))"),
    (2314, "AdamWBoundHardSoft", "2314_adamwboundhardsoft", "AdamWBoundHardSoft", "935_linear_185", "opt",
     ["AdamW境界硬軟", "減衰つき", "枠二段"], ["硬", "軟"], [r"\eta\leftarrow\mathrm{hard}(\eta)", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{hard}(\mathrm{bound}(\eta)))"),
    (2315, "LionClipBoundHard", "2315_lionclipboundhard", "LionClipBoundHard", "935_linear_185", "opt",
     ["Lionクリップ境界硬", "符号更新", "枠二段"], ["クリップ", "硬"], [r"\eta\leftarrow\mathrm{clip}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{clip}(\eta))\in[L,U]"),
    (2316, "垂心類似九点弧心比", "2316_h_sym_nine_arc_center", "HSymNineArcCenter", "936_geometry_185", "tri",
     ["垂心類似九点弧心", "弧と心", "比"], ["配置", "比"], [r"H", r"\widehat{\ell}/HN"], r"\widehat{\ell}/HN"),
    (2317, "重心類似九点弧心比", "2317_g_sym_nine_arc_center", "GSymNineArcCenter", "936_geometry_185", "tri",
     ["重心類似九点弧心", "弧と心", "比"], ["配置", "比"], [r"G", r"\widehat{\ell}/GN"], r"\widehat{\ell}/GN"),
    (2318, "九点類似弧心比", "2318_n_sym_nine_arc_center", "NSymNineArcCenter", "936_geometry_185", "tri",
     ["九点類似弧心", "弧と心", "比"], ["配置", "比"], [r"N", r"\widehat{\ell}/NN'"], r"\widehat{\ell}/NN'"),
    (2319, "経験被覆データ半径", "2319_emp_cov_data_radius", "EmpCovDataRadius", "937_probability_183", "pts",
     ["経験被覆データ半径", "経験被覆", "サイズ"], ["定義", "サイズ"], [r"r_n^{\mathrm{ecov}}", r"N\lesssim(r/\epsilon)^d"], r"N\lesssim(r_n^{\mathrm{ecov}}/\epsilon)^d"),
    (2320, "経験パッキングデータ半径", "2320_emp_pack_data_radius", "EmpPackDataRadius", "937_probability_183", "pts",
     ["経験パッキングデータ半径", "経験パッキング", "分離"], ["定義", "サイズ"], [r"r_n^{\mathrm{epack}}", r"M\lesssim(r/\epsilon)^d"], r"M\lesssim(r_n^{\mathrm{epack}}/\epsilon)^d"),
    (2321, "無根増加根林細分", "2321_unrooted_inc_root_grove", "UnrootedIncRootGrove", "938_combinatorics_182", "nums",
     ["無根増加根林", "無根根林", "細分"], ["定義", "細分"], [r"UIRG_n", r"UIRG(n,k)"], r"UIRG(n,k)", [1, 1, 2, 5, 14]),
    (2322, "ログ随伴準数値対", "2322_log_adj_seminumeric", "LogAdjSeminumeric", "939_analysis_186", "box",
     ["ログ随伴準数値", "準数値", "対"], ["定義", "条件"], [r"\kappa_{\mathrm{semi}}\ge 0", r"(X,D)\ \mathrm{seminumeric}"], r"(X,D)\ \mathrm{seminumeric}"),
    (2323, "相対ログ随伴準数値対", "2323_rel_log_adj_seminumeric", "RelLogAdjSeminumeric", "939_analysis_186", "box",
     ["相対ログ随伴準数値", "相対準数値", "ファイバー"], ["定義", "条件"], [r"\kappa_{\mathrm{semi}}/S\ge 0", r"(X/S,D)\ \mathrm{seminumeric}"], r"(X/S,D)\ \mathrm{seminumeric}"),
    (2324, "ログ随伴準κ対", "2324_log_adj_semikappa", "LogAdjSemiKappa", "939_analysis_186", "box",
     ["ログ随伴準κ", "準κ", "対"], ["定義", "値"], [r"\kappa_{\mathrm{semi}}", r"\kappa_{\mathrm{semi}}\in\{0,\ldots,n\}"], r"\kappa_{\mathrm{semi}}(K+D)"),
    (2325, "SophiaClipBoundHard", "2325_sophiaclipboundhard", "SophiaClipBoundHard", "940_linear_186", "opt",
     ["Sophiaクリップ境界硬", "二階情報", "枠二段"], ["クリップ", "硬"], [r"\eta\leftarrow\mathrm{clip}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{clip}(\eta))\in[L,U]"),
    (2326, "ApolloBoundHardSoft", "2326_apolloboundhardsoft", "ApolloBoundHardSoft", "940_linear_186", "opt",
     ["Apollo境界硬軟", "準ニュートン", "枠二段"], ["硬", "軟"], [r"\eta\leftarrow\mathrm{hard}(\eta)", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{hard}(\mathrm{bound}(\eta)))"),
    (2327, "MuonSoftClipHard", "2327_muonsoftcliphard", "MuonSoftClipHard", "940_linear_186", "opt",
     ["Muon軟クリップ硬", "直交更新", "枠二段"], ["軟", "硬"], [r"\eta\leftarrow\mathrm{soft}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{soft}(\mathrm{clip}(\eta)))"),
    (2328, "内心九点弧弦心比", "2328_in_nine_arc_chord_center", "InNineArcChordCenter", "941_geometry_186", "tri",
     ["内心九点弧弦心", "弧弦心", "比"], ["配置", "比"], [r"I", r"\widehat{\ell}/\ell_9/IN"], r"(\widehat{\ell}/\ell_9)/IN"),
    (2329, "傍心九点弧弦心比", "2329_ex_nine_arc_chord_center", "ExNineArcChordCenter", "941_geometry_186", "tri",
     ["傍心九点弧弦心", "弧弦心", "比"], ["配置", "比"], [r"I_a", r"\widehat{\ell}/\ell_9/I_aN"], r"(\widehat{\ell}/\ell_9)/I_aN"),
    (2330, "外心九点弧弦心比", "2330_o_nine_arc_chord_center", "ONineArcChordCenter", "941_geometry_186", "tri",
     ["外心九点弧弦心", "弧弦心", "比"], ["配置", "比"], [r"O", r"\widehat{\ell}/\ell_9/ON"], r"(\widehat{\ell}/\ell_9)/ON"),
    (2331, "一様被覆データ半径", "2331_unif_cov_data_radius", "UnifCovDataRadius", "942_probability_184", "pts",
     ["一様被覆データ半径", "一様被覆", "サイズ"], ["定義", "サイズ"], [r"r_n^{\mathrm{ucov}}", r"N\lesssim(r/\epsilon)^d"], r"N\lesssim(r_n^{\mathrm{ucov}}/\epsilon)^d"),
    (2332, "一様パッキングデータ半径", "2332_unif_pack_data_radius", "UnifPackDataRadius", "942_probability_184", "pts",
     ["一様パッキングデータ半径", "一様パッキング", "分離"], ["定義", "サイズ"], [r"r_n^{\mathrm{upack}}", r"M\lesssim(r/\epsilon)^d"], r"M\lesssim(r_n^{\mathrm{upack}}/\epsilon)^d"),
    (2333, "有向増加根林細分", "2333_directed_inc_root_grove", "DirectedIncRootGrove", "943_combinatorics_183", "nums",
     ["有向増加根林", "有向根林", "細分"], ["定義", "細分"], [r"DIRG_n", r"DIRG(n,k)"], r"DIRG(n,k)", [1, 2, 6, 22, 90]),
]


def patch_catalog(created):
    cp = ROOT / "project/math/catalog.py"
    text = cp.read_text(encoding="utf-8")
    assert "VIDEOS_2298_2309" not in text

    def block(name, items):
        lines = [f"\n\n{name}: tuple[Video, ...] = ("]
        for num, title, path, cls in items:
            lines.append(f'    Video({num}, "{title}", "{path}", "{cls}"),')
        lines.append(")")
        return "\n".join(lines)

    cp.write_text(
        text.rstrip()
        + block("VIDEOS_2298_2309", created[:12])
        + block("VIDEOS_2310_2321", created[12:24])
        + block("VIDEOS_2322_2333", created[24:])
        + "\n",
        encoding="utf-8",
    )


def patch_tests():
    tp = ROOT / "tests/test_catalog.py"
    t = tp.read_text(encoding="utf-8")
    if "VIDEOS_2298_2309" in t:
        return
    # append imports after last VIDEOS_22xx import line
    import re
    imports = (
        "VIDEOS_2298_2309 = _catalog.VIDEOS_2298_2309\n"
        "VIDEOS_2310_2321 = _catalog.VIDEOS_2310_2321\n"
        "VIDEOS_2322_2333 = _catalog.VIDEOS_2322_2333\n"
    )
    m = list(re.finditer(r'^VIDEOS_\d+_\d+ = _catalog\.VIDEOS_\d+_\d+\n', t, re.M))
    assert m
    last = m[-1]
    t = t[: last.end()] + imports + t[last.end() :]

    insert = """
    def test_numbers_are_2298_to_2309(self):
        nums = [v.number for v in VIDEOS_2298_2309]
        self.assertEqual(nums, list(range(2298, 2310)))


    def test_numbers_are_2310_to_2321(self):
        nums = [v.number for v in VIDEOS_2310_2321]
        self.assertEqual(nums, list(range(2310, 2322)))


    def test_numbers_are_2322_to_2333(self):
        nums = [v.number for v in VIDEOS_2322_2333]
        self.assertEqual(nums, list(range(2322, 2334)))

"""
    t = t.replace(
        "    def test_each_scene_file_defines_the_class(self):",
        insert + "    def test_each_scene_file_defines_the_class(self):",
    )
    stars = (
        "            *VIDEOS_2298_2309,\n"
        "            *VIDEOS_2310_2321,\n"
        "            *VIDEOS_2322_2333,\n"
    )
    sm = list(re.finditer(r'^            \*VIDEOS_\d+_\d+,\n', t, re.M))
    assert sm
    last_s = sm[-1]
    # insert before the closing `        ):` after last star
    t = t[: last_s.end()] + stars + t[last_s.end() :]
    tp.write_text(t, encoding="utf-8")


def patch_plan(created):
    plan = ROOT / "project/math/PLAN.md"
    p = plan.read_text(encoding="utf-8")
    if "#2298" in p:
        return
    extra = "\n\n## 導出つき続き（#2298–#2309）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
    for num, title, _, _ in created[:12]:
        extra += f"| {num} | {title} | 実装 |\n"
    extra += "\n\n## 導出つき続き（#2310–#2321）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
    for num, title, _, _ in created[12:24]:
        extra += f"| {num} | {title} | 実装 |\n"
    extra += "\n\n## 導出つき続き（#2322–#2333）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
    for num, title, _, _ in created[24:]:
        extra += f"| {num} | {title} | 実装 |\n"
    p = p.replace("## 1 本の作業フロー", extra + "\n## 1 本の作業フロー")
    plan.write_text(p, encoding="utf-8")


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

    patch_catalog(created)
    patch_tests()
    patch_plan(created)
    print("created", created[0][0], "-", created[-1][0])


if __name__ == "__main__":
    main()
