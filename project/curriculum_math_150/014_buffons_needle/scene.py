from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import LessonScene


class BuffonsNeedle(LessonScene):
    """#14 針を落として円周率は出るか（約10分）"""

    FLOOR_W = 6.20
    FLOOR_GAP = 0.88
    FLOOR_N = 4
    NEEDLE_LEN = 0.78

    def construct(self):
        self.header = self._open_header()
        self.part_question()
        self.part_trial_count()
        self.part_trial_why_pi()
        self.part_step1_coords()
        self.part_step2_hit()
        self.part_step3_area()
        self.part_step4_solve()
        self.part_example()
        self.part_generalize()
        self.part_summary()

    def _open_header(self):
        title = self._line(
            "針を落として円周率は出るか",
            MathTex(r"\pi", font_size=36),
            font_size=36,
        )
        self.play(FadeIn(title), run_time=0.8)
        self.pause_new_screen()
        self.linger(1.5)
        self.play(title.animate.scale(0.52).to_edge(UP, buff=0.16), run_time=0.5)
        title.set_x(0)
        return title

    def part_question(self):
        fig = self._floor(
            specs=[(0.15, 1.5 * self.FLOOR_GAP + 0.28, 0.42)],
            show_d=True,
            show_l=True,
        )
        cap = self.ja_text(
            "等間隔の平行線の上に、長さの決まった針を 1 本置きます。",
            font_size=18,
        )
        self._fit(cap, 13.0)
        pair = VGroup(fig, cap).arrange(DOWN, buff=0.22)
        pair.next_to(self.header, DOWN, buff=0.26)
        pair.set_x(0)
        self._nudge(pair)
        self.play(FadeIn(fig), FadeIn(cap), run_time=0.8)
        self.pause_new_screen()
        self.linger(cap.text)

        q1 = self._line(
            "等間隔の平行線を床に引く、とおく。間隔を",
            MathTex(r"D", font_size=24, color=TEAL),
            "とおく。",
            font_size=20,
        )
        self.stack_below(q1, pair, buff=0.20)
        q1.set_x(0)
        self._fit(q1, 13.0)
        q1.set_x(0)
        self.play(FadeIn(q1), run_time=0.7)
        self.linger("等間隔の平行線を床に引く、とおく。間隔を D とおく。")

        q2 = self._line(
            "長さ",
            MathTex(r"L", font_size=24, color=ORANGE),
            "の針を、無作為に落とします。ただし",
            MathTex(r"L\le D", font_size=24),
            "とおく。",
            font_size=20,
        )
        self.stack_below(q2, q1, buff=0.12)
        q2.set_x(0)
        self._fit(q2, 13.0)
        q2.set_x(0)
        self.play(FadeIn(q2), run_time=0.7)
        self.linger("長さ L の針を、無作為に落とします。ただし L≤D とおく。")

        q3 = self.ja_text(
            "線と交わる割合から、なぜ円周率が出るのでしょうか。",
            font_size=20,
        )
        self.stack_below(q3, q2, buff=0.12)
        q3.set_x(0)
        self._fit(q3, 13.0)
        q3.set_x(0)
        self.play(FadeIn(q3), run_time=0.7)
        self.linger(q3.text, extra=0.35)

    def part_trial_count(self):
        chip = self.begin_step("試行  交差を数える", self.header)

        lead = self.ja_text(
            "まず、何度も落として、交わる回数を数える方法を最後までやります。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        g = self.FLOOR_GAP
        drops = [
            ([(-1.70, 1 * g + 0.08, 1.22)], "1 回目。交わる"),
            (
                [(-1.70, 1 * g + 0.08, 1.22), (0.20, 2 * g + 0.44, 0.12)],
                "2 回目。交わらない",
            ),
            (
                [
                    (-1.70, 1 * g + 0.08, 1.22),
                    (0.20, 2 * g + 0.44, 0.12),
                    (1.85, 1 * g + 0.10, 0.95),
                ],
                "3 回目。交わる",
            ),
        ]
        fig = self._floor(specs=drops[0][0])
        self.stack_below(fig, lead, buff=0.18)
        fig.set_x(0)
        self._nudge(fig)
        cap = self.ja_text(drops[0][1], font_size=18)
        self._fit(cap, 13.0)
        self.stack_below(cap, fig, buff=0.22)
        cap.set_x(0)
        self.play(FadeIn(fig), FadeIn(cap), run_time=0.7)
        self.pause_new_screen()
        self.linger(drops[0][1])

        for specs, text in drops[1:]:
            nxt = self._floor(specs=specs)
            nxt.move_to(fig)
            new_cap = self.ja_text(text, font_size=18)
            self._fit(new_cap, 13.0)
            self.stack_below(new_cap, nxt, buff=0.22)
            new_cap.set_x(0)
            self.play(FadeOut(fig), FadeIn(nxt), FadeOut(cap), run_time=0.65)
            fig = nxt
            cap = new_cap
            self.play(FadeIn(cap), run_time=0.55)
            self.linger(text)

        self.play(FadeOut(VGroup(fig, cap)), run_time=0.45)
        self.pause_topic()

        table = self.aligned_table(
            [
                [
                    self.ja_text("落とした回数", font_size=16, color=GREY_B),
                    self.ja_text("交わる回数", font_size=16, color=GREY_B),
                ],
                [
                    MathTex(r"3", font_size=28),
                    MathTex(r"2", font_size=28, color=YELLOW),
                ],
            ],
            h_buff=0.40,
            v_buff=0.12,
        )
        table.scale(0.90)
        self.stack_below(table, lead, buff=0.16)
        table.set_x(0)
        self.reveal_table(table, row_wait=1.20)

        notes = [
            self.ja_text("3 回だけだと、割合はまだ安定しません。", font_size=18),
            self.ja_text(
                "回数を増やせば割合は安定しそうでも、なぜ円周率が出るかは、数えているだけでは分かりません。",
                font_size=18,
            ),
        ]
        self._show_notes(notes, table, buff=0.14)

    def part_trial_why_pi(self):
        chip = self.begin_step("試行  円周率？", self.header)

        lead = self._line(
            "交わる割合を",
            MathTex(r"p", font_size=24, color=YELLOW),
            "とおき、円周率で割る式を、理由なしに書いてみます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger("交わる割合を p とおき、円周率で割る式を、理由なしに書いてみます。")

        rows = [
            self._line(
                "交わる割合",
                MathTex(r"p", font_size=26, color=YELLOW),
                "が何かの式になる、と予想する",
                font_size=18,
            ),
            self._line(
                "円が出てこない実験なのに",
                MathTex(r"\pi", font_size=26, color=YELLOW),
                "が答えに入る、とだけ言ってしまう",
                font_size=18,
            ),
            self.ja_text("針の位置と角度を、まだ分けて書いていない", font_size=18),
        ]
        block = self._formula_rows(rows, lead, buff=0.12, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(block), run_time=0.45)
        self.pause_topic()

        notes = [
            self.ja_text(
                "実験の回数を増やしても、交わる条件の図が無いと、円周率の出所は見えません。",
                font_size=18,
            ),
            self.ja_text(
                "この問いが欲しいのは、交わる配置が、全部の配置のうちどれだけの面積かです。",
                font_size=18,
            ),
        ]
        self._show_notes(notes, lead, buff=0.16)

    def part_step1_coords(self):
        chip = self.begin_step("STEP 1  位置と角度", self.header)

        lead = self.ja_text(
            "針の置き方を、近くの線からの距離と、線との角度で書きます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        defs = [
            self._line(
                "一番近い線からの距離を",
                MathTex(r"x", font_size=24, color=TEAL),
                "とおく。範囲は",
                MathTex(r"0\le x\le\dfrac{D}{2}", font_size=26, color=TEAL),
                font_size=18,
            ),
            self._line(
                "針と線のなす角を",
                MathTex(r"\theta", font_size=24, color=YELLOW),
                "とおく。範囲は",
                MathTex(r"0\le\theta\le\pi", font_size=26, color=YELLOW),
                font_size=18,
            ),
            self._line(
                MathTex(r"x", font_size=24, color=TEAL),
                "と",
                MathTex(r"\theta", font_size=24, color=YELLOW),
                "は独立で、それぞれの範囲に一様、とおく",
                font_size=18,
            ),
        ]
        block = self._formula_rows(defs, lead, buff=0.12, hold=self.PAUSE_SHORT_FORMULA)
        self.pause_conclusion()
        self.play(FadeOut(block), run_time=0.45)
        self.pause_topic()

        fig = self._coord_figure()
        meaning = VGroup(
            self._line(
                MathTex(r"x", font_size=26, color=TEAL),
                "一番近い線からの距離",
                font_size=18,
            ),
            self._line(
                MathTex(r"\theta", font_size=26, color=YELLOW),
                "針と線のなす角",
                font_size=18,
            ),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        pair = VGroup(fig, meaning).arrange(RIGHT, buff=0.48, aligned_edge=UP)
        self.stack_below(pair, lead, buff=0.16)
        pair.set_x(0)
        self._nudge(pair)
        cap = self.ja_text(
            "左が床の線と針、右が二つの数の意味です。",
            font_size=18,
        )
        self._fit(cap, 13.0)
        self.stack_below(cap, pair, buff=0.18)
        cap.set_x(0)
        self.play(FadeIn(fig), FadeIn(meaning), run_time=0.7)
        self.pause_new_screen()
        self.play(FadeIn(cap), run_time=0.55)
        self.linger(cap.text)
        self.linger(3.2)

        self.play(FadeOut(VGroup(pair, cap)), run_time=0.45)
        self.pause_topic()

        notes = [
            self._line(
                "落とすたびに、",
                MathTex(r"(x,\theta)", font_size=24),
                "が一つ決まります。",
                font_size=18,
            ),
            self.ja_text("交わるかどうかは、この二つの数の関係で決まります。", font_size=18),
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
            self.play(FadeIn(mob), run_time=0.55)
            shown.add(mob)
            if i == 0:
                self.linger("落とすたびに、(x,θ) が一つ決まります。")
            else:
                self.linger(mob.text)

    def part_step2_hit(self):
        chip = self.begin_step("STEP 2  交わる条件", self.header)

        lead = self._line(
            "針の端が線に届くときを、",
            MathTex(r"x", font_size=22, color=TEAL),
            "と",
            MathTex(r"\theta", font_size=22, color=YELLOW),
            "の不等式にします。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger("針の端が線に届くときを、x と θ の不等式にします。")

        restate = self._line(
            "針の長さ",
            MathTex(r"L", font_size=24, color=ORANGE),
            "。半長",
            MathTex(r"\dfrac{L}{2}", font_size=24, color=ORANGE),
            "。",
            font_size=18,
        )
        self.stack_below(restate, lead, buff=0.10)
        restate.set_x(0)
        self.play(FadeIn(restate), run_time=0.55)
        self.pause_short_formula()
        self.linger("針の長さ L。半長 L/2。")
        self.play(FadeOut(lead), run_time=0.45)

        fig = self._hit_figure(theta=0.70)
        formulas = VGroup(
            self._line(
                "針の中心から端までの、線に垂直な成分は",
                MathTex(r"\dfrac{L}{2}\sin\theta", font_size=26, color=ORANGE),
                font_size=16,
            ),
            self._line(
                "交わるのは、この成分が",
                MathTex(r"x", font_size=22, color=TEAL),
                "以上のとき",
                font_size=16,
            ),
            self._line(
                "だから",
                MathTex(r"x\le\dfrac{L}{2}\sin\theta", font_size=30, color=YELLOW),
                font_size=18,
            ),
        ).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        pair = VGroup(fig, formulas).arrange(RIGHT, buff=0.42, aligned_edge=UP)
        self.stack_below(pair, restate, buff=0.14)
        pair.set_x(0)
        self._nudge(pair)
        self.play(FadeIn(fig), run_time=0.7)
        self.pause_new_screen()
        for row in formulas:
            self.play(FadeIn(row), run_time=self.PAUSE_REWRITE)
            super().wait(self.PAUSE_COMPLEX)
        self.pause_conclusion()

        self.play(FadeOut(formulas), run_time=0.40)
        fig0 = self._hit_figure(theta=0.0, show_angle=False)
        fig0.move_to(fig)
        check0 = VGroup(
            self._line(
                MathTex(r"\theta=0", font_size=26, color=YELLOW),
                "のときは",
                MathTex(r"\sin 0=0", font_size=26),
                font_size=16,
            ),
            self.ja_text("中心が線の上にない限り、交わりません。", font_size=16),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        check0.next_to(fig0, RIGHT, buff=0.42)
        check0.align_to(fig0, UP)
        self._nudge(VGroup(fig0, check0))
        self.play(FadeOut(fig), FadeIn(fig0), FadeIn(check0), run_time=0.65)
        fig = fig0
        self.linger("θ=0 のときは sin 0=0 で、中心が線の上にない限り交わりません。")
        self.pause_short_formula()

        fig90 = self._hit_figure(theta=PI / 2)
        fig90.move_to(fig)
        check90 = VGroup(
            self._line(
                MathTex(r"\theta=\dfrac{\pi}{2}", font_size=26, color=YELLOW),
                "のときは",
                MathTex(r"\sin\dfrac{\pi}{2}=1", font_size=26),
                font_size=16,
            ),
            self._line(
                MathTex(r"x\le\dfrac{L}{2}", font_size=26, color=YELLOW),
                "なら交わります。",
                font_size=16,
            ),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        check90.next_to(fig90, RIGHT, buff=0.42)
        check90.align_to(fig90, UP)
        self._nudge(VGroup(fig90, check90))
        self.play(FadeOut(fig), FadeIn(fig90), FadeOut(check0), FadeIn(check90), run_time=0.65)
        fig = fig90
        self.linger("θ=π/2 のときは sin(π/2)=1 で、x≤L/2 なら交わります。")
        self.pause_short_formula()

        self.play(FadeOut(VGroup(fig, check90)), run_time=0.45)
        self.pause_topic()

        note = self.ja_text(
            "角度が寝ていると、届く垂直成分は小さいです。立っていると大きいです。",
            font_size=18,
        )
        self.stack_below(note, restate, buff=0.16)
        note.set_x(0)
        self._fit(note, 13.0)
        note.set_x(0)
        self.play(FadeIn(note), run_time=0.55)
        self.linger(note.text)

    def part_step3_area(self):
        chip = self.begin_step("STEP 3  配置の面積", self.header)

        lead = self._line(
            MathTex(r"(x,\theta)", font_size=22),
            "の動ける長方形のうち、交わる領域の面積を出します。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger("(x,θ) の動ける長方形のうち、交わる領域の面積を出します。")

        restate = self._line(
            MathTex(r"0\le\theta\le\pi", font_size=22, color=YELLOW),
            "、",
            MathTex(r"0\le x\le\dfrac{D}{2}", font_size=22, color=TEAL),
            "。",
            font_size=18,
        )
        self.stack_below(restate, lead, buff=0.10)
        restate.set_x(0)
        self.play(FadeIn(restate), run_time=0.55)
        self.pause_short_formula()
        self.linger("θ は 0 から π、x は 0 から D/2。")
        self.play(FadeOut(lead), run_time=0.40)

        plot = self._config_plot()
        self.stack_below(plot, restate, buff=0.14)
        plot.set_x(0)
        self._nudge(plot)
        cap = self._line(
            "横が",
            MathTex(r"\theta", font_size=20),
            "、縦が",
            MathTex(r"x", font_size=20),
            "です。交わる領域は曲線の下側です。",
            font_size=16,
        )
        self._fit(cap, 13.0)
        self.stack_below(cap, plot, buff=0.16)
        cap.set_x(0)
        self.play(FadeIn(plot), run_time=0.8)
        self.pause_new_screen()
        self.play(FadeIn(cap), run_time=0.55)
        self.linger("横が θ、縦が x です。交わる領域は曲線の下側です。")
        self.linger(3.2)

        self.play(FadeOut(VGroup(plot, cap)), run_time=0.45)
        self.pause_topic()

        row1 = self._line(
            "全部の配置の面積は",
            MathTex(r"\pi\cdot\dfrac{D}{2}=\dfrac{\pi D}{2}", font_size=28, color=YELLOW),
            font_size=18,
        )
        self.stack_below(row1, restate, buff=0.12)
        row1.set_x(0)
        self._fit(row1, 12.8)
        row1.set_x(0)
        self.play(FadeIn(row1), run_time=self.PAUSE_REWRITE)
        self.pause_complex()

        row2 = self._line(
            "交わる領域の面積は",
            MathTex(
                r"\displaystyle\int_{0}^{\pi}\dfrac{L}{2}\sin\theta\,d\theta",
                font_size=28,
                color=ORANGE,
            ),
            font_size=18,
        )
        self.stack_below(row2, row1, buff=0.12)
        row2.set_x(0)
        self._fit(row2, 12.8)
        row2.set_x(0)
        self.play(FadeIn(row2), run_time=self.PAUSE_REWRITE)
        self.pause_complex()

        self.play(FadeOut(VGroup(row1, row2)), run_time=0.40)

        sin_plot = self._sin_area_plot()
        self.stack_below(sin_plot, restate, buff=0.12)
        sin_plot.set_x(0)
        self._nudge(sin_plot)
        sin_txt = self._line(
            "正弦のグラフの下の面積として見ます。",
            MathTex(r"0", font_size=20),
            "から",
            MathTex(r"\pi", font_size=20),
            "まで、高さは",
            MathTex(r"0", font_size=20),
            "から",
            MathTex(r"1", font_size=20),
            "に上がってまた",
            MathTex(r"0", font_size=20),
            "です。",
            font_size=16,
        )
        self._fit(sin_txt, 13.0)
        self.stack_below(sin_txt, sin_plot, buff=0.14)
        sin_txt.set_x(0)
        self.play(FadeIn(sin_plot), run_time=0.7)
        self.pause_new_screen()
        self.play(FadeIn(sin_txt), run_time=0.55)
        self.linger("正弦のグラフの下の面積として見ます。0 から π まで、高さは 0 から 1 に上がってまた 0 です。")
        self.linger(3.2)
        self.play(FadeOut(VGroup(sin_plot, sin_txt)), run_time=0.40)
        self.pause_topic()

        algebra = [
            self._line(
                MathTex(r"\cos\pi=-1", font_size=26),
                "、",
                MathTex(r"\cos 0=1", font_size=26),
                font_size=18,
            ),
            MathTex(
                r"\int_{0}^{\pi}\sin\theta\,d\theta=\bigl[-\cos\theta\bigr]_{0}^{\pi}",
                font_size=28,
            ),
            MathTex(
                r"-\cos\pi-(-\cos 0)=-(-1)-(-1)=1+1=2",
                font_size=26,
                color=YELLOW,
            ),
            MathTex(
                r"\bigl[-\cos\theta\bigr]_{0}^{\pi}=-(-1)-(-1)=2",
                font_size=28,
                color=YELLOW,
            ),
            self._line(
                "だから交わる面積は",
                MathTex(r"\dfrac{L}{2}\cdot 2=L", font_size=28, color=ORANGE),
                font_size=18,
            ),
            self._line(
                "交わる割合は",
                MathTex(
                    r"\dfrac{L}{\pi D/2}=\dfrac{2L}{\pi D}",
                    font_size=30,
                    color=YELLOW,
                ),
                font_size=18,
            ),
        ]
        eval_rows = algebra[:4]
        block1 = self._formula_rows(eval_rows, restate, buff=0.10, hold=self.PAUSE_COMPLEX)
        self.pause_conclusion()
        self.play(FadeOut(block1), run_time=0.40)
        self.pause_topic()

        result_rows = algebra[4:]
        block2 = self._formula_rows(result_rows, restate, buff=0.12, hold=self.PAUSE_CONCLUSION)
        self.pause_conclusion()
        self.play(FadeOut(block2), run_time=0.40)
        self.pause_topic()

        note = self._line(
            "円周率は、角度",
            MathTex(r"\theta", font_size=22),
            "の範囲が",
            MathTex(r"0", font_size=22),
            "から",
            MathTex(r"\pi", font_size=22),
            "であることと、",
            MathTex(r"\sin\theta", font_size=22),
            "の面積から入ります。",
            font_size=16,
        )
        self.stack_below(note, restate, buff=0.14)
        note.set_x(0)
        self._fit(note, 13.0)
        note.set_x(0)
        self.play(FadeIn(note), run_time=0.55)
        self.linger("円周率は、角度 θ の範囲が 0 から π であることと、sinθ の面積から入ります。")

    def part_step4_solve(self):
        chip = self.begin_step("STEP 4  円周率", self.header)

        lead = self.ja_text(
            "交わる割合を実験で置き換えて、円周率について解きます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        restate = self._line(
            "割合",
            MathTex(r"p=\dfrac{2L}{\pi D}", font_size=26, color=YELLOW),
            "。",
            font_size=18,
        )
        self.stack_below(restate, lead, buff=0.10)
        restate.set_x(0)
        self.play(FadeIn(restate), run_time=0.55)
        self.pause_short_formula()
        self.linger("割合 p は 2L を πD で割った値です。")

        first = [
            self._line(
                MathTex(r"N", font_size=24),
                "回落として、交わる回数を",
                MathTex(r"C", font_size=24, color=ORANGE),
                "とおく",
                font_size=18,
            ),
            MathTex(r"\dfrac{C}{N}\approx\dfrac{2L}{\pi D}", font_size=32, color=YELLOW),
            self._line(
                MathTex(r"\dfrac{C}{N}=\dfrac{2L}{\pi D}", font_size=28),
                "とおく",
                font_size=18,
            ),
            self._line(
                "両辺に",
                MathTex(r"\pi D", font_size=24),
                "を掛ける",
                font_size=18,
            ),
            MathTex(r"\dfrac{C}{N}\cdot\pi D=2L", font_size=30),
        ]
        block1 = self._formula_rows(first, restate, buff=0.10, hold=self.PAUSE_REWRITE)
        self.pause_complex()
        self.play(FadeOut(block1), run_time=0.40)
        self.pause_topic()

        second = [
            self._line(
                "両辺に",
                MathTex(r"N", font_size=24),
                "を掛ける",
                font_size=18,
            ),
            MathTex(r"C\cdot\pi D=2LN", font_size=30),
            self._line(
                "両辺を",
                MathTex(r"C D", font_size=24),
                "で割る",
                font_size=18,
            ),
            MathTex(r"\pi=\dfrac{2LN}{CD}", font_size=32, color=YELLOW),
            MathTex(r"\pi\approx\dfrac{2LN}{CD}", font_size=32, color=GREEN),
        ]
        block2 = self._formula_rows(second, restate, buff=0.10, hold=self.PAUSE_REWRITE)
        self.pause_conclusion()
        self.play(FadeOut(block2), run_time=0.45)
        self.pause_topic()

        note = self.ja_text(
            "針と線だけの実験なのに円周率が出るのは、角度の範囲と正弦の面積に半円の分が入るからです。",
            font_size=18,
        )
        self.stack_below(note, restate, buff=0.16)
        note.set_x(0)
        self._fit(note, 13.0)
        note.set_x(0)
        self.play(FadeIn(note), run_time=0.55)
        self.linger(note.text)

    def part_example(self):
        chip = self.begin_step("実例", self.header)

        lead = self._line(
            MathTex(r"L=D", font_size=24, color=YELLOW),
            "とおいて、公式と 1 回分の図を最後まで通します。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger("L=D とおいて、公式と 1 回分の図を最後まで通します。")

        fig = self._floor(
            specs=[(0.05, 1 * self.FLOOR_GAP + 0.06, 1.15)],
            show_d=True,
            show_l=True,
            needle_len=self.FLOOR_GAP * 0.98,
        )
        self.stack_below(fig, lead, buff=0.14)
        fig.set_x(0)
        self._nudge(fig)
        cap = self._line(
            "長さと間隔を同じにします。",
            MathTex(r"L=D", font_size=22, color=YELLOW),
            font_size=16,
        )
        self._fit(cap, 13.0)
        self.stack_below(cap, fig, buff=0.16)
        cap.set_x(0)
        self.play(FadeIn(fig), FadeIn(cap), run_time=0.7)
        self.pause_new_screen()
        self.linger("長さと間隔を同じにします。")
        self.linger(3.2)

        self.play(FadeOut(VGroup(fig, cap)), run_time=0.45)
        self.pause_topic()

        rows = [
            MathTex(r"p=\dfrac{2D}{\pi D}=\dfrac{2}{\pi}", font_size=32, color=YELLOW),
            MathTex(r"\dfrac{2}{\pi}\approx 0.637", font_size=30),
            MathTex(r"\pi\approx\dfrac{2N}{C}", font_size=32, color=GREEN),
        ]
        block = self._formula_rows(rows, lead, buff=0.12, hold=self.PAUSE_COMPLEX)
        self.pause_conclusion()
        self.play(FadeOut(block), run_time=0.40)
        self.pause_topic()

        table = self.aligned_table(
            [
                [
                    self.ja_text("量", font_size=16, color=GREY_B),
                    self.ja_text("値", font_size=16, color=GREY_B),
                ],
                [
                    self.ja_text("交わる割合", font_size=20),
                    MathTex(r"\dfrac{2}{\pi}", font_size=28, color=YELLOW),
                ],
                [
                    self.ja_text("円周率の見積もり", font_size=20),
                    MathTex(r"\dfrac{2N}{C}", font_size=28, color=GREEN),
                ],
            ],
            h_buff=0.36,
            v_buff=0.10,
        )
        table.scale(0.88)
        self.stack_below(table, lead, buff=0.14)
        table.set_x(0)
        self.reveal_table(table, row_wait=1.20)

        notes = [
            self.ja_text(
                "長さと間隔が同じなら、およそ 10 回に 6 回は線と交わります。",
                font_size=18,
            ),
            self._line(
                "交わる回数",
                MathTex(r"C", font_size=22, color=ORANGE),
                "が多いほど、見積もりの分母が大きくなり、円周率の値は安定します。",
                font_size=16,
            ),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, table, buff=0.12)
            else:
                self.stack_below(mob, shown, buff=0.10)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            shown.add(mob)
            if i == 0:
                self.linger(mob.text)
            else:
                self.linger("交わる回数 C が多いほど、見積もりの分母が大きくなり、円周率の値は安定します。")

    def part_generalize(self):
        chip = self.begin_step("一般化", self.header)

        lead = self.ja_text(
            "今やったことは、配置の全体を面積と見て、条件を満たす部分の面積の比を確率にする、という考え方でした。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        first = [
            self._line(
                MathTex(r"x", font_size=22, color=TEAL),
                "と",
                MathTex(r"\theta", font_size=22, color=YELLOW),
                "は一様。交わるのは",
                MathTex(r"x\le\dfrac{L}{2}\sin\theta", font_size=26, color=YELLOW),
                "。",
                font_size=16,
            ),
            self.ja_text(
                "幾何確率と呼ばれます。ビュフォンの針の問題が、この型です。無作為な配置を何度も作る方法は、モンテカルロ法の原型でもあります。",
                font_size=16,
            ),
            MathTex(r"p=\dfrac{2L}{\pi D}", font_size=32, color=YELLOW),
            MathTex(r"\pi\approx\dfrac{2LN}{CD}", font_size=32, color=GREEN),
        ]
        block = self._formula_rows(first, lead, buff=0.10, hold=self.PAUSE_CONCLUSION)
        self.play(FadeOut(VGroup(lead, block)), run_time=0.45)
        self.pause_topic()

        name = self.ja_text("ビュフォンの針", font_size=22, color=GREY_B)
        self.below_chip(name, chip, buff=0.16)
        self.play(FadeIn(name), run_time=0.55)
        self.linger(name.text)

        close = [
            self.ja_text(
                "確率は回数の極限ではなく、配置空間の面積の比として先に決まります。実験はその比を読む方法です。",
                font_size=18,
            ),
        ]
        self._formula_rows(close, name, buff=0.12, hold=self.PAUSE_CONCLUSION)

    def part_summary(self):
        chip = self.begin_step("まとめ", self.header)

        rows = [
            self._line(
                "針の置き方は、近い線からの距離",
                MathTex(r"x", font_size=22, color=TEAL),
                "と角度",
                MathTex(r"\theta", font_size=22, color=YELLOW),
                "で書けます",
                font_size=16,
            ),
            self._line(
                "交わる条件は",
                MathTex(r"x\le\dfrac{L}{2}\sin\theta", font_size=24, color=YELLOW),
                "です",
                font_size=16,
            ),
            self._line(
                "全部の配置の面積は",
                MathTex(r"\dfrac{\pi D}{2}", font_size=24),
                "、交わる面積は",
                MathTex(r"L", font_size=24, color=ORANGE),
                "、比は",
                MathTex(r"\dfrac{2L}{\pi D}", font_size=24, color=YELLOW),
                font_size=16,
            ),
            self._line(
                "実験の交わる回数から、",
                MathTex(r"\pi\approx\dfrac{2LN}{CD}", font_size=24, color=GREEN),
                "と読めます",
                font_size=16,
            ),
        ]
        shown = VGroup()
        for i, mob in enumerate(rows):
            if i == 0:
                self.below_chip(mob, chip, buff=0.22)
            else:
                self.stack_below(mob, shown, buff=0.14)
            self._fit_left(mob)
            self.play(FadeIn(mob), run_time=0.70)
            shown.add(mob)
            self.pause_conclusion()

        trivia = self._line(
            "針を短くして",
            MathTex(r"L=\dfrac{D}{2}", font_size=20, color=GREY_B),
            "とおくと、交わる割合は",
            MathTex(r"\dfrac{1}{\pi}", font_size=20, color=GREY_B),
            "です。10 回に 3 回ほどしか交わらないので、同じ回数でも見積もりのばらつきは大きくなります。",
            font_size=14,
            color=GREY_B,
        )
        self.stack_below(trivia, shown, buff=0.22)
        self._fit_left(trivia)
        self.play(FadeIn(trivia), run_time=0.70)
        self.linger(
            "針を短くして L=D/2 とおくと、交わる割合は 1/π です。10 回に 3 回ほどしか交わらないので、同じ回数でも見積もりのばらつきは大きくなります。",
            extra=0.40,
        )
        self.pause_conclusion()

    def _needle(self, center, length, angle, color=ORANGE, stroke_width=5.5, dot_r=0.065):
        c = np.array(center, dtype=float)
        if c.shape[0] == 2:
            c = np.array([c[0], c[1], 0.0])
        hx = (length / 2.0) * np.cos(angle)
        hy = (length / 2.0) * np.sin(angle)
        p1 = c + np.array([-hx, -hy, 0.0])
        p2 = c + np.array([hx, hy, 0.0])
        bar = Line(p1, p2, color=color, stroke_width=stroke_width)
        d1 = Dot(p1, radius=dot_r, color=color)
        d2 = Dot(p2, radius=dot_r, color=color)
        grp = VGroup(bar, d1, d2)
        grp.bar = bar
        grp.end_a = d1
        grp.end_b = d2
        return grp

    def _align_needles(self, needles):
        y = needles[0].bar.get_center()[1]
        for n in needles:
            n.shift(UP * (y - n.bar.get_center()[1]))
        return needles

    def _floor(self, specs=(), width=None, gap=None, n_lines=None, show_d=False, show_l=False, needle_len=None):
        width = self.FLOOR_W if width is None else width
        gap = self.FLOOR_GAP if gap is None else gap
        n_lines = self.FLOOR_N if n_lines is None else n_lines
        needle_len = self.NEEDLE_LEN if needle_len is None else needle_len
        lines = VGroup()
        for i in range(n_lines):
            y = i * gap
            lines.add(
                Line(
                    np.array([-width / 2, y, 0.0]),
                    np.array([width / 2, y, 0.0]),
                    color=GREY_B,
                    stroke_width=2.5,
                )
            )
        needles = VGroup()
        for cx, cy, ang in specs:
            needles.add(self._needle(np.array([cx, cy, 0.0]), needle_len, ang))
        extras = VGroup()
        if show_d and n_lines >= 2:
            x0 = -width / 2 - 0.22
            y0 = 0.0
            y1 = gap
            arr = DoubleArrow(
                np.array([x0, y0, 0.0]),
                np.array([x0, y1, 0.0]),
                color=TEAL,
                stroke_width=2.0,
                tip_length=0.12,
                buff=0.0,
            )
            d_lab = MathTex(r"D", font_size=22, color=TEAL)
            d_lab.next_to(arr, LEFT, buff=0.08)
            extras.add(arr, d_lab)
        if show_l and len(needles) > 0:
            l_lab = MathTex(r"L", font_size=20, color=ORANGE)
            bar = needles[0].bar
            mid = bar.get_center()
            dxy = bar.get_end() - bar.get_start()
            nrm = np.array([-dxy[1], dxy[0], 0.0])
            ln = np.linalg.norm(nrm)
            if ln > 1e-8:
                nrm = nrm / ln * 0.22
            l_lab.move_to(mid + nrm)
            extras.add(l_lab)
        body = VGroup(lines, needles, extras)
        frame = Rectangle(
            width=width + 1.10,
            height=(n_lines - 1) * gap + 0.85,
            stroke_opacity=0.0,
            fill_opacity=0.0,
        )
        frame.move_to(body.get_center())
        grp = VGroup(frame, body)
        grp.move_to(ORIGIN)
        return grp

    def _coord_figure(self):
        line_w = 3.50
        gap = 1.55
        low = Line(LEFT * line_w / 2, RIGHT * line_w / 2, color=GREY_B, stroke_width=3.0)
        high = low.copy().shift(UP * gap)
        x_vis = 0.52
        center = UP * x_vis
        theta = 0.70
        half = 0.72
        needle = self._needle(center, 2 * half, theta)
        cdot = Dot(center, radius=0.07, color=YELLOW)
        x_seg = DashedLine(center, ORIGIN, color=TEAL, stroke_width=2.5)
        x_lab = MathTex(r"x", font_size=22, color=TEAL)
        x_lab.next_to(x_seg, RIGHT, buff=0.10)
        href = DashedLine(center + LEFT * 1.05, center + RIGHT * 1.15, color=GREY_A, stroke_width=1.6)
        h_arm = Line(center, center + RIGHT * 1.05, color=GREY_A)
        p2 = needle.bar.get_end()
        if (p2 - center)[0] < 0:
            p2 = needle.bar.get_start()
        n_arm = Line(center, p2, color=ORANGE)
        mark = Angle(h_arm, n_arm, radius=0.34, color=YELLOW, stroke_width=4.0)
        th = MathTex(r"\theta", font_size=20, color=YELLOW)
        th.move_to(center + 0.52 * np.array([np.cos(theta / 2), np.sin(theta / 2), 0.0]))
        d_arr = DoubleArrow(
            high.get_left() + LEFT * 0.18,
            low.get_left() + LEFT * 0.18,
            color=TEAL,
            stroke_width=2.0,
            tip_length=0.12,
            buff=0.0,
        )
        d_lab = MathTex(r"D", font_size=20, color=TEAL)
        d_lab.next_to(d_arr, LEFT, buff=0.06)
        frame = Rectangle(width=4.40, height=2.55, stroke_opacity=0.0, fill_opacity=0.0)
        body = VGroup(low, high, href, needle, cdot, x_seg, x_lab, h_arm, n_arm, mark, th, d_arr, d_lab)
        body.move_to(ORIGIN)
        frame.move_to(body)
        return VGroup(frame, body)

    def _hit_figure(self, theta=0.70, show_angle=True):
        line_w = 3.70
        floor = Line(LEFT * line_w / 2, RIGHT * line_w / 2, color=GREY_B, stroke_width=3.0)
        x_vis = 0.55
        half_l = 0.85
        center = UP * x_vis
        needle = self._needle(center, 2 * half_l, theta)
        cdot = Dot(center, radius=0.07, color=YELLOW)
        x_seg = DashedLine(center, ORIGIN, color=TEAL, stroke_width=2.5)
        x_lab = MathTex(r"x", font_size=22, color=TEAL)
        x_lab.next_to(x_seg, RIGHT, buff=0.08)
        parts = [floor, needle, cdot, x_seg, x_lab]
        reach = half_l * np.sin(theta)
        if reach > 0.08:
            reach_end = center + DOWN * reach
            reach_seg = DashedLine(center, reach_end, color=ORANGE, stroke_width=2.2)
            reach_lab = MathTex(r"\dfrac{L}{2}\sin\theta", font_size=20, color=ORANGE)
            reach_lab.next_to(reach_seg, LEFT, buff=0.10)
            parts.extend([reach_seg, reach_lab])
        if show_angle and theta > 0.08:
            href = DashedLine(center + LEFT * 1.10, center + RIGHT * 1.10, color=GREY_A, stroke_width=1.5)
            h_arm = Line(center, center + RIGHT * 1.05, color=GREY_A)
            p2 = needle.bar.get_end()
            if (p2 - center)[0] < 0:
                p2 = needle.bar.get_start()
            n_arm = Line(center, p2, color=ORANGE)
            mark = Angle(h_arm, n_arm, radius=0.32, color=YELLOW, stroke_width=3.5)
            th = MathTex(r"\theta", font_size=20, color=YELLOW)
            th.move_to(center + 0.50 * np.array([np.cos(theta / 2), np.sin(theta / 2), 0.0]))
            half_lab = MathTex(r"\dfrac{L}{2}", font_size=18, color=ORANGE)
            mid = (center + p2) / 2
            half_lab.move_to(mid + 0.22 * np.array([-np.sin(theta), np.cos(theta), 0.0]))
            parts.extend([href, h_arm, n_arm, mark, th, half_lab])
        frame = Rectangle(width=4.35, height=2.70, stroke_opacity=0.0, fill_opacity=0.0)
        body = VGroup(*parts)
        body.move_to(ORIGIN)
        frame.move_to(body)
        return VGroup(frame, body)

    def _config_plot(self, l_frac=0.72):
        w, h = 4.35, 2.20

        def to_pt(theta, x_over_d2):
            px = -w / 2 + (theta / PI) * w
            py = -h / 2 + x_over_d2 * h
            return np.array([px, py, 0.0])

        rect = Rectangle(width=w, height=h, color=GREY_B, stroke_width=2.0)
        rect.set_fill(GREY_E, 0.20)
        ts = np.linspace(0.0, PI, 64)
        pts = [to_pt(t, l_frac * np.sin(t)) for t in ts]
        curve = VMobject(color=ORANGE, stroke_width=3.5)
        curve.set_points_smoothly(pts)
        area_pts = [to_pt(0.0, 0.0)] + pts + [to_pt(PI, 0.0)]
        area = Polygon(*area_pts, color=ORANGE, fill_opacity=0.38, stroke_width=0)
        zero = MathTex(r"0", font_size=18)
        zero.next_to(rect.get_corner(DL), DOWN, buff=0.08)
        pi_t = MathTex(r"\pi", font_size=18)
        pi_t.next_to(rect.get_corner(DR), DOWN, buff=0.08)
        th_lab = MathTex(r"\theta", font_size=22)
        th_lab.next_to(pi_t, RIGHT, buff=0.14)
        x_lab = MathTex(r"x", font_size=22)
        x_lab.next_to(rect, LEFT, buff=0.42)
        d2 = MathTex(r"\dfrac{D}{2}", font_size=18, color=TEAL)
        d2.next_to(rect.get_corner(UL), LEFT, buff=0.08)
        eq = MathTex(r"x=\dfrac{L}{2}\sin\theta", font_size=18, color=ORANGE)
        eq.move_to(to_pt(0.78 * PI, 0.86))
        return VGroup(rect, area, curve, zero, pi_t, th_lab, x_lab, d2, eq)

    def _sin_area_plot(self):
        w, h = 3.80, 1.45

        def to_pt(theta, y):
            px = -w / 2 + (theta / PI) * w
            py = -h / 2 + y * h
            return np.array([px, py, 0.0])

        rect = Rectangle(width=w, height=h, color=GREY_B, stroke_width=2.0)
        ts = np.linspace(0.0, PI, 64)
        pts = [to_pt(t, np.sin(t)) for t in ts]
        curve = VMobject(color=YELLOW, stroke_width=3.2)
        curve.set_points_smoothly(pts)
        area_pts = [to_pt(0.0, 0.0)] + pts + [to_pt(PI, 0.0)]
        area = Polygon(*area_pts, color=YELLOW, fill_opacity=0.35, stroke_width=0)
        zero = MathTex(r"0", font_size=16)
        zero.next_to(rect.get_corner(DL), DOWN, buff=0.06)
        pi_t = MathTex(r"\pi", font_size=16)
        pi_t.next_to(rect.get_corner(DR), DOWN, buff=0.06)
        th_lab = MathTex(r"\theta", font_size=18)
        th_lab.next_to(pi_t, RIGHT, buff=0.12)
        y_lab = MathTex(r"\sin\theta", font_size=18, color=YELLOW)
        y_lab.next_to(rect, LEFT, buff=0.12)
        one = MathTex(r"1", font_size=16)
        one.next_to(rect.get_corner(UL), LEFT, buff=0.08)
        return VGroup(rect, area, curve, zero, pi_t, th_lab, y_lab, one)

    def _show_notes(self, notes, under, buff=0.14):
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, under, buff=buff)
            else:
                self.stack_below(mob, shown, buff=0.10)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            shown.add(mob)
            self.linger(getattr(mob, "text", 2.0))
        return shown

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
