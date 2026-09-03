from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import LessonScene


class BirthdayParadox(LessonScene):
    """#9 何人集まると誕生日がぶつかるか（約8分）"""

    DOT_COLORS = [GOLD, ORANGE, TEAL, BLUE_B, GREEN, PURPLE]

    def construct(self):
        self.header = self._open_header()
        self.part_question()
        self.part_trial_half()
        self.part_trial_self()
        self.part_step1_complement()
        self.part_step2_product()
        self.part_step3_small()
        self.part_step4_approx()
        self.part_example()
        self.part_generalize()
        self.part_summary()

    def _open_header(self):
        title = self.ja_text("何人集まると誕生日がぶつかるか", font_size=36)
        self.play(FadeIn(title), run_time=0.8)
        self.linger(1.2)
        self.play(title.animate.scale(0.52).to_edge(UP, buff=0.16), run_time=0.5)
        title.set_x(0)
        return title

    def part_question(self):
        fig = self._people_graph(6, mode="plain")
        cap = self._line(
            "1 年を",
            MathTex(r"365", font_size=24),
            "日とおく。うるう年の 2 月 29 日は数えない。",
            font_size=18,
        )
        pair = VGroup(fig, cap).arrange(RIGHT, buff=0.40, aligned_edge=UP)
        pair.next_to(self.header, DOWN, buff=0.30)
        pair.set_x(0)
        self._nudge(pair)
        self.play(FadeIn(fig), FadeIn(cap), run_time=0.8)
        self.linger(3.2)

        q1 = self.ja_text(
            "同じ誕生日の 2 人が出る確率が、半分を超えるのは何人でしょう。",
            font_size=24,
        )
        q1.next_to(pair, DOWN, buff=0.26)
        q1.set_x(0)
        self._fit(q1, 13.0)
        q1.set_x(0)
        self.play(FadeIn(q1), run_time=0.45)
        self.linger(q1.text)

        q2 = self.ja_text("一年の半分、183 人では、なぜ大きすぎるのでしょうか。", font_size=24)
        self.stack_below(q2, q1, buff=0.14)
        q2.set_x(0)
        self._fit(q2, 13.0)
        q2.set_x(0)
        self.play(FadeIn(q2), run_time=0.45)
        self.linger(q2.text, extra=0.35)

    def part_trial_half(self):
        self.wipe(self.header)
        chip = self.step_label("試行  半分")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("まず、一年の半分の人数で見てみます。", font_size=22)
        self.below_chip(lead, chip, buff=0.18)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        rows = [
            self._line("1 年を", MathTex(r"365", font_size=26), "日とおく。", font_size=20),
            MathTex(r"\dfrac{365}{2}=182.5", font_size=34, color=YELLOW),
            self.ja_text("近い整数は 183 人です。", font_size=22),
        ]
        self._formula_rows(rows, lead, buff=0.16)

        table = self.aligned_table(
            [
                [
                    self.ja_text("考え方", font_size=16, color=GREY_B),
                    self.ja_text("人数", font_size=16, color=GREY_B),
                ],
                [
                    self.ja_text("日を半分埋める", font_size=20),
                    MathTex(r"183", font_size=28, color=YELLOW),
                ],
            ],
            h_buff=0.40,
            v_buff=0.12,
        )
        table.scale(0.90)
        self.play(FadeOut(VGroup(*rows)), run_time=0.3)
        self.stack_below(table, lead, buff=0.16)
        table.set_x(0)
        self.reveal_table(table, row_wait=0.70)

        notes = [
            self.ja_text("日が半分埋まれば、同じ日が出そうだ、と思ってしまいます。", font_size=20),
            self.ja_text("でも欲しいのは、日が半分埋まることではなく、どれか 2 人が同じ日を持つことです。", font_size=20),
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
            self.play(FadeIn(mob), run_time=0.4)
            shown.add(mob)
            self.linger(3.2)

    def part_trial_self(self):
        self.wipe(self.header)
        chip = self.step_label("試行  自分だけ")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("こんどは、自分の誕生日に誰かが一致するか、だけを数えてみます。", font_size=20)
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        fig = self._people_graph(6, mode="star")
        right = VGroup(
            self.ja_text("自分と他の人の組は、6 人なら 5 本です。", font_size=18),
            MathTex(r"6-1=5", font_size=30, color=YELLOW),
        ).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        pair = VGroup(fig, right).arrange(RIGHT, buff=0.40, aligned_edge=UP)
        self.stack_below(pair, lead, buff=0.12)
        pair.set_x(0)
        self._nudge(pair)
        self.play(FadeIn(fig), FadeIn(right), run_time=0.65)
        self.linger(3.4)

        complete = self._people_graph(6, mode="complete")
        complete.move_to(fig)
        new_right = VGroup(
            self._line("全てのペアは", MathTex(r"\dfrac{n(n-1)}{2}", font_size=26), font_size=18),
            MathTex(r"n=6:\quad \dfrac{6\cdot 5}{2}=15", font_size=30, color=GREEN),
        ).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        new_right.next_to(complete, RIGHT, buff=0.40, aligned_edge=UP)
        self._nudge(VGroup(complete, new_right))
        self.play(FadeOut(fig), FadeIn(complete), FadeOut(right), FadeIn(new_right), run_time=0.65)
        fig = complete
        right = new_right
        self.linger(3.4)

        self.play(FadeOut(VGroup(fig, right)), run_time=0.3)
        table = self.aligned_table(
            [
                [
                    self.ja_text("数え方", font_size=16, color=GREY_B),
                    self.ja_text("6 人の組", font_size=16, color=GREY_B),
                ],
                [
                    self.ja_text("自分だけ", font_size=20),
                    MathTex(r"5", font_size=26),
                ],
                [
                    self.ja_text("全てのペア", font_size=20),
                    MathTex(r"15", font_size=26, color=GREEN),
                ],
            ],
            h_buff=0.36,
            v_buff=0.10,
        )
        table.scale(0.88)
        self.stack_below(table, lead, buff=0.12)
        table.set_x(0)
        self.reveal_table(table, row_wait=0.65)

        notes = [
            self.ja_text("自分だけの組は、全体の一部です。ぶつかりやすさを過小に見ます。", font_size=20),
            self.ja_text("全てのペアは、人数より速く増えます。6 人で 15 組です。", font_size=20),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, table, buff=0.12)
            else:
                self.stack_below(mob, shown, buff=0.08)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.4)
            shown.add(mob)
            self.linger(3.2)

        self.play(FadeOut(VGroup(table, shown)), run_time=0.3)
        grow = [
            self._line(MathTex(r"\dfrac{n(n-1)}{2}", font_size=26), "を、組の個数とおく。", font_size=20),
            MathTex(r"n=10:\quad \dfrac{10\cdot 9}{2}=45", font_size=28),
            MathTex(r"183\cdot 180=32940,\quad 183\cdot 2=366", font_size=26),
            MathTex(r"183\cdot 182=33306,\quad \dfrac{33306}{2}=16653", font_size=26, color=YELLOW),
        ]
        block = self._formula_rows(grow, lead, buff=0.12)
        close = self.ja_text(
            "183 人なら組は 16653 です。日は 365 しかないので、半分を埋める人数は組の多さを見落としています。",
            font_size=18,
        )
        self.stack_below(close, block, buff=0.12)
        close.set_x(0)
        self._fit(close, 13.0)
        close.set_x(0)
        self.play(FadeIn(close), run_time=0.4)
        self.linger(close.text, extra=0.30)

    def part_step1_complement(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 1  余事象")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("同じ日の 2 人が出る、を正面から数えるのは大変です。出ないほうから書きます。", font_size=20)
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        defs = [
            self._line(MathTex(r"d", font_size=26, color=YELLOW), "を、1 年の日数とおく。いま", MathTex(r"d=365", font_size=26), font_size=20),
            self._line(MathTex(r"n", font_size=26, color=ORANGE), "を、集まる人数とおく。", font_size=20),
            self.ja_text("誕生日は独立で、どの日も同じ確からしさ、とおく。", font_size=20),
            self._line(MathTex(r"A", font_size=26, color=TEAL), "を、同じ誕生日の 2 人が少なくとも 1 組いること、とおく。", font_size=18),
            self.ja_text("A の余事象を、全員の誕生日が違うこと、とおく。", font_size=20),
            self._line(
                MathTex(r"P(A)", font_size=30, color=TEAL),
                "=",
                MathTex(r"1", font_size=30),
                "−（全員違う確率）",
                font_size=22,
            ),
        ]
        block = self._formula_rows(defs, lead, buff=0.12)
        self.linger(3.4)
        self.play(FadeOut(block), run_time=0.3)

        notes = [
            self.ja_text("全員違う確率が分かれば、ぶつかる確率が分かります。", font_size=20),
            self.ja_text("必ずぶつかる人数ではなく、半分を超える人数を求めます。", font_size=20),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, lead, buff=0.16)
            else:
                self.stack_below(mob, shown, buff=0.10)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.4)
            shown.add(mob)
            self.linger(3.2)

    def part_step2_product(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 2  積")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("全員違う確率を、1 人ずつ足しながら掛ける方法で書きます。", font_size=22)
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        restate = self._line(
            MathTex(r"d=365", font_size=24, color=YELLOW),
            "、",
            MathTex(r"n", font_size=24, color=ORANGE),
            "を人数とおく。",
            font_size=20,
        )
        self.stack_below(restate, lead, buff=0.10)
        restate.set_x(0)
        self.play(FadeIn(restate), run_time=0.4)
        self.linger(3.2)

        steps = [
            self._line("1 人目。どの日でもよい。", MathTex(r"\dfrac{365}{365}", font_size=26), font_size=18),
            self._line("2 人目。1 人目と違う日。", MathTex(r"\dfrac{364}{365}", font_size=26), font_size=18),
            self._line("3 人目。先の 2 人と違う日。", MathTex(r"\dfrac{363}{365}", font_size=26), font_size=18),
            self._line(
                MathTex(r"n", font_size=22, color=ORANGE),
                "人目。先の",
                MathTex(r"n-1", font_size=22),
                "人と違う日。",
                MathTex(r"\dfrac{365-n+1}{365}", font_size=26),
                font_size=18,
            ),
        ]
        block = self._formula_rows(steps, restate, buff=0.10)
        self.play(FadeOut(block), run_time=0.3)

        prod = [
            MathTex(
                r"\dfrac{365}{365}\cdot\dfrac{364}{365}\cdot\dfrac{363}{365}\cdots\dfrac{365-n+1}{365}",
                font_size=28,
            ),
            self._line("ぶつかる確率は", MathTex(r"P(A)=1-\dfrac{d(d-1)\cdots(d-n+1)}{d^{n}}", font_size=28, color=YELLOW), font_size=18),
        ]
        block2 = self._formula_rows(prod, restate, buff=0.16)
        note = self.ja_text("この積を、小さい暦で最後まで計算してみます。", font_size=20)
        self.stack_below(note, block2, buff=0.16)
        note.set_x(0)
        self._fit(note, 13.0)
        note.set_x(0)
        self.play(FadeIn(note), run_time=0.4)
        self.linger(note.text)

    def part_step3_small(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 3  小さい暦")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("日が 10 日しかない暦で、人数を 1 人ずつ足します。", font_size=22)
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        first = [
            self._line(MathTex(r"d=10", font_size=26, color=YELLOW), "とおく。", font_size=20),
            MathTex(r"n=2:\quad \dfrac{10}{10}\cdot\dfrac{9}{10}=\dfrac{9}{10}", font_size=28),
            MathTex(r"P(A)=1-\dfrac{9}{10}=\dfrac{1}{10}", font_size=28, color=YELLOW),
            MathTex(r"n=3:\quad \dfrac{10\cdot 9\cdot 8}{10^{3}}=\dfrac{720}{1000}=0.72", font_size=26),
            MathTex(r"P(A)=1-0.72=0.28", font_size=28),
        ]
        block = self._formula_rows(first, lead, buff=0.10)
        self.play(FadeOut(block), run_time=0.3)

        second = [
            MathTex(r"n=4:\quad \dfrac{10\cdot 9\cdot 8\cdot 7}{10^{4}}=\dfrac{5040}{10000}=0.504", font_size=26),
            MathTex(r"P(A)=1-0.504=0.496", font_size=28, color=YELLOW),
            MathTex(r"n=5:\quad 0.504\times\dfrac{6}{10}=0.3024", font_size=26),
            MathTex(r"P(A)=1-0.3024=0.6976", font_size=28, color=GREEN),
        ]
        block2 = self._formula_rows(second, lead, buff=0.10)
        self.play(FadeOut(block2), run_time=0.3)

        table = self.aligned_table(
            [
                [
                    MathTex(r"n", font_size=22, color=ORANGE),
                    self.ja_text("全員違う", font_size=16, color=GREY_B),
                    self.ja_text("ぶつかる", font_size=16, color=GREY_B),
                ],
                [MathTex(r"2", font_size=24), MathTex(r"0.900", font_size=24), MathTex(r"0.100", font_size=24)],
                [MathTex(r"3", font_size=24), MathTex(r"0.720", font_size=24), MathTex(r"0.280", font_size=24)],
                [MathTex(r"4", font_size=24), MathTex(r"0.504", font_size=24), MathTex(r"0.496", font_size=24, color=YELLOW)],
                [MathTex(r"5", font_size=24), MathTex(r"0.302", font_size=24), MathTex(r"0.698", font_size=24, color=GREEN)],
            ],
            h_buff=0.32,
            v_buff=0.08,
        )
        table.scale(0.82)
        self.stack_below(table, lead, buff=0.12)
        table.set_x(0)
        self.reveal_table(table, row_wait=0.62)

        notes = [
            self.ja_text("10 日の暦なら、4 人でほぼ半分です。", font_size=20),
            self.ja_text("365 日でも、半分の 183 人よりずっと手前で半分を超えそうです。", font_size=20),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, table, buff=0.12)
            else:
                self.stack_below(mob, shown, buff=0.08)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.4)
            shown.add(mob)
            self.linger(3.2)

    def part_step4_approx(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 4  近似")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self._line(
            "積を、指数関数でまとめます。高校の",
            MathTex(r"\left(1-\dfrac{1}{m}\right)^{m}\approx\dfrac{1}{e}", font_size=24),
            "から入ります。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.14)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(3.2)

        first = [
            self._line(MathTex(r"d", font_size=22, color=YELLOW), "を日数、", MathTex(r"n", font_size=22, color=ORANGE), "を人数とおく。", font_size=18),
            self._line(MathTex(r"m", font_size=24), "を大きい正の整数とおく。", MathTex(r"\left(1-\dfrac{1}{m}\right)^{m}\approx\dfrac{1}{e}", font_size=24), font_size=18),
            MathTex(r"x=\dfrac{1}{m}\quad\Rightarrow\quad (1-x)^{1/x}\approx\dfrac{1}{e}", font_size=26),
            MathTex(r"1-x\approx e^{-x}", font_size=30, color=YELLOW),
            MathTex(r"1-\dfrac{k}{d}\approx e^{-k/d}", font_size=28),
        ]
        block = self._formula_rows(first, lead, buff=0.10)
        self.play(FadeOut(block), run_time=0.3)

        second = [
            MathTex(
                r"\prod_{k=1}^{n-1}\left(1-\dfrac{k}{d}\right)\approx \exp\left(-\dfrac{1+\cdots+(n-1)}{d}\right)",
                font_size=24,
            ),
            MathTex(r"1+2+\cdots+(n-1)=\dfrac{(n-1)n}{2}", font_size=28),
            MathTex(r"P(A)\approx 1-e^{-n(n-1)/(2d)}", font_size=32, color=YELLOW),
        ]
        block2 = self._formula_rows(second, lead, buff=0.10)
        self.linger(3.4)
        self.play(FadeOut(block2), run_time=0.3)

        third = [
            MathTex(r"1-e^{-n(n-1)/(2d)}=\dfrac{1}{2}", font_size=28),
            MathTex(r"e^{-n(n-1)/(2d)}=\dfrac{1}{2}\quad\Rightarrow\quad \dfrac{n(n-1)}{2d}=\ln 2", font_size=24),
            MathTex(r"n(n-1)=2d\ln 2", font_size=30),
            self._line(MathTex(r"n", font_size=22), "が大きいとき", MathTex(r"n(n-1)\approx n^{2}", font_size=26), font_size=18),
            MathTex(r"n\approx\sqrt{2d\ln 2}", font_size=34, color=YELLOW),
        ]
        block3 = self._formula_rows(third, lead, buff=0.10)
        self.play(FadeOut(block3), run_time=0.3)

        nums = [
            MathTex(r"\ln 2\approx 0.693,\quad e^{\ln 2}=2", font_size=26),
            MathTex(r"d=365:\quad 2\cdot 365=730", font_size=28),
            MathTex(r"730\cdot 0.693=505.89", font_size=28),
            MathTex(r"22^{2}=484,\quad 23^{2}=529,\quad 22.5^{2}=506.25", font_size=26, color=GREEN),
            self._line("だから", MathTex(r"n\approx 22.5", font_size=26, color=YELLOW), "。整数なら 23 人を当たります。", font_size=20),
        ]
        block4 = self._formula_rows(nums, lead, buff=0.10)
        close = self.ja_text("一年の半分 183 ではなく、日数の平方根のくらいです。", font_size=20)
        self.play(FadeOut(block4), run_time=0.3)
        self.stack_below(close, lead, buff=0.16)
        close.set_x(0)
        self._fit(close, 13.0)
        close.set_x(0)
        self.play(FadeIn(close), run_time=0.4)
        self.linger(close.text)

    def part_example(self):
        self.wipe(self.header)
        chip = self.step_label("実例")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("365 日で、22 人と 23 人を最後まで代入します。", font_size=22)
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        first = [
            self._line(MathTex(r"d=365", font_size=24, color=YELLOW), "、", MathTex(r"P(A)\approx 1-e^{-n(n-1)/(2d)}", font_size=24), "とおく。", font_size=18),
            MathTex(r"n=22:\quad 22\cdot 21=462,\quad 2\cdot 365=730", font_size=26),
            MathTex(r"1-e^{-462/730}\approx 0.469", font_size=30, color=YELLOW),
            self.ja_text("22 人は半分未満。", font_size=20),
        ]
        block = self._formula_rows(first, lead, buff=0.10)
        self.play(FadeOut(block), run_time=0.3)

        second = [
            MathTex(r"n=23:\quad 23\cdot 22=506", font_size=28),
            MathTex(r"1-e^{-506/730}\approx 0.500", font_size=32, color=GREEN),
            self.ja_text("23 人で半分を超えます。", font_size=20),
        ]
        block2 = self._formula_rows(second, lead, buff=0.12)
        self.play(FadeOut(block2), run_time=0.3)

        table = self.aligned_table(
            [
                [
                    MathTex(r"n", font_size=22, color=ORANGE),
                    self.ja_text("ぶつかる確率", font_size=16, color=GREY_B),
                ],
                [MathTex(r"10", font_size=24), MathTex(r"0.117", font_size=24)],
                [MathTex(r"20", font_size=24), MathTex(r"0.411", font_size=24)],
                [MathTex(r"22", font_size=24), MathTex(r"0.476", font_size=24)],
                [MathTex(r"23", font_size=24), MathTex(r"0.507", font_size=24, color=GREEN)],
                [MathTex(r"30", font_size=24), MathTex(r"0.706", font_size=24)],
                [MathTex(r"183", font_size=24), MathTex(r"1.000", font_size=24, color=YELLOW)],
            ],
            h_buff=0.36,
            v_buff=0.08,
        )
        table.scale(0.78)
        self.stack_below(table, lead, buff=0.12)
        table.set_x(0)
        self.reveal_table(table, row_wait=0.58)

        notes = [
            self.ja_text("22 人では半分未満。23 人で半分を超えます。", font_size=20),
            self.ja_text("183 人は、半分を超える人数としては大きすぎます。", font_size=20),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, table, buff=0.12)
            else:
                self.stack_below(mob, shown, buff=0.08)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.4)
            shown.add(mob)
            self.linger(3.2)

    def part_generalize(self):
        self.wipe(self.header)
        chip = self.step_label("一般化")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("今やったことは、全てのペアを余事象の積で数え、指数関数でまとめる考え方でした。", font_size=18)
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        first = [
            self._line(MathTex(r"d", font_size=22, color=YELLOW), "を箱の個数、", MathTex(r"n", font_size=22, color=ORANGE), "を独立に入る物の個数とおく。", font_size=18),
            self.ja_text("ぶつかるとは、どれかの箱に 2 個以上入ること、とおく。", font_size=18),
            self.ja_text("誕生日のパラドックスと呼ばれます。直感より少ない人数で、衝突の確率が半分を超えます。", font_size=18),
            MathTex(r"P\approx 1-e^{-n(n-1)/(2d)}\approx 1-e^{-n^{2}/(2d)}", font_size=26, color=YELLOW),
            MathTex(r"n\approx\sqrt{2d\ln 2}", font_size=32, color=GREEN),
        ]
        block = self._formula_rows(first, lead, buff=0.10)
        self.linger(3.4)
        self.play(FadeOut(VGroup(lead, block)), run_time=0.3)

        name = self.ja_text("必ずぶつかる人数との差", font_size=20, color=GREY_B)
        self.below_chip(name, chip, buff=0.16)
        self.play(FadeIn(name), run_time=0.35)
        self.linger(name.text)

        close = [
            self._line("全員違うには、箱が人数以上いります。必ずぶつかるのは", MathTex(r"d+1", font_size=24), "人。", font_size=18),
            self._line("半分を超える人数は、その平方根のくらい、", MathTex(r"\sqrt{d}", font_size=26, color=YELLOW), "まで下がります。", font_size=18),
            self.ja_text("各物は d 個の箱のどれかへ、独立に同じ確からしさで入ります。", font_size=18, color=GREY_B),
        ]
        self._formula_rows(close, name, buff=0.12)

    def part_summary(self):
        self.wipe(self.header)
        chip = self.step_label("まとめ")
        self.play(FadeIn(chip), run_time=0.35)

        rows = [
            self.ja_text("183 人は、日を半分埋める人数", font_size=22),
            self.ja_text("自分と誰かが同じ、だけだと組を過小に数える", font_size=22),
            self._line("全てのペアは", MathTex(r"\dfrac{n(n-1)}{2}", font_size=24, color=YELLOW), "で、人数より速く増える", font_size=20),
            self._line("余事象の積をまとめると", MathTex(r"1-e^{-n(n-1)/(2d)}", font_size=24, color=YELLOW), font_size=20),
            self._line(
                "半分を超えるのは",
                MathTex(r"n\approx\sqrt{2d\ln 2}", font_size=24, color=GREEN),
                "。365 日なら 23 人",
                font_size=20,
            ),
        ]
        shown = VGroup()
        for i, mob in enumerate(rows):
            if i == 0:
                self.below_chip(mob, chip, buff=0.24)
            else:
                self.stack_below(mob, shown, buff=0.14)
            self._fit_left(mob)
            self.play(FadeIn(mob), run_time=0.45)
            shown.add(mob)
            self.linger(3.2)

        trivia = self._line(
            "箱が",
            MathTex(r"10000", font_size=20, color=GREY_B),
            "個のハッシュでも、およそ",
            MathTex(r"120", font_size=20, color=GREY_B),
            "個で衝突の確率が半分を超えます。",
            font_size=18,
            color=GREY_B,
        )
        self.stack_below(trivia, shown, buff=0.22)
        self._fit_left(trivia)
        self.play(FadeIn(trivia), run_time=0.45)
        self.linger(
            "箱が 1 万個のハッシュでも、およそ 120 個で衝突の確率が半分を超えます。",
            extra=0.40,
        )

    def _people_graph(self, n, mode="plain", radius=1.35):
        pts = []
        dots = VGroup()
        for i in range(n):
            ang = PI / 2 + i * TAU / n
            p = radius * np.array([np.cos(ang), np.sin(ang), 0.0])
            pts.append(p)
            color = GOLD if (mode == "star" and i == 0) else self.DOT_COLORS[i % len(self.DOT_COLORS)]
            dots.add(Dot(p, radius=0.12, color=color))
        lines = VGroup()
        if mode == "star":
            for j in range(1, n):
                lines.add(Line(pts[0], pts[j], color=GOLD, stroke_width=3.0))
        elif mode == "complete":
            for i in range(n):
                for j in range(i + 1, n):
                    lines.add(Line(pts[i], pts[j], color=GREY_B, stroke_width=1.6))
        frame = Circle(radius=radius + 0.28, color=GREY_E, stroke_width=1.0)
        return VGroup(frame, lines, dots)

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

    def _formula_rows(self, rows, under, buff=0.36):
        block = VGroup(*rows).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        self.stack_below(block, under, buff=buff)
        block.set_x(0)
        self._fit(block, 12.6)
        block.set_x(0)
        for row in block:
            self.play(FadeIn(row), run_time=0.45)
            self.linger(3.2)
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
