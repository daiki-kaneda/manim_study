#!/usr/bin/env python3
"""Regenerate #1326–#1397 with derive/proof beats for ~40–45s pacing."""
from __future__ import annotations

import ast
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

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


CONTENT: dict[int, dict] = {}


def add(num, kind, notes, dnotes, dtex, final, vals=None, slug=None, cls=None, season=None, title=None):
    CONTENT[num] = dict(
        kind=kind,
        notes=notes,
        dnotes=dnotes,
        dtex=dtex,
        final=final,
        vals=vals,
        slug=slug,
        cls=cls,
        season=season,
        title=title,
    )


# 1326-1361
add(1326, "box", ["因子的端末", "特異点の類", "食い違い正"], ["定義から", "例外因子で"], [r"a(E;X,D)", r"a(E)>0"], r"a(E)>0")
add(1327, "box", ["因子的正準", "非負の食い違い", "境界つき"], ["定義", "判定"], [r"a(E;X,D)", r"a(E)\ge 0"], r"a(E)\ge 0")
add(1328, "box", ["因子的klt", "強い端末", "対数端末"], ["下限", "結論"], [r"a(E)>-1", r"a(E)>-1"], r"a(E)>-1")
add(1329, "opt", ["Lionに重み減衰", "符号更新", "クリップ"], ["更新式", "減衰を合成"], [r"x\leftarrow x-\eta\,\mathrm{sign}(m)", r"x\leftarrow x-\lambda x"], r"x\leftarrow\mathrm{clip}(x-\eta\mathrm{sign}(m)-\lambda x)")
add(1330, "opt", ["Sophiaに重み減衰", "二階情報", "クリップ"], ["Hessian近似", "減衰付き"], [r"\theta\leftarrow\theta-\eta m/\hat H", r"\theta\leftarrow\theta-\lambda\theta"], r"\theta\leftarrow\mathrm{clip}(\theta-\eta m/\hat H-\lambda\theta)")
add(1331, "opt", ["Muonに重み減衰", "直交更新", "クリップ"], ["Muon核", "減衰"], [r"U\leftarrow\mathrm{Muon}(G)", r"U\leftarrow U-\lambda W"], r"W\leftarrow\mathrm{clip}(W-\eta U-\lambda W)")
add(1332, "tri", ["スチュワート", "中線の長さ", "辺で表す"], ["公式の核", "中線特例"], [r"a(d^2+mn)=b^2m+c^2n", r"m_a=\frac{1}{2}\sqrt{2b^2+2c^2-a^2}"], r"m_a=\frac{1}{2}\sqrt{2b^2+2c^2-a^2}")
add(1333, "tri", ["アポロニウス", "中線比", "辺の二乗"], ["定理", "比へ"], [r"b^2+c^2=2m_a^2+\frac{1}{2}a^2", r"b^2+c^2=2m_a^2+\frac{1}{2}a^2"], r"b^2+c^2=2m_a^2+\frac{1}{2}a^2")
add(1334, "tri", ["直角の拡張", "余弦経由", "比の形"], ["余弦定理", "整理"], [r"c^2=a^2+b^2-2ab\cos C", r"c^2=a^2+b^2-2ab\cos C"], r"c^2=a^2+b^2-2ab\cos C")
add(1335, "pts", ["PAC上界", "仮説集合", "標本数"], ["失敗確率", "解いてn"], [r"P(err>\epsilon)\le\delta", r"n\gtrsim\frac{1}{\epsilon^2}\log\frac{|H|}{\delta}"], r"n\gtrsim\epsilon^{-2}\log(|H|/\delta)")
add(1336, "pts", ["VC次元", "粉砕", "成長関数"], ["定義", "サウアーへ"], [r"VCdim(H)=d", r"\Pi_H(n)\le\sum_{i=0}^d\binom{n}{i}"], r"VCdim=d")
add(1337, "nums", ["カタラン路", "細分計数", "再帰"], ["定義", "細分"], [r"C_n=\frac{1}{n+1}\binom{2n}{n}", r"C(n,k)"], r"C(n,k)", [1, 2, 5, 14, 42])
add(1338, "box", ["因子的plt", "純対数端末", "境界条件"], ["食い違い", "plt"], [r"a(E)\ge -1", r"a(E)\ge -1"], r"a(E)\ge -1")
add(1339, "box", ["因子的dlt", "弱い対数端末", "例外条件"], ["条件分岐", "dlt"], [r"a(E)>-1", r"a(E)\ge -1"], r"a(E)\ge -1")
add(1340, "box", ["因子的lc", "対数正準", "下限-1"], ["定義", "lc"], [r"a(E)\ge -1", r"a(E)\ge -1"], r"a(E)\ge -1")
add(1341, "opt", ["SOAPに重み", "二次近似", "クリップ"], ["SOAP段", "減衰"], [r"\Delta\leftarrow\mathrm{SOAP}(g)", r"w\leftarrow w-\eta\Delta-\lambda w"], r"w\leftarrow\mathrm{clip}(w-\eta\Delta-\lambda w)")
add(1342, "opt", ["Shampooに重み", "左右前処理", "クリップ"], ["前処理", "減衰"], [r"G\leftarrow L^{-1/2}GR^{-1/2}", r"w\leftarrow w-\eta G-\lambda w"], r"w\leftarrow\mathrm{clip}(w-\eta G-\lambda w)")
add(1343, "opt", ["QHMに重み", "準双曲", "クリップ"], ["QHM核", "減衰"], [r"v\leftarrow\beta v+(1-\beta)g", r"w\leftarrow w-\eta v-\lambda w"], r"w\leftarrow\mathrm{clip}(w-\eta v-\lambda w)")
add(1344, "tri", ["ヘロン", "面積", "半周"], ["公式", "比"], [r"s=\frac{a+b+c}{2}", r"S=\sqrt{s(s-a)(s-b)(s-c)}"], r"S=\sqrt{s(s-a)(s-b)(s-c)}")
add(1345, "tri", ["ブレッチナイダー", "四辺形面積", "対角"], ["一般化", "余弦"], [r"S^2=(s-a)(s-b)(s-c)(s-d)-abcd\cos^2(\theta/2)", r"S=\sqrt{(s-a)(s-b)(s-c)(s-d)-abcd\cos^2(\theta/2)}"], r"S=\sqrt{(s-a)(s-b)(s-c)(s-d)-abcd\cos^2(\theta/2)}")
add(1346, "tri", ["カラノイ", "垂線和", "外接"], ["関係", "比"], [r"d_a+d_b+d_c=R+r", r"(d_a+d_b+d_c)/R"], r"d_a+d_b+d_c=R+r")
add(1347, "pts", ["ショック数", "粉砕能力", "二値ラベル"], ["定義", "上界"], [r"S_H(n)", r"S_H(n)\le\Pi_H(n)"], r"S_H(n)\le\Pi_H(n)")
add(1348, "pts", ["成長関数", "標本上の多様度", "VCと結ぶ"], ["定義", "多項式界"], [r"\Pi_H(n)", r"\Pi_H(n)\le n^d+1"], r"\Pi_H(n)\le n^d+1")
add(1349, "nums", ["ナラヤナ", "カタラン細分", "峰の数"], ["定義", "和がC"], [r"N(n,k)=\frac{1}{n}\binom{n}{k}\binom{n}{k-1}", r"\sum_k N(n,k)=C_n"], r"N(n,k)", [1, 1, 3, 6, 15])
add(1350, "box", ["サウアー", "成長の折れ", "VC次元"], ["補題", "結論"], [r"\Pi_H(n)\le\sum_{i=0}^d\binom{n}{i}", r"d=VCdim"], r"\Pi_H(n)\le\sum_{i=0}^d\binom{n}{i}")
add(1351, "box", ["パック数", "分離半径", "被覆と双対"], ["定義", "関係"], [r"M(\epsilon)", r"M(\epsilon)\le N(\epsilon/2)"], r"M(\epsilon)\le N(\epsilon/2)")
add(1352, "box", ["計量エントロピー", "被覆の対数", "積分"], ["定義", "ダドリーへ"], [r"H(\epsilon)=\log N(\epsilon)", r"\int\sqrt{H(\epsilon)}\,d\epsilon"], r"H(\epsilon)=\log N(\epsilon)")
add(1353, "opt", ["LionW軟化", "符号+減衰", "平滑"], ["核", "軟閾値"], [r"x\leftarrow x-\eta\mathrm{sign}(m)", r"x\leftarrow\mathrm{soft}(x-\lambda x)"], r"x\leftarrow\mathrm{soft}(x-\eta\mathrm{sign}(m)-\lambda x)")
add(1354, "opt", ["SophiaW軟化", "二階+減衰", "平滑"], ["核", "軟閾値"], [r"\theta\leftarrow\theta-\eta m/\hat H", r"\theta\leftarrow\mathrm{soft}(\theta-\lambda\theta)"], r"\theta\leftarrow\mathrm{soft}(\theta-\eta m/\hat H-\lambda\theta)")
add(1355, "opt", ["MuonW軟化", "直交+減衰", "平滑"], ["核", "軟閾値"], [r"U\leftarrow\mathrm{Muon}(G)", r"W\leftarrow\mathrm{soft}(W-\lambda W)"], r"W\leftarrow\mathrm{soft}(W-\eta U-\lambda W)")
add(1356, "tri", ["キャヴァリエリ", "断面積", "高さ"], ["原理", "比"], [r"A(h)", r"V=\int A(h)\,dh"], r"V=\int A(h)\,dh")
add(1357, "tri", ["相似比", "線型比k", "面積"], ["線の比", "面積の比"], [r"\ell'/\ell=k", r"S'/S=k^2"], r"S'/S=k^2")
add(1358, "tri", ["相似と体積", "面積の次", "体積"], ["面積比", "体積比"], [r"S'/S=k^2", r"V'/V=k^3"], r"V'/V=k^3")
add(1359, "pts", ["経験過程", "一様偏差", "集中"], ["定義", "尾"], [r"\|P_n-P\|", r"P(\|P_n-P\|>t)\le 2e^{-2nt^2}"], r"P(\|P_n-P\|>t)\le 2e^{-2nt^2}")
add(1360, "pts", ["汎化ギャップ", "訓練と真", "複雑度"], ["分解", "上界"], [r"R-R_n", r"R-R_n\le 2R_n+\epsilon"], r"R-R_n\le 2R_n+\epsilon")
add(1361, "nums", ["デラノイ", "3方向路", "細分"], ["定義", "細分"], [r"D(n)", r"D(n,k)"], r"D(n,k)", [1, 3, 13, 63, 321])

