from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import LessonScene


class RegionsFromLines(LessonScene):
    """#7 直線 n 本で領域は最大いくつか（約8分）"""

    WIN_W = 5.40
    WIN_H = 3.20

    def construct(self):
        self.header = self._open_header()
        self.part_question()
        self.part_trial_parallel()
        self.part_trial_point()
        self.part_step1_count()
        self.part_step2_maximize()
        self.part_step3_recurrence()
        self.part_step4_sum()
        self.part_example()
        self.part_generalize()
        self.part_summary()

    def _open_header(self):
        title = self._line(
            "直線",
            MathTex(r"n", font_size=40),
            "本で領域は最大いくつか",
            font_size=36,
        )
        self.play(FadeIn(title), run_time=0.8)
        self.linger(1.2)
        self.play(title.animate.scale(0.52).to_edge(UP, buff=0.16), run_time=0.5)
        title.set_x(0)
        return title

    def part_question(self):
        fig = self._arrangement(
            [(0.0, 0.0)],
            fills=True,
        )
        fig.next_to(self.header, DOWN, buff=0.36)
        fig.set_x(0)
        self.play(FadeIn(fig), run_time=0.9)
        self.linger(3.2)

        q1 = self.ja_text("平面に直線を 1 本ずつ引いていきます。", font_size=26)
        q1.next_to(fig, DOWN, buff=0.30)
        q1.set_x(0)
        self.play(FadeIn(q1), run_time=0.45)
        self.linger(q1.text)

        q2 = self.ja_text("領域の個数をいちばん多くするには、どう交わせばよいでしょう。", font_size=26)
        self.stack_below(q2, q1, buff=0.16)
        q2.set_x(0)
        self._fit(q2, 13.0)
        q2.set_x(0)
        self.play(FadeIn(q2), run_time=0.45)
        self.linger(q2.text, extra=0.35)

    def part_trial_parallel(self):
        self.wipe(self.header)
        chip = self.step_label("試行  平行")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("まず、どの 2 本も交わらないように、全部平行にしてみます。", font_size=22)
        self.below_chip(lead, chip, buff=0.20)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        slopes = [(0.0, -1.05), (0.0, -0.35), (0.0, 0.35), (0.0, 1.05)]
        fig = self._arrangement(slopes[:1])
        count = MathTex(r"1", font_size=40, color=YELLOW)
        label = self.ja_text("領域", font_size=20, color=GREY_B)
        right = VGroup(label, count).arrange(DOWN, buff=0.10)
        pair = VGroup(fig, right).arrange(RIGHT, buff=0.55, aligned_edge=UP)
        self.stack_below(pair, lead, buff=0.18)
        pair.set_x(0)
        self._nudge(pair)

        self.play(FadeIn(fig), FadeIn(right), run_time=0.6)
        self.linger(3.2)

        totals = ["2", "3", "4", "5"]
        for i, tex in enumerate(totals):
            nxt = self._arrangement(slopes[: i + 1])
            nxt.move_to(fig)
            new_count = MathTex(tex, font_size=40, color=YELLOW)
            new_count.move_to(count)
            self.play(FadeOut(fig), FadeIn(nxt), Transform(count, new_count), run_time=0.55)
            fig = nxt
            self.linger(3.2)

        table = self.aligned_table(
            [
                [
                    self.ja_text("本数", font_size=16, color=GREY_B),
                    self.ja_text("増えた数", font_size=16, color=GREY_B),
                    self.ja_text("領域", font_size=16, color=GREY_B),
                ],
                [MathTex(r"0", font_size=24), self.ja_text("—", font_size=18), MathTex(r"1", font_size=24)],
                [MathTex(r"1", font_size=24), MathTex(r"+1", font_size=24), MathTex(r"2", font_size=24)],
                [MathTex(r"2", font_size=24), MathTex(r"+1", font_size=24), MathTex(r"3", font_size=24)],
                [MathTex(r"3", font_size=24), MathTex(r"+1", font_size=24), MathTex(r"4", font_size=24)],
                [MathTex(r"4", font_size=24), MathTex(r"+1", font_size=24), MathTex(r"5", font_size=24)],
            ],
            h_buff=0.32,
            v_buff=0.10,
        )
        table.scale(0.78)
        self.play(FadeOut(VGroup(fig, right)), run_time=0.3)
        self.stack_below(table, lead, buff=0.16)
        table.set_x(0)
        self.reveal_table(table, row_wait=0.70)

        notes = [
            self.ja_text("平行だと、新しい直線は既存の直線と 1 点も交わりません。", font_size=22),
            self.ja_text("何本足しても、増える数はいつも 1 です。", font_size=22),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, table, buff=0.14)
            else:
                self.stack_below(mob, shown, buff=0.10)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.4)
            shown.add(mob)
            self.linger(3.2)

    def part_trial_point(self):
        self.wipe(self.header)
        chip = self.step_label("試行  1 点")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("こんどは、全部の直線を 1 点で交わるようにしてみます。", font_size=22)
        self.below_chip(lead, chip, buff=0.20)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        # y = m x, all through the origin. Last two nearly vertical via large slope.
        slopes = [(0.0, 0.0), (0.70, 0.0), (-0.85, 0.0), (2.40, 0.0)]
        fig = self._arrangement(slopes[:1], mark_origin=True)
        self.stack_below(fig, lead, buff=0.16)
        fig.to_edge(LEFT, buff=0.40)
        self._nudge(fig)
        self.play(FadeIn(fig), run_time=0.55)
        self.linger(3.2)

        rows = [
            self.ja_text("新しい直線は、1 点で 2 本の半直線に切れる。", font_size=18),
            MathTex(r"2+2=4", font_size=30),
            MathTex(r"4+2=6", font_size=30),
            MathTex(r"6+2=8", font_size=30, color=YELLOW),
        ]
        block = VGroup(*rows).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        block.next_to(fig, RIGHT, buff=0.40)
        block.align_to(fig, UP)
        self._nudge(block)
        self.play(FadeIn(rows[0]), run_time=0.35)
        self.linger(3.2)

        adds = [slopes[:2], slopes[:3], slopes[:4]]
        for spec, row in zip(adds, rows[1:]):
            nxt = self._arrangement(spec, mark_origin=True, pieces_of=-1)
            nxt.move_to(fig)
            self.play(FadeOut(fig), FadeIn(nxt), FadeIn(row), run_time=0.55)
            fig = nxt
            self.linger(3.2)

        table = self.aligned_table(
            [
                [
                    self.ja_text("本数", font_size=16, color=GREY_B),
                    self.ja_text("増えた数", font_size=16, color=GREY_B),
                    self.ja_text("領域", font_size=16, color=GREY_B),
                ],
                [MathTex(r"1", font_size=24), MathTex(r"+1", font_size=24), MathTex(r"2", font_size=24)],
                [MathTex(r"2", font_size=24), MathTex(r"+2", font_size=24), MathTex(r"4", font_size=24)],
                [MathTex(r"3", font_size=24), MathTex(r"+2", font_size=24), MathTex(r"6", font_size=24)],
                [MathTex(r"4", font_size=24), MathTex(r"+2", font_size=24), MathTex(r"8", font_size=24)],
            ],
            h_buff=0.32,
            v_buff=0.10,
        )
        table.scale(0.80)
        self.play(FadeOut(VGroup(fig, block)), run_time=0.3)
        self.stack_below(table, lead, buff=0.16)
        table.set_x(0)
        self.reveal_table(table, row_wait=0.70)

        notes = [
            self.ja_text("1 点に集めると、平行よりは増えます。", font_size=22),
            self.ja_text("3 本目からは、増える数が 2 で止まります。交点が 1 か所に固まっているからです。", font_size=22),
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

    def part_step1_count(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 1  個数")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("領域の個数の最大を、記号で書いておきます。", font_size=22)
        self.below_chip(lead, chip, buff=0.22)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        defs = [
            self._line(MathTex(r"n", font_size=28, color=YELLOW), "を、引く直線の本数とおく。", font_size=22),
            self._line(MathTex(r"R(n)", font_size=28, color=ORANGE), "を、", MathTex(r"n", font_size=26, color=YELLOW), "本で作れる領域の個数の最大とおく。", font_size=22),
            MathTex(r"R(0)=1", font_size=36, color=YELLOW),
            MathTex(r"R(1)=2", font_size=36, color=TEAL),
        ]
        self._formula_rows(defs, lead, buff=0.18)
        self.linger(3.4)

        notes = [
            self.ja_text("最大にするには、新しい直線がいちばん多く領域を切ればよい。", font_size=22),
            self.ja_text("切る回数は、新しい直線が何個に分かれるかで決まります。", font_size=22),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            mob.to_edge(DOWN, buff=0.70 if i == 0 else 0.32)
            if i == 1:
                self.stack_below(mob, shown, buff=0.10)
                mob.set_x(0)
            else:
                mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.4)
            shown.add(mob)
            self.linger(3.2)

    def part_step2_maximize(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 2  増やす")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("新しい直線が、既存の直線とどう交わると、いちばん多く切れるかを見ます。", font_size=20)
        self.below_chip(lead, chip, buff=0.18)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        kdef = self._line(
            MathTex(r"k", font_size=26, color=YELLOW),
            "を、すでに引いてある直線の本数とおく。新しい直線は",
            MathTex(r"k+1", font_size=26),
            "本目。",
            font_size=18,
        )
        self.stack_below(kdef, lead, buff=0.12)
        kdef.set_x(0)
        self._fit(kdef, 13.0)
        kdef.set_x(0)
        self.play(FadeIn(kdef), run_time=0.4)
        self.linger(3.2)

        # 2本目
        two = [(0.0, 0.0), (0.70, 0.0)]
        fig2 = self._arrangement(two, pieces_of=-1, mark_origin=True)
        rows2 = [
            self.ja_text("2 本目", font_size=20, color=GREY_B),
            self.ja_text("交点は 1 個。直線は 2 本の半直線に切れる。", font_size=18),
            MathTex(r"R(1)+2=2+2=4", font_size=30, color=YELLOW),
        ]
        block2 = VGroup(*rows2).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        pair2 = VGroup(fig2, block2).arrange(RIGHT, buff=0.40, aligned_edge=UP)
        self.stack_below(pair2, kdef, buff=0.14)
        pair2.set_x(0)
        self._nudge(pair2)
        self.play(FadeIn(fig2), run_time=0.55)
        for row in rows2:
            self.play(FadeIn(row), run_time=0.35)
            self.linger(3.2)
        self.play(FadeOut(pair2), run_time=0.3)

        # 3本目
        three = [(0.0, 0.0), (0.70, 0.0), (-0.80, 0.90)]
        fig3 = self._arrangement(three, pieces_of=-1)
        rows3 = [
            self.ja_text("3 本目", font_size=20, color=GREY_B),
            self.ja_text("既存の 2 本と、異なる 2 点で交わる。", font_size=18),
            self.ja_text("直線は 3 つに切れる。半直線、線分、半直線。", font_size=18),
            MathTex(r"R(2)+3=4+3=7", font_size=32, color=YELLOW),
        ]
        block3 = VGroup(*rows3).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        pair3 = VGroup(fig3, block3).arrange(RIGHT, buff=0.36, aligned_edge=UP)
        self.stack_below(pair3, kdef, buff=0.12)
        pair3.set_x(0)
        self._nudge(pair3)
        self.play(FadeIn(fig3), run_time=0.65)
        for row in rows3:
            self.play(FadeIn(row), run_time=0.35)
            self.linger(3.2)
        self.linger(3.4)
        self.play(FadeOut(pair3), run_time=0.3)

        notes = [
            self.ja_text("既存のどの直線とも 1 点で交わり、その交点がすべて異なるときがいちばん増えます。", font_size=20),
            self.ja_text("そのとき、新しい直線は既存の本数より 1 つ多くに切れます。", font_size=20),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                mob.to_edge(DOWN, buff=0.58)
            else:
                self.stack_below(mob, shown, buff=0.08)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.4)
            shown.add(mob)
            self.linger(3.2)

    def part_step3_recurrence(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 3  漸化式")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("いま観察した増え方を、記号で書きます。", font_size=22)
        self.below_chip(lead, chip, buff=0.20)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        first = [
            self._line(MathTex(r"R(n)", font_size=26, color=ORANGE), "を、", MathTex(r"n", font_size=24, color=YELLOW), "本で作れる領域の個数の最大とおく。", font_size=20),
            self._line(MathTex(r"n", font_size=24, color=YELLOW), "本目は、既存の", MathTex(r"n-1", font_size=24), "本と異なる", MathTex(r"n-1", font_size=24), "点で交わる。", font_size=20),
            self._line("直線上の異なる", MathTex(r"n-1", font_size=24), "点は、その直線を", MathTex(r"n", font_size=24, color=YELLOW), "個に分ける。", font_size=20),
            MathTex(r"R(n)=R(n-1)+n", font_size=40, color=YELLOW),
            MathTex(r"R(0)=1", font_size=32),
        ]
        block = self._formula_rows(first, lead, buff=0.14)
        self.linger(3.6)
        self.play(FadeOut(block), run_time=0.3)

        table = self.aligned_table(
            [
                [
                    MathTex(r"n", font_size=22, color=YELLOW),
                    self.ja_text("増えた数", font_size=16, color=GREY_B),
                    MathTex(r"R(n)", font_size=22, color=ORANGE),
                ],
                [MathTex(r"0", font_size=24), self.ja_text("—", font_size=18), MathTex(r"1", font_size=24)],
                [MathTex(r"1", font_size=24), MathTex(r"+1", font_size=24), MathTex(r"1+1=2", font_size=24)],
                [MathTex(r"2", font_size=24), MathTex(r"+2", font_size=24), MathTex(r"2+2=4", font_size=24)],
                [MathTex(r"3", font_size=24), MathTex(r"+3", font_size=24), MathTex(r"4+3=7", font_size=24)],
                [MathTex(r"4", font_size=24), MathTex(r"+4", font_size=24), MathTex(r"7+4=11", font_size=24)],
                [MathTex(r"5", font_size=24), MathTex(r"+5", font_size=24), MathTex(r"11+5=16", font_size=24)],
            ],
            h_buff=0.34,
            v_buff=0.08,
        )
        table.scale(0.78)
        self.stack_below(table, lead, buff=0.14)
        table.set_x(0)
        self.reveal_table(table, row_wait=0.72)

        notes = [
            self.ja_text("増える数は 1、2、3、4、5 と、本数そのものです。", font_size=22),
            self.ja_text("閉じた式は、この足し算をまとめれば出ます。", font_size=22),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, table, buff=0.14)
            else:
                self.stack_below(mob, shown, buff=0.10)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.4)
            shown.add(mob)
            self.linger(3.2)

    def part_step4_sum(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 4  ほどく")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("漸化式を、最初までほどいて和にします。", font_size=22)
        self.below_chip(lead, chip, buff=0.18)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        first = [
            self._line(MathTex(r"R(n)", font_size=26, color=ORANGE), "を最大の領域の個数、", MathTex(r"R(0)=1", font_size=26), "とおく。", font_size=20),
            MathTex(r"R(n)=R(n-1)+n", font_size=32),
            MathTex(r"R(n)=R(n-2)+(n-1)+n", font_size=30),
            MathTex(r"R(n)=R(0)+1+2+\cdots+n", font_size=30),
            MathTex(r"R(n)=1+(1+2+\cdots+n)", font_size=32, color=YELLOW),
        ]
        block1 = self._formula_rows(first, lead, buff=0.12)
        self.play(FadeOut(block1), run_time=0.3)

        second = [
            self._line(MathTex(r"n=4", font_size=26), "なら", MathTex(r"1+2+3+4", font_size=28), font_size=20),
            MathTex(r"1+4=5,\quad 2+3=5", font_size=30),
            MathTex(r"\dfrac{4}{2}=2\qquad 2\times 5=10", font_size=30),
            MathTex(r"1+2+\cdots+n=\dfrac{n}{2}\cdot(n+1)=\dfrac{n(n+1)}{2}", font_size=28),
            MathTex(r"R(n)=1+\dfrac{n(n+1)}{2}", font_size=40, color=YELLOW),
        ]
        block2 = self._formula_rows(second, lead, buff=0.12)
        self.linger(3.6)
        self.play(FadeOut(block2), run_time=0.3)

        checks = [
            self.ja_text("STEP 3 の表でも、同じ式になる。", font_size=20),
            MathTex(r"n=4:\quad 1+\dfrac{4\cdot 5}{2}=1+10=11", font_size=30),
            MathTex(r"n=5:\quad 1+\dfrac{5\cdot 6}{2}=1+15=16", font_size=30, color=YELLOW),
        ]
        self._formula_rows(checks, lead, buff=0.16)

    def part_example(self):
        self.wipe(self.header)
        chip = self.step_label("実例")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("4 本で、いちばん増やす交わりを最後まで数えます。", font_size=22)
        self.below_chip(lead, chip, buff=0.18)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        four = [(0.0, 0.0), (0.70, 0.0), (-0.80, 0.90), (0.35, -0.75)]
        fig = self._arrangement(four, pieces_of=-1)
        rows = [
            self._line(MathTex(r"R(n)", font_size=26, color=ORANGE), "を最大の領域の個数とおく。", font_size=18),
            MathTex(r"n=4", font_size=28),
            MathTex(r"R(4)=1+\dfrac{4\cdot 5}{2}=1+10=11", font_size=28, color=YELLOW),
            self.ja_text("4 本目は既存の 3 本と、異なる 3 点で交わる。", font_size=18),
            MathTex(r"7+4=11", font_size=32, color=GREEN),
        ]
        block = VGroup(*rows).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        pair = VGroup(fig, block).arrange(RIGHT, buff=0.36, aligned_edge=UP)
        self.stack_below(pair, lead, buff=0.12)
        pair.set_x(0)
        self._nudge(pair)
        self.play(FadeIn(fig), run_time=0.7)
        for row in rows:
            self.play(FadeIn(row), run_time=0.35)
            self.linger(3.2)
        self.linger(3.4)
        self.play(FadeOut(pair), run_time=0.3)

        table = self.aligned_table(
            [
                [
                    self.ja_text("交わり方", font_size=16, color=GREY_B),
                    self.ja_text("4 本の領域", font_size=16, color=GREY_B),
                ],
                [
                    self.ja_text("全部平行", font_size=20),
                    MathTex(r"5", font_size=28),
                ],
                [
                    self.ja_text("1 点で交わる", font_size=20),
                    MathTex(r"8", font_size=28),
                ],
                [
                    self.ja_text("交点をばらす", font_size=20),
                    MathTex(r"11", font_size=28, color=GREEN),
                ],
            ],
            h_buff=0.42,
            v_buff=0.12,
        )
        table.scale(0.90)
        self.stack_below(table, lead, buff=0.16)
        table.set_x(0)
        self.reveal_table(table, row_wait=0.80)

        notes = [
            self.ja_text("平行でも 1 点でもなく、交点を重ねない方法がいちばん多い。", font_size=22),
            self.ja_text("新しい直線が何個に切れるかを数えれば、増え方が書けます。", font_size=22),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, table, buff=0.14)
            else:
                self.stack_below(mob, shown, buff=0.10)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.4)
            shown.add(mob)
            self.linger(3.2)

    def part_generalize(self):
        self.wipe(self.header)
        chip = self.step_label("一般化")
        self.play(FadeIn(chip), run_time=0.4)

        lead_lines = [
            self.ja_text("今やったことは、直線を 1 本足すときの増え方を、漸化式に書く考え方でした。", font_size=20),
            self._line(MathTex(r"R(n)", font_size=24, color=ORANGE), "を、平面を直線", MathTex(r"n", font_size=22, color=YELLOW), "本で切ったときの、領域の個数の最大とおく。", font_size=18),
            self._line("いちばん増やす交わりなら", MathTex(r"R(n)=R(n-1)+n", font_size=24), "、", MathTex(r"R(0)=1", font_size=24), font_size=18),
            self._line("ほどくと", MathTex(r"R(n)=1+\dfrac{n(n+1)}{2}", font_size=26, color=YELLOW), "。", font_size=20),
        ]
        shown = VGroup()
        for i, mob in enumerate(lead_lines):
            if i == 0:
                self.below_chip(mob, chip, buff=0.22)
            else:
                self.stack_below(mob, shown, buff=0.12)
            self._fit_left(mob)
            self.play(FadeIn(mob), run_time=0.45)
            shown.add(mob)
            self.linger(3.2)

        self.play(FadeOut(shown), run_time=0.3)
        name = self.ja_text("帰納法", font_size=22, color=GREY_B)
        self.below_chip(name, chip, buff=0.20)
        self.play(FadeIn(name), run_time=0.35)
        self.linger(name.text)

        proof = [
            MathTex(r"n=0:\quad 1=1", font_size=28),
            self._line(MathTex(r"k", font_size=24), "本で", MathTex(r"R(k)=1+\dfrac{k(k+1)}{2}", font_size=26), "とおく。", font_size=20),
            MathTex(r"R(k)+(k+1)=1+\dfrac{k(k+1)}{2}+(k+1)", font_size=28),
            MathTex(r"\dfrac{k(k+1)}{2}+(k+1)=\dfrac{k(k+1)+2(k+1)}{2}", font_size=26),
            MathTex(r"=\dfrac{(k+1)(k+2)}{2}", font_size=30, color=GREEN),
            MathTex(r"R(k+1)=1+\dfrac{(k+1)(k+2)}{2}", font_size=32, color=YELLOW),
        ]
        block = self._formula_rows(proof, name, buff=0.12)
        self.linger(3.4)

        close = self.ja_text("0 本で合って、1 本足しても形が保たれるなら、何本でも合います。これが帰納法です。", font_size=20)
        self.stack_below(close, block, buff=0.14)
        close.set_x(0)
        self._fit(close, 13.0)
        close.set_x(0)
        self.play(FadeIn(close), run_time=0.45)
        self.linger(close.text, extra=0.35)

    def part_summary(self):
        self.wipe(self.header)
        chip = self.step_label("まとめ")
        self.play(FadeIn(chip), run_time=0.35)

        rows = [
            self.ja_text("全部平行だと、増える数はいつも 1", font_size=24),
            self.ja_text("1 点に集めると、増える数は 2 で止まる", font_size=24),
            self._line("既存の直線と異なる点で交わるとき、", MathTex(r"n", font_size=26, color=YELLOW), "本目は", MathTex(r"n", font_size=26, color=YELLOW), "個に切れて", MathTex(r"n", font_size=26), "増える", font_size=22),
            self._line(MathTex(r"R(n)=R(n-1)+n", font_size=26), "をほどくと", MathTex(r"R(n)=1+\dfrac{n(n+1)}{2}", font_size=26, color=YELLOW), font_size=22),
        ]
        shown = VGroup()
        for i, mob in enumerate(rows):
            if i == 0:
                self.below_chip(mob, chip, buff=0.32)
            else:
                self.stack_below(mob, shown, buff=0.20)
            self._fit_left(mob)
            self.play(FadeIn(mob), run_time=0.5)
            shown.add(mob)
            self.linger(3.2)

        related = self._line(
            "円",
            MathTex(r"n", font_size=22, color=GREY_B),
            "個で平面を切るときも、新しい円が既存の円といくつ交わるかで増え方が書けます。",
            font_size=20,
            color=GREY_B,
        )
        self.stack_below(related, shown, buff=0.28)
        self._fit_left(related)
        self.play(FadeIn(related), run_time=0.45)
        self.linger(related.text, extra=0.40)

    def _arrangement(self, specs, pieces_of=None, mark_origin=False, fills=False):
        hw = self.WIN_W / 2
        hh = self.WIN_H / 2
        frame = Rectangle(width=self.WIN_W, height=self.WIN_H, color=GREY_B, stroke_width=1.6)
        parts = [frame]
        if fills:
            upper = Polygon(
                np.array([-hw, 0, 0]),
                np.array([hw, 0, 0]),
                np.array([hw, hh, 0]),
                np.array([-hw, hh, 0]),
                color=BLUE,
                stroke_width=0,
            )
            upper.set_fill(BLUE, 0.28)
            lower = Polygon(
                np.array([-hw, 0, 0]),
                np.array([hw, 0, 0]),
                np.array([hw, -hh, 0]),
                np.array([-hw, -hh, 0]),
                color=TEAL,
                stroke_width=0,
            )
            lower.set_fill(TEAL, 0.28)
            parts.extend([upper, lower])

        colors = [BLUE_B, TEAL, ORANGE, PURPLE, GREEN]
        lines = []
        for i, (m, b) in enumerate(specs):
            seg = self._clipped_mb(m, b, color=colors[i % len(colors)])
            if seg is not None:
                parts.append(seg)
                lines.append((m, b))
        if mark_origin:
            parts.append(Dot(ORIGIN, radius=0.07, color=YELLOW))

        if pieces_of is not None and specs:
            idx = pieces_of if pieces_of >= 0 else len(specs) - 1
            m, b = specs[idx]
            others = [specs[j] for j in range(len(specs)) if j != idx]
            parts.extend(self._pieces(m, b, others))
        group = VGroup(*parts)
        return group

    def _clipped_mb(self, m, b, color=WHITE, stroke_width=3.0):
        pts = self._window_hits(m, b)
        if len(pts) < 2:
            return None
        return Line(pts[0], pts[1], color=color, stroke_width=stroke_width)

    def _window_hits(self, m, b):
        hw = self.WIN_W / 2 - 0.02
        hh = self.WIN_H / 2 - 0.02
        raw = []
        for x in (-hw, hw):
            y = m * x + b
            if abs(y) <= hh + 1e-6:
                raw.append(np.array([x, float(np.clip(y, -hh, hh)), 0.0]))
        if abs(m) > 1e-9:
            for y in (-hh, hh):
                x = (y - b) / m
                if abs(x) <= hw + 1e-6:
                    raw.append(np.array([float(np.clip(x, -hw, hw)), y, 0.0]))
        uniq = []
        for p in raw:
            if not any(np.linalg.norm(p - q) < 1e-4 for q in uniq):
                uniq.append(p)
        if len(uniq) < 2:
            return uniq
        uniq.sort(key=lambda p: float(p[0] if abs(m) < 8 else p[1]))
        return [uniq[0], uniq[-1]]

    def _pieces(self, m, b, others):
        hw = self.WIN_W / 2 - 0.04
        hh = self.WIN_H / 2 - 0.04
        xs = []
        for p in self._window_hits(m, b):
            xs.append(float(p[0]))
        for m2, b2 in others:
            if abs(m - m2) < 1e-8:
                continue
            x = (b2 - b) / (m - m2)
            y = m * x + b
            if abs(x) <= hw and abs(y) <= hh:
                xs.append(float(x))
        xs = sorted(set(round(x, 5) for x in xs))
        if len(xs) < 2:
            return []
        palette = [GOLD, GREEN, RED, BLUE, PINK]
        out = []
        for i in range(len(xs) - 1):
            x0, x1 = xs[i], xs[i + 1]
            if abs(x1 - x0) < 0.08:
                continue
            xm = 0.5 * (x0 + x1)
            y0, y1, ym = m * x0 + b, m * x1 + b, m * xm + b
            if abs(ym) > hh:
                continue
            color = palette[i % len(palette)]
            out.append(Line([x0, y0, 0], [x1, y1, 0], color=color, stroke_width=8))
            lab = MathTex(rf"{i + 1}", font_size=20, color=WHITE)
            # Offset the number off the line so it does not sit on the stroke.
            nrm = np.array([-m, 1.0, 0.0])
            nlen = np.linalg.norm(nrm)
            if nlen > 1e-8:
                nrm = nrm / nlen
            lab.move_to(np.array([xm, ym, 0.0]) + 0.22 * nrm)
            out.append(lab)
        return out

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
