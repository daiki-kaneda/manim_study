#!/usr/bin/env python3
"""Generate #1938–#1973 with derive/proof beats."""
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
    (1938, "ログ小平対", "1938_log_kodaira_pair", "LogKodairaPair", "779_analysis_154", "box",
     ["ログ小平", "次元分類", "境界"], ["定義", "値"], [r"\kappa(X,K+D)", r"\kappa\in\{-\infty,0,\ldots,n\}"], r"\kappa(X,K+D)"),
    (1939, "相対ログ小平対", "1939_rel_log_kodaira", "RelLogKodaira", "779_analysis_154", "box",
     ["相対ログ小平", "相対次元", "ファイバー"], ["定義", "値"], [r"\kappa(X/S,K+D)", r"\kappa(X/S,K+D)"], r"\kappa(X/S,K+D)"),
    (1940, "ログ飯高ファイバー対", "1940_log_iitaka_fiber", "LogIitakaFiber", "779_analysis_154", "box",
     ["ログ飯高ファイバー", "飯高射", "ファイバー"], ["写像", "ファイバー"], [r"\phi_{|m(K+D)|}", r"F=\phi^{-1}(pt)"], r"F=\phi^{-1}(pt)"),
    (1941, "RMSSoftBoundClip", "1941_rmssoftboundclip", "RMSSoftBoundClip", "780_linear_154", "opt",
     ["RMS軟境界クリップ", "二乗平均", "三重"], ["核", "軟境界"], [r"v\leftarrow\beta v+(1-\beta)g^2", r"\eta\leftarrow\mathrm{clip}(\mathrm{soft}(\eta))"], r"\eta\leftarrow\mathrm{clip}(\mathrm{soft}(\eta))\in[L,U]"),
    (1942, "LAMBBoundClip", "1942_lambboundclip", "LAMBBoundClip", "780_linear_154", "opt",
     ["LAMB境界クリップ", "層信頼域", "枠"], ["核", "境界クリップ"], [r"r\leftarrow\|w\|/\|\hat u\|", r"r\leftarrow\mathrm{clip}(r)"], r"r\leftarrow\mathrm{clip}(r)\in[L,U]"),
    (1943, "AdamWSoftBoundClip", "1943_adamwsoftboundclip", "AdamWSoftBoundClip", "780_linear_154", "opt",
     ["AdamW軟境界クリップ", "減衰つき", "三重"], ["核", "軟境界"], [r"u\leftarrow\hat m/\sqrt{\hat v}", r"\eta\leftarrow\mathrm{clip}(\mathrm{soft}(\eta))"], r"\eta\leftarrow\mathrm{clip}(\mathrm{soft}(\eta))\in[L,U]"),
    (1944, "内心九点弦比", "1944_in_nine_chord", "InNineChord", "781_geometry_154", "tri",
     ["内心九点弦", "九点円弦", "比"], ["配置", "比"], [r"I", r"\ell_9/r"], r"\ell_9/r"),
    (1945, "傍心九点弦比", "1945_ex_nine_chord", "ExNineChord", "781_geometry_154", "tri",
     ["傍心九点弦", "九点円弦", "比"], ["配置", "比"], [r"I_a", r"\ell_9/r_a"], r"\ell_9/r_a"),
    (1946, "外心九点弦比", "1946_o_nine_chord", "ONineChord", "781_geometry_154", "tri",
     ["外心九点弦", "九点円弦", "比"], ["配置", "比"], [r"O", r"\ell_9/R"], r"\ell_9/R"),
    (1947, "データ半径エントロピー", "1947_data_radius_entropy", "DataRadiusEntropy", "782_probability_152", "pts",
     ["データ半径エントロピー", "標本半径", "対数"], ["定義", "依存"], [r"H_n(r,\epsilon)", r"H_n\propto r^{\alpha}"], r"H_n\propto r^{\alpha}"),
    (1948, "標本半径複雑度", "1948_sample_radius_comp", "SampleRadiusComp", "782_probability_152", "pts",
     ["標本半径複雑度", "有限標本", "上界"], ["定義", "上界"], [r"\mathfrak{C}_n(r)", r"\mathfrak{C}_n(r)\le C r^{\alpha}"], r"\mathfrak{C}_n(r)\le C r^{\alpha}"),
    (1949, "減少森細分", "1949_dec_forest_refine", "DecForestRefine", "783_combinatorics_151", "nums",
     ["減少森", "ラベル減少", "細分"], ["定義", "細分"], [r"DF_n", r"DF(n,k)"], r"DF(n,k)", [1, 2, 7, 38, 291]),
    (1950, "相対ログ飯高ファイバー対", "1950_rel_log_iitaka_fiber", "RelLogIitakaFiber", "784_analysis_155", "box",
     ["相対ログ飯高ファイバー", "相対飯高射", "ファイバー"], ["写像", "ファイバー"], [r"\phi/S", r"F=\phi^{-1}(pt)"], r"F=\phi^{-1}(pt)"),
    (1951, "ログ随伴対", "1951_log_adjoint_pair", "LogAdjointPair", "784_analysis_155", "box",
     ["ログ随伴", "随伴環", "境界"], ["定義", "環"], [r"R(K+D)", r"R=\bigoplus H^0(m(K+D))"], r"R(K+D)"),
    (1952, "相対ログ随伴対", "1952_rel_log_adjoint", "RelLogAdjoint", "784_analysis_155", "box",
     ["相対ログ随伴", "相対随伴", "ファイバー"], ["定義", "環"], [r"R(K+D/S)", r"R=\bigoplus H^0(m(K+D))"], r"R(K+D/S)"),
    (1953, "ScheduleFreeSoftBound", "1953_schedulefreesoftbound", "ScheduleFreeSoftBound", "785_linear_155", "opt",
     ["平均化軟境界", "スケジュール不要", "平滑枠"], ["核", "軟境界"], [r"z\leftarrow(1-c)z+cx", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{clip}(\eta))"),
    (1954, "ApolloHardBound", "1954_apollohardbound", "ApolloHardBound", "785_linear_155", "opt",
     ["Apollo硬境界", "準ニュートン", "枠剪定"], ["核", "硬境界"], [r"B\leftarrow B+uu^\top", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{clip}(\eta))"),
    (1955, "MuonSoftHardBound", "1955_muonsofthardbound", "MuonSoftHardBound", "785_linear_155", "opt",
     ["Muon軟硬境界", "直交更新", "枠二段"], ["軟", "硬"], [r"\eta\leftarrow\mathrm{soft}(\eta)", r"\eta\leftarrow\mathrm{hard}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{hard}(\mathrm{soft}(\mathrm{clip}(\eta)))"),
    (1956, "垂心九点弦比", "1956_h_nine_chord", "HNineChord", "786_geometry_155", "tri",
     ["垂心九点弦", "九点円弦", "比"], ["配置", "比"], [r"H", r"\ell_9/R"], r"\ell_9/R"),
    (1957, "重心九点弦比", "1957_g_nine_chord", "GNineChord", "786_geometry_155", "tri",
     ["重心九点弦", "九点円弦", "比"], ["配置", "比"], [r"G", r"\ell_9/\ell"], r"\ell_9/\ell"),
    (1958, "九点弦長比", "1958_n_nine_chord", "NNineChord", "786_geometry_155", "tri",
     ["九点弦長", "弦", "比"], ["配置", "比"], [r"N", r"\ell_9/R_N"], r"\ell_9/R_N"),
    (1959, "局所標本スケール被覆", "1959_local_sample_scale_cov", "LocalSampleScaleCov", "787_probability_153", "pts",
     ["局所標本スケール被覆", "半径標本", "サイズ"], ["定義", "サイズ"], [r"N_n(B,r,\epsilon)", r"N_n\lesssim(r/\epsilon)^d"], r"N_n\lesssim(r/\epsilon)^d"),
    (1960, "局所標本スケールパッキング", "1960_local_sample_scale_pack", "LocalSampleScalePack", "787_probability_153", "pts",
     ["局所標本スケールパッキング", "半径標本", "分離"], ["定義", "サイズ"], [r"M_n(B,r,\epsilon)", r"M_n\lesssim(r/\epsilon)^d"], r"M_n\lesssim(r/\epsilon)^d"),
    (1961, "根つき三分木細分", "1961_rooted_ternary_refine", "RootedTernaryRefine", "788_combinatorics_152", "nums",
     ["根つき三分木", "根と三分岐", "細分"], ["定義", "細分"], [r"RT_n", r"RT(n,k)"], r"RT(n,k)", [1, 1, 3, 12, 55]),
    (1962, "ログ随伴豊富対", "1962_log_adj_ample", "LogAdjAmple", "789_analysis_156", "box",
     ["ログ随伴豊富", "随伴豊富", "境界"], ["定義", "判定"], [r"K+D", r"K+D>0"], r"K+D>0"),
    (1963, "相対ログ随伴豊富対", "1963_rel_log_adj_ample", "RelLogAdjAmple", "789_analysis_156", "box",
     ["相対ログ随伴豊富", "相対随伴豊富", "ファイバー"], ["定義", "判定"], [r"(K+D)|_F", r"(K+D)|_F>0"], r"(K+D)|_F>0"),
    (1964, "ログ随伴ネフ対", "1964_log_adj_nef", "LogAdjNef", "789_analysis_156", "box",
     ["ログ随伴ネフ", "随伴ネフ", "境界"], ["定義", "判定"], [r"(K+D).C", r"(K+D).C\ge 0"], r"(K+D).C\ge 0"),
    (1965, "SamSoftBoundClip", "1965_samsoftboundclip", "SamSoftBoundClip", "790_linear_156", "opt",
     ["SAM軟境界クリップ", "鋭度", "三重"], ["核", "軟境界"], [r"\epsilon\leftarrow\rho g/\|g\|", r"\rho\leftarrow\mathrm{clip}(\mathrm{soft}(\rho))"], r"\rho\leftarrow\mathrm{clip}(\mathrm{soft}(\rho))\in[L,U]"),
    (1966, "NAdamSoftBoundClip", "1966_nadamsoftboundclip", "NAdamSoftBoundClip", "790_linear_156", "opt",
     ["NAdam軟境界クリップ", "ネステロフ", "三重"], ["核", "軟境界"], [r"m\leftarrow\beta m+(1-\beta)g", r"\eta\leftarrow\mathrm{clip}(\mathrm{soft}(\eta))"], r"\eta\leftarrow\mathrm{clip}(\mathrm{soft}(\eta))\in[L,U]"),
    (1967, "LARSSoftBound", "1967_larssoftbound", "LARSSoftBound", "790_linear_156", "opt",
     ["LARS軟境界", "層正規化", "平滑枠"], ["核", "軟境界"], [r"\eta\leftarrow\|w\|/\|g\|", r"\eta\leftarrow\mathrm{soft}(\eta)\in[L,U]"], r"\eta\leftarrow\mathrm{soft}(\mathrm{clip}(\eta))"),
    (1968, "内心類似九点弦比", "1968_in_sym_nine_chord", "InSymNineChord", "791_geometry_156", "tri",
     ["内心類似九点弦", "九点円弦", "比"], ["配置", "比"], [r"I", r"\ell_{9,s}/r"], r"\ell_{9,s}/r"),
    (1969, "傍心類似九点弦比", "1969_ex_sym_nine_chord", "ExSymNineChord", "791_geometry_156", "tri",
     ["傍心類似九点弦", "九点円弦", "比"], ["配置", "比"], [r"I_a", r"\ell_{9,s}/r_a"], r"\ell_{9,s}/r_a"),
    (1970, "外心類似九点弦比", "1970_o_sym_nine_chord", "OSymNineChord", "791_geometry_156", "tri",
     ["外心類似九点弦", "九点円弦", "比"], ["配置", "比"], [r"O", r"\ell_{9,s}/R"], r"\ell_{9,s}/R"),
    (1971, "経験一様スケール被覆", "1971_emp_unif_scale_cov", "EmpUnifScaleCov", "792_probability_154", "pts",
     ["経験一様スケール被覆", "データ一様半径", "サイズ"], ["定義", "サイズ"], [r"N_{n,u}(r,\epsilon)", r"N_{n,u}\lesssim(r/\epsilon)^d"], r"N_{n,u}\lesssim(r/\epsilon)^d"),
    (1972, "経験一様スケールパッキング", "1972_emp_unif_scale_pack", "EmpUnifScalePack", "792_probability_154", "pts",
     ["経験一様スケールパッキング", "データ一様半径", "分離"], ["定義", "サイズ"], [r"M_{n,u}(r,\epsilon)", r"M_{n,u}\lesssim(r/\epsilon)^d"], r"M_{n,u}\lesssim(r/\epsilon)^d"),
    (1973, "ラベル三分木細分", "1973_labeled_ternary_refine", "LabeledTernaryRefine", "793_combinatorics_153", "nums",
     ["ラベル三分木", "三分岐ラベル", "細分"], ["定義", "細分"], [r"LT_n", r"LT(n,k)"], r"LT(n,k)", [1, 1, 3, 12, 55]),
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
    assert "VIDEOS_1938_1949" not in text

    def block(name, items):
        lines = [f"\n\n{name}: tuple[Video, ...] = ("]
        for num, title, path, cls in items:
            lines.append(f'    Video({num}, "{title}", "{path}", "{cls}"),')
        lines.append(")")
        return "\n".join(lines)

    cp.write_text(
        text.rstrip()
        + block("VIDEOS_1938_1949", created[:12])
        + block("VIDEOS_1950_1961", created[12:24])
        + block("VIDEOS_1962_1973", created[24:])
        + "\n",
        encoding="utf-8",
    )

    tp = ROOT / "tests/test_catalog.py"
    t = tp.read_text(encoding="utf-8")
    if "VIDEOS_1938_1949" not in t:
        t = t.replace(
            "VIDEOS_1926_1937 = _catalog.VIDEOS_1926_1937\n",
            "VIDEOS_1926_1937 = _catalog.VIDEOS_1926_1937\n"
            "VIDEOS_1938_1949 = _catalog.VIDEOS_1938_1949\n"
            "VIDEOS_1950_1961 = _catalog.VIDEOS_1950_1961\n"
            "VIDEOS_1962_1973 = _catalog.VIDEOS_1962_1973\n",
        )
        insert = """
    def test_numbers_are_1938_to_1949(self):
        nums = [v.number for v in VIDEOS_1938_1949]
        self.assertEqual(nums, list(range(1938, 1950)))


    def test_numbers_are_1950_to_1961(self):
        nums = [v.number for v in VIDEOS_1950_1961]
        self.assertEqual(nums, list(range(1950, 1962)))


    def test_numbers_are_1962_to_1973(self):
        nums = [v.number for v in VIDEOS_1962_1973]
        self.assertEqual(nums, list(range(1962, 1974)))

"""
        t = t.replace(
            "    def test_each_scene_file_defines_the_class(self):",
            insert + "    def test_each_scene_file_defines_the_class(self):",
        )
        t = t.replace(
            "            *VIDEOS_1926_1937,\n        ):",
            "            *VIDEOS_1926_1937,\n"
            "            *VIDEOS_1938_1949,\n"
            "            *VIDEOS_1950_1961,\n"
            "            *VIDEOS_1962_1973,\n"
            "        ):",
        )
        tp.write_text(t, encoding="utf-8")

    plan = ROOT / "project/math/PLAN.md"
    p = plan.read_text(encoding="utf-8")
    if "#1938" not in p:
        extra = "\n\n## 導出つき続き（#1938–#1949）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[:12]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#1950–#1961）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[12:24]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#1962–#1973）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[24:]:
            extra += f"| {num} | {title} | 実装 |\n"
        p = p.replace("## 1 本の作業フロー", extra + "\n## 1 本の作業フロー")
        plan.write_text(p, encoding="utf-8")

    print("created", created[0][0], "-", created[-1][0])


if __name__ == "__main__":
    main()