# 1362-1397
add(1362, "box", ["有理係数", "丸め操作", "端末判定"], ["係数の集合", "表示"], [r"a_i\in\mathbb{Q}", r"D=\sum a_i V_i"], r"D=\sum a_i V_i", slug="1362_qq_divisor", cls="QQDivisor", season="539_analysis_106", title="QQ因子")
add(1363, "box", ["実係数", "ネフ性", "数値類"], ["係数の集合", "表示"], [r"a_i\in\mathbb{R}", r"D=\sum a_i V_i"], r"D=\sum a_i V_i", slug="1363_rr_divisor", cls="RRDivisor", season="539_analysis_106", title="RR因子")
add(1364, "box", ["境界つき混合", "K+D", "対数ペア"], ["標準+境界", "ペア"], [r"K_X", r"K_X+D"], r"K_X+D", slug="1364_mixed_divisor", cls="MixedDivisor", season="539_analysis_106", title="混合因子")
add(1365, "opt", ["SOAP重み軟化", "二次近似", "平滑"], ["SOAP核", "軟減衰"], [r"\Delta\leftarrow\mathrm{SOAP}(g)", r"w\leftarrow\mathrm{soft}(w-\lambda w)"], r"w\leftarrow\mathrm{soft}(w-\eta\Delta-\lambda w)", slug="1365_soapwsoft", cls="SOAPWSoft", season="540_linear_106", title="SOAPWSoft")
add(1366, "opt", ["前処理軟化", "行列根", "平滑"], ["Shampoo核", "軟減衰"], [r"G\leftarrow L^{-1/2}GR^{-1/2}", r"w\leftarrow\mathrm{soft}(w-\lambda w)"], r"w\leftarrow\mathrm{soft}(w-\eta G-\lambda w)", slug="1366_shampoowsoft", cls="ShampooWSoft", season="540_linear_106", title="ShampooWSoft")
add(1367, "opt", ["QHM重み軟化", "準双曲", "平滑"], ["QHM核", "軟減衰"], [r"v\leftarrow\beta v+(1-\beta)g", r"w\leftarrow\mathrm{soft}(w-\lambda w)"], r"w\leftarrow\mathrm{soft}(w-\eta v-\lambda w)", slug="1367_qhmwsoft", cls="QHMWSoft", season="540_linear_106", title="QHMWSoft")
add(1368, "tri", ["九点円の弦", "中点弦", "比"], ["弦長", "半径比"], [r"c_N", r"c_N/R"], r"c_N/R", slug="1368_nine_chord_ratio", cls="NineChordRatio", season="541_geometry_106", title="九点円弦比")
add(1369, "tri", ["内接と傍接", "半径比", "面積"], ["公式", "比"], [r"r=(s-a)\tan(A/2)", r"r/r_a"], r"r/r_a", slug="1369_in_excircle_ratio", cls="InExcircleRatio", season="541_geometry_106", title="内心傍接比")
add(1370, "tri", ["傍心と外接", "距離比", "角"], ["オイラー型", "比"], [r"OI_a^2=R(R-2r_a)", r"OI_a/R"], r"OI_a/R", slug="1370_ex_circum_ratio", cls="ExCircumRatio", season="541_geometry_106", title="傍心外接比")
add(1371, "pts", ["有界和再訪", "劣ガウス尾", "分散不要"], ["仮定", "指数上界"], [r"|X_i|\le L_i", r"P(|S|\ge t)\le 2e^{-2t^2/\sum L_i^2}"], r"P(|S|\ge t)\le 2e^{-2t^2/\sum L_i^2}", slug="1371_hoeffding_revisit", cls="HoeffdingRevisit", season="542_probability_104", title="ホフディング再訪")
add(1372, "pts", ["分散つき尾", "有界+分散", "指数上界"], ["仮定", "Bernstein"], [r"Var(X_i)\le v_i", r"P(S\ge t)\le e^{-t^2/2(v+Mt/3)}"], r"P(S\ge t)\le e^{-t^2/2(v+Mt/3)}", slug="1372_bernstein_revisit", cls="BernsteinRevisit", season="542_probability_104", title="バーンスタイン再訪")
add(1373, "nums", ["大きなCatalan", "格子路細分", "再帰"], ["定義", "細分"], [r"C_n=\frac{1}{n+1}\binom{2n}{n}", r"C_n^{(2)}"], r"C_n^{(2)}", [1, 2, 5, 14, 42], slug="1373_large_catalan_ref", cls="LargeCatalanRefine", season="543_combinatorics_103", title="大きなカタラン細分")
add(1374, "box", ["対数ペア", "境界条件", "端末性"], ["ペア", "食い違い"], [r"(X,D)", r"a(E;X,D)"], r"(X,D)", slug="1374_log_pair", cls="LogPair", season="544_analysis_107", title="対数ペア")
add(1375, "box", ["相対対数", "ファイバー上", "K+D"], ["相対", "ペア"], [r"K_{X/S}+D", r"(X/S,D)"], r"(X/S,D)", slug="1375_rel_log_pair", cls="RelLogPair", season="544_analysis_107", title="相対対数ペア")
add(1376, "box", ["準対数端末", "中間クラス", "食い違い"], ["下限", "結論"], [r"a(E)>-1", r"a(E)>-1+\delta"], r"a(E)>-1", slug="1376_quasi_log", cls="QuasiLogTerminal", season="544_analysis_107", title="準対数端末")
add(1377, "opt", ["累積勾配軟化", "学習率平滑", "安定化"], ["AdaGrad", "軟閾値"], [r"G\leftarrow G+g^2", r"G\leftarrow\mathrm{soft}(G)"], r"\eta/\sqrt{G+\epsilon}", slug="1377_adagradsoft", cls="AdaGradSoft", season="545_linear_107", title="AdaGradSoft")
add(1378, "opt", ["Nesterov軟化", "加速平滑", "更新"], ["NAdam核", "軟閾値"], [r"m\leftarrow\beta m+g", r"m\leftarrow\mathrm{soft}(m)"], r"x\leftarrow x-\eta\mathrm{soft}(m)", slug="1378_nadamsoft", cls="NAdamSoft", season="545_linear_107", title="NAdamSoft")
add(1379, "opt", ["整流Adam軟化", "分散補正", "平滑"], ["RAdam", "軟学習率"], [r"\eta_r", r"\eta\leftarrow\mathrm{soft}(\eta)"], r"x\leftarrow x-\mathrm{soft}(\eta)m/\sqrt{v}", slug="1379_radamsoft", cls="RAdamSoft", season="545_linear_107", title="RAdamSoft")
add(1380, "tri", ["垂心と中線", "交点比", "オイラー"], ["配置", "比"], [r"H,M_a", r"HM/m_a"], r"HM/m_a", slug="1380_h_median_ratio", cls="HMedianRatio", season="546_geometry_107", title="垂心中線比")
add(1381, "tri", ["重心は2:1", "中線分割", "固定比"], ["中線", "分割比"], [r"G\in AM_a", r"AG:GM=2:1"], r"AG:GM=2:1", slug="1381_g_median_ratio", cls="GMedianRatio", season="546_geometry_107", title="重心中線比")
add(1382, "tri", ["内心と中線", "距離比", "辺長"], ["配置", "比"], [r"I,M_a", r"IM/m_a"], r"IM/m_a", slug="1382_i_median_ratio", cls="IMedianRatio", season="546_geometry_107", title="内心中線比")
add(1383, "pts", ["分散既知再訪", "h関数", "指数上界"], ["Bennett核", "h"], [r"h(u)=(1+u)\log(1+u)-u", r"P(S\ge t)\le e^{-vh(t/v)}"], r"P(S\ge t)\le e^{-vh(t/v)}", slug="1383_bennett_revisit", cls="BennettRevisit", season="547_probability_105", title="ベネット再訪")
add(1384, "pts", ["差分有界再訪", "マルチンゲール", "集中"], ["増分", "Azuma"], [r"|M_k-M_{k-1}|\le c_k", r"P(|M|\ge t)\le 2e^{-t^2/2\sum c^2}"], r"P(|M|\ge t)\le 2e^{-t^2/2\sum c^2}", slug="1384_azuma_revisit", cls="AzumaRevisit", season="547_probability_105", title="アズーマ再訪")
add(1385, "nums", ["色付きモツキン", "水準細分", "計数"], ["定義", "細分"], [r"M_n", r"M_{n,k}"], r"M_{n,k}", [1, 1, 2, 4, 9], slug="1385_motzkin_path_ref2", cls="MotzkinPathRef2", season="548_combinatorics_104", title="モツキン細分路")
add(1386, "box", ["SNC対数ペア", "横断交差", "局所座標"], ["SNC", "ペア"], [r"D=\sum D_i", r"(X,\sum D_i)"], r"(X,\sum D_i)", slug="1386_snc_pair", cls="SNCPair", season="549_analysis_108", title="スネイドペア")
add(1387, "box", ["純対数ペア", "plt条件", "境界"], ["条件", "ペア"], [r"a(E)\ge -1", r"(X,D)"], r"(X,D)", slug="1387_plt_pair", cls="PLTPair", season="549_analysis_108", title="純対数ペア")
add(1388, "box", ["端末ペア", "食い違い正", "閾値"], ["条件", "ペア"], [r"a(E)>0", r"(X,D)"], r"(X,D)", slug="1388_terminal_pair", cls="TerminalPair", season="549_analysis_108", title="端末ペア")
add(1389, "opt", ["SOAP重み硬閾", "二次近似", "剪定"], ["SOAP", "硬減衰"], [r"\Delta\leftarrow\mathrm{SOAP}(g)", r"w\leftarrow\mathrm{hard}(w-\lambda w)"], r"w\leftarrow\mathrm{hard}(w-\eta\Delta-\lambda w)", slug="1389_soapwhard", cls="SOAPWHard", season="550_linear_108", title="SOAPWHard")
add(1390, "opt", ["前処理硬閾", "行列根", "剪定"], ["Shampoo", "硬減衰"], [r"G\leftarrow L^{-1/2}GR^{-1/2}", r"w\leftarrow\mathrm{hard}(w-\lambda w)"], r"w\leftarrow\mathrm{hard}(w-\eta G-\lambda w)", slug="1390_shampoowhard", cls="ShampooWHard", season="550_linear_108", title="ShampooWHard")
add(1391, "opt", ["QHM重み硬閾", "準双曲", "剪定"], ["QHM", "硬減衰"], [r"v\leftarrow\beta v+(1-\beta)g", r"w\leftarrow\mathrm{hard}(w-\lambda w)"], r"w\leftarrow\mathrm{hard}(w-\eta v-\lambda w)", slug="1391_qhmwhard", cls="QHMWHard", season="550_linear_108", title="QHMWHard")
add(1392, "tri", ["外心と中線", "垂直二等分", "比"], ["配置", "比"], [r"O,M_a", r"OM/m_a"], r"OM/m_a", slug="1392_o_median_ratio", cls="OMedianRatio", season="551_geometry_108", title="外心中線比")
add(1393, "tri", ["九点円と中線", "中点", "比"], ["配置", "比"], [r"N,M_a", r"NM/m_a"], r"NM/m_a", slug="1393_n_median_ratio", cls="NMedianRatio", season="551_geometry_108", title="九点中線比")
add(1394, "tri", ["傍心と中線", "角条件", "比"], ["配置", "比"], [r"I_a,M_a", r"I_aM/m_a"], r"I_aM/m_a", slug="1394_ex_median_ratio", cls="ExMedianRatio", season="551_geometry_108", title="傍心中線比")
add(1395, "pts", ["有界差再訪", "関数安定性", "集中"], ["差条件", "尾"], [r"|f(x)-f(x_i)|\le c_i", r"P(|f-\mathbb{E}f|\ge t)\le 2e^{-2t^2/\sum c_i^2}"], r"P(|f-\mathbb{E}f|\ge t)\le 2e^{-2t^2/\sum c_i^2}", slug="1395_mcdiarmid_revisit", cls="McDiarmidRevisit", season="552_probability_106", title="マクディアミド再訪")
add(1396, "pts", ["和上界再訪", "ユニオン", "単純評価"], ["事象", "和"], [r"P(\cup A_i)", r"P(\cup A_i)\le\sum P(A_i)"], r"P(\cup A_i)\le\sum P(A_i)", slug="1396_boole_revisit", cls="BooleRevisit", season="552_probability_106", title="ブール再訪")
add(1397, "nums", ["シュレーダー細分", "括弧列", "再帰"], ["定義", "細分"], [r"S_n", r"S_{n,k}"], r"S_{n,k}", [1, 2, 6, 22, 90], slug="1397_schroeder_ref", cls="SchroederRefine", season="553_combinatorics_105", title="シュレーダー細分")


