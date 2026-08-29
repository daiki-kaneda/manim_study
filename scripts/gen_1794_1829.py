#!/usr/bin/env python3
"""Generate #1794–#1829 with derive/proof beats."""
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
    (1794, "ログ多重度対", "1794_log_mult_pair", "LogMultPair", "719_analysis_142", "box",
     ["ログ多重度", "特異多重度", "境界"], ["定義", "判定"], [r"\mathrm{mult}", r"\mathrm{mult}_x\ge m"], r"m_x\ge m"),
    (1795, "相対ログ多重度対", "1795_rel_log_mult", "RelLogMult", "719_analysis_142", "box",
     ["相対ログ多重度", "相対多重度", "ファイバー"], ["定義", "判定"], [r"\mathrm{mult}/S", r"m_x\ge m"], r"m_x\ge m"),
    (1796, "ログ交点数対", "1796_log_intersect_pair", "LogIntersectPair", "719_analysis_142", "box",
     ["ログ交点数", "交差形式", "数値"], ["定義", "値"], [r"(D_1\cdot D_2)", r"(D_1\cdot D_2)\in\mathbb{Z}"], r"(D_1\cdot D_2)"),
    (1797, "ApolloBoundHard", "1797_apolloboundhard", "ApolloBoundHard", "720_linear_142", "opt",
     ["Apollo境界硬閾", "準ニュートン", "剪定"], ["核", "硬境界"], [r"B\leftarrow B+uu^\top", r"\eta\leftarrow\mathrm{hard}(\eta)"], r"\eta\leftarrow\mathrm{hard}(\mathrm{clip}(\eta))"),
    (1798, "MuonSoftBoundClip", "1798_muonsoftboundclip", "MuonSoftBoundClip", "720_linear_142", "opt",
     ["Muon軟境界クリップ", "直交更新", "三重"], ["核", "軟境界"], [r"U^\top U=I", r"\eta\leftarrow\mathrm{clip}(\mathrm{soft}(\eta))"], r"\eta\leftarrow\mathrm{clip}(\mathrm{soft}(\eta))\in[L,U]"),
    (1799, "SamHardBound", "1799_samhardbound", "SamHardBound", "720_linear_142", "opt",
     ["SAM硬境界", "鋭度", "枠剪定"], ["核", "硬境界"], [r"\epsilon\leftarrow\rho g/\|g\|", r"\rho\leftarrow\mathrm{hard}(\rho)\in[L,U]"], r"\rho\leftarrow\mathrm{hard}(\mathrm{clip}(\rho))"),
    (1800, "内心フォイエル弧比", "1800_in_feuer_arc", "InFeuerArc", "721_geometry_142", "tri",
     ["内心フォイエル弧", "九点円弧", "比"], ["配置", "比"], [r"I", r"\overset{\frown}{AB}/r"], r"\ell_{\mathrm{arc}}/r"),
    (1801, "傍心フォイエル弧比", "1801_ex_feuer_arc", "ExFeuerArc", "721_geometry_142", "tri",
     ["傍心フォイエル弧", "九点円弧", "比"], ["配置", "比"], [r"I_a", r"\ell_{\mathrm{arc}}/r_a"], r"\ell_{\mathrm{arc}}/r_a"),
    (1802, "外心フォイエル弧比", "1802_o_feuer_arc", "OFeuerArc", "721_geometry_142", "tri",
     ["外心フォイエル弧", "九点円弧", "比"], ["配置", "比"], [r"O", r"\ell_{\mathrm{arc}}/R"], r"\ell_{\mathrm{arc}}/R"),
    (1803, "局所半径被覆", "1803_local_radius_covering", "LocalRadiusCovering", "722_probability_140", "pts",
     ["局所半径被覆", "球内被覆", "サイズ"], ["定義", "サイズ"], [r"N(B(f,r),\epsilon)", r"N\lesssim (r/\epsilon)^d"], r"N\lesssim (r/\epsilon)^d"),
    (1804, "局所半径パッキング", "1804_local_radius_packing", "LocalRadiusPacking", "722_probability_140", "pts",
     ["局所半径パッキング", "球内分離", "サイズ"], ["定義", "サイズ"], [r"M(B(f,r),\epsilon)", r"M\lesssim (r/\epsilon)^d"], r"M\lesssim (r/\epsilon)^d"),
    (1805, "増加森細分", "1805_inc_forest_refine", "IncForestRefine", "723_combinatorics_139", "nums",
     ["増加森", "ラベル増加", "細分"], ["定義", "細分"], [r"IF_n", r"IF(n,k)"], r"IF(n,k)", [1, 2, 7, 38, 291]),
    (1806, "相対ログ交点数対", "1806_rel_log_intersect", "RelLogIntersect", "724_analysis_143", "box",
     ["相対ログ交点数", "相対交差", "数値"], ["定義", "値"], [r"(D_1\cdot D_2)_S", r"(D_1\cdot D_2)_S"], r"(D_1\cdot D_2)_S"),
    (1807, "ログ次数対", "1807_log_degree_pair", "LogDegreePair", "724_analysis_143", "box",
     ["ログ次数", "因子次数", "数値"], ["定義", "値"], [r"\deg(D)", r"\deg(D)=\int c_1(D)"], r"\deg(D)"),
    (1808, "相対ログ次数対", "1808_rel_log_degree", "RelLogDegree", "724_analysis_143", "box",
     ["相対ログ次数", "相対次数", "ファイバー"], ["定義", "値"], [r"\deg(D/S)", r"\deg(D|_F)"], r"\deg(D|_F)"),
    (1809, "AdaFactorSoftBound", "1809_adafactorsoftbound", "AdaFactorSoftBound", "725_linear_143", "opt",
     ["AdaFactor軟境界", "因子化", "平滑枠"], ["核", "軟境界"], [r"R_{ij}C_{ij}\approx G_{ij}^2", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{clip}(\eta))"),
    (1810, "NAdamHardSoft", "1810_nadamhardsoft", "NAdamHardSoft", "725_linear_143", "opt",
     ["NAdam硬軟", "ネステロフ", "逆二段"], ["硬", "軟"], [r"u\leftarrow\mathrm{hard}(u)", r"u\leftarrow\mathrm{soft}(u)"], r"u\leftarrow\mathrm{soft}(\mathrm{hard}(u))"),
    (1811, "LAMBHardBound", "1811_lambhardbound", "LAMBHardBound", "725_linear_143", "opt",
     ["LAMB硬境界", "層信頼域", "枠剪定"], ["核", "硬境界"], [r"r\leftarrow\|w\|/\|\hat u\|", r"r\leftarrow\mathrm{hard}(r)\in[L,U]"], r"r\leftarrow\mathrm{hard}(\mathrm{clip}(r))"),
    (1812, "垂心フォイエル弧比", "1812_h_feuer_arc", "HFeuerArc", "726_geometry_143", "tri",
     ["垂心フォイエル弧", "九点円弧", "比"], ["配置", "比"], [r"H", r"\ell_{\mathrm{arc}}/R"], r"\ell_{\mathrm{arc}}/R"),
    (1813, "重心フォイエル弧比", "1813_g_feuer_arc", "GFeuerArc", "726_geometry_143", "tri",
     ["重心フォイエル弧", "九点円弧", "比"], ["配置", "比"], [r"G", r"\ell_{\mathrm{arc}}/\ell"], r"\ell_{\mathrm{arc}}/\ell"),
    (1814, "九点フォイエル弧比", "1814_n_feuer_arc", "NFeuerArc", "726_geometry_143", "tri",
     ["九点円フォイエル弧", "弧", "比"], ["配置", "比"], [r"N", r"\ell_{\mathrm{arc}}/R_N"], r"\ell_{\mathrm{arc}}/R_N"),
    (1815, "経験半径被覆", "1815_emp_radius_covering", "EmpRadiusCovering", "727_probability_141", "pts",
     ["経験半径被覆", "データ球被覆", "サイズ"], ["定義", "サイズ"], [r"N_n(r,\epsilon)", r"N_n\lesssim (r/\epsilon)^d"], r"N_n\lesssim (r/\epsilon)^d"),
    (1816, "経験半径パッキング", "1816_emp_radius_packing", "EmpRadiusPacking", "727_probability_141", "pts",
     ["経験半径パッキング", "データ球分離", "サイズ"], ["定義", "サイズ"], [r"M_n(r,\epsilon)", r"M_n\lesssim (r/\epsilon)^d"], r"M_n\lesssim (r/\epsilon)^d"),
    (1817, "減少木細分", "1817_dec_tree_refine", "DecTreeRefine", "728_combinatorics_140", "nums",
     ["減少木", "ラベル減少", "細分"], ["定義", "細分"], [r"DT_n", r"DT(n,k)"], r"DT(n,k)", [1, 1, 3, 13, 71]),
    (1818, "ログ体積多項式対", "1818_log_vol_poly_pair", "LogVolPolyPair", "729_analysis_144", "box",
     ["ログ体積多項式", "体積展開", "係数"], ["定義", "展開"], [r"vol(tD)", r"vol(tD)=\sum a_k t^k"], r"vol(tD)=\sum a_k t^k"),
    (1819, "相対ログ体積多項式対", "1819_rel_log_vol_poly", "RelLogVolPoly", "729_analysis_144", "box",
     ["相対ログ体積多項式", "相対体積", "係数"], ["定義", "展開"], [r"vol_{X/S}(tD)", r"vol=\sum a_k t^k"], r"vol=\sum a_k t^k"),
    (1820, "ログ自己交対", "1820_log_self_intersect", "LogSelfIntersect", "729_analysis_144", "box",
     ["ログ自己交", "自己交差", "数値"], ["定義", "値"], [r"D^2", r"D^2=(D\cdot D)"], r"D^2"),
    (1821, "LookaheadHardBound", "1821_lookaheadhardbound", "LookaheadHardBound", "730_linear_144", "opt",
     ["Lookahead硬境界", "外側平均", "枠剪定"], ["核", "硬境界"], [r"x\leftarrow x+\alpha(y-x)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{clip}(\eta))"),
    (1822, "ProdigyHardBound", "1822_prodigyhardbound", "ProdigyHardBound", "730_linear_144", "opt",
     ["Prodigy硬境界", "D推定", "枠剪定"], ["核", "硬境界"], [r"d\leftarrow\|g\|", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{clip}(\eta))"),
    (1823, "ScheduleFreeHardBound", "1823_schedulefreehardbound", "ScheduleFreeHardBound", "730_linear_144", "opt",
     ["平均化硬境界", "スケジュール不要", "枠剪定"], ["核", "硬境界"], [r"z\leftarrow (1-c)z+cx", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{clip}(\eta))"),
    (1824, "内心類似フォイエル弧比", "1824_in_sym_feuer_arc", "InSymFeuerArc", "731_geometry_144", "tri",
     ["内心類似弧", "九点円弧", "比"], ["配置", "比"], [r"I", r"\ell_{\mathrm{arc},s}/r"], r"\ell_{\mathrm{arc},s}/r"),
    (1825, "傍心類似フォイエル弧比", "1825_ex_sym_feuer_arc", "ExSymFeuerArc", "731_geometry_144", "tri",
     ["傍心類似弧", "九点円弧", "比"], ["配置", "比"], [r"I_a", r"\ell_{\mathrm{arc},s}/r_a"], r"\ell_{\mathrm{arc},s}/r_a"),
    (1826, "外心類似フォイエル弧比", "1826_o_sym_feuer_arc", "OSymFeuerArc", "731_geometry_144", "tri",
     ["外心類似弧", "九点円弧", "比"], ["配置", "比"], [r"O", r"\ell_{\mathrm{arc},s}/R"], r"\ell_{\mathrm{arc},s}/R"),
    (1827, "一様半径被覆", "1827_uniform_radius_covering", "UniformRadiusCovering", "732_probability_142", "pts",
     ["一様半径被覆", "全空間球", "サイズ"], ["定義", "サイズ"], [r"N_u(r,\epsilon)", r"N_u\lesssim (r/\epsilon)^d"], r"N_u\lesssim (r/\epsilon)^d"),
    (1828, "一様半径パッキング", "1828_uniform_radius_packing", "UniformRadiusPacking", "732_probability_142", "pts",
     ["一様半径パッキング", "全空間分離", "サイズ"], ["定義", "サイズ"], [r"M_u(r,\epsilon)", r"M_u\lesssim (r/\epsilon)^d"], r"M_u\lesssim (r/\epsilon)^d"),
    (1829, "二分ヒープ細分", "1829_binheap_refine", "BinHeapRefine", "733_combinatorics_141", "nums",
     ["二分ヒープ", "ヒープ順序", "細分"], ["定義", "細分"], [r"BH_n", r"BH(n,k)"], r"BH(n,k)", [1, 1, 2, 3, 8]),
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
        clean_dtex, clean_final = list(dtex), final
        # scrub English-ish mathrm for arcs/mult
        if num == 1794:
            clean_dtex = [r"m_x", r"m_x\ge m"]; clean_final = r"m_x\ge m"
        elif num == 1795:
            clean_dtex = [r"m_x", r"m_x\ge m"]; clean_final = r"m_x\ge m"
        elif num in (1800, 1801, 1802, 1812, 1813, 1814, 1824, 1825, 1826):
            # replace mathrm{arc} with arc symbol-free form
            clean_dtex = [dtex[0], dtex[1].replace(r"\mathrm{arc}", r"a").replace(r"\overset{\frown}{AB}/r", r"\ell_a/r")]
            clean_final = final.replace(r"\mathrm{arc}", r"a").replace(r"\ell_{\mathrm{arc}}/r", r"\ell_a/r")
            if num == 1800:
                clean_dtex = [r"I", r"\ell_a/r"]; clean_final = r"\ell_a/r"
            elif num == 1801:
                clean_dtex = [r"I_a", r"\ell_a/r_a"]; clean_final = r"\ell_a/r_a"
            elif num == 1802:
                clean_dtex = [r"O", r"\ell_a/R"]; clean_final = r"\ell_a/R"
            elif num == 1812:
                clean_dtex = [r"H", r"\ell_a/R"]; clean_final = r"\ell_a/R"
            elif num == 1813:
                clean_dtex = [r"G", r"\ell_a/\ell"]; clean_final = r"\ell_a/\ell"
            elif num == 1814:
                clean_dtex = [r"N", r"\ell_a/R_N"]; clean_final = r"\ell_a/R_N"
            elif num == 1824:
                clean_dtex = [r"I", r"\ell_{a,s}/r"]; clean_final = r"\ell_{a,s}/r"
            elif num == 1825:
                clean_dtex = [r"I_a", r"\ell_{a,s}/r_a"]; clean_final = r"\ell_{a,s}/r_a"
            elif num == 1826:
                clean_dtex = [r"O", r"\ell_{a,s}/R"]; clean_final = r"\ell_{a,s}/R"
        path = f"project/math/{season}/{slug}/scene.py"
        code = mk(kind, cls, num, title, notes, dnotes, clean_dtex, clean_final, vals)
        folder = ROOT / "project/math" / season / slug
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "scene.py").write_text(code, encoding="utf-8")
        (folder / "storyboard.md").write_text(story(num, title), encoding="utf-8")
        ast.parse(code)
        created.append((num, title, path, cls))
        titles.add(title)

    cp = ROOT / "project/math/catalog.py"
    text = cp.read_text(encoding="utf-8")
    assert "VIDEOS_1794_1805" not in text

    def block(name, items):
        lines = [f"\n\n{name}: tuple[Video, ...] = ("]
        for num, title, path, cls in items:
            lines.append(f'    Video({num}, "{title}", "{path}", "{cls}"),')
        lines.append(")")
        return "\n".join(lines)

    cp.write_text(
        text.rstrip()
        + block("VIDEOS_1794_1805", created[:12])
        + block("VIDEOS_1806_1817", created[12:24])
        + block("VIDEOS_1818_1829", created[24:])
        + "\n",
        encoding="utf-8",
    )

    tp = ROOT / "tests/test_catalog.py"
    t = tp.read_text(encoding="utf-8")
    if "VIDEOS_1794_1805" not in t:
        t = t.replace(
            "VIDEOS_1782_1793 = _catalog.VIDEOS_1782_1793\n",
            "VIDEOS_1782_1793 = _catalog.VIDEOS_1782_1793\n"
            "VIDEOS_1794_1805 = _catalog.VIDEOS_1794_1805\n"
            "VIDEOS_1806_1817 = _catalog.VIDEOS_1806_1817\n"
            "VIDEOS_1818_1829 = _catalog.VIDEOS_1818_1829\n",
        )
        insert = """
    def test_numbers_are_1794_to_1805(self):
        nums = [v.number for v in VIDEOS_1794_1805]
        self.assertEqual(nums, list(range(1794, 1806)))


    def test_numbers_are_1806_to_1817(self):
        nums = [v.number for v in VIDEOS_1806_1817]
        self.assertEqual(nums, list(range(1806, 1818)))


    def test_numbers_are_1818_to_1829(self):
        nums = [v.number for v in VIDEOS_1818_1829]
        self.assertEqual(nums, list(range(1818, 1830)))

"""
        t = t.replace(
            "    def test_each_scene_file_defines_the_class(self):",
            insert + "    def test_each_scene_file_defines_the_class(self):",
        )
        t = t.replace(
            "            *VIDEOS_1782_1793,\n        ):",
            "            *VIDEOS_1782_1793,\n"
            "            *VIDEOS_1794_1805,\n"
            "            *VIDEOS_1806_1817,\n"
            "            *VIDEOS_1818_1829,\n"
            "        ):",
        )
        tp.write_text(t, encoding="utf-8")

    plan = ROOT / "project/math/PLAN.md"
    p = plan.read_text(encoding="utf-8")
    if "#1794" not in p:
        extra = "\n\n## 導出つき続き（#1794–#1805）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[:12]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#1806–#1817）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[12:24]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#1818–#1829）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[24:]:
            extra += f"| {num} | {title} | 実装 |\n"
        p = p.replace("## 1 本の作業フロー", extra + "\n## 1 本の作業フロー")
        plan.write_text(p, encoding="utf-8")

    print("created", created[0][0], "-", created[-1][0])


if __name__ == "__main__":
    main()
