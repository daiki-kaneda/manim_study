from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import LessonScene


class RootsOfUnity(LessonScene):
    """#19 1 の n 乗根は正多角形か（約9分）"""

    def construct(self):
        self.header = self._open_header()
        self.part_question()
        self.part_trial_reals()
        self.part_trial_four()
        self.part_step1_polar()
        self.part_step2_divide()
        self.part_step3_n4()
        self.part_step4_polygon()
        self.part_example()
        self.part_generalize()
        self.part_summary()

    def _open_header(self):
        title = self._line(
            "1 の",
            MathTex(r"n", font_size=40, color=YELLOW),
            "乗根は正多角形か",
            font_size=34,
        )
        self._fit(title, 13.2)
        title.set_x(0)
        self.play(FadeIn(title), run_time=0.8)
        self.pause_new_screen()
        self.linger(1.5)
        self.play(title.animate.scale(0.52).to_edge(UP, buff=0.16), run_time=0.5)
        title.set_x(0)
        return title

    def part_question(self):
        fig = self._roots_figure(n=0, r=1.40, labels=False, polygon=False)
        cap = self._line(
            MathTex(r"n", font_size=24, color=YELLOW),
            "乗して 1 になる数を、平面の点として並べてみます。",
            font_size=16,
        )
        self._fit(cap, 13.0)
        pair = VGroup(fig, cap).arrange(DOWN, buff=0.22)
        pair.next_to(self.header, DOWN, buff=0.22)
        pair.set_x(0)
        self._nudge(pair)
        self.play(FadeIn(fig), FadeIn(cap), run_time=0.8)
        self.pause_new_screen()
        self.linger("n 乗して 1 になる数を、平面の点として並べてみます。")

        q1 = self._line(
            "方程式",
            MathTex(r"z^{n}=1", font_size=26, color=YELLOW),
            "の解は、何個あるでしょうか。",
            font_size=18,
        )
        self.stack_below(q1, pair, buff=0.16)
        q1.set_x(0)
        self._fit(q1, 13.0)
        q1.set_x(0)
        self.play(FadeIn(q1), run_time=0.7)
        self.linger("方程式 z^n=1 の解は、何個あるでしょうか。")

        q2 = self._line(
            "それらは、正",
            MathTex(r"n", font_size=24, color=YELLOW),
            "角形の頂点になっているでしょうか。",
            font_size=18,
        )
        self.stack_below(q2, q1, buff=0.12)
        q2.set_x(0)
        self.play(FadeIn(q2), run_time=0.7)
        self._read(q2, extra=0.35)

    def part_trial_reals(self):
        chip = self.begin_step("試行  実数だけ", self.header)

        lead = self.ja_text(
            "まず、実数の中だけで、2 乗、3 乗、4 乗して 1 になる数を探します。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)
        self.play(FadeOut(lead), run_time=0.40)

        rows = [
            self._line(
                MathTex(r"n=2", font_size=24, color=YELLOW),
                ":",
                MathTex(r"z^{2}=1", font_size=24),
                "。",
                MathTex(r"z=1", font_size=24, color=GREEN),
                "と",
                MathTex(r"z=-1", font_size=24, color=GREEN),
                "。実数は 2 個です。",
                font_size=16,
            ),
            self._line(
                MathTex(r"n=3", font_size=24, color=ORANGE),
                ":",
                MathTex(r"z^{3}=1", font_size=24),
                "。正なら",
                MathTex(r"z=1", font_size=24, color=GREEN),
                "。負の 3 乗は負なので、実数は 1 個です。",
                font_size=14,
            ),
            self._line(
                MathTex(r"n=4", font_size=24, color=TEAL),
                ":",
                MathTex(r"z^{4}=1", font_size=24),
                "。",
                MathTex(r"z=1", font_size=24, color=GREEN),
                "と",
                MathTex(r"z=-1", font_size=24, color=GREEN),
                "。実数は 2 個です。",
                font_size=16,
            ),
        ]
        block = self._formula_rows(rows, chip, buff=0.16, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(block), run_time=0.40)

        table = self.aligned_table(
            [
                [
                    MathTex(r"n", font_size=22, color=GREY_B),
                    self.ja_text("実数の解の個数", font_size=16, color=GREY_B),
                ],
                [MathTex(r"2", font_size=26), MathTex(r"2", font_size=26, color=YELLOW)],
                [MathTex(r"3", font_size=26), MathTex(r"1", font_size=26, color=ORANGE)],
                [MathTex(r"4", font_size=26), MathTex(r"2", font_size=26, color=TEAL)],
            ],
            h_buff=0.40,
            v_buff=0.10,
        )
        table.scale(0.90)
        self.below_chip(table, chip, buff=0.16)
        table.set_x(0)
        self.play(FadeIn(table), run_time=0.7)
        self.pause_new_screen()

        notes = [
            self._line(
                "実数だけだと、",
                MathTex(r"n=3", font_size=22, color=ORANGE),
                "も",
                MathTex(r"n=4", font_size=22, color=TEAL),
                "も、",
                MathTex(r"n", font_size=22, color=YELLOW),
                "個には足りません。",
                font_size=16,
            ),
            self.ja_text(
                "実数の数直線の上では、確かに足りないように感じます。足りない分は、無い、で止めると、平面に並べる場所がなくなります。",
                font_size=16,
            ),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, table, buff=0.14)
            else:
                self.stack_below(mob, shown, buff=0.10)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            shown.add(mob)
            self._read(mob)

    def part_trial_four(self):
        chip = self.begin_step("試行  4 乗", self.header)

        lead = self._line(
            MathTex(r"z^{4}=1", font_size=24, color=YELLOW),
            "を、実数の二次方程式に分けて、足りない 2 個の居場所を探します。",
            font_size=16,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger("z^4=1 を、実数の二次方程式に分けて、足りない 2 個の居場所を探します。")
        self.play(FadeOut(lead), run_time=0.40)

        rows = [
            self._line(MathTex(r"z^{4}-1=0", font_size=26, color=YELLOW), font_size=16),
            self._line(
                MathTex(r"z^{4}-1=(z^{2}-1)(z^{2}+1)", font_size=26, color=GREEN),
                font_size=16,
            ),
            self._line(
                MathTex(r"z^{2}-1=(z-1)(z+1)", font_size=24),
                "。ここから",
                MathTex(r"z=1", font_size=24, color=YELLOW),
                "、",
                MathTex(r"z=-1", font_size=24, color=ORANGE),
                font_size=16,
            ),
            self._line(
                MathTex(r"z^{2}+1=0", font_size=24),
                "なら",
                MathTex(r"z^{2}=-1", font_size=24, color=TEAL),
                "。実数の平方は 0 以上なので、実数には解がありません。",
                font_size=14,
            ),
            self._line(
                MathTex(r"i^{2}=-1", font_size=24, color=GREEN),
                "とすると、",
                MathTex(r"z=i", font_size=24, color=GREEN),
                "と",
                MathTex(r"z=-i", font_size=24, color=TEAL),
                "が入ります。",
                font_size=16,
            ),
        ]
        block = self._formula_rows(rows, chip, buff=0.12, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(block), run_time=0.40)

        fig = self._roots_figure(
            n=4,
            r=1.25,
            labels=True,
            polygon=True,
            names=[r"1", r"i", r"-1", r"-i"],
        )
        self.below_chip(fig, chip, buff=0.12)
        fig.set_x(0)
        self.play(FadeIn(fig), run_time=0.8)
        self.pause_new_screen()

        notes = [
            self._line(
                "実数に無いなら解はそこで終わり、ではありません。",
                MathTex(r"z^{2}+1=0", font_size=22, color=TEAL),
                "は、平面では",
                MathTex(r"i", font_size=22, color=GREEN),
                "と",
                MathTex(r"-i", font_size=22, color=TEAL),
                "です。",
                font_size=14,
            ),
            self._line(
                "4 個の点が、原点のまわりに等間隔で並びました。正方形の頂点に見えます。一般の",
                MathTex(r"n", font_size=22, color=YELLOW),
                "でも同じか、まだ分かりません。",
                font_size=14,
            ),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, fig, buff=0.12)
            else:
                self.stack_below(mob, shown, buff=0.08)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            shown.add(mob)
            self._read(mob)

    def part_step1_polar(self):
        chip = self.begin_step("STEP 1  極形式", self.header)

        lead = self.ja_text(
            "複素数を、長さと角で書く決まりを置きます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        rows = [
            self._line(
                "原点からの長さを",
                MathTex(r"r", font_size=24, color=TEAL),
                "、実軸から左へ測った角を",
                MathTex(r"\theta", font_size=24, color=YELLOW),
                "とおく。",
                font_size=16,
            ),
            self._line(
                MathTex(r"z=r(\cos\theta+i\sin\theta)", font_size=26, color=YELLOW),
                "です。",
                font_size=18,
            ),
            self._line(
                MathTex(r"i^{2}=-1", font_size=24, color=GREEN),
                "です。",
                MathTex(r"i", font_size=24, color=GREEN),
                "自身は長さ 1、角",
                MathTex(r"\dfrac{\pi}{2}", font_size=24, color=GREEN),
                "です。",
                font_size=16,
            ),
            self.ja_text(
                "掛けると、長さは積、角は和になります。今回はこれを認めて使います。",
                font_size=16,
            ),
        ]
        shown = self._formula_rows(rows, lead, buff=0.10, hold=self.PAUSE_COMPLEX)

        notes = [
            self._line(
                MathTex(r"z^{n}=1", font_size=24, color=YELLOW),
                "なら、長さも角も、1 と合う必要があります。",
                font_size=16,
            ),
            self.ja_text(
                "1 は、長さ 1、角 0 の点です。角は一周するごとに同じ点へ戻ります。",
                font_size=16,
            ),
        ]
        extra = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, shown, buff=0.12)
            else:
                self.stack_below(mob, extra, buff=0.10)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            extra.add(mob)
            self._read(mob)

    def part_step2_divide(self):
        chip = self.begin_step("STEP 2  n 等分", self.header)

        lead = self._line(
            MathTex(r"n", font_size=24, color=YELLOW),
            "乗すると長さが 1、角が 0 に戻る、という条件を式にします。",
            font_size=16,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger("n 乗すると長さが 1、角が 0 に戻る、という条件を式にします。")

        restate = self._line(
            MathTex(r"z=r(\cos\theta+i\sin\theta)", font_size=24, color=YELLOW),
            "です。角を等分する方法を次の式で見ます。",
            font_size=16,
        )
        self.stack_below(restate, lead, buff=0.10)
        restate.set_x(0)
        self._fit(restate, 13.0)
        restate.set_x(0)
        self.play(FadeIn(restate), run_time=0.55)
        self.linger("z=r(cos θ + i sin θ) です。角を等分する方法を次の式で見ます。")
        self.play(FadeOut(lead), run_time=0.40)

        rows = [
            self._line(
                MathTex(
                    r"z^{n}=\bigl(r(\cos\theta+i\sin\theta)\bigr)^{n}=r^{n}\bigl(\cos(n\theta)+i\sin(n\theta)\bigr)",
                    font_size=20,
                    color=YELLOW,
                ),
                font_size=14,
            ),
            self._line(
                "これが 1 に等しい。1 は",
                MathTex(r"1\cdot(\cos 0+i\sin 0)", font_size=22, color=GREEN),
                font_size=16,
            ),
            self._line(
                "だから",
                MathTex(r"r^{n}=1", font_size=26, color=TEAL),
                "。長さは正なので",
                MathTex(r"r=1", font_size=26, color=TEAL),
                font_size=16,
            ),
            self._line(
                "角は",
                MathTex(r"n\theta=2\pi k", font_size=26, color=ORANGE),
                "。整数",
                MathTex(r"k", font_size=24, color=ORANGE),
                "とおく。",
                font_size=16,
            ),
            self._line(
                MathTex(r"\theta=\dfrac{2\pi k}{n}", font_size=30, color=GOLD),
                font_size=18,
            ),
        ]
        shown = self._formula_rows(rows, restate, buff=0.08, hold=self.PAUSE_COMPLEX)

        notes = [
            self._line(
                MathTex(r"k=0,1,2,\ldots,n-1", font_size=22, color=ORANGE),
                "で、同じ点が繰り返す前の",
                MathTex(r"n", font_size=22, color=YELLOW),
                "個が出ます。",
                MathTex(r"k=n", font_size=22),
                "は",
                MathTex(r"k=0", font_size=22),
                "と同じ点です。",
                font_size=14,
            ),
            self._line(
                "解は単位円の上に、角を",
                MathTex(r"n", font_size=22, color=YELLOW),
                "等分した位置へ",
                MathTex(r"n", font_size=22, color=YELLOW),
                "個あります。実数に足りなかった分は、この円の上にあります。",
                font_size=14,
            ),
        ]
        extra = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, shown, buff=0.10)
            else:
                self.stack_below(mob, extra, buff=0.08)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            extra.add(mob)
            self._read(mob)
            if i == 1:
                self.pause_conclusion()

    def part_step3_n4(self):
        chip = self.begin_step("STEP 3  n=4", self.header)

        lead = self._line(
            MathTex(r"n=4", font_size=24, color=YELLOW),
            "に代入して、試行の 4 点へ戻します。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger("n=4 に代入して、試行の 4 点へ戻します。")
        self.play(FadeOut(lead), run_time=0.40)

        rows = [
            self._line(
                MathTex(r"k=0", font_size=22, color=YELLOW),
                ":",
                MathTex(r"\theta=0", font_size=22),
                "。点",
                MathTex(r"\cos 0+i\sin 0=1", font_size=22, color=YELLOW),
                font_size=16,
            ),
            self._line(
                MathTex(r"k=1", font_size=22, color=GREEN),
                ":",
                MathTex(r"\theta=\dfrac{\pi}{2}", font_size=22),
                "。点",
                MathTex(r"\cos\dfrac{\pi}{2}+i\sin\dfrac{\pi}{2}=i", font_size=22, color=GREEN),
                font_size=14,
            ),
            self._line(
                MathTex(r"k=2", font_size=22, color=ORANGE),
                ":",
                MathTex(r"\theta=\pi", font_size=22),
                "。点",
                MathTex(r"\cos\pi+i\sin\pi=-1", font_size=22, color=ORANGE),
                font_size=16,
            ),
            self._line(
                MathTex(r"k=3", font_size=22, color=TEAL),
                ":",
                MathTex(r"\theta=\dfrac{3\pi}{2}", font_size=22),
                "。点",
                MathTex(
                    r"\cos\dfrac{3\pi}{2}+i\sin\dfrac{3\pi}{2}=-i",
                    font_size=20,
                    color=TEAL,
                ),
                font_size=14,
            ),
        ]
        block = self._formula_rows(rows, chip, buff=0.14, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(block), run_time=0.40)

        fig = self._roots_figure(
            n=4,
            r=1.20,
            labels=True,
            polygon=True,
            names=[r"1", r"i", r"-1", r"-i"],
        )
        self.below_chip(fig, chip, buff=0.12)
        fig.set_x(0)
        self.play(FadeIn(fig), run_time=0.8)
        self.pause_new_screen()

        notes = [
            self._line(
                "試行で足りなかった",
                MathTex(r"i", font_size=22, color=GREEN),
                "と",
                MathTex(r"-i", font_size=22, color=TEAL),
                "は、角を 4 等分した点でした。",
                font_size=16,
            ),
            self._line(
                "隣どうしの角は",
                MathTex(r"\dfrac{\pi}{2}", font_size=24, color=YELLOW),
                "。4 辺の長さはどれも同じです。",
                font_size=16,
            ),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, fig, buff=0.12)
            else:
                self.stack_below(mob, shown, buff=0.08)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            shown.add(mob)
            self._read(mob)

    def part_step4_polygon(self):
        chip = self.begin_step("STEP 4  正多角形", self.header)

        lead = self.ja_text(
            "単位円上で、隣り合う点の間隔が一定なら、頂点を結ぶ図形は正多角形です。",
            font_size=16,
        )
        self.below_chip(lead, chip, buff=0.14)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)
        self.play(FadeOut(lead), run_time=0.40)

        fig = self._roots_figure(n=6, r=1.20, labels=True, polygon=True)
        self.below_chip(fig, chip, buff=0.10)
        fig.shift(LEFT * 3.15)
        self._nudge(fig)
        self.play(FadeIn(fig), run_time=0.8)
        self.pause_new_screen()

        rows = [
            self.ja_text("各点は原点から長さ 1 です。", font_size=16),
            self._line(
                "隣の点との中心角はどれも",
                MathTex(r"\dfrac{2\pi}{n}", font_size=24, color=YELLOW),
                "です。",
                font_size=16,
            ),
            self.ja_text("弦の長さはどれも同じ。内角も同じです。", font_size=16),
            self._line(
                "だから正",
                MathTex(r"n", font_size=24, color=YELLOW),
                "角形です。",
                font_size=16,
            ),
        ]
        block = VGroup(*rows).arrange(DOWN, buff=0.10, aligned_edge=LEFT)
        block.next_to(fig, RIGHT, buff=0.35)
        block.align_to(fig, UP)
        self._nudge(block)
        for row in block:
            self.play(FadeIn(row), run_time=self.PAUSE_REWRITE)
            super().wait(self.PAUSE_COMPLEX)

        notes = [
            self._line(
                "解の個数は",
                MathTex(r"n", font_size=22, color=YELLOW),
                "個。並び方は正",
                MathTex(r"n", font_size=22, color=YELLOW),
                "角形の頂点です。",
                font_size=16,
            ),
            self._line(
                "実数の解は、この多角形が実軸と交わる点だけです。残りは平面へ出ます。",
                MathTex(r"n", font_size=20, color=YELLOW),
                "次方程式",
                MathTex(r"z^{n}-1=0", font_size=22, color=YELLOW),
                "の解は、重複なく",
                MathTex(r"n", font_size=20, color=YELLOW),
                "個あります。実数に見える個数で終わりではありません。",
                font_size=14,
            ),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, fig, buff=0.14)
            else:
                self.stack_below(mob, shown, buff=0.08)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            shown.add(mob)
            self._read(mob)
            if i == 1:
                self.pause_conclusion()

    def part_example(self):
        chip = self.begin_step("実例", self.header)

        lead = self._line(
            MathTex(r"n=3", font_size=24, color=YELLOW),
            "を、因数分解から点の座標まで通します。",
            font_size=16,
        )
        self.below_chip(lead, chip, buff=0.14)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger("n=3 を、因数分解から点の座標まで通します。")

        rows = [
            self._line(
                MathTex(r"z^{3}-1=(z-1)(z^{2}+z+1)", font_size=26, color=YELLOW),
                font_size=16,
            ),
            self._line(
                MathTex(r"z-1=0", font_size=22),
                "なら",
                MathTex(r"z=1", font_size=24, color=YELLOW),
                "。角",
                MathTex(r"0", font_size=22),
                font_size=16,
            ),
            self._line(
                MathTex(r"z^{2}+z+1=0", font_size=22, color=ORANGE),
                "。解の公式:",
                MathTex(
                    r"z=\dfrac{-1\pm\sqrt{1-4}}{2}=\dfrac{-1\pm\sqrt{-3}}{2}",
                    font_size=20,
                    color=ORANGE,
                ),
                font_size=14,
            ),
            self._line(
                MathTex(r"\sqrt{-3}=i\sqrt{3}", font_size=22, color=GREEN),
                "なので",
                MathTex(r"z=\dfrac{-1\pm i\sqrt{3}}{2}", font_size=24, color=GREEN),
                font_size=16,
            ),
        ]
        block = self._formula_rows(rows, lead, buff=0.08, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(VGroup(lead, block)), run_time=0.40)

        more = [
            self._line(
                MathTex(r"k=0", font_size=20, color=YELLOW),
                ":",
                MathTex(r"\theta=0", font_size=20),
                "。点",
                MathTex(r"1", font_size=22, color=YELLOW),
                font_size=16,
            ),
            self._line(
                MathTex(r"k=1", font_size=20, color=GREEN),
                ":",
                MathTex(r"\theta=\dfrac{2\pi}{3}", font_size=20),
                "。",
                MathTex(
                    r"\cos\dfrac{2\pi}{3}=-\dfrac{1}{2},\ \sin\dfrac{2\pi}{3}=\dfrac{\sqrt{3}}{2}",
                    font_size=18,
                    color=GREEN,
                ),
                font_size=12,
            ),
            self._line(
                "点",
                MathTex(r"-\dfrac{1}{2}+i\dfrac{\sqrt{3}}{2}", font_size=22, color=GREEN),
                font_size=16,
            ),
            self._line(
                MathTex(r"k=2", font_size=20, color=ORANGE),
                ":",
                MathTex(r"\theta=\dfrac{4\pi}{3}", font_size=20),
                "。点",
                MathTex(r"-\dfrac{1}{2}-i\dfrac{\sqrt{3}}{2}", font_size=22, color=ORANGE),
                font_size=14,
            ),
            self._line(
                "解の公式の",
                MathTex(r"\dfrac{-1\pm i\sqrt{3}}{2}", font_size=20, color=GREEN),
                "と一致します。",
                font_size=16,
            ),
        ]
        extra = self._formula_rows(more, chip, buff=0.12, hold=self.PAUSE_SHORT_FORMULA)
        self.play(FadeOut(extra), run_time=0.40)

        fig = self._roots_figure(
            n=3,
            r=1.05,
            labels=True,
            polygon=True,
            names=[r"1", r"\omega", r"\omega^{2}"],
        )
        table = self.aligned_table(
            [
                [
                    MathTex(r"k", font_size=18, color=GREY_B),
                    MathTex(r"\theta", font_size=18, color=GREY_B),
                    self.ja_text("点", font_size=14, color=GREY_B),
                ],
                [
                    MathTex(r"0", font_size=20, color=YELLOW),
                    MathTex(r"0", font_size=20),
                    MathTex(r"1", font_size=20, color=YELLOW),
                ],
                [
                    MathTex(r"1", font_size=20, color=GREEN),
                    MathTex(r"\dfrac{2\pi}{3}", font_size=20, color=GREEN),
                    MathTex(r"-\dfrac{1}{2}+i\dfrac{\sqrt{3}}{2}", font_size=18, color=GREEN),
                ],
                [
                    MathTex(r"2", font_size=20, color=ORANGE),
                    MathTex(r"\dfrac{4\pi}{3}", font_size=20, color=ORANGE),
                    MathTex(r"-\dfrac{1}{2}-i\dfrac{\sqrt{3}}{2}", font_size=18, color=ORANGE),
                ],
            ],
            h_buff=0.22,
            v_buff=0.08,
        )
        table.scale(0.78)
        pair = VGroup(fig, table).arrange(RIGHT, buff=0.40)
        self.below_chip(pair, chip, buff=0.10)
        pair.set_x(0)
        self._nudge(pair)
        self.play(FadeIn(fig), FadeIn(table), run_time=0.8)
        self.pause_new_screen()

        notes = [
            self._line(
                "実数は",
                MathTex(r"z=1", font_size=22, color=YELLOW),
                "の 1 個だけ。残り 2 個は、正三角形の上の頂点と下の頂点です。",
                font_size=14,
            ),
            self.ja_text("3 乗して 1 になる数は、この 3 点です。", font_size=16),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, pair, buff=0.12)
            else:
                self.stack_below(mob, shown, buff=0.08)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            shown.add(mob)
            self._read(mob)

    def part_generalize(self):
        chip = self.begin_step("一般化", self.header)

        lead = self._line(
            "今やったことは、ド・モアブルの定理から、1 の",
            MathTex(r"n", font_size=24, color=YELLOW),
            "乗根が正",
            MathTex(r"n", font_size=24, color=YELLOW),
            "角形になる、という考え方でした。",
            font_size=16,
        )
        self.below_chip(lead, chip, buff=0.14)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger("今やったことは、ド・モアブルの定理から、1 の n 乗根が正 n 角形になる、という考え方でした。")
        self.pause_conclusion()

        rows = [
            self._line(
                MathTex(r"z=r(\cos\theta+i\sin\theta)", font_size=24, color=YELLOW),
                "とおく。",
                font_size=16,
            ),
            self._line(
                MathTex(
                    r"z^{n}=r^{n}\bigl(\cos(n\theta)+i\sin(n\theta)\bigr)",
                    font_size=24,
                    color=GREEN,
                ),
                font_size=16,
            ),
            self._line(
                MathTex(r"z^{n}=1", font_size=22),
                "の解は",
                MathTex(
                    r"z=\cos\dfrac{2\pi k}{n}+i\sin\dfrac{2\pi k}{n}",
                    font_size=22,
                    color=GOLD,
                ),
                font_size=14,
            ),
            self._line(
                MathTex(r"k=0,1,\ldots,n-1", font_size=20, color=ORANGE),
                "。単位円上の正",
                MathTex(r"n", font_size=22, color=YELLOW),
                "角形の頂点です。",
                font_size=16,
            ),
            self._line(
                MathTex(
                    r"z^{n}-1=(z-1)\bigl(z^{n-1}+z^{n-2}+\cdots+1\bigr)",
                    font_size=20,
                    color=TEAL,
                ),
                font_size=14,
            ),
        ]
        block = self._formula_rows(rows, lead, buff=0.08, hold=self.PAUSE_COMPLEX)

        notes = [
            self.ja_text(
                "実数に足りない分は、円の上へ等間隔に出ます。",
                font_size=16,
            ),
            self._line(
                MathTex(r"k=1", font_size=20, color=GREEN),
                "の点を",
                MathTex(r"\omega", font_size=24, color=GREEN),
                "とおくと、",
                MathTex(r"1,\omega,\omega^{2},\ldots,\omega^{n-1}", font_size=20),
                "は巡回です。",
                font_size=14,
            ),
            self._line(
                MathTex(r"n=3", font_size=20, color=YELLOW),
                "なら",
                MathTex(r"\omega=\dfrac{-1+i\sqrt{3}}{2}", font_size=20, color=GREEN),
                "、",
                MathTex(r"\omega^{3}=1", font_size=20),
                "、",
                MathTex(r"1+\omega+\omega^{2}=0", font_size=20, color=GOLD),
                font_size=12,
            ),
        ]
        extra = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, block, buff=0.10)
            else:
                self.stack_below(mob, extra, buff=0.08)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            extra.add(mob)
            self._read(mob)

    def part_summary(self):
        chip = self.begin_step("まとめ", self.header)

        rows = [
            self._line(
                "実数だけだと、",
                MathTex(r"z^{n}=1", font_size=24, color=YELLOW),
                "の解は",
                MathTex(r"n", font_size=24, color=YELLOW),
                "個に足りないことがある",
                font_size=16,
            ),
            self._line(
                "極形式では",
                MathTex(r"r=1", font_size=22, color=TEAL),
                "、角",
                MathTex(r"\theta=\dfrac{2\pi k}{n}", font_size=24, color=GOLD),
                font_size=16,
            ),
            self._line(
                "解は単位円上に",
                MathTex(r"n", font_size=22, color=YELLOW),
                "個。隣の中心角は",
                MathTex(r"\dfrac{2\pi}{n}", font_size=22, color=YELLOW),
                "。正",
                MathTex(r"n", font_size=22),
                "角形の頂点",
                font_size=14,
            ),
            self._line(
                MathTex(
                    r"z^{n}=r^{n}(\cos n\theta+i\sin n\theta)",
                    font_size=22,
                    color=GREEN,
                ),
                "。これをド・モアブルの定理とおく",
                font_size=14,
            ),
            self._line(
                MathTex(r"n=3", font_size=20, color=YELLOW),
                "なら",
                MathTex(r"1+\omega+\omega^{2}=0", font_size=22, color=GOLD),
                "です。3 点が原点のまわりで打ち消し合います。",
                font_size=14,
            ),
        ]
        shown = VGroup()
        for i, mob in enumerate(rows):
            if i == 0:
                self.below_chip(mob, chip, buff=0.20)
            else:
                self.stack_below(mob, shown, buff=0.12)
            self._fit_left(mob, 13.0)
            self.play(FadeIn(mob), run_time=0.55)
            shown.add(mob)
            self._read(mob)
            if i == 2:
                self.pause_conclusion()

    def _roots_figure(self, n=4, r=1.30, labels=True, polygon=False, names=None):
        circ = Circle(radius=r, color=GREY_B, stroke_width=2.0)
        xax = Line(LEFT * (r + 0.40), RIGHT * (r + 0.40), color=GREY_A, stroke_width=1.6)
        yax = Line(DOWN * (r + 0.32), UP * (r + 0.32), color=GREY_A, stroke_width=1.6)
        group = VGroup(xax, yax, circ)
        cols = [YELLOW, GREEN, ORANGE, TEAL, GOLD, BLUE_B]
        verts = []
        if n > 0:
            for k in range(n):
                ang = 2 * PI * k / n
                p = r * np.array([np.cos(ang), np.sin(ang), 0.0])
                verts.append(p)
                col = cols[k % len(cols)]
                group.add(Dot(p, radius=0.08, color=col))
                if labels:
                    if names is not None and k < len(names):
                        lab = MathTex(names[k], font_size=20, color=col)
                    else:
                        lab = MathTex(rf"{k}", font_size=18, color=col)
                    radial = p / (np.linalg.norm(p) + 1e-9)
                    lab.next_to(p, radial, buff=0.12)
                    group.add(lab)
            if polygon and len(verts) >= 3:
                poly = Polygon(*verts, color=TEAL, stroke_width=2.4)
                poly.set_fill(TEAL, 0.08)
                group.add(poly)
                group.submobjects.remove(poly)
                group.submobjects.insert(3, poly)
        frame = Rectangle(
            width=(r + 0.70) * 2,
            height=(r + 0.55) * 2,
            stroke_opacity=0.0,
        )
        frame.move_to(ORIGIN)
        return VGroup(frame, group)

    def _read(self, mob, extra=0.0):
        if hasattr(mob, "text"):
            self.linger(mob.text, extra=extra)
            return
        parts = [sub.text for sub in mob if hasattr(sub, "text")]
        self.linger("".join(parts) if parts else 2.0, extra=extra)

    def _line(self, *chunks, font_size=24, color=None, buff=0.08):
        parts = []
        for chunk in chunks:
            if isinstance(chunk, str):
                kw = {"font_size": font_size}
                if color is not None:
                    kw["color"] = color
                parts.append(self.ja_text(chunk, **kw))
            else:
                parts.append(chunk)
        return VGroup(*parts).arrange(RIGHT, buff=buff)

    def _formula_rows(self, rows, under, buff=0.36, hold=None):
        if hold is None:
            hold = self.PAUSE_COMPLEX
        block = VGroup(*rows).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        self.stack_below(block, under, buff=buff)
        block.set_x(0)
        self._fit(block, 12.6)
        block.set_x(0)
        for row in block:
            self.play(FadeIn(row), run_time=self.PAUSE_REWRITE)
            super().wait(hold)
        return block

    def _fit(self, mob, max_w=12.4):
        if mob.width > max_w:
            mob.scale_to_fit_width(max_w)
        return mob

    def _fit_left(self, mob, max_w=12.2):
        left = mob.get_left().copy()
        self._fit(mob, max_w)
        mob.shift(left - mob.get_left())
        return mob

    def _nudge(self, mob):
        frame_left = -config.frame_width / 2 + 0.08
        overflow = frame_left - mob.get_left()[0]
        if overflow > 0:
            mob.shift(RIGHT * overflow)
        frame_right = config.frame_width / 2 - 0.08
        over_r = mob.get_right()[0] - frame_right
        if over_r > 0:
            mob.shift(LEFT * over_r)
        return mob
