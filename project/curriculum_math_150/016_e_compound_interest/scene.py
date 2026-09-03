from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import LessonScene


class CompoundInterestE(LessonScene):
    """#16 利息を細かくすると何に近づくか（約9分）"""

    def construct(self):
        self.header = self._open_header()
        self.part_question()
        self.part_trial_one_two()
        self.part_trial_explode()
        self.part_step1_formula()
        self.part_step2_expand()
        self.part_step3_cap()
        self.part_step4_limit()
        self.part_example()
        self.part_generalize()
        self.part_summary()

    def _open_header(self):
        title = self.ja_text("利息を細かくすると何に近づくか", font_size=36)
        self._fit(title, 13.2)
        title.set_x(0)
        self.play(FadeIn(title), run_time=0.8)
        self.pause_new_screen()
        self.linger(1.5)
        self.play(title.animate.scale(0.52).to_edge(UP, buff=0.16), run_time=0.5)
        title.set_x(0)
        return title

    def part_question(self):
        fig = self._note()
        cap = self.ja_text(
            "元本は 1 だとします。年利は 100 パーセントだとします。",
            font_size=18,
        )
        self._fit(cap, 13.0)
        pair = VGroup(fig, cap).arrange(DOWN, buff=0.28)
        pair.next_to(self.header, DOWN, buff=0.28)
        pair.set_x(0)
        self._nudge(pair)
        self.play(FadeIn(fig), FadeIn(cap), run_time=0.8)
        self.pause_new_screen()
        self.linger(cap.text)

        q1 = self.ja_text(
            "利息を、年に 1 回、2 回、12 回、毎日と細かく付けると、1 年後の金額はいくらになるでしょうか。",
            font_size=18,
        )
        self.stack_below(q1, pair, buff=0.20)
        q1.set_x(0)
        self._fit(q1, 13.0)
        q1.set_x(0)
        self.play(FadeIn(q1), run_time=0.7)
        self.linger(q1.text)

        q2 = self.ja_text(
            "無限に細かくしても、金額は爆発しないのでしょうか。",
            font_size=20,
        )
        self.stack_below(q2, q1, buff=0.14)
        q2.set_x(0)
        self.play(FadeIn(q2), run_time=0.7)
        self.linger(q2.text, extra=0.35)

    def part_trial_one_two(self):
        chip = self.begin_step("試行  1 回と 2 回", self.header)

        lead = self.ja_text(
            "まず、年に 1 回と 2 回だけ、最後まで計算します。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)
        self.play(FadeOut(lead), run_time=0.45)

        rows = [
            self._line(
                "年 1 回なら、1 年で利息が元本と同じだけ付きます。",
                MathTex(r"1+1=2", font_size=28, color=YELLOW),
                font_size=18,
            ),
            self._line(
                "年 2 回なら、半年ごとに利率は",
                MathTex(r"\dfrac{1}{2}", font_size=26, color=TEAL),
                "です。",
                font_size=18,
            ),
            self._line(
                "半年後は",
                MathTex(r"1+\dfrac{1}{2}=\dfrac{3}{2}", font_size=28, color=YELLOW),
                "です。",
                font_size=18,
            ),
            self._line(
                "さらに半年:",
                MathTex(r"\left(\dfrac{3}{2}\right)^{2}=\dfrac{9}{4}=2.25", font_size=28, color=GREEN),
                font_size=16,
            ),
        ]
        block = self._formula_rows(rows, chip, buff=0.18, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(block), run_time=0.45)

        table = self.aligned_table(
            [
                [
                    self.ja_text("付ける回数", font_size=16, color=GREY_B),
                    self.ja_text("1 年後", font_size=16, color=GREY_B),
                ],
                [MathTex(r"1", font_size=28), MathTex(r"2", font_size=28, color=YELLOW)],
                [
                    MathTex(r"2", font_size=28),
                    MathTex(r"\dfrac{9}{4}", font_size=28, color=GREEN),
                ],
            ],
            h_buff=0.40,
            v_buff=0.12,
        )
        table.scale(0.90)
        self.below_chip(table, chip, buff=0.18)
        table.set_x(0)
        self.play(FadeIn(table), run_time=0.7)
        self.pause_new_screen()

        notes = [
            self.ja_text("2 回に分けると、1 回より少し増えます。", font_size=18),
            self.ja_text(
                "細かくするほど、いくらでも増えていきそうに感じます。",
                font_size=18,
            ),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, table, buff=0.16)
            else:
                self.stack_below(mob, shown, buff=0.10)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            shown.add(mob)
            self.linger(mob.text)

    def part_trial_explode(self):
        chip = self.begin_step("試行  爆発？", self.header)

        lead = self.ja_text(
            "回数を 12 回、365 回まで増やして、爆発するかを見ます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)
        self.play(FadeOut(lead), run_time=0.45)

        rows = [
            self._line(
                "年 12 回:",
                MathTex(
                    r"\left(1+\dfrac{1}{12}\right)^{12}=\left(\dfrac{13}{12}\right)^{12}\approx 2.613",
                    font_size=26,
                    color=YELLOW,
                ),
                font_size=16,
            ),
            self._line(
                "年 365 回:",
                MathTex(
                    r"\left(1+\dfrac{1}{365}\right)^{365}\approx 2.715",
                    font_size=26,
                    color=TEAL,
                ),
                font_size=16,
            ),
            self.ja_text(
                "2 から 2.25 へは 0.25 増えた。12 回でも 2.613、毎日でも 2.715 で、増え方が鈍いです。",
                font_size=16,
            ),
        ]
        block = self._formula_rows(rows, chip, buff=0.16, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(block), run_time=0.45)

        chart = self._bar_chart(
            [2.0, 2.25, 2.613, 2.715],
            [r"1", r"2", r"12", r"365"],
            y_name="1 年後の金額",
            unit=0.85,
        )
        self.below_chip(chart, chip, buff=0.20)
        chart.set_x(0)
        self._nudge(chart)
        self._play_bars(chart)

        notes = [
            self.ja_text(
                "細かくしても、2.8 を超えて飛び跳ねてはいません。",
                font_size=18,
            ),
            self.ja_text(
                "無限に細かくすると爆発する、という予想は、この数字では支えられません。",
                font_size=18,
            ),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, chart, buff=0.16)
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

    def part_step1_formula(self):
        chip = self.begin_step("STEP 1  回数の式", self.header)

        lead = self.ja_text(
            "付ける回数を記号にして、同じ計算を一つの式にします。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        rows = [
            self._line(
                "1 年を",
                MathTex(r"n", font_size=26, color=YELLOW),
                "回に分けるとおく。",
                font_size=18,
            ),
            self._line(
                "1 回あたりの利率は",
                MathTex(r"\dfrac{1}{n}", font_size=28, color=TEAL),
                "です。",
                font_size=18,
            ),
            self._line(
                "1 年後の金額は",
                MathTex(r"\left(1+\dfrac{1}{n}\right)^{n}", font_size=32, color=YELLOW),
                "です。",
                font_size=18,
            ),
        ]
        block = self._formula_rows(rows, lead, buff=0.12, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(VGroup(lead, block)), run_time=0.45)

        back = [
            self._line(
                MathTex(r"n=1", font_size=26, color=YELLOW),
                ":",
                MathTex(r"(1+1)^{1}=2", font_size=28, color=YELLOW),
                font_size=18,
            ),
            self._line(
                MathTex(r"n=2", font_size=26, color=GREEN),
                ":",
                MathTex(r"\left(1+\dfrac{1}{2}\right)^{2}=\dfrac{9}{4}", font_size=28, color=GREEN),
                font_size=18,
            ),
        ]
        shown = self._formula_rows(back, chip, buff=0.18, hold=self.PAUSE_COMPLEX)

        notes = [
            self._line(
                "細かくする、とは、この",
                MathTex(r"n", font_size=24, color=YELLOW),
                "を大きくすることです。",
                font_size=18,
            ),
            self.ja_text(
                "爆発するかどうかは、この式の値がどこまで増えるかの問題です。",
                font_size=18,
            ),
        ]
        extra = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, shown, buff=0.14)
            else:
                self.stack_below(mob, extra, buff=0.10)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            extra.add(mob)
            self.linger(mob.text)

    def part_step2_expand(self):
        chip = self.begin_step("STEP 2  展開", self.header)

        lead = self.ja_text(
            "掛け算のままだと増え方が見えないので、展開して項に分けます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        restate = self._line(
            "1 年後の金額は",
            MathTex(r"\left(1+\dfrac{1}{n}\right)^{n}", font_size=26, color=YELLOW),
            "です。",
            font_size=18,
        )
        self.stack_below(restate, lead, buff=0.12)
        restate.set_x(0)
        self.play(FadeIn(restate), run_time=0.55)
        self.linger("1 年後の金額は (1+1/n)^n です。")
        self.play(FadeOut(lead), run_time=0.40)

        n2 = self._line(
            MathTex(r"n=2", font_size=24, color=GREEN),
            ":",
            MathTex(
                r"\left(1+\dfrac{1}{2}\right)^{2}=1+2\cdot\dfrac{1}{2}+1\cdot\dfrac{1}{4}=1+1+\dfrac{1}{4}=\dfrac{9}{4}",
                font_size=22,
                color=GREEN,
            ),
            font_size=16,
        )
        self._fit(n2, 13.0)
        block = self._formula_rows([n2], restate, buff=0.12, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(block), run_time=0.40)

        gen = [
            self._line(
                MathTex(
                    r"\left(1+\dfrac{1}{n}\right)^{n}=\displaystyle\sum_{k=0}^{n}\dbinom{n}{k}\left(\dfrac{1}{n}\right)^{k}",
                    font_size=26,
                    color=YELLOW,
                ),
                font_size=16,
            ),
            self._line(
                "最初の 3 項:",
                MathTex(
                    r"1+n\cdot\dfrac{1}{n}+\dfrac{n(n-1)}{2}\cdot\dfrac{1}{n^{2}}",
                    font_size=26,
                    color=ORANGE,
                ),
                font_size=16,
            ),
            self._line(
                MathTex(
                    r"=1+1+\dfrac{1-\dfrac{1}{n}}{2}",
                    font_size=30,
                    color=GREEN,
                ),
                font_size=16,
            ),
        ]
        shown = self._formula_rows(gen, restate, buff=0.10, hold=self.PAUSE_COMPLEX)

        notes = [
            self._line(
                "先頭の 2 項は、回数によらず",
                MathTex(r"1+1=2", font_size=26, color=YELLOW),
                "です。",
                font_size=18,
            ),
            self._line(
                "3 項目は",
                MathTex(r"\dfrac{1}{2}", font_size=26, color=TEAL),
                "より少し小さいです。",
                MathTex(r"n", font_size=24),
                "を増やすと",
                MathTex(r"\dfrac{1}{2}", font_size=26, color=TEAL),
                "に近づきます。",
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

    def part_step3_cap(self):
        chip = self.begin_step("STEP 3  頭打ち", self.header)

        lead = self.ja_text(
            "あとの項も、n を増やしても一定の数より大きくはなりません。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        rows = [
            self._line(
                MathTex(
                    r"\dfrac{n(n-1)(n-2)}{6}\cdot\dfrac{1}{n^{3}}=\dfrac{\left(1-\dfrac{1}{n}\right)\left(1-\dfrac{2}{n}\right)}{6}",
                    font_size=24,
                    color=YELLOW,
                ),
                font_size=16,
            ),
            self._line(
                MathTex(r"n", font_size=24),
                "が大きいと、これは",
                MathTex(r"\dfrac{1}{6}", font_size=26, color=TEAL),
                "に近づく。",
                MathTex(r"\dfrac{1}{6}", font_size=26, color=TEAL),
                "より大きい値にはなりません。",
                font_size=16,
            ),
        ]
        block = self._formula_rows(rows, lead, buff=0.12, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(VGroup(lead, block)), run_time=0.45)

        chart = self._term_bars()
        self.below_chip(chart, chip, buff=0.18)
        chart.set_x(0)
        self._nudge(chart)
        self._play_bars(chart)

        notes = [
            self.ja_text(
                "新しい項は階乗で割られるので、どんどん小さくなっていきます。",
                font_size=18,
            ),
            self.ja_text(
                "回数を増やしても、足し切った合計は、決まった高さより上へは行けません。",
                font_size=18,
            ),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, chart, buff=0.14)
            else:
                self.stack_below(mob, shown, buff=0.10)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            shown.add(mob)
            self.linger(mob.text)

    def part_step4_limit(self):
        chip = self.begin_step("STEP 4  極限", self.header)

        lead = self.ja_text(
            "回数を限りなく大きくしたときの値に、名前を付ける準備をします。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        rows = [
            self._line(
                MathTex(r"n\to\infty", font_size=26, color=YELLOW),
                "のとき、各項は",
                MathTex(r"\dfrac{1}{k!}", font_size=28, color=TEAL),
                "に近づきます。",
                font_size=18,
            ),
            self._line(
                "合計は",
                MathTex(
                    r"1+1+\dfrac{1}{2}+\dfrac{1}{6}+\dfrac{1}{24}+\cdots",
                    font_size=26,
                    color=GREEN,
                ),
                "に近づきます。",
                font_size=16,
            ),
            self._line(
                "この極限はおよそ",
                MathTex(r"2.718", font_size=30, color=YELLOW),
                "です。名前は次で残します。",
                font_size=18,
            ),
        ]
        shown = self._formula_rows(rows, lead, buff=0.12, hold=self.PAUSE_COMPLEX)

        notes = [
            self.ja_text(
                "無限に細かくしても、金額はおよそ 2.718 に近づくだけで、爆発しません。",
                font_size=18,
            ),
            self.ja_text(
                "増え方が鈍ったのは、あとの項が小さくなっていくからです。",
                font_size=18,
            ),
        ]
        extra = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, shown, buff=0.14)
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
            MathTex(r"n=3", font_size=26, color=YELLOW),
            "を、展開から合計まで通します。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger("n=3 を、展開から合計まで通します。")

        rows = [
            self._line(
                MathTex(
                    r"\left(1+\dfrac{1}{3}\right)^{3}=\left(\dfrac{4}{3}\right)^{3}=\dfrac{64}{27}",
                    font_size=28,
                    color=YELLOW,
                ),
                font_size=16,
            ),
            self._line(
                "展開:",
                MathTex(
                    r"1+3\cdot\dfrac{1}{3}+3\cdot\dfrac{1}{9}+1\cdot\dfrac{1}{27}=1+1+\dfrac{1}{3}+\dfrac{1}{27}",
                    font_size=22,
                    color=ORANGE,
                ),
                font_size=16,
            ),
            self._line(
                MathTex(
                    r"1+1+\dfrac{9}{27}+\dfrac{1}{27}=2+\dfrac{10}{27}=\dfrac{64}{27}",
                    font_size=26,
                    color=GREEN,
                ),
                font_size=16,
            ),
            self._line(
                "小数にすると",
                MathTex(r"\approx 2.370", font_size=26, color=TEAL),
                "です。",
                MathTex(r"2.25", font_size=24),
                "より増えているが、まだ",
                MathTex(r"2.718", font_size=24, color=YELLOW),
                "より小さいです。",
                font_size=16,
            ),
        ]
        block = self._formula_rows(rows, lead, buff=0.10, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(VGroup(lead, block)), run_time=0.45)

        table = self.aligned_table(
            [
                [
                    MathTex(r"n", font_size=22, color=GREY_B),
                    MathTex(r"\left(1+\dfrac{1}{n}\right)^{n}", font_size=22, color=GREY_B),
                ],
                [MathTex(r"1", font_size=26), MathTex(r"2", font_size=26, color=YELLOW)],
                [
                    MathTex(r"2", font_size=26),
                    MathTex(r"\dfrac{9}{4}", font_size=26, color=GREEN),
                ],
                [
                    MathTex(r"3", font_size=26),
                    MathTex(r"\dfrac{64}{27}", font_size=26, color=TEAL),
                ],
            ],
            h_buff=0.36,
            v_buff=0.10,
        )
        table.scale(0.88)
        self.below_chip(table, chip, buff=0.16)
        table.set_x(0)
        self.play(FadeIn(table), run_time=0.7)
        self.pause_new_screen()

        notes = [
            self.ja_text("3 回でも、まだ 2.718 までは届きません。", font_size=18),
            self.ja_text("届くのは、回数を限りなく増やした極限です。", font_size=18),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, table, buff=0.14)
            else:
                self.stack_below(mob, shown, buff=0.10)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            shown.add(mob)
            self.linger(mob.text)

    def part_generalize(self):
        chip = self.begin_step("一般化", self.header)

        lead = self._line(
            "今やったことは、連続複利の極限がネイピア数",
            MathTex(r"e", font_size=28, color=YELLOW),
            "である、という考え方でした。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger("今やったことは、連続複利の極限がネイピア数 e である、という考え方でした。")
        self.pause_conclusion()

        rows = [
            self._line(
                "回数",
                MathTex(r"n", font_size=24),
                "を大きくした 1 年後の金額を",
                MathTex(
                    r"\displaystyle\lim_{n\to\infty}\left(1+\dfrac{1}{n}\right)^{n}",
                    font_size=24,
                    color=YELLOW,
                ),
                "とおく。",
                font_size=16,
            ),
            self._line(
                "この極限を",
                MathTex(r"e", font_size=28, color=YELLOW),
                "とおく。",
                font_size=18,
            ),
            self._line(
                MathTex(
                    r"e=\displaystyle\lim_{n\to\infty}\left(1+\dfrac{1}{n}\right)^{n}",
                    font_size=30,
                    color=GREEN,
                ),
                font_size=16,
            ),
            self._line(
                "同じ数は",
                MathTex(
                    r"e=1+1+\dfrac{1}{2!}+\dfrac{1}{3!}+\dfrac{1}{4!}+\cdots",
                    font_size=24,
                    color=TEAL,
                ),
                "でも書けます。",
                font_size=16,
            ),
        ]
        block = self._formula_rows(rows, lead, buff=0.10, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(VGroup(lead, block)), run_time=0.45)

        why = [
            self._line(
                MathTex(r"y=e^{x}", font_size=26, color=YELLOW),
                "は、増える速さがいまの値と同じ、つまり",
                MathTex(r"y'=y", font_size=26, color=GREEN),
                "を満たします。",
                font_size=16,
            ),
            self.ja_text(
                "底が 10 や 2 だと、その比例定数が 1 になりません。",
                font_size=18,
            ),
            self.ja_text(
                "細かく付ける方法を、極限で一気に見る、というやり方です。",
                font_size=18,
            ),
            self._line(
                "細かくしても爆発しないのは、",
                MathTex(r"e", font_size=26, color=YELLOW),
                "が有限の数だからです。",
                font_size=18,
            ),
            self._line(
                "元本 1、年利 100 パーセントを連続で付けると、1 年後はちょうど",
                MathTex(r"e", font_size=26, color=YELLOW),
                "です。",
                font_size=16,
            ),
        ]
        self._formula_rows(why, chip, buff=0.16, hold=self.PAUSE_CONCLUSION)

    def part_summary(self):
        chip = self.begin_step("まとめ", self.header)

        rows = [
            self._line(
                "年 1 回なら 1 年後は",
                MathTex(r"2", font_size=26, color=YELLOW),
                "。2 回なら",
                MathTex(r"\dfrac{9}{4}", font_size=26, color=GREEN),
                font_size=18,
            ),
            self._line(
                "回数",
                MathTex(r"n", font_size=24),
                "のとき、1 年後は",
                MathTex(r"\left(1+\dfrac{1}{n}\right)^{n}", font_size=26, color=YELLOW),
                font_size=16,
            ),
            self._line(
                "展開すると先頭はいつも",
                MathTex(r"1+1", font_size=24, color=ORANGE),
                "。あとの項は小さくなっていきます",
                font_size=16,
            ),
            self._line(
                "極限",
                MathTex(
                    r"\displaystyle\lim_{n\to\infty}\left(1+\dfrac{1}{n}\right)^{n}",
                    font_size=22,
                    color=GREEN,
                ),
                "を",
                MathTex(r"e", font_size=26, color=YELLOW),
                "とおく。細かくしても爆発しません",
                font_size=16,
            ),
            self._line(
                "連続複利なら、1 年後はちょうど",
                MathTex(r"e", font_size=26, color=YELLOW),
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
            self.linger(mob.text if hasattr(mob, "text") else 2.0)
            if i == 3:
                self.pause_conclusion()

    def _note(self):
        body = RoundedRectangle(
            width=2.2,
            height=1.35,
            corner_radius=0.12,
            color=GOLD,
            stroke_width=2.4,
        )
        body.set_fill("#3A3220", 0.95)
        lab = MathTex(r"1", font_size=44, color=GOLD)
        tag = self.ja_text("元本", font_size=18, color=GREY_B)
        tag.next_to(body, UP, buff=0.10)
        inner = VGroup(body, lab)
        lab.move_to(body.get_center())
        rate = self.ja_text("年利 100%", font_size=16, color=TEAL)
        rate.next_to(body, DOWN, buff=0.12)
        return VGroup(tag, inner, rate)

    def _term_bars(self):
        return self._bar_chart(
            [1, 1, 0.5, 1 / 6, 1 / 24],
            [r"1", r"1", r"1/2", r"1/6", r"1/24"],
            y_name="項の大きさ",
            unit=1.35,
            bar_w=0.70,
            colors=[YELLOW, YELLOW, ORANGE, TEAL, GREEN],
        )

    def _bar_chart(
        self,
        heights,
        labels,
        y_name="1 年後の金額",
        color=BLUE_B,
        colors=None,
        unit=0.85,
        bar_w=0.70,
        gap=0.18,
        label_size=16,
    ):
        n = len(heights)
        if colors is None:
            colors = [color] * n
        bars = VGroup()
        labs = VGroup()
        stride = bar_w + gap
        width = n * bar_w + (n - 1) * gap
        x0 = -width / 2 + bar_w / 2
        y0 = 0.0
        label_y = y0 - 0.32
        max_h = max(heights) if heights else 1
        axis_h = max(max_h, 1.05) * unit
        for i, (h, text) in enumerate(zip(heights, labels)):
            col = colors[i]
            height = max(h * unit, 0.08)
            bar = Rectangle(width=bar_w, height=height, color=col, stroke_width=1.2)
            bar.set_fill(col, 0.85)
            x = x0 + i * stride
            bar.move_to([x, y0 + height / 2, 0])
            lab = MathTex(rf"{text}", font_size=label_size)
            lab.move_to([x, label_y, 0])
            bars.add(bar)
            labs.add(lab)
        left = bars[0].get_left()[0] - 0.14
        right = bars[-1].get_right()[0] + 0.12
        baseline = Line([left, y0, 0], [right, y0, 0], color=GREY_B, stroke_width=1.6)
        y_axis = Line([left, y0, 0], [left, y0 + axis_h + 0.08, 0], color=GREY_B, stroke_width=1.6)
        ticks = VGroup()
        if max_h <= 1.05:
            tick_vals = [0.5, 1]
        else:
            tick_vals = [1, 2, 3]
        for val in tick_vals:
            ty = y0 + val * unit
            if ty > y0 + axis_h + 0.05:
                continue
            tick = Line([left - 0.07, ty, 0], [left, ty, 0], color=GREY_B, stroke_width=1.4)
            tlab = MathTex(rf"{val}", font_size=14, color=GREY_B)
            tlab.next_to(tick, LEFT, buff=0.06)
            ticks.add(VGroup(tick, tlab))
        name = self.ja_text(y_name, font_size=14, color=GREY_B)
        name.next_to(y_axis, UP, buff=0.08)
        name.align_to(y_axis, LEFT)
        chart = VGroup(baseline, y_axis, ticks, name, bars, labs)
        chart.bars = bars
        chart.labels = labs
        chart.baseline = baseline
        chart.y_axis = VGroup(y_axis, ticks, name)
        return chart

    def _play_bars(self, chart):
        self.add(chart.baseline, chart.y_axis)
        self.play(
            LaggedStart(
                *[GrowFromEdge(bar, DOWN) for bar in chart.bars],
                lag_ratio=0.10,
            ),
            FadeIn(chart.labels),
            run_time=1.35,
        )
        self.pause_new_screen()

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
