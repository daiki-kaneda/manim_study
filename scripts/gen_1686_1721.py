#!/usr/bin/env python3
"""Generate #1686–#1721 with derive/proof beats."""
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
    (1686, "相対ログ簡約対", "1686_rel_log_slc", "RelLogSlc", "674_analysis_133", "box",
     ["相対ログ簡約", "半対数標準", "ファイバー"], ["定義", "判定"], [r"a(E,X/S,D)", r"a(E,X/S,D)\ge -1"], r"a(E,X/S,D)\ge -1"),
    (1687, "ログ平坦対", "1687_log_flat_pair", "LogFlatPair", "674_analysis_133", "box",
     ["ログ平坦", "平坦族", "相対"], ["定義", "条件"], [r"(X,D)/S", r"f:(X,D)\to S"], r"f:(X,D)\to S"),
    (1688, "相対ログ平坦対", "1688_rel_log_flat", "RelLogFlat", "674_analysis_133", "box",
     ["相対ログ平坦", "平坦射", "ファイバー"], ["定義", "条件"], [r"f:X\to S", r"f\ \mathrm{flat}"], r"f:X\to S"),
    (1689, "LAMBBoundSoft", "1689_lambboundsoft", "LAMBBoundSoft", "675_linear_133", "opt",
     ["LAMB境界軟化", "層信頼域", "平滑"], ["核", "軟境界"], [r"r\leftarrow\|w\|/\|\hat u\|", r"r\leftarrow\mathrm{soft}(r)"], r"r\leftarrow\mathrm{soft}(\mathrm{clip}(r))"),
    (1690, "ApolloBound", "1690_apollobound", "ApolloBound", "675_linear_133", "opt",
     ["Apollo境界", "準ニュートン", "枠"], ["核", "境界"], [r"B\leftarrow B+uu^\top", r"\eta\in[L,U]"], r"\eta\in[L,U]"),
    (1691, "ApolloSoftHard", "1691_apollosofthard", "ApolloSoftHard", "675_linear_133", "opt",
     ["Apollo軟硬", "準ニュートン", "二段"], ["軟", "硬"], [r"u\leftarrow\mathrm{soft}(u)", r"u\leftarrow\mathrm{hard}(u)"], r"u\leftarrow\mathrm{hard}(\mathrm{soft}(u))"),
    (1692, "垂心フォイエル接点比", "1692_h_feuerbach_touch", "HFeuerbachTouch", "676_geometry_133", "tri",
     ["垂心接点比", "九点円", "比"], ["配置", "比"], [r"H", r"HT/R"], r"HT/R"),
    (1693, "重心フォイエル接点比", "1693_g_feuerbach_touch", "GFeuerbachTouch", "676_geometry_133", "tri",
     ["重心接点比", "九点円", "比"], ["配置", "比"], [r"G", r"GT/\ell"], r"GT/\ell"),
    (1694, "九点フォイエル接点比", "1694_n_feuerbach_touch", "NFeuerbachTouch", "676_geometry_133", "tri",
     ["九点円接点比", "接点", "比"], ["配置", "比"], [r"N", r"NT/R_N"], r"NT/R_N"),
    (1695, "経験スケール敏感度", "1695_emp_scale_sens", "EmpScaleSens", "677_probability_131", "pts",
     ["経験スケール敏感度", "データ依存", "傾き"], ["定義", "傾き"], [r"\phi_n'(r)", r"\phi_n'(r)\propto r^{\alpha-1}"], r"\phi_n'(r)\propto r^{\alpha-1}"),
    (1696, "局所スケールエントロピー", "1696_local_scale_entropy", "LocalScaleEntropy", "677_probability_131", "pts",
     ["局所スケールエントロピー", "半径球", "対数"], ["定義", "依存"], [r"H(B(f,r),\epsilon)", r"H\propto r^{\alpha}"], r"H\propto r^{\alpha}"),
    (1697, "シュレーダー路細分", "1697_schroeder_path_refine", "SchroederPathRefine", "678_combinatorics_130", "nums",
     ["シュレーダー路", "弱上昇", "細分"], ["定義", "細分"], [r"S_n", r"S(n,k)"], r"S(n,k)", [1, 2, 6, 22, 90]),
    (1698, "ログ正規対", "1698_log_normal_pair", "LogNormalPair", "679_analysis_134", "box",
     ["ログ正規", "正規交叉", "境界"], ["定義", "判定"], [r"(X,D)", r"D=\sum D_i"], r"D=\sum D_i"),
    (1699, "相対ログ正規対", "1699_rel_log_normal", "RelLogNormal", "679_analysis_134", "box",
     ["相対ログ正規", "相対正規交叉", "ファイバー"], ["定義", "判定"], [r"(X,D)/S", r"D=\sum D_i"], r"D=\sum D_i"),
    (1700, "ログクッション対", "1700_log_cushion_pair", "LogCushionPair", "679_analysis_134", "box",
     ["ログクッション", "食い違い余裕", "安定"], ["定義", "余裕"], [r"a(E)+1", r"\delta=\inf(a+1)"], r"\delta=\inf(a+1)"),
    (1701, "LionWHardClip", "1701_lionwhardclip", "LionWHardClip", "680_linear_134", "opt",
     ["LionW硬クリップ", "減衰符号", "硬閾"], ["核", "硬クリップ"], [r"x\leftarrow x-\eta\mathrm{sign}(m)-\lambda x", r"u\leftarrow\mathrm{hard}(\mathrm{clip}(u))"], r"u\leftarrow\mathrm{hard}(\mathrm{clip}(u))"),
    (1702, "SophiaWHardClip", "1702_sophiawhardclip", "SophiaWHardClip", "680_linear_134", "opt",
     ["SophiaW硬クリップ", "減衰二階", "硬閾"], ["核", "硬クリップ"], [r"\theta\leftarrow\theta-\eta m/\hat H-\lambda\theta", r"u\leftarrow\mathrm{hard}(\mathrm{clip}(u))"], r"u\leftarrow\mathrm{hard}(\mathrm{clip}(u))"),
    (1703, "AdaFactorBoundSoft", "1703_adafactorboundsoft", "AdaFactorBoundSoft", "680_linear_134", "opt",
     ["AdaFactor境界軟化", "因子化", "平滑"], ["核", "軟境界"], [r"R_{ij}C_{ij}\approx G_{ij}^2", r"\eta\leftarrow\mathrm{soft}(\eta)"], r"\eta\leftarrow\mathrm{soft}(\mathrm{clip}(\eta))"),
    (1704, "内心類似フォイエル比", "1704_in_sym_feuerbach", "InSymFeuerbach", "681_geometry_134", "tri",
     ["内心と類似フォイエル", "九点円", "比"], ["配置", "比"], [r"I", r"d(I,N)_s/r"], r"d(I,N)_s/r"),
    (1705, "傍心類似フォイエル比", "1705_ex_sym_feuerbach", "ExSymFeuerbach", "681_geometry_134", "tri",
     ["傍心と類似フォイエル", "九点円", "比"], ["配置", "比"], [r"I_a", r"d(I_a,N)_s/r_a"], r"d(I_a,N)_s/r_a"),
    (1706, "外心類似フォイエル比", "1706_o_sym_feuerbach", "OSymFeuerbach", "681_geometry_134", "tri",
     ["外心と類似フォイエル", "九点円", "比"], ["配置", "比"], [r"O", r"ON_s/R"], r"ON_s/R"),
    (1707, "一様半径敏感度", "1707_uniform_radius_sens", "UniformRadiusSens", "682_probability_132", "pts",
     ["一様半径敏感度", "全空間", "傾き"], ["定義", "傾き"], [r"\phi_u'(r)", r"\phi_u'(r)\propto r^{\alpha-1}"], r"\phi_u'(r)\propto r^{\alpha-1}"),
    (1708, "データ依存チャイニング", "1708_data_chaining", "DataChaining", "682_probability_132", "pts",
     ["データ依存チェイニング", "標本階層", "上界"], ["構成", "上界"], [r"\gamma_{2,n}", r"\mathbb{E}\sup X\le C\gamma_{2,n}"], r"\mathbb{E}\sup X\le C\gamma_{2,n}"),
    (1709, "モツキン三角形細分", "1709_motzkin_tri_refine", "MotzkinTriRefine", "683_combinatorics_131", "nums",
     ["モツキン三角形", "配列", "細分"], ["定義", "細分"], [r"M(n,k)", r"M_n=\sum_k M(n,k)"], r"M(n,k)", [1, 1, 2, 4, 9]),
    (1710, "相対ログクッション対", "1710_rel_log_cushion", "RelLogCushion", "684_analysis_135", "box",
     ["相対ログクッション", "相対余裕", "安定"], ["定義", "余裕"], [r"a(E/S)+1", r"\delta=\inf(a+1)"], r"\delta=\inf(a+1)"),
    (1711, "ログ平滑対", "1711_log_smooth_pair", "LogSmoothPair", "684_analysis_135", "box",
     ["ログ平滑", "スムース境界", "正規"], ["定義", "条件"], [r"(X,D)", r"X\ \mathrm{smooth}"], r"X"),
    (1712, "相対ログ平滑対", "1712_rel_log_smooth", "RelLogSmooth", "684_analysis_135", "box",
     ["相対ログ平滑", "相対スムース", "ファイバー"], ["定義", "条件"], [r"(X,D)/S", r"X/S\ \mathrm{smooth}"], r"X/S"),
    (1713, "NAdamHardBound", "1713_nadamhardbound", "NAdamHardBound", "685_linear_135", "opt",
     ["NAdam硬境界", "ネステロフ", "枠剪定"], ["核", "硬境界"], [r"m\leftarrow\beta m+(1-\beta)g", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{clip}(\eta))"),
    (1714, "RMSSoftBound", "1714_rmssoftbound", "RMSSoftBound", "685_linear_135", "opt",
     ["RMS軟境界", "二乗平均", "平滑枠"], ["核", "軟境界"], [r"v\leftarrow\beta v+(1-\beta)g^2", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{clip}(\eta))"),
    (1715, "LAMBSoftHard", "1715_lambsofthard", "LAMBSoftHard", "685_linear_135", "opt",
     ["LAMB軟硬", "層信頼域", "二段"], ["軟", "硬"], [r"r\leftarrow\mathrm{soft}(r)", r"r\leftarrow\mathrm{hard}(r)"], r"r\leftarrow\mathrm{hard}(\mathrm{soft}(r))"),
    (1716, "垂心類似フォイエル比", "1716_h_sym_feuerbach", "HSymFeuerbach", "686_geometry_135", "tri",
     ["垂心と類似フォイエル", "九点円", "比"], ["配置", "比"], [r"H", r"HN_s/R"], r"HN_s/R"),
    (1717, "重心類似フォイエル比", "1717_g_sym_feuerbach", "GSymFeuerbach", "686_geometry_135", "tri",
     ["重心と類似フォイエル", "九点円", "比"], ["配置", "比"], [r"G", r"GN_s/\ell"], r"GN_s/\ell"),
    (1718, "九点類似フォイエル比", "1718_n_sym_feuerbach", "NSymFeuerbach", "686_geometry_135", "tri",
     ["九点円類似フォイエル", "接点", "比"], ["配置", "比"], [r"N", r"NT_s/R_N"], r"NT_s/R_N"),
    (1719, "標本被覆数", "1719_sample_covering", "SampleCovering", "687_probability_133", "pts",
     ["標本被覆数", "有限標本", "サイズ"], ["定義", "サイズ"], [r"N_n(\epsilon)", r"N_n(\epsilon)\le N(\epsilon)"], r"N_n(\epsilon)\le N(\epsilon)"),
    (1720, "標本パッキング数", "1720_sample_packing", "SamplePacking", "687_probability_133", "pts",
     ["標本パッキング数", "有限標本", "分離"], ["定義", "サイズ"], [r"M_n(\epsilon)", r"M_n(\epsilon)\le M(\epsilon)"], r"M_n(\epsilon)\le M(\epsilon)"),
    (1721, "大きなナラヤナ細分", "1721_large_narayana_refine", "LargeNarayanaRefine", "688_combinatorics_132", "nums",
     ["大きなナラヤナ", "拡張", "細分"], ["定義", "細分"], [r"N(n,k;m)", r"C_n^{(m)}=\sum_k N(n,k;m)"], r"N(n,k;m)", [1, 3, 6, 15, 36]),
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
        if num == 1688:
            clean_dtex = [r"f:X\to S", r"f:X\to S"]
            clean_final = r"f:X\to S"
        elif num == 1711:
            clean_dtex = [r"(X,D)", r"X"]
            clean_final = r"X"
        elif num == 1712:
            clean_dtex = [r"(X,D)/S", r"X/S"]
            clean_final = r"X/S"
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
    assert "VIDEOS_1686_1697" not in text

    def block(name, items):
        lines = [f"\n\n{name}: tuple[Video, ...] = ("]
        for num, title, path, cls in items:
            lines.append(f'    Video({num}, "{title}", "{path}", "{cls}"),')
        lines.append(")")
        return "\n".join(lines)

    cp.write_text(
        text.rstrip()
        + block("VIDEOS_1686_1697", created[:12])
        + block("VIDEOS_1698_1709", created[12:24])
        + block("VIDEOS_1710_1721", created[24:])
        + "\n",
        encoding="utf-8",
    )

    tp = ROOT / "tests/test_catalog.py"
    t = tp.read_text(encoding="utf-8")
    if "VIDEOS_1686_1697" not in t:
        t = t.replace(
            "VIDEOS_1674_1685 = _catalog.VIDEOS_1674_1685\n",
            "VIDEOS_1674_1685 = _catalog.VIDEOS_1674_1685\n"
            "VIDEOS_1686_1697 = _catalog.VIDEOS_1686_1697\n"
            "VIDEOS_1698_1709 = _catalog.VIDEOS_1698_1709\n"
            "VIDEOS_1710_1721 = _catalog.VIDEOS_1710_1721\n",
        )
        insert = """
    def test_numbers_are_1686_to_1697(self):
        nums = [v.number for v in VIDEOS_1686_1697]
        self.assertEqual(nums, list(range(1686, 1698)))


    def test_numbers_are_1698_to_1709(self):
        nums = [v.number for v in VIDEOS_1698_1709]
        self.assertEqual(nums, list(range(1698, 1710)))


    def test_numbers_are_1710_to_1721(self):
        nums = [v.number for v in VIDEOS_1710_1721]
        self.assertEqual(nums, list(range(1710, 1722)))

"""
        t = t.replace(
            "    def test_each_scene_file_defines_the_class(self):",
            insert + "    def test_each_scene_file_defines_the_class(self):",
        )
        t = t.replace(
            "            *VIDEOS_1674_1685,\n        ):",
            "            *VIDEOS_1674_1685,\n"
            "            *VIDEOS_1686_1697,\n"
            "            *VIDEOS_1698_1709,\n"
            "            *VIDEOS_1710_1721,\n"
            "        ):",
        )
        tp.write_text(t, encoding="utf-8")

    plan = ROOT / "project/math/PLAN.md"
    p = plan.read_text(encoding="utf-8")
    if "#1686" not in p:
        extra = "\n\n## 導出つき続き（#1686–#1697）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[:12]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#1698–#1709）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[12:24]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#1710–#1721）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[24:]:
            extra += f"| {num} | {title} | 実装 |\n"
        p = p.replace("## 1 本の作業フロー", extra + "\n## 1 本の作業フロー")
        plan.write_text(p, encoding="utf-8")

    print("created", created[0][0], "-", created[-1][0])


if __name__ == "__main__":
    main()
