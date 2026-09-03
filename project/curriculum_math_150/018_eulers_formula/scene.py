from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import LessonScene


class EulersFormula(LessonScene):
    """#18 e^{iπ}+1=0 はなぜか（約10分）"""

    def construct(self):
        self.header = self._open_header()
        self.part_question()
        self.part_trial_separate()
        self.part_trial_rotate()
        self.part_step1_series()
        self.part_step2_powers()
        self.part_step3_parts()
        self.part_step4_pi()
        self.part_example()
        self.part_generalize()
        self.part_summary()

    def _open_header(self):
        title = self._line(
            MathTex(r"e^{i\pi}+1=0", font_size=40, color=YELLOW),
            "はなぜか",
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
        fig = self._unit_circle(mark_minus=True)
        cap = self._line(
            "指数の底",
            MathTex(r"e", font_size=24, color=YELLOW),
            "、円周率",
            MathTex(r"\pi", font_size=24, color=TEAL),
            "、平方して",
            MathTex(r"-1", font_size=24, color=ORANGE),
            "になる",
            MathTex(r"i", font_size=24, color=GREEN),
            "が、一つの式に入ります。",
            font_size=16,
        )
        self._fit(cap, 13.0)
        pair = VGroup(fig, cap).arrange(DOWN, buff=0.22)
        pair.next_to(self.header, DOWN, buff=0.22)
        pair.set_x(0)
        self._nudge(pair)
        self.play(FadeIn(fig), FadeIn(cap), run_time=0.8)
        self.pause_new_screen()
        self.linger("指数の底 e、円周率 π、平方して -1 になる i が、一つの式に入ります。")

        q1 = self.ja_text("これは、どういう回転の話なのでしょうか。", font_size=20)
        self.stack_below(q1, pair, buff=0.16)
        q1.set_x(0)
        self.play(FadeIn(q1), run_time=0.7)
        self.linger(q1.text)

        q2 = self._line(
            "左辺が 0 になるのは、どこで",
            MathTex(r"-1", font_size=24, color=ORANGE),
            "と",
            MathTex(r"+1", font_size=24, color=YELLOW),
            "が打ち消し合うからでしょうか。",
            font_size=18,
        )
        self.stack_below(q2, q1, buff=0.12)
        q2.set_x(0)
        self._fit(q2, 13.0)
        q2.set_x(0)
        self.play(FadeIn(q2), run_time=0.7)
        self.linger("左辺が 0 になるのは、どこで -1 と +1 が打ち消し合うからでしょうか。", extra=0.35)

    def part_trial_separate(self):
        chip = self.begin_step("試行  別々", self.header)

        lead = self._line(
            "まず、",
            MathTex(r"e", font_size=24, color=YELLOW),
            "と",
            MathTex(r"\pi", font_size=24, color=TEAL),
            "と",
            MathTex(r"i", font_size=24, color=GREEN),
            "を、互いに無関係な定数として並べてみます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger("まず、e と π と i を、互いに無関係な定数として並べてみます。")

        rows = [
            self._line(
                MathTex(r"e", font_size=26, color=YELLOW),
                "は、利息を細かくした極限などから出る数です。およそ",
                MathTex(r"2.718", font_size=24, color=YELLOW),
                font_size=16,
            ),
            self._line(
                MathTex(r"\pi", font_size=26, color=TEAL),
                "は円周と直径の比です。",
                font_size=18,
            ),
            self._line(
                MathTex(r"i", font_size=26, color=GREEN),
                "は",
                MathTex(r"i^{2}=-1", font_size=26, color=ORANGE),
                "を満たす数です。",
                font_size=18,
            ),
            self.ja_text(
                "掛けて足す場所が無いと、一つの式になる理由が見えません。",
                font_size=18,
            ),
        ]
        block = self._formula_rows(rows, lead, buff=0.12, hold=self.PAUSE_COMPLEX)

        notes = [
            self.ja_text(
                "別々の定数のままでは、なぜ +1 して 0 になるのか分かりません。",
                font_size=18,
            ),
            self.ja_text("同じ平面の回転として、つなぐ方法を見ます。", font_size=18),
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
            self._read(mob)

    def part_trial_rotate(self):
        chip = self.begin_step("試行  90 度", self.header)

        lead = self._line(
            MathTex(r"i", font_size=24, color=GREEN),
            "を平面の点と見ると、掛ける操作は左へ 90 度回すことです。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger("i を平面の点と見ると、掛ける操作は左へ 90 度回すことです。")
        self.play(FadeOut(lead), run_time=0.40)

        fig = self._unit_circle(points=True)
        self.below_chip(fig, chip, buff=0.14)
        fig.set_x(0)
        self.play(FadeIn(fig), run_time=0.8)
        self.pause_new_screen()

        rows = [
            self._line(
                MathTex(r"1", font_size=24),
                "は点",
                MathTex(r"(1,0)", font_size=24, color=YELLOW),
                font_size=18,
            ),
            self._line(
                MathTex(r"1\cdot i=i", font_size=24, color=GREEN),
                "は点",
                MathTex(r"(0,1)", font_size=24, color=GREEN),
                "。左へ 90 度です。",
                font_size=18,
            ),
            self._line(
                MathTex(r"i\cdot i=-1", font_size=24, color=ORANGE),
                "は点",
                MathTex(r"(-1,0)", font_size=24, color=ORANGE),
                "。さらに 90 度、合わせて 180 度です。",
                font_size=16,
            ),
        ]
        block = self._formula_rows(rows, fig, buff=0.12, hold=self.PAUSE_COMPLEX)

        notes = [
            self._line(
                MathTex(r"-1", font_size=24, color=ORANGE),
                "は、1 を 180 度回した点です。",
                font_size=18,
            ),
            self._line(
                "式が 0 になるなら、どこかでこの",
                MathTex(r"-1", font_size=24, color=ORANGE),
                "と",
                MathTex(r"+1", font_size=24, color=YELLOW),
                "が出会うはずです。",
                font_size=18,
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
            self._read(mob)

    def part_step1_series(self):
        chip = self.begin_step("STEP 1  級数", self.header)

        lead = self.ja_text(
            "指数関数を、多項式を足した式で書きます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        rows = [
            self._line(
                "実数",
                MathTex(r"x", font_size=24),
                "に対し、",
                MathTex(
                    r"e^{x}=1+x+\dfrac{x^{2}}{2}+\dfrac{x^{3}}{6}+\dfrac{x^{4}}{24}+\dfrac{x^{5}}{120}+\cdots",
                    font_size=22,
                    color=YELLOW,
                ),
                "とおく。",
                font_size=14,
            ),
            self._line(
                "分母は",
                MathTex(r"1,\ 1,\ 2,\ 6,\ 24,\ 120", font_size=22, color=TEAL),
                "、つまり",
                MathTex(r"k!", font_size=24, color=TEAL),
                "です。",
                font_size=16,
            ),
            self._line(
                MathTex(r"x=0", font_size=24),
                "なら",
                MathTex(r"e^{0}=1", font_size=26, color=YELLOW),
                "。",
                MathTex(r"x=1", font_size=24),
                "なら",
                MathTex(r"e", font_size=26, color=YELLOW),
                "に近づきます。",
                font_size=16,
            ),
        ]
        shown = self._formula_rows(rows, lead, buff=0.12, hold=self.PAUSE_COMPLEX)

        notes = [
            self._line(
                "この足し算は、実数の",
                MathTex(r"x", font_size=24),
                "で使っている式です。",
                font_size=18,
            ),
            self._line(
                "同じ形のまま、",
                MathTex(r"x", font_size=24),
                "のところへ",
                MathTex(r"i\theta", font_size=24, color=GREEN),
                "を入れる方法を次で見ます。",
                font_size=18,
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

    def part_step2_powers(self):
        chip = self.begin_step("STEP 2  i の累乗", self.header)

        lead = self._line(
            MathTex(r"i", font_size=24, color=GREEN),
            "を繰り返し掛けると、1、",
            MathTex(r"i", font_size=24, color=GREEN),
            "、",
            MathTex(r"-1", font_size=24, color=ORANGE),
            "、",
            MathTex(r"-i", font_size=24, color=TEAL),
            "が周期 4 で戻ります。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger("i を繰り返し掛けると、1、i、-1、-i が周期 4 で戻ります。")

        rows = [
            self._line(MathTex(r"i^{1}=i", font_size=28, color=GREEN), font_size=18),
            self._line(MathTex(r"i^{2}=-1", font_size=28, color=ORANGE), font_size=18),
            self._line(
                MathTex(r"i^{3}=i^{2}\cdot i=-i", font_size=28, color=TEAL),
                font_size=18,
            ),
            self._line(
                MathTex(r"i^{4}=i^{2}\cdot i^{2}=(-1)\cdot(-1)=1", font_size=26, color=YELLOW),
                font_size=16,
            ),
            self._line(MathTex(r"i^{5}=i", font_size=28, color=GREEN), font_size=18),
        ]
        block = self._formula_rows(rows, lead, buff=0.10, hold=self.PAUSE_SHORT_FORMULA)
        self.play(FadeOut(VGroup(lead, block)), run_time=0.40)

        fig = self._unit_circle(points=True)
        self.below_chip(fig, chip, buff=0.14)
        fig.set_x(0)
        self.play(FadeIn(fig), run_time=0.8)
        self.pause_new_screen()

        notes = [
            self.ja_text("偶数乗は実数、奇数乗は i の実数倍です。", font_size=18),
            self.ja_text("級数に入れると、項が実部と虚部に分かれます。", font_size=18),
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
            self._read(mob)

    def part_step3_parts(self):
        chip = self.begin_step("STEP 3  実部と虚部", self.header)

        lead = self._line(
            "級数の",
            MathTex(r"x", font_size=24),
            "に",
            MathTex(r"i\theta", font_size=24, color=GREEN),
            "を入れて、実数の項と",
            MathTex(r"i", font_size=24, color=GREEN),
            "の項に分けます。",
            font_size=16,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger("級数の x に iθ を入れて、実数の項と i の項に分けます。")

        restate = self._line(
            MathTex(r"e^{x}", font_size=24, color=YELLOW),
            "の級数と",
            MathTex(r"i^{2}=-1", font_size=24, color=ORANGE),
            "を使います。",
            MathTex(r"\theta", font_size=24, color=TEAL),
            "は実数とおく。",
            font_size=16,
        )
        self.stack_below(restate, lead, buff=0.10)
        restate.set_x(0)
        self._fit(restate, 13.0)
        restate.set_x(0)
        self.play(FadeIn(restate), run_time=0.55)
        self.linger("e^x の級数と i^2=-1 を使います。θ は実数とおく。")
        self.play(FadeOut(lead), run_time=0.40)

        rows = [
            self._line(
                MathTex(
                    r"e^{i\theta}=1+(i\theta)+\dfrac{(i\theta)^{2}}{2}+\dfrac{(i\theta)^{3}}{6}+\dfrac{(i\theta)^{4}}{24}+\dfrac{(i\theta)^{5}}{120}+\cdots",
                    font_size=18,
                    color=YELLOW,
                ),
                font_size=14,
            ),
            self._line(
                MathTex(r"(i\theta)^{2}=i^{2}\theta^{2}=-\theta^{2}", font_size=22, color=ORANGE),
                "、",
                MathTex(r"(i\theta)^{3}=-i\theta^{3}", font_size=22, color=TEAL),
                font_size=16,
            ),
            self._line(
                MathTex(r"(i\theta)^{4}=\theta^{4}", font_size=22),
                "、",
                MathTex(r"(i\theta)^{5}=i\theta^{5}", font_size=22, color=GREEN),
                font_size=16,
            ),
            self._line(
                "実部:",
                MathTex(r"1-\dfrac{\theta^{2}}{2}+\dfrac{\theta^{4}}{24}-\cdots", font_size=24, color=YELLOW),
                font_size=16,
            ),
            self._line(
                "虚部:",
                MathTex(r"\theta-\dfrac{\theta^{3}}{6}+\dfrac{\theta^{5}}{120}-\cdots", font_size=24, color=GREEN),
                font_size=16,
            ),
        ]
        block = self._formula_rows(rows, restate, buff=0.08, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(block), run_time=0.40)

        match = [
            self._line(
                MathTex(r"\cos\theta=1-\dfrac{\theta^{2}}{2}+\dfrac{\theta^{4}}{24}-\cdots", font_size=22, color=YELLOW),
                font_size=14,
            ),
            self._line(
                MathTex(r"\sin\theta=\theta-\dfrac{\theta^{3}}{6}+\dfrac{\theta^{5}}{120}-\cdots", font_size=22, color=GREEN),
                font_size=14,
            ),
            self._line(
                "だから",
                MathTex(r"e^{i\theta}=\cos\theta+i\sin\theta", font_size=30, color=GOLD),
                font_size=18,
            ),
        ]
        shown = self._formula_rows(match, restate, buff=0.10, hold=self.PAUSE_CONCLUSION)

        scope = self.ja_text(
            "厳密な収束の証明では無限級数を使います。今回は最初の数項が一致する、という範囲までとします。",
            font_size=16,
        )
        self.stack_below(scope, shown, buff=0.12)
        scope.set_x(0)
        self._fit(scope, 13.0)
        scope.set_x(0)
        self.play(FadeIn(scope), run_time=0.55)
        self.linger(scope.text)

        notes = [
            self._line(
                "指数の級数を、平面の点",
                MathTex(r"\cos\theta+i\sin\theta", font_size=22, color=GOLD),
                "と同一視します。",
                font_size=16,
            ),
            self._line(
                "角",
                MathTex(r"\theta", font_size=22, color=TEAL),
                "だけ左へ回った、単位円上の点です。",
                font_size=18,
            ),
        ]
        extra = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, scope, buff=0.10)
            else:
                self.stack_below(mob, extra, buff=0.08)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            extra.add(mob)
            self._read(mob)

    def part_step4_pi(self):
        chip = self.begin_step("STEP 4  π", self.header)

        lead = self._line(
            "角を",
            MathTex(r"\pi", font_size=26, color=TEAL),
            "、つまり 180 度に取ると、点は",
            MathTex(r"-1", font_size=26, color=ORANGE),
            "に来ます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger("角を π、つまり 180 度に取ると、点は -1 に来ます。")

        rows = [
            self._line(
                MathTex(r"\theta=\pi", font_size=26, color=TEAL),
                "を代入します。",
                font_size=18,
            ),
            self._line(
                MathTex(r"\cos\pi=-1", font_size=26, color=ORANGE),
                "、",
                MathTex(r"\sin\pi=0", font_size=26),
                font_size=18,
            ),
            self._line(
                MathTex(r"e^{i\pi}=\cos\pi+i\sin\pi=-1", font_size=28, color=YELLOW),
                font_size=16,
            ),
            self._line(
                "両辺に 1 を足す:",
                MathTex(r"e^{i\pi}+1=0", font_size=32, color=GOLD),
                font_size=18,
            ),
        ]
        block = self._formula_rows(rows, lead, buff=0.10, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(VGroup(lead, block)), run_time=0.40)

        fig = self._unit_circle(mark_minus=True, arc=True)
        self.below_chip(fig, chip, buff=0.14)
        fig.set_x(0)
        self.play(FadeIn(fig), run_time=0.8)
        self.pause_new_screen()
        self.pause_conclusion()

        notes = [
            self._line(
                MathTex(r"+1", font_size=24, color=YELLOW),
                "と打ち消し合うのは、180 度回った先が",
                MathTex(r"-1", font_size=24, color=ORANGE),
                "だからです。",
                font_size=16,
            ),
            self.ja_text(
                "指数と円周率と虚数が一つの式に入るのは、単位円を半周する回転の話です。",
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
            self._read(mob)

    def part_example(self):
        chip = self.begin_step("実例", self.header)

        lead = self._line(
            MathTex(r"\theta=\pi", font_size=24, color=TEAL),
            "で、級数の最初の数項だけを足して、",
            MathTex(r"-1", font_size=24, color=ORANGE),
            "に寄るかを見ます。",
            font_size=16,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger("θ=π で、級数の最初の数項だけを足して、-1 に寄るかを見ます。")

        rows = [
            self.ja_text("実部だけ。", font_size=16, color=GREY_B),
            self._line(
                MathTex(r"1-\dfrac{\pi^{2}}{2}+\dfrac{\pi^{4}}{24}", font_size=26, color=YELLOW),
                font_size=16,
            ),
            self._line(
                MathTex(r"\pi^{2}\approx 9.870", font_size=22),
                "、",
                MathTex(r"\dfrac{\pi^{2}}{2}\approx 4.935", font_size=22, color=ORANGE),
                font_size=16,
            ),
            self._line(
                MathTex(r"1-4.935=-3.935", font_size=24, color=ORANGE),
                font_size=16,
            ),
            self._line(
                MathTex(r"\pi^{4}\approx 97.409", font_size=22),
                "、",
                MathTex(r"\dfrac{\pi^{4}}{24}\approx 4.059", font_size=22, color=TEAL),
                font_size=16,
            ),
            self._line(
                MathTex(r"-3.935+4.059=0.124", font_size=26, color=YELLOW),
                "。まだ",
                MathTex(r"-1", font_size=24, color=ORANGE),
                "ではない。",
                font_size=16,
            ),
        ]
        block = self._formula_rows(rows, lead, buff=0.08, hold=self.PAUSE_SHORT_FORMULA)
        self.play(FadeOut(VGroup(lead, block)), run_time=0.40)

        more = [
            self._line(
                "次の項",
                MathTex(r"-\dfrac{\pi^{6}}{720}", font_size=24, color=GREEN),
                "は負で、下へ戻します。",
                font_size=16,
            ),
            self._line(
                "虚部:",
                MathTex(r"\pi-\dfrac{\pi^{3}}{6}", font_size=24, color=TEAL),
                "。",
                MathTex(r"\dfrac{\pi^{3}}{6}\approx 5.168", font_size=22),
                "、",
                MathTex(r"\pi-5.168\approx -2.026", font_size=22, color=ORANGE),
                font_size=14,
            ),
            self.ja_text("0 にはまだ遠い。あとの項で 0 に寄ります。", font_size=16),
        ]
        extra = self._formula_rows(more, chip, buff=0.14, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(extra), run_time=0.40)

        table = self.aligned_table(
            [
                [
                    self.ja_text(" ", font_size=14, color=GREY_B),
                    self.ja_text("数項の途中", font_size=14, color=GREY_B),
                    self.ja_text("全部", font_size=14, color=GREY_B),
                ],
                [
                    self.ja_text("実部", font_size=16),
                    MathTex(r"0.124", font_size=22, color=YELLOW),
                    MathTex(r"-1", font_size=22, color=ORANGE),
                ],
                [
                    self.ja_text("虚部", font_size=16),
                    self.ja_text("まだ 0 から遠い", font_size=16, color=GREY_B),
                    MathTex(r"0", font_size=22, color=GREEN),
                ],
            ],
            h_buff=0.32,
            v_buff=0.10,
        )
        table.scale(0.86)
        self.below_chip(table, chip, buff=0.16)
        table.set_x(0)
        self.play(FadeIn(table), run_time=0.7)
        self.pause_new_screen()

        notes = [
            self._line(
                "数項では粗いが、実部は",
                MathTex(r"-1", font_size=22, color=ORANGE),
                "の側へ、虚部は 0 の側へ向かいます。",
                font_size=16,
            ),
            self._line(
                "全部足した先が",
                MathTex(r"\cos\pi+i\sin\pi=-1", font_size=24, color=GOLD),
                "です。",
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

    def part_generalize(self):
        chip = self.begin_step("一般化", self.header)

        lead = self.ja_text(
            "今やったことは、オイラーの公式と呼ばれる等式でした。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)
        self.pause_conclusion()

        rows = [
            self._line(
                "角",
                MathTex(r"\theta", font_size=22, color=TEAL),
                "は実数とおく。",
                font_size=16,
            ),
            self._line(
                MathTex(r"e^{i\theta}=\cos\theta+i\sin\theta", font_size=32, color=GOLD),
                font_size=18,
            ),
            self._line(
                "とくに",
                MathTex(r"\theta=\pi", font_size=24, color=TEAL),
                "なら",
                MathTex(r"e^{i\pi}=-1", font_size=26, color=ORANGE),
                "、よって",
                MathTex(r"e^{i\pi}+1=0", font_size=28, color=YELLOW),
                font_size=16,
            ),
            self._line(
                "指数関数",
                MathTex(r"e^{i\theta}", font_size=24, color=GREEN),
                "は、角",
                MathTex(r"\theta", font_size=24, color=TEAL),
                "で単位円を等速に回る点です。",
                font_size=16,
            ),
        ]
        block = self._formula_rows(rows, lead, buff=0.10, hold=self.PAUSE_COMPLEX)

        notes = [
            self.ja_text(
                "神秘的な偶然ではなく、級数が余弦と正弦に分かれ、π で半周する、という計算です。",
                font_size=16,
            ),
            self._line(
                MathTex(r"\theta=\dfrac{\pi}{2}", font_size=24, color=TEAL),
                "なら",
                MathTex(r"e^{i\pi/2}=i", font_size=26, color=GREEN),
                "。指数の言葉で、90 度回転が書けます。",
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
            self._read(mob)

    def part_summary(self):
        chip = self.begin_step("まとめ", self.header)

        rows = [
            self._line(
                MathTex(r"i", font_size=24, color=GREEN),
                "を掛けると、平面で左へ 90 度回る。2 回で",
                MathTex(r"-1", font_size=24, color=ORANGE),
                font_size=18,
            ),
            self._line(
                MathTex(r"e^{x}", font_size=22, color=YELLOW),
                "の級数に",
                MathTex(r"x=i\theta", font_size=22, color=GREEN),
                "を入れると、実部は",
                MathTex(r"\cos\theta", font_size=22, color=YELLOW),
                "、虚部は",
                MathTex(r"\sin\theta", font_size=22, color=GREEN),
                font_size=14,
            ),
            self._line(
                MathTex(r"e^{i\theta}=\cos\theta+i\sin\theta", font_size=26, color=GOLD),
                font_size=18,
            ),
            self._line(
                MathTex(r"\theta=\pi", font_size=22, color=TEAL),
                "なら半周して",
                MathTex(r"-1", font_size=22, color=ORANGE),
                "。だから",
                MathTex(r"e^{i\pi}+1=0", font_size=26, color=YELLOW),
                font_size=16,
            ),
            self._line(
                MathTex(r"\theta=\dfrac{\pi}{2}", font_size=22, color=TEAL),
                "なら",
                MathTex(r"e^{i\pi/2}=i", font_size=24, color=GREEN),
                "です。",
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

    def _unit_circle(self, mark_minus=False, points=False, arc=False):
        r = 1.35
        circ = Circle(radius=r, color=GREY_B, stroke_width=2.0)
        xax = Line(LEFT * (r + 0.45), RIGHT * (r + 0.45), color=GREY_A, stroke_width=1.6)
        yax = Line(DOWN * (r + 0.35), UP * (r + 0.35), color=GREY_A, stroke_width=1.6)
        group = VGroup(xax, yax, circ)
        if mark_minus:
            p = LEFT * r
            dot = Dot(p, radius=0.09, color=ORANGE)
            lab = MathTex(r"-1", font_size=22, color=ORANGE)
            lab.next_to(dot, LEFT, buff=0.12)
            group.add(dot, lab)
        if points:
            pts = [
                (RIGHT * r, r"1", YELLOW, DOWN),
                (UP * r, r"i", GREEN, RIGHT),
                (LEFT * r, r"-1", ORANGE, LEFT),
                (DOWN * r, r"-i", TEAL, DOWN),
            ]
            for i, (pos, name, col, side) in enumerate(pts):
                d = Dot(pos, radius=0.08, color=col)
                lab = MathTex(name, font_size=20, color=col)
                lab.next_to(d, side, buff=0.10)
                arr = Arrow(ORIGIN, pos, buff=0.08, color=col, stroke_width=2.8)
                group.add(arr, d, lab)
                if i == 1:
                    mark = RightAngle(
                        Line(ORIGIN, RIGHT * r),
                        Line(ORIGIN, UP * r),
                        length=0.22,
                        color=YELLOW,
                        stroke_width=2.4,
                    )
                    group.add(mark)
        if arc:
            a = Arc(radius=r, start_angle=0, angle=PI, color=TEAL, stroke_width=4.0)
            th = MathTex(r"\pi", font_size=22, color=TEAL)
            th.move_to(UP * (r * 0.55) + LEFT * 0.15)
            group.add(a, th)
        frame = Rectangle(width=(r + 0.7) * 2, height=(r + 0.55) * 2, stroke_opacity=0.0)
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