def catalog_rows(a: int, b: int):
    rows = []
    for name, val in vars(cat).items():
        if name.startswith("VIDEOS_") and isinstance(val, tuple):
            for v in val:
                if a <= v.number <= b:
                    rows.append(v)
    return sorted(rows, key=lambda v: v.number)


def main() -> None:
    rows_1326 = catalog_rows(1326, 1361)
    assert len(rows_1326) == 36, len(rows_1326)
    created = []
    for v in rows_1326:
        meta = CONTENT[v.number]
        parts = v.path.split("/")
        season, slug = parts[2], parts[3]
        code = mk(
            meta["kind"],
            v.scene,
            v.number,
            v.title,
            meta["notes"],
            meta["dnotes"],
            meta["dtex"],
            meta["final"],
            meta.get("vals"),
        )
        folder = ROOT / "project/math" / season / slug
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "scene.py").write_text(code, encoding="utf-8")
        (folder / "storyboard.md").write_text(story(v.number, v.title), encoding="utf-8")
        ast.parse(code)
        created.append((v.number, v.title, v.path, v.scene))

    for num in range(1362, 1398):
        meta = CONTENT[num]
        title = meta["title"]
        if title in titles and not any(v.number == num for v in catalog_rows(1362, 1397)):
            # allow overwrite of WIP titles not yet in catalog tip
            pass
        season, slug, cls = meta["season"], meta["slug"], meta["cls"]
        path = f"project/math/{season}/{slug}/scene.py"
        code = mk(
            meta["kind"],
            cls,
            num,
            title,
            meta["notes"],
            meta["dnotes"],
            meta["dtex"],
            meta["final"],
            meta.get("vals"),
        )
        folder = ROOT / "project/math" / season / slug
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "scene.py").write_text(code, encoding="utf-8")
        (folder / "storyboard.md").write_text(story(num, title), encoding="utf-8")
        ast.parse(code)
        created.append((num, title, path, cls))

    print("wrote", len(created), "scenes", created[0][0], "-", created[-1][0])

    catalog_path = ROOT / "project/math/catalog.py"
    text = catalog_path.read_text(encoding="utf-8")
    if "VIDEOS_1362_1373" not in text:
        def block(name, items):
            lines = [f"\n\n{name}: tuple[Video, ...] = ("]
            for num, title, path, cls in items:
                lines.append(f'    Video({num}, "{title}", "{path}", "{cls}"),')
            lines.append(")")
            return "\n".join(lines)

        items = created[36:]
        text = (
            text.rstrip()
            + block("VIDEOS_1362_1373", items[:12])
            + block("VIDEOS_1374_1385", items[12:24])
            + block("VIDEOS_1386_1397", items[24:])
            + "\n"
        )
        catalog_path.write_text(text, encoding="utf-8")

    tp = ROOT / "tests/test_catalog.py"
    t = tp.read_text(encoding="utf-8")
    if "VIDEOS_1362_1373" not in t:
        t = t.replace(
            "VIDEOS_1350_1361 = _catalog.VIDEOS_1350_1361\n",
            "VIDEOS_1350_1361 = _catalog.VIDEOS_1350_1361\n"
            "VIDEOS_1362_1373 = _catalog.VIDEOS_1362_1373\n"
            "VIDEOS_1374_1385 = _catalog.VIDEOS_1374_1385\n"
            "VIDEOS_1386_1397 = _catalog.VIDEOS_1386_1397\n",
        )
        insert = """
    def test_numbers_are_1362_to_1373(self):
        nums = [v.number for v in VIDEOS_1362_1373]
        self.assertEqual(nums, list(range(1362, 1374)))


    def test_numbers_are_1374_to_1385(self):
        nums = [v.number for v in VIDEOS_1374_1385]
        self.assertEqual(nums, list(range(1374, 1386)))


    def test_numbers_are_1386_to_1397(self):
        nums = [v.number for v in VIDEOS_1386_1397]
        self.assertEqual(nums, list(range(1386, 1398)))

"""
        t = t.replace(
            "    def test_each_scene_file_defines_the_class(self):",
            insert + "    def test_each_scene_file_defines_the_class(self):",
        )
        t = t.replace(
            "            *VIDEOS_1350_1361,\n        ):",
            "            *VIDEOS_1350_1361,\n"
            "            *VIDEOS_1362_1373,\n"
            "            *VIDEOS_1374_1385,\n"
            "            *VIDEOS_1386_1397,\n"
            "        ):",
        )
        tp.write_text(t, encoding="utf-8")

    plan = ROOT / "project/math/PLAN.md"
    p = plan.read_text(encoding="utf-8")
    if "導出2段" not in p:
        note = (
            "\n\n> **尺メモ（#1326–）**: 見出し→図→要点→**導出2段**→結論式。"
            "アイドル待ちではなく途中式の `Write`/`Transform` で 40秒前後を狙う。\n"
        )
        p = p.replace("## 1 本の作業フロー", note + "\n## 1 本の作業フロー")
    if "#1362" not in p:
        extra = "\n\n## 導出つき続き（#1362–#1373）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[36:48]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#1374–#1385）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[48:60]:
            extra += f"| {num} | {title} | 実装 |\n"
        extra += "\n\n## 導出つき続き（#1386–#1397）\n\n| # | 内容 | 状態 |\n|---|---|---|\n"
        for num, title, _, _ in created[60:]:
            extra += f"| {num} | {title} | 実装 |\n"
        p = p.replace("## 1 本の作業フロー", extra + "\n## 1 本の作業フロー")
    if "導出つきへ更新" not in p:
        p = p.replace(
            "## 1 本の作業フロー",
            "\n\n## #1326–#1361 導出つきへ更新\n\n"
            "既存シーズンを `derive()` 付きに再実装（約45秒）。\n\n## 1 本の作業フロー",
        )
    plan.write_text(p, encoding="utf-8")
    print("ok")


if __name__ == "__main__":
    main()
