from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import LessonScene


class PicksTheorem(LessonScene):
    """#6 格子点だけで多角形の面積は出るか（約7分）"""

    CELL = 0.50

    def construct(self):
        self.header = self._open_header()
        self.part_question()
        self.part_trial_halves()
        self.part_trial_subtract()
        self.part_step1_primitive()
        self.part_step2_rectangle()
        self.part_step3_split()
        self.part_step4_count()
        self.part_example()
        self.part_generalize()
        self.part_summary()

    def _xy(self, x, y):
        return x * self.CELL * RIGHT + y * self.CELL * UP

    def _open_header(self):
        title = self.ja_text("格子点だけで多角形の面積は出るか", font_size=36)
        self.play(FadeIn(title), run_time=0.8)
        self.linger(1.2)
        self.play(title.animate.scale(0.55).to_edge(UP, buff=0.16), run_time=0.5)
        return title

    def part_question(self):
        fig = self._lattice(
            4,
            3,
            poly=[(0, 0), (4, 0), (4, 2), (2, 3), (0, 2)],
            fill_color=BLUE,
        )
        fig.next_to(self.header, DOWN, buff=0.38)
        fig.set_x(0)
        self.play(FadeIn(fig), run_time=0.9)
        self.linger(3.2)

        q1 = self.ja_text("方眼紙に、頂点が格子点の多角形を描きます。", font_size=26)
        q1.next_to(fig, DOWN, buff=0.32)
        q1.set_x(0)
        self.play(FadeIn(q1), run_time=0.45)
        self.linger(q1.text)

        q2 = self.ja_text("内部の点の個数と、境界の点の個数だけで、面積は出るでしょうか。", font_size=26)
        self.stack_below(q2, q1, buff=0.16)
        q2.set_x(0)
        self._fit(q2, 13.0)
        q2.set_x(0)
        self.play(FadeIn(q2), run_time=0.45)
        self.linger(q2.text, extra=0.35)

    def part_trial_halves(self):
        self.wipe(self.header)
        chip = self.step_label("試行  半分ずつ")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("まず、三角形でマスを半分ずつ数えてみます。", font_size=24)
        self.below_chip(lead, chip, buff=0.22)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        fig = self._lattice(
            5,
            3,
            poly=[(0, 0), (5, 0), (2, 3)],
            fill_color=BLUE,
        )
        self.stack_below(fig, lead, buff=0.18)
        fig.to_edge(LEFT, buff=0.40)
        self._nudge(fig)
        self.play(FadeIn(fig), run_time=0.7)
        self.linger(3.2)

        rows = [
            MathTex(r"\dfrac{5\times 3}{2}=\dfrac{15}{2}", font_size=34, color=YELLOW),
            self.ja_text("完全に中に入るマスと、斜めに切られるマスが混ざる", font_size=20),
        ]
        block = VGroup(*rows).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        block.next_to(fig, RIGHT, buff=0.42)
        block.align_to(fig, UP)
        self._nudge(block)
        for row in rows:
            self.play(FadeIn(row), run_time=0.45)
            self.linger(3.2)

        shift = fig.anchor.get_center() - self._xy(0, 0)
        cells = [
            self._cell(2, 0, GREEN, 0.45).shift(shift),
            self._cell(3, 1, YELLOW, 0.40).shift(shift),
            self._cell(0, 0, ORANGE, 0.40).shift(shift),
            self._cell(1, 1, PURPLE, 0.40).shift(shift),
        ]
        labels = [
            self.ja_text("完全", font_size=18, color=GREEN),
            self.ja_text("半分", font_size=18, color=YELLOW),
            self.ja_text("斜め", font_size=18, color=ORANGE),
            self.ja_text("中途半端", font_size=18, color=PURPLE),
        ]
        legend = VGroup()
        for cell, lab in zip(cells, labels):
            if len(legend) == 0:
                lab.next_to(block, DOWN, buff=0.20)
                lab.align_to(block, LEFT)
            else:
                self.stack_below(lab, legend, buff=0.08)
            self.play(FadeIn(cell), FadeIn(lab), run_time=0.35)
            legend.add(lab)
            self.linger(3.2)

        notes = [
            self._line("面積", MathTex(r"\dfrac{15}{2}", font_size=26), "は底辺と高さならすぐ出ます。", font_size=22),
            self.ja_text("マスの切り口を全部追うと、場合分けが増えて止まります。", font_size=22),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                mob.to_edge(DOWN, buff=0.58)
            else:
                self.stack_below(mob, shown, buff=0.10)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.4)
            shown.add(mob)
            self.linger(3.2)

    def part_trial_subtract(self):
        self.wipe(self.header)
        chip = self.step_label("試行  欠けを引く")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("同じ三角形を、大きい長方形から欠けた分を引いてみます。", font_size=22)
        self.below_chip(lead, chip, buff=0.20)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        fig = self._lattice(
            5,
            3,
            poly=[(0, 0), (5, 0), (2, 3)],
            fill_color=BLUE,
            extras=[
                self._poly([(0, 0), (0, 3), (2, 3)], GREY_B, 0.28, dashed=True),
                self._poly([(5, 0), (5, 3), (2, 3)], GREY_A, 0.22, dashed=True),
            ],
        )
        calc = [
            MathTex(r"5\times 3=15", font_size=30),
            MathTex(r"\dfrac{2\times 3}{2}=3", font_size=28),
            MathTex(r"\dfrac{3\times 3}{2}=\dfrac{9}{2}", font_size=28),
            MathTex(r"15-3-\dfrac{9}{2}=\dfrac{15}{2}", font_size=32, color=YELLOW),
        ]
        calc_block = VGroup(*calc).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        pair = VGroup(fig, calc_block).arrange(RIGHT, buff=0.40, aligned_edge=UP)
        self.stack_below(pair, lead, buff=0.16)
        pair.set_x(0)
        self._nudge(pair)
        self.play(FadeIn(fig), run_time=0.6)
        for row in calc:
            self.play(FadeIn(row), run_time=0.4)
            self.linger(3.2)

        aligned = self.ja_text("頂点が軸に揃っているから、欠けが三角形になりました。", font_size=20)
        self.stack_below(aligned, pair, buff=0.16)
        aligned.set_x(0)
        self.play(FadeIn(aligned), run_time=0.4)
        self.linger(aligned.text)

        self.play(FadeOut(VGroup(fig, calc_block, aligned)), run_time=0.35)

        skewed = self._lattice(
            5,
            3,
            poly=[(0, 0), (5, 1), (1, 3)],
            fill_color=ORANGE,
            extras=[
                self._poly([(0, 0), (5, 0), (5, 1)], GREY_B, 0.30, dashed=True),
                self._poly([(0, 0), (0, 3), (1, 3)], GREY_B, 0.30, dashed=True),
                self._poly([(5, 1), (5, 3), (1, 3)], GREY_A, 0.22, dashed=True),
            ],
        )
        self.stack_below(skewed, lead, buff=0.16)
        skewed.set_x(0)
        self._nudge(skewed)
        self.play(FadeIn(skewed), run_time=0.7)
        self.linger(3.2)

        notes = [
            self.ja_text("欠けが 3 つ、形もバラバラ。多角形が変わるたびに場合分けが要ります。", font_size=22),
            self.ja_text("内部と境界の点の個数だけを数える道は、まだ見えていません。", font_size=22),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                mob.to_edge(DOWN, buff=0.56)
            else:
                self.stack_below(mob, shown, buff=0.10)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.4)
            shown.add(mob)
            self.linger(3.2)

    def part_step1_primitive(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 1  小さい三角形")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("格子点だけを頂点に持つ、いちばん小さい三角形から始めます。", font_size=22)
        self.below_chip(lead, chip, buff=0.22)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        fig = self._lattice(
            2,
            2,
            poly=[(0, 0), (1, 0), (0, 1)],
            interior=(),
            boundary=[(0, 0), (1, 0), (0, 1)],
            fill_color=BLUE,
        )
        self.stack_below(fig, lead, buff=0.20)
        fig.to_edge(LEFT, buff=0.55)
        self._nudge(fig)
        self.play(FadeIn(fig), run_time=0.7)
        self.linger(3.2)

        rows = [
            MathTex(r"\dfrac{1\times 1}{2}=\dfrac{1}{2}", font_size=32),
            self._line("内部の格子点は", MathTex(r"0", font_size=28, color=YELLOW), "個", font_size=22),
            self._line("境界の格子点は", MathTex(r"3", font_size=28, color=TEAL), "個", font_size=22),
            MathTex(r"I=0,\quad B=3", font_size=32),
            MathTex(r"I+\dfrac{B}{2}-1=0+\dfrac{3}{2}-1=\dfrac{1}{2}", font_size=30, color=YELLOW),
        ]
        block = VGroup(*rows).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        block.next_to(fig, RIGHT, buff=0.48)
        block.align_to(fig, UP)
        self._fit(block, 8.4)
        self._nudge(block)
        for row in rows:
            self.play(FadeIn(row), run_time=0.4)
            self.linger(3.2)
        self.linger(3.4)

        note = self._line(
            "この小さい三角形では、点の個数から面積",
            MathTex(r"\dfrac{1}{2}", font_size=26),
            "が出ました。",
            font_size=22,
        )
        note.to_edge(DOWN, buff=0.50)
        note.set_x(0)
        self.play(FadeIn(note), run_time=0.4)
        self.linger(3.2)

    def part_step2_rectangle(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 2  長方形")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("マスがそろった長方形でも、同じ計算をしてみます。", font_size=24)
        self.below_chip(lead, chip, buff=0.22)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        fig = self._lattice(
            3,
            2,
            poly=[(0, 0), (3, 0), (3, 2), (0, 2)],
            interior=[(1, 1), (2, 1)],
            boundary=[
                (0, 0),
                (1, 0),
                (2, 0),
                (3, 0),
                (3, 1),
                (3, 2),
                (2, 2),
                (1, 2),
                (0, 2),
                (0, 1),
            ],
            fill_color=TEAL,
        )
        self.stack_below(fig, lead, buff=0.20)
        fig.to_edge(LEFT, buff=0.45)
        self._nudge(fig)
        self.play(FadeIn(fig), run_time=0.7)
        self.linger(3.2)

        rows = [
            MathTex(r"3\times 2=6", font_size=32),
            MathTex(r"I=2", font_size=32, color=YELLOW),
            MathTex(r"B=10", font_size=32, color=TEAL),
            MathTex(r"I+\dfrac{B}{2}-1=2+\dfrac{10}{2}-1", font_size=30),
            MathTex(r"2+5-1=6", font_size=36, color=YELLOW),
        ]
        block = VGroup(*rows).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        block.next_to(fig, RIGHT, buff=0.50)
        block.align_to(fig, UP)
        self._nudge(block)
        for row in rows:
            self.play(FadeIn(row), run_time=0.4)
            self.linger(3.2)
        self.linger(3.4)

    def part_step3_split(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 3  分割")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("もう少し大きい三角形を、小さい三角形に分けます。", font_size=22)
        self.below_chip(lead, chip, buff=0.20)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        tris = [
            [(0, 0), (1, 0), (1, 1)],
            [(1, 0), (2, 0), (1, 1)],
            [(2, 0), (3, 0), (1, 1)],
            [(3, 0), (0, 2), (1, 1)],
            [(0, 2), (0, 1), (1, 1)],
            [(0, 1), (0, 0), (1, 1)],
        ]
        colors = [ORANGE, GOLD, GREEN, TEAL, BLUE, PURPLE]
        fig = self._lattice(
            3,
            2,
            poly=[(0, 0), (3, 0), (0, 2)],
            interior=[(1, 1)],
            boundary=[(0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (0, 2)],
            triangles=list(zip(tris, colors)),
            fill_color=BLUE,
        )
        self.stack_below(fig, lead, buff=0.16)
        fig.to_edge(LEFT, buff=0.40)
        self._nudge(fig)
        self.play(FadeIn(fig), run_time=0.8)
        self.linger(3.2)

        rows = [
            MathTex(r"\dfrac{3\times 2}{2}=3", font_size=30),
            MathTex(r"I=1", font_size=30, color=YELLOW),
            MathTex(r"B=6", font_size=30, color=TEAL),
            self._line("小さい三角形は 6 個。どれも面積", MathTex(r"\dfrac{1}{2}", font_size=24), font_size=20),
            MathTex(r"6\times\dfrac{1}{2}=3", font_size=34, color=YELLOW),
        ]
        block = VGroup(*rows).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        block.next_to(fig, RIGHT, buff=0.40)
        block.align_to(fig, UP)
        self._nudge(block)
        for row in rows:
            self.play(FadeIn(row), run_time=0.4)
            self.linger(3.2)
        self.linger(3.4)

    def part_step4_count(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 4  関係")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("小さい三角形の個数を、内部と境界の個数で書きます。", font_size=22)
        self.below_chip(lead, chip, buff=0.20)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        first = [
            MathTex(r"T=6", font_size=32),
            MathTex(r"S=\dfrac{T}{2}=3", font_size=32),
            MathTex(r"2I+B-2=2\times 1+6-2=6", font_size=30),
            self.ja_text("分割して数えると、この引き算が出る。", font_size=20),
        ]
        block1 = self._formula_rows(first, lead, buff=0.16)
        self.play(FadeOut(block1), run_time=0.3)

        second = [
            self.ja_text("長方形でも、小さい三角形でも、同じ関係になる。", font_size=20),
            MathTex(r"T=12,\quad 2I+B-2=4+10-2=12", font_size=28),
            MathTex(r"T=1,\quad 2I+B-2=0+3-2=1", font_size=28),
            MathTex(r"T=2I+B-2", font_size=34, color=GREEN),
            MathTex(r"S=\dfrac{T}{2}=I+\dfrac{B}{2}-1", font_size=36, color=YELLOW),
        ]
        block2 = self._formula_rows(second, lead, buff=0.14)
        self.linger(3.6)

    def part_example(self):
        self.wipe(self.header)
        chip = self.step_label("実例")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("問いの五角形で、内部と境界を最後まで数えます。", font_size=22)
        self.below_chip(lead, chip, buff=0.18)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        fig = self._lattice(
            4,
            3,
            poly=[(0, 0), (4, 0), (4, 2), (2, 3), (0, 2)],
            interior=[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2)],
            boundary=[
                (0, 0),
                (1, 0),
                (2, 0),
                (3, 0),
                (4, 0),
                (4, 1),
                (4, 2),
                (2, 3),
                (0, 2),
                (0, 1),
            ],
            fill_color=BLUE,
        )
        self.stack_below(fig, lead, buff=0.14)
        fig.to_edge(LEFT, buff=0.40)
        self._nudge(fig)
        self.play(FadeIn(fig), run_time=0.7)
        self.linger(3.2)

        rows = [
            MathTex(r"I=6", font_size=32, color=YELLOW),
            MathTex(r"B=10", font_size=32, color=TEAL),
            MathTex(r"I+\dfrac{B}{2}-1=6+\dfrac{10}{2}-1", font_size=28),
            MathTex(r"6+5-1=10", font_size=36, color=GREEN),
        ]
        block = VGroup(*rows).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        block.next_to(fig, RIGHT, buff=0.42)
        block.align_to(fig, UP)
        self._nudge(block)
        for row in rows:
            self.play(FadeIn(row), run_time=0.4)
            self.linger(3.2)
        self.linger(3.4)

        self.play(FadeOut(block), run_time=0.3)

        check = [
            self.ja_text("下の長方形と屋根", font_size=20),
            MathTex(r"4\times 2=8", font_size=30),
            MathTex(r"\dfrac{4\times 1}{2}=2", font_size=30),
            MathTex(r"8+2=10", font_size=34, color=GREEN),
        ]
        block2 = VGroup(*check).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        block2.next_to(fig, RIGHT, buff=0.42)
        block2.align_to(fig, UP)
        self._nudge(block2)
        for row in check:
            self.play(FadeIn(row), run_time=0.4)
            self.linger(3.2)
        self.linger(3.4)
        self.play(FadeOut(VGroup(fig, block2)), run_time=0.3)

        table = self.aligned_table(
            [
                [
                    self.ja_text("見方", font_size=16, color=GREY_B),
                    self.ja_text("面積", font_size=16, color=GREY_B),
                ],
                [
                    self.ja_text("点の個数", font_size=20),
                    MathTex(r"6+5-1=10", font_size=28, color=GREEN),
                ],
                [
                    self.ja_text("長方形と屋根", font_size=20),
                    MathTex(r"8+2=10", font_size=28, color=GREEN),
                ],
            ],
            h_buff=0.46,
            v_buff=0.14,
        )
        table.scale(0.92)
        self.stack_below(table, lead, buff=0.18)
        table.set_x(0)
        self.reveal_table(table, row_wait=0.85)

        notes = [
            self.ja_text("マスの切り口を追わなくても、格子点を数えると面積が出ました。", font_size=22),
            self.ja_text("内部と境界を数えてから、半分と 1 を足し引きします。", font_size=22),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, table, buff=0.16)
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

        lines = [
            self.ja_text("今やったことは、頂点が格子点の多角形の面積を、格子点の個数だけで書く考え方でした。", font_size=22),
            self._line("いちばん小さい三角形の面積は", MathTex(r"\dfrac{1}{2}", font_size=26), "。", font_size=22),
            self._line("分割すると、", MathTex(r"T=2I+B-2", font_size=26), "が出る。", font_size=22),
            self._line("だから面積は", MathTex(r"S=I+\dfrac{B}{2}-1", font_size=26), "。", font_size=22),
        ]
        shown = VGroup()
        for i, mob in enumerate(lines):
            if i == 0:
                self.below_chip(mob, chip, buff=0.30)
            else:
                self.stack_below(mob, shown, buff=0.20)
            self._fit_left(mob)
            self.play(FadeIn(mob), run_time=0.5)
            shown.add(mob)
            self.linger("今やったことは、頂点が格子点の多角形の面積を、格子点の個数だけで書く考え方でした。" if i == 0 else 3.2)

        name = self.ja_text("ピックの定理", font_size=26, color=GREY_B)
        self.stack_below(name, shown, buff=0.28)
        name.set_x(0)
        self.play(FadeIn(name), run_time=0.4)
        self.linger(name.text)

        ineq = MathTex(r"S=I+\dfrac{B}{2}-1", font_size=44, color=YELLOW)
        self.stack_below(ineq, name, buff=0.28)
        ineq.set_x(0)
        self.play(Write(ineq), run_time=1.0)
        self.linger(3.6)

    def part_summary(self):
        self.wipe(self.header)
        chip = self.step_label("まとめ")
        self.play(FadeIn(chip), run_time=0.35)

        rows = [
            self.ja_text("マスを半分ずつ数えると、切り口の場合分けが増える", font_size=24),
            self.ja_text("大きい長方形から欠けを引くと、形が変わるたびに場合分けが要る", font_size=24),
            self._line("いちばん小さい三角形の面積は", MathTex(r"\dfrac{1}{2}", font_size=28), font_size=24),
            self._line("内部", MathTex(r"I", font_size=28, color=YELLOW), "と境界", MathTex(r"B", font_size=28, color=TEAL), "で", MathTex(r"S=I+\dfrac{B}{2}-1", font_size=28, color=YELLOW), font_size=24),
        ]
        shown = VGroup()
        for i, mob in enumerate(rows):
            if i == 0:
                self.below_chip(mob, chip, buff=0.36)
            else:
                self.stack_below(mob, shown, buff=0.24)
            self._fit_left(mob)
            self.play(FadeIn(mob), run_time=0.5)
            shown.add(mob)
            self.linger(3.2)

        related = self.ja_text(
            "穴のあいた多角形でも、外側と内側の格子点を足し引きすると、面積が書けます。",
            font_size=22,
            color=GREY_B,
        )
        self.stack_below(related, shown, buff=0.34)
        self._fit_left(related)
        self.play(FadeIn(related), run_time=0.45)
        self.linger(related.text, extra=0.45)

    def _cell(self, x, y, color, opacity):
        bl = self._xy(x, y)
        poly = Polygon(
            bl,
            bl + self.CELL * RIGHT,
            bl + self.CELL * RIGHT + self.CELL * UP,
            bl + self.CELL * UP,
            color=color,
            stroke_width=1.5,
        )
        poly.set_fill(color, opacity)
        return poly

    def _poly(self, verts, color, opacity, dashed=False):
        pts = [self._xy(x, y) for x, y in verts]
        if dashed:
            mob = DashedVMobject(Polygon(*pts, color=color, stroke_width=2), num_dashes=24)
            fill = Polygon(*pts, color=color, stroke_width=0)
            fill.set_fill(color, opacity)
            return VGroup(fill, mob)
        poly = Polygon(*pts, color=color, stroke_width=3)
        poly.set_fill(color, opacity)
        return poly

    def _lattice(
        self,
        xmax,
        ymax,
        poly=None,
        interior=None,
        boundary=None,
        triangles=None,
        extras=None,
        fill_color=BLUE,
        xmin=0,
        ymin=0,
    ):
        parts = []
        for x in range(xmin, xmax + 1):
            parts.append(Line(self._xy(x, ymin), self._xy(x, ymax), color=GREY_D, stroke_width=1.2))
        for y in range(ymin, ymax + 1):
            parts.append(Line(self._xy(xmin, y), self._xy(xmax, y), color=GREY_D, stroke_width=1.2))
        for x in range(xmin, xmax + 1):
            for y in range(ymin, ymax + 1):
                parts.append(Dot(self._xy(x, y), radius=0.035, color=GREY_C))

        if extras:
            parts.extend(extras)
        if triangles:
            for i, (verts, color) in enumerate(triangles, 1):
                parts.append(self._poly(verts, color, 0.28))
                cx = sum(v[0] for v in verts) / 3
                cy = sum(v[1] for v in verts) / 3
                parts.append(
                    MathTex(rf"{i}", font_size=18, color=WHITE).move_to(self._xy(cx, cy))
                )
        if poly:
            parts.append(self._poly(poly, fill_color, 0.16 if not triangles else 0.0))

        if interior:
            for x, y in interior:
                parts.append(Dot(self._xy(x, y), radius=0.08, color=YELLOW))
        if boundary:
            for x, y in boundary:
                parts.append(Dot(self._xy(x, y), radius=0.08, color=TEAL))
        group = VGroup(*parts)
        n_v = xmax - xmin + 1
        n_h = ymax - ymin + 1
        group.anchor = parts[n_v + n_h]
        return group

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
        block = VGroup(*rows).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
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
