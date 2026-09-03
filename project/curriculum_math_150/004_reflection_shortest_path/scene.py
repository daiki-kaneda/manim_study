from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import LessonScene


class ReflectionShortestPath(LessonScene):
    """#4 鏡を使った最短経路（約7分）"""

    SCALE = 0.38
    AX, AY = 0.0, 6.0
    BX, BY = 8.0, 2.0

    def construct(self):
        self.header = self._open_header()
        self.part_question()
        self.part_trial_near_b()
        self.part_trial_samples()
        self.part_step1_length()
        self.part_step2_reflect()
        self.part_step3_straight()
        self.part_step4_angles()
        self.part_example()
        self.part_generalize()
        self.part_summary()

    def _xy(self, wx, wy):
        return wx * self.SCALE * RIGHT + wy * self.SCALE * UP

    def _open_header(self):
        title = self.ja_text("鏡を使った最短経路", font_size=40)
        self.play(FadeIn(title), run_time=0.8)
        self.linger(1.2)
        self.play(title.animate.scale(0.55).to_edge(UP, buff=0.16), run_time=0.5)
        return title

    def part_question(self):
        fig = self._base_figure(p_x=4.0, path_opacity=0.55)
        fig.next_to(self.header, DOWN, buff=0.38)
        fig.set_x(0)
        self.play(FadeIn(fig), run_time=0.9)
        self.linger(3.2)

        q1 = self._line(
            "川に一度だけ触れて、",
            MathTex(r"A", font_size=28),
            "から",
            MathTex(r"B", font_size=28),
            "へ行きます。",
            font_size=26,
        )
        q1.next_to(fig, DOWN, buff=0.34)
        q1.set_x(0)
        self.play(FadeIn(q1), run_time=0.45)
        self.linger("川に一度だけ触れて、A から B へ行きます。")

        q2 = self.ja_text("触れる場所をどこに取ると、道がいちばん短くなるでしょう。", font_size=26)
        self.stack_below(q2, q1, buff=0.16)
        q2.set_x(0)
        self.play(FadeIn(q2), run_time=0.45)
        self.linger(q2.text, extra=0.35)

    def part_trial_near_b(self):
        self.wipe(self.header)
        chip = self.step_label("試行  近いほう")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self._line(
            MathTex(r"B", font_size=28),
            "のほうが川に近いので、",
            MathTex(r"B", font_size=28),
            "の真下で触れると短そうに見えます。",
            font_size=24,
        )
        self.below_chip(lead, chip, buff=0.26)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger("B のほうが川に近いので、B の真下で触れると短そうに見えます。")

        fig = self._base_figure(p_x=8.0, ap_len=r"10", pb_len=r"2")
        self.stack_below(fig, lead, buff=0.28)
        fig.to_edge(LEFT, buff=0.45)
        self._nudge(fig)
        self.play(FadeIn(fig), run_time=0.7)
        self.linger(3.2)

        rows = [
            MathTex(r"A=(0,6),\ B=(8,2),\ P=(8,0)", font_size=28),
            MathTex(r"AP=\sqrt{8^2+6^2}=\sqrt{64+36}=\sqrt{100}=10", font_size=28),
            MathTex(r"PB=2", font_size=30),
            MathTex(r"10+2=12", font_size=36, color=YELLOW),
        ]
        block = VGroup(*rows).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        block.next_to(fig, RIGHT, buff=0.38)
        block.align_to(fig, UP)
        self._fit(block, 8.4)
        self._nudge(block)
        for row in rows:
            self.play(FadeIn(row), run_time=0.45)
            self.linger(3.2)

        notes = [
            self.ja_text("近いほうの真下は、短そうに見えます。", font_size=22),
            self.ja_text("でも、ほかの場所と比べていません。", font_size=22),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                mob.to_edge(DOWN, buff=0.62)
            else:
                self.stack_below(mob, shown, buff=0.10)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.4)
            shown.add(mob)
            self.linger(mob.text)

    def part_trial_samples(self):
        self.wipe(self.header)
        chip = self.step_label("試行  いくつか試す")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("触れる点の横座標を動かして、長さを足してみます。", font_size=24)
        self.below_chip(lead, chip, buff=0.24)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        fig = self._base_figure(p_x=4.0, ap_len=r"7.211", pb_len=r"4.472")
        calc = [
            MathTex(r"P=(4,0)", font_size=28, color=ORANGE),
            MathTex(r"AP=\sqrt{4^2+6^2}=\sqrt{16+36}=\sqrt{52}", font_size=26),
            MathTex(r"\sqrt{52}=\sqrt{4\cdot 13}=2\sqrt{13}\approx 7.211", font_size=26),
            MathTex(r"PB=\sqrt{4^2+2^2}=\sqrt{16+4}=\sqrt{20}", font_size=26),
            MathTex(r"\sqrt{20}=\sqrt{4\cdot 5}=2\sqrt{5}\approx 4.472", font_size=26),
            MathTex(r"7.211+4.472=11.683", font_size=32, color=YELLOW),
        ]
        calc_block = VGroup(*calc).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        pair = VGroup(fig, calc_block).arrange(RIGHT, buff=0.42, aligned_edge=UP)
        self.stack_below(pair, lead, buff=0.18)
        pair.set_x(0)
        self._nudge(pair)
        self.play(FadeIn(fig), run_time=0.55)
        for row in calc:
            self.play(FadeIn(row), run_time=0.4)
            self.linger(3.2)

        self.play(FadeOut(pair), run_time=0.3)

        table = self.aligned_table(
            [
                [
                    self._line(
                        MathTex(r"P", font_size=22, color=GREY_B),
                        "の横",
                        MathTex(r"x", font_size=22, color=GREY_B),
                        font_size=16,
                        color=GREY_B,
                    ),
                    MathTex(r"AP", font_size=22, color=GREY_B),
                    MathTex(r"PB", font_size=22, color=GREY_B),
                    self.ja_text("合計", font_size=16, color=GREY_B),
                ],
                [MathTex(r"0", font_size=26), MathTex(r"6", font_size=26), MathTex(r"8.246", font_size=26), MathTex(r"14.246", font_size=26)],
                [MathTex(r"2", font_size=26), MathTex(r"6.325", font_size=26), MathTex(r"6.325", font_size=26), MathTex(r"12.649", font_size=26)],
                [
                    MathTex(r"4", font_size=26, color=YELLOW),
                    MathTex(r"7.211", font_size=26, color=YELLOW),
                    MathTex(r"4.472", font_size=26, color=YELLOW),
                    MathTex(r"11.683", font_size=26, color=YELLOW),
                ],
                [MathTex(r"8", font_size=26), MathTex(r"10", font_size=26), MathTex(r"2", font_size=26), MathTex(r"12", font_size=26)],
            ],
            h_buff=0.34,
            v_buff=0.12,
        )
        table.scale(0.86)
        self.stack_below(table, lead, buff=0.2)
        table.set_x(0)
        self.reveal_table(table, row_wait=0.85)

        notes = [
            self._line("試した中では", MathTex(r"x=4", font_size=26), "がいちばん短い。", font_size=22),
            self.ja_text("B の真下より短いので、近いほう仮説は破綻します。", font_size=22),
            self._line(
                MathTex(r"4", font_size=26),
                "と",
                MathTex(r"8", font_size=26),
                "のあいだは、まだ調べていません。",
                font_size=22,
            ),
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

    def part_step1_length(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 1  長さ")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self._line(
            "触れる点を",
            MathTex(r"P=(x,0)", font_size=28),
            "とおいて、長さを式にします。",
            font_size=24,
        )
        self.below_chip(lead, chip, buff=0.28)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger("触れる点を P=(x,0) とおいて、長さを式にします。")

        rows = [
            MathTex(r"A=(0,a),\quad B=(c,b)", font_size=32),
            MathTex(r"AP=\sqrt{x^2+a^2}", font_size=34),
            MathTex(r"PB=\sqrt{(c-x)^2+b^2}", font_size=34),
            MathTex(r"L(x)=\sqrt{x^2+a^2}+\sqrt{(c-x)^2+b^2}", font_size=34, color=GREEN),
        ]
        self._formula_rows(rows, lead, buff=0.2)
        self.linger(3.4)

        notes = [
            self._line(
                "このまま",
                MathTex(r"x", font_size=26),
                "で微分してもよいのですが、計算が重いです。",
                font_size=22,
            ),
            self.ja_text("図のほうで、同じ長さを作り変えます。", font_size=22),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                mob.to_edge(DOWN, buff=0.62)
            else:
                self.stack_below(mob, shown, buff=0.10)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.4)
            shown.add(mob)
            self.linger(3.2)

    def part_step2_reflect(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 2  折り返す")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self._line(
            MathTex(r"B", font_size=28),
            "を、川に対して反対側へ折り返します。",
            font_size=24,
        )
        self.below_chip(lead, chip, buff=0.22)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger("B を、川に対して反対側へ折り返します。")

        fig = self._base_figure(p_x=4.0, show_b_prime=True)
        self.stack_below(fig, lead, buff=0.16)
        fig.to_edge(LEFT, buff=0.38)
        self._nudge(fig)
        self.play(FadeIn(fig), run_time=0.8)
        self.linger(3.2)

        rows = [
            self._line(
                MathTex(r"H", font_size=26),
                "は",
                MathTex(r"BB'", font_size=26),
                "の中点で、川の上にある",
                font_size=20,
            ),
            MathTex(r"BH=B'H", font_size=28),
            self._line(
                "角",
                MathTex(r"BHP", font_size=24),
                "と角",
                MathTex(r"B'HP", font_size=24),
                "は直角。",
                MathTex(r"HP", font_size=24),
                "は共通",
                font_size=18,
            ),
            self._line(
                "直角三角形",
                MathTex(r"BHP", font_size=24),
                "と",
                MathTex(r"B'HP", font_size=24),
                "は合同",
                font_size=20,
            ),
            MathTex(r"BP=B'P", font_size=36, color=YELLOW),
        ]
        block = VGroup(*rows).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        block.next_to(fig, RIGHT, buff=0.32)
        block.align_to(fig, UP)
        self._fit(block, 7.8)
        self._nudge(block)
        for row in rows:
            self.play(FadeIn(row), run_time=0.45)
            self.linger(3.2)

        notes = [
            self._line(
                "どの",
                MathTex(r"P", font_size=24),
                "でも、川の上なら",
                MathTex(r"BP=B'P", font_size=24),
                "です。",
                font_size=20,
            ),
            self._line(
                "だから",
                MathTex(r"AP+PB", font_size=24),
                "は",
                MathTex(r"AP+PB'", font_size=24),
                "と同じ長さです。",
                font_size=20,
            ),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                mob.to_edge(DOWN, buff=0.52)
            else:
                self.stack_below(mob, shown, buff=0.10)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.4)
            shown.add(mob)
            self.linger(3.2)

    def part_step3_straight(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 3  直線")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self._line(
            MathTex(r"A", font_size=28),
            "から",
            MathTex(r"B'", font_size=28),
            "へ行く道は、直線がいちばん短いです。",
            font_size=24,
        )
        self.below_chip(lead, chip, buff=0.22)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger("A から B' へ行く道は、直線がいちばん短いです。")

        fig = self._base_figure(p_x=6.0, show_b_prime=True, show_straight=True)
        self.stack_below(fig, lead, buff=0.16)
        fig.to_edge(LEFT, buff=0.38)
        self._nudge(fig)
        self.play(FadeIn(fig), run_time=0.8)
        self.linger(3.2)

        rows = [
            self._line(
                "任意の",
                MathTex(r"P", font_size=26),
                "に対して",
                MathTex(r"AP+PB'", font_size=26),
                "は折れ線",
                font_size=20,
            ),
            self.ja_text("二点を結ぶ最短は直線", font_size=20),
            MathTex(r"AP+PB'\ge AB'", font_size=32, color=YELLOW),
            self._line(
                "等号は、",
                MathTex(r"P", font_size=24),
                "が線分",
                MathTex(r"AB'", font_size=24),
                "の上にあるとき",
                font_size=20,
            ),
            self._line(
                MathTex(r"P", font_size=24),
                "は川の上にもいなければならない",
                font_size=20,
            ),
            self._line(
                "最短の",
                MathTex(r"P", font_size=24),
                "は、直線",
                MathTex(r"AB'", font_size=24),
                "と川の交点",
                font_size=20,
            ),
            MathTex(r"AP_*+P_*B=AB'", font_size=34, color=GREEN),
        ]
        block = VGroup(*rows).arrange(DOWN, buff=0.11, aligned_edge=LEFT)
        block.next_to(fig, RIGHT, buff=0.30)
        block.align_to(fig, UP)
        self._fit(block, 7.8)
        self._nudge(block)
        for row in rows:
            self.play(FadeIn(row), run_time=0.4)
            self.linger(3.2)

    def part_step4_angles(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 4  角")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("この交点では、入る角と出る角が等しくなります。", font_size=24)
        self.below_chip(lead, chip, buff=0.22)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        fig = self._base_figure(
            p_x=6.0,
            show_b_prime=True,
            show_straight=True,
            show_angles=True,
        )
        self.stack_below(fig, lead, buff=0.14)
        fig.to_edge(LEFT, buff=0.36)
        self._nudge(fig)
        self.play(FadeIn(fig), run_time=0.8)
        self.linger(3.2)

        rows = [
            self._line(
                MathTex(r"A", font_size=26),
                "、",
                MathTex(r"P_*", font_size=26),
                "、",
                MathTex(r"B'", font_size=26),
                "は一直線",
                font_size=20,
            ),
            self.ja_text("法線とこの直線がつくる対頂角は等しい", font_size=20),
            self._line(
                "折り返しで",
                MathTex(r"B'P_*", font_size=24),
                "の角は",
                MathTex(r"BP_*", font_size=24),
                "の角に等しい",
                font_size=18,
            ),
            self._line(
                "よって入る角と出る角はどちらも",
                MathTex(r"\theta", font_size=28, color=YELLOW),
                font_size=20,
            ),
        ]
        block = VGroup(*rows).arrange(DOWN, buff=0.13, aligned_edge=LEFT)
        block.next_to(fig, RIGHT, buff=0.34)
        block.align_to(fig, UP)
        self._fit(block, 7.4)
        self._nudge(block)
        for row in rows:
            self.play(FadeIn(row), run_time=0.45)
            self.linger(3.2)

        note = self.ja_text("光が鏡で跳ね返るときと同じ角です。", font_size=22)
        note.to_edge(DOWN, buff=0.32)
        note.set_x(0)
        self.play(FadeIn(note), run_time=0.4)
        self.linger(note.text, extra=0.35)

    def part_example(self):
        self.wipe(self.header)
        chip = self.step_label("実例")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("試行で止まった数を、折り返しで最後まで計算します。", font_size=24)
        self.below_chip(lead, chip, buff=0.22)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        first = [
            MathTex(r"B'=(8,-2)", font_size=32, color=YELLOW),
            MathTex(r"\dfrac{-2-6}{8-0}=\dfrac{-8}{8}=-1", font_size=32),
            MathTex(r"y-6=-1(x-0)", font_size=32),
            MathTex(r"y=6-x", font_size=34),
            MathTex(r"6-x=0\qquad x=6", font_size=36, color=GREEN),
        ]
        block1 = self._formula_rows(first, lead, buff=0.14)
        self.play(FadeOut(block1), run_time=0.3)

        fig = self._base_figure(p_x=6.0, show_b_prime=True, show_straight=True)
        self.stack_below(fig, lead, buff=0.16)
        fig.set_x(0)
        self._nudge(fig)
        self.play(FadeIn(fig), run_time=0.7)
        self.linger(3.4)
        self.play(FadeOut(fig), run_time=0.3)

        second = [
            MathTex(r"AP=\sqrt{6^2+6^2}=\sqrt{72}=6\sqrt{2}", font_size=30),
            MathTex(r"PB=\sqrt{2^2+2^2}=\sqrt{8}=2\sqrt{2}", font_size=30),
            MathTex(r"6\sqrt{2}+2\sqrt{2}=8\sqrt{2}\approx 11.314", font_size=34, color=GREEN),
            self._line(
                MathTex(r"x=4", font_size=30),
                "の合計",
                MathTex(r"11.683", font_size=30),
                font_size=22,
            ),
            MathTex(r"11.683-11.314=0.369", font_size=32, color=YELLOW),
        ]
        block2 = self._formula_rows(second, lead, buff=0.14)
        self.linger(3.4)
        self.play(FadeOut(block2), run_time=0.3)

        table = self.aligned_table(
            [
                [
                    self._line(
                        MathTex(r"P", font_size=22, color=GREY_B),
                        "の横",
                        MathTex(r"x", font_size=22, color=GREY_B),
                        font_size=16,
                        color=GREY_B,
                    ),
                    self.ja_text("合計", font_size=16, color=GREY_B),
                ],
                [MathTex(r"4", font_size=28), MathTex(r"11.683", font_size=28)],
                [
                    MathTex(r"6", font_size=28, color=GREEN),
                    MathTex(r"11.314", font_size=28, color=GREEN),
                ],
                [MathTex(r"8", font_size=28), MathTex(r"12", font_size=28)],
            ],
            h_buff=0.5,
            v_buff=0.16,
        )
        table.scale(0.9)
        self.stack_below(table, lead, buff=0.2)
        table.set_x(0)
        self.reveal_table(table, row_wait=0.9)

        notes = [
            self._line(
                "試行で残っていたあいだに、交点",
                MathTex(r"x=6", font_size=26),
                "がありました。",
                font_size=22,
            ),
            self._line(
                "B の真下でも、まん中でもなく、直線",
                MathTex(r"AB'", font_size=26),
                "が川を切る場所です。",
                font_size=22,
            ),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, table, buff=0.18)
            else:
                self.stack_below(mob, shown, buff=0.12)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.4)
            shown.add(mob)
            self.linger(3.2)

    def part_generalize(self):
        self.wipe(self.header)
        chip = self.step_label("一般化")
        self.play(FadeIn(chip), run_time=0.4)

        lines = [
            self.ja_text("今やったことは、反射の原理と呼ばれる考え方でした。", font_size=24),
            self.ja_text("境界で一度触れる最短路は、先を折り返して直線に直す。", font_size=24),
            self.ja_text("その交点では、入る角と出る角が等しい。", font_size=24),
            self.ja_text("光の道も、同じ折り返しで最短になっています。", font_size=24),
        ]
        shown = VGroup()
        for i, mob in enumerate(lines):
            if i == 0:
                self.below_chip(mob, chip, buff=0.32)
            else:
                self.stack_below(mob, shown, buff=0.22)
            self._fit_left(mob)
            self.play(FadeIn(mob), run_time=0.5)
            shown.add(mob)
            self.linger(mob.text)

        ineq = MathTex(r"AP+PB=AP+PB'\ge AB'", font_size=40, color=YELLOW)
        self.stack_below(ineq, shown, buff=0.34)
        ineq.set_x(0)
        self.play(Write(ineq), run_time=1.0)
        self.linger(3.6)

        eq = self._line(
            "等号は、",
            MathTex(r"P", font_size=26),
            "が",
            MathTex(r"AB'", font_size=26),
            "と境界の交点のときです。",
            font_size=22,
        )
        self.stack_below(eq, ineq, buff=0.24)
        eq.set_x(0)
        self.play(FadeIn(eq), run_time=0.4)
        self.linger("等号は、P が AB' と境界の交点のときです。", extra=0.3)

    def part_summary(self):
        self.wipe(self.header)
        chip = self.step_label("まとめ")
        self.play(FadeIn(chip), run_time=0.35)

        rows = [
            self.ja_text("近いほうの真下は、短そうに見えて最短ではない", font_size=24),
            self.ja_text("点をいくつか試すと、あいだが残って止まる", font_size=24),
            self.ja_text("先を折り返すと、折れ線の長さが直線の長さに変わる", font_size=24),
            self.ja_text("直線と境界の交点が、いちばん短い触れ方", font_size=24),
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

        related = self.ja_text(
            "速さが途中で変わる道なら、角は等しくならず、折れ方が変わります。",
            font_size=22,
            color=GREY_B,
        )
        self.stack_below(related, shown, buff=0.36)
        self._fit_left(related)
        self.play(FadeIn(related), run_time=0.45)
        self.linger(related.text, extra=0.45)

    def _base_figure(
        self,
        p_x,
        show_b_prime=False,
        show_straight=False,
        show_angles=False,
        path_opacity=1.0,
        ap_len=None,
        pb_len=None,
    ):
        a = self._xy(self.AX, self.AY)
        b = self._xy(self.BX, self.BY)
        p = self._xy(p_x, 0.0)

        river = Line(self._xy(-0.7, 0.0), self._xy(8.7, 0.0), color=BLUE, stroke_width=5)
        river_lab = self.ja_text("川", font_size=20, color=BLUE)
        river_lab.next_to(river, RIGHT, buff=0.10)

        a_dot = Dot(a, color=YELLOW, radius=0.08)
        b_dot = Dot(b, color=TEAL, radius=0.08)
        p_dot = Dot(p, color=ORANGE, radius=0.08)
        a_lab = MathTex(r"A", font_size=28, color=YELLOW).next_to(a_dot, UL, buff=0.08)
        b_lab = MathTex(r"B", font_size=28, color=TEAL).next_to(b_dot, UR, buff=0.08)
        p_lab = MathTex(r"P", font_size=26, color=ORANGE).next_to(p_dot, DL, buff=0.10)
        if abs(p_x - 6.0) < 1e-6 and show_straight:
            p_lab = MathTex(r"P_*", font_size=26, color=ORANGE).next_to(p_dot, DL, buff=0.10)

        ap = Line(a, p, color=YELLOW, stroke_width=3)
        pb = Line(p, b, color=TEAL, stroke_width=3)
        ap.set_opacity(path_opacity)
        pb.set_opacity(path_opacity)

        parts = [river, river_lab, ap, pb, a_dot, b_dot, p_dot, a_lab, b_lab, p_lab]
        if ap_len is not None:
            parts.append(self._seg_label(a, p, ap_len, YELLOW, side=1))
        if pb_len is not None:
            parts.append(self._seg_label(p, b, pb_len, TEAL, side=1))
        if show_b_prime:
            parts.extend(self._b_prime_layer(p_x, include_path=True, show_straight=show_straight))
        if show_angles:
            parts.extend(self._angle_layer(p_x))
        return VGroup(*parts)

    def _b_prime_layer(self, p_x, include_path=True, show_straight=False):
        b = self._xy(self.BX, self.BY)
        bp = self._xy(self.BX, -self.BY)
        h = self._xy(self.BX, 0.0)
        p = self._xy(p_x, 0.0)
        a = self._xy(self.AX, self.AY)

        bb = DashedLine(b, bp, color=GREY_B, stroke_width=2)
        h_dot = Dot(h, color=GREY_B, radius=0.06)
        h_lab = MathTex(r"H", font_size=22, color=GREY_B).next_to(h_dot, DR, buff=0.08)
        bp_dot = Dot(bp, color=PURPLE, radius=0.08)
        bp_lab = MathTex(r"B'", font_size=26, color=PURPLE).next_to(bp_dot, DR, buff=0.08)
        items = [bb, h_dot, h_lab, bp_dot, bp_lab]
        if include_path:
            items.append(DashedLine(p, bp, color=PURPLE, stroke_width=2.5))
        if show_straight:
            items.insert(0, DashedLine(a, bp, color=WHITE, stroke_width=2.2))
        return items

    def _angle_layer(self, p_x):
        a = self._xy(self.AX, self.AY)
        b = self._xy(self.BX, self.BY)
        bp = self._xy(self.BX, -self.BY)
        p = self._xy(p_x, 0.0)
        n_full = DashedLine(p + DOWN * 0.82, p + UP * 1.12, color=GREY_A, stroke_width=2)
        n_up = Line(p, p + UP * 1.12, color=GREY_A)
        n_down = Line(p, p + DOWN * 0.82, color=GREY_A)
        to_a = Line(p, a, color=YELLOW)
        to_b = Line(p, b, color=TEAL)
        to_bp = Line(p, bp, color=PURPLE)
        ang_i = Angle(n_up, to_a, radius=0.36, color=YELLOW, stroke_width=4)
        ang_r = Angle(to_b, n_up, radius=0.50, color=TEAL, stroke_width=4)
        ang_below = Angle(n_down, to_bp, radius=0.40, color=PURPLE, stroke_width=4)
        th1 = MathTex(r"\theta", font_size=22, color=YELLOW)
        th2 = MathTex(r"\theta", font_size=22, color=TEAL)
        th3 = MathTex(r"\theta", font_size=22, color=PURPLE)
        th1.move_to(p + 0.58 * UP + 0.42 * LEFT)
        th2.move_to(p + 0.58 * UP + 0.52 * RIGHT)
        th3.move_to(p + 0.52 * DOWN + 0.50 * RIGHT)
        n_lab = self.ja_text("法線", font_size=16, color=GREY_A)
        n_lab.next_to(n_full, RIGHT, buff=0.08)
        n_lab.align_to(n_full, UP)
        return [n_full, ang_i, ang_r, ang_below, th1, th2, th3, n_lab]

    def _seg_label(self, p1, p2, tex, color, side=1):
        lab = MathTex(tex, font_size=20, color=color)
        mid = (p1 + p2) / 2
        d = p2 - p1
        nrm = np.array([-d[1], d[0], 0.0])
        length = np.linalg.norm(nrm)
        if length > 1e-8:
            nrm = nrm / length * 0.22 * side
        lab.move_to(mid + nrm)
        return lab

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
