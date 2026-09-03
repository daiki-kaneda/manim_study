from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import LessonScene


class RepeatingNines(LessonScene):
    """#1 0.999… は 1 か（約8分）"""

    def construct(self):
        self.header = self._open_header()
        self.part_question()
        self.part_trial_finite()
        self.part_trial_third()
        self.part_step1_gap()
        self.part_step2_line()
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
        left = self._value_card(r"0.999\ldots", BLUE)
        right = self._value_card(r"1", GREEN)
        cards = VGroup(left, right).arrange(RIGHT, buff=1.1)
        cards.next_to(self.header, DOWN, buff=0.7)
        cards.set_x(0)
        self.play(FadeIn(left, shift=LEFT * 0.2), FadeIn(right, shift=RIGHT * 0.2), run_time=0.8)
        self.linger(1.2)

        q1 = self.ja_text("この二つの書き方は、同じ数でしょうか。", font_size=28)
        q1.next_to(cards, DOWN, buff=0.45)
        q1.set_x(0)
        self.play(FadeIn(q1), run_time=0.5)
        self.linger(q1.text)

        q2 = self.ja_text("それとも、左のほうが、ほんの少し小さいでしょうか。", font_size=28)
        self.stack_below(q2, q1, buff=0.28)
        q2.set_x(0)
        self.play(FadeIn(q2), run_time=0.5)
        self.linger(q2.text, extra=0.3)

    def part_trial_finite(self):
        self.wipe(self.header)
        chip = self.step_label("試行  有限の 9")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("まず、9 を有限個だけ書いて、1 から引いてみます。", font_size=26)
        self.below_chip(lead, chip, buff=0.36)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.5)
        self.linger(lead.text)

        sub = self.ja_text("無限はいったん置いて、途中で止めた数だけを見ます。", font_size=26)
        self.stack_below(sub, lead, buff=0.22)
        self._fit_left(sub)
        self.play(FadeIn(sub), run_time=0.45)
        self.linger(sub.text)

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
            v_buff=0.18,
        )
        table.scale(0.82)
        self.stack_below(table, sub, buff=0.28)
        table.set_x(0)
        self.reveal_table(table, row_wait=0.95)

        note1 = self.ja_text("差は小さくなります。でも、どこで止めても 0 にはなりません。", font_size=24)
        self.stack_below(note1, table, buff=0.28)
        note1.set_x(0)
        self.play(FadeIn(note1), run_time=0.45)
        self.linger(note1.text)

        note2 = self.ja_text("だから「永遠に 1 より小さい」と感じます。", font_size=24, color=ORANGE)
        self.stack_below(note2, note1, buff=0.18)
        note2.set_x(0)
        self.play(FadeIn(note2), run_time=0.45)
        self.linger(note2.text, extra=0.35)

    def part_trial_third(self):
        self.wipe(self.header)
        chip = self.step_label("試行  三分の一")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("一方で、よく知っている分数からも同じ記号が出ます。", font_size=26)
        self.below_chip(lead, chip, buff=0.36)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.5)
        self.linger(lead.text)

        rows = [
            MathTex(r"\dfrac{1}{3}=0.333\ldots", font_size=36),
            MathTex(r"3\times\dfrac{1}{3}=1", font_size=36),
            MathTex(r"3\times 0.333\ldots=0.999\ldots", font_size=36),
            MathTex(r"0.999\ldots=1", font_size=40, color=GREEN),
        ]
        block = self._formula_rows(rows, lead, buff=0.32)
        self.linger(3.2)

        self.play(FadeOut(block), run_time=0.35)
        left = self._idea_card("有限桁を引く", "差が残る", ORANGE)
        right = self._idea_card("三分の一を 3 倍する", r"0.999\ldots=1", GREEN, extra_math=True)
        cols = VGroup(left, right).arrange(RIGHT, buff=0.7)
        self.stack_below(cols, lead, buff=0.4)
        cols.set_x(0)
        self.play(FadeIn(left), run_time=0.55)
        self.linger("差が残る")
        self.play(FadeIn(right), run_time=0.55)
        self.linger("同じ記号なのに、二つの直観がぶつかります。")

        clash = self.ja_text("同じ記号なのに、二つの直観がぶつかります。", font_size=26, color=YELLOW)
        self.stack_below(clash, cols, buff=0.32)
        clash.set_x(0)
        self.play(FadeIn(clash), run_time=0.45)
        self.linger(clash.text)

        hold = self.ja_text("どちらを信じるか、まだ決めません。差の式を最後まで書きます。", font_size=24)
        self.stack_below(hold, clash, buff=0.2)
        hold.set_x(0)
        self.play(FadeIn(hold), run_time=0.45)
        self.linger(hold.text, extra=0.3)

    def part_step1_gap(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 1  差の式")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("有限桁のほうを、記号で書いてみます。", font_size=26)
        self.below_chip(lead, chip, buff=0.36)
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
        gap = MathTex(r"1-a_n=10^{-n}", font_size=42, color=YELLOW)
        check1 = self._line(
            "検算:",
            MathTex(r"n=1", font_size=30),
            "なら",
            MathTex(r"10^{-1}=0.1", font_size=30),
            "。表の差と同じ",
            font_size=24,
        )
        check3 = self._line(
            "検算:",
            MathTex(r"n=3", font_size=30),
            "なら",
            MathTex(r"10^{-3}=0.001", font_size=30),
            "。これも同じ",
            font_size=24,
        )
        rows = [def_row, examples, gap, check1, check3]
        self._formula_rows(rows, lead, buff=0.28)
        self.linger(3.4)

        note1 = self._line(
            "止めた位置が",
            MathTex(r"n", font_size=28),
            "なら、残りはいつも",
            MathTex(r"10^{-n}", font_size=28),
            "です。",
            font_size=24,
        )
        note1.to_edge(DOWN, buff=0.55)
        note1.set_x(0)
        self.play(FadeIn(note1), run_time=0.4)
        self.linger("止めた位置が n なら、残りはいつも 10^{-n} です。")

        note2 = self._line(
            "「差が残る」は正しい。問題は、",
            MathTex(r"n", font_size=28),
            "を止めずに進めたときです。",
            font_size=24,
        )
        note2.next_to(note1, DOWN, buff=0.12)
        note2.set_x(0)
        self.play(FadeIn(note2), run_time=0.4)
        self.linger("問題は、n を止めずに進めたときです。", extra=0.3)

    def part_step2_line(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 2  数直線")
        self.play(FadeIn(chip), run_time=0.4)

        axis = NumberLine(
            x_range=[0.85, 1.05, 0.05],
            length=11.0,
            include_numbers=False,
            include_ticks=False,
            stroke_width=3,
            color=GREY_B,
        )
        self.below_chip(axis, chip, buff=0.7)
        axis.set_x(0)
        tick1 = Line(axis.n2p(1.0) + UP * 0.12, axis.n2p(1.0) + DOWN * 0.12, color=GREEN, stroke_width=4)
        lab1 = MathTex(r"1", font_size=32, color=GREEN)
        lab1.next_to(tick1, UP, buff=0.16)
        self.play(Create(axis), FadeIn(tick1), FadeIn(lab1), run_time=0.7)

        stages = [
            (0.9, r"0.9", r"1-0.9=0.1", BLUE),
            (0.99, r"0.99", r"1-0.99=0.01", TEAL),
            (0.999, r"0.999", r"1-0.999=0.001", GOLD),
        ]
        trail = VGroup()
        moving = None
        name_lab = None
        gap_lab = None
        brace = None
        for x, name, gap_tex, color in stages:
            dot = Dot(axis.n2p(x), color=color, radius=0.1)
            nxt_name = MathTex(name, font_size=30, color=color)
            nxt_name.next_to(dot, DOWN, buff=0.22)
            if x >= 0.99:
                nxt_name.shift(LEFT * 0.55)
            nxt_gap = MathTex(gap_tex, font_size=28, color=YELLOW)
            nxt_gap.next_to(axis, DOWN, buff=1.05)
            nxt_gap.set_x(0)
            nxt_brace = BraceBetweenPoints(axis.n2p(x), axis.n2p(1.0), direction=DOWN, color=ORANGE)
            if moving is None:
                self.play(FadeIn(dot, scale=0.4), FadeIn(nxt_name), GrowFromCenter(nxt_brace), FadeIn(nxt_gap), run_time=0.7)
                moving = dot
                name_lab = nxt_name
                gap_lab = nxt_gap
                brace = nxt_brace
            else:
                ghost = moving.copy().set_opacity(0.35)
                trail.add(ghost)
                self.add(ghost)
                self.play(
                    moving.animate.move_to(axis.n2p(x)).set_color(color),
                    Transform(name_lab, nxt_name),
                    Transform(brace, nxt_brace),
                    Transform(gap_lab, nxt_gap),
                    run_time=0.75,
                )
            self.linger(1.2)

        end_dot = Dot(axis.n2p(1.0), color=GREEN, radius=0.1)
        end_gap = MathTex(r"1-1=0", font_size=28, color=GREEN)
        end_gap.move_to(gap_lab)
        self.play(
            moving.animate.move_to(axis.n2p(1.0)).set_color(GREEN),
            FadeIn(end_dot),
            FadeOut(brace),
            FadeOut(name_lab),
            Transform(gap_lab, end_gap),
            run_time=0.8,
        )
        self.linger(1.3)

        note1 = self.ja_text("点は 1 にどんどん近づきます。", font_size=26)
        note1.next_to(gap_lab, DOWN, buff=0.32)
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
        self.stack_below(note2, note1, buff=0.16)
        note2.set_x(0)
        self.play(FadeIn(note2), run_time=0.4)
        self.linger("隙間は 10^{-n} で、n を大きくすると 0 に近づきます。")

        lim = MathTex(r"\lim_{n\to\infty}(1-a_n)=\lim_{n\to\infty}10^{-n}=0", font_size=36, color=YELLOW)
        self.stack_below(lim, note2, buff=0.22)
        lim.set_x(0)
        self.play(Write(lim), run_time=1.0)
        self.linger(3.5)

    def part_step3_tenx(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 3  10倍して引く")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("無限に続くほうを、いったん x と置きます。", font_size=26)
        self.below_chip(lead, chip, buff=0.36)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.5)
        self.linger(lead.text)

        steps = [
            MathTex(r"x=0.999\ldots", font_size=38),
            MathTex(r"10x=9.999\ldots", font_size=38),
            MathTex(r"10x-x=9.999\ldots-0.999\ldots", font_size=36),
            MathTex(r"9x=9", font_size=38),
            MathTex(r"x=1", font_size=44, color=GREEN),
        ]
        self._formula_rows(steps, lead, buff=0.28)
        self.linger(3.3)

        note1 = self.ja_text("9 がどこまでも続くなら、引いたあとに小数部分は残りません。", font_size=24)
        note1.to_edge(DOWN, buff=0.55)
        note1.set_x(0)
        self.play(FadeIn(note1), run_time=0.4)
        self.linger(note1.text)

        note2 = self.ja_text("有限で止めると残りが出たのは、そこで 9 を切ったからです。", font_size=24)
        note2.next_to(note1, DOWN, buff=0.12)
        note2.set_x(0)
        self.play(FadeIn(note2), run_time=0.4)
        self.linger(note2.text, extra=0.3)

    def part_step4_series(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 4  等比級数")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("桁ごとにばらして足しても、同じ答えになります。", font_size=26)
        self.below_chip(lead, chip, buff=0.36)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.5)
        self.linger(lead.text)

        steps = [
            MathTex(r"0.999\ldots=0.9+0.09+0.009+\cdots", font_size=34),
            MathTex(r"=\dfrac{9}{10}+\dfrac{9}{100}+\dfrac{9}{1000}+\cdots", font_size=34),
            MathTex(r"=\dfrac{9}{10}\left(1+\dfrac{1}{10}+\dfrac{1}{100}+\cdots\right)", font_size=34),
            self._line(
                "初項",
                MathTex(r"1", font_size=30),
                "、公比",
                MathTex(r"1/10", font_size=30),
                "の無限等比級数",
                font_size=24,
            ),
            MathTex(r"\dfrac{1}{1-1/10}=\dfrac{10}{9}", font_size=36),
            MathTex(r"\dfrac{9}{10}\times\dfrac{10}{9}=1", font_size=40, color=GREEN),
        ]
        self._formula_rows(steps, lead, buff=0.24)
        self.linger(3.3)

        note = self._line(
            "ばらして足しても、",
            MathTex(r"10x-x", font_size=28),
            "でも、答えは 1 です。",
            font_size=24,
        )
        note.to_edge(DOWN, buff=0.38)
        note.set_x(0)
        self.play(FadeIn(note), run_time=0.45)
        self.linger("ばらして足しても、10x-x でも、答えは 1 です。", extra=0.35)

    def part_example(self):
        self.wipe(self.header)
        chip = self.step_label("実例")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("同じ数を、最初から最後までもう一度辿ります。", font_size=26)
        self.below_chip(lead, chip, buff=0.36)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        items = [
            (
                "有限",
                MathTex(r"1-0.9=0.1,\ 1-0.99=0.01,\ 1-0.999=0.001", font_size=28),
            ),
            (
                "一般",
                MathTex(r"1-a_n=10^{-n}", font_size=34),
            ),
            (
                "極限",
                MathTex(r"n\to\infty\ \Rightarrow\ 10^{-n}\to 0", font_size=34),
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
                self.stack_below(row, lead, buff=0.38)
            else:
                self.stack_below(row, shown, buff=0.3)
            self._fit_left(row, 12.4)
            self.play(FadeIn(row), run_time=0.5)
            shown.add(row)
            self.linger(1.35)

        note1 = self.ja_text("「差が残る」は、止めたときの話でした。", font_size=26)
        self.stack_below(note1, shown, buff=0.4)
        self._fit_left(note1)
        self.play(FadeIn(note1), run_time=0.45)
        self.linger(note1.text)

        note2 = self.ja_text("止めないときの差は 0 なので、二つの書き方は同じ数です。", font_size=26, color=GREEN)
        self.stack_below(note2, note1, buff=0.2)
        self._fit_left(note2)
        self.play(FadeIn(note2), run_time=0.45)
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
        shown = VGroup()
        linger_texts = [
            "今やったことは、無限小数を極限として読む、ということでした。",
            "0.999… は、9 を n 個書いた数の、n を限りなく進めた先です。",
            "その先では差 10^{-n} が 0 になるので、1 と同じ実数です。",
            "書き方が二つあっても、指している数は一つ、ということがあります。",
        ]
        for i, (mob, text) in enumerate(zip(lines, linger_texts)):
            if i == 0:
                self.below_chip(mob, chip, buff=0.38)
            else:
                self.stack_below(mob, shown, buff=0.26)
            self._fit_left(mob)
            self.play(FadeIn(mob), run_time=0.5)
            shown.add(mob)
            self.linger(text)

        lim = MathTex(
            r"0.999\ldots\ :=\ \lim_{n\to\infty}a_n=\lim_{n\to\infty}(1-10^{-n})=1",
            font_size=36,
            color=YELLOW,
        )
        self.stack_below(lim, shown, buff=0.4)
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
                MathTex(r"10^{-n}", font_size=30),
                "が残る",
                font_size=26,
            ),
            self.ja_text("9 を止めずに進めると、その差は 0 に収束する", font_size=26),
            self._line(
                "だから",
                MathTex(r"0.999\ldots", font_size=30),
                "と",
                MathTex(r"1", font_size=30),
                "は同じ数",
                font_size=26,
            ),
            self.ja_text("無限小数は、「どこまでも続く桁」の極限として読む", font_size=26),
        ]
        shown = VGroup()
        for i, mob in enumerate(rows):
            if i == 0:
                self.below_chip(mob, chip, buff=0.4)
            else:
                self.stack_below(mob, shown, buff=0.3)
            self._fit_left(mob)
            self.play(FadeIn(mob), run_time=0.5)
            shown.add(mob)
            self.linger(1.4)

        related = self.ja_text("循環小数が分数になる話も、同じ読み方で閉じます。", font_size=24, color=GREY_B)
        self.stack_below(related, shown, buff=0.42)
        self._fit_left(related)
        self.play(FadeIn(related), run_time=0.45)
        self.linger(related.text, extra=0.4)

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
            self.linger(1.15)
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
