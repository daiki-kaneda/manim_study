#!/usr/bin/env python3
"""Generate #1434–#1469 with derive/proof beats."""
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
    # 1434-1445
    (1434, "豊富対", "1434_ample_pair", "AmplePair", "569_analysis_112", "box",
     ["豊富な対", "正値性", "埋め込み"], ["定義", "判定"], [r"L-(K+D)", r"L-(K+D)\ \mathrm{ample}"], r"L-(K+D)"),
    (1435, "ネフ対", "1435_nef_pair", "NefPair", "569_analysis_112", "box",
     ["ネフな対", "交差非負", "境界"], ["定義", "判定"], [r"(L.C)\ge 0", r"L\ \mathrm{nef}"], r"(L.C)\ge 0"),
    (1436, "ビッグ対", "1436_big_pair", "BigPair", "569_analysis_112", "box",
     ["ビッグな対", "体積正", "開錐"], ["体積", "ビッグ"], [r"vol(L)>0", r"L\in\mathrm{Big}"], r"vol(L)>0"),
    (1437, "ProdigySoftClip", "1437_prodigysoftclip", "ProdigySoftClip", "570_linear_112", "opt",
     ["D推定軟クリップ", "学習率", "二重制限"], ["核", "軟クリップ"], [r"d\leftarrow\mathrm{soft}(d)", r"d\leftarrow\mathrm{clip}(d)"], r"d\leftarrow\mathrm{clip}(\mathrm{soft}(d))"),
    (1438, "ScheduleFreeSoftClip", "1438_schedulefreesoftclip", "ScheduleFreeSoftClip", "570_linear_112", "opt",
     ["平均化軟クリップ", "スケジュール不要", "二重"], ["核", "軟クリップ"], [r"z\leftarrow\mathrm{soft}(z)", r"z\leftarrow\mathrm{clip}(z)"], r"z\leftarrow\mathrm{clip}(\mathrm{soft}(z))"),
    (1439, "MuonSoftHard", "1439_muonsofthard", "MuonSoftHard", "570_linear_112", "opt",
     ["Muon軟硬", "直交更新", "二段閾値"], ["軟", "硬"], [r"U\leftarrow\mathrm{soft}(U)", r"U\leftarrow\mathrm{hard}(U)"], r"U\leftarrow\mathrm{hard}(\mathrm{soft}(U))"),
    (1440, "内心角二等分比", "1440_in_bisector_ratio", "InBisectorRatio", "571_geometry_112", "tri",
     ["内心と二等分", "辺比", "定理"], ["配置", "比"], [r"I", r"BD/DC=AB/AC"], r"BD/DC=AB/AC"),
    (1441, "傍心角二等分比", "1441_ex_bisector_ratio", "ExBisectorRatio", "571_geometry_112", "tri",
     ["傍心と二等分", "外角", "比"], ["配置", "比"], [r"I_a", r"BD/DC=AB/AC"], r"BD/DC=c/b"),
    (1442, "外心角二等分比", "1442_o_bisector_ratio", "OBisectorRatio", "571_geometry_112", "tri",
     ["外心と二等分", "円周角", "比"], ["配置", "比"], [r"O", r"\ell/\ell'"], r"\ell/\ell'"),
    (1443, "VCサウアー再訪", "1443_vc_sauer_revisit", "VCSauerRevisit", "572_probability_110", "pts",
     ["VC次元", "成長関数", "折れ線"], ["補題", "上界"], [r"d=VCdim", r"\Pi(n)\le\sum_{i=0}^d\binom{n}{i}"], r"\Pi(n)\le\sum_{i=0}^d\binom{n}{i}"),
    (1444, "粉砕係数", "1444_shattering_coef", "ShatteringCoef", "572_probability_110", "pts",
     ["粉砕係数", "ラベル多様度", "上界"], ["定義", "関係"], [r"S(n)", r"S(n)\le\Pi(n)"], r"S(n)\le\Pi(n)"),
    (1445, "タッチャード細分", "1445_touchard_refine", "TouchardRefine", "573_combinatorics_109", "nums",
     ["タッチャード", "集合分割", "細分"], ["定義", "細分"], [r"T_n(x)", r"T(n,k)"], r"T(n,k)", [1, 1, 3, 13, 75]),
    # 1446-1457
    (1446, "擬有効対", "1446_psef_pair", "PsefPair", "574_analysis_113", "box",
     ["擬有効対", "閉錐", "数値"], ["定義", "閉包"], [r"\overline{Eff}", r"D\in\overline{Eff}"], r"D\in\overline{Eff}"),
    (1447, "移動対", "1447_movable_pair", "MovablePair", "574_analysis_113", "box",
     ["移動対", "正値部", "ネフとの差"], ["定義", "錐"], [r"Mov", r"D\in Mov"], r"D\in Mov"),
    (1448, "正値対", "1448_positive_pair", "PositivePair", "574_analysis_113", "box",
     ["正値対", "交差形式", "双対"], ["定義", "錐"], [r"Pos", r"D\in Pos"], r"D\in Pos"),
    (1449, "AdaBoundSoft", "1449_adaboundsoft", "AdaBoundSoft", "575_linear_113", "opt",
     ["境界つき軟化", "学習率枠", "平滑"], ["核", "軟境界"], [r"\eta\in[L,U]", r"\eta\leftarrow\mathrm{soft}(\eta)"], r"\eta\leftarrow\mathrm{soft}(\mathrm{clip}(\eta))"),
    (1450, "LionBoundSoft", "1450_lionboundsoft", "LionBoundSoft", "575_linear_113", "opt",
     ["Lion境界軟化", "符号更新", "平滑"], ["核", "軟境界"], [r"x\leftarrow x-\eta\mathrm{sign}(m)", r"\eta\leftarrow\mathrm{soft}(\eta)"], r"x\leftarrow x-\mathrm{soft}(\eta)\mathrm{sign}(m)"),
    (1451, "SophiaBoundSoft", "1451_sophiaboundsoft", "SophiaBoundSoft", "575_linear_113", "opt",
     ["Sophia境界軟化", "二階情報", "平滑"], ["核", "軟境界"], [r"\theta\leftarrow\theta-\eta m/\hat H", r"\eta\leftarrow\mathrm{soft}(\eta)"], r"\theta\leftarrow\theta-\mathrm{soft}(\eta)m/\hat H"),
    (1452, "垂心角二等分比", "1452_h_bisector_ratio", "HBisectorRatio", "576_geometry_113", "tri",
     ["垂心と二等分", "角条件", "比"], ["配置", "比"], [r"H", r"\ell_H"], r"\ell_H/\ell"),
    (1453, "重心角二等分比", "1453_g_bisector_ratio", "GBisectorRatio", "576_geometry_113", "tri",
     ["重心と二等分", "中線近傍", "比"], ["配置", "比"], [r"G", r"\ell_G"], r"\ell_G/\ell"),
    (1454, "九点角二等分比", "1454_n_bisector_ratio", "NBisectorRatio", "576_geometry_113", "tri",
     ["九点円と二等分", "中点", "比"], ["配置", "比"], [r"N", r"\ell_N"], r"\ell_N/\ell"),
    (1455, "成長多項式", "1455_growth_poly", "GrowthPolynomial", "577_probability_111", "pts",
     ["成長の多項式界", "VC次元", "次数d"], ["上界", "次数"], [r"\Pi(n)\le n^d+1", r"\deg\le d"], r"\Pi(n)\le n^d+1"),
    (1456, "ネット近似", "1456_net_approx", "NetApproximation", "577_probability_111", "pts",
     ["ネット", "一様近似", "誤差"], ["定義", "誤差"], [r"N_\epsilon", r"\sup|f-\hat f|\le\epsilon"], r"\sup|f-\hat f|\le\epsilon"),
    (1457, "フォア細分", "1457_fuss_refine", "FussRefine", "578_combinatorics_110", "nums",
     ["Fuss–Catalan", "多角形細分", "配列"], ["定義", "細分"], [r"C_n^{(m)}", r"C(n,k;m)"], r"C(n,k;m)", [1, 3, 12, 55, 273]),
    # 1458-1469
    (1458, "体積対", "1458_volume_pair", "VolumePair", "579_analysis_114", "box",
     ["対の体積", "連続性", "ビッグ錐"], ["定義", "性質"], [r"vol(D)", r"vol(D)>0"], r"vol(D)"),
    (1459, "数値的次元対", "1459_num_dim_pair", "NumDimPair", "579_analysis_114", "box",
     ["対の数値次元", "成長率", "κ"], ["定義", "値"], [r"\kappa_\sigma(D)", r"\kappa_\sigma(D)\in\{0,\ldots,n\}"], r"\kappa_\sigma(D)"),
    (1460, "飯高次元対", "1460_iitaka_pair", "IitakaPair", "579_analysis_114", "box",
     ["対の飯高次元", "線形系像", "κ"], ["写像", "次元"], [r"\phi_{|m(K+D)|}", r"\kappa(X,K+D)"], r"\kappa(X,K+D)"),
    (1461, "AdaBoundHard", "1461_adaboundhard", "AdaBoundHard", "580_linear_114", "opt",
     ["境界つき硬閾", "学習率枠", "剪定"], ["核", "硬境界"], [r"\eta\in[L,U]", r"\eta\leftarrow\mathrm{hard}(\eta)"], r"\eta\leftarrow\mathrm{hard}(\mathrm{clip}(\eta))"),
    (1462, "LionBoundHard", "1462_lionboundhard", "LionBoundHard", "580_linear_114", "opt",
     ["Lion境界硬閾", "符号更新", "剪定"], ["核", "硬境界"], [r"x\leftarrow x-\eta\mathrm{sign}(m)", r"\eta\leftarrow\mathrm{hard}(\eta)"], r"x\leftarrow x-\mathrm{hard}(\eta)\mathrm{sign}(m)"),
    (1463, "SophiaBoundHard", "1463_sophiaboundhard", "SophiaBoundHard", "580_linear_114", "opt",
     ["Sophia境界硬閾", "二階情報", "剪定"], ["核", "硬境界"], [r"\theta\leftarrow\theta-\eta m/\hat H", r"\eta\leftarrow\mathrm{hard}(\eta)"], r"\theta\leftarrow\theta-\mathrm{hard}(\eta)m/\hat H"),
    (1464, "内心高さ比", "1464_in_altitude_ratio", "InAltitudeRatio", "581_geometry_114", "tri",
     ["内心と高さ", "面積", "比"], ["配置", "比"], [r"r=S/s", r"r/h_a"], r"r/h_a"),
    (1465, "傍心高さ比", "1465_ex_altitude_ratio", "ExAltitudeRatio", "581_geometry_114", "tri",
     ["傍心と高さ", "傍接半径", "比"], ["配置", "比"], [r"r_a=S/(s-a)", r"r_a/h_a"], r"r_a/h_a"),
    (1466, "外心高さ比", "1466_o_altitude_ratio", "OAltitudeRatio", "581_geometry_114", "tri",
     ["外心と高さ", "外接半径", "比"], ["配置", "比"], [r"R=abc/4S", r"R/h_a"], r"R/h_a"),
    (1467, "イプシロンネット", "1467_epsilon_net", "EpsilonNet", "582_probability_112", "pts",
     ["εネット", "被覆", "一様収束"], ["定義", "サイズ"], [r"N(\epsilon)", r"|N|\lesssim\epsilon^{-d}"], r"|N|\lesssim\epsilon^{-d}"),
    (1468, "チャイニング再訪", "1468_chaining_revisit", "ChainingRevisit", "582_probability_112", "pts",
     ["チェイニング", "階層ネット", "集中"], ["構成", "上界"], [r"\gamma_2", r"\mathbb{E}\sup X_t\le C\gamma_2"], r"\mathbb{E}\sup X_t\le C\gamma_2"),
    (1469, "アペル細分", "1469_appel_refine", "AppelRefine", "583_combinatorics_111", "nums",
     ["アペル列", "微分関係", "細分"], ["定義", "細分"], [r"A_n'(x)=nA_{n-1}(x)", r"A(n,k)"], r"A(n,k)", [1, 1, 2, 5, 16]),
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
        # scrub English-only mathrm finals to symbols where needed
        if "mathrm{ample}" in final or "mathrm{nef}" in final or "mathrm{Big}" in final:
            pass
        path = f"project/math/{season}/{slug}/scene.py"
        # clean dtex/final of English mathrm for a few
        clean_dtex = list(dtex)
        clean_final = final
        replacements = {
            r"L-(K+D)\ \mathrm{ample}": r"L-(K+D)",
            r"L\ \mathrm{nef}": r"(L.C)\ge 0",
            r"L\in\mathrm{Big}": r"vol(L)>0",
            r"D\in\overline{Eff}": r"D\in\overline{Eff}",
            r"D\in Mov": r"D\in Mov",
            r"D\in Pos": r"D\in Pos",
        }
        clean_dtex = [replacements.get(x, x) for x in clean_dtex]
        clean_final = replacements.get(clean_final, clean_final)
        # for ample/nef/big use cleaner second steps already in list - fix first season
        if num == 1434:
            clean_dtex = [r"L-(K+D)", r"L-(K+D)>0"]
            clean_final = r"L-(K+D)>0"
        elif num == 1435:
            clean_dtex = [r"(L.C)", r"(L.C)\ge 0"]
            clean_final = r"(L.C)\ge 0"
        elif num == 1436:
            clean_dtex = [r"vol(L)", r"vol(L)>0"]
            clean_final = r"vol(L)>0"
        elif num == 1446:
            clean_dtex = [r"\overline{Eff}", r"D\in\overline{Eff}"]
            clean_final = r"D\in\overline{Eff}"
        elif num == 1447:
            clean_dtex = [r"Mov", r"D\in Mov"]
            clean_final = r"D\in Mov"
        elif num == 1448:
            clean_dtex = [r"Pos", r"D\in Pos"]
            clean_final = r"D\in Pos"

        code = mk(kind, cls, num, title, notes, dnotes, clean_dtex, clean_final, vals)
        folder = ROOT / "project/math" / season / slug
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "scene.py").write_text(code, encoding="utf-8")
        (folder / "storyboard.md").write_text(story(num, title), encoding="utf-8")
        ast.parse(code)
        created.append((num, title, path, cls))

    cp = ROOT / "project/math/catalog.py"
    text = cp.read_text(encoding="utf-8")
    assert "VIDEOS_1434_1445" not in text

    def block(name, items):
        lines = [f"\n\n{name}: tuple[Video, ...] = ("]
        for num, title, path, cls in items:
            lines.append(f'    Video({num}, "{title}", "{path}", "{cls}"),')
        lines.append(")")
        return "\n".join(lines)

    cp.write_text(
        text.rstrip()
        + block("VIDEOS_1434_1445", created[:12])
        + block("VIDEOS_1446_1457", created[12:24])
        + block("VIDEOS_1458_1469", created[24:])
        + "\n",
        encoding="utf-8",
    )

    tp = ROOT / "tests/test_catalog.py"
    t = tp.read_text(encoding="utf-8")
    if "VIDEOS_1434_1445" not in t:
        t = t.replace(
            "VIDEOS_1422_1433 = _catalog.VIDEOS_1422_1433\n",
            "VIDEOS_1422_1433 = _catalog.VIDEOS_1422_1433\n"
            "VIDEOS_1434_1445 = _catalog.VIDEOS_1434_1445\n"
            "VIDEOS_1446_1457 = _catalog.VIDEOS_1446_1457\n"
            "VIDEOS_1458_1469 = _catalog.VIDEOS_1458_1469\n",
        )
        insert = """
    def test_numbers_are_1434_to_1445(self):
        nums = [v.number for v in VIDEOS_1434_1445]
        self.assertEqual(nums, list(range(1434, 1446)))


    def test_numbers_are_1446_to_1457(self):
        nums = [v.number for v in VIDEOS_1446_1457]
        self.assertEqual(nums, list(range(1446, 1458)))


    def test_numbers_are_1458_to_1469(self):
        nums = [v.number for v in VIDEOS_1458_1469]
        self.assertEqual(nums, list(range(1458, 1470)))

"""
        t = t.replace(
            "    def test_each_scene_file_defines_the_class(self):",
            insert + "    def test_each_scene_file_defines_the_class(self):",
        )
        t = t.replace(
            "            *VIDEOS_1422_1433,\n        ):",
            "            *VIDEOS_1422_1433,\n"
            "            *VIDEOS_1434_1445,\n"
            "            *VIDEOS_1446_1457,\n"
            "            *VIDEOS_1458_1469,\n"
            "        ):",
        )
        tp.write_text(t, encoding="utf-8")

    plan = ROOT / "project/math/PLAN.md"
    p = plan.read_text(encoding="utf-8")
    if "#1434" not in p:
        extra = "\n\n## 導出つき続き（#1434–#1445）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[:12]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#1446–#1457）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[12:24]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#1458–#1469）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[24:]:
            extra += f"| {num} | {title} | 実装 |\n"
        p = p.replace("## 1 本の作業フロー", extra + "\n## 1 本の作業フロー")
        plan.write_text(p, encoding="utf-8")

    print("created", created[0][0], "-", created[-1][0])


if __name__ == "__main__":
    main()
