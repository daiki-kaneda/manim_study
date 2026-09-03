from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import LessonScene


class AntOnCube(LessonScene):
    """#5 立方体の表面を歩く蟻（約7分）"""

    ISO_X = 0.88
    ISO_Z = 0.52
    ISO_Y = 0.82
    ISO_D = 0.24
    NET = 1.05

    def construct(self):
        self.header = self._open_header()
        self.part_question()
        self.part_trial_edges()
        self.part_trial_samples()
        self.part_step1_unfold()
        self.part_step2_place()
        self.part_step3_straight()
        self.part_step4_other()
        self.part_example()
        self.part_generalize()
        self.part_summary()

    def _iso(self, x, y, z):
        # 左右を非対称にして、反対頂点 S と T が画面上で縦に重ならないようにする。
        return (x * self.ISO_X - z * self.ISO_Z) * RIGHT + (
            y * self.ISO_Y + (x + z) * self.ISO_D
        ) * UP

    def _open_header(self):
        title = self.ja_text("立方体の表面を歩く蟻", font_size=40)
        self.play(FadeIn(title), run_time=0.8)
        self.linger(1.2)
        self.play(title.animate.scale(0.55).to_edge(UP, buff=0.16), run_time=0.5)
        return title

    def part_question(self):
        fig = self._cube()
        fig.next_to(self.header, DOWN, buff=0.42)
        fig.set_x(0)
        self.play(FadeIn(fig), run_time=0.9)
        self.linger(3.2)

        q1 = self._line(
            "立方体の表面だけを歩いて、",
            MathTex(r"S", font_size=28, color=YELLOW),
            "から反対側の",
            MathTex(r"T", font_size=28, color=TEAL),
            "へ行きます。",
            font_size=26,
        )
        q1.next_to(fig, DOWN, buff=0.36)
        q1.set_x(0)
        self._fit(q1, 13.0)
        q1.set_x(0)
        self.play(FadeIn(q1), run_time=0.45)
        self.linger("立方体の表面だけを歩いて、S から反対側の T へ行きます。")

        q2 = self.ja_text("いちばん短い道は、どの面をまたぐ道でしょう。", font_size=26)
        self.stack_below(q2, q1, buff=0.16)
        q2.set_x(0)
        self.play(FadeIn(q2), run_time=0.45)
        self.linger(q2.text, extra=0.35)

    def part_trial_edges(self):
        self.wipe(self.header)
        chip = self.step_label("試行  辺沿い")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("まず、辺だけをたどると、3 本で着きます。", font_size=24)
        self.below_chip(lead, chip, buff=0.24)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        fig = self._cube(
            path_edges=[("S", "B"), ("B", "C"), ("C", "T")],
            path_color=ORANGE,
            mark_lens=True,
        )
        self.stack_below(fig, lead, buff=0.22)
        fig.to_edge(LEFT, buff=0.45)
        self._nudge(fig)
        self.play(FadeIn(fig), run_time=0.7)
        self.linger(3.2)

        rows = [
            self.ja_text("各辺の長さは 1", font_size=24),
            MathTex(r"1+1=2", font_size=32),
            MathTex(r"2+1=3", font_size=36, color=YELLOW),
        ]
        block = VGroup(*rows).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        block.next_to(fig, RIGHT, buff=0.5)
        block.align_to(fig, UP)
        self._nudge(block)
        for row in rows:
            self.play(FadeIn(row), run_time=0.45)
            self.linger(3.2)

        notes = [
            self.ja_text("着きます。長さは 3 です。", font_size=22),
            self.ja_text("でも、面の中を斜めに歩けば、もっと短い可能性があります。", font_size=22),
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

        self.play(FadeOut(VGroup(fig, block, shown)), run_time=0.35)
        face = self._cube(path_edges=[("S", "C")], path_color=YELLOW)
        space = DashedLine(
            self._iso(0, 0, 0),
            self._iso(1, 1, 1),
            color=GREY_A,
            stroke_width=3.5,
        )
        combo = VGroup(face, space)
        extra = [
            MathTex(r"\sqrt{1^2+1^2}=\sqrt{2}", font_size=32, color=YELLOW),
            self.ja_text("前面の対角線は、隣の頂点で止まる。T には着かない。", font_size=20),
            MathTex(r"\sqrt{3}", font_size=32, color=GREY_A),
            self.ja_text("立方体を貫く直線は、表面の道ではありません。", font_size=20),
        ]
        extra_block = VGroup(*extra).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        pair = VGroup(combo, extra_block).arrange(RIGHT, buff=0.5, aligned_edge=UP)
        self.stack_below(pair, lead, buff=0.2)
        pair.set_x(0)
        self._nudge(pair)
        self.play(FadeIn(face), run_time=0.55)
        self.play(FadeIn(extra[0]), FadeIn(extra[1]), run_time=0.5)
        self.linger(3.2)
        self.play(FadeIn(space), FadeIn(extra[2]), FadeIn(extra[3]), run_time=0.55)
        self.linger(3.4)

    def part_trial_samples(self):
        self.wipe(self.header)
        chip = self.step_label("試行  いくつか試す")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("前面と上面の境目で、横切る点を動かして長さを足してみます。", font_size=22)
        self.below_chip(lead, chip, buff=0.22)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        fig = self._cube(path_edges=[("S", "P"), ("P", "T")], path_color=ORANGE, p_t=0.5)
        calc = [
            MathTex(r"P=\bigl(1/2,\,1\bigr)", font_size=28, color=ORANGE),
            MathTex(r"SP=\sqrt{(1/2)^2+1^2}=\sqrt{1/4+1}=\sqrt{5/4}", font_size=26),
            MathTex(r"\sqrt{5/4}=\dfrac{\sqrt{5}}{2}", font_size=26),
            MathTex(r"PT=\sqrt{(1-1/2)^2+1^2}=\dfrac{\sqrt{5}}{2}", font_size=26),
            MathTex(r"\dfrac{\sqrt{5}}{2}+\dfrac{\sqrt{5}}{2}=\sqrt{5}\approx 2.236", font_size=30, color=YELLOW),
        ]
        calc_block = VGroup(*calc).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        pair = VGroup(fig, calc_block).arrange(RIGHT, buff=0.42, aligned_edge=UP)
        self.stack_below(pair, lead, buff=0.16)
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
                    self._line("境目", MathTex(r"t", font_size=22, color=GREY_B), font_size=16, color=GREY_B),
                    MathTex(r"SP", font_size=22, color=GREY_B),
                    MathTex(r"PT", font_size=22, color=GREY_B),
                    self.ja_text("合計", font_size=16, color=GREY_B),
                ],
                [MathTex(r"0", font_size=26), MathTex(r"1", font_size=26), MathTex(r"1.414", font_size=26), MathTex(r"2.414", font_size=26)],
                [
                    MathTex(r"1/2", font_size=26, color=YELLOW),
                    MathTex(r"1.118", font_size=26, color=YELLOW),
                    MathTex(r"1.118", font_size=26, color=YELLOW),
                    MathTex(r"2.236", font_size=26, color=YELLOW),
                ],
                [MathTex(r"1", font_size=26), MathTex(r"1.414", font_size=26), MathTex(r"1", font_size=26), MathTex(r"2.414", font_size=26)],
            ],
            h_buff=0.34,
            v_buff=0.12,
        )
        table.scale(0.86)
        self.stack_below(table, lead, buff=0.18)
        table.set_x(0)
        self.reveal_table(table, row_wait=0.85)

        notes = [
            self._line("試した中では", MathTex(r"t=1/2", font_size=26), "がいちばん短い。", font_size=22),
            self.ja_text("辺沿いの 3 より短いので、辺だけ仮説は破綻します。", font_size=22),
            self._line(
                MathTex(r"0", font_size=26),
                "と",
                MathTex(r"1", font_size=26),
                "のあいだは、半分以外をまだ調べていません。",
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

    def part_step1_unfold(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 1  展開")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("表面の道は、面を順にまたぐ折れ線です。面を広げると、一枚の紙の上の道になります。", font_size=22)
        self.below_chip(lead, chip, buff=0.22)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        cube = self._cube(highlight_faces=("front", "top"))
        net = self._net_1x2()
        pair = VGroup(cube, net).arrange(RIGHT, buff=0.7, aligned_edge=DOWN)
        self.stack_below(pair, lead, buff=0.22)
        pair.set_x(0)
        self._nudge(pair)
        self.play(FadeIn(cube), run_time=0.6)
        self.linger(3.2)
        self.play(FadeIn(net), run_time=0.7)
        self.linger(3.2)

        rows = [
            self.ja_text("前面と上面は、境目の辺でつながっている", font_size=22),
            self.ja_text("境目で切らず、そこを蝶番にして開く", font_size=22),
            self.ja_text("二つの正方形が、縦に並んだ長方形になる", font_size=22),
            self.ja_text("表面の道は、この長方形の上の道と同じ長さ", font_size=22),
        ]
        shown = VGroup()
        for i, mob in enumerate(rows):
            if i == 0:
                mob.to_edge(DOWN, buff=1.15)
            else:
                self.stack_below(mob, shown, buff=0.08)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.4)
            shown.add(mob)
            self.linger(3.2)

    def part_step2_place(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 2  置く")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self._line(
            "広げた紙の上に、",
            MathTex(r"S", font_size=28, color=YELLOW),
            "と",
            MathTex(r"T", font_size=28, color=TEAL),
            "を置きます。",
            font_size=24,
        )
        self.below_chip(lead, chip, buff=0.22)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger("広げた紙の上に、S と T を置きます。")

        fig = self._net_1x2(show_points=True)
        self.stack_below(fig, lead, buff=0.2)
        fig.to_edge(LEFT, buff=0.55)
        self._nudge(fig)
        self.play(FadeIn(fig), run_time=0.7)
        self.linger(3.2)

        rows = [
            self.ja_text("前面の左下を原点にする", font_size=22),
            MathTex(r"S=(0,0)", font_size=32, color=YELLOW),
            MathTex(r"y=1", font_size=30),
            MathTex(r"T=(1,2)", font_size=36, color=TEAL),
        ]
        block = VGroup(*rows).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        block.next_to(fig, RIGHT, buff=0.55)
        block.align_to(fig, UP)
        self._nudge(block)
        for row in rows:
            self.play(FadeIn(row), run_time=0.45)
            self.linger(3.2)
        self.linger(3.4)

    def part_step3_straight(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 3  直線")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("広げた紙の上では、二点を結ぶ最短は直線です。", font_size=24)
        self.below_chip(lead, chip, buff=0.22)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        fig = self._net_1x2(show_points=True, show_line=True, p_t=0.5)
        self.stack_below(fig, lead, buff=0.16)
        fig.to_edge(LEFT, buff=0.45)
        self._nudge(fig)
        self.play(FadeIn(fig), run_time=0.8)
        self.linger(3.2)

        rows = [
            self._line("任意の境目", MathTex(r"P=(t,1)", font_size=26), "に対して、道は折れ線", font_size=20),
            self.ja_text("二点を結ぶ最短は直線", font_size=20),
            MathTex(r"ST=\sqrt{(1-0)^2+(2-0)^2}", font_size=28),
            MathTex(r"\sqrt{1^2+2^2}=\sqrt{1+4}=\sqrt{5}", font_size=32, color=YELLOW),
            self._line("等号は、", MathTex(r"P", font_size=24), "が線分", MathTex(r"ST", font_size=24), "の上", font_size=20),
            MathTex(r"y=2x,\quad y=1\qquad t=1/2", font_size=30, color=GREEN),
        ]
        block = VGroup(*rows).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        block.next_to(fig, RIGHT, buff=0.36)
        block.align_to(fig, UP)
        self._fit(block, 8.0)
        self._nudge(block)
        for row in rows:
            self.play(FadeIn(row), run_time=0.4)
            self.linger(3.2)

    def part_step4_other(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 4  ほかの展開")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("展開の仕方を変えると、紙の上の T の場所が変わります。", font_size=22)
        self.below_chip(lead, chip, buff=0.2)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        net_h = self._net_2x1(show_line=True)
        cap1 = VGroup(
            net_h,
            MathTex(r"S=(0,0),\ T=(2,1)", font_size=24),
            MathTex(r"\sqrt{2^2+1^2}=\sqrt{5}", font_size=28, color=GREEN),
        ).arrange(DOWN, buff=0.12)
        self.stack_below(cap1, lead, buff=0.16)
        cap1.set_x(-3.2)
        self._nudge(cap1)
        self.play(FadeIn(cap1), run_time=0.7)
        self.linger(3.2)

        strip = self._net_1x3()
        cap2 = VGroup(
            strip,
            self.ja_text("辺だけで 3 面ぶん", font_size=20),
            MathTex(r"3", font_size=28, color=YELLOW),
        ).arrange(DOWN, buff=0.10)
        cap2.next_to(cap1, RIGHT, buff=0.55)
        cap2.align_to(cap1, UP)
        self.play(FadeIn(cap2), run_time=0.7)
        self.linger(3.2)

        self.play(FadeOut(cap1), FadeOut(cap2), run_time=0.35)
        ell = self._net_L()
        cap3 = VGroup(
            ell,
            self.ja_text("L 字の欠けた角を直線がまたぐ。表面の道ではない。", font_size=20),
            MathTex(r"2\sqrt{2}", font_size=28, color=GREY_B),
        ).arrange(DOWN, buff=0.12)
        self.stack_below(cap3, lead, buff=0.18)
        cap3.set_x(0)
        self._nudge(cap3)
        self.play(FadeIn(cap3), run_time=0.75)
        self.linger(3.4)

        notes = [
            self.ja_text("直線が面の内側を通る展開だけが、表面の道になります。", font_size=22),
            self._line("その中でいちばん短いのが", MathTex(r"\sqrt{5}", font_size=28, color=GREEN), "です。", font_size=22),
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

    def part_example(self):
        self.wipe(self.header)
        chip = self.step_label("実例")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("試行で止まった数を、展開図の直線で最後まで計算します。", font_size=22)
        self.below_chip(lead, chip, buff=0.2)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        first = [
            MathTex(r"S=(0,0),\quad T=(1,2)", font_size=30),
            MathTex(r"\dfrac{2-0}{1-0}=2", font_size=30),
            MathTex(r"y=2x", font_size=32),
            MathTex(r"2x=1\qquad t=1/2", font_size=34, color=GREEN),
        ]
        block1 = self._formula_rows(first, lead, buff=0.14)
        self.play(FadeOut(block1), run_time=0.3)

        fig = self._net_1x2(show_points=True, show_line=True, p_t=0.5)
        self.stack_below(fig, lead, buff=0.16)
        fig.set_x(0)
        self._nudge(fig)
        self.play(FadeIn(fig), run_time=0.7)
        self.linger(3.4)
        self.play(FadeOut(fig), run_time=0.3)

        second = [
            MathTex(r"ST=\sqrt{1^2+2^2}=\sqrt{5}", font_size=32, color=GREEN),
            MathTex(r"\sqrt{5}\approx 2.236", font_size=30),
            self._line(MathTex(r"t=0", font_size=28), "の合計", MathTex(r"2.414", font_size=28), font_size=22),
            MathTex(r"2.414-2.236=0.178", font_size=30, color=YELLOW),
            MathTex(r"3-2.236=0.764", font_size=30),
        ]
        block2 = self._formula_rows(second, lead, buff=0.12)
        self.linger(3.4)
        self.play(FadeOut(block2), run_time=0.3)

        table = self.aligned_table(
            [
                [
                    self.ja_text("道", font_size=16, color=GREY_B),
                    self.ja_text("長さ", font_size=16, color=GREY_B),
                ],
                [self.ja_text("辺 3 本", font_size=20), MathTex(r"3", font_size=28)],
                [self._line("境目", MathTex(r"t=0", font_size=24), font_size=18), MathTex(r"2.414", font_size=28)],
                [
                    self._line("境目", MathTex(r"t=1/2", font_size=24, color=GREEN), font_size=18),
                    MathTex(r"2.236", font_size=28, color=GREEN),
                ],
                [self._line("境目", MathTex(r"t=1", font_size=24), font_size=18), MathTex(r"2.414", font_size=28)],
            ],
            h_buff=0.46,
            v_buff=0.14,
        )
        table.scale(0.88)
        self.stack_below(table, lead, buff=0.18)
        table.set_x(0)
        self.reveal_table(table, row_wait=0.85)

        notes = [
            self.ja_text("試行で残っていたあいだの、ちょうど真ん中が交点でした。", font_size=22),
            self.ja_text("いちばん短いのは、前面と上面をまたぐ、展開図上の直線です。", font_size=22),
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
            self.ja_text("今やったことは、立体の表面の最短経路を、展開図の直線で求める考え方でした。", font_size=22),
            self.ja_text("面を広げると、折れ線の長さが、紙の上の長さに変わる。", font_size=22),
            self.ja_text("紙の上では、二点を結ぶ最短は直線。", font_size=22),
            self.ja_text("直線が面の内側を通る展開だけを数え、その中でいちばん短いものを取る。", font_size=22),
        ]
        shown = VGroup()
        for i, mob in enumerate(lines):
            if i == 0:
                self.below_chip(mob, chip, buff=0.3)
            else:
                self.stack_below(mob, shown, buff=0.2)
            self._fit_left(mob)
            self.play(FadeIn(mob), run_time=0.5)
            shown.add(mob)
            self.linger(mob.text)

        ineq = MathTex(r"ST=\sqrt{1^2+2^2}=\sqrt{5}", font_size=40, color=YELLOW)
        self.stack_below(ineq, shown, buff=0.32)
        ineq.set_x(0)
        self.play(Write(ineq), run_time=1.0)
        self.linger(3.6)

        eq = self._line(
            "辺の長さが",
            MathTex(r"s", font_size=28),
            "なら",
            MathTex(r"s\sqrt{5}", font_size=32, color=YELLOW),
            font_size=22,
        )
        self.stack_below(eq, ineq, buff=0.22)
        eq.set_x(0)
        self.play(FadeIn(eq), run_time=0.4)
        self.linger("辺の長さが s なら s√5。", extra=0.3)

    def part_summary(self):
        self.wipe(self.header)
        chip = self.step_label("まとめ")
        self.play(FadeIn(chip), run_time=0.35)

        rows = [
            self.ja_text("辺だけたどると着くが、長い", font_size=24),
            self.ja_text("境目の点をいくつか試すと、あいだが残って止まる", font_size=24),
            self.ja_text("面を広げると、表面の道が紙の上の道になる", font_size=24),
            self.ja_text("展開図上の直線が、いちばん短いまたぎ方", font_size=24),
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
            "部屋の 2 点を、壁と天井だけ伝って歩くときも、同じように展開します。",
            font_size=22,
            color=GREY_B,
        )
        self.stack_below(related, shown, buff=0.36)
        self._fit_left(related)
        self.play(FadeIn(related), run_time=0.45)
        self.linger(related.text, extra=0.45)

    def _cube(self, path_edges=None, path_color=ORANGE, highlight_faces=(), p_t=None, mark_lens=False):
        pts = {
            "S": self._iso(0, 0, 0),
            "B": self._iso(1, 0, 0),
            "C": self._iso(1, 1, 0),
            "D": self._iso(0, 1, 0),
            "E": self._iso(0, 0, 1),
            "F": self._iso(1, 0, 1),
            "T": self._iso(1, 1, 1),
            "H": self._iso(0, 1, 1),
        }
        if p_t is not None:
            pts["P"] = self._iso(p_t, 1, 0)

        hidden = {("S", "E"), ("E", "F"), ("E", "H")}
        all_edges = [
            ("S", "B"),
            ("B", "C"),
            ("C", "D"),
            ("D", "S"),
            ("B", "F"),
            ("C", "T"),
            ("D", "H"),
            ("F", "T"),
            ("H", "T"),
            ("S", "E"),
            ("E", "F"),
            ("E", "H"),
        ]
        parts = []
        for a, b in all_edges:
            key = (a, b)
            dashed = key in hidden or (b, a) in hidden
            cls = DashedLine if dashed else Line
            parts.append(cls(pts[a], pts[b], color=GREY_B, stroke_width=2))

        if "front" in highlight_faces:
            front = Polygon(pts["S"], pts["B"], pts["C"], pts["D"], color=YELLOW, stroke_width=0)
            front.set_fill(YELLOW, 0.22)
            parts.insert(0, front)
        if "top" in highlight_faces:
            top = Polygon(pts["D"], pts["C"], pts["T"], pts["H"], color=TEAL, stroke_width=0)
            top.set_fill(TEAL, 0.22)
            parts.insert(0, top)

        if path_edges:
            for a, b in path_edges:
                parts.append(Line(pts[a], pts[b], color=path_color, stroke_width=5))
                if mark_lens:
                    mid = (np.array(pts[a]) + np.array(pts[b])) / 2
                    lab = MathTex(r"1", font_size=20, color=path_color)
                    lab.move_to(mid)
                    shift = mid - np.array(pts[a])
                    if abs(shift[0]) >= abs(shift[1]):
                        lab.shift(0.16 * UP)
                    else:
                        lab.shift(0.18 * RIGHT)
                    parts.append(lab)

        s_dot = Dot(pts["S"], color=YELLOW, radius=0.08)
        t_dot = Dot(pts["T"], color=TEAL, radius=0.08)
        s_lab = MathTex(r"S", font_size=26, color=YELLOW).next_to(s_dot, DL, buff=0.08)
        t_lab = MathTex(r"T", font_size=26, color=TEAL).next_to(t_dot, UR, buff=0.08)
        parts.extend([s_dot, t_dot, s_lab, t_lab])
        if p_t is not None:
            p_dot = Dot(pts["P"], color=ORANGE, radius=0.07)
            p_lab = MathTex(r"P", font_size=24, color=ORANGE).next_to(p_dot, UP, buff=0.08)
            parts.extend([p_dot, p_lab])
        return VGroup(*parts)

    def _sq(self, x0, y0, color=GREY_A):
        bl = x0 * self.NET * RIGHT + y0 * self.NET * UP
        br = bl + self.NET * RIGHT
        tr = br + self.NET * UP
        tl = bl + self.NET * UP
        poly = Polygon(bl, br, tr, tl, color=color, stroke_width=2.5)
        poly.set_fill(color, 0.12)
        return poly, bl, br, tr, tl

    def _net_1x2(self, show_points=True, show_line=False, p_t=None):
        front, s, _, c, d = self._sq(0, 0, YELLOW)
        top, _, _, t, _ = self._sq(0, 1, TEAL)
        parts = [front, top]
        front_lab = self.ja_text("前面", font_size=16, color=YELLOW)
        front_lab.move_to((s + c) / 2)
        top_lab = self.ja_text("上面", font_size=16, color=TEAL)
        top_lab.move_to((d + t) / 2)
        parts.extend([front_lab, top_lab])
        if show_points:
            s_dot = Dot(s, color=YELLOW, radius=0.07)
            t_dot = Dot(t, color=TEAL, radius=0.07)
            s_lab = MathTex(r"S", font_size=24, color=YELLOW).next_to(s_dot, DL, buff=0.08)
            t_lab = MathTex(r"T", font_size=24, color=TEAL).next_to(t_dot, UR, buff=0.08)
            parts.extend([s_dot, t_dot, s_lab, t_lab])
        if show_line:
            parts.append(Line(s, t, color=ORANGE, stroke_width=4))
        if p_t is not None:
            p = s + p_t * self.NET * RIGHT + self.NET * UP
            parts.append(Dot(p, color=ORANGE, radius=0.07))
            parts.append(MathTex(r"P", font_size=22, color=ORANGE).next_to(p, RIGHT, buff=0.08))
        g = VGroup(*parts)
        return g

    def _net_2x1(self, show_line=True):
        front, s, b, _, _ = self._sq(0, 0, YELLOW)
        right, _, _, t, _ = self._sq(1, 0, PURPLE)
        s_dot = Dot(s, color=YELLOW, radius=0.06)
        t_dot = Dot(t, color=TEAL, radius=0.06)
        parts = [front, right, s_dot, t_dot]
        if show_line:
            parts.append(Line(s, t, color=ORANGE, stroke_width=3.5))
        parts.append(MathTex(r"S", font_size=20, color=YELLOW).next_to(s_dot, DL, buff=0.06))
        parts.append(MathTex(r"T", font_size=20, color=TEAL).next_to(t_dot, UR, buff=0.06))
        return VGroup(*parts)

    def _net_1x3(self):
        sqs = [self._sq(i, 0, GREY_A)[0] for i in range(3)]
        s = ORIGIN
        t = 3 * self.NET * RIGHT
        s_dot = Dot(s, color=YELLOW, radius=0.06)
        t_dot = Dot(t, color=TEAL, radius=0.06)
        path = Line(s, t, color=YELLOW, stroke_width=3.5)
        s_lab = MathTex(r"S", font_size=20, color=YELLOW).next_to(s_dot, DL, buff=0.06)
        t_lab = MathTex(r"T", font_size=20, color=TEAL).next_to(t_dot, DR, buff=0.06)
        return VGroup(*sqs, path, s_dot, t_dot, s_lab, t_lab)

    def _net_L(self):
        front, s, _, _, _ = self._sq(0, 0, YELLOW)
        top, _, _, _, _ = self._sq(0, 1, TEAL)
        right, _, _, _, _ = self._sq(1, 0, PURPLE)
        ghost, _, _, ghost_tr, _ = self._sq(1, 1, GREY_B)
        ghost.set_fill(GREY_B, 0.05)
        ghost.set_stroke(GREY_B, 1.5, opacity=0.7)
        t = ghost_tr
        dash = DashedLine(s, t, color=GREY_A, stroke_width=3)
        hole = self.ja_text("面がない", font_size=16, color=GREY_B)
        hole.move_to((ghost.get_center()))
        s_dot = Dot(s, color=YELLOW, radius=0.06)
        t_dot = Dot(t, color=GREY_B, radius=0.06)
        t_lab = MathTex(r"T", font_size=20, color=GREY_B).next_to(t_dot, UR, buff=0.06)
        s_lab = MathTex(r"S", font_size=20, color=YELLOW).next_to(s_dot, DL, buff=0.06)
        return VGroup(front, top, right, ghost, dash, hole, s_dot, t_dot, s_lab, t_lab)

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
