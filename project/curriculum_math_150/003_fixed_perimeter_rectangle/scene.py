from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import LessonScene


class FixedPerimeterRectangle(LessonScene):
    """#3 周が同じなら、いちばん広い長方形は（約7分）"""

    UNIT = 0.30

    def construct(self):
        self.header = self._open_header()
        self.part_question()
        self.part_trial_skinny()
        self.part_trial_integers()
        self.part_step1_symbols()
        self.part_step2_square()
        self.part_step3_amgm()
        self.part_step4_move()
        self.part_example()
        self.part_generalize()
        self.part_summary()

    def _open_header(self):
        title = self.ja_text("周が同じなら、いちばん広い長方形は", font_size=36)
        self.play(FadeIn(title), run_time=0.8)
        self.linger(1.2)
        self.play(title.animate.scale(0.55).to_edge(UP, buff=0.16), run_time=0.5)
        return title

    def part_question(self):
        left = self._labeled_rect(2, 8, MathTex(r"x", font_size=26, color=ORANGE), MathTex(r"y", font_size=26, color=YELLOW))
        right = self._labeled_rect(4, 6, MathTex(r"x", font_size=26, color=ORANGE), MathTex(r"y", font_size=26, color=YELLOW))
        pair = VGroup(left, right).arrange(RIGHT, buff=1.1, aligned_edge=DOWN)
        pair.next_to(self.header, DOWN, buff=0.45)
        pair.set_x(0)
        self.play(FadeIn(left), run_time=0.6)
        self.play(FadeIn(right), run_time=0.6)
        self.linger(3.2)

        q1 = self.ja_text("同じ長さのひもで、長方形の畑を囲います。", font_size=26)
        q1.next_to(pair, DOWN, buff=0.38)
        q1.set_x(0)
        self.play(FadeIn(q1), run_time=0.45)
        self.linger(q1.text)

        q2 = self.ja_text("周が同じなら、いちばん広い縦横は何でしょう。", font_size=26)
        self.stack_below(q2, q1, buff=0.18)
        q2.set_x(0)
        self.play(FadeIn(q2), run_time=0.45)
        self.linger(q2.text, extra=0.35)

    def part_trial_skinny(self):
        self.wipe(self.header)
        chip = self.step_label("試行  細長い")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("まず、極端に細長い長方形を描いてみます。", font_size=26)
        self.below_chip(lead, chip, buff=0.28)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        cond = self._line(
            "周",
            MathTex(r"2(x+y)=20", font_size=32),
            "、つまり",
            MathTex(r"x+y=10", font_size=32, color=YELLOW),
            font_size=24,
        )
        self.stack_below(cond, lead, buff=0.22)
        cond.set_x(0)
        self.play(FadeIn(cond), run_time=0.45)
        self.linger(3.2)

        shown = None
        for x, y, prod in ((1, 9, 9), (2, 8, 16), (3, 7, 21)):
            fig = self._labeled_rect(
                x,
                y,
                MathTex(str(x), font_size=26, color=ORANGE),
                MathTex(str(y), font_size=26, color=YELLOW),
            )
            area = self._line("面積", MathTex(rf"{x}\times {y}={prod}", font_size=32, color=GREEN), font_size=24)
            row = VGroup(fig, area).arrange(RIGHT, buff=0.55, aligned_edge=DOWN)
            self.stack_below(row, cond, buff=0.32)
            row.set_x(0)
            overflow = (-config.frame_width / 2 + 0.08) - row.get_left()[0]
            if overflow > 0:
                row.shift(RIGHT * overflow)
            if shown is None:
                self.play(FadeIn(row), run_time=0.7)
            else:
                self.play(ReplacementTransform(shown, row), run_time=0.85)
            shown = row
            self.linger(3.2)

        notes = [
            self.ja_text("細長いほど、面積は小さいです。", font_size=24),
            self.ja_text("正方形に近づけると、増えていきます。", font_size=24),
        ]
        shown_n = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                mob.to_edge(DOWN, buff=0.72)
            else:
                self.stack_below(mob, shown_n, buff=0.12)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.4)
            shown_n.add(mob)
            self.linger(mob.text)

    def part_trial_integers(self):
        self.wipe(self.header)
        chip = self.step_label("試行  整数")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("横を整数にして、面積を全部書いてみます。", font_size=26)
        self.below_chip(lead, chip, buff=0.28)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        calc = [
            MathTex(r"y=10-4=6", font_size=34),
            MathTex(r"4\times 6=24", font_size=34, color=YELLOW),
        ]
        calc_block = self._formula_rows(calc, lead, buff=0.26)
        self.play(FadeOut(calc_block), run_time=0.3)

        table = self.aligned_table(
            [
                [
                    self._line("横", MathTex(r"x", font_size=24, color=GREY_B), font_size=18, color=GREY_B),
                    self._line("縦", MathTex(r"10-x", font_size=24, color=GREY_B), font_size=18, color=GREY_B),
                    self._line("面積", MathTex(r"xy", font_size=24, color=GREY_B), font_size=18, color=GREY_B),
                ],
                [MathTex(r"1", font_size=28), MathTex(r"9", font_size=28), MathTex(r"9", font_size=28)],
                [MathTex(r"2", font_size=28), MathTex(r"8", font_size=28), MathTex(r"16", font_size=28)],
                [MathTex(r"3", font_size=28), MathTex(r"7", font_size=28), MathTex(r"21", font_size=28)],
                [MathTex(r"4", font_size=28), MathTex(r"6", font_size=28), MathTex(r"24", font_size=28)],
                [MathTex(r"5", font_size=28, color=GREEN), MathTex(r"5", font_size=28, color=GREEN), MathTex(r"25", font_size=28, color=GREEN)],
                [MathTex(r"6", font_size=28), MathTex(r"4", font_size=28), MathTex(r"24", font_size=28)],
            ],
            h_buff=0.42,
            v_buff=0.14,
        )
        table.scale(0.82)
        self.stack_below(table, lead, buff=0.22)
        table.set_x(0)
        self.reveal_table(table, row_wait=0.85)

        notes = [
            self._line("整数では、", MathTex(r"5", font_size=26), "と", MathTex(r"5", font_size=26), "がいちばん大きい。", font_size=22),
            self.ja_text("でも整数以外は試していません。", font_size=22),
            self._line(MathTex(r"4.5", font_size=26), "と", MathTex(r"5.5", font_size=26), "の方が、大きいかもしれません。", font_size=22),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, table, buff=0.18)
            else:
                self.stack_below(mob, shown, buff=0.10)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.4)
            shown.add(mob)
            self.linger(3.2)

    def part_step1_symbols(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 1  記号")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("周が決まっている、ということを式にします。", font_size=26)
        self.below_chip(lead, chip, buff=0.30)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        rows = [
            self._line("横を", MathTex(r"x", font_size=32), "、縦を", MathTex(r"y", font_size=32), "と書く", font_size=24),
            MathTex(r"2(x+y)=L", font_size=36),
            MathTex(r"x+y=\dfrac{L}{2}", font_size=36),
            self._line("この和を", MathTex(r"s", font_size=32, color=YELLOW), "とおく。", MathTex(r"s=L/2", font_size=32, color=YELLOW), font_size=24),
            MathTex(r"S=xy=x(s-x)", font_size=40, color=GREEN),
        ]
        self._formula_rows(rows, lead, buff=0.22)
        self.linger(3.4)

        note = self._line(
            "残る問いは、",
            MathTex(r"x", font_size=28),
            "を動かしたとき",
            MathTex(r"S", font_size=28),
            "がいちばん大きくなる場所です。",
            font_size=22,
        )
        note.to_edge(DOWN, buff=0.36)
        note.set_x(0)
        self._fit(note, 13.0)
        note.set_x(0)
        self.play(FadeIn(note), run_time=0.4)
        self.linger("残る問いは、x を動かしたとき S がいちばん大きくなる場所です。", extra=0.3)

    def part_step2_square(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 2  平方完成")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("二次式を、平方の差の形に直します。", font_size=26)
        self.below_chip(lead, chip, buff=0.28)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        first = [
            MathTex(r"S=x(s-x)", font_size=36),
            MathTex(r"S=sx-x^2", font_size=36),
            MathTex(r"S=-(x^2-sx)", font_size=36),
            self._line(
                MathTex(r"x^2-sx", font_size=32),
                "に",
                MathTex(r"(s/2)^2", font_size=32),
                "を足して引く",
                font_size=24,
            ),
        ]
        block1 = self._formula_rows(first, lead, buff=0.22)
        self.play(FadeOut(block1), run_time=0.3)

        second = [
            MathTex(r"S=-\bigl(x^2-sx+(s/2)^2-(s/2)^2\bigr)", font_size=34),
            MathTex(r"S=-\bigl((x-s/2)^2-s^2/4\bigr)", font_size=34),
            MathTex(r"S=\dfrac{s^2}{4}-(x-s/2)^2", font_size=40, color=YELLOW),
        ]
        block2 = self._formula_rows(second, lead, buff=0.22)
        self.linger(3.5)

        self.play(FadeOut(block2), run_time=0.3)
        obs = [
            self._line(MathTex(r"(x-s/2)^2", font_size=30), "は 0 以上", font_size=24),
            self._line("だから", MathTex(r"S", font_size=30), "は", MathTex(r"s^2/4", font_size=30), "を超えない", font_size=24),
            self._line("差が 0 になるのは", MathTex(r"x=s/2", font_size=30, color=YELLOW), "のとき", font_size=24),
            MathTex(r"y=s-x=s/2", font_size=36, color=YELLOW),
        ]
        self._formula_rows(obs, lead, buff=0.20)

        note = self.ja_text("いちばん広いのは、横と縦が等しいときです。正方形です。", font_size=24)
        note.to_edge(DOWN, buff=0.32)
        note.set_x(0)
        self.play(FadeIn(note), run_time=0.4)
        self.linger(note.text, extra=0.35)

    def part_step3_amgm(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 3  相加相乗")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("同じ結論を、平方が 0 以上であることからも出せます。", font_size=24)
        self.below_chip(lead, chip, buff=0.28)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        pos = self._line(
            MathTex(r"x>0", font_size=28),
            "、",
            MathTex(r"y>0", font_size=28),
            "として進みます。",
            font_size=22,
        )
        self.stack_below(pos, lead, buff=0.18)
        self._fit_left(pos)
        self.play(FadeIn(pos), run_time=0.4)
        self.linger("x>0、y>0 として進みます。")

        first = [
            MathTex(r"\bigl(\sqrt{x}-\sqrt{y}\bigr)^2\ge 0", font_size=36, color=YELLOW),
            MathTex(r"x+y-2\sqrt{xy}\ge 0", font_size=34),
            MathTex(r"x+y\ge 2\sqrt{xy}", font_size=34),
            self._line("両辺は 0 以上なので、2 で割る。", font_size=22),
            MathTex(r"\dfrac{x+y}{2}\ge\sqrt{xy}", font_size=36),
        ]
        block1 = self._formula_rows(first, pos, buff=0.18)
        kept = first[-1]
        self.play(*[FadeOut(row) for row in first[:-1]], run_time=0.3)
        self.play(kept.animate.next_to(pos, DOWN, buff=0.22).set_x(0), run_time=0.4)

        second = [
            self.ja_text("両辺は 0 以上なので、平方してよい。", font_size=22),
            MathTex(r"\left(\dfrac{x+y}{2}\right)^2\ge xy", font_size=36),
            MathTex(r"\dfrac{s^2}{4}\ge S", font_size=40, color=GREEN),
            self._line("等号は", MathTex(r"\sqrt{x}=\sqrt{y}", font_size=30), "のとき。よって", MathTex(r"x=y", font_size=30, color=YELLOW), font_size=22),
        ]
        self._formula_rows(second, kept, buff=0.18)
        self.linger(3.5)

    def part_step4_move(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 4  動かす")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("周を保ったまま、横を動かします。", font_size=26)
        self.below_chip(lead, chip, buff=0.28)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        shown = None
        for x, y, area_tex in (
            (2, 8, r"S=x(s-x)"),
            (5, 5, r"S=s^2/4"),
            (8, 2, r"S=x(s-x)"),
        ):
            w_sym = MathTex(r"s/2", font_size=26, color=ORANGE) if x == 5 else MathTex(r"x", font_size=26, color=ORANGE)
            h_sym = MathTex(r"s/2", font_size=26, color=YELLOW) if x == 5 else MathTex(r"s-x", font_size=26, color=YELLOW)
            fig = self._labeled_rect(x, y, w_sym, h_sym)
            area = MathTex(area_tex, font_size=36, color=GREEN)
            row = VGroup(fig, area).arrange(RIGHT, buff=0.55, aligned_edge=DOWN)
            self.stack_below(row, lead, buff=0.35)
            row.set_x(-0.4)
            overflow = (-config.frame_width / 2 + 0.08) - row.get_left()[0]
            if overflow > 0:
                row.shift(RIGHT * overflow)
            if shown is None:
                self.play(FadeIn(row), run_time=0.7)
            else:
                self.play(ReplacementTransform(shown, row), run_time=0.9)
            shown = row
            self.linger(3.2)

        result = [
            self._line("細長いと", MathTex(r"(x-s/2)^2", font_size=30), "が大きいので", MathTex(r"S", font_size=30), "は小さい", font_size=22),
            self._line(MathTex(r"x=s/2", font_size=30), "で差が消え、", MathTex(r"S=s^2/4", font_size=30, color=GREEN), font_size=22),
            self.ja_text("反対側へ行き過ぎても、また小さくなる", font_size=22),
        ]
        block = VGroup(*result).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        self.stack_below(block, shown, buff=0.28)
        block.set_x(0)
        for row in result:
            self.play(FadeIn(row), run_time=0.4)
            self.linger(3.2)

    def part_example(self):
        self.wipe(self.header)
        chip = self.step_label("実例")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("周 20 のひもで、整数で止まった疑いを、式で確かめます。", font_size=24)
        self.below_chip(lead, chip, buff=0.26)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        calc = [
            MathTex(r"y=10-4.5=5.5", font_size=32),
            MathTex(r"4.5\times 5.5=4.5\times(5+0.5)", font_size=32),
            MathTex(r"4.5\times 5=22.5", font_size=32),
            MathTex(r"4.5\times 0.5=2.25", font_size=32),
            MathTex(r"22.5+2.25=24.75", font_size=32, color=YELLOW),
        ]
        calc_block = self._formula_rows(calc, lead, buff=0.16)
        self.play(FadeOut(calc_block), run_time=0.3)

        close = [
            MathTex(r"5\times 5=25", font_size=34, color=GREEN),
            MathTex(r"25-24.75=0.25=(4.5-5)^2", font_size=34),
            MathTex(r"S=25-(x-5)^2", font_size=40, color=YELLOW),
        ]
        close_block = self._formula_rows(close, lead, buff=0.18)
        self.linger(3.4)
        self.play(FadeOut(close_block), run_time=0.3)

        table = self.aligned_table(
            [
                [
                    self._line("横", MathTex(r"x", font_size=22, color=GREY_B), font_size=16, color=GREY_B),
                    self._line("縦", MathTex(r"10-x", font_size=22, color=GREY_B), font_size=16, color=GREY_B),
                    self._line("面積", MathTex(r"xy", font_size=22, color=GREY_B), font_size=16, color=GREY_B),
                ],
                [MathTex(r"4", font_size=28), MathTex(r"6", font_size=28), MathTex(r"24", font_size=28)],
                [MathTex(r"4.5", font_size=28), MathTex(r"5.5", font_size=28), MathTex(r"24.75", font_size=28)],
                [MathTex(r"5", font_size=28, color=GREEN), MathTex(r"5", font_size=28, color=GREEN), MathTex(r"25", font_size=28, color=GREEN)],
                [MathTex(r"5.5", font_size=28), MathTex(r"4.5", font_size=28), MathTex(r"24.75", font_size=28)],
                [MathTex(r"6", font_size=28), MathTex(r"4", font_size=28), MathTex(r"24", font_size=28)],
            ],
            h_buff=0.40,
            v_buff=0.14,
        )
        table.scale(0.84)
        self.stack_below(table, lead, buff=0.20)
        table.set_x(0)
        self.reveal_table(table, row_wait=0.8)

        notes = [
            self._line("面積", MathTex(r"24.75", font_size=26), "は", MathTex(r"25", font_size=26), "より小さい。", font_size=22),
            self.ja_text("ずれの平方のぶんだけ、面積が落ちます。", font_size=22),
            self.ja_text("周 20 なら、いちばん広いのは 5 かける 5 の正方形です。", font_size=22),
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
            self.ja_text("今やったことは、平方完成と、相加相乗平均の不等式でした。", font_size=24),
            self._line(
                "和",
                MathTex(r"x+y", font_size=30),
                "が一定なら、積",
                MathTex(r"xy", font_size=30),
                "は",
                MathTex(r"x=y", font_size=30),
                "のとき最大です。",
                font_size=22,
            ),
            self.ja_text("相加平均は相乗平均以上。等号は二つの数が等しいときです。", font_size=24),
            self.ja_text("制約の下でいちばんよい値を探す、という型でもあります。", font_size=24),
        ]
        linger_texts = [
            "今やったことは、平方完成と、相加相乗平均の不等式でした。",
            "和 x+y が一定なら、積 xy は x=y のとき最大です。",
            "相加平均は相乗平均以上。等号は二つの数が等しいときです。",
            "制約の下でいちばんよい値を探す、という型でもあります。",
        ]
        shown = VGroup()
        for i, (mob, text) in enumerate(zip(lines, linger_texts)):
            if i == 0:
                self.below_chip(mob, chip, buff=0.32)
            else:
                self.stack_below(mob, shown, buff=0.22)
            self._fit_left(mob)
            self.play(FadeIn(mob), run_time=0.5)
            shown.add(mob)
            self.linger(text)

        ineq = MathTex(
            r"\dfrac{x+y}{2}\ge\sqrt{xy},\qquad xy\le\left(\dfrac{x+y}{2}\right)^2",
            font_size=36,
            color=YELLOW,
        )
        self.stack_below(ineq, shown, buff=0.36)
        ineq.set_x(0)
        self._fit(ineq, 12.8)
        ineq.set_x(0)
        self.play(Write(ineq), run_time=1.1)
        self.linger(3.6)

    def part_summary(self):
        self.wipe(self.header)
        chip = self.step_label("まとめ")
        self.play(FadeIn(chip), run_time=0.35)

        rows = [
            self.ja_text("周が一定なら、横と縦の和が一定", font_size=24),
            self.ja_text("細長い長方形は面積が小さい。整数だけ試すと、正方形の隣が疑わしく残る", font_size=24),
            self.ja_text("平方完成すると、ずれの平方のぶんだけ面積が落ちる", font_size=24),
            self.ja_text("だからいちばん広い長方形は正方形", font_size=24),
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
            self.linger(3.2)

        related = self.ja_text("周が同じでも、長方形に限らなければ、もっと広い形があります。", font_size=22, color=GREY_B)
        self.stack_below(related, shown, buff=0.36)
        self._fit_left(related)
        self.play(FadeIn(related), run_time=0.45)
        self.linger(related.text, extra=0.45)

    def _labeled_rect(self, width, height, w_tex, h_tex):
        rect = Rectangle(
            width=width * self.UNIT,
            height=height * self.UNIT,
            color=TEAL,
            stroke_width=3,
        )
        rect.set_fill(TEAL, 0.38)
        w_brace = Brace(rect, DOWN, color=ORANGE, buff=0.12)
        w_lab = self._line("横", w_tex, font_size=20, color=ORANGE)
        w_brace.put_at_tip(w_lab)
        h_brace = Brace(rect, LEFT, color=YELLOW, buff=0.12)
        h_lab = self._line("縦", h_tex, font_size=20, color=YELLOW)
        h_brace.put_at_tip(h_lab)
        group = VGroup(rect, w_brace, w_lab, h_brace, h_lab)
        group.rect = rect
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
        block = VGroup(*rows).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
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
