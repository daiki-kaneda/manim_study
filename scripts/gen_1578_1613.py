#!/usr/bin/env python3
"""Generate #1578–#1613 with derive/proof beats."""
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
    (1578, "ログ移動対", "1578_log_movable_pair", "LogMovablePair", "629_analysis_124", "box",
     ["ログ移動", "正値部", "ネフとの差"], ["定義", "錐"], [r"Mov", r"D\in Mov"], r"D\in Mov"),
    (1579, "ログ正値対", "1579_log_positive_pair", "LogPositivePair", "629_analysis_124", "box",
     ["ログ正値", "交差形式", "双対"], ["定義", "錐"], [r"Pos", r"D\in Pos"], r"D\in Pos"),
    (1580, "ログ体積対", "1580_log_volume_pair", "LogVolumePair", "629_analysis_124", "box",
     ["ログ体積", "連続性", "ビッグ錐"], ["定義", "性質"], [r"vol(D)", r"vol(D)>0"], r"vol(D)"),
    (1581, "RMSSoftClip", "1581_rmssoftclip", "RMSSoftClip", "630_linear_124", "opt",
     ["RMS軟クリップ", "二乗平均", "二重"], ["核", "軟クリップ"], [r"v\leftarrow\beta v+(1-\beta)g^2", r"u\leftarrow\mathrm{clip}(\mathrm{soft}(u))"], r"u\leftarrow\mathrm{clip}(\mathrm{soft}(u))"),
    (1582, "RMSHardClip", "1582_rmshardclip", "RMSHardClip", "630_linear_124", "opt",
     ["RMS硬クリップ", "二乗平均", "硬閾"], ["核", "硬クリップ"], [r"v\leftarrow\beta v+(1-\beta)g^2", r"u\leftarrow\mathrm{hard}(\mathrm{clip}(u))"], r"u\leftarrow\mathrm{hard}(\mathrm{clip}(u))"),
    (1583, "LionSoftHard", "1583_lionsofthard", "LionSoftHard", "630_linear_124", "opt",
     ["Lion軟硬", "符号更新", "二段"], ["軟", "硬"], [r"u\leftarrow\mathrm{soft}(\mathrm{sign}(m))", r"u\leftarrow\mathrm{hard}(u)"], r"u\leftarrow\mathrm{hard}(\mathrm{soft}(\mathrm{sign}(m)))"),
    (1584, "垂心シュタイナー比", "1584_h_steiner_ratio", "HSteinerRatio", "631_geometry_124", "tri",
     ["垂心とシュタイナー", "楕円", "比"], ["配置", "比"], [r"H", r"\ell_S/\ell_H"], r"\ell_S/\ell_H"),
    (1585, "重心シュタイナー比", "1585_g_steiner_ratio", "GSteinerRatio", "631_geometry_124", "tri",
     ["重心とシュタイナー", "楕円", "比"], ["配置", "比"], [r"G", r"\ell_S/\ell_G"], r"\ell_S/\ell_G"),
    (1586, "九点シュタイナー比", "1586_n_steiner_ratio", "NSteinerRatio", "631_geometry_124", "tri",
     ["九点円とシュタイナー", "楕円", "比"], ["配置", "比"], [r"N", r"\ell_S/\ell_N"], r"\ell_S/\ell_N"),
    (1587, "ベンネット再訪", "1587_bennett_revisit", "BennettRevisit", "632_probability_122", "pts",
     ["ベンネット", "分散敏感", "指数尾"], ["仮定", "不等式"], [r"\mathbb{E}e^{\lambda X}", r"\mathbb{P}(S\ge t)\le e^{-vh(t/v)}"], r"\mathbb{P}(S\ge t)\le e^{-vh(t/v)}"),
    (1588, "ブールガンディ再訪", "1588_bousquet_revisit", "BousquetRevisit", "632_probability_122", "pts",
     ["ブールガンディ", "経験過程", "集中"], ["仮定", "不等式"], [r"Z=\sup(P_n-P)f", r"\mathbb{P}(Z-\mathbb{E}Z\ge t)\le e^{-t^2/2v}"], r"\mathbb{P}(Z-\mathbb{E}Z\ge t)\le e^{-t^2/2v}"),
    (1589, "ツリー細分", "1589_tree_refine", "TreeRefine", "633_combinatorics_121", "nums",
     ["木の数え上げ", "ケイリー", "細分"], ["定義", "細分"], [r"n^{n-2}", r"T(n,k)"], r"T(n,k)", [1, 1, 3, 16, 125]),
    (1590, "相対ログネフ対", "1590_rel_log_nef_pair", "RelLogNefPair", "634_analysis_125", "box",
     ["相対ログネフ", "曲線交差", "ファイバー"], ["定義", "判定"], [r"(L.C)", r"(L.C)\ge 0"], r"(L.C)\ge 0"),
    (1591, "相対ログビッグ対", "1591_rel_log_big_pair", "RelLogBigPair", "634_analysis_125", "box",
     ["相対ログビッグ", "相対体積", "開錐"], ["体積", "判定"], [r"vol_{X/S}(L)", r"vol_{X/S}(L)>0"], r"vol_{X/S}(L)>0"),
    (1592, "相対ログ擬有効対", "1592_rel_log_psef_pair", "RelLogPsefPair", "634_analysis_125", "box",
     ["相対ログ擬有効", "閉錐", "数値"], ["定義", "閉包"], [r"\overline{Eff}_{X/S}", r"D\in\overline{Eff}"], r"D\in\overline{Eff}"),
    (1593, "AdaFactorBound", "1593_adafactorbound", "AdaFactorBound", "635_linear_125", "opt",
     ["AdaFactor境界", "因子化", "枠"], ["核", "境界"], [r"R_{ij}C_{ij}\approx G_{ij}^2", r"\eta\in[L,U]"], r"\eta\in[L,U]"),
    (1594, "NAdamBound", "1594_nadambound", "NAdamBound", "635_linear_125", "opt",
     ["NAdam境界", "ネステロフ", "枠"], ["核", "境界"], [r"m\leftarrow\beta m+(1-\beta)g", r"\eta\in[L,U]"], r"\eta\in[L,U]"),
    (1595, "LookaheadHardClip", "1595_lookaheadhardclip", "LookaheadHardClip", "635_linear_125", "opt",
     ["Lookahead硬クリップ", "外側平均", "硬閾"], ["核", "硬クリップ"], [r"x\leftarrow x+\alpha(y-x)", r"u\leftarrow\mathrm{hard}(\mathrm{clip}(u))"], r"u\leftarrow\mathrm{hard}(\mathrm{clip}(u))"),
    (1596, "内心類似ジェルゴンヌ比", "1596_in_sym_gergonne_ratio", "InSymGergonneRatio", "636_geometry_125", "tri",
     ["内心と類似ジェルゴンヌ", "接点", "比"], ["配置", "比"], [r"I", r"IGe_s/\ell"], r"IGe_s/\ell"),
    (1597, "傍心類似ナーゲル比", "1597_ex_sym_nagel_ratio", "ExSymNagelRatio", "636_geometry_125", "tri",
     ["傍心と類似ナーゲル", "接点", "比"], ["配置", "比"], [r"I_a", r"I_aNa_s/\ell"], r"I_aNa_s/\ell"),
    (1598, "外心類似ミッテン比", "1598_o_sym_mitten_ratio", "OSymMittenRatio", "636_geometry_125", "tri",
     ["外心と類似ミッテン", "中点", "比"], ["配置", "比"], [r"O", r"OM_s/\ell"], r"OM_s/\ell"),
    (1599, "経験パッキング", "1599_empirical_packing", "EmpiricalPacking", "637_probability_123", "pts",
     ["経験パッキング", "データ依存", "分離"], ["定義", "サイズ"], [r"M_n(\epsilon)", r"M_n(\epsilon)\le M(\epsilon)"], r"M_n(\epsilon)\le M(\epsilon)"),
    (1600, "局所エントロピー", "1600_local_entropy", "LocalEntropy", "637_probability_123", "pts",
     ["局所エントロピー", "半径球", "対数"], ["定義", "尺度"], [r"H(B(f,r),\epsilon)", r"H_{\mathrm{loc}}(\epsilon)"], r"H_{\mathrm{loc}}(\epsilon)"),
    (1601, "森細分", "1601_forest_refine", "ForestRefine", "638_combinatorics_122", "nums",
     ["森の数え上げ", "成分", "細分"], ["定義", "細分"], [r"F_n", r"F(n,k)"], r"F(n,k)", [1, 1, 2, 7, 38]),
    (1602, "ログ数値次元対", "1602_log_num_dim_pair", "LogNumDimPair", "639_analysis_126", "box",
     ["ログ数値次元", "成長率", "κ"], ["定義", "値"], [r"\kappa_\sigma(D)", r"\kappa_\sigma(D)\in\{0,\ldots,n\}"], r"\kappa_\sigma(D)"),
    (1603, "ログ飯高次元対", "1603_log_iitaka_pair", "LogIitakaPair", "639_analysis_126", "box",
     ["ログ飯高次元", "線形系像", "κ"], ["写像", "次元"], [r"\phi_{|m(K+D)|}", r"\kappa(X,K+D)"], r"\kappa(X,K+D)"),
    (1604, "相対ログ移動対", "1604_rel_log_movable_pair", "RelLogMovablePair", "639_analysis_126", "box",
     ["相対ログ移動", "正値部", "ファイバー"], ["定義", "錐"], [r"Mov_{X/S}", r"D\in Mov"], r"D\in Mov"),
    (1605, "MuonBoundHard", "1605_muonboundhard", "MuonBoundHard", "640_linear_126", "opt",
     ["Muon境界硬閾", "直交更新", "剪定"], ["核", "硬境界"], [r"U^\top U=I", r"\eta\leftarrow\mathrm{hard}(\eta)"], r"\eta\leftarrow\mathrm{hard}(\mathrm{clip}(\eta))"),
    (1606, "ProdigyBoundSoft", "1606_prodigyboundsoft", "ProdigyBoundSoft", "640_linear_126", "opt",
     ["Prodigy境界軟化", "D推定", "平滑"], ["核", "軟境界"], [r"d\leftarrow\|g\|", r"\eta\leftarrow\mathrm{soft}(\eta)"], r"\eta\leftarrow\mathrm{soft}(\mathrm{clip}(\eta))"),
    (1607, "ScheduleFreeSoftHard", "1607_schedulefreesofthard", "ScheduleFreeSoftHard", "640_linear_126", "opt",
     ["平均化軟硬", "スケジュール不要", "二段"], ["軟", "硬"], [r"z\leftarrow\mathrm{soft}(z)", r"z\leftarrow\mathrm{hard}(z)"], r"z\leftarrow\mathrm{hard}(\mathrm{soft}(z))"),
    (1608, "内心オイラー比", "1608_in_euler_ratio", "InEulerRatio", "641_geometry_126", "tri",
     ["内心とオイラー線", "線分", "比"], ["配置", "比"], [r"I", r"d(I,OH)/\ell"], r"d(I,OH)/\ell"),
    (1609, "傍心オイラー比", "1609_ex_euler_ratio", "ExEulerRatio", "641_geometry_126", "tri",
     ["傍心とオイラー線", "線分", "比"], ["配置", "比"], [r"I_a", r"d(I_a,OH)/\ell"], r"d(I_a,OH)/\ell"),
    (1610, "外心オイラー比", "1610_o_euler_ratio", "OEulerRatio", "641_geometry_126", "tri",
     ["外心とオイラー線", "線分", "比"], ["配置", "比"], [r"O", r"OH/R"], r"OH/R"),
    (1611, "一様被覆数", "1611_uniform_covering", "UniformCovering", "642_probability_124", "pts",
     ["一様被覆", "全空間", "サイズ"], ["定義", "サイズ"], [r"N_u(\epsilon)", r"N_u(\epsilon)\le N(\epsilon)"], r"N_u(\epsilon)\le N(\epsilon)"),
    (1612, "ピネリス再訪", "1612_pinelis_revisit", "PinelisRevisit", "642_probability_124", "pts",
     ["ピネリス", "ベクトル値", "集中"], ["仮定", "不等式"], [r"\|S\|", r"\mathbb{P}(\|S\|\ge t)\le 2e^{-t^2/2v}"], r"\mathbb{P}(\|S\|\ge t)\le 2e^{-t^2/2v}"),
    (1613, "平面木細分", "1613_plane_tree_refine", "PlaneTreeRefine", "643_combinatorics_123", "nums",
     ["平面木", "順序つき", "細分"], ["定義", "細分"], [r"P_n", r"P(n,k)"], r"P(n,k)", [1, 1, 2, 5, 14]),
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
    assert "VIDEOS_1578_1589" not in text

    def block(name, items):
        lines = [f"\n\n{name}: tuple[Video, ...] = ("]
        for num, title, path, cls in items:
            lines.append(f'    Video({num}, "{title}", "{path}", "{cls}"),')
        lines.append(")")
        return "\n".join(lines)

    cp.write_text(
        text.rstrip()
        + block("VIDEOS_1578_1589", created[:12])
        + block("VIDEOS_1590_1601", created[12:24])
        + block("VIDEOS_1602_1613", created[24:])
        + "\n",
        encoding="utf-8",
    )

    tp = ROOT / "tests/test_catalog.py"
    t = tp.read_text(encoding="utf-8")
    if "VIDEOS_1578_1589" not in t:
        t = t.replace(
            "VIDEOS_1566_1577 = _catalog.VIDEOS_1566_1577\n",
            "VIDEOS_1566_1577 = _catalog.VIDEOS_1566_1577\n"
            "VIDEOS_1578_1589 = _catalog.VIDEOS_1578_1589\n"
            "VIDEOS_1590_1601 = _catalog.VIDEOS_1590_1601\n"
            "VIDEOS_1602_1613 = _catalog.VIDEOS_1602_1613\n",
        )
        insert = """
    def test_numbers_are_1578_to_1589(self):
        nums = [v.number for v in VIDEOS_1578_1589]
        self.assertEqual(nums, list(range(1578, 1590)))


    def test_numbers_are_1590_to_1601(self):
        nums = [v.number for v in VIDEOS_1590_1601]
        self.assertEqual(nums, list(range(1590, 1602)))


    def test_numbers_are_1602_to_1613(self):
        nums = [v.number for v in VIDEOS_1602_1613]
        self.assertEqual(nums, list(range(1602, 1614)))

"""
        t = t.replace(
            "    def test_each_scene_file_defines_the_class(self):",
            insert + "    def test_each_scene_file_defines_the_class(self):",
        )
        t = t.replace(
            "            *VIDEOS_1566_1577,\n        ):",
            "            *VIDEOS_1566_1577,\n"
            "            *VIDEOS_1578_1589,\n"
            "            *VIDEOS_1590_1601,\n"
            "            *VIDEOS_1602_1613,\n"
            "        ):",
        )
        tp.write_text(t, encoding="utf-8")

    plan = ROOT / "project/math/PLAN.md"
    p = plan.read_text(encoding="utf-8")
    if "#1578" not in p:
        extra = "\n\n## 導出つき続き（#1578–#1589）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[:12]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#1590–#1601）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[12:24]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#1602–#1613）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[24:]:
            extra += f"| {num} | {title} | 実装 |\n"
        p = p.replace("## 1 本の作業フロー", extra + "\n## 1 本の作業フロー")
        plan.write_text(p, encoding="utf-8")

    print("created", created[0][0], "-", created[-1][0])


if __name__ == "__main__":
    main()
