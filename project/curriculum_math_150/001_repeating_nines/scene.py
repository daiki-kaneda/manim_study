from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import LessonScene


class RepeatingNines(LessonScene):
    """#1 0.999… は 1 か（約7分）"""

    def construct(self):
        self.header = self._open_header()
        self.part_question()
        self.part_trial_finite()
        self.part_trial_third()
        self.part_step1_gap()
        self.part_step2_bar()
        self.part_step3_tenx()
        self.part_step4_series()
        self.part_example()
        self.part_generalize()
        self.part_summary()

    def _open_header(self):
        title = self.ja_text("0.999… は 1 か", font_size=42)
        self.play(FadeIn(title), run_time=0.8)
        self.linger(1.2)
        self.play(title.animate.scale(0.55).to_edge(UP, buff=0.16), run_time=0.5)
        return title

    def part_question(self):
        digits = VGroup(
            MathTex(r"0", font_size=52, color=BLUE),
            MathTex(r".", font_size=52, color=BLUE),
            MathTex(r"9", font_size=52, color=BLUE),
            MathTex(r"9", font_size=52, color=BLUE),
            MathTex(r"9", font_size=52, color=BLUE),
            MathTex(r"\ldots", font_size=52, color=BLUE),
        )
        digits.arrange(RIGHT, buff=0.08)
        left_box = RoundedRectangle(
            width=4.4,
            height=2.0,
            corner_radius=0.14,
            color=BLUE,
            stroke_width=3,
            fill_color=BLUE,
            fill_opacity=0.16,
        )
        digits.move_to(left_box)
        left = VGroup(left_box, digits)
        right = self._value_card(r"1", GREEN)
        cards = VGroup(left, right).arrange(RIGHT, buff=1.1)
        cards.next_to(self.header, DOWN, buff=0.7)
        cards.set_x(0)

        self.play(FadeIn(left_box), FadeIn(digits[0]), FadeIn(digits[1]), FadeIn(right), run_time=0.7)
        for d in digits[2:]:
            self.play(FadeIn(d, shift=UP * 0.12), run_time=0.35)
            self.linger(0.7)
        self.linger(1.0)

        q1 = self.ja_text("この二つの書き方は、同じ数でしょうか。", font_size=28)
        q1.next_to(cards, DOWN, buff=0.45)
        q1.set_x(0)
        self.play(FadeIn(q1), run_time=0.5)
        self.linger(q1.text)

        q2 = self.ja_text("それとも、左のほうが、ほんの少し小さいでしょうか。", font_size=28)
        self.stack_below(q2, q1, buff=0.28)
        q2.set_x(0)
        self.play(FadeIn(q2), run_time=0.5)
        self.linger(q2.text, extra=0.35)

    def part_trial_finite(self):
        self.wipe(self.header)
        chip = self.step_label("試行  有限の 9")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("まず、9 を有限個だけ書いて、1 から引いてみます。", font_size=26)
        self.below_chip(lead, chip, buff=0.32)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.5)
        self.linger(lead.text)

        sub = self.ja_text("無限はいったん置いて、途中で止めた数だけを見ます。", font_size=26)
        self.stack_below(sub, lead, buff=0.18)
        self._fit_left(sub)
        self.play(FadeIn(sub), run_time=0.45)
        self.linger(sub.text)

        subtractions = [
            r"1.0-0.9=0.1",
            r"1.00-0.99=0.01",
            r"1.000-0.999=0.001",
            r"1.0000-0.9999=0.0001",
        ]
        shown = None
        for tex in subtractions:
            row = MathTex(tex, font_size=36)
            if shown is None:
                self.stack_below(row, sub, buff=0.28)
                row.set_x(0)
                self.play(FadeIn(row), run_time=0.45)
                shown = VGroup(row)
            else:
                self.stack_below(row, shown, buff=0.16)
                row.set_x(0)
                self.play(FadeIn(row), run_time=0.4)
                shown.add(row)
            self.linger(1.25)

        self.play(FadeOut(shown), run_time=0.35)
        table = self.aligned_table(
            [
                [
                    MathTex(r"n", font_size=28, color=GREY_B),
                    self.ja_text("有限の 9", font_size=22, color=GREY_B),
                    self.ja_text("1 との差", font_size=22, color=GREY_B),
                ],
                [
                    MathTex(r"1", font_size=30),
                    MathTex(r"0.9", font_size=30),
                    MathTex(r"1-0.9=0.1", font_size=30),
                ],
                [
                    MathTex(r"2", font_size=30),
                    MathTex(r"0.99", font_size=30),
                    MathTex(r"1-0.99=0.01", font_size=30),
                ],
                [
                    MathTex(r"3", font_size=30),
                    MathTex(r"0.999", font_size=30),
                    MathTex(r"1-0.999=0.001", font_size=30),
                ],
                [
                    MathTex(r"4", font_size=30),
                    MathTex(r"0.9999", font_size=30),
                    MathTex(r"1-0.9999=0.0001", font_size=30),
                ],
            ],
            h_buff=0.48,
            v_buff=0.16,
        )
        table.scale(0.8)
        self.stack_below(table, sub, buff=0.26)
        table.set_x(0)
        self.reveal_table(table, row_wait=0.85)

        note1 = self.ja_text("差は小さくなります。でも、どこで止めても 0 にはなりません。", font_size=24)
        self.stack_below(note1, table, buff=0.24)
        note1.set_x(0)
        self.play(FadeIn(note1), run_time=0.45)
        self.linger(note1.text)

        note2 = self.ja_text("だから「永遠に 1 より小さい」と感じます。", font_size=24, color=ORANGE)
        self.stack_below(note2, note1, buff=0.16)
        note2.set_x(0)
        self.play(FadeIn(note2), run_time=0.45)
        self.linger(note2.text, extra=0.35)

    def part_trial_third(self):
        self.wipe(self.header)
        chip = self.step_label("試行  三分の一")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("一方で、よく知っている分数からも同じ記号が出ます。", font_size=26)
        self.below_chip(lead, chip, buff=0.32)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.5)
        self.linger(lead.text)

        first = [
            MathTex(r"\dfrac{1}{3}=0.333\ldots", font_size=36),
            MathTex(r"3\times\dfrac{1}{3}=1", font_size=36),
        ]
        self._formula_rows(first, lead, buff=0.28)
        self.play(FadeOut(VGroup(*first)), run_time=0.3)

        col = MathTex(
            r"\begin{array}{r}0.333\ldots\\\times\ 3\\\hline 0.999\ldots\end{array}",
            font_size=36,
        )
        self.stack_below(col, lead, buff=0.32)
        col.set_x(0)
        self.play(FadeIn(col), run_time=0.55)
        self.linger(2.2)

        eq = MathTex(r"0.999\ldots=1", font_size=40, color=GREEN)
        self.stack_below(eq, col, buff=0.28)
        eq.set_x(0)
        self.play(FadeIn(eq), run_time=0.45)
        self.linger(3.2)

        self.play(FadeOut(col), FadeOut(eq), run_time=0.3)
        left = self._idea_card("有限桁を引く", "差が残る", ORANGE)
        right = self._idea_card("三分の一を 3 倍する", r"0.999\ldots=1", GREEN, extra_math=True)
        cols = VGroup(left, right).arrange(RIGHT, buff=0.7)
        self.stack_below(cols, lead, buff=0.36)
        cols.set_x(0)
        self.play(FadeIn(left), run_time=0.55)
        self.linger("差が残る")
        self.play(FadeIn(right), run_time=0.55)
        self.linger("同じ記号なのに、二つの直観がぶつかります。")

        clash = self.ja_text("同じ記号なのに、二つの直観がぶつかります。", font_size=26, color=YELLOW)
        self.stack_below(clash, cols, buff=0.28)
        clash.set_x(0)
        self.play(FadeIn(clash), run_time=0.45)
        self.linger(clash.text)

        hold = self.ja_text("どちらを信じるか、まだ決めません。差の式を最後まで書きます。", font_size=24)
        self.stack_below(hold, clash, buff=0.18)
        hold.set_x(0)
        self.play(FadeIn(hold), run_time=0.45)
        self.linger(hold.text, extra=0.3)

    def part_step1_gap(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 1  差の式")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("有限桁のほうを、記号で書いてみます。", font_size=26)
        self.below_chip(lead, chip, buff=0.32)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.5)
        self.linger(lead.text)

        def_row = self._line(
            MathTex(r"n", font_size=34),
            "個の 9 を並べた数を",
            MathTex(r"a_n", font_size=34),
            "と書く",
            font_size=26,
        )
        examples = MathTex(r"a_1=0.9,\quad a_2=0.99,\quad a_3=0.999", font_size=34)
        expand = MathTex(r"a_n=\dfrac{9}{10}+\dfrac{9}{100}+\cdots+\dfrac{9}{10^n}", font_size=34)
        defs = [def_row, examples, expand]
        self._formula_rows(defs, lead, buff=0.28)
        self.linger(2.4)

        self.play(FadeOut(VGroup(*defs)), run_time=0.3)
        derived = [
            MathTex(r"a_n=\dfrac{9}{10}\cdot\dfrac{1-10^{-n}}{1-1/10}", font_size=34),
            MathTex(r"=\dfrac{9}{10}\cdot\dfrac{10}{9}\bigl(1-10^{-n}\bigr)", font_size=34),
            MathTex(r"=1-10^{-n}", font_size=38),
            MathTex(r"1-a_n=10^{-n}", font_size=42, color=YELLOW),
        ]
        self._formula_rows(derived, lead, buff=0.26)
        self.linger(3.4)

        check = self._line(
            "検算:",
            MathTex(r"n=1", font_size=28),
            "なら",
            MathTex(r"10^{-1}=0.1", font_size=28),
            "、",
            MathTex(r"n=3", font_size=28),
            "なら",
            MathTex(r"10^{-3}=0.001", font_size=28),
            font_size=22,
        )
        check.to_edge(DOWN, buff=0.72)
        check.set_x(0)
        self.play(FadeIn(check), run_time=0.4)
        self.linger("検算: n=1 なら 10^{-1}=0.1、n=3 なら 10^{-3}=0.001")

        note = self._line(
            "「差が残る」は正しい。問題は、",
            MathTex(r"n", font_size=26),
            "を止めずに進めたときです。",
            font_size=22,
        )
        note.next_to(check, DOWN, buff=0.12)
        note.set_x(0)
        self.play(FadeIn(note), run_time=0.4)
        self.linger("問題は、n を止めずに進めたときです。", extra=0.3)

    def part_step2_bar(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 2  数直線")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("0 から 1 までの棒で、青い部分と残りの隙間を見ます。", font_size=24)
        self.below_chip(lead, chip, buff=0.3)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        stages = [
            (0.9, r"a_1=0.9", r"1-0.9=0.1", BLUE),
            (0.99, r"a_2=0.99", r"1-0.99=0.01", TEAL),
            (0.999, r"a_3=0.999", r"1-0.999=0.001", GOLD),
        ]
        bar = None
        cap = None
        gap = None
        zero = self.ja_text("0", font_size=20, color=GREY_B)
        one = MathTex(r"1", font_size=24, color=GREEN)
        for filled, name, gap_tex, color in stages:
            nxt_bar = self._gap_bar(filled, color=color)
            self.stack_below(nxt_bar, lead, buff=0.55)
            nxt_bar.set_x(0)
            nxt_zero = zero.copy().next_to(nxt_bar, LEFT, buff=0.16)
            nxt_one = one.copy().next_to(nxt_bar, RIGHT, buff=0.16)
            nxt_cap = MathTex(name, font_size=30, color=color)
            nxt_cap.next_to(nxt_bar, DOWN, buff=0.28)
            nxt_cap.set_x(0)
            nxt_gap = MathTex(gap_tex, font_size=32, color=YELLOW)
            nxt_gap.next_to(nxt_cap, DOWN, buff=0.18)
            nxt_gap.set_x(0)
            if bar is None:
                self.play(FadeIn(nxt_bar), FadeIn(nxt_zero), FadeIn(nxt_one), run_time=0.55)
                self.play(FadeIn(nxt_cap), FadeIn(nxt_gap), run_time=0.4)
                bar = nxt_bar
                cap = nxt_cap
                gap = nxt_gap
            else:
                self.play(Transform(bar, nxt_bar), run_time=0.7)
                self.play(Transform(cap, nxt_cap), Transform(gap, nxt_gap), run_time=0.45)
            self.linger(1.35)

        end_bar = self._gap_bar(1.0, color=GREEN)
        end_bar.move_to(bar)
        end_cap = MathTex(r"a_n\to 1", font_size=30, color=GREEN)
        end_cap.move_to(cap)
        end_gap = MathTex(r"1-1=0", font_size=32, color=GREEN)
        end_gap.move_to(gap)
        self.play(Transform(bar, end_bar), Transform(cap, end_cap), Transform(gap, end_gap), run_time=0.75)
        self.linger(1.4)

        note1 = self.ja_text("点は 1 にどんどん近づきます。", font_size=26)
        note1.next_to(gap, DOWN, buff=0.32)
        note1.set_x(0)
        self.play(FadeIn(note1), run_time=0.4)
        self.linger(note1.text)

        note2 = self._line(
            "隙間は",
            MathTex(r"10^{-n}", font_size=30),
            "で、",
            MathTex(r"n", font_size=30),
            "を大きくすると 0 に近づきます。",
            font_size=24,
        )
        self.stack_below(note2, note1, buff=0.14)
        note2.set_x(0)
        self.play(FadeIn(note2), run_time=0.4)
        self.linger("隙間は 10^{-n} で、n を大きくすると 0 に近づきます。")

        lim = MathTex(r"\lim_{n\to\infty}(1-a_n)=\lim_{n\to\infty}10^{-n}=0", font_size=34, color=YELLOW)
        self.stack_below(lim, note2, buff=0.2)
        lim.set_x(0)
        self.play(Write(lim), run_time=1.0)
        self.linger(3.5)

    def part_step3_tenx(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 3  10倍して引く")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("無限に続くほうを、いったん x と置きます。", font_size=26)
        self.below_chip(lead, chip, buff=0.32)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.5)
        self.linger(lead.text)

        first = [
            MathTex(r"x=0.999\ldots", font_size=38),
            MathTex(r"10x=9.999\ldots", font_size=38),
        ]
        first_block = self._formula_rows(first, lead, buff=0.28)

        col = MathTex(
            r"\begin{array}{r}9.999\ldots\\-0.999\ldots\\\hline 9.000\ldots\end{array}",
            font_size=36,
        )
        self.stack_below(col, first_block, buff=0.28)
        col.set_x(0)
        self.play(FadeIn(col), run_time=0.55)
        self.linger(2.4)

        self.play(FadeOut(first_block), run_time=0.3)
        self.play(col.animate.next_to(lead, DOWN, buff=0.28).set_x(0), run_time=0.4)

        rest = [
            MathTex(r"10x-x=9.999\ldots-0.999\ldots", font_size=32),
            MathTex(r"9x=9", font_size=38),
            MathTex(r"x=1", font_size=44, color=GREEN),
        ]
        rest_block = VGroup(*rest).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        self.stack_below(rest_block, col, buff=0.26)
        rest_block.set_x(0)
        for row in rest:
            self.play(FadeIn(row), run_time=0.45)
            self.linger(1.2)
        self.linger(3.3)

        note1 = self.ja_text("9 がどこまでも続くなら、引いたあとに小数部分は残りません。", font_size=22)
        note1.to_edge(DOWN, buff=0.52)
        note1.set_x(0)
        self.play(FadeIn(note1), run_time=0.4)
        self.linger(note1.text)

        note2 = self.ja_text("有限で止めると残りが出たのは、そこで 9 を切ったからです。", font_size=22)
        note2.next_to(note1, DOWN, buff=0.1)
        note2.set_x(0)
        self.play(FadeIn(note2), run_time=0.4)
        self.linger(note2.text, extra=0.3)

    def part_step4_series(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 4  等比級数")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("桁ごとにばらして足しても、同じ答えになります。", font_size=26)
        self.below_chip(lead, chip, buff=0.32)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.5)
        self.linger(lead.text)

        setup = [
            MathTex(r"0.999\ldots=0.9+0.09+0.009+\cdots", font_size=32),
            MathTex(r"=\dfrac{9}{10}+\dfrac{9}{100}+\dfrac{9}{1000}+\cdots", font_size=32),
            MathTex(r"=\dfrac{9}{10}\left(1+\dfrac{1}{10}+\dfrac{1}{100}+\cdots\right)", font_size=32),
            self._line(
                "初項",
                MathTex(r"1", font_size=28),
                "、公比",
                MathTex(r"1/10", font_size=28),
                "の無限等比級数。和を",
                MathTex(r"S", font_size=28),
                "と置く",
                font_size=22,
            ),
        ]
        setup_block = self._formula_rows(setup, lead, buff=0.2)
        self.play(FadeOut(setup_block), run_time=0.3)

        derived = [
            MathTex(r"S=1+\dfrac{1}{10}+\dfrac{1}{100}+\cdots", font_size=34),
            MathTex(r"\dfrac{1}{10}S=\dfrac{1}{10}+\dfrac{1}{100}+\cdots", font_size=34),
            MathTex(r"S-\dfrac{1}{10}S=1", font_size=36),
            MathTex(r"S=\dfrac{10}{9}", font_size=36),
            MathTex(r"\dfrac{9}{10}\times\dfrac{10}{9}=1", font_size=40, color=GREEN),
        ]
        self._formula_rows(derived, lead, buff=0.22)
        self.linger(3.3)

        note = self._line(
            "ばらして足しても、",
            MathTex(r"10x-x", font_size=28),
            "でも、答えは 1 です。",
            font_size=24,
        )
        note.to_edge(DOWN, buff=0.32)
        note.set_x(0)
        self.play(FadeIn(note), run_time=0.45)
        self.linger("ばらして足しても、10x-x でも、答えは 1 です。", extra=0.35)

    def part_example(self):
        self.wipe(self.header)
        chip = self.step_label("実例")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("同じ数を、最初から最後までもう一度辿ります。", font_size=26)
        self.below_chip(lead, chip, buff=0.32)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        items = [
            (
                "有限",
                MathTex(r"1-0.9=0.1,\ 1-0.99=0.01,\ 1-0.999=0.001", font_size=26),
            ),
            (
                "一般",
                MathTex(r"1-a_n=10^{-n}", font_size=34),
            ),
            (
                "極限",
                MathTex(r"n\to\infty\ \Rightarrow\ 10^{-n}\to 0", font_size=32),
            ),
            (
                "別計算",
                self._line(
                    MathTex(r"10x-x", font_size=30),
                    "でも等比級数でも",
                    MathTex(r"x=1", font_size=30),
                    font_size=26,
                ),
            ),
        ]
        shown = VGroup()
        for i, (tag, formula) in enumerate(items):
            tag_m = self.ja_text(tag, font_size=22, color=YELLOW)
            row = VGroup(tag_m, formula).arrange(RIGHT, buff=0.28)
            if i == 0:
                self.stack_below(row, lead, buff=0.34)
            else:
                self.stack_below(row, shown, buff=0.26)
            self._fit_left(row, 12.4)
            self.play(FadeIn(row), run_time=0.5)
            shown.add(row)
            self.linger(1.4)

        note1 = self.ja_text("「差が残る」は、止めたときの話でした。", font_size=26)
        self.stack_below(note1, shown, buff=0.36)
        self._fit_left(note1)
        self.play(FadeIn(note1), run_time=0.45)
        self.linger(note1.text)

        note2 = self.ja_text("止めないときの差は 0 なので、二つの書き方は同じ数です。", font_size=26, color=GREEN)
        self.stack_below(note2, note1, buff=0.18)
        self._fit_left(note2)
        self.play(FadeIn(note2), run_time=0.45)
        self.linger(3.2)

        self.play(FadeOut(shown), FadeOut(note1), FadeOut(note2), run_time=0.35)
        same = self.ja_text("同じ読み方で、よく知っている循環小数も閉じます。", font_size=24)
        self.stack_below(same, lead, buff=0.3)
        self._fit_left(same)
        self.play(FadeIn(same), run_time=0.4)
        self.linger(same.text)
        third = [
            MathTex(r"0.333\ldots=0.3+0.03+0.003+\cdots", font_size=32),
            MathTex(
                r"=\dfrac{3}{10}\left(1+\dfrac{1}{10}+\dfrac{1}{100}+\cdots\right)",
                font_size=32,
            ),
            MathTex(r"=\dfrac{3}{10}\times\dfrac{10}{9}=\dfrac{1}{3}", font_size=36, color=GREEN),
        ]
        self._formula_rows(third, same, buff=0.24)
        self.linger(3.2)

    def part_generalize(self):
        self.wipe(self.header)
        chip = self.step_label("一般化")
        self.play(FadeIn(chip), run_time=0.4)

        lines = [
            self.ja_text("今やったことは、無限小数を極限として読む、ということでした。", font_size=26),
            self._line(
                MathTex(r"0.999\ldots", font_size=30),
                "は、「9 を",
                MathTex(r"n", font_size=30),
                "個書いた数」の、",
                MathTex(r"n", font_size=30),
                "を限りなく進めた先です。",
                font_size=26,
            ),
            self._line(
                "その先では差",
                MathTex(r"10^{-n}", font_size=30),
                "が 0 になるので、",
                MathTex(r"1", font_size=30),
                "と同じ実数です。",
                font_size=26,
            ),
            self.ja_text("書き方が二つあっても、指している数は一つ、ということがあります。", font_size=26),
        ]
        linger_texts = [
            "今やったことは、無限小数を極限として読む、ということでした。",
            "0.999… は、9 を n 個書いた数の、n を限りなく進めた先です。",
            "その先では差 10^{-n} が 0 になるので、1 と同じ実数です。",
            "書き方が二つあっても、指している数は一つ、ということがあります。",
        ]
        shown = VGroup()
        for i, (mob, text) in enumerate(zip(lines, linger_texts)):
            if i == 0:
                self.below_chip(mob, chip, buff=0.34)
            else:
                self.stack_below(mob, shown, buff=0.24)
            self._fit_left(mob)
            self.play(FadeIn(mob), run_time=0.5)
            shown.add(mob)
            self.linger(text)

        lim = MathTex(
            r"0.999\ldots\ :=\ \lim_{n\to\infty}a_n=\lim_{n\to\infty}(1-10^{-n})=1",
            font_size=34,
            color=YELLOW,
        )
        self.stack_below(lim, shown, buff=0.36)
        lim.set_x(0)
        self.play(Write(lim), run_time=1.1)
        self.linger(3.6)

    def part_summary(self):
        self.wipe(self.header)
        chip = self.step_label("まとめ")
        self.play(FadeIn(chip), run_time=0.35)

        rows = [
            self._line(
                "有限個の 9 を 1 から引くと、差",
                MathTex(r"10^{-n}", font_size=28),
                "が残る",
                font_size=24,
            ),
            self.ja_text("9 を止めずに進めると、その差は 0 に収束する", font_size=24),
            self._line(
                "だから",
                MathTex(r"0.999\ldots", font_size=28),
                "と",
                MathTex(r"1", font_size=28),
                "は同じ数",
                font_size=24,
            ),
            self.ja_text("無限小数は、「どこまでも続く桁」の極限として読む", font_size=24),
        ]
        shown = VGroup()
        for i, mob in enumerate(rows):
            if i == 0:
                self.below_chip(mob, chip, buff=0.36)
            else:
                self.stack_below(mob, shown, buff=0.26)
            self._fit_left(mob)
            self.play(FadeIn(mob), run_time=0.5)
            shown.add(mob)
            self.linger(1.5)

        related = self.ja_text("循環小数が分数になる話も、同じ読み方で閉じます。", font_size=22, color=GREY_B)
        self.stack_below(related, shown, buff=0.36)
        self._fit_left(related)
        self.play(FadeIn(related), run_time=0.45)
        self.linger(related.text, extra=0.45)

    def _gap_bar(self, filled, color=BLUE, width=10.0, height=0.48):
        track = Rectangle(width=width, height=height, color=GREY_B, stroke_width=2)
        fill_w = max(width * filled - 0.04, 0.04)
        gap_w = max(width * (1.0 - filled) - 0.04, 0.03 if filled < 1 else 0.001)
        fill = Rectangle(
            width=fill_w,
            height=height - 0.1,
            color=color,
            fill_color=color,
            fill_opacity=0.75,
            stroke_width=0,
        )
        gap = Rectangle(
            width=gap_w,
            height=height - 0.1,
            color=ORANGE,
            fill_color=ORANGE,
            fill_opacity=0.0 if filled >= 1 else 0.8,
            stroke_width=0,
        )
        fill.move_to(track.get_left() + RIGHT * (fill_w / 2 + 0.02))
        if filled >= 1:
            gap.set_opacity(0)
            gap.move_to(track.get_right())
        else:
            gap.move_to(track.get_right() + LEFT * (gap_w / 2 + 0.02))
        return VGroup(track, fill, gap)

    def _value_card(self, tex, color):
        box = RoundedRectangle(
            width=4.4,
            height=2.0,
            corner_radius=0.14,
            color=color,
            stroke_width=3,
            fill_color=color,
            fill_opacity=0.16,
        )
        lab = MathTex(tex, font_size=56, color=color)
        lab.move_to(box)
        return VGroup(box, lab)

    def _idea_card(self, title, body, color, extra_math=False):
        box = RoundedRectangle(
            width=5.6,
            height=2.05,
            corner_radius=0.12,
            color=color,
            stroke_width=3,
            fill_color=color,
            fill_opacity=0.16,
        )
        t = self.ja_text(title, font_size=24, color=color)
        if extra_math:
            b = MathTex(body, font_size=34, color=color)
        else:
            b = self.ja_text(body, font_size=26)
        col = VGroup(t, b).arrange(DOWN, buff=0.22)
        col.move_to(box)
        return VGroup(box, col)

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
        block = VGroup(*rows).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        self.stack_below(block, under, buff=buff)
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
