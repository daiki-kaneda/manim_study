#!/usr/bin/env python3
"""Generate #1830–#1865 with derive/proof beats."""
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
    (1830, "相対ログ自己交対", "1830_rel_log_self_int", "RelLogSelfInt", "734_analysis_145", "box",
     ["相対ログ自己交", "相対自己交差", "数値"], ["定義", "値"], [r"D^2/S", r"D^2=(D\cdot D)_S"], r"D^2"),
    (1831, "ログ交多項式対", "1831_log_int_poly_pair", "LogIntPolyPair", "734_analysis_145", "box",
     ["ログ交多項式", "交差展開", "係数"], ["定義", "展開"], [r"(tD)^n", r"(tD)^n=\sum a_k t^k"], r"(tD)^n=\sum a_k t^k"),
    (1832, "相対ログ交多項式対", "1832_rel_log_int_poly", "RelLogIntPoly", "734_analysis_145", "box",
     ["相対ログ交多項式", "相対交差", "係数"], ["定義", "展開"], [r"(tD)^n_S", r"(tD)^n=\sum a_k t^k"], r"(tD)^n=\sum a_k t^k"),
    (1833, "AdamWHardBound", "1833_adamwhardbound", "AdamWHardBound", "735_linear_145", "opt",
     ["AdamW硬境界", "減衰つき", "枠剪定"], ["核", "硬境界"], [r"u\leftarrow\hat m/\sqrt{\hat v}", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{clip}(\eta))"),
    (1834, "LionSoftBoundClip", "1834_lionsoftboundclip", "LionSoftBoundClip", "735_linear_145", "opt",
     ["Lion軟境界クリップ", "符号更新", "三重"], ["核", "軟境界"], [r"x\leftarrow x-\eta\mathrm{sign}(m)", r"\eta\leftarrow\mathrm{clip}(\mathrm{soft}(\eta))"], r"\eta\leftarrow\mathrm{clip}(\mathrm{soft}(\eta))\in[L,U]"),
    (1835, "SophiaSoftBoundClip", "1835_sophiasoftboundclip", "SophiaSoftBoundClip", "735_linear_145", "opt",
     ["Sophia軟境界クリップ", "二階情報", "三重"], ["核", "軟境界"], [r"\theta\leftarrow\theta-\eta m/\hat H", r"\eta\leftarrow\mathrm{clip}(\mathrm{soft}(\eta))"], r"\eta\leftarrow\mathrm{clip}(\mathrm{soft}(\eta))\in[L,U]"),
    (1836, "垂心類似フォイエル弧比", "1836_h_sym_feuer_arc", "HSymFeuerArc", "736_geometry_145", "tri",
     ["垂心類似弧", "九点円弧", "比"], ["配置", "比"], [r"H", r"\ell_{a,s}/R"], r"\ell_{a,s}/R"),
    (1837, "重心類似フォイエル弧比", "1837_g_sym_feuer_arc", "GSymFeuerArc", "736_geometry_145", "tri",
     ["重心類似弧", "九点円弧", "比"], ["配置", "比"], [r"G", r"\ell_{a,s}/\ell"], r"\ell_{a,s}/\ell"),
    (1838, "九点類似フォイエル弧比", "1838_n_sym_feuer_arc", "NSymFeuerArc", "736_geometry_145", "tri",
     ["九点円類似弧", "弧", "比"], ["配置", "比"], [r"N", r"\ell_{a,s}/R_N"], r"\ell_{a,s}/R_N"),
    (1839, "局所一様被覆", "1839_local_uniform_covering", "LocalUniformCovering", "737_probability_143", "pts",
     ["局所一様被覆", "半径球一様", "サイズ"], ["定義", "サイズ"], [r"N_{\mathrm{loc},u}(\epsilon)", r"N_{\mathrm{loc},u}\le N_u"], r"N_{\mathrm{loc},u}\le N_u"),
    (1840, "局所一様パッキング", "1840_local_uniform_packing", "LocalUniformPacking", "737_probability_143", "pts",
     ["局所一様パッキング", "半径球一様", "分離"], ["定義", "サイズ"], [r"M_{\mathrm{loc},u}(\epsilon)", r"M_{\mathrm{loc},u}\le M_u"], r"M_{\mathrm{loc},u}\le M_u"),
    (1841, "三分木細分", "1841_ternary_tree_refine", "TernaryTreeRefine", "738_combinatorics_142", "nums",
     ["三分木", "三分岐", "細分"], ["定義", "細分"], [r"T_n^{(3)}", r"T(n,k;3)"], r"T(n,k;3)", [1, 1, 3, 12, 55]),
    (1842, "ログ数値類対", "1842_log_num_class_pair", "LogNumClassPair", "739_analysis_146", "box",
     ["ログ数値類", "数値同値", "類群"], ["定義", "類"], [r"D\equiv_{\mathrm{num}} D'", r"[D]_{\mathrm{num}}"], r"[D]"),
    (1843, "相対ログ数値類対", "1843_rel_log_num_class", "RelLogNumClass", "739_analysis_146", "box",
     ["相対ログ数値類", "相対数値", "類群"], ["定義", "類"], [r"D\equiv_S D'", r"[D]_S"], r"[D]_S"),
    (1844, "ログピカール対", "1844_log_picard_pair", "LogPicardPair", "739_analysis_146", "box",
     ["ログピカール", "直線束", "階数"], ["定義", "階数"], [r"\mathrm{Pic}(X)", r"\rho=\mathrm{rank}\,\mathrm{Pic}"], r"\rho(X)"),
    (1845, "ApolloSoftBound", "1845_apollosoftbound", "ApolloSoftBound", "740_linear_146", "opt",
     ["Apollo軟境界", "準ニュートン", "平滑枠"], ["核", "軟境界"], [r"B\leftarrow B+uu^\top", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{clip}(\eta))"),
    (1846, "MuonHardBound", "1846_muonhardbound", "MuonHardBound", "740_linear_146", "opt",
     ["Muon硬境界", "直交更新", "枠剪定"], ["核", "硬境界"], [r"U^\top U=I", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{clip}(\eta))"),
    (1847, "SamSoftHardBound", "1847_samsofthardbound", "SamSoftHardBound", "740_linear_146", "opt",
     ["SAM軟硬境界", "鋭度", "枠二段"], ["軟", "硬"], [r"\rho\leftarrow\mathrm{soft}(\rho)", r"\rho\leftarrow\mathrm{hard}(\rho)\in[L,U]"], r"\rho\leftarrow\mathrm{hard}(\mathrm{soft}(\mathrm{clip}(\rho)))"),
    (1848, "内心フォイエル中心比", "1848_in_feuer_center", "InFeuerCenter", "741_geometry_146", "tri",
     ["内心フォイエル中心", "九点円心", "比"], ["配置", "比"], [r"I", r"IN/r"], r"IN/r"),
    (1849, "傍心フォイエル中心比", "1849_ex_feuer_center", "ExFeuerCenter", "741_geometry_146", "tri",
     ["傍心フォイエル中心", "九点円心", "比"], ["配置", "比"], [r"I_a", r"I_aN/r_a"], r"I_aN/r_a"),
    (1850, "外心フォイエル中心比", "1850_o_feuer_center", "OFeuerCenter", "741_geometry_146", "tri",
     ["外心フォイエル中心", "九点円心", "比"], ["配置", "比"], [r"O", r"ON/R"], r"ON/R"),
    (1851, "経験一様被覆", "1851_emp_uniform_covering", "EmpUniformCovering", "742_probability_144", "pts",
     ["経験一様被覆", "データ一様", "サイズ"], ["定義", "サイズ"], [r"N_{n,u}(\epsilon)", r"N_{n,u}\le N_u"], r"N_{n,u}\le N_u"),
    (1852, "経験一様パッキング", "1852_emp_uniform_packing", "EmpUniformPacking", "742_probability_144", "pts",
     ["経験一様パッキング", "データ一様", "分離"], ["定義", "サイズ"], [r"M_{n,u}(\epsilon)", r"M_{n,u}\le M_u"], r"M_{n,u}\le M_u"),
    (1853, "平面増加木細分", "1853_plane_inc_tree_refine", "PlaneIncTreeRefine", "743_combinatorics_143", "nums",
     ["平面増加木", "順序増加", "細分"], ["定義", "細分"], [r"PI_n", r"PI(n,k)"], r"PI(n,k)", [1, 1, 3, 13, 71]),
    (1854, "相対ログピカール対", "1854_rel_log_picard", "RelLogPicard", "744_analysis_147", "box",
     ["相対ログピカール", "相対直線束", "階数"], ["定義", "階数"], [r"\mathrm{Pic}(X/S)", r"\rho(X/S)"], r"\rho(X/S)"),
    (1855, "ログネロンセベリ対", "1855_log_ns_pair", "LogNsPair", "744_analysis_147", "box",
     ["ログネロンセベリ", "数値ピカール", "階数"], ["定義", "階数"], [r"NS(X)", r"\rho=\mathrm{rank}\,NS"], r"\rho(X)"),
    (1856, "相対ログネロンセベリ対", "1856_rel_log_ns", "RelLogNs", "744_analysis_147", "box",
     ["相対ログネロンセベリ", "相対数値", "階数"], ["定義", "階数"], [r"NS(X/S)", r"\rho(X/S)"], r"\rho(X/S)"),
    (1857, "LARSHardBound", "1857_larshardbound", "LARSHardBound", "745_linear_147", "opt",
     ["LARS硬境界", "層正規化", "枠剪定"], ["核", "硬境界"], [r"\eta\leftarrow\|w\|/\|g\|", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{clip}(\eta))"),
    (1858, "AdaFactorHardBound", "1858_adafactorhardbound", "AdaFactorHardBound", "745_linear_147", "opt",
     ["AdaFactor硬境界", "因子化", "枠剪定"], ["核", "硬境界"], [r"R_{ij}C_{ij}\approx G_{ij}^2", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{clip}(\eta))"),
    (1859, "NAdamBoundSoftClip", "1859_nadamboundsoftclip", "NAdamBoundSoftClip", "745_linear_147", "opt",
     ["NAdam境界軟クリップ", "ネステロフ", "三重"], ["核", "軟境界"], [r"m\leftarrow\beta m+(1-\beta)g", r"\eta\leftarrow\mathrm{clip}(\mathrm{soft}(\eta))"], r"\eta\leftarrow\mathrm{clip}(\mathrm{soft}(\eta))\in[L,U]"),
    (1860, "垂心フォイエル中心比", "1860_h_feuer_center", "HFeuerCenter", "746_geometry_147", "tri",
     ["垂心フォイエル中心", "九点円心", "比"], ["配置", "比"], [r"H", r"HN/R"], r"HN/R"),
    (1861, "重心フォイエル中心比", "1861_g_feuer_center", "GFeuerCenter", "746_geometry_147", "tri",
     ["重心フォイエル中心", "九点円心", "比"], ["配置", "比"], [r"G", r"GN/\ell"], r"GN/\ell"),
    (1862, "九点フォイエル中心比", "1862_n_feuer_center", "NFeuerCenter", "746_geometry_147", "tri",
     ["九点円中心比", "中心", "比"], ["配置", "比"], [r"N", r"R_N=R/2"], r"R_N=R/2"),
    (1863, "スケール一様エントロピー", "1863_scale_uniform_entropy", "ScaleUniformEntropy", "747_probability_145", "pts",
     ["スケール一様エントロピー", "半径一様", "対数"], ["定義", "依存"], [r"H_u(r,\epsilon)", r"H_u\propto r^{\alpha}"], r"H_u\propto r^{\alpha}"),
    (1864, "半径一様複雑度", "1864_radius_uniform_comp", "RadiusUniformComp", "747_probability_145", "pts",
     ["半径一様複雑度", "一様球", "上界"], ["定義", "上界"], [r"\mathfrak{C}_u(r)", r"\mathfrak{C}_u(r)\le C r^{\alpha}"], r"\mathfrak{C}_u(r)\le C r^{\alpha}"),
    (1865, "順序森細分", "1865_ordered_forest_refine", "OrderedForestRefine", "748_combinatorics_144", "nums",
     ["順序森", "平面順序", "細分"], ["定義", "細分"], [r"OF_n", r"OF(n,k)"], r"OF(n,k)", [1, 2, 7, 38, 291]),
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
        if num == 1842:
            clean_dtex = [r"D\equiv D'", r"[D]"]; clean_final = r"[D]"
        elif num == 1844:
            clean_dtex = [r"\mathrm{Pic}", r"\rho"]; clean_final = r"\rho(X)"
            clean_dtex = [r"Pic", r"\rho"]; clean_final = r"\rho(X)"
        elif num == 1854:
            clean_dtex = [r"Pic(X/S)", r"\rho(X/S)"]; clean_final = r"\rho(X/S)"
        elif num == 1855:
            clean_dtex = [r"NS(X)", r"\rho"]; clean_final = r"\rho(X)"
        elif num in (1839, 1840):
            clean_dtex = [dtex[0].replace(r"\mathrm{loc},u", r"lu"), dtex[1].replace(r"\mathrm{loc},u", r"lu")]
            clean_final = final.replace(r"\mathrm{loc},u", r"lu")
            if num == 1839:
                clean_dtex = [r"N_{lu}(\epsilon)", r"N_{lu}\le N_u"]; clean_final = r"N_{lu}\le N_u"
            else:
                clean_dtex = [r"M_{lu}(\epsilon)", r"M_{lu}\le M_u"]; clean_final = r"M_{lu}\le M_u"
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
    assert "VIDEOS_1830_1841" not in text

    def block(name, items):
        lines = [f"\n\n{name}: tuple[Video, ...] = ("]
        for num, title, path, cls in items:
            lines.append(f'    Video({num}, "{title}", "{path}", "{cls}"),')
        lines.append(")")
        return "\n".join(lines)

    cp.write_text(
        text.rstrip()
        + block("VIDEOS_1830_1841", created[:12])
        + block("VIDEOS_1842_1853", created[12:24])
        + block("VIDEOS_1854_1865", created[24:])
        + "\n",
        encoding="utf-8",
    )

    tp = ROOT / "tests/test_catalog.py"
    t = tp.read_text(encoding="utf-8")
    if "VIDEOS_1830_1841" not in t:
        t = t.replace(
            "VIDEOS_1818_1829 = _catalog.VIDEOS_1818_1829\n",
            "VIDEOS_1818_1829 = _catalog.VIDEOS_1818_1829\n"
            "VIDEOS_1830_1841 = _catalog.VIDEOS_1830_1841\n"
            "VIDEOS_1842_1853 = _catalog.VIDEOS_1842_1853\n"
            "VIDEOS_1854_1865 = _catalog.VIDEOS_1854_1865\n",
        )
        insert = """
    def test_numbers_are_1830_to_1841(self):
        nums = [v.number for v in VIDEOS_1830_1841]
        self.assertEqual(nums, list(range(1830, 1842)))


    def test_numbers_are_1842_to_1853(self):
        nums = [v.number for v in VIDEOS_1842_1853]
        self.assertEqual(nums, list(range(1842, 1854)))


    def test_numbers_are_1854_to_1865(self):
        nums = [v.number for v in VIDEOS_1854_1865]
        self.assertEqual(nums, list(range(1854, 1866)))

"""
        t = t.replace(
            "    def test_each_scene_file_defines_the_class(self):",
            insert + "    def test_each_scene_file_defines_the_class(self):",
        )
        t = t.replace(
            "            *VIDEOS_1818_1829,\n        ):",
            "            *VIDEOS_1818_1829,\n"
            "            *VIDEOS_1830_1841,\n"
            "            *VIDEOS_1842_1853,\n"
            "            *VIDEOS_1854_1865,\n"
            "        ):",
        )
        tp.write_text(t, encoding="utf-8")

    plan = ROOT / "project/math/PLAN.md"
    p = plan.read_text(encoding="utf-8")
    if "#1830" not in p:
        extra = "\n\n## 導出つき続き（#1830–#1841）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[:12]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#1842–#1853）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[12:24]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#1854–#1865）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[24:]:
            extra += f"| {num} | {title} | 実装 |\n"
        p = p.replace("## 1 本の作業フロー", extra + "\n## 1 本の作業フロー")
        plan.write_text(p, encoding="utf-8")

    print("created", created[0][0], "-", created[-1][0])


if __name__ == "__main__":
    main()
