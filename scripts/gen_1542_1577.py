#!/usr/bin/env python3
"""Generate #1542–#1577 with derive/proof beats."""
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
    (1542, "端末対", "1542_terminal_pair", "TerminalPair", "614_analysis_121", "box",
     ["端末対", "食い違い正", "特異点"], ["定義", "判定"], [r"a(E,X,D)", r"a(E,X,D)>0"], r"a(E,X,D)>0"),
    (1543, "標準対", "1543_canonical_sing_pair", "CanonicalSingPair", "614_analysis_121", "box",
     ["標準対", "食い違い非負", "特異点"], ["定義", "判定"], [r"a(E,X,D)", r"a(E,X,D)\ge 0"], r"a(E,X,D)\ge 0"),
    (1544, "ログ豊富対", "1544_log_ample_pair", "LogAmplePair", "614_analysis_121", "box",
     ["ログ豊富", "正値性", "埋め込み"], ["定義", "判定"], [r"L-(K+D)", r"L-(K+D)>0"], r"L-(K+D)>0"),
    (1545, "SAMSoftClip", "1545_samsoftclip", "SAMSoftClip", "615_linear_121", "opt",
     ["SAM軟クリップ", "鋭度", "二重"], ["核", "軟クリップ"], [r"\epsilon\leftarrow\rho g/\|g\|", r"\epsilon\leftarrow\mathrm{clip}(\mathrm{soft}(\epsilon))"], r"\epsilon\leftarrow\mathrm{clip}(\mathrm{soft}(\epsilon))"),
    (1546, "SAMSoftHard", "1546_samsofthard", "SAMSoftHard", "615_linear_121", "opt",
     ["SAM軟硬", "鋭度", "二段"], ["軟", "硬"], [r"\epsilon\leftarrow\mathrm{soft}(\epsilon)", r"\epsilon\leftarrow\mathrm{hard}(\epsilon)"], r"\epsilon\leftarrow\mathrm{hard}(\mathrm{soft}(\epsilon))"),
    (1547, "LookaheadSoftClip", "1547_lookaheadsoftclip", "LookaheadSoftClip", "615_linear_121", "opt",
     ["Lookahead軟クリップ", "外側平均", "二重"], ["核", "軟クリップ"], [r"x\leftarrow x+\alpha(y-x)", r"u\leftarrow\mathrm{clip}(\mathrm{soft}(u))"], r"u\leftarrow\mathrm{clip}(\mathrm{soft}(u))"),
    (1548, "垂心スピーカー比", "1548_h_spieker_ratio", "HSpiekerRatio", "616_geometry_121", "tri",
     ["垂心とスピーカー", "中点三角形", "比"], ["配置", "比"], [r"H", r"HSp/\ell"], r"HSp/\ell"),
    (1549, "重心スピーカー比", "1549_g_spieker_ratio", "GSpiekerRatio", "616_geometry_121", "tri",
     ["重心とスピーカー", "中点三角形", "比"], ["配置", "比"], [r"G", r"GSp/\ell"], r"GSp/\ell"),
    (1550, "九点スピーカー比", "1550_n_spieker_ratio", "NSpiekerRatio", "616_geometry_121", "tri",
     ["九点円とスピーカー", "中点", "比"], ["配置", "比"], [r"N", r"NSp/\ell"], r"NSp/\ell"),
    (1551, "マッカーサー再訪", "1551_mcdiarmid_revisit", "McDiarmidRevisit", "617_probability_119", "pts",
     ["マッカーサー", "有界差", "集中"], ["仮定", "不等式"], [r"|f(x)-f(x')|\le c_i", r"\mathbb{P}(f-\mathbb{E}f\ge t)\le e^{-2t^2/\sum c_i^2}"], r"\mathbb{P}(f-\mathbb{E}f\ge t)\le e^{-2t^2/\sum c_i^2}"),
    (1552, "経験エントロピー", "1552_empirical_entropy", "EmpiricalEntropy", "617_probability_119", "pts",
     ["経験エントロピー", "データ依存", "対数"], ["定義", "尺度"], [r"H_n(\epsilon)", r"H_n(\epsilon)=\log N_n(\epsilon)"], r"H_n(\epsilon)=\log N_n(\epsilon)"),
    (1553, "トリボナッチ細分", "1553_tribonacci_refine", "TribonacciRefine", "618_combinatorics_118", "nums",
     ["トリボナッチ", "三項漸化", "細分"], ["定義", "細分"], [r"T_n=T_{n-1}+T_{n-2}+T_{n-3}", r"T(n,k)"], r"T(n,k)", [1, 1, 2, 4, 7]),
    (1554, "ログネフ対", "1554_log_nef_pair", "LogNefPair", "619_analysis_122", "box",
     ["ログネフ", "交差非負", "境界"], ["定義", "判定"], [r"(L.C)", r"(L.C)\ge 0"], r"(L.C)\ge 0"),
    (1555, "ログビッグ対", "1555_log_big_pair", "LogBigPair", "619_analysis_122", "box",
     ["ログビッグ", "体積正", "開錐"], ["体積", "判定"], [r"vol(L)", r"vol(L)>0"], r"vol(L)>0"),
    (1556, "ログ擬有効対", "1556_log_psef_pair", "LogPsefPair", "619_analysis_122", "box",
     ["ログ擬有効", "閉錐", "数値"], ["定義", "閉包"], [r"\overline{Eff}", r"D\in\overline{Eff}"], r"D\in\overline{Eff}"),
    (1557, "LAMBHardClip", "1557_lambhardclip", "LAMBHardClip", "620_linear_122", "opt",
     ["LAMB硬クリップ", "層信頼域", "硬閾"], ["核", "硬クリップ"], [r"r\leftarrow\|w\|/\|\hat u\|", r"r\leftarrow\mathrm{hard}(\mathrm{clip}(r))"], r"r\leftarrow\mathrm{hard}(\mathrm{clip}(r))"),
    (1558, "LARSBound", "1558_larsbound", "LARSBound", "620_linear_122", "opt",
     ["LARS境界", "層正規化", "枠"], ["核", "境界"], [r"\eta\leftarrow\|w\|/\|g\|", r"\eta\in[L,U]"], r"\eta\in[L,U]"),
    (1559, "MuonBoundSoft", "1559_muonboundsoft", "MuonBoundSoft", "620_linear_122", "opt",
     ["Muon境界軟化", "直交更新", "平滑"], ["核", "軟境界"], [r"U^\top U=I", r"\eta\leftarrow\mathrm{soft}(\eta)"], r"\eta\leftarrow\mathrm{soft}(\mathrm{clip}(\eta))"),
    (1560, "内心シュタイナー比", "1560_in_steiner_ratio", "InSteinerRatio", "621_geometry_122", "tri",
     ["内心とシュタイナー", "楕円", "比"], ["配置", "比"], [r"I", r"\ell_S/\ell"], r"\ell_S/\ell"),
    (1561, "傍心シュタイナー比", "1561_ex_steiner_ratio", "ExSteinerRatio", "621_geometry_122", "tri",
     ["傍心とシュタイナー", "楕円", "比"], ["配置", "比"], [r"I_a", r"\ell_S/\ell'"], r"\ell_S/\ell'"),
    (1562, "外心シュタイナー比", "1562_o_steiner_ratio", "OSteinerRatio", "621_geometry_122", "tri",
     ["外心とシュタイナー", "楕円", "比"], ["配置", "比"], [r"O", r"\ell_S/R"], r"\ell_S/R"),
    (1563, "局所ラデマッハ再訪", "1563_local_rademacher_revisit", "LocalRademacherRevisit", "622_probability_120", "pts",
     ["局所ラデマッハ", "半径球", "複雑度"], ["定義", "上界"], [r"\mathfrak{R}(B(f,r))", r"\mathfrak{R}_{\mathrm{loc}}\le C/\sqrt n"], r"\mathfrak{R}_{\mathrm{loc}}\le C/\sqrt n"),
    (1564, "鎖状エントロピー", "1564_chaining_entropy", "ChainingEntropy", "622_probability_120", "pts",
     ["鎖状エントロピー", "階層被覆", "積分"], ["構成", "上界"], [r"\gamma_2", r"\mathbb{E}\sup X\le C\gamma_2"], r"\mathbb{E}\sup X\le C\gamma_2"),
    (1565, "テトラナッチ細分", "1565_tetranacci_refine", "TetranacciRefine", "623_combinatorics_119", "nums",
     ["テトラナッチ", "四項漸化", "細分"], ["定義", "細分"], [r"A_n=\sum_{i=1}^4 A_{n-i}", r"A(n,k)"], r"A(n,k)", [1, 1, 1, 1, 4]),
    (1566, "相対端末対", "1566_rel_terminal_pair", "RelTerminalPair", "624_analysis_123", "box",
     ["相対端末", "食い違い正", "ファイバー"], ["定義", "判定"], [r"a(E,X/S,D)", r"a(E,X/S,D)>0"], r"a(E,X/S,D)>0"),
    (1567, "相対標準対", "1567_rel_can_sing_pair", "RelCanSingPair", "624_analysis_123", "box",
     ["相対標準", "食い違い非負", "ファイバー"], ["定義", "判定"], [r"a(E,X/S,D)", r"a(E,X/S,D)\ge 0"], r"a(E,X/S,D)\ge 0"),
    (1568, "相対ログ豊富対", "1568_rel_log_ample_pair", "RelLogAmplePair", "624_analysis_123", "box",
     ["相対ログ豊富", "ファイバー正", "埋め込み"], ["定義", "判定"], [r"(L-(K+D))|_F", r"(L-(K+D))|_F>0"], r"(L-(K+D))|_F>0"),
    (1569, "ProdigySoftHard", "1569_prodigysofthard", "ProdigySoftHard", "625_linear_123", "opt",
     ["Prodigy軟硬", "D推定", "二段"], ["軟", "硬"], [r"d\leftarrow\mathrm{soft}(d)", r"d\leftarrow\mathrm{hard}(d)"], r"d\leftarrow\mathrm{hard}(\mathrm{soft}(d))"),
    (1570, "ScheduleFreeHardClip", "1570_schedulefreehardclip", "ScheduleFreeHardClip", "625_linear_123", "opt",
     ["平均化硬クリップ", "スケジュール不要", "硬閾"], ["核", "硬クリップ"], [r"z\leftarrow (1-c)z+cx", r"z\leftarrow\mathrm{hard}(\mathrm{clip}(z))"], r"z\leftarrow\mathrm{hard}(\mathrm{clip}(z))"),
    (1571, "SophiaWHard", "1571_sophiawhard", "SophiaWHard", "625_linear_123", "opt",
     ["SophiaW硬閾", "減衰二階", "剪定"], ["核", "硬閾"], [r"\theta\leftarrow\theta-\eta m/\hat H-\lambda\theta", r"u\leftarrow\mathrm{hard}(u)"], r"u\leftarrow\mathrm{hard}(u)"),
    (1572, "垂心ジェルゴンヌ比", "1572_h_gergonne_ratio", "HGergonneRatio", "626_geometry_123", "tri",
     ["垂心とジェルゴンヌ", "接点", "比"], ["配置", "比"], [r"H", r"HGe/\ell"], r"HGe/\ell"),
    (1573, "重心ナーゲル比", "1573_g_nagel_ratio", "GNagelRatio", "626_geometry_123", "tri",
     ["重心とナーゲル", "接点", "比"], ["配置", "比"], [r"G", r"GNa/\ell"], r"GNa/\ell"),
    (1574, "九点ミッテン比", "1574_n_mitten_ratio", "NMittenRatio", "626_geometry_123", "tri",
     ["九点円とミッテン", "中点", "比"], ["配置", "比"], [r"N", r"NM/\ell"], r"NM/\ell"),
    (1575, "双対被覆数", "1575_dual_covering", "DualCovering", "627_probability_121", "pts",
     ["双対被覆", "パッキング双対", "関係"], ["定義", "関係"], [r"N^*(\epsilon)", r"N^*(\epsilon)\asymp M(\epsilon)"], r"N^*(\epsilon)\asymp M(\epsilon)"),
    (1576, "スケール敏感度", "1576_scale_sensitivity", "ScaleSensitivity", "627_probability_121", "pts",
     ["スケール敏感度", "局所複雑度", "半径"], ["定義", "依存"], [r"\phi(r)", r"\phi(r)\propto r^\alpha"], r"\phi(r)\propto r^\alpha"),
    (1577, "大きなフィボナッチ細分", "1577_large_fib_refine", "LargeFibRefine", "628_combinatorics_120", "nums",
     ["大きなフィボナッチ", "拡張", "細分"], ["定義", "細分"], [r"F_n^{(m)}", r"F(n,k;m)"], r"F(n,k;m)", [1, 2, 3, 5, 8]),
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
    assert "VIDEOS_1542_1553" not in text

    def block(name, items):
        lines = [f"\n\n{name}: tuple[Video, ...] = ("]
        for num, title, path, cls in items:
            lines.append(f'    Video({num}, "{title}", "{path}", "{cls}"),')
        lines.append(")")
        return "\n".join(lines)

    cp.write_text(
        text.rstrip()
        + block("VIDEOS_1542_1553", created[:12])
        + block("VIDEOS_1554_1565", created[12:24])
        + block("VIDEOS_1566_1577", created[24:])
        + "\n",
        encoding="utf-8",
    )

    tp = ROOT / "tests/test_catalog.py"
    t = tp.read_text(encoding="utf-8")
    if "VIDEOS_1542_1553" not in t:
        t = t.replace(
            "VIDEOS_1530_1541 = _catalog.VIDEOS_1530_1541\n",
            "VIDEOS_1530_1541 = _catalog.VIDEOS_1530_1541\n"
            "VIDEOS_1542_1553 = _catalog.VIDEOS_1542_1553\n"
            "VIDEOS_1554_1565 = _catalog.VIDEOS_1554_1565\n"
            "VIDEOS_1566_1577 = _catalog.VIDEOS_1566_1577\n",
        )
        insert = """
    def test_numbers_are_1542_to_1553(self):
        nums = [v.number for v in VIDEOS_1542_1553]
        self.assertEqual(nums, list(range(1542, 1554)))


    def test_numbers_are_1554_to_1565(self):
        nums = [v.number for v in VIDEOS_1554_1565]
        self.assertEqual(nums, list(range(1554, 1566)))


    def test_numbers_are_1566_to_1577(self):
        nums = [v.number for v in VIDEOS_1566_1577]
        self.assertEqual(nums, list(range(1566, 1578)))

"""
        t = t.replace(
            "    def test_each_scene_file_defines_the_class(self):",
            insert + "    def test_each_scene_file_defines_the_class(self):",
        )
        t = t.replace(
            "            *VIDEOS_1530_1541,\n        ):",
            "            *VIDEOS_1530_1541,\n"
            "            *VIDEOS_1542_1553,\n"
            "            *VIDEOS_1554_1565,\n"
            "            *VIDEOS_1566_1577,\n"
            "        ):",
        )
        tp.write_text(t, encoding="utf-8")

    plan = ROOT / "project/math/PLAN.md"
    p = plan.read_text(encoding="utf-8")
    if "#1542" not in p:
        extra = "\n\n## 導出つき続き（#1542–#1553）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[:12]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#1554–#1565）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[12:24]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#1566–#1577）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[24:]:
            extra += f"| {num} | {title} | 実装 |\n"
        p = p.replace("## 1 本の作業フロー", extra + "\n## 1 本の作業フロー")
        plan.write_text(p, encoding="utf-8")

    print("created", created[0][0], "-", created[-1][0])


if __name__ == "__main__":
    main()
