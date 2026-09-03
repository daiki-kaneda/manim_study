from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import LessonScene


class ComplexAsRotation(LessonScene):
    """#17 i を掛けるとなぜ 90 度回るか（約9分）"""

    def construct(self):
        self.header = self._open_header()
        self.part_question()
        self.part_trial_missing()
        self.part_trial_one()
        self.part_step1_point()
        self.part_step2_angle()
        self.part_step3_general()
        self.part_step4_polar()
        self.part_example()
        self.part_generalize()
        self.part_summary()

    def _open_header(self):
        title = self._line(
            MathTex(r"i", font_size=40, color=YELLOW),
            "を掛けるとなぜ 90 度回るか",
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
        fig = self._plane(size=2.05)
        cap = self._line(
            MathTex(r"i^{2}=-1", font_size=26, color=YELLOW),
            "を満たす数",
            MathTex(r"i", font_size=26, color=YELLOW),
            "を、無い数とせず、平面の点と見てみます。",
            font_size=16,
        )
        self._fit(cap, 13.0)
        pair = VGroup(fig, cap).arrange(DOWN, buff=0.24)
        pair.next_to(self.header, DOWN, buff=0.24)
        pair.set_x(0)
        self._nudge(pair)
        self.play(FadeIn(fig), FadeIn(cap), run_time=0.8)
        self.pause_new_screen()
        self.linger("i^2=-1 を満たす数 i を、無い数とせず、平面の点と見てみます。")

        q1 = self._line(
            "このとき、何かの数に",
            MathTex(r"i", font_size=24, color=YELLOW),
            "を掛ける操作は、何をしているのでしょうか。",
            font_size=18,
        )
        self.stack_below(q1, pair, buff=0.16)
        q1.set_x(0)
        self._fit(q1, 13.0)
        q1.set_x(0)
        self.play(FadeIn(q1), run_time=0.7)
        self.linger("このとき、何かの数に i を掛ける操作は、何をしているのでしょうか。")

        q2 = self.ja_text("90 度回している、と言ってよいのでしょうか。", font_size=20)
        self.stack_below(q2, q1, buff=0.12)
        q2.set_x(0)
        self.play(FadeIn(q2), run_time=0.7)
        self.linger(q2.text, extra=0.35)

    def part_trial_missing(self):
        chip = self.begin_step("試行  無い数？", self.header)

        lead = self.ja_text(
            "まず、平方して -1 になる実数を探して、無い、と結論してみます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        rows = [
            self.ja_text("正の数の平方は正です。", font_size=18),
            self.ja_text("負の数の平方も正です。", font_size=18),
            self._line(
                MathTex(r"0", font_size=26),
                "の平方は",
                MathTex(r"0", font_size=26),
                "です。",
                font_size=18,
            ),
            self._line(
                "だから実数の中には、平方して",
                MathTex(r"-1", font_size=26, color=ORANGE),
                "になる数はありません。",
                font_size=18,
            ),
        ]
        block = self._formula_rows(rows, lead, buff=0.12, hold=self.PAUSE_COMPLEX)

        notes = [
            self.ja_text("実数の数直線の上には、確かにありません。", font_size=18),
            self.ja_text(
                "無い数のように感じます。無い、で止めると、掛ける操作を見る場所がなくなります。",
                font_size=16,
            ),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, block, buff=0.14)
            else:
                self.stack_below(mob, shown, buff=0.10)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            shown.add(mob)
            self.linger(mob.text)

    def part_trial_one(self):
        chip = self.begin_step("試行  1 に掛ける", self.header)

        lead = self._line(
            "約束",
            MathTex(r"i^{2}=-1", font_size=24, color=YELLOW),
            "だけを使って、1 に",
            MathTex(r"i", font_size=24, color=YELLOW),
            "を繰り返し掛けてみます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger("約束 i^2=-1 だけを使って、1 に i を繰り返し掛けてみます。")
        self.play(FadeOut(lead), run_time=0.45)

        fig = self._plane(size=2.15, points=[(1, 0, "1"), (0, 1, "i"), (-1, 0, "-1"), (0, -1, "-i")])
        self.below_chip(fig, chip, buff=0.12)
        fig.set_x(-2.4)
        self._nudge(fig)
        self.play(FadeIn(fig), run_time=0.8)
        self.pause_new_screen()

        table = self.aligned_table(
            [
                [
                    self.ja_text("式", font_size=16, color=GREY_B),
                    self.ja_text("点", font_size=16, color=GREY_B),
                ],
                [MathTex(r"1", font_size=24), MathTex(r"(1,0)", font_size=24)],
                [MathTex(r"i", font_size=24, color=YELLOW), MathTex(r"(0,1)", font_size=24, color=YELLOW)],
                [MathTex(r"-1", font_size=24, color=ORANGE), MathTex(r"(-1,0)", font_size=24, color=ORANGE)],
                [MathTex(r"-i", font_size=24, color=TEAL), MathTex(r"(0,-1)", font_size=24, color=TEAL)],
            ],
            h_buff=0.32,
            v_buff=0.08,
        )
        table.scale(0.78)
        table.next_to(fig, RIGHT, buff=0.45, aligned_edge=UP)
        self.play(FadeIn(table), run_time=0.7)

        notes = [
            self.ja_text(
                "原点のまわりを、左へ 90 度ずつ回っているように見えます。",
                font_size=18,
            ),
            self.ja_text("1 以外の点でも同じか、まだ分かりません。", font_size=18),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, fig, buff=0.16)
            else:
                self.stack_below(mob, shown, buff=0.10)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            shown.add(mob)
            self.linger(mob.text)

    def part_step1_point(self):
        chip = self.begin_step("STEP 1  平面の点", self.header)

        lead = self.ja_text(
            "複素数を、平面の点として書く決まりを置きます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        rows = [
            self._line(
                "実数",
                MathTex(r"a", font_size=24, color=TEAL),
                "と実数",
                MathTex(r"b", font_size=24, color=ORANGE),
                "を使って、",
                MathTex(r"z=a+bi", font_size=28, color=YELLOW),
                "とおく。",
                font_size=18,
            ),
            self._line(
                "これを点",
                MathTex(r"(a,b)", font_size=26, color=YELLOW),
                "とおく。",
                font_size=18,
            ),
            self.ja_text("実軸が横、虚軸が縦です。", font_size=18),
            self._line(
                MathTex(r"i", font_size=24, color=YELLOW),
                "自身は",
                MathTex(r"0+1\cdot i", font_size=26),
                "なので、点",
                MathTex(r"(0,1)", font_size=26, color=YELLOW),
                "です。",
                font_size=18,
            ),
        ]
        shown = self._formula_rows(rows, lead, buff=0.12, hold=self.PAUSE_COMPLEX)

        notes = [
            self.ja_text("無い数ではなく、座標が 2 つある数、と見ます。", font_size=18),
            self.ja_text("掛ける操作は、この点を別の点へ移す写し方です。", font_size=18),
        ]
        extra = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, shown, buff=0.12)
            else:
                self.stack_below(mob, extra, buff=0.10)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            extra.add(mob)
            self.linger(mob.text)

    def part_step2_angle(self):
        chip = self.begin_step("STEP 2  90 度", self.header)

        lead = self._line(
            "1 に",
            MathTex(r"i", font_size=24, color=YELLOW),
            "を掛けた 4 点が、原点を中心に何度回ったかを測ります。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger("1 に i を掛けた 4 点が、原点を中心に何度回ったかを測ります。")
        self.play(FadeOut(lead), run_time=0.40)

        fig = self._plane(
            size=2.20,
            points=[(1, 0, "1"), (0, 1, "i"), (-1, 0, "-1"), (0, -1, "-i")],
            arrows=True,
            right_angle=True,
        )
        self.below_chip(fig, chip, buff=0.12)
        fig.set_x(0)
        self.play(FadeIn(fig), run_time=0.8)
        self.pause_new_screen()

        notes = [
            self._line(
                MathTex(r"(1,0)", font_size=22),
                "から",
                MathTex(r"(0,1)", font_size=22, color=YELLOW),
                "は、左へ 90 度です。",
                font_size=18,
            ),
            self._line(
                MathTex(r"(0,1)", font_size=22, color=YELLOW),
                "から",
                MathTex(r"(-1,0)", font_size=22, color=ORANGE),
                "も左へ 90 度です。時計まわりではありません。",
                font_size=16,
            ),
            self.ja_text(
                "単位円の上では、i を 1 回掛けると 90 度左へ回ります。",
                font_size=18,
            ),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, fig, buff=0.14)
            else:
                self.stack_below(mob, shown, buff=0.10)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            shown.add(mob)
            self.linger(mob.text)
            if i == 1:
                self.pause_conclusion()

    def part_step3_general(self):
        chip = self.begin_step("STEP 3  一般の点", self.header)

        lead = self._line(
            "任意の点",
            MathTex(r"a+bi", font_size=26, color=YELLOW),
            "に",
            MathTex(r"i", font_size=26, color=YELLOW),
            "を掛けて、成分で確かめます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger("任意の点 a+bi に i を掛けて、成分で確かめます。")

        restate = self._line(
            MathTex(r"z=a+bi", font_size=26, color=YELLOW),
            "を点",
            MathTex(r"(a,b)", font_size=26, color=TEAL),
            "と見ます。",
            font_size=18,
        )
        self.stack_below(restate, lead, buff=0.10)
        restate.set_x(0)
        self.play(FadeIn(restate), run_time=0.55)
        self.linger("z=a+bi を点 (a,b) と見ます。")
        self.play(FadeOut(lead), run_time=0.40)

        rows = [
            self._line(
                MathTex(r"(a+bi)\cdot i=ai+bi^{2}", font_size=28, color=YELLOW),
                font_size=16,
            ),
            self._line(
                MathTex(r"i^{2}=-1", font_size=24),
                "なので",
                MathTex(r"ai+b(-1)=-b+ai", font_size=28, color=GREEN),
                font_size=16,
            ),
            self._line(
                "点",
                MathTex(r"(a,b)", font_size=24, color=TEAL),
                "は点",
                MathTex(r"(-b,a)", font_size=24, color=ORANGE),
                "へ移ります。",
                font_size=18,
            ),
        ]
        block = self._formula_rows(rows, restate, buff=0.10, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(block), run_time=0.40)

        fig = self._ab_figure()
        self.stack_below(fig, restate, buff=0.12)
        fig.set_x(0)
        self.play(FadeIn(fig), run_time=0.8)
        self.pause_new_screen()

        notes = [
            self._line(
                "横が",
                MathTex(r"a", font_size=22, color=TEAL),
                "、縦が",
                MathTex(r"b", font_size=22, color=ORANGE),
                "だった点は、横が",
                MathTex(r"-b", font_size=22, color=ORANGE),
                "、縦が",
                MathTex(r"a", font_size=22, color=TEAL),
                "になります。",
                font_size=16,
            ),
            self.ja_text(
                "これは、原点を中心に左へ 90 度回す写し方です。成分で確かめる方法です。",
                font_size=18,
            ),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, fig, buff=0.12)
            else:
                self.stack_below(mob, shown, buff=0.10)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            shown.add(mob)
            self.linger(mob.text)

    def part_step4_polar(self):
        chip = self.begin_step("STEP 4  極形式", self.header)

        lead = self.ja_text(
            "長さと角度で書くと、掛けることが足し算になります。",
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
                MathTex(r"i=\cos\dfrac{\pi}{2}+i\sin\dfrac{\pi}{2}", font_size=26, color=ORANGE),
                "です。",
                font_size=18,
            ),
        ]
        block = self._formula_rows(rows, lead, buff=0.10, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(VGroup(lead, block)), run_time=0.40)

        add = self.ja_text(
            "余弦と正弦の加法定理を認めて使います。",
            font_size=16,
            color=GREY_B,
        )
        self.below_chip(add, chip, buff=0.14)
        add.set_x(0)
        self.play(FadeIn(add), run_time=0.5)
        self.linger(add.text)

        more = [
            self._line(
                MathTex(
                    r"z\cdot i=r\left(\cos\left(\theta+\dfrac{\pi}{2}\right)+i\sin\left(\theta+\dfrac{\pi}{2}\right)\right)",
                    font_size=24,
                    color=GREEN,
                ),
                font_size=14,
            ),
            self._line(
                MathTex(r"\cos\left(\theta+\dfrac{\pi}{2}\right)=-\sin\theta", font_size=24),
                "、",
                MathTex(r"\sin\left(\theta+\dfrac{\pi}{2}\right)=\cos\theta", font_size=24),
                font_size=16,
            ),
            self._line(
                "だから",
                MathTex(
                    r"r(\cos\theta+i\sin\theta)\cdot i=r(-\sin\theta+i\cos\theta)",
                    font_size=22,
                    color=GREEN,
                ),
                font_size=14,
            ),
            self._line(
                "成分は",
                MathTex(r"(-r\sin\theta,\ r\cos\theta)", font_size=24, color=ORANGE),
                "。これは STEP 3 の",
                MathTex(r"(-b,a)", font_size=24, color=ORANGE),
                "と同じです。",
                font_size=16,
            ),
        ]
        shown = self._formula_rows(more, add, buff=0.10, hold=self.PAUSE_COMPLEX)

        notes = [
            self._line(
                "長さは変わらず、角だけ",
                MathTex(r"\dfrac{\pi}{2}", font_size=24, color=YELLOW),
                "増えます。",
                font_size=18,
            ),
            self.ja_text(
                "実数を掛けると長さが変わり、角は 0 度か 180 度しか回りません。90 度は実数の掛け算では書けません。",
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
            self.linger(mob.text)
            if i == 1:
                self.pause_conclusion()

    def part_example(self):
        chip = self.begin_step("実例", self.header)

        lead = self._line(
            MathTex(r"3+2i", font_size=26, color=YELLOW),
            "に",
            MathTex(r"i", font_size=26, color=YELLOW),
            "を掛けて、成分と図を最後まで通します。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger("3+2i に i を掛けて、成分と図を最後まで通します。")

        rows = [
            self._line(
                MathTex(r"(3+2i)\cdot i=3i+2i^{2}=3i-2=-2+3i", font_size=26, color=GREEN),
                font_size=16,
            ),
            self._line(
                "点",
                MathTex(r"(3,2)", font_size=24, color=TEAL),
                "は点",
                MathTex(r"(-2,3)", font_size=24, color=ORANGE),
                "へ移ります。",
                font_size=18,
            ),
            self._line(
                "長さ:",
                MathTex(r"\sqrt{3^{2}+2^{2}}=\sqrt{13}", font_size=24, color=YELLOW),
                "。行き先も",
                MathTex(r"\sqrt{(-2)^{2}+3^{2}}=\sqrt{13}", font_size=24, color=YELLOW),
                font_size=16,
            ),
        ]
        block = self._formula_rows(rows, lead, buff=0.10, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(VGroup(lead, block)), run_time=0.40)

        fig = self._example_points()
        self.below_chip(fig, chip, buff=0.10)
        fig.set_x(-2.6)
        self.play(FadeIn(fig), run_time=0.8)

        table = self.aligned_table(
            [
                [
                    self.ja_text(" ", font_size=14, color=GREY_B),
                    self.ja_text("点", font_size=14, color=GREY_B),
                    self.ja_text("長さ", font_size=14, color=GREY_B),
                ],
                [
                    self.ja_text("もと", font_size=16),
                    MathTex(r"(3,2)", font_size=22, color=TEAL),
                    MathTex(r"\sqrt{13}", font_size=22, color=YELLOW),
                ],
                [
                    self.ja_text("あと", font_size=16),
                    MathTex(r"(-2,3)", font_size=22, color=ORANGE),
                    MathTex(r"\sqrt{13}", font_size=22, color=YELLOW),
                ],
            ],
            h_buff=0.28,
            v_buff=0.08,
        )
        table.scale(0.82)
        table.next_to(fig, RIGHT, buff=0.40, aligned_edge=UP)
        self.play(FadeIn(table), run_time=0.7)

        notes = [
            self.ja_text("長さは同じで、左へ 90 度回っています。", font_size=18),
            self.ja_text("1 のときと同じ写し方です。", font_size=18),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, fig, buff=0.14)
            else:
                self.stack_below(mob, shown, buff=0.10)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            shown.add(mob)
            self.linger(mob.text)

    def part_generalize(self):
        chip = self.begin_step("一般化", self.header)

        lead = self.ja_text(
            "今やったことは、複素数の掛け算が拡大と回転である、という考え方でした。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)
        self.pause_conclusion()

        rows = [
            self._line(
                MathTex(r"z=r(\cos\theta+i\sin\theta)", font_size=22, color=YELLOW),
                "、",
                MathTex(r"w=s(\cos\phi+i\sin\phi)", font_size=22, color=TEAL),
                "とおく。",
                font_size=16,
            ),
            self._line(
                MathTex(
                    r"zw=rs\bigl(\cos(\theta+\phi)+i\sin(\theta+\phi)\bigr)",
                    font_size=24,
                    color=GREEN,
                ),
                font_size=16,
            ),
            self._line(
                "長さは積",
                MathTex(r"rs", font_size=24, color=YELLOW),
                "、角は和",
                MathTex(r"\theta+\phi", font_size=24, color=ORANGE),
                "です。",
                font_size=18,
            ),
            self._line(
                "とくに",
                MathTex(r"w=i", font_size=24, color=YELLOW),
                "なら",
                MathTex(r"s=1", font_size=24),
                "、",
                MathTex(r"\phi=\dfrac{\pi}{2}", font_size=24, color=YELLOW),
                "。長さはそのまま、角は",
                MathTex(r"\dfrac{\pi}{2}", font_size=24, color=YELLOW),
                "増えます。",
                font_size=14,
            ),
        ]
        block = self._formula_rows(rows, lead, buff=0.10, hold=self.PAUSE_COMPLEX)

        notes = [
            self.ja_text(
                "実数だけでは、90 度回転を掛け算で書けません。",
                font_size=18,
            ),
            self._line(
                MathTex(r"-1", font_size=24, color=ORANGE),
                "を掛けるのは 180 度回転です。",
                MathTex(r"i^{2}=-1", font_size=24, color=YELLOW),
                "は、90 度を 2 回回ると反対向き、と読めます。",
                font_size=16,
            ),
        ]
        extra = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, block, buff=0.12)
            else:
                self.stack_below(mob, extra, buff=0.10)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            extra.add(mob)
            self.linger(mob.text)

    def part_summary(self):
        chip = self.begin_step("まとめ", self.header)

        rows = [
            self._line(
                "実数の中には、平方して",
                MathTex(r"-1", font_size=24, color=ORANGE),
                "になる数はありません",
                font_size=18,
            ),
            self._line(
                MathTex(r"i", font_size=24, color=YELLOW),
                "を平面の点",
                MathTex(r"(0,1)", font_size=24, color=YELLOW),
                "と見ると、1 に",
                MathTex(r"i", font_size=24),
                "を掛けるたびに左へ 90 度回る",
                font_size=16,
            ),
            self._line(
                MathTex(r"(a+bi)\cdot i=-b+ai", font_size=24, color=GREEN),
                "。点",
                MathTex(r"(a,b)", font_size=22),
                "は点",
                MathTex(r"(-b,a)", font_size=22),
                "へ移る",
                font_size=16,
            ),
            self._line(
                "極形式では長さはそのまま、角に",
                MathTex(r"\dfrac{\pi}{2}", font_size=24, color=YELLOW),
                "が足される。掛け算は拡大と回転",
                font_size=16,
            ),
            self._line(
                MathTex(r"i^{2}=-1", font_size=24, color=YELLOW),
                "は、90 度を 2 回回ると 180 度、つまり",
                MathTex(r"-1", font_size=24, color=ORANGE),
                "倍です。",
                font_size=16,
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
            self.linger(2.0)
            if i == 2:
                self.pause_conclusion()

    def _plane(self, size=2.2, points=None, arrows=False, right_angle=False):
        xax = Line(LEFT * size, RIGHT * size, color=GREY_B, stroke_width=2.0)
        yax = Line(DOWN * size, UP * size, color=GREY_B, stroke_width=2.0)
        xl = MathTex(r"1", font_size=16, color=GREY_B)
        xl.next_to(xax.get_right(), DOWN, buff=0.08)
        yl = MathTex(r"i", font_size=16, color=GREY_B)
        yl.next_to(yax.get_top(), LEFT, buff=0.08)
        group = VGroup(xax, yax, xl, yl)
        if points:
            scale = size * 0.72
            cols = [YELLOW, ORANGE, TEAL, GREEN]
            prev = None
            for i, (a, b, name) in enumerate(points):
                p = np.array([a * scale, b * scale, 0.0])
                dot = Dot(p, radius=0.08, color=cols[i % len(cols)])
                lab = MathTex(name, font_size=20, color=cols[i % len(cols)])
                if abs(a) >= abs(b):
                    lab.next_to(dot, DOWN if b <= 0 else UP, buff=0.10)
                else:
                    lab.next_to(dot, RIGHT if a >= 0 else LEFT, buff=0.10)
                group.add(dot, lab)
                if arrows:
                    arr = Arrow(ORIGIN, p, buff=0.08, color=cols[i % len(cols)], stroke_width=3.0)
                    group.add(arr)
                if right_angle and prev is not None and i == 1:
                    mark = RightAngle(
                        Line(ORIGIN, prev),
                        Line(ORIGIN, p),
                        length=0.22,
                        color=YELLOW,
                        stroke_width=2.5,
                    )
                    group.add(mark)
                prev = p
        frame = Rectangle(width=size * 2.15, height=size * 2.15, stroke_opacity=0.0)
        frame.move_to(ORIGIN)
        return VGroup(frame, group)

    def _ab_figure(self):
        size = 1.85
        plane = self._plane(size=size)
        a, b = 1.15, 0.70
        p = np.array([a, b, 0.0])
        q = np.array([-b, a, 0.0])
        d1 = Dot(p, radius=0.08, color=TEAL)
        d2 = Dot(q, radius=0.08, color=ORANGE)
        a1 = Arrow(ORIGIN, p, buff=0.08, color=TEAL, stroke_width=3.2)
        a2 = Arrow(ORIGIN, q, buff=0.08, color=ORANGE, stroke_width=3.2)
        l1 = MathTex(r"(a,b)", font_size=20, color=TEAL)
        l1.next_to(d1, RIGHT, buff=0.10)
        l2 = MathTex(r"(-b,a)", font_size=20, color=ORANGE)
        l2.next_to(d2, LEFT, buff=0.10)
        mark = RightAngle(Line(ORIGIN, p), Line(ORIGIN, q), length=0.20, color=YELLOW, stroke_width=2.5)
        body = VGroup(plane, a1, a2, d1, d2, l1, l2, mark)
        return body

    def _example_points(self):
        size = 1.90
        plane = self._plane(size=size)
        s = 0.42
        p = np.array([3 * s, 2 * s, 0.0])
        q = np.array([-2 * s, 3 * s, 0.0])
        d1 = Dot(p, radius=0.08, color=TEAL)
        d2 = Dot(q, radius=0.08, color=ORANGE)
        a1 = Arrow(ORIGIN, p, buff=0.08, color=TEAL, stroke_width=3.2)
        a2 = Arrow(ORIGIN, q, buff=0.08, color=ORANGE, stroke_width=3.2)
        l1 = MathTex(r"(3,2)", font_size=18, color=TEAL)
        l1.next_to(d1, RIGHT, buff=0.08)
        l2 = MathTex(r"(-2,3)", font_size=18, color=ORANGE)
        l2.next_to(d2, LEFT, buff=0.08)
        mark = RightAngle(Line(ORIGIN, p), Line(ORIGIN, q), length=0.18, color=YELLOW, stroke_width=2.5)
        return VGroup(plane, a1, a2, d1, d2, l1, l2, mark)

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
        block = VGroup(*rows).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
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
