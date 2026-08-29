#!/usr/bin/env python3
"""Generate #1506–#1541 with derive/proof beats."""
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
    # 1506-1517
    (1506, "相対純端末対", "1506_rel_plt_pair", "RelPltPair", "599_analysis_118", "box",
     ["相対純端末", "食い違い", "ファイバー"], ["定義", "判定"], [r"a(E,X/S,D)", r"a(E,X/S,D)\ge -1"], r"a(E,X/S,D)\ge -1"),
    (1507, "相対純標準対", "1507_rel_klt_pair", "RelKltPair", "599_analysis_118", "box",
     ["相対純標準", "食い違い", "開条件"], ["定義", "判定"], [r"a(E,X/S,D)", r"a(E,X/S,D)>-1"], r"a(E,X/S,D)>-1"),
    (1508, "相対カノニカル対", "1508_rel_canonical_pair", "RelCanonicalPair", "599_analysis_118", "box",
     ["相対カノニカル", "食い違い非負", "閉条件"], ["定義", "判定"], [r"a(E,X/S,D)", r"a(E,X/S,D)\ge 0"], r"a(E,X/S,D)\ge 0"),
    (1509, "ScheduleFreeBound", "1509_schedulefreebound", "ScheduleFreeBound", "600_linear_118", "opt",
     ["平均化境界", "スケジュール不要", "枠"], ["核", "境界"], [r"z\leftarrow (1-c)z+cx", r"\eta\in[L,U]"], r"\eta\in[L,U]"),
    (1510, "ProdigyBound", "1510_prodigybound", "ProdigyBound", "600_linear_118", "opt",
     ["D推定境界", "学習率枠", "制限"], ["核", "境界"], [r"d\leftarrow\|g\|", r"\eta\in[L,U]"], r"\eta\in[L,U]"),
    (1511, "ProdigyHardClip", "1511_prodigyhardclip", "ProdigyHardClip", "600_linear_118", "opt",
     ["D推定硬クリップ", "学習率", "硬閾"], ["核", "硬クリップ"], [r"d\leftarrow\|g\|", r"d\leftarrow\mathrm{hard}(\mathrm{clip}(d))"], r"d\leftarrow\mathrm{hard}(\mathrm{clip}(d))"),
    (1512, "垂心傍接円比", "1512_h_excircle_ratio", "HExcircleRatio", "601_geometry_118", "tri",
     ["垂心と傍接円", "直交", "比"], ["配置", "比"], [r"H", r"\ell_H/r_a"], r"\ell_H/r_a"),
    (1513, "重心傍接円比", "1513_g_excircle_ratio", "GExcircleRatio", "601_geometry_118", "tri",
     ["重心と傍接円", "中線", "比"], ["配置", "比"], [r"G", r"\ell_G/r_a"], r"\ell_G/r_a"),
    (1514, "九点傍接円比", "1514_n_excircle_ratio", "NExcircleRatio", "601_geometry_118", "tri",
     ["九点円と傍接円", "中点", "比"], ["配置", "比"], [r"N", r"R_N/r_a"], r"R_N/r_a"),
    (1515, "劣ガウス再訪", "1515_subgaussian_revisit", "SubgaussianRevisit", "602_probability_116", "pts",
     ["劣ガウス", "尾部", "集中"], ["定義", "尾部"], [r"\psi_2", r"\mathbb{P}(|X|>t)\le 2e^{-t^2/K}"], r"\mathbb{P}(|X|>t)\le 2e^{-t^2/K}"),
    (1516, "ヘフディング再訪", "1516_hoeffding_revisit", "HoeffdingRevisit", "602_probability_116", "pts",
     ["ヘフディング", "有界和", "指数尾"], ["仮定", "不等式"], [r"X_i\in[a_i,b_i]", r"\mathbb{P}(S-\mathbb{E}S\ge t)\le e^{-2t^2/\sum(b_i-a_i)^2}"], r"\mathbb{P}(S-\mathbb{E}S\ge t)\le e^{-2t^2/\sum(b_i-a_i)^2}"),
    (1517, "リュカ細分", "1517_lucas_refine", "LucasRefine", "603_combinatorics_115", "nums",
     ["リュカ数", "漸化式", "細分"], ["定義", "細分"], [r"L_n=L_{n-1}+L_{n-2}", r"L(n,k)"], r"L(n,k)", [2, 1, 3, 4, 7]),
    # 1518-1529
    (1518, "対数端末対", "1518_log_terminal_pair", "LogTerminalPair", "604_analysis_119", "box",
     ["対数端末", "食い違い", "境界"], ["定義", "判定"], [r"a(E,X,D)", r"a(E,X,D)>-1"], r"a(E,X,D)>-1"),
    (1519, "対数標準対", "1519_log_canonical_pair", "LogCanonicalPair", "604_analysis_119", "box",
     ["対数標準", "食い違い", "閉条件"], ["定義", "判定"], [r"a(E,X,D)", r"a(E,X,D)\ge -1"], r"a(E,X,D)\ge -1"),
    (1520, "対数カノニカル対", "1520_log_can_pair", "LogCanPair", "604_analysis_119", "box",
     ["対数カノニカル", "食い違い非負", "厳密"], ["定義", "判定"], [r"a(E,X,D)", r"a(E,X,D)\ge 0"], r"a(E,X,D)\ge 0"),
    (1521, "MuonHardClip", "1521_muonhardclip", "MuonHardClip", "605_linear_119", "opt",
     ["Muon硬クリップ", "直交更新", "硬閾"], ["核", "硬クリップ"], [r"U^\top U=I", r"U\leftarrow\mathrm{hard}(\mathrm{clip}(U))"], r"U\leftarrow\mathrm{hard}(\mathrm{clip}(U))"),
    (1522, "SamHardClip", "1522_samhardclip", "SamHardClip", "605_linear_119", "opt",
     ["SAM硬クリップ", "鋭度", "硬閾"], ["核", "硬クリップ"], [r"\epsilon\leftarrow\rho g/\|g\|", r"\epsilon\leftarrow\mathrm{hard}(\mathrm{clip}(\epsilon))"], r"\epsilon\leftarrow\mathrm{hard}(\mathrm{clip}(\epsilon))"),
    (1523, "AdamWHardClip", "1523_adamwhardclip", "AdamWHardClip", "605_linear_119", "opt",
     ["AdamW硬クリップ", "減衰つき", "硬閾"], ["核", "硬クリップ"], [r"\theta\leftarrow\theta-\eta\hat m/\sqrt{\hat v}", r"u\leftarrow\mathrm{hard}(\mathrm{clip}(u))"], r"u\leftarrow\mathrm{hard}(\mathrm{clip}(u))"),
    (1524, "内心ジェルゴンヌ比", "1524_in_gergonne_ratio", "InGergonneRatio", "606_geometry_119", "tri",
     ["内心とジェルゴンヌ", "接点", "比"], ["配置", "比"], [r"I", r"IG/\ell"], r"IG/\ell"),
    (1525, "傍心ナーゲル比", "1525_ex_nagel_ratio", "ExNagelRatio", "606_geometry_119", "tri",
     ["傍心とナーゲル", "接点", "比"], ["配置", "比"], [r"I_a", r"I_aNa/\ell"], r"I_aNa/\ell"),
    (1526, "外心ミッテン比", "1526_o_mitten_ratio", "OMittenRatio", "606_geometry_119", "tri",
     ["外心とミッテン", "中点", "比"], ["配置", "比"], [r"O", r"OM/\ell"], r"OM/\ell"),
    (1527, "アズラ再訪", "1527_azuma_revisit", "AzumaRevisit", "607_probability_117", "pts",
     ["アズラ", "有界差", "マルチンゲール"], ["仮定", "不等式"], [r"|D_i|\le c_i", r"\mathbb{P}(S\ge t)\le e^{-t^2/2\sum c_i^2}"], r"\mathbb{P}(S\ge t)\le e^{-t^2/2\sum c_i^2}"),
    (1528, "タルラール再訪", "1528_talagrand_revisit", "TalagrandRevisit", "607_probability_117", "pts",
     ["タルラール", "凸距離", "集中"], ["仮定", "不等式"], [r"|f(x)-f(y)|\le d(x,y)", r"\mathbb{P}(|f-Mf|\ge t)\le 2e^{-t^2/2}"], r"\mathbb{P}(|f-Mf|\ge t)\le 2e^{-t^2/2}"),
    (1529, "ペル細分", "1529_pell_refine", "PellRefine", "608_combinatorics_116", "nums",
     ["ペル数", "漸化式", "細分"], ["定義", "細分"], [r"P_n=2P_{n-1}+P_{n-2}", r"P(n,k)"], r"P(n,k)", [0, 1, 2, 5, 12]),
    # 1530-1541
    (1530, "相対フリップ対", "1530_rel_flip_pair", "RelFlipPair", "609_analysis_120", "box",
     ["相対フリップ", "小収縮", "双有理"], ["定義", "変換"], [r"\phi^-", r"X\dashrightarrow_S X^+"], r"X\dashrightarrow_S X^+"),
    (1531, "相対フロップ対", "1531_rel_flop_pair", "RelFlopPair", "609_analysis_120", "box",
     ["相対フロップ", "K自明", "双有理"], ["定義", "変換"], [r"K_X\cdot C=0", r"X\dashrightarrow_S X'"], r"X\dashrightarrow_S X'"),
    (1532, "相対収縮対", "1532_rel_contraction_pair", "RelContractionPair", "609_analysis_120", "box",
     ["相対収縮", "極小モデル", "射"], ["定義", "射"], [r"\phi:X\to Y", r"\rho(X/Y)=1"], r"\rho(X/Y)=1"),
    (1533, "AdamWSoftClip", "1533_adamwsoftclip", "AdamWSoftClip", "610_linear_120", "opt",
     ["AdamW軟クリップ", "減衰つき", "二重"], ["核", "軟クリップ"], [r"u\leftarrow\hat m/\sqrt{\hat v}", r"u\leftarrow\mathrm{clip}(\mathrm{soft}(u))"], r"u\leftarrow\mathrm{clip}(\mathrm{soft}(u))"),
    (1534, "LionWHard", "1534_lionwhard", "LionWHard", "610_linear_120", "opt",
     ["LionW硬閾", "減衰符号", "剪定"], ["核", "硬閾"], [r"x\leftarrow x-\eta\mathrm{sign}(m)-\lambda x", r"u\leftarrow\mathrm{hard}(u)"], r"u\leftarrow\mathrm{hard}(u)"),
    (1535, "AdaFactorHard", "1535_adafactorhard", "AdaFactorHard", "610_linear_120", "opt",
     ["AdaFactor硬閾", "因子化", "剪定"], ["核", "硬閾"], [r"R_{ij}C_{ij}\approx G_{ij}^2", r"u\leftarrow\mathrm{hard}(u)"], r"u\leftarrow\mathrm{hard}(u)"),
    (1536, "内心スピーカー比", "1536_in_spieker_ratio", "InSpiekerRatio", "611_geometry_120", "tri",
     ["内心とスピーカー", "中点三角形", "比"], ["配置", "比"], [r"I", r"ISp/\ell"], r"ISp/\ell"),
    (1537, "傍心スピーカー比", "1537_ex_spieker_ratio", "ExSpiekerRatio", "611_geometry_120", "tri",
     ["傍心とスピーカー", "中点三角形", "比"], ["配置", "比"], [r"I_a", r"I_aSp/\ell"], r"I_aSp/\ell"),
    (1538, "外心スピーカー比", "1538_o_spieker_ratio", "OSpiekerRatio", "611_geometry_120", "tri",
     ["外心とスピーカー", "中点三角形", "比"], ["配置", "比"], [r"O", r"OSp/\ell"], r"OSp/\ell"),
    (1539, "パッキング数", "1539_packing_number", "PackingNumber", "612_probability_118", "pts",
     ["パッキング数", "分離点", "双対"], ["定義", "関係"], [r"M(\epsilon)", r"N(\epsilon)\le M(\epsilon)\le N(\epsilon/2)"], r"N(\epsilon)\le M(\epsilon)\le N(\epsilon/2)"),
    (1540, "メトリックエントロピー", "1540_metric_entropy", "MetricEntropy", "612_probability_118", "pts",
     ["メトリックエントロピー", "対数被覆", "尺度"], ["定義", "尺度"], [r"H(\epsilon)=\log N(\epsilon)", r"H(\epsilon)\asymp\log M(\epsilon)"], r"H(\epsilon)=\log N(\epsilon)"),
    (1541, "ゼッケンドルフ細分", "1541_zeckendorf_refine", "ZeckendorfRefine", "613_combinatorics_117", "nums",
     ["ゼッケンドルフ", "フィボナッチ和", "細分"], ["定義", "細分"], [r"n=\sum F_{k_i}", r"Z(n,k)"], r"Z(n,k)", [1, 1, 1, 2, 3]),
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
        # Fix geometry tuples that accidentally have 3 mid notes in dtex position - check 1524
        if num in (1524, 1525, 1526, 1536, 1537, 1538) and len(dtex) == 3:
            # mistyped: notes ok, but dtex had extra - rebuild
            pass
        path = f"project/math/{season}/{slug}/scene.py"
        # sanitize dtex length
        if len(dtex) != 2:
            # InGergonne etc: I wrote [r"I", r"Ge", r"IG/\ell"] by mistake
            dtex = [dtex[0], dtex[-1]]
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
    assert "VIDEOS_1506_1517" not in text

    def block(name, items):
        lines = [f"\n\n{name}: tuple[Video, ...] = ("]
        for num, title, path, cls in items:
            lines.append(f'    Video({num}, "{title}", "{path}", "{cls}"),')
        lines.append(")")
        return "\n".join(lines)

    cp.write_text(
        text.rstrip()
        + block("VIDEOS_1506_1517", created[:12])
        + block("VIDEOS_1518_1529", created[12:24])
        + block("VIDEOS_1530_1541", created[24:])
        + "\n",
        encoding="utf-8",
    )

    tp = ROOT / "tests/test_catalog.py"
    t = tp.read_text(encoding="utf-8")
    if "VIDEOS_1506_1517" not in t:
        t = t.replace(
            "VIDEOS_1494_1505 = _catalog.VIDEOS_1494_1505\n",
            "VIDEOS_1494_1505 = _catalog.VIDEOS_1494_1505\n"
            "VIDEOS_1506_1517 = _catalog.VIDEOS_1506_1517\n"
            "VIDEOS_1518_1529 = _catalog.VIDEOS_1518_1529\n"
            "VIDEOS_1530_1541 = _catalog.VIDEOS_1530_1541\n",
        )
        insert = """
    def test_numbers_are_1506_to_1517(self):
        nums = [v.number for v in VIDEOS_1506_1517]
        self.assertEqual(nums, list(range(1506, 1518)))


    def test_numbers_are_1518_to_1529(self):
        nums = [v.number for v in VIDEOS_1518_1529]
        self.assertEqual(nums, list(range(1518, 1530)))


    def test_numbers_are_1530_to_1541(self):
        nums = [v.number for v in VIDEOS_1530_1541]
        self.assertEqual(nums, list(range(1530, 1542)))

"""
        t = t.replace(
            "    def test_each_scene_file_defines_the_class(self):",
            insert + "    def test_each_scene_file_defines_the_class(self):",
        )
        t = t.replace(
            "            *VIDEOS_1494_1505,\n        ):",
            "            *VIDEOS_1494_1505,\n"
            "            *VIDEOS_1506_1517,\n"
            "            *VIDEOS_1518_1529,\n"
            "            *VIDEOS_1530_1541,\n"
            "        ):",
        )
        tp.write_text(t, encoding="utf-8")

    plan = ROOT / "project/math/PLAN.md"
    p = plan.read_text(encoding="utf-8")
    if "#1506" not in p:
        extra = "\n\n## 導出つき続き（#1506–#1517）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[:12]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#1518–#1529）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[12:24]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#1530–#1541）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[24:]:
            extra += f"| {num} | {title} | 実装 |\n"
        p = p.replace("## 1 本の作業フロー", extra + "\n## 1 本の作業フロー")
        plan.write_text(p, encoding="utf-8")

    print("created", created[0][0], "-", created[-1][0])


if __name__ == "__main__":
    main()
