#!/usr/bin/env python3
"""Generate #2154–#2189 with derive/proof beats."""
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
    (2154, "ログ随伴準正対", "2154_log_adj_semipositive", "LogAdjSemipositive", "869_analysis_172", "box",
     ["ログ随伴準正", "準正モデル", "対"], ["定義", "条件"], [r"(K+D)\cdot C\ge 0", r"(X,D)\ \mathrm{semipositive}"], r"(X,D)\ \mathrm{semipositive}"),
    (2155, "相対ログ随伴準正対", "2155_rel_log_adj_semipositive", "RelLogAdjSemipositive", "869_analysis_172", "box",
     ["相対ログ随伴準正", "相対準正", "ファイバー"], ["定義", "条件"], [r"(K+D)\cdot C\ge 0", r"(X/S,D)\ \mathrm{semipositive}"], r"(X/S,D)\ \mathrm{semipositive}"),
    (2156, "ログ随伴強終端対", "2156_log_adj_strong_terminal", "LogAdjStrongTerminal", "869_analysis_172", "box",
     ["ログ随伴強終端", "強終端", "対"], ["定義", "条件"], [r"a(E,X,D)>0", r"(X,D)\ \mathrm{strong\ terminal}"], r"(X,D)\ \mathrm{strong\ terminal}"),
    (2157, "RMSHardSoftBound", "2157_rmshardsoftbound", "RMSHardSoftBound", "870_linear_172", "opt",
     ["RMS硬軟境界", "二乗平均", "枠二段"], ["硬", "軟"], [r"\eta\leftarrow\mathrm{hard}(\eta)", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{hard}(\mathrm{clip}(\eta)))"),
    (2158, "LookaheadBoundSoftHard", "2158_lookaheadboundsofthard", "LookaheadBoundSoftHard", "870_linear_172", "opt",
     ["Lookahead境界軟硬", "外側平均", "枠二段"], ["軟", "硬"], [r"\eta\leftarrow\mathrm{soft}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{soft}(\mathrm{bound}(\eta)))"),
    (2159, "ProdigyBoundSoftHard", "2159_prodigyboundsofthard", "ProdigyBoundSoftHard", "870_linear_172", "opt",
     ["Prodigy境界軟硬", "D推定", "枠二段"], ["軟", "硬"], [r"\eta\leftarrow\mathrm{soft}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{soft}(\mathrm{bound}(\eta)))"),
    (2160, "内心九点弧半径比", "2160_in_nine_arc_radius", "InNineArcRadius", "871_geometry_172", "tri",
     ["内心九点弧半径", "弧と半径", "比"], ["配置", "比"], [r"I", r"\widehat{\ell}/r"], r"\widehat{\ell}/r"),
    (2161, "傍心九点弧半径比", "2161_ex_nine_arc_radius", "ExNineArcRadius", "871_geometry_172", "tri",
     ["傍心九点弧半径", "弧と半径", "比"], ["配置", "比"], [r"I_a", r"\widehat{\ell}/r_a"], r"\widehat{\ell}/r_a"),
    (2162, "外心九点弧半径比", "2162_o_nine_arc_radius", "ONineArcRadius", "871_geometry_172", "tri",
     ["外心九点弧半径", "弧と半径", "比"], ["配置", "比"], [r"O", r"\widehat{\ell}/R"], r"\widehat{\ell}/R"),
    (2163, "局所経験スケール被覆", "2163_local_emp_scale_cov", "LocalEmpScaleCov", "872_probability_170", "pts",
     ["局所経験スケール被覆", "経験局所", "サイズ"], ["定義", "サイズ"], [r"N_n^{les}(r,\epsilon)", r"N_n^{les}\lesssim(r/\epsilon)^d"], r"N_n^{les}\lesssim(r/\epsilon)^d"),
    (2164, "局所経験スケールパッキング", "2164_local_emp_scale_pack", "LocalEmpScalePack", "872_probability_170", "pts",
     ["局所経験スケールパッキング", "経験局所", "分離"], ["定義", "サイズ"], [r"M_n^{les}(r,\epsilon)", r"M_n^{les}\lesssim(r/\epsilon)^d"], r"M_n^{les}\lesssim(r/\epsilon)^d"),
    (2165, "二分増加林細分", "2165_binary_inc_grove", "BinaryIncGrove", "873_combinatorics_169", "nums",
     ["二分増加林", "二分岐林", "細分"], ["定義", "細分"], [r"BIG_n", r"BIG(n,k)"], r"BIG(n,k)", [1, 2, 4, 10, 26]),
    (2166, "相対ログ随伴強終端対", "2166_rel_log_adj_strong_terminal", "RelLogAdjStrongTerminal", "874_analysis_173", "box",
     ["相対ログ随伴強終端", "相対強終端", "ファイバー"], ["定義", "条件"], [r"a(E,X/S,D)>0", r"(X/S,D)\ \mathrm{strong\ terminal}"], r"(X/S,D)\ \mathrm{strong\ terminal}"),
    (2167, "ログ随伴弱終端対", "2167_log_adj_weak_terminal", "LogAdjWeakTerminal", "874_analysis_173", "box",
     ["ログ随伴弱終端", "弱終端", "対"], ["定義", "条件"], [r"a(E,X,D)\ge -1", r"(X,D)\ \mathrm{weak\ terminal}"], r"(X,D)\ \mathrm{weak\ terminal}"),
    (2168, "相対ログ随伴弱終端対", "2168_rel_log_adj_weak_terminal", "RelLogAdjWeakTerminal", "874_analysis_173", "box",
     ["相対ログ随伴弱終端", "相対弱終端", "ファイバー"], ["定義", "条件"], [r"a(E,X/S,D)\ge -1", r"(X/S,D)\ \mathrm{weak\ terminal}"], r"(X/S,D)\ \mathrm{weak\ terminal}"),
    (2169, "ScheduleFreeBoundSoftHard", "2169_schedulefreeboundsofthard", "ScheduleFreeBoundSoftHard", "875_linear_173", "opt",
     ["平均化境界軟硬", "スケジュール不要", "枠二段"], ["軟", "硬"], [r"\eta\leftarrow\mathrm{soft}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{soft}(\mathrm{bound}(\eta)))"),
    (2170, "AdamWBoundSoftHard", "2170_adamwboundsofthard", "AdamWBoundSoftHard", "875_linear_173", "opt",
     ["AdamW境界軟硬", "減衰つき", "枠二段"], ["軟", "硬"], [r"\eta\leftarrow\mathrm{soft}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{soft}(\mathrm{bound}(\eta)))"),
    (2171, "LionClipHardBound", "2171_lioncliphardbound", "LionClipHardBound", "875_linear_173", "opt",
     ["Lionクリップ硬境界", "符号更新", "枠二段"], ["クリップ", "硬"], [r"\eta\leftarrow\mathrm{clip}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{clip}(\eta))\in[L,U]"),
    (2172, "垂心九点弧半径比", "2172_h_nine_arc_radius", "HNineArcRadius", "876_geometry_173", "tri",
     ["垂心九点弧半径", "弧と半径", "比"], ["配置", "比"], [r"H", r"\widehat{\ell}/R"], r"\widehat{\ell}/R"),
    (2173, "重心九点弧半径比", "2173_g_nine_arc_radius", "GNineArcRadius", "876_geometry_173", "tri",
     ["重心九点弧半径", "弧と半径", "比"], ["配置", "比"], [r"G", r"\widehat{\ell}/\ell"], r"\widehat{\ell}/\ell"),
    (2174, "九点弧半径比", "2174_nine_arc_radius", "NineArcRadius", "876_geometry_173", "tri",
     ["九点弧半径", "弧と半径", "比"], ["配置", "比"], [r"N", r"\widehat{\ell}/R_N"], r"\widehat{\ell}/R_N"),
    (2175, "経験データスケール被覆", "2175_emp_data_scale_cov", "EmpDataScaleCov", "877_probability_171", "pts",
     ["経験データスケール被覆", "経験データ", "サイズ"], ["定義", "サイズ"], [r"N_n^{eds}(r,\epsilon)", r"N_n^{eds}\lesssim(r/\epsilon)^d"], r"N_n^{eds}\lesssim(r/\epsilon)^d"),
    (2176, "経験データスケールパッキング", "2176_emp_data_scale_pack", "EmpDataScalePack", "877_probability_171", "pts",
     ["経験データスケールパッキング", "経験データ", "分離"], ["定義", "サイズ"], [r"M_n^{eds}(r,\epsilon)", r"M_n^{eds}\lesssim(r/\epsilon)^d"], r"M_n^{eds}\lesssim(r/\epsilon)^d"),
    (2177, "三分増加林細分", "2177_ternary_inc_grove", "TernaryIncGrove", "878_combinatorics_170", "nums",
     ["三分増加林", "三分岐林", "細分"], ["定義", "細分"], [r"TIG_n", r"TIG(n,k)"], r"TIG(n,k)", [1, 1, 3, 9, 28]),
    (2178, "ログ随伴強正則対", "2178_log_adj_strong_regular", "LogAdjStrongRegular", "879_analysis_174", "box",
     ["ログ随伴強正則", "強正則", "対"], ["定義", "条件"], [r"a(E,X,D)\gg 0", r"(X,D)\ \mathrm{strong\ regular}"], r"(X,D)\ \mathrm{strong\ regular}"),
    (2179, "相対ログ随伴強正則対", "2179_rel_log_adj_strong_regular", "RelLogAdjStrongRegular", "879_analysis_174", "box",
     ["相対ログ随伴強正則", "相対強正則", "ファイバー"], ["定義", "条件"], [r"a(E,X/S,D)\gg 0", r"(X/S,D)\ \mathrm{strong\ regular}"], r"(X/S,D)\ \mathrm{strong\ regular}"),
    (2180, "ログ随伴弱正則対", "2180_log_adj_weak_regular", "LogAdjWeakRegular", "879_analysis_174", "box",
     ["ログ随伴弱正則", "弱正則", "対"], ["定義", "条件"], [r"a(E,X,D)\ge -1/2", r"(X,D)\ \mathrm{weak\ regular}"], r"(X,D)\ \mathrm{weak\ regular}"),
    (2181, "SophiaClipHardBound", "2181_sophiacliphardbound", "SophiaClipHardBound", "880_linear_174", "opt",
     ["Sophiaクリップ硬境界", "二階情報", "枠二段"], ["クリップ", "硬"], [r"\eta\leftarrow\mathrm{clip}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{clip}(\eta))\in[L,U]"),
    (2182, "ApolloBoundSoftHard", "2182_apolloboundsofthard", "ApolloBoundSoftHard", "880_linear_174", "opt",
     ["Apollo境界軟硬", "準ニュートン", "枠二段"], ["軟", "硬"], [r"\eta\leftarrow\mathrm{soft}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{soft}(\mathrm{bound}(\eta)))"),
    (2183, "MuonBoundHardSoft", "2183_muonboundhardsoft", "MuonBoundHardSoft", "880_linear_174", "opt",
     ["Muon境界硬軟", "直交更新", "枠二段"], ["硬", "軟"], [r"\eta\leftarrow\mathrm{hard}(\eta)", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{hard}(\mathrm{bound}(\eta)))"),
    (2184, "内心類似九点弦弧比", "2184_in_sym_nine_chord_arc", "InSymNineChordArc", "881_geometry_174", "tri",
     ["内心類似九点弦弧", "弦と弧", "比"], ["配置", "比"], [r"I", r"\ell_9/\widehat{\ell}"], r"\ell_9/\widehat{\ell}"),
    (2185, "傍心類似九点弦弧比", "2185_ex_sym_nine_chord_arc", "ExSymNineChordArc", "881_geometry_174", "tri",
     ["傍心類似九点弦弧", "弦と弧", "比"], ["配置", "比"], [r"I_a", r"\ell_9/\widehat{\ell}"], r"\ell_9/\widehat{\ell}"),
    (2186, "外心類似九点弦弧比", "2186_o_sym_nine_chord_arc", "OSymNineChordArc", "881_geometry_174", "tri",
     ["外心類似九点弦弧", "弦と弧", "比"], ["配置", "比"], [r"O", r"\ell_9/\widehat{\ell}"], r"\ell_9/\widehat{\ell}"),
    (2187, "一様経験スケール被覆", "2187_unif_emp_scale_cov", "UnifEmpScaleCov", "882_probability_172", "pts",
     ["一様経験スケール被覆", "一様経験", "サイズ"], ["定義", "サイズ"], [r"N_n^{ues}(r,\epsilon)", r"N_n^{ues}\lesssim(r/\epsilon)^d"], r"N_n^{ues}\lesssim(r/\epsilon)^d"),
    (2188, "一様経験スケールパッキング", "2188_unif_emp_scale_pack", "UnifEmpScalePack", "882_probability_172", "pts",
     ["一様経験スケールパッキング", "一様経験", "分離"], ["定義", "サイズ"], [r"M_n^{ues}(r,\epsilon)", r"M_n^{ues}\lesssim(r/\epsilon)^d"], r"M_n^{ues}\lesssim(r/\epsilon)^d"),
    (2189, "ラベル増加林細分", "2189_labeled_inc_grove", "LabeledIncGrove", "883_combinatorics_171", "nums",
     ["ラベル増加林", "ラベル林", "細分"], ["定義", "細分"], [r"LIG_n", r"LIG(n,k)"], r"LIG(n,k)", [1, 1, 2, 6, 20]),
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
    assert "VIDEOS_2154_2165" not in text

    def block(name, items):
        lines = [f"\n\n{name}: tuple[Video, ...] = ("]
        for num, title, path, cls in items:
            lines.append(f'    Video({num}, "{title}", "{path}", "{cls}"),')
        lines.append(")")
        return "\n".join(lines)

    cp.write_text(
        text.rstrip()
        + block("VIDEOS_2154_2165", created[:12])
        + block("VIDEOS_2166_2177", created[12:24])
        + block("VIDEOS_2178_2189", created[24:])
        + "\n",
        encoding="utf-8",
    )

    tp = ROOT / "tests/test_catalog.py"
    t = tp.read_text(encoding="utf-8")
    if "VIDEOS_2154_2165" not in t:
        t = t.replace(
            "VIDEOS_2142_2153 = _catalog.VIDEOS_2142_2153\n",
            "VIDEOS_2142_2153 = _catalog.VIDEOS_2142_2153\n"
            "VIDEOS_2154_2165 = _catalog.VIDEOS_2154_2165\n"
            "VIDEOS_2166_2177 = _catalog.VIDEOS_2166_2177\n"
            "VIDEOS_2178_2189 = _catalog.VIDEOS_2178_2189\n",
        )
        insert = """
    def test_numbers_are_2154_to_2165(self):
        nums = [v.number for v in VIDEOS_2154_2165]
        self.assertEqual(nums, list(range(2154, 2166)))


    def test_numbers_are_2166_to_2177(self):
        nums = [v.number for v in VIDEOS_2166_2177]
        self.assertEqual(nums, list(range(2166, 2178)))


    def test_numbers_are_2178_to_2189(self):
        nums = [v.number for v in VIDEOS_2178_2189]
        self.assertEqual(nums, list(range(2178, 2190)))

"""
        t = t.replace(
            "    def test_each_scene_file_defines_the_class(self):",
            insert + "    def test_each_scene_file_defines_the_class(self):",
        )
        t = t.replace(
            "            *VIDEOS_2142_2153,\n        ):",
            "            *VIDEOS_2142_2153,\n"
            "            *VIDEOS_2154_2165,\n"
            "            *VIDEOS_2166_2177,\n"
            "            *VIDEOS_2178_2189,\n"
            "        ):",
        )
        tp.write_text(t, encoding="utf-8")

    plan = ROOT / "project/math/PLAN.md"
    p = plan.read_text(encoding="utf-8")
    if "#2154" not in p:
        extra = "\n\n## 導出つき続き（#2154–#2165）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[:12]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#2166–#2177）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[12:24]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#2178–#2189）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[24:]:
            extra += f"| {num} | {title} | 実装 |\n"
        p = p.replace("## 1 本の作業フロー", extra + "\n## 1 本の作業フロー")
        plan.write_text(p, encoding="utf-8")

    print("created", created[0][0], "-", created[-1][0])


if __name__ == "__main__":
    main()
