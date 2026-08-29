#!/usr/bin/env python3
"""Generate #1614–#1649 with derive/proof beats."""
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
    (1614, "相対ログ正値対", "1614_rel_log_positive_pair", "RelLogPositivePair", "644_analysis_127", "box",
     ["相対ログ正値", "交差形式", "ファイバー"], ["定義", "錐"], [r"Pos_{X/S}", r"D\in Pos"], r"D\in Pos"),
    (1615, "相対ログ体積対", "1615_rel_log_volume_pair", "RelLogVolumePair", "644_analysis_127", "box",
     ["相対ログ体積", "連続性", "相対ビッグ"], ["定義", "性質"], [r"vol_{X/S}(D)", r"vol_{X/S}(D)>0"], r"vol_{X/S}(D)"),
    (1616, "ログ収縮対", "1616_log_contraction_pair", "LogContractionPair", "644_analysis_127", "box",
     ["ログ収縮", "極小モデル", "射"], ["定義", "射"], [r"\phi:X\to Y", r"\rho(X/Y)=1"], r"\rho(X/Y)=1"),
    (1617, "AdamWBoundSoft", "1617_adamwboundsoft", "AdamWBoundSoft", "645_linear_127", "opt",
     ["AdamW境界軟化", "減衰つき", "平滑"], ["核", "軟境界"], [r"u\leftarrow\hat m/\sqrt{\hat v}", r"\eta\leftarrow\mathrm{soft}(\eta)"], r"\eta\leftarrow\mathrm{soft}(\mathrm{clip}(\eta))"),
    (1618, "LionBoundClip", "1618_lionboundclip", "LionBoundClip", "645_linear_127", "opt",
     ["Lion境界クリップ", "符号更新", "枠"], ["核", "境界クリップ"], [r"x\leftarrow x-\eta\mathrm{sign}(m)", r"\eta\leftarrow\mathrm{clip}(\eta)"], r"\eta\leftarrow\mathrm{clip}(\eta)\in[L,U]"),
    (1619, "SophiaBoundClip", "1619_sophiaboundclip", "SophiaBoundClip", "645_linear_127", "opt",
     ["Sophia境界クリップ", "二階情報", "枠"], ["核", "境界クリップ"], [r"\theta\leftarrow\theta-\eta m/\hat H", r"\eta\leftarrow\mathrm{clip}(\eta)"], r"\eta\leftarrow\mathrm{clip}(\eta)\in[L,U]"),
    (1620, "垂心オイラー比", "1620_h_euler_ratio", "HEulerRatio", "646_geometry_127", "tri",
     ["垂心とオイラー線", "線分", "比"], ["配置", "比"], [r"H", r"OH/R"], r"OH/R"),
    (1621, "重心オイラー比", "1621_g_euler_ratio", "GEulerRatio", "646_geometry_127", "tri",
     ["重心とオイラー線", "線分", "比"], ["配置", "比"], [r"G", r"OG:GH=1:2"], r"OG:GH=1:2"),
    (1622, "九点オイラー比", "1622_n_euler_ratio", "NEulerRatio", "646_geometry_127", "tri",
     ["九点円とオイラー線", "中点", "比"], ["配置", "比"], [r"N", r"ON=NH"], r"ON=NH"),
    (1623, "経験チャイニング", "1623_empirical_chaining", "EmpiricalChaining", "647_probability_125", "pts",
     ["経験チェイニング", "データ階層", "上界"], ["構成", "上界"], [r"\gamma_{2,n}", r"\mathbb{E}\sup X\le C\gamma_{2,n}"], r"\mathbb{E}\sup X\le C\gamma_{2,n}"),
    (1624, "局所パッキング", "1624_local_packing", "LocalPacking", "647_probability_125", "pts",
     ["局所パッキング", "半径球", "分離"], ["定義", "サイズ"], [r"M(B(f,r),\epsilon)", r"M_{\mathrm{loc}}(\epsilon)"], r"M_{\mathrm{loc}}(\epsilon)"),
    (1625, "ホフスタッター細分", "1625_hofstadter_refine", "HofstadterRefine", "648_combinatorics_124", "nums",
     ["ホフスタッター", "入れ子漸化", "細分"], ["定義", "細分"], [r"a(n)=n-a(a(n-1))", r"H(n,k)"], r"H(n,k)", [1, 1, 2, 2, 3]),
    (1626, "相対ログ数値次元対", "1626_rel_log_num_dim", "RelLogNumDim", "649_analysis_128", "box",
     ["相対ログ数値次元", "成長率", "κ"], ["定義", "値"], [r"\kappa_\sigma(X/S,D)", r"\kappa_\sigma\in\{0,\ldots\}"], r"\kappa_\sigma(X/S,D)"),
    (1627, "相対ログ飯高次元対", "1627_rel_log_iitaka", "RelLogIitaka", "649_analysis_128", "box",
     ["相対ログ飯高次元", "相対線形系", "κ"], ["写像", "次元"], [r"\phi_{|m(K+D)|/S}", r"\kappa(X/S,K+D)"], r"\kappa(X/S,K+D)"),
    (1628, "ログフリップ対", "1628_log_flip_pair", "LogFlipPair", "649_analysis_128", "box",
     ["ログフリップ", "小収縮", "双有理"], ["定義", "変換"], [r"\phi^-", r"X\dashrightarrow X^+"], r"X\dashrightarrow X^+"),
    (1629, "AdaFactorSoftHard", "1629_adafactorsofthard", "AdaFactorSoftHard", "650_linear_128", "opt",
     ["AdaFactor軟硬", "因子化", "二段"], ["軟", "硬"], [r"u\leftarrow\mathrm{soft}(u)", r"u\leftarrow\mathrm{hard}(u)"], r"u\leftarrow\mathrm{hard}(\mathrm{soft}(u))"),
    (1630, "NAdamSoftBound", "1630_nadamsoftbound", "NAdamSoftBound", "650_linear_128", "opt",
     ["NAdam軟境界", "ネステロフ", "平滑枠"], ["核", "軟境界"], [r"m\leftarrow\beta m+(1-\beta)g", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{clip}(\eta))"),
    (1631, "RMSBoundSoft", "1631_rmsboundsoft", "RMSBoundSoft", "650_linear_128", "opt",
     ["RMS境界軟化", "二乗平均", "平滑"], ["核", "軟境界"], [r"v\leftarrow\beta v+(1-\beta)g^2", r"\eta\leftarrow\mathrm{soft}(\eta)"], r"\eta\leftarrow\mathrm{soft}(\mathrm{clip}(\eta))"),
    (1632, "内心類似スピーカー比", "1632_in_sym_spieker_ratio", "InSymSpiekerRatio", "651_geometry_128", "tri",
     ["内心と類似スピーカー", "中点三角形", "比"], ["配置", "比"], [r"I", r"ISp_s/\ell"], r"ISp_s/\ell"),
    (1633, "傍心類似スピーカー比", "1633_ex_sym_spieker_ratio", "ExSymSpiekerRatio", "651_geometry_128", "tri",
     ["傍心と類似スピーカー", "中点三角形", "比"], ["配置", "比"], [r"I_a", r"I_aSp_s/\ell"], r"I_aSp_s/\ell"),
    (1634, "外心類似スピーカー比", "1634_o_sym_spieker_ratio", "OSymSpiekerRatio", "651_geometry_128", "tri",
     ["外心と類似スピーカー", "中点三角形", "比"], ["配置", "比"], [r"O", r"OSp_s/\ell"], r"OSp_s/\ell"),
    (1635, "一様パッキング", "1635_uniform_packing", "UniformPacking", "652_probability_126", "pts",
     ["一様パッキング", "全空間", "分離"], ["定義", "サイズ"], [r"M_u(\epsilon)", r"M_u(\epsilon)\le M(\epsilon)"], r"M_u(\epsilon)\le M(\epsilon)"),
    (1636, "劣指数再訪", "1636_subexp_revisit", "SubexpRevisit", "652_probability_126", "pts",
     ["劣指数", "尾部", "集中"], ["定義", "尾部"], [r"\psi_1", r"\mathbb{P}(|X|>t)\le 2e^{-t/K}"], r"\mathbb{P}(|X|>t)\le 2e^{-t/K}"),
    (1637, "ディセクト細分", "1637_dissect_refine", "DissectRefine", "653_combinatorics_125", "nums",
     ["多角形細分", "対角線", "数え上げ"], ["定義", "細分"], [r"D_n", r"D(n,k)"], r"D(n,k)", [1, 2, 5, 14, 42]),
    (1638, "相対ログ収縮対", "1638_rel_log_contraction", "RelLogContraction", "654_analysis_129", "box",
     ["相対ログ収縮", "極小モデル", "射"], ["定義", "射"], [r"\phi:X\to Y", r"\rho(X/Y)=1"], r"\rho(X/Y)=1"),
    (1639, "相対ログフリップ対", "1639_rel_log_flip", "RelLogFlip", "654_analysis_129", "box",
     ["相対ログフリップ", "小収縮", "双有理"], ["定義", "変換"], [r"\phi^-", r"X\dashrightarrow_S X^+"], r"X\dashrightarrow_S X^+"),
    (1640, "ログフロップ対", "1640_log_flop_pair", "LogFlopPair", "654_analysis_129", "box",
     ["ログフロップ", "K自明", "双有理"], ["定義", "変換"], [r"K_X\cdot C=0", r"X\dashrightarrow X'"], r"X\dashrightarrow X'"),
    (1641, "AdamWSoftHard", "1641_adamwsofthard", "AdamWSoftHard", "655_linear_129", "opt",
     ["AdamW軟硬", "減衰つき", "二段"], ["軟", "硬"], [r"u\leftarrow\mathrm{soft}(u)", r"u\leftarrow\mathrm{hard}(u)"], r"u\leftarrow\mathrm{hard}(\mathrm{soft}(u))"),
    (1642, "LookaheadBound", "1642_lookaheadbound", "LookaheadBound", "655_linear_129", "opt",
     ["Lookahead境界", "外側平均", "枠"], ["核", "境界"], [r"x\leftarrow x+\alpha(y-x)", r"\eta\in[L,U]"], r"\eta\in[L,U]"),
    (1643, "SAMBoundSoft", "1643_samboundsoft", "SAMBoundSoft", "655_linear_129", "opt",
     ["SAM境界軟化", "鋭度", "平滑"], ["核", "軟境界"], [r"\epsilon\leftarrow\rho g/\|g\|", r"\rho\leftarrow\mathrm{soft}(\rho)"], r"\rho\leftarrow\mathrm{soft}(\mathrm{clip}(\rho))"),
    (1644, "垂心類似スピーカー比", "1644_h_sym_spieker_ratio", "HSymSpiekerRatio", "656_geometry_129", "tri",
     ["垂心と類似スピーカー", "中点三角形", "比"], ["配置", "比"], [r"H", r"HSp_s/\ell"], r"HSp_s/\ell"),
    (1645, "重心類似スピーカー比", "1645_g_sym_spieker_ratio", "GSymSpiekerRatio", "656_geometry_129", "tri",
     ["重心と類似スピーカー", "中点三角形", "比"], ["配置", "比"], [r"G", r"GSp_s/\ell"], r"GSp_s/\ell"),
    (1646, "九点類似スピーカー比", "1646_n_sym_spieker_ratio", "NSymSpiekerRatio", "656_geometry_129", "tri",
     ["九点円と類似スピーカー", "中点", "比"], ["配置", "比"], [r"N", r"NSp_s/\ell"], r"NSp_s/\ell"),
    (1647, "有界差再訪", "1647_bounded_diff_revisit", "BoundedDiffRevisit", "657_probability_127", "pts",
     ["有界差", "置換感度", "集中"], ["仮定", "不等式"], [r"|f(x)-f(x')|\le c_i", r"\mathbb{P}(f-\mathbb{E}f\ge t)\le e^{-2t^2/\sum c_i^2}"], r"\mathbb{P}(f-\mathbb{E}f\ge t)\le e^{-2t^2/\sum c_i^2}"),
    (1648, "ベクトル集中再訪", "1648_vector_conc_revisit", "VectorConcRevisit", "657_probability_127", "pts",
     ["ベクトル集中", "ノルム", "尾部"], ["仮定", "不等式"], [r"\|S\|", r"\mathbb{P}(\|S\|\ge t)\le 2e^{-t^2/2v}"], r"\mathbb{P}(\|S\|\ge t)\le 2e^{-t^2/2v}"),
    (1649, "カータラン路細分", "1649_catalan_path_refine", "CatalanPathRefine", "658_combinatorics_126", "nums",
     ["カタラン路", "Dyck路", "細分"], ["定義", "細分"], [r"C_n", r"C(n,k)"], r"C(n,k)", [1, 2, 5, 14, 42]),
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
    assert "VIDEOS_1614_1625" not in text

    def block(name, items):
        lines = [f"\n\n{name}: tuple[Video, ...] = ("]
        for num, title, path, cls in items:
            lines.append(f'    Video({num}, "{title}", "{path}", "{cls}"),')
        lines.append(")")
        return "\n".join(lines)

    cp.write_text(
        text.rstrip()
        + block("VIDEOS_1614_1625", created[:12])
        + block("VIDEOS_1626_1637", created[12:24])
        + block("VIDEOS_1638_1649", created[24:])
        + "\n",
        encoding="utf-8",
    )

    tp = ROOT / "tests/test_catalog.py"
    t = tp.read_text(encoding="utf-8")
    if "VIDEOS_1614_1625" not in t:
        t = t.replace(
            "VIDEOS_1602_1613 = _catalog.VIDEOS_1602_1613\n",
            "VIDEOS_1602_1613 = _catalog.VIDEOS_1602_1613\n"
            "VIDEOS_1614_1625 = _catalog.VIDEOS_1614_1625\n"
            "VIDEOS_1626_1637 = _catalog.VIDEOS_1626_1637\n"
            "VIDEOS_1638_1649 = _catalog.VIDEOS_1638_1649\n",
        )
        insert = """
    def test_numbers_are_1614_to_1625(self):
        nums = [v.number for v in VIDEOS_1614_1625]
        self.assertEqual(nums, list(range(1614, 1626)))


    def test_numbers_are_1626_to_1637(self):
        nums = [v.number for v in VIDEOS_1626_1637]
        self.assertEqual(nums, list(range(1626, 1638)))


    def test_numbers_are_1638_to_1649(self):
        nums = [v.number for v in VIDEOS_1638_1649]
        self.assertEqual(nums, list(range(1638, 1650)))

"""
        t = t.replace(
            "    def test_each_scene_file_defines_the_class(self):",
            insert + "    def test_each_scene_file_defines_the_class(self):",
        )
        t = t.replace(
            "            *VIDEOS_1602_1613,\n        ):",
            "            *VIDEOS_1602_1613,\n"
            "            *VIDEOS_1614_1625,\n"
            "            *VIDEOS_1626_1637,\n"
            "            *VIDEOS_1638_1649,\n"
            "        ):",
        )
        tp.write_text(t, encoding="utf-8")

    plan = ROOT / "project/math/PLAN.md"
    p = plan.read_text(encoding="utf-8")
    if "#1614" not in p:
        extra = "\n\n## 導出つき続き（#1614–#1625）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[:12]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#1626–#1637）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[12:24]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#1638–#1649）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[24:]:
            extra += f"| {num} | {title} | 実装 |\n"
        p = p.replace("## 1 本の作業フロー", extra + "\n## 1 本の作業フロー")
        plan.write_text(p, encoding="utf-8")

    print("created", created[0][0], "-", created[-1][0])


if __name__ == "__main__":
    main()
