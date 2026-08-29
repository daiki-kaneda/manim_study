#!/usr/bin/env python3
"""Generate #1398–#1433 with derive/proof beats (~45–50s)."""
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


def mk(kind, cls, num, title, notes, derive_notes, derive_texes, final_tex, vals=None) -> str:
    n1, n2, n3 = notes
    d1, d2 = derive_notes
    t1, t2 = derive_texes
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
        formula = MathTex({math_expr(final_tex)}).scale(0.68)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.55)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.9)
'''
    head = (
        HEADER
        + f'''class {cls}(PacedScene):
    """#{num} {title}（約45秒・導出つき）"""

    def construct(self):
        self.show_heading("{title}")
        self.draw()
        self.mid()
        self.derive()
        self.show_formula()
        self.read(1.6)
'''
    )
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


# (num, title, slug, cls, season, kind, notes, dnotes, dtex, final, vals?)
VIDEOS = [
    # 1398-1409
    (1398, "乗法イデアル対", "1398_multiplier_pair", "MultiplierPair", "554_analysis_109", "box",
     ["乗法イデアル", "対との関係", "消滅へ"], ["定義", "対へ"], [r"\mathcal{J}(X,D)", r"\mathcal{J}(X,cD)"], r"\mathcal{J}(X,D)"),
    (1399, "跳躍イデアル対", "1399_jumping_pair", "JumpingPair", "554_analysis_109", "box",
     ["跳躍数", "イデアル変化", "閾値列"], ["跳躍", "対"], [r"c_i", r"\mathcal{J}(X,cD)"], r"c_i"),
    (1400, "対数的閾値対", "1400_lct_pair", "LCTPair", "554_analysis_109", "box",
     ["LCT", "対数ペア", "最小跳躍"], ["定義", "対"], [r"\mathrm{lct}(X,D)", r"\inf\{c:\mathcal{J}(cD)\ne\mathcal{O}\}"], r"lct(X,D)"),
    (1401, "AdaDeltaSoft", "1401_adadeltasoft", "AdaDeltaSoft", "555_linear_109", "opt",
     ["RMS比軟化", "更新幅平滑", "適応刻み"], ["核", "軟閾値"], [r"\Delta x\leftarrow\mathrm{RMS}", r"\Delta x\leftarrow\mathrm{soft}(\Delta x)"], r"\Delta x\leftarrow\mathrm{soft}(\mathrm{RMS})"),
    (1402, "AdamaxSoft", "1402_adamaxsoft", "AdamaxSoft", "555_linear_109", "opt",
     ["∞ノルム軟化", "更新平滑", "安定化"], ["核", "軟閾値"], [r"u\leftarrow\max(\beta u,|g|)", r"u\leftarrow\mathrm{soft}(u)"], r"x\leftarrow x-\eta\,m/\mathrm{soft}(u)"),
    (1403, "DemonSoft", "1403_demonsoft", "DemonSoft", "555_linear_109", "opt",
     ["減衰係数軟化", "モーメンタム", "平滑"], ["核", "軟閾値"], [r"\beta_t", r"\beta_t\leftarrow\mathrm{soft}(\beta_t)"], r"v\leftarrow\mathrm{soft}(\beta_t)v+g"),
    (1404, "中線面積比", "1404_median_area_ratio", "MedianAreaRatio", "556_geometry_109", "tri",
     ["中線と面積", "分割比", "辺長"], ["中線", "面積比"], [r"m_a", r"S_1/S_2"], r"S_1/S_2"),
    (1405, "角二等分比", "1405_angle_bisector_ratio", "AngleBisectorRatio", "556_geometry_109", "tri",
     ["角の二等分", "辺の比", "定理"], ["定理", "比"], [r"\frac{BD}{DC}=\frac{AB}{AC}", r"BD/DC=c/b"], r"BD/DC=AB/AC"),
    (1406, "傍接弦比", "1406_ex_tangent_ratio", "ExTangentRatio", "556_geometry_109", "tri",
     ["傍接線", "弦の比", "半周"], ["接線長", "比"], [r"s-a", r"t_a/t_b"], r"t_a=s-a"),
    (1407, "経験ラデマッハー再訪", "1407_emp_rad_revisit", "EmpRadRevisit", "557_probability_107", "pts",
     ["標本複雑度", "データ依存", "上界"], ["定義", "期待値"], [r"\hat R_n(\mathcal{F})", r"\mathbb{E}\hat R_n\le R_n"], r"\hat R_n\le R_n+\epsilon"),
    (1408, "PACベイズ", "1408_pac_bayes", "PACBayes", "557_probability_107", "pts",
     ["事後分布", "KL項", "汎化"], ["分解", "上界"], [r"KL(Q\|P)", r"R(Q)\le R_n(Q)+\sqrt{\frac{KL+\log(n/\delta)}{2n}}"], r"R(Q)\le R_n(Q)+\sqrt{(KL+\log(n/\delta))/(2n)}"),
    (1409, "ベル三角形細分", "1409_bell_tri_ref", "BellTriangleRefine", "558_combinatorics_106", "nums",
     ["ベル配列", "集合分割", "細分"], ["定義", "細分"], [r"B_n", r"B(n,k)"], r"B(n,k)", [1, 1, 2, 5, 15]),
    # 1410-1421
    (1410, "乗法イデアル濾過", "1410_multiplier_filtration", "MultiplierFiltration", "559_analysis_110", "box",
     ["濾過", "係数増加", "イデアル列"], ["濾過", "単調"], [r"c<c'", r"\mathcal{J}(c'D)\subset\mathcal{J}(cD)"], r"\mathcal{J}(c'D)\subset\mathcal{J}(cD)"),
    (1411, "跳躍数列", "1411_jumping_sequence", "JumpingSequence", "559_analysis_110", "box",
     ["跳躍の列", "有限性", "閾値"], ["列", "有限"], [r"c_1<c_2<\cdots", r"c_1<\cdots<c_m"], r"c_1<c_2<\cdots<c_m"),
    (1412, "相対LCT", "1412_relative_lct", "RelativeLCT", "559_analysis_110", "box",
     ["相対閾値", "ファイバー", "対数対"], ["相対", "定義"], [r"lct(X/S,D)", r"\inf c"], r"lct(X/S,D)"),
    (1413, "DiffGradHard", "1413_diffgradhard", "DiffGradHard", "560_linear_110", "opt",
     ["差分勾配硬閾", "平滑係数", "剪定"], ["核", "硬閾値"], [r"\xi\leftarrow|\Delta g|", r"\xi\leftarrow\mathrm{hard}(\xi)"], r"x\leftarrow x-\eta\,\mathrm{hard}(\xi)g"),
    (1414, "YogiHard", "1414_yogihard", "YogiHard", "560_linear_110", "opt",
     ["Yogi硬閾値", "符号付き分散", "剪定"], ["核", "硬閾値"], [r"v\leftarrow v+\mathrm{sign}(g^2-v)g^2", r"v\leftarrow\mathrm{hard}(v)"], r"x\leftarrow x-\eta m/\sqrt{\mathrm{hard}(v)}"),
    (1415, "YHSoft", "1415_yhsoft", "YHSoft", "560_linear_110", "opt",
     ["YH軟化", "ハイブリッド", "平滑"], ["核", "軟閾値"], [r"\Delta", r"\Delta\leftarrow\mathrm{soft}(\Delta)"], r"x\leftarrow x-\eta\,\mathrm{soft}(\Delta)"),
    (1416, "接点弦比", "1416_contact_chord_ratio", "ContactChordRatio", "561_geometry_110", "tri",
     ["接点弦", "内接円", "比"], ["接点", "比"], [r"x=s-a", r"x/y"], r"x/y=(s-a)/(s-b)"),
    (1417, "垂足弦比", "1417_pedal_chord_ratio", "PedalChordRatio", "561_geometry_110", "tri",
     ["垂足弦", "垂足三角形", "比"], ["垂足", "比"], [r"H_aH_b", r"H_aH_b/a"], r"H_aH_b/a"),
    (1418, "中点弦比", "1418_midpoint_chord_ratio", "MidpointChordRatio", "561_geometry_110", "tri",
     ["中点弦", "中点三角形", "比"], ["中点", "比"], [r"M_bM_c", r"M_bM_c/a"], r"M_bM_c=a/2"),
    (1419, "マージン界", "1419_margin_bound", "MarginBound", "562_probability_108", "pts",
     ["マージン", "汎化", "複雑度"], ["定義", "上界"], [r"\gamma", r"R\le\hat R_\gamma+\mathfrak{R}/\gamma"], r"R\le R_\gamma+R_n/\gamma"),
    (1420, "局所ラデマッハー", "1420_local_rademacher", "LocalRademacher", "562_probability_108", "pts",
     ["局所複雑度", "固定点", "速い率"], ["局所", "方程式"], [r"R_n(r)", r"r=\psi(r)"], r"r_*=\psi(r_*)"),
    (1421, "オイラー細分", "1421_euler_refine", "EulerRefine", "563_combinatorics_107", "nums",
     ["オイラー数", "上昇細分", "配列"], ["定義", "細分"], [r"A_n", r"A(n,k)"], r"A(n,k)", [1, 1, 4, 11, 26]),
    # 1422-1433
    (1422, "Nadelイデアル対", "1422_nadel_pair", "NadelPair", "564_analysis_111", "box",
     ["Nadel", "乗法イデアル", "消滅"], ["定義", "対"], [r"\mathcal{J}(D)", r"H^i(K+L\otimes\mathcal{J})=0"], r"H^i=0"),
    (1423, "川又対", "1423_kawamata_pair", "KawamataPair", "564_analysis_111", "box",
     ["川又・フィーベック", "対数対", "消滅"], ["仮定", "消滅"], [r"L-(K+D)\ \mathrm{nef}", r"H^i(X,K+D+L)=0"], r"H^i(K+D+L)=0"),
    (1424, "端末対の体積", "1424_terminal_volume", "TerminalVolume", "564_analysis_111", "box",
     ["端末対", "体積", "正値"], ["端末", "体積"], [r"(X,D)\ \mathrm{term}", r"vol(K+D)>0"], r"vol(K_X+D)"),
    (1425, "AdaFactorSoft", "1425_adafactorsoft", "AdaFactorSoft", "565_linear_111", "opt",
     ["因子分解軟化", "メモリ削減", "平滑"], ["核", "軟閾値"], [r"\eta", r"\eta\leftarrow\mathrm{soft}(\eta)"], r"\Delta\leftarrow\mathrm{soft}(\eta)g"),
    (1426, "LAMBSoft", "1426_lambsoft", "LAMBSoft", "565_linear_111", "opt",
     ["層適応軟化", "信頼比", "平滑"], ["核", "軟閾値"], [r"r=\|w\|/\|\Delta\|", r"r\leftarrow\mathrm{soft}(r)"], r"w\leftarrow w-\eta\,\mathrm{soft}(r)\Delta"),
    (1427, "LARSSoft", "1427_larssoft", "LARSSoft", "565_linear_111", "opt",
     ["局所学習率軟化", "ノルム比", "平滑"], ["核", "軟閾値"], [r"\eta_\ell", r"\eta_\ell\leftarrow\mathrm{soft}(\eta_\ell)"], r"w\leftarrow w-\mathrm{soft}(\eta_\ell)g"),
    (1428, "角二等分長", "1428_bisector_length", "BisectorLength", "566_geometry_111", "tri",
     ["二等分線長", "辺長公式", "比"], ["公式", "整理"], [r"t_a^2=bc(1-(a/(b+c))^2)", r"t_a"], r"t_a^2=bc(1-(a/(b+c))^2)"),
    (1429, "中線長比", "1429_median_length_ratio", "MedianLengthRatio", "566_geometry_111", "tri",
     ["中線長", "辺の二乗", "比"], ["公式", "比"], [r"m_a=\frac{1}{2}\sqrt{2b^2+2c^2-a^2}", r"m_a/a"], r"m_a/a"),
    (1430, "高さ比", "1430_altitude_ratio", "AltitudeRatio", "566_geometry_111", "tri",
     ["高さ", "面積経由", "比"], ["定義", "比"], [r"h_a=2S/a", r"h_a/h_b"], r"h_a/h_b=b/a"),
    (1431, "安定性汎化", "1431_stability_gen", "StabilityGeneralization", "567_probability_109", "pts",
     ["一様安定性", "汎化ギャップ", "期待値"], ["安定性", "ギャップ"], [r"|L(A_S)-L(A_{S'})|\le\beta", r"\mathbb{E}(R-R_n)\le\beta"], r"\mathbb{E}(R-R_n)\le\beta"),
    (1432, "アルゴリズム安定性", "1432_alg_stability", "AlgorithmicStability", "567_probability_109", "pts",
     ["置換安定", "仮説変化", "上界"], ["定義", "尾"], [r"\beta", r"P(R-R_n>\epsilon)\le e^{-2n\epsilon^2/\beta^2}"], r"P(R-R_n>\epsilon)\le e^{-2n\epsilon^2/\beta^2}"),
    (1433, "エルミート細分", "1433_hermite_refine", "HermiteRefine", "568_combinatorics_108", "nums",
     ["エルミート", "直交細分", "配列"], ["定義", "細分"], [r"H_n", r"H(n,k)"], r"H(n,k)", [1, 2, 6, 10, 30]),
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
        # scrub English-heavy finals where needed
        if final.startswith(r"\mathrm{lct}"):
            final = "lct(X,D)"
        path = f"project/math/{season}/{slug}/scene.py"
        code = mk(kind, cls, num, title, notes, dnotes, dtex, final, vals)
        # post-fix English in a few derive steps
        code = code.replace(
            'chr(92)+"mathrm"+\'{lct}(X,D)\'',
            '"lct(X,D)"',
        )
        folder = ROOT / "project/math" / season / slug
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "scene.py").write_text(code, encoding="utf-8")
        (folder / "storyboard.md").write_text(story(num, title), encoding="utf-8")
        ast.parse(code)
        created.append((num, title, path, cls))

    # Fix LCT and jumping finite mathrm / Nadel English via direct formula patches
    import re

    def set_formula_line(path: str, which: str, rhs: str) -> None:
        p = ROOT / path
        t = p.read_text(encoding="utf-8")
        # replace first MathTex in derive (t1) or leave; simpler: replace known bad finals
        if which == "final":
            t2, n = re.subn(
                r"(def show_formula\(self\):\n\s+formula = MathTex\().+?(\)\.scale\(0\.68\))",
                rf"\1{rhs}\2",
                t,
                count=1,
            )
            assert n == 1, path
            p.write_text(t2, encoding="utf-8")

    set_formula_line("project/math/554_analysis_109/1400_lct_pair/scene.py", "final", '"lct(X,D)"')
    # fix 1411 finite english if present
    p = ROOT / "project/math/559_analysis_110/1411_jumping_sequence/scene.py"
    t = p.read_text(encoding="utf-8")
    t = t.replace('chr(92)+"mathrm"+\'{finite}\'', '"finite"')
    # better replace the whole second derive eq
    t = re.sub(
        r"eq2 = MathTex\(.+?\)\.scale\(0\.62\)",
        'eq2 = MathTex("c_1<\\\\cdots<c_m").scale(0.62)'.replace("\\\\", "\\"),
        t,
        count=1,
    )
    # use chr form
    t = re.sub(
        r"eq2 = MathTex\(.+?\)\.scale\(0\.62\)",
        'eq2 = MathTex("c_1<"+chr(92)+"cdots"+"<c_m").scale(0.62)',
        t,
        count=1,
    )
    p.write_text(t, encoding="utf-8")
    # 1423/1424 english
    for path, rhs in [
        ("project/math/564_analysis_111/1423_kawamata_pair/scene.py", '"H^i(K+D+L)=0"'),
        ("project/math/564_analysis_111/1424_terminal_volume/scene.py", '"vol(K+D)"'),
    ]:
        set_formula_line(path, "final", rhs)
    # fix 1423 derive first line with english nef - replace dtex in file
    p = ROOT / "project/math/564_analysis_111/1423_kawamata_pair/scene.py"
    t = p.read_text(encoding="utf-8")
    t = re.sub(
        r"eq = MathTex\(.+?\)\.scale\(0\.62\)",
        'eq = MathTex("L-(K+D)").scale(0.62)',
        t,
        count=1,
    )
    p.write_text(t, encoding="utf-8")
    p = ROOT / "project/math/564_analysis_111/1424_terminal_volume/scene.py"
    t = p.read_text(encoding="utf-8")
    t = re.sub(
        r"eq = MathTex\(.+?\)\.scale\(0\.62\)",
        'eq = MathTex("(X,D)").scale(0.62)',
        t,
        count=1,
    )
    p.write_text(t, encoding="utf-8")

    # catalog
    cp = ROOT / "project/math/catalog.py"
    text = cp.read_text(encoding="utf-8")
    assert "VIDEOS_1398_1409" not in text

    def block(name, items):
        lines = [f"\n\n{name}: tuple[Video, ...] = ("]
        for num, title, path, cls in items:
            lines.append(f'    Video({num}, "{title}", "{path}", "{cls}"),')
        lines.append(")")
        return "\n".join(lines)

    cp.write_text(
        text.rstrip()
        + block("VIDEOS_1398_1409", created[:12])
        + block("VIDEOS_1410_1421", created[12:24])
        + block("VIDEOS_1422_1433", created[24:])
        + "\n",
        encoding="utf-8",
    )

    tp = ROOT / "tests/test_catalog.py"
    t = tp.read_text(encoding="utf-8")
    if "VIDEOS_1398_1409" not in t:
        t = t.replace(
            "VIDEOS_1386_1397 = _catalog.VIDEOS_1386_1397\n",
            "VIDEOS_1386_1397 = _catalog.VIDEOS_1386_1397\n"
            "VIDEOS_1398_1409 = _catalog.VIDEOS_1398_1409\n"
            "VIDEOS_1410_1421 = _catalog.VIDEOS_1410_1421\n"
            "VIDEOS_1422_1433 = _catalog.VIDEOS_1422_1433\n",
        )
        insert = """
    def test_numbers_are_1398_to_1409(self):
        nums = [v.number for v in VIDEOS_1398_1409]
        self.assertEqual(nums, list(range(1398, 1410)))


    def test_numbers_are_1410_to_1421(self):
        nums = [v.number for v in VIDEOS_1410_1421]
        self.assertEqual(nums, list(range(1410, 1422)))


    def test_numbers_are_1422_to_1433(self):
        nums = [v.number for v in VIDEOS_1422_1433]
        self.assertEqual(nums, list(range(1422, 1434)))

"""
        t = t.replace(
            "    def test_each_scene_file_defines_the_class(self):",
            insert + "    def test_each_scene_file_defines_the_class(self):",
        )
        t = t.replace(
            "            *VIDEOS_1386_1397,\n        ):",
            "            *VIDEOS_1386_1397,\n"
            "            *VIDEOS_1398_1409,\n"
            "            *VIDEOS_1410_1421,\n"
            "            *VIDEOS_1422_1433,\n"
            "        ):",
        )
        tp.write_text(t, encoding="utf-8")

    plan = ROOT / "project/math/PLAN.md"
    p = plan.read_text(encoding="utf-8")
    if "#1398" not in p:
        extra = "\n\n## 導出つき続き（#1398–#1409）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[:12]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#1410–#1421）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[12:24]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#1422–#1433）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[24:]:
            extra += f"| {num} | {title} | 実装 |\n"
        p = p.replace("## 1 本の作業フロー", extra + "\n## 1 本の作業フロー")
        plan.write_text(p, encoding="utf-8")

    # re-parse all
    for num, title, path, cls in created:
        ast.parse((ROOT / path).read_text(encoding="utf-8"))
    print("created", created[0][0], "-", created[-1][0])


if __name__ == "__main__":
    main()
