#!/usr/bin/env python3
"""Generate #1974–#2009 with derive/proof beats."""
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
    (1974, "相対ログ随伴ネフ対", "1974_rel_log_adj_nef", "RelLogAdjNef", "794_analysis_157", "box",
     ["相対ログ随伴ネフ", "相対交差", "ファイバー"], ["定義", "判定"], [r"(K+D).C", r"(K+D).C\ge 0"], r"(K+D).C\ge 0"),
    (1975, "ログ随伴ビッグ対", "1975_log_adj_big", "LogAdjBig", "794_analysis_157", "box",
     ["ログ随伴ビッグ", "体積正", "境界"], ["体積", "判定"], [r"vol(K+D)", r"vol(K+D)>0"], r"vol(K+D)>0"),
    (1976, "相対ログ随伴ビッグ対", "1976_rel_log_adj_big", "RelLogAdjBig", "794_analysis_157", "box",
     ["相対ログ随伴ビッグ", "相対体積", "ファイバー"], ["体積", "判定"], [r"vol_{X/S}(K+D)", r"vol_{X/S}(K+D)>0"], r"vol_{X/S}(K+D)>0"),
    (1977, "LionWBoundClip", "1977_lionwboundclip", "LionWBoundClip", "795_linear_157", "opt",
     ["LionW境界クリップ", "減衰符号", "枠"], ["核", "境界クリップ"], [r"x\leftarrow x-\eta\mathrm{sign}(m)-\lambda x", r"\eta\leftarrow\mathrm{clip}(\eta)"], r"\eta\leftarrow\mathrm{clip}(\eta)\in[L,U]"),
    (1978, "SophiaWBoundClip", "1978_sophiawboundclip", "SophiaWBoundClip", "795_linear_157", "opt",
     ["SophiaW境界クリップ", "減衰二階", "枠"], ["核", "境界クリップ"], [r"\theta\leftarrow\theta-\eta m/\hat H-\lambda\theta", r"\eta\leftarrow\mathrm{clip}(\eta)"], r"\eta\leftarrow\mathrm{clip}(\eta)\in[L,U]"),
    (1979, "ApolloSoftBoundClip", "1979_apollosoftboundclip", "ApolloSoftBoundClip", "795_linear_157", "opt",
     ["Apollo軟境界クリップ", "準ニュートン", "三重"], ["核", "軟境界"], [r"B\leftarrow B+uu^\top", r"\eta\leftarrow\mathrm{clip}(\mathrm{soft}(\eta))"], r"\eta\leftarrow\mathrm{clip}(\mathrm{soft}(\eta))\in[L,U]"),
    (1980, "垂心類似九点弦比", "1980_h_sym_nine_chord", "HSymNineChord", "796_geometry_157", "tri",
     ["垂心類似九点弦", "九点円弦", "比"], ["配置", "比"], [r"H", r"\ell_{9,s}/R"], r"\ell_{9,s}/R"),
    (1981, "重心類似九点弦比", "1981_g_sym_nine_chord", "GSymNineChord", "796_geometry_157", "tri",
     ["重心類似九点弦", "九点円弦", "比"], ["配置", "比"], [r"G", r"\ell_{9,s}/\ell"], r"\ell_{9,s}/\ell"),
    (1982, "九点類似弦比", "1982_n_sym_nine_chord", "NSymNineChord", "796_geometry_157", "tri",
     ["九点類似弦", "弦", "比"], ["配置", "比"], [r"N", r"\ell_{9,s}/R_N"], r"\ell_{9,s}/R_N"),
    (1983, "局所一様スケール被覆", "1983_local_unif_scale_cov", "LocalUnifScaleCov", "797_probability_155", "pts",
     ["局所一様スケール被覆", "半径一様", "サイズ"], ["定義", "サイズ"], [r"N_{lu}(r,\epsilon)", r"N_{lu}\lesssim(r/\epsilon)^d"], r"N_{lu}\lesssim(r/\epsilon)^d"),
    (1984, "局所一様スケールパッキング", "1984_local_unif_scale_pack", "LocalUnifScalePack", "797_probability_155", "pts",
     ["局所一様スケールパッキング", "半径一様", "分離"], ["定義", "サイズ"], [r"M_{lu}(r,\epsilon)", r"M_{lu}\lesssim(r/\epsilon)^d"], r"M_{lu}\lesssim(r/\epsilon)^d"),
    (1985, "順序三分木細分", "1985_ordered_ternary_refine", "OrderedTernaryRefine", "798_combinatorics_154", "nums",
     ["順序三分木", "三分岐順序", "細分"], ["定義", "細分"], [r"OT_n", r"OT(n,k)"], r"OT(n,k)", [1, 1, 3, 12, 55]),
    (1986, "ログ随伴擬有効対", "1986_log_adj_psef", "LogAdjPsef", "799_analysis_158", "box",
     ["ログ随伴擬有効", "閉錐", "境界"], ["定義", "閉包"], [r"\overline{Eff}", r"K+D\in\overline{Eff}"], r"K+D\in\overline{Eff}"),
    (1987, "相対ログ随伴擬有効対", "1987_rel_log_adj_psef", "RelLogAdjPsef", "799_analysis_158", "box",
     ["相対ログ随伴擬有効", "相対閉錐", "ファイバー"], ["定義", "閉包"], [r"\overline{Eff}_{X/S}", r"K+D\in\overline{Eff}"], r"K+D\in\overline{Eff}"),
    (1988, "ログ随伴移動対", "1988_log_adj_movable", "LogAdjMovable", "799_analysis_158", "box",
     ["ログ随伴移動", "正値部", "境界"], ["定義", "錐"], [r"Mov", r"K+D\in Mov"], r"K+D\in Mov"),
    (1989, "MuonHardBoundClip", "1989_muonhardboundclip", "MuonHardBoundClip", "800_linear_158", "opt",
     ["Muon硬境界クリップ", "直交更新", "三重"], ["核", "硬境界"], [r"U^\top U=I", r"\eta\leftarrow\mathrm{clip}(\mathrm{hard}(\eta))"], r"\eta\leftarrow\mathrm{clip}(\mathrm{hard}(\eta))\in[L,U]"),
    (1990, "SamHardBoundClip", "1990_samhardboundclip", "SamHardBoundClip", "800_linear_158", "opt",
     ["SAM硬境界クリップ", "鋭度", "三重"], ["核", "硬境界"], [r"\epsilon\leftarrow\rho g/\|g\|", r"\rho\leftarrow\mathrm{clip}(\mathrm{hard}(\rho))"], r"\rho\leftarrow\mathrm{clip}(\mathrm{hard}(\rho))\in[L,U]"),
    (1991, "AdaFactorSoftBoundClip", "1991_adafactorsoftboundclip", "AdaFactorSoftBoundClip", "800_linear_158", "opt",
     ["AdaFactor軟境界クリップ", "因子化", "三重"], ["核", "軟境界"], [r"R_{ij}C_{ij}\approx G_{ij}^2", r"\eta\leftarrow\mathrm{clip}(\mathrm{soft}(\eta))"], r"\eta\leftarrow\mathrm{clip}(\mathrm{soft}(\eta))\in[L,U]"),
    (1992, "内心九点弧比", "1992_in_nine_arc", "InNineArc", "801_geometry_158", "tri",
     ["内心九点弧", "九点円弧", "比"], ["配置", "比"], [r"I", r"\ell_a/r"], r"\ell_a/r"),
    (1993, "傍心九点弧比", "1993_ex_nine_arc", "ExNineArc", "801_geometry_158", "tri",
     ["傍心九点弧", "九点円弧", "比"], ["配置", "比"], [r"I_a", r"\ell_a/r_a"], r"\ell_a/r_a"),
    (1994, "外心九点弧比", "1994_o_nine_arc", "ONineArc", "801_geometry_158", "tri",
     ["外心九点弧", "九点円弧", "比"], ["配置", "比"], [r"O", r"\ell_a/R"], r"\ell_a/R"),
    (1995, "一様標本スケール被覆", "1995_unif_sample_scale_cov", "UnifSampleScaleCov", "802_probability_156", "pts",
     ["一様標本スケール被覆", "一様標本半径", "サイズ"], ["定義", "サイズ"], [r"N_{n,u}(r,\epsilon)", r"N_{n,u}\lesssim(r/\epsilon)^d"], r"N_{n,u}\lesssim(r/\epsilon)^d"),
    (1996, "一様標本スケールパッキング", "1996_unif_sample_scale_pack", "UnifSampleScalePack", "802_probability_156", "pts",
     ["一様標本スケールパッキング", "一様標本半径", "分離"], ["定義", "サイズ"], [r"M_{n,u}(r,\epsilon)", r"M_{n,u}\lesssim(r/\epsilon)^d"], r"M_{n,u}\lesssim(r/\epsilon)^d"),
    (1997, "平面増加森細分", "1997_plane_inc_forest_refine", "PlaneIncForestRefine", "803_combinatorics_155", "nums",
     ["平面増加森", "順序増加", "細分"], ["定義", "細分"], [r"PIF_n", r"PIF(n,k)"], r"PIF(n,k)", [1, 2, 7, 38, 291]),
    (1998, "相対ログ随伴移動対", "1998_rel_log_adj_mov", "RelLogAdjMov", "804_analysis_159", "box",
     ["相対ログ随伴移動", "相対移動", "ファイバー"], ["定義", "錐"], [r"Mov_{X/S}", r"K+D\in Mov"], r"K+D\in Mov"),
    (1999, "ログ随伴正値対", "1999_log_adj_pos", "LogAdjPos", "804_analysis_159", "box",
     ["ログ随伴正値", "交差形式", "境界"], ["定義", "錐"], [r"Pos", r"K+D\in Pos"], r"K+D\in Pos"),
    (2000, "相対ログ随伴正値対", "2000_rel_log_adj_pos", "RelLogAdjPos", "804_analysis_159", "box",
     ["相対ログ随伴正値", "相対正値", "ファイバー"], ["定義", "錐"], [r"Pos_{X/S}", r"K+D\in Pos"], r"K+D\in Pos"),
    (2001, "NAdamHardBoundClip", "2001_nadamhardboundclip", "NAdamHardBoundClip", "805_linear_159", "opt",
     ["NAdam硬境界クリップ", "ネステロフ", "三重"], ["核", "硬境界"], [r"m\leftarrow\beta m+(1-\beta)g", r"\eta\leftarrow\mathrm{clip}(\mathrm{hard}(\eta))"], r"\eta\leftarrow\mathrm{clip}(\mathrm{hard}(\eta))\in[L,U]"),
    (2002, "LARSHardBoundClip", "2002_larshardboundclip", "LARSHardBoundClip", "805_linear_159", "opt",
     ["LARS硬境界クリップ", "層正規化", "三重"], ["核", "硬境界"], [r"\eta\leftarrow\|w\|/\|g\|", r"\eta\leftarrow\mathrm{clip}(\mathrm{hard}(\eta))"], r"\eta\leftarrow\mathrm{clip}(\mathrm{hard}(\eta))\in[L,U]"),
    (2003, "LAMBSoftBoundClip", "2003_lambsoftboundclip", "LAMBSoftBoundClip", "805_linear_159", "opt",
     ["LAMB軟境界クリップ", "層信頼域", "三重"], ["核", "軟境界"], [r"r\leftarrow\|w\|/\|\hat u\|", r"r\leftarrow\mathrm{clip}(\mathrm{soft}(r))"], r"r\leftarrow\mathrm{clip}(\mathrm{soft}(r))\in[L,U]"),
    (2004, "垂心九点弧比", "2004_h_nine_arc", "HNineArc", "806_geometry_159", "tri",
     ["垂心九点弧", "九点円弧", "比"], ["配置", "比"], [r"H", r"\ell_a/R"], r"\ell_a/R"),
    (2005, "重心九点弧比", "2005_g_nine_arc", "GNineArc", "806_geometry_159", "tri",
     ["重心九点弧", "九点円弧", "比"], ["配置", "比"], [r"G", r"\ell_a/\ell"], r"\ell_a/\ell"),
    (2006, "九点円弧比", "2006_n_nine_arc", "NNineArc", "806_geometry_159", "tri",
     ["九点円弧", "弧", "比"], ["配置", "比"], [r"N", r"\ell_a/R_N"], r"\ell_a/R_N"),
    (2007, "半径データ複雑度", "2007_radius_data_comp", "RadiusDataComp", "807_probability_157", "pts",
     ["半径データ複雑度", "データ半径", "上界"], ["定義", "上界"], [r"\mathfrak{C}_n(r)", r"\mathfrak{C}_n(r)\le C r^{\alpha}"], r"\mathfrak{C}_n(r)\le C r^{\alpha}"),
    (2008, "スケール一様被覆再訪", "2008_scale_unif_cov_rev", "ScaleUnifCovRev", "807_probability_157", "pts",
     ["スケール一様被覆", "再訪", "サイズ"], ["定義", "サイズ"], [r"N_u(r,\epsilon)", r"N_u\propto(r/\epsilon)^d"], r"N_u\propto(r/\epsilon)^d"),
    (2009, "ケイリー三分木細分", "2009_cayley_ternary_refine", "CayleyTernaryRefine", "808_combinatorics_156", "nums",
     ["ケイリー三分木", "三分岐公式", "細分"], ["定義", "細分"], [r"CT_n", r"CT(n,k)"], r"CT(n,k)", [1, 1, 3, 12, 55]),
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
    assert "VIDEOS_1974_1985" not in text

    def block(name, items):
        lines = [f"\n\n{name}: tuple[Video, ...] = ("]
        for num, title, path, cls in items:
            lines.append(f'    Video({num}, "{title}", "{path}", "{cls}"),')
        lines.append(")")
        return "\n".join(lines)

    cp.write_text(
        text.rstrip()
        + block("VIDEOS_1974_1985", created[:12])
        + block("VIDEOS_1986_1997", created[12:24])
        + block("VIDEOS_1998_2009", created[24:])
        + "\n",
        encoding="utf-8",
    )

    tp = ROOT / "tests/test_catalog.py"
    t = tp.read_text(encoding="utf-8")
    if "VIDEOS_1974_1985" not in t:
        t = t.replace(
            "VIDEOS_1962_1973 = _catalog.VIDEOS_1962_1973\n",
            "VIDEOS_1962_1973 = _catalog.VIDEOS_1962_1973\n"
            "VIDEOS_1974_1985 = _catalog.VIDEOS_1974_1985\n"
            "VIDEOS_1986_1997 = _catalog.VIDEOS_1986_1997\n"
            "VIDEOS_1998_2009 = _catalog.VIDEOS_1998_2009\n",
        )
        insert = """
    def test_numbers_are_1974_to_1985(self):
        nums = [v.number for v in VIDEOS_1974_1985]
        self.assertEqual(nums, list(range(1974, 1986)))


    def test_numbers_are_1986_to_1997(self):
        nums = [v.number for v in VIDEOS_1986_1997]
        self.assertEqual(nums, list(range(1986, 1998)))


    def test_numbers_are_1998_to_2009(self):
        nums = [v.number for v in VIDEOS_1998_2009]
        self.assertEqual(nums, list(range(1998, 2010)))

"""
        t = t.replace(
            "    def test_each_scene_file_defines_the_class(self):",
            insert + "    def test_each_scene_file_defines_the_class(self):",
        )
        t = t.replace(
            "            *VIDEOS_1962_1973,\n        ):",
            "            *VIDEOS_1962_1973,\n"
            "            *VIDEOS_1974_1985,\n"
            "            *VIDEOS_1986_1997,\n"
            "            *VIDEOS_1998_2009,\n"
            "        ):",
        )
        tp.write_text(t, encoding="utf-8")

    plan = ROOT / "project/math/PLAN.md"
    p = plan.read_text(encoding="utf-8")
    if "#1974" not in p:
        extra = "\n\n## 導出つき続き（#1974–#1985）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[:12]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#1986–#1997）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[12:24]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#1998–#2009）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[24:]:
            extra += f"| {num} | {title} | 実装 |\n"
        p = p.replace("## 1 本の作業フロー", extra + "\n## 1 本の作業フロー")
        plan.write_text(p, encoding="utf-8")

    print("created", created[0][0], "-", created[-1][0])


if __name__ == "__main__":
    main()
