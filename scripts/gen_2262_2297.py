#!/usr/bin/env python3
"""Generate #2262–#2297 with derive/proof beats."""
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
    (2262, "相対ログ随伴準フロップ対", "2262_rel_log_adj_semiflop", "RelLogAdjSemiflop", "914_analysis_181", "box",
     ["相対ログ随伴準フロップ", "相対準フロップ", "ファイバー"], ["定義", "変換"], [r"(K+D)\cdot C=0", r"X\dashrightarrow_S X'"], r"X\dashrightarrow_S X'"),
    (2263, "ログ随伴準収縮対", "2263_log_adj_semicontraction", "LogAdjSemicontraction", "914_analysis_181", "box",
     ["ログ随伴準収縮", "準収縮", "対"], ["定義", "像"], [r"\mathrm{Exc}_{\mathrm{semi}}(\phi)", r"X\to X'"], r"X\to X'"),
    (2264, "相対ログ随伴準収縮対", "2264_rel_log_adj_semicontraction", "RelLogAdjSemicontraction", "914_analysis_181", "box",
     ["相対ログ随伴準収縮", "相対準収縮", "ファイバー"], ["定義", "像"], [r"\mathrm{Exc}_{\mathrm{semi}}(\phi/S)", r"X\to_S X'"], r"X\to_S X'"),
    (2265, "RMSSoftHardBound", "2265_rmssofthardbound", "RMSSoftHardBound", "915_linear_181", "opt",
     ["RMS軟硬境界", "二乗平均", "枠二段"], ["軟", "硬"], [r"\eta\leftarrow\mathrm{soft}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{soft}(\mathrm{clip}(\eta)))"),
    (2266, "LookaheadSoftHardBound", "2266_lookaheadsofthardbound", "LookaheadSoftHardBound", "915_linear_181", "opt",
     ["Lookahead軟硬境界", "外側平均", "枠二段"], ["軟", "硬"], [r"\eta\leftarrow\mathrm{soft}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{soft}(\mathrm{clip}(\eta)))"),
    (2267, "ProdigyBoundHardSoft", "2267_prodigyboundhardsoft", "ProdigyBoundHardSoft", "915_linear_181", "opt",
     ["Prodigy境界硬軟", "D推定", "枠二段"], ["硬", "軟"], [r"\eta\leftarrow\mathrm{hard}(\eta)", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{hard}(\mathrm{bound}(\eta)))"),
    (2268, "垂心九点弧心比", "2268_h_nine_arc_center", "HNineArcCenter", "916_geometry_181", "tri",
     ["垂心九点弧心", "弧と心", "比"], ["配置", "比"], [r"H", r"\widehat{\ell}/HN"], r"\widehat{\ell}/HN"),
    (2269, "重心九点弧心比", "2269_g_nine_arc_center", "GNineArcCenter", "916_geometry_181", "tri",
     ["重心九点弧心", "弧と心", "比"], ["配置", "比"], [r"G", r"\widehat{\ell}/GN"], r"\widehat{\ell}/GN"),
    (2270, "九点弧心比", "2270_nine_arc_center", "NineArcCenter", "916_geometry_181", "tri",
     ["九点弧心", "弧と心", "比"], ["配置", "比"], [r"N", r"\widehat{\ell}/NN'"], r"\widehat{\ell}/NN'"),
    (2271, "局所半径データ被覆", "2271_local_radius_data_cov", "LocalRadiusDataCov", "917_probability_179", "pts",
     ["局所半径データ被覆", "半径データ", "サイズ"], ["定義", "サイズ"], [r"N_n^{lrd}(r,\epsilon)", r"N_n^{lrd}\lesssim(r/\epsilon)^d"], r"N_n^{lrd}\lesssim(r/\epsilon)^d"),
    (2272, "局所半径データパッキング", "2272_local_radius_data_pack", "LocalRadiusDataPack", "917_probability_179", "pts",
     ["局所半径データパッキング", "半径データ", "分離"], ["定義", "サイズ"], [r"M_n^{lrd}(r,\epsilon)", r"M_n^{lrd}\lesssim(r/\epsilon)^d"], r"M_n^{lrd}\lesssim(r/\epsilon)^d"),
    (2273, "二分増加根林細分", "2273_binary_inc_root_grove", "BinaryIncRootGrove", "918_combinatorics_178", "nums",
     ["二分増加根林", "二分根林", "細分"], ["定義", "細分"], [r"BIRG_n", r"BIRG(n,k)"], r"BIRG(n,k)", [1, 2, 4, 10, 26]),
    (2274, "ログ随伴準移動対", "2274_log_adj_semimove", "LogAdjSemimove", "919_analysis_182", "box",
     ["ログ随伴準移動", "準移動", "対"], ["定義", "変換"], [r"\phi_{\mathrm{semi}}", r"X\dashrightarrow X'"], r"X\dashrightarrow X'"),
    (2275, "相対ログ随伴準移動対", "2275_rel_log_adj_semimove", "RelLogAdjSemimove", "919_analysis_182", "box",
     ["相対ログ随伴準移動", "相対準移動", "ファイバー"], ["定義", "変換"], [r"\phi_{\mathrm{semi}}/S", r"X\dashrightarrow_S X'"], r"X\dashrightarrow_S X'"),
    (2276, "ログ随伴準正値対", "2276_log_adj_semipositive_pair", "LogAdjSemipositivePair", "919_analysis_182", "box",
     ["ログ随伴準正値", "準正値", "対"], ["定義", "条件"], [r"(K+D)\cdot C>0", r"(X,D)\ \mathrm{semipositive}"], r"(X,D)\ \mathrm{semipositive+}"),
    (2277, "ScheduleFreeSoftHardBound", "2277_schedulefreesofthardbound", "ScheduleFreeSoftHardBound", "920_linear_182", "opt",
     ["平均化軟硬境界", "スケジュール不要", "枠二段"], ["軟", "硬"], [r"\eta\leftarrow\mathrm{soft}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{soft}(\mathrm{clip}(\eta)))"),
    (2278, "AdamWSoftHardBound", "2278_adamwsofthardbound", "AdamWSoftHardBound", "920_linear_182", "opt",
     ["AdamW軟硬境界", "減衰つき", "枠二段"], ["軟", "硬"], [r"\eta\leftarrow\mathrm{soft}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{soft}(\mathrm{clip}(\eta)))"),
    (2279, "LionBoundHardSoft", "2279_lionboundhardsoft", "LionBoundHardSoft", "920_linear_182", "opt",
     ["Lion境界硬軟", "符号更新", "枠二段"], ["硬", "軟"], [r"\eta\leftarrow\mathrm{hard}(\eta)", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{hard}(\mathrm{bound}(\eta)))"),
    (2280, "内心九点弦心比", "2280_in_nine_chord_center", "InNineChordCenter", "921_geometry_182", "tri",
     ["内心九点弦心", "弦と心", "比"], ["配置", "比"], [r"I", r"\ell_9/IN"], r"\ell_9/IN"),
    (2281, "傍心九点弦心比", "2281_ex_nine_chord_center", "ExNineChordCenter", "921_geometry_182", "tri",
     ["傍心九点弦心", "弦と心", "比"], ["配置", "比"], [r"I_a", r"\ell_9/I_aN"], r"\ell_9/I_aN"),
    (2282, "外心九点弦心比", "2282_o_nine_chord_center", "ONineChordCenter", "921_geometry_182", "tri",
     ["外心九点弦心", "弦と心", "比"], ["配置", "比"], [r"O", r"\ell_9/ON"], r"\ell_9/ON"),
    (2283, "経験半径データ被覆", "2283_emp_radius_data_cov", "EmpRadiusDataCov", "922_probability_180", "pts",
     ["経験半径データ被覆", "経験半径", "サイズ"], ["定義", "サイズ"], [r"N_n^{erd}(r,\epsilon)", r"N_n^{erd}\lesssim(r/\epsilon)^d"], r"N_n^{erd}\lesssim(r/\epsilon)^d"),
    (2284, "経験半径データパッキング", "2284_emp_radius_data_pack", "EmpRadiusDataPack", "922_probability_180", "pts",
     ["経験半径データパッキング", "経験半径", "分離"], ["定義", "サイズ"], [r"M_n^{erd}(r,\epsilon)", r"M_n^{erd}\lesssim(r/\epsilon)^d"], r"M_n^{erd}\lesssim(r/\epsilon)^d"),
    (2285, "三分増加根林細分", "2285_ternary_inc_root_grove", "TernaryIncRootGrove", "923_combinatorics_179", "nums",
     ["三分増加根林", "三分根林", "細分"], ["定義", "細分"], [r"TIRG_n", r"TIRG(n,k)"], r"TIRG(n,k)", [1, 1, 3, 9, 28]),
    (2286, "相対ログ随伴準正値対", "2286_rel_log_adj_semipositive_pair", "RelLogAdjSemipositivePair", "924_analysis_183", "box",
     ["相対ログ随伴準正値", "相対準正値", "ファイバー"], ["定義", "条件"], [r"(K+D)\cdot C>0", r"(X/S,D)\ \mathrm{semipositive+}"], r"(X/S,D)\ \mathrm{semipositive+}"),
    (2287, "ログ随伴準体積対", "2287_log_adj_semivolume", "LogAdjSemivolume", "924_analysis_183", "box",
     ["ログ随伴準体積", "準体積", "対"], ["定義", "性質"], [r"vol_{\mathrm{semi}}(K+D)", r"vol_{\mathrm{semi}}(K+D)"], r"vol_{\mathrm{semi}}(K+D)"),
    (2288, "相対ログ随伴準体積対", "2288_rel_log_adj_semivolume", "RelLogAdjSemivolume", "924_analysis_183", "box",
     ["相対ログ随伴準体積", "相対準体積", "ファイバー"], ["定義", "性質"], [r"vol_{\mathrm{semi},X/S}(K+D)", r"vol_{\mathrm{semi},X/S}"], r"vol_{\mathrm{semi},X/S}(K+D)"),
    (2289, "SophiaBoundHardSoft", "2289_sophiaboundhardsoft", "SophiaBoundHardSoft", "925_linear_183", "opt",
     ["Sophia境界硬軟", "二階情報", "枠二段"], ["硬", "軟"], [r"\eta\leftarrow\mathrm{hard}(\eta)", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{hard}(\mathrm{bound}(\eta)))"),
    (2290, "ApolloSoftHardBound", "2290_apollosofthardbound", "ApolloSoftHardBound", "925_linear_183", "opt",
     ["Apollo軟硬境界", "準ニュートン", "枠二段"], ["軟", "硬"], [r"\eta\leftarrow\mathrm{soft}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{soft}(\mathrm{clip}(\eta)))"),
    (2291, "MuonClipBoundHard", "2291_muonclipboundhard", "MuonClipBoundHard", "925_linear_183", "opt",
     ["Muonクリップ境界硬", "直交更新", "枠二段"], ["クリップ", "硬"], [r"\eta\leftarrow\mathrm{clip}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{clip}(\eta))\in[L,U]"),
    (2292, "垂心九点弦心比", "2292_h_nine_chord_center", "HNineChordCenter", "926_geometry_183", "tri",
     ["垂心九点弦心", "弦と心", "比"], ["配置", "比"], [r"H", r"\ell_9/HN"], r"\ell_9/HN"),
    (2293, "重心九点弦心比", "2293_g_nine_chord_center", "GNineChordCenter", "926_geometry_183", "tri",
     ["重心九点弦心", "弦と心", "比"], ["配置", "比"], [r"G", r"\ell_9/GN"], r"\ell_9/GN"),
    (2294, "九点弦心比", "2294_nine_chord_center", "NineChordCenter", "926_geometry_183", "tri",
     ["九点弦心", "弦と心", "比"], ["配置", "比"], [r"N", r"\ell_9/NN'"], r"\ell_9/NN'"),
    (2295, "一様半径データ被覆", "2295_unif_radius_data_cov", "UnifRadiusDataCov", "927_probability_181", "pts",
     ["一様半径データ被覆", "一様半径", "サイズ"], ["定義", "サイズ"], [r"N_n^{urd}(r,\epsilon)", r"N_n^{urd}\lesssim(r/\epsilon)^d"], r"N_n^{urd}\lesssim(r/\epsilon)^d"),
    (2296, "一様半径データパッキング", "2296_unif_radius_data_pack", "UnifRadiusDataPack", "927_probability_181", "pts",
     ["一様半径データパッキング", "一様半径", "分離"], ["定義", "サイズ"], [r"M_n^{urd}(r,\epsilon)", r"M_n^{urd}\lesssim(r/\epsilon)^d"], r"M_n^{urd}\lesssim(r/\epsilon)^d"),
    (2297, "ラベル増加根林細分", "2297_labeled_inc_root_grove", "LabeledIncRootGrove", "928_combinatorics_180", "nums",
     ["ラベル増加根林", "ラベル根林", "細分"], ["定義", "細分"], [r"LIRG_n", r"LIRG(n,k)"], r"LIRG(n,k)", [1, 1, 2, 6, 20]),

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
    assert "VIDEOS_2262_2273" not in text

    def block(name, items):
        lines = [f"\n\n{name}: tuple[Video, ...] = ("]
        for num, title, path, cls in items:
            lines.append(f'    Video({num}, "{title}", "{path}", "{cls}"),')
        lines.append(")")
        return "\n".join(lines)

    cp.write_text(
        text.rstrip()
        + block("VIDEOS_2262_2273", created[:12])
        + block("VIDEOS_2274_2285", created[12:24])
        + block("VIDEOS_2286_2297", created[24:])
        + "\n",
        encoding="utf-8",
    )

    tp = ROOT / "tests/test_catalog.py"
    t = tp.read_text(encoding="utf-8")
    if "VIDEOS_2262_2273" not in t:
        t = t.replace(
            "VIDEOS_2250_2261 = _catalog.VIDEOS_2250_2261\n",
            "VIDEOS_2250_2261 = _catalog.VIDEOS_2250_2261\n"
            "VIDEOS_2262_2273 = _catalog.VIDEOS_2262_2273\n"
            "VIDEOS_2274_2285 = _catalog.VIDEOS_2274_2285\n"
            "VIDEOS_2286_2297 = _catalog.VIDEOS_2286_2297\n",
        )
        insert = """
    def test_numbers_are_2262_to_2273(self):
        nums = [v.number for v in VIDEOS_2262_2273]
        self.assertEqual(nums, list(range(2262, 2274)))


    def test_numbers_are_2274_to_2285(self):
        nums = [v.number for v in VIDEOS_2274_2285]
        self.assertEqual(nums, list(range(2274, 2286)))


    def test_numbers_are_2286_to_2297(self):
        nums = [v.number for v in VIDEOS_2286_2297]
        self.assertEqual(nums, list(range(2286, 2298)))

"""
        t = t.replace(
            "    def test_each_scene_file_defines_the_class(self):",
            insert + "    def test_each_scene_file_defines_the_class(self):",
        )
        t = t.replace(
            "            *VIDEOS_2250_2261,\n        ):",
            "            *VIDEOS_2250_2261,\n"
            "            *VIDEOS_2262_2273,\n"
            "            *VIDEOS_2274_2285,\n"
            "            *VIDEOS_2286_2297,\n"
            "        ):",
        )
        tp.write_text(t, encoding="utf-8")

    plan = ROOT / "project/math/PLAN.md"
    p = plan.read_text(encoding="utf-8")
    if "#2262" not in p:
        extra = "\n\n## 導出つき続き（#2262–#2273）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[:12]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#2274–#2285）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[12:24]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#2286–#2297）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[24:]:
            extra += f"| {num} | {title} | 実装 |\n"
        p = p.replace("## 1 本の作業フロー", extra + "\n## 1 本の作業フロー")
        plan.write_text(p, encoding="utf-8")

    print("created", created[0][0], "-", created[-1][0])


if __name__ == "__main__":
    main()
