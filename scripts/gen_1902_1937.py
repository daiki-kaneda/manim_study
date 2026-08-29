#!/usr/bin/env python3
"""Generate #1902–#1937 with derive/proof beats."""
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
    (1902, "相対ログアルバネーゼ対", "1902_rel_log_albanese", "RelLogAlbanese", "764_analysis_151", "box",
     ["相対ログアルバネーゼ", "相対射", "ファイバー"], ["定義", "射"], [r"alb/S", r"alb:X\to_S Alb"], r"alb:X\to_S Alb"),
    (1903, "ログクレモナ対", "1903_log_cremona_pair", "LogCremonaPair", "764_analysis_151", "box",
     ["ログクレモナ", "双有理変換", "境界"], ["定義", "変換"], [r"\sigma", r"\sigma:\mathbb{P}\dashrightarrow\mathbb{P}"], r"\sigma:\mathbb{P}^2\dashrightarrow\mathbb{P}^2"),
    (1904, "相対ログクレモナ対", "1904_rel_log_cremona", "RelLogCremona", "764_analysis_151", "box",
     ["相対ログクレモナ", "相対変換", "ファイバー"], ["定義", "変換"], [r"\sigma/S", r"\sigma:\mathbb{P}\dashrightarrow_S\mathbb{P}"], r"\sigma:\mathbb{P}\dashrightarrow_S\mathbb{P}"),
    (1905, "MuonBoundSoftClip", "1905_muonboundsoftclip", "MuonBoundSoftClip", "765_linear_151", "opt",
     ["Muon境界軟クリップ", "直交更新", "三重"], ["核", "軟境界"], [r"U^\top U=I", r"\eta\leftarrow\mathrm{clip}(\mathrm{soft}(\eta))"], r"\eta\leftarrow\mathrm{clip}(\mathrm{soft}(\eta))\in[L,U]"),
    (1906, "SamBoundClip", "1906_samboundclip", "SamBoundClip", "765_linear_151", "opt",
     ["SAM境界クリップ", "鋭度", "枠"], ["核", "境界クリップ"], [r"\epsilon\leftarrow\rho g/\|g\|", r"\rho\leftarrow\mathrm{clip}(\rho)"], r"\rho\leftarrow\mathrm{clip}(\rho)\in[L,U]"),
    (1907, "AdaFactorBoundClip", "1907_adafactorboundclip", "AdaFactorBoundClip", "765_linear_151", "opt",
     ["AdaFactor境界クリップ", "因子化", "枠"], ["核", "境界クリップ"], [r"R_{ij}C_{ij}\approx G_{ij}^2", r"\eta\leftarrow\mathrm{clip}(\eta)"], r"\eta\leftarrow\mathrm{clip}(\eta)\in[L,U]"),
    (1908, "垂心フォイエル半径比", "1908_h_feuer_radius", "HFeuerRadius", "766_geometry_151", "tri",
     ["垂心フォイエル半径", "九点円半径", "比"], ["配置", "比"], [r"H", r"R/R_N"], r"R/R_N=2"),
    (1909, "重心フォイエル半径比", "1909_g_feuer_radius", "GFeuerRadius", "766_geometry_151", "tri",
     ["重心フォイエル半径", "九点円半径", "比"], ["配置", "比"], [r"G", r"\ell/R_N"], r"\ell/R_N"),
    (1910, "九点フォイエル半径比", "1910_n_feuer_radius", "NFeuerRadius", "766_geometry_151", "tri",
     ["九点円半径比", "半径", "比"], ["配置", "比"], [r"N", r"R_N=R/2"], r"R_N=R/2"),
    (1911, "経験スケールエントロピー", "1911_emp_scale_entropy", "EmpScaleEntropy", "767_probability_149", "pts",
     ["経験スケールエントロピー", "データ半径", "対数"], ["定義", "依存"], [r"H_n(r,\epsilon)", r"H_n\propto r^{\alpha}"], r"H_n\propto r^{\alpha}"),
    (1912, "半径スケール複雑度", "1912_radius_scale_comp", "RadiusScaleComp", "767_probability_149", "pts",
     ["半径スケール複雑度", "スケール上界", "依存"], ["定義", "上界"], [r"\mathfrak{C}(r)", r"\mathfrak{C}(r)\le C r^{\alpha}"], r"\mathfrak{C}(r)\le C r^{\alpha}"),
    (1913, "三分ヒープ細分", "1913_ternary_heap_refine", "TernaryHeapRefine", "768_combinatorics_148", "nums",
     ["三分ヒープ", "三分ヒープ順", "細分"], ["定義", "細分"], [r"TH_n", r"TH(n,k)"], r"TH(n,k)", [1, 1, 2, 4, 10]),
    (1914, "ログカラビ対", "1914_log_calabi_pair", "LogCalabiPair", "769_analysis_152", "box",
     ["ログカラビ", "リッチ平坦", "境界"], ["定義", "条件"], [r"Ric(\omega)", r"Ric(\omega)=0"], r"Ric(\omega)=0"),
    (1915, "相対ログカラビ対", "1915_rel_log_calabi", "RelLogCalabi", "769_analysis_152", "box",
     ["相対ログカラビ", "相対リッチ", "ファイバー"], ["定義", "条件"], [r"Ric(\omega)/S", r"Ric(\omega_F)=0"], r"Ric(\omega_F)=0"),
    (1916, "ログカラビヤウ対", "1916_log_cy_pair", "LogCyPair", "769_analysis_152", "box",
     ["ログカラビヤウ", "K自明", "境界"], ["定義", "条件"], [r"K+D", r"K+D\equiv 0"], r"K+D\equiv 0"),
    (1917, "NAdamBoundClip", "1917_nadamboundclip", "NAdamBoundClip", "770_linear_152", "opt",
     ["NAdam境界クリップ", "ネステロフ", "枠"], ["核", "境界クリップ"], [r"m\leftarrow\beta m+(1-\beta)g", r"\eta\leftarrow\mathrm{clip}(\eta)"], r"\eta\leftarrow\mathrm{clip}(\eta)\in[L,U]"),
    (1918, "LARSBoundClip", "1918_larsboundclip", "LARSBoundClip", "770_linear_152", "opt",
     ["LARS境界クリップ", "層正規化", "枠"], ["核", "境界クリップ"], [r"\eta\leftarrow\|w\|/\|g\|", r"\eta\leftarrow\mathrm{clip}(\eta)"], r"\eta\leftarrow\mathrm{clip}(\eta)\in[L,U]"),
    (1919, "LionWBoundHard", "1919_lionwboundhard", "LionWBoundHard", "770_linear_152", "opt",
     ["LionW境界硬閾", "減衰符号", "枠剪定"], ["核", "硬境界"], [r"x\leftarrow x-\eta\mathrm{sign}(m)-\lambda x", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{clip}(\eta))"),
    (1920, "内心類似フォイエル半径比", "1920_in_sym_feuer_radius", "InSymFeuerRadius", "771_geometry_152", "tri",
     ["内心類似半径", "九点円半径", "比"], ["配置", "比"], [r"I", r"r/R_{N,s}"], r"r/R_{N,s}"),
    (1921, "傍心類似フォイエル半径比", "1921_ex_sym_feuer_radius", "ExSymFeuerRadius", "771_geometry_152", "tri",
     ["傍心類似半径", "九点円半径", "比"], ["配置", "比"], [r"I_a", r"r_a/R_{N,s}"], r"r_a/R_{N,s}"),
    (1922, "外心類似フォイエル半径比", "1922_o_sym_feuer_radius", "OSymFeuerRadius", "771_geometry_152", "tri",
     ["外心類似半径", "九点円半径", "比"], ["配置", "比"], [r"O", r"R/R_{N,s}"], r"R/R_{N,s}"),
    (1923, "標本スケール被覆", "1923_sample_scale_covering", "SampleScaleCovering", "772_probability_150", "pts",
     ["標本スケール被覆", "有限標本半径", "サイズ"], ["定義", "サイズ"], [r"N_n(r,\epsilon)", r"N_n\lesssim(r/\epsilon)^d"], r"N_n\lesssim(r/\epsilon)^d"),
    (1924, "標本スケールパッキング", "1924_sample_scale_packing", "SampleScalePacking", "772_probability_150", "pts",
     ["標本スケールパッキング", "有限標本半径", "分離"], ["定義", "サイズ"], [r"M_n(r,\epsilon)", r"M_n\lesssim(r/\epsilon)^d"], r"M_n\lesssim(r/\epsilon)^d"),
    (1925, "平面三分木細分", "1925_plane_ternary_refine", "PlaneTernaryRefine", "773_combinatorics_149", "nums",
     ["平面三分木", "三分岐順序", "細分"], ["定義", "細分"], [r"PT_n", r"PT(n,k)"], r"PT(n,k)", [1, 1, 3, 12, 55]),
    (1926, "相対ログカラビヤウ対", "1926_rel_log_cy", "RelLogCy", "774_analysis_153", "box",
     ["相対ログカラビヤウ", "相対K自明", "ファイバー"], ["定義", "条件"], [r"K+D", r"(K+D)|_F\equiv 0"], r"(K+D)|_F\equiv 0"),
    (1927, "ログ一般型対", "1927_log_general_type", "LogGeneralType", "774_analysis_153", "box",
     ["ログ一般型", "ビッグ標準", "境界"], ["定義", "判定"], [r"K+D", r"K+D\in\mathrm{Big}"], r"vol(K+D)>0"),
    (1928, "相対ログ一般型対", "1928_rel_log_general_type", "RelLogGeneralType", "774_analysis_153", "box",
     ["相対ログ一般型", "相対ビッグ", "ファイバー"], ["定義", "判定"], [r"K+D", r"vol_{X/S}(K+D)>0"], r"vol_{X/S}(K+D)>0"),
    (1929, "SophiaWBoundHard", "1929_sophiawboundhard", "SophiaWBoundHard", "775_linear_153", "opt",
     ["SophiaW境界硬閾", "減衰二階", "枠剪定"], ["核", "硬境界"], [r"\theta\leftarrow\theta-\eta m/\hat H-\lambda\theta", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{clip}(\eta))"),
    (1930, "LookaheadBoundClip", "1930_lookaheadboundclip", "LookaheadBoundClip", "775_linear_153", "opt",
     ["Lookahead境界クリップ", "外側平均", "枠"], ["核", "境界クリップ"], [r"x\leftarrow x+\alpha(y-x)", r"\eta\leftarrow\mathrm{clip}(\eta)"], r"\eta\leftarrow\mathrm{clip}(\eta)\in[L,U]"),
    (1931, "ProdigySoftBoundClip", "1931_prodigysoftboundclip", "ProdigySoftBoundClip", "775_linear_153", "opt",
     ["Prodigy軟境界クリップ", "D推定", "三重"], ["核", "軟境界"], [r"d\leftarrow\|g\|", r"\eta\leftarrow\mathrm{clip}(\mathrm{soft}(\eta))"], r"\eta\leftarrow\mathrm{clip}(\mathrm{soft}(\eta))\in[L,U]"),
    (1932, "垂心類似フォイエル半径比", "1932_h_sym_feuer_radius", "HSymFeuerRadius", "776_geometry_153", "tri",
     ["垂心類似半径", "九点円半径", "比"], ["配置", "比"], [r"H", r"R/R_{N,s}"], r"R/R_{N,s}"),
    (1933, "重心類似フォイエル半径比", "1933_g_sym_feuer_radius", "GSymFeuerRadius", "776_geometry_153", "tri",
     ["重心類似半径", "九点円半径", "比"], ["配置", "比"], [r"G", r"\ell/R_{N,s}"], r"\ell/R_{N,s}"),
    (1934, "九点類似フォイエル半径比", "1934_n_sym_feuer_radius", "NSymFeuerRadius", "776_geometry_153", "tri",
     ["九点円類似半径", "半径", "比"], ["配置", "比"], [r"N", r"R_{N,s}"], r"R_{N,s}=R/2"),
    (1935, "局所スケールエントロピー再訪", "1935_local_scale_entropy_rev", "LocalScaleEntropyRev", "777_probability_151", "pts",
     ["局所スケールエントロピー", "半径球", "再訪"], ["定義", "依存"], [r"H(B,r,\epsilon)", r"H\propto r^{\alpha}"], r"H\propto r^{\alpha}"),
    (1936, "一様スケールエントロピー再訪", "1936_uniform_scale_entropy_rev", "UniformScaleEntropyRev", "777_probability_151", "pts",
     ["一様スケールエントロピー", "全空間", "再訪"], ["定義", "依存"], [r"H_u(r,\epsilon)", r"H_u\propto r^{\alpha}"], r"H_u\propto r^{\alpha}"),
    (1937, "増加ヒープ細分", "1937_inc_heap_refine", "IncHeapRefine", "778_combinatorics_150", "nums",
     ["増加ヒープ", "ヒープ増加", "細分"], ["定義", "細分"], [r"IH_n", r"IH(n,k)"], r"IH(n,k)", [1, 1, 2, 3, 8]),
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
        if num == 1927:
            clean_dtex = [r"K+D", r"vol(K+D)>0"]
            clean_final = r"vol(K+D)>0"
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
    assert "VIDEOS_1902_1913" not in text

    def block(name, items):
        lines = [f"\n\n{name}: tuple[Video, ...] = ("]
        for num, title, path, cls in items:
            lines.append(f'    Video({num}, "{title}", "{path}", "{cls}"),')
        lines.append(")")
        return "\n".join(lines)

    cp.write_text(
        text.rstrip()
        + block("VIDEOS_1902_1913", created[:12])
        + block("VIDEOS_1914_1925", created[12:24])
        + block("VIDEOS_1926_1937", created[24:])
        + "\n",
        encoding="utf-8",
    )

    tp = ROOT / "tests/test_catalog.py"
    t = tp.read_text(encoding="utf-8")
    if "VIDEOS_1902_1913" not in t:
        t = t.replace(
            "VIDEOS_1890_1901 = _catalog.VIDEOS_1890_1901\n",
            "VIDEOS_1890_1901 = _catalog.VIDEOS_1890_1901\n"
            "VIDEOS_1902_1913 = _catalog.VIDEOS_1902_1913\n"
            "VIDEOS_1914_1925 = _catalog.VIDEOS_1914_1925\n"
            "VIDEOS_1926_1937 = _catalog.VIDEOS_1926_1937\n",
        )
        insert = """
    def test_numbers_are_1902_to_1913(self):
        nums = [v.number for v in VIDEOS_1902_1913]
        self.assertEqual(nums, list(range(1902, 1914)))


    def test_numbers_are_1914_to_1925(self):
        nums = [v.number for v in VIDEOS_1914_1925]
        self.assertEqual(nums, list(range(1914, 1926)))


    def test_numbers_are_1926_to_1937(self):
        nums = [v.number for v in VIDEOS_1926_1937]
        self.assertEqual(nums, list(range(1926, 1938)))

"""
        t = t.replace(
            "    def test_each_scene_file_defines_the_class(self):",
            insert + "    def test_each_scene_file_defines_the_class(self):",
        )
        t = t.replace(
            "            *VIDEOS_1890_1901,\n        ):",
            "            *VIDEOS_1890_1901,\n"
            "            *VIDEOS_1902_1913,\n"
            "            *VIDEOS_1914_1925,\n"
            "            *VIDEOS_1926_1937,\n"
            "        ):",
        )
        tp.write_text(t, encoding="utf-8")

    plan = ROOT / "project/math/PLAN.md"
    p = plan.read_text(encoding="utf-8")
    if "#1902" not in p:
        extra = "\n\n## 導出つき続き（#1902–#1913）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[:12]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#1914–#1925）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[12:24]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#1926–#1937）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[24:]:
            extra += f"| {num} | {title} | 実装 |\n"
        p = p.replace("## 1 本の作業フロー", extra + "\n## 1 本の作業フロー")
        plan.write_text(p, encoding="utf-8")

    print("created", created[0][0], "-", created[-1][0])


if __name__ == "__main__":
    main()
