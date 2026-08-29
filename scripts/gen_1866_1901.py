#!/usr/bin/env python3
"""Generate #1866–#1901 with derive/proof beats."""
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
    (1866, "ログ有理対", "1866_log_rational_pair", "LogRationalPair", "749_analysis_148", "box",
     ["ログ有理", "有理連結", "境界"], ["定義", "判定"], [r"X", r"X\dashrightarrow\mathbb{P}^n"], r"X\dashrightarrow\mathbb{P}^n"),
    (1867, "相対ログ有理対", "1867_rel_log_rational", "RelLogRational", "749_analysis_148", "box",
     ["相対ログ有理", "相対有理", "ファイバー"], ["定義", "判定"], [r"X/S", r"X\dashrightarrow_S\mathbb{P}"], r"X\dashrightarrow_S\mathbb{P}"),
    (1868, "ログ双有理対", "1868_log_birational_pair", "LogBirationalPair", "749_analysis_148", "box",
     ["ログ双有理", "双有理写像", "境界"], ["定義", "写像"], [r"X\dashrightarrow Y", r"(X,D)\dashrightarrow(Y,D')"], r"(X,D)\dashrightarrow(Y,D')"),
    (1869, "RMSBoundClip", "1869_rmsboundclip", "RMSBoundClip", "750_linear_148", "opt",
     ["RMS境界クリップ", "二乗平均", "枠"], ["核", "境界クリップ"], [r"v\leftarrow\beta v+(1-\beta)g^2", r"\eta\leftarrow\mathrm{clip}(\eta)"], r"\eta\leftarrow\mathrm{clip}(\eta)\in[L,U]"),
    (1870, "LAMBSoftBound", "1870_lambsoftbound", "LAMBSoftBound", "750_linear_148", "opt",
     ["LAMB軟境界", "層信頼域", "平滑枠"], ["核", "軟境界"], [r"r\leftarrow\|w\|/\|\hat u\|", r"r\leftarrow\mathrm{soft}(r)\in[L,U]"], r"r\leftarrow\mathrm{soft}(\mathrm{clip}(r))"),
    (1871, "LookaheadSoftBound", "1871_lookaheadsoftbound", "LookaheadSoftBound", "750_linear_148", "opt",
     ["Lookahead軟境界", "外側平均", "平滑枠"], ["核", "軟境界"], [r"x\leftarrow x+\alpha(y-x)", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{clip}(\eta))"),
    (1872, "内心類似フォイエル中心比", "1872_in_sym_feuer_center", "InSymFeuerCenter", "751_geometry_148", "tri",
     ["内心類似中心", "九点円心", "比"], ["配置", "比"], [r"I", r"IN_s/r"], r"IN_s/r"),
    (1873, "傍心類似フォイエル中心比", "1873_ex_sym_feuer_center", "ExSymFeuerCenter", "751_geometry_148", "tri",
     ["傍心類似中心", "九点円心", "比"], ["配置", "比"], [r"I_a", r"I_aN_s/r_a"], r"I_aN_s/r_a"),
    (1874, "外心類似フォイエル中心比", "1874_o_sym_feuer_center", "OSymFeuerCenter", "751_geometry_148", "tri",
     ["外心類似中心", "九点円心", "比"], ["配置", "比"], [r"O", r"ON_s/R"], r"ON_s/R"),
    (1875, "局所スケール被覆", "1875_local_scale_covering", "LocalScaleCovering", "752_probability_146", "pts",
     ["局所スケール被覆", "半径依存", "サイズ"], ["定義", "サイズ"], [r"N(r,\epsilon)", r"N\propto(r/\epsilon)^d"], r"N\propto(r/\epsilon)^d"),
    (1876, "局所スケールパッキング", "1876_local_scale_packing", "LocalScalePacking", "752_probability_146", "pts",
     ["局所スケールパッキング", "半径依存", "分離"], ["定義", "サイズ"], [r"M(r,\epsilon)", r"M\propto(r/\epsilon)^d"], r"M\propto(r/\epsilon)^d"),
    (1877, "根つき増加木細分", "1877_rooted_inc_tree_refine", "RootedIncTreeRefine", "753_combinatorics_145", "nums",
     ["根つき増加木", "根と増加", "細分"], ["定義", "細分"], [r"RI_n", r"RI(n,k)"], r"RI(n,k)", [1, 1, 3, 13, 71]),
    (1878, "相対ログ双有理対", "1878_rel_log_birational", "RelLogBirational", "754_analysis_149", "box",
     ["相対ログ双有理", "相対双有理", "ファイバー"], ["定義", "写像"], [r"X\dashrightarrow_S Y", r"(X,D)\dashrightarrow_S(Y,D')"], r"(X,D)\dashrightarrow_S(Y,D')"),
    (1879, "ログ射影対", "1879_log_proj_pair", "LogProjPair", "754_analysis_149", "box",
     ["ログ射影", "射影埋め込み", "境界"], ["定義", "埋め込み"], [r"|L|", r"X\hookrightarrow\mathbb{P}^N"], r"X\hookrightarrow\mathbb{P}^N"),
    (1880, "相対ログ射影対", "1880_rel_log_proj", "RelLogProj", "754_analysis_149", "box",
     ["相対ログ射影", "相対埋め込み", "ファイバー"], ["定義", "埋め込み"], [r"|L|/S", r"X\hookrightarrow_S\mathbb{P}"], r"X\hookrightarrow_S\mathbb{P}"),
    (1881, "ProdigyBoundClip", "1881_prodigyboundclip", "ProdigyBoundClip", "755_linear_149", "opt",
     ["Prodigy境界クリップ", "D推定", "枠"], ["核", "境界クリップ"], [r"d\leftarrow\|g\|", r"\eta\leftarrow\mathrm{clip}(\eta)"], r"\eta\leftarrow\mathrm{clip}(\eta)\in[L,U]"),
    (1882, "ScheduleFreeBoundHard", "1882_schedulefreeboundhard", "ScheduleFreeBoundHard", "755_linear_149", "opt",
     ["平均化境界硬閾", "スケジュール不要", "枠剪定"], ["核", "硬境界"], [r"z\leftarrow(1-c)z+cx", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{clip}(\eta))"),
    (1883, "AdamWBoundClip", "1883_adamwboundclip", "AdamWBoundClip", "755_linear_149", "opt",
     ["AdamW境界クリップ", "減衰つき", "枠"], ["核", "境界クリップ"], [r"u\leftarrow\hat m/\sqrt{\hat v}", r"\eta\leftarrow\mathrm{clip}(\eta)"], r"\eta\leftarrow\mathrm{clip}(\eta)\in[L,U]"),
    (1884, "垂心類似フォイエル中心比", "1884_h_sym_feuer_center", "HSymFeuerCenter", "756_geometry_149", "tri",
     ["垂心類似中心", "九点円心", "比"], ["配置", "比"], [r"H", r"HN_s/R"], r"HN_s/R"),
    (1885, "重心類似フォイエル中心比", "1885_g_sym_feuer_center", "GSymFeuerCenter", "756_geometry_149", "tri",
     ["重心類似中心", "九点円心", "比"], ["配置", "比"], [r"G", r"GN_s/\ell"], r"GN_s/\ell"),
    (1886, "九点類似フォイエル中心比", "1886_n_sym_feuer_center", "NSymFeuerCenter", "756_geometry_149", "tri",
     ["九点円類似中心", "中心", "比"], ["配置", "比"], [r"N", r"R_N=R/2"], r"R_N=R/2"),
    (1887, "経験スケール被覆", "1887_emp_scale_covering", "EmpScaleCovering", "757_probability_147", "pts",
     ["経験スケール被覆", "データ半径", "サイズ"], ["定義", "サイズ"], [r"N_n(r,\epsilon)", r"N_n\propto(r/\epsilon)^d"], r"N_n\propto(r/\epsilon)^d"),
    (1888, "経験スケールパッキング", "1888_emp_scale_packing", "EmpScalePacking", "757_probability_147", "pts",
     ["経験スケールパッキング", "データ半径", "分離"], ["定義", "サイズ"], [r"M_n(r,\epsilon)", r"M_n\propto(r/\epsilon)^d"], r"M_n\propto(r/\epsilon)^d"),
    (1889, "ラベル森細分", "1889_labeled_forest_refine", "LabeledForestRefine", "758_combinatorics_146", "nums",
     ["ラベル森", "頂点ラベル", "細分"], ["定義", "細分"], [r"LF_n", r"LF(n,k)"], r"LF(n,k)", [1, 2, 7, 38, 291]),
    (1890, "ログファノ対", "1890_log_fano_pair", "LogFanoPair", "759_analysis_150", "box",
     ["ログファノ", "反豊富", "境界"], ["定義", "判定"], [r"-(K+D)", r"-(K+D)>0"], r"-(K+D)>0"),
    (1891, "相対ログファノ対", "1891_rel_log_fano", "RelLogFano", "759_analysis_150", "box",
     ["相対ログファノ", "相対反豊富", "ファイバー"], ["定義", "判定"], [r"-(K+D)|_F", r"-(K+D)|_F>0"], r"-(K+D)|_F>0"),
    (1892, "ログアルバネーゼ対", "1892_log_albanese_pair", "LogAlbanesePair", "759_analysis_150", "box",
     ["ログアルバネーゼ", "アルバネーゼ射", "境界"], ["定義", "射"], [r"alb", r"alb:X\to Alb"], r"alb:X\to Alb"),
    (1893, "LionWSoftBound", "1893_lionwsoftbound", "LionWSoftBound", "760_linear_150", "opt",
     ["LionW軟境界", "減衰符号", "平滑枠"], ["核", "軟境界"], [r"x\leftarrow x-\eta\mathrm{sign}(m)-\lambda x", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{clip}(\eta))"),
    (1894, "SophiaWSoftBound", "1894_sophiawsoftbound", "SophiaWSoftBound", "760_linear_150", "opt",
     ["SophiaW軟境界", "減衰二階", "平滑枠"], ["核", "軟境界"], [r"\theta\leftarrow\theta-\eta m/\hat H-\lambda\theta", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{clip}(\eta))"),
    (1895, "ApolloBoundClip", "1895_apolloboundclip", "ApolloBoundClip", "760_linear_150", "opt",
     ["Apollo境界クリップ", "準ニュートン", "枠"], ["核", "境界クリップ"], [r"B\leftarrow B+uu^\top", r"\eta\leftarrow\mathrm{clip}(\eta)"], r"\eta\leftarrow\mathrm{clip}(\eta)\in[L,U]"),
    (1896, "内心フォイエル半径比", "1896_in_feuer_radius", "InFeuerRadius", "761_geometry_150", "tri",
     ["内心フォイエル半径", "九点円半径", "比"], ["配置", "比"], [r"I", r"r/R_N"], r"r/R_N"),
    (1897, "傍心フォイエル半径比", "1897_ex_feuer_radius", "ExFeuerRadius", "761_geometry_150", "tri",
     ["傍心フォイエル半径", "九点円半径", "比"], ["配置", "比"], [r"I_a", r"r_a/R_N"], r"r_a/R_N"),
    (1898, "外心フォイエル半径比", "1898_o_feuer_radius", "OFeuerRadius", "761_geometry_150", "tri",
     ["外心フォイエル半径", "九点円半径", "比"], ["配置", "比"], [r"O", r"R/R_N"], r"R/R_N=2"),
    (1899, "一様スケール被覆", "1899_uniform_scale_covering", "UniformScaleCovering", "762_probability_148", "pts",
     ["一様スケール被覆", "全空間半径", "サイズ"], ["定義", "サイズ"], [r"N_u(r,\epsilon)", r"N_u\propto(r/\epsilon)^d"], r"N_u\propto(r/\epsilon)^d"),
    (1900, "一様スケールパッキング", "1900_uniform_scale_packing", "UniformScalePacking", "762_probability_148", "pts",
     ["一様スケールパッキング", "全空間半径", "分離"], ["定義", "サイズ"], [r"M_u(r,\epsilon)", r"M_u\propto(r/\epsilon)^d"], r"M_u\propto(r/\epsilon)^d"),
    (1901, "ケイリー森細分", "1901_cayley_forest_refine", "CayleyForestRefine", "763_combinatorics_147", "nums",
     ["ケイリー森", "森の公式", "細分"], ["定義", "細分"], [r"CF_n", r"CF(n,k)"], r"CF(n,k)", [1, 2, 7, 38, 291]),
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
    assert "VIDEOS_1866_1877" not in text

    def block(name, items):
        lines = [f"\n\n{name}: tuple[Video, ...] = ("]
        for num, title, path, cls in items:
            lines.append(f'    Video({num}, "{title}", "{path}", "{cls}"),')
        lines.append(")")
        return "\n".join(lines)

    cp.write_text(
        text.rstrip()
        + block("VIDEOS_1866_1877", created[:12])
        + block("VIDEOS_1878_1889", created[12:24])
        + block("VIDEOS_1890_1901", created[24:])
        + "\n",
        encoding="utf-8",
    )

    tp = ROOT / "tests/test_catalog.py"
    t = tp.read_text(encoding="utf-8")
    if "VIDEOS_1866_1877" not in t:
        t = t.replace(
            "VIDEOS_1854_1865 = _catalog.VIDEOS_1854_1865\n",
            "VIDEOS_1854_1865 = _catalog.VIDEOS_1854_1865\n"
            "VIDEOS_1866_1877 = _catalog.VIDEOS_1866_1877\n"
            "VIDEOS_1878_1889 = _catalog.VIDEOS_1878_1889\n"
            "VIDEOS_1890_1901 = _catalog.VIDEOS_1890_1901\n",
        )
        insert = """
    def test_numbers_are_1866_to_1877(self):
        nums = [v.number for v in VIDEOS_1866_1877]
        self.assertEqual(nums, list(range(1866, 1878)))


    def test_numbers_are_1878_to_1889(self):
        nums = [v.number for v in VIDEOS_1878_1889]
        self.assertEqual(nums, list(range(1878, 1890)))


    def test_numbers_are_1890_to_1901(self):
        nums = [v.number for v in VIDEOS_1890_1901]
        self.assertEqual(nums, list(range(1890, 1902)))

"""
        t = t.replace(
            "    def test_each_scene_file_defines_the_class(self):",
            insert + "    def test_each_scene_file_defines_the_class(self):",
        )
        t = t.replace(
            "            *VIDEOS_1854_1865,\n        ):",
            "            *VIDEOS_1854_1865,\n"
            "            *VIDEOS_1866_1877,\n"
            "            *VIDEOS_1878_1889,\n"
            "            *VIDEOS_1890_1901,\n"
            "        ):",
        )
        tp.write_text(t, encoding="utf-8")

    plan = ROOT / "project/math/PLAN.md"
    p = plan.read_text(encoding="utf-8")
    if "#1866" not in p:
        extra = "\n\n## 導出つき続き（#1866–#1877）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[:12]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#1878–#1889）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[12:24]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#1890–#1901）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[24:]:
            extra += f"| {num} | {title} | 実装 |\n"
        p = p.replace("## 1 本の作業フロー", extra + "\n## 1 本の作業フロー")
        plan.write_text(p, encoding="utf-8")

    print("created", created[0][0], "-", created[-1][0])


if __name__ == "__main__":
    main()
