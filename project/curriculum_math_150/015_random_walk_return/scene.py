from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import LessonScene


class RandomWalkReturn(LessonScene):
    """#15 酔歩は出発点に戻るか（約9分）"""

    CELL_1D = 0.62
    CELL_2D = 0.46
    ISO_X = 0.72
    ISO_Y = 0.50
    ISO_Z = 0.64
    ISO_D = 0.16
    MARK_R = 0.10

    def construct(self):
        self.header = self._open_header()
        self.part_question()
        self.part_trial_1d()
        self.part_trial_2d()
        self.part_step1_two_steps()
        self.part_step2_must_cross()
        self.part_step3_2d()
        self.part_step4_3d()
        self.part_example()
        self.part_generalize()
        self.part_summary()

    def _open_header(self):
        title = self.ja_text("酔歩は出発点に戻るか", font_size=36)
        self.play(FadeIn(title), run_time=0.8)
        self.pause_new_screen()
        self.linger(1.5)
        self.play(title.animate.scale(0.52).to_edge(UP, buff=0.16), run_time=0.5)
        title.set_x(0)
        return title

    def part_question(self):
        fig = self._fig_1d(current=None, arrows=True, walk_marks=False)
        cap = self.ja_text(
            "直線上を、毎ステップ左右へ同じ確からしさで 1 歩歩きます。",
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

        q1 = self.ja_text("いつかは出発点に戻るのでしょうか。", font_size=20)
        self.stack_below(q1, pair, buff=0.22)
        q1.set_x(0)
        self._fit(q1, 13.0)
        q1.set_x(0)
        self.play(FadeIn(q1), run_time=0.7)
        self.linger(q1.text)

        q2 = self.ja_text("平面や空間でも、同じでしょうか。", font_size=20)
        self.stack_below(q2, q1, buff=0.14)
        q2.set_x(0)
        self._fit(q2, 13.0)
        q2.set_x(0)
        self.play(FadeIn(q2), run_time=0.7)
        self.linger(q2.text, extra=0.35)

    def part_trial_1d(self):
        chip = self.begin_step("試行  1 次元", self.header)

        lead = self.ja_text(
            "まず、直線上で数歩だけ歩いて、出発点に戻るかを見ます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)
        self.play(FadeOut(lead), run_time=0.45)

        walks = [
            ([1, -1], "右、左。2 歩で出発点に戻ります。"),
            ([1, 1], "右、右。2 歩では出発点に戻りません。"),
            ([-1, 1], "左、右。2 歩で出発点に戻ります。"),
        ]
        fig, cap = self._play_1d_walk(walks[0][0], walks[0][1], chip, prev=None)
        for steps, text in walks[1:]:
            fig, cap = self._play_1d_walk(steps, text, chip, prev=(fig, cap))

        self.play(FadeOut(VGroup(fig, cap)), run_time=0.45)
        self.pause_topic()

        table = self.aligned_table(
            [
                [
                    self.ja_text("経路", font_size=16, color=GREY_B),
                    self.ja_text("2 歩で戻るか", font_size=16, color=GREY_B),
                ],
                [
                    self.ja_text("右左", font_size=20),
                    self.ja_text("戻る", font_size=20, color=GREEN),
                ],
                [
                    self.ja_text("右右", font_size=20),
                    self.ja_text("戻らない", font_size=20),
                ],
                [
                    self.ja_text("左右", font_size=20),
                    self.ja_text("戻る", font_size=20, color=GREEN),
                ],
            ],
            h_buff=0.40,
            v_buff=0.12,
        )
        table.scale(0.90)
        self.below_chip(table, chip, buff=0.20)
        table.set_x(0)
        self.reveal_table(table, row_wait=1.20)

        notes = [
            self.ja_text(
                "短い実験だと、戻る経路と戻らない経路がどちらも出ます。",
                font_size=18,
            ),
            self.ja_text(
                "いつかは必ず戻るかは、数歩だけでは決まりません。",
                font_size=18,
            ),
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
            self.play(FadeIn(mob), run_time=0.55)
            shown.add(mob)
            self.linger(mob.text)

    def part_trial_2d(self):
        chip = self.begin_step("試行  2 次元", self.header)

        lead = self.ja_text(
            "平面の格子でも、近くをうろつくので、いつかは出発点に戻れそう、と思ってみます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)
        self.play(FadeOut(lead), run_time=0.45)

        path = [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0), (0, -1), (1, -1), (1, 0)]
        fig = self._fig_2d(path=path, current=path[-1])
        fig.scale(0.88)
        self.below_chip(fig, chip, buff=0.18)
        fig.set_x(0)
        self._nudge(fig)
        cap = self.ja_text(
            "数歩の経路が、すでに自分自身と交差して見えます。",
            font_size=18,
        )
        self._fit(cap, 13.0)
        self.stack_below(cap, fig, buff=0.36)
        cap.set_x(0)
        self.play(FadeIn(fig), FadeIn(cap), run_time=0.8)
        self.pause_new_screen()
        self.linger(cap.text)

        notes = [
            self.ja_text(
                "2 次元でも、足跡が重なって見えるので、戻れそうに感じます。",
                font_size=18,
            ),
            self.ja_text(
                "3 次元の隙間は、この平面の図からはまだ見えません。",
                font_size=18,
            ),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, cap, buff=0.12)
            else:
                self.stack_below(mob, shown, buff=0.10)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            shown.add(mob)
            self.linger(mob.text)

    def part_step1_two_steps(self):
        chip = self.begin_step("STEP 1  2 歩", self.header)

        lead = self.ja_text(
            "直線上の 2 歩を、全部の経路として数えます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        rows = [
            self._line(
                "各歩は右か左。確率はどちらも",
                MathTex(r"\dfrac{1}{2}", font_size=28, color=YELLOW),
                "です。各歩は独立です。",
                font_size=18,
            ),
            self._line(
                "2 歩の経路は",
                MathTex(r"2^{2}=4", font_size=30, color=YELLOW),
                "通りです。",
                font_size=18,
            ),
            self.ja_text("右右、右左、左右、左左。", font_size=18),
            self.ja_text("戻るのは右左と左右の 2 通りです。", font_size=18),
            self._line(
                "戻る確率は",
                MathTex(r"\dfrac{2}{4}=\dfrac{1}{2}", font_size=30, color=GREEN),
                "です。",
                font_size=18,
            ),
            self.ja_text("戻る割合は、全部の経路を数える方法で出します。", font_size=18),
        ]
        block = self._formula_rows(rows, lead, buff=0.12, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(block), run_time=0.45)
        self.pause_topic()

        notes = [
            self.ja_text(
                "偶数歩でないと、直線上では出発点に戻れません。1 歩では戻れない、と確認します。",
                font_size=18,
            ),
            self.ja_text("2 歩では、半分の経路が戻ります。", font_size=18),
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
            self.linger(mob.text)

    def part_step2_must_cross(self):
        chip = self.begin_step("STEP 2  横切る", self.header)

        lead = self.ja_text(
            "1 次元では、遠くへ行く経路も、戻るときに出発点を通らずには通れません。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        restate = self.ja_text("左右の差が、そのときの位置です。", font_size=18)
        self.stack_below(restate, lead, buff=0.10)
        restate.set_x(0)
        self.play(FadeIn(restate), run_time=0.55)
        self.pause_short_formula()
        self.linger(restate.text)
        self.play(FadeOut(lead), run_time=0.45)

        fig = self._fig_polyline()
        fig.scale(0.92)
        self.stack_below(fig, restate, buff=0.16)
        fig.set_x(0)
        self._nudge(fig)
        cap = self.ja_text(
            "右に 3 歩したあと左へ戻る折線です。途中で必ず位置 0 を通ります。",
            font_size=18,
        )
        self._fit(cap, 13.0)
        self.stack_below(cap, fig, buff=0.36)
        cap.set_x(0)
        self.play(FadeIn(fig), FadeIn(cap), run_time=0.7)
        self.pause_new_screen()
        self.linger(cap.text)

        self.play(FadeOut(VGroup(fig, cap)), run_time=0.45)
        self.pause_topic()

        rows = [
            self.ja_text("位置は、右の回数引く左の回数です。", font_size=18),
            self.ja_text("右へ行ったあと左へ戻るには、途中で差が 0 になります。", font_size=18),
            self.ja_text("だから 1 次元の軌跡は、出発点を何度も横切りやすいです。", font_size=18),
        ]
        block = self._formula_rows(rows, restate, buff=0.12, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(block), run_time=0.45)
        self.pause_topic()

        notes = [
            self.ja_text(
                "進める向きが左右しかないので、足跡は同じ線の上に重なります。",
                font_size=18,
            ),
            self.ja_text(
                "長く歩くほど、どこかで差が 0 になる機会が増えます。",
                font_size=18,
            ),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, restate, buff=0.16)
            else:
                self.stack_below(mob, shown, buff=0.10)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            shown.add(mob)
            self.linger(mob.text)

    def part_step3_2d(self):
        chip = self.begin_step("STEP 3  2 次元", self.header)

        lead = self.ja_text(
            "平面では上下左右の 4 方向ですが、足跡はまだ面の上で交差しやすいです。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        restate = self._line(
            "各歩は 4 方向です。確率はどれも",
            MathTex(r"\dfrac{1}{4}", font_size=28, color=YELLOW),
            "です。",
            font_size=18,
        )
        self.stack_below(restate, lead, buff=0.10)
        restate.set_x(0)
        self.play(FadeIn(restate), run_time=0.55)
        self.pause_short_formula()
        self.linger("各歩は 4 方向です。確率はどれも 1/4 です。")
        self.play(FadeOut(lead), run_time=0.45)

        path = [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0), (0, -1), (1, -1), (1, 0)]
        fig = self._fig_2d(path=path, current=path[-1], n=2)
        fig.scale(0.82)
        self.stack_below(fig, restate, buff=0.14)
        fig.set_x(0)
        self._nudge(fig)
        cap = self.ja_text(
            "格子上の経路が自分自身と交差します。2 次元でも、面はまだ薄いです。",
            font_size=18,
        )
        self._fit(cap, 13.0)
        self.stack_below(cap, fig, buff=0.36)
        cap.set_x(0)
        self.play(FadeIn(fig), FadeIn(cap), run_time=0.7)
        self.pause_new_screen()
        self.linger(cap.text)

        self.play(FadeOut(VGroup(fig, cap)), run_time=0.45)
        self.pause_topic()

        rows = [
            self.ja_text("2 歩で戻るには、往復の 1 組です。方向の選び方は限られます。", font_size=18),
            self.ja_text(
                "それでも面全体を埋めるほどは広がらず、あとから同じ点を踏みやすいです。",
                font_size=18,
            ),
        ]
        block = self._formula_rows(rows, restate, buff=0.12, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(block), run_time=0.45)
        self.pause_topic()

        notes = [
            self.ja_text(
                "2 次元は、1 次元ほど強制ではないが、隙間がすぐには残らない、という中間です。",
                font_size=18,
            ),
            self.ja_text(
                "厳密な証明では、戻る確率を級数で書いて、その級数が発散するか収束するかを見ます。今回は高校で使う範囲として、次元ごとの経路の広がりまでとします。",
                font_size=16,
            ),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, restate, buff=0.16)
            else:
                self.stack_below(mob, shown, buff=0.10)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            shown.add(mob)
            self.linger(mob.text)

    def part_step4_3d(self):
        chip = self.begin_step("STEP 4  3 次元", self.header)

        lead = self.ja_text(
            "空間では、前・後ろの方向が加わり、通らなかった格子点が残りやすくなります。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        restate = self._line(
            "各歩は 6 方向です。確率はどれも",
            MathTex(r"\dfrac{1}{6}", font_size=28, color=YELLOW),
            "です。",
            font_size=18,
        )
        self.stack_below(restate, lead, buff=0.10)
        restate.set_x(0)
        self.play(FadeIn(restate), run_time=0.55)
        self.pause_short_formula()
        self.linger("各歩は 6 方向です。確率はどれも 1/6 です。")
        self.play(FadeOut(lead), run_time=0.45)

        fig = self._fig_3d()
        fig.scale(0.88)
        self.stack_below(fig, restate, buff=0.14)
        fig.set_x(0)
        self._nudge(fig)
        cap = self.ja_text(
            "1 本の経路が角を曲がって隣の層へ抜けます。元の平面には、戻らない隙間が残ります。",
            font_size=16,
        )
        self._fit(cap, 13.0)
        self.stack_below(cap, fig, buff=0.32)
        cap.set_x(0)
        self.play(FadeIn(fig), FadeIn(cap), run_time=0.7)
        self.pause_new_screen()
        self.linger(cap.text)

        self.play(FadeOut(VGroup(fig, cap)), run_time=0.45)
        self.pause_topic()

        rows = [
            self.ja_text("同じ歩数でも、選べる方向が増えます。", font_size=18),
            self.ja_text("一度外れた層へ行くと、出発点の平面に戻る必要がありません。", font_size=18),
            self.ja_text("だから、戻らない経路の割合が、1 次元より明らかに大きいです。", font_size=18),
        ]
        block = self._formula_rows(rows, restate, buff=0.10, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(block), run_time=0.45)
        self.pause_topic()

        notes = [
            self._line(
                "3 次元以上では、いつかは戻る確率は",
                MathTex(r"p_{d}<1", font_size=26, color=YELLOW),
                "です。戻らない確率が正です。いつかは必ず戻る、とは言えません。",
                font_size=16,
            ),
            self._line(
                "1 次元と 2 次元では、重なりが多く、",
                MathTex(r"p_{1}=p_{2}=1", font_size=26, color=GREEN),
                "でいつかは戻ります。",
                font_size=16,
            ),
            self.ja_text(
                "厳密な証明では、戻る確率を級数で書いて、その級数が発散するか収束するかを見ます。今回は高校で使う範囲として、次元ごとの経路の広がりまでとします。",
                font_size=16,
            ),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, restate, buff=0.14)
            else:
                self.stack_below(mob, shown, buff=0.10)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            shown.add(mob)
            if i < 2:
                self.pause_conclusion()
            else:
                self.linger(mob.text)

    def part_example(self):
        chip = self.begin_step("実例", self.header)

        lead = self.ja_text(
            "1 次元の 4 歩を、戻る／戻らないまで数えます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        rows = [
            self._line(
                "4 歩の経路は",
                MathTex(r"2^{4}=16", font_size=30, color=YELLOW),
                "通りです。",
                font_size=18,
            ),
            self.ja_text("出発点にいるのは、右を 2 回、左を 2 回選ぶ経路です。", font_size=18),
            self._line(
                "4 歩のうち右を 2 回選ぶ:",
                MathTex(r"\dbinom{4}{2}=\dfrac{4\cdot 3}{2\cdot 1}=6", font_size=28, color=YELLOW),
                font_size=16,
            ),
            self._line(
                "確率は",
                MathTex(r"\dfrac{6}{16}=\dfrac{3}{8}", font_size=30, color=GREEN),
                "です。",
                font_size=18,
            ),
        ]
        block = self._formula_rows(rows, lead, buff=0.10, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(block), run_time=0.45)
        self.pause_topic()

        table = self.aligned_table(
            [
                [
                    self.ja_text("歩数", font_size=14, color=GREY_B),
                    self.ja_text("全経路", font_size=14, color=GREY_B),
                    self.ja_text("出発点にいる経路", font_size=14, color=GREY_B),
                    self.ja_text("割合", font_size=14, color=GREY_B),
                ],
                [
                    MathTex(r"2", font_size=24),
                    MathTex(r"4", font_size=24),
                    MathTex(r"2", font_size=24),
                    MathTex(r"\dfrac{1}{2}", font_size=24, color=YELLOW),
                ],
                [
                    MathTex(r"4", font_size=24),
                    MathTex(r"16", font_size=24),
                    MathTex(r"6", font_size=24),
                    MathTex(r"\dfrac{3}{8}", font_size=24, color=GREEN),
                ],
            ],
            h_buff=0.28,
            v_buff=0.10,
        )
        table.scale(0.88)
        self.stack_below(table, lead, buff=0.14)
        table.set_x(0)
        self.reveal_table(table, row_wait=1.20)

        notes = [
            self._line(
                "4 歩の時点では、出発点にいる割合は",
                MathTex(r"\dfrac{3}{8}", font_size=24, color=GREEN),
                "で、2 歩の",
                MathTex(r"\dfrac{1}{2}", font_size=24, color=YELLOW),
                "より小さいです。",
                font_size=16,
            ),
            self.ja_text(
                "時点での滞在と、いつかは戻ることとは別です。1 次元では、あとから戻る分がまだ残ります。",
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
            self.linger(
                "4 歩の時点では、出発点にいる割合は 3/8 で、2 歩の 1/2 より小さいです。"
                if i == 0
                else mob.text
            )

    def part_generalize(self):
        chip = self.begin_step("一般化", self.header)

        lead = self.ja_text(
            "今やったことは、格子上の酔歩が出発点へ戻るかどうかが、次元で変わる、という考え方でした。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        first = [
            self.ja_text("各方向は同じ確からしさです。各歩は独立です。", font_size=18),
            self._line(
                "格子",
                MathTex(r"\mathbb{Z}^{d}", font_size=26, color=YELLOW),
                "の隣へ、同じ確からしさで歩くとします。",
                font_size=16,
            ),
            self._line(
                "出発点へいつか戻る確率を",
                MathTex(r"p_{d}", font_size=28, color=YELLOW),
                "とおく。",
                font_size=18,
            ),
            self.ja_text("ポリアの定理と呼ばれます。主張は次の式です。", font_size=16),
            MathTex(
                r"p_{1}=p_{2}=1,\qquad p_{d}<1\quad(d\ge 3)",
                font_size=28,
                color=YELLOW,
            ),
        ]
        block = self._formula_rows(first, lead, buff=0.10, hold=self.PAUSE_CONCLUSION)
        self.play(FadeOut(VGroup(lead, block)), run_time=0.45)
        self.pause_topic()

        name = self.ja_text(
            "次元が低いと経路が重なり、次元が高いと隙間が残ります。戻る／戻らないの差は、この重なり方です。",
            font_size=18,
        )
        self.below_chip(name, chip, buff=0.16)
        self._fit_left(name)
        self.play(FadeIn(name), run_time=0.55)
        self.linger(name.text)

        close = [
            self._line(
                "厳密な証明では",
                MathTex(r"p_{d}", font_size=22, color=GREY_B),
                "を級数で書きます。今回は主張の式までとします。",
                font_size=16,
                color=GREY_B,
            ),
        ]
        self._formula_rows(close, name, buff=0.12, hold=self.PAUSE_COMPLEX)

    def part_summary(self):
        chip = self.begin_step("まとめ", self.header)

        rows = [
            self.ja_text(
                "1 次元の 2 歩では、4 通りのうち 2 通りが出発点に戻ります",
                font_size=18,
            ),
            self.ja_text(
                "1 次元では進める向きが線しかないので、足跡が重なり、いつかは出発点を横切ります",
                font_size=16,
            ),
            self._line(
                "2 次元でも面の上で交差しやすく、",
                MathTex(r"p_{2}=1", font_size=24, color=GREEN),
                "で戻ります",
                font_size=16,
            ),
            self._line(
                "ポリアの定理:",
                MathTex(r"p_{1}=p_{2}=1", font_size=22, color=GREEN),
                "、",
                MathTex(r"d\ge 3", font_size=22, color=YELLOW),
                "では",
                MathTex(r"p_{d}<1", font_size=22, color=YELLOW),
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

        trivia = self.ja_text(
            "同じ格子でも、各歩でその場に留まる、という待ちを入れると、戻るまでにかかる歩数の平均は変わります。戻るかどうかの次元の境は、単純な左右上下前後の酔歩の話です。",
            font_size=16,
            color=GREY_B,
        )
        self.stack_below(trivia, shown, buff=0.22)
        self._fit_left(trivia)
        self.play(FadeIn(trivia), run_time=0.70)
        self.linger(trivia.text, extra=0.40)
        self.pause_conclusion()

    def _play_1d_walk(self, steps, text, chip, prev=None):
        states = self._walk_states(steps)
        visited0, current0 = states[0]
        fig = self._fig_1d(visited=visited0, current=current0)
        if prev is None:
            self.below_chip(fig, chip, buff=0.22)
            fig.set_x(0)
            self._nudge(fig)
        else:
            old_fig, old_cap = prev
            fig.move_to(old_fig)
            self.play(FadeOut(old_fig), FadeOut(old_cap), run_time=0.65)
        cap = self.ja_text(text, font_size=18)
        self._fit(cap, 13.0)
        self.stack_below(cap, fig, buff=0.40)
        cap.set_x(0)
        self.play(FadeIn(fig), FadeIn(cap), run_time=0.7)
        self.pause_new_screen()
        for visited, current in states[1:]:
            nxt = self._fig_1d(visited=visited, current=current)
            nxt.move_to(fig)
            self.play(FadeOut(fig), FadeIn(nxt), run_time=0.55)
            fig = nxt
        self.linger(text)
        return fig, cap

    def _walk_states(self, steps):
        visited = [0]
        pos = 0
        states = [(list(visited), pos)]
        for step in steps:
            pos += step
            visited.append(pos)
            states.append((list(visited), pos))
        return states

    def _pt1(self, i):
        return i * self.CELL_1D * RIGHT

    def _pt2(self, x, y):
        return x * self.CELL_2D * RIGHT + y * self.CELL_2D * UP

    def _iso(self, x, y, z):
        return (x * self.ISO_X - y * self.ISO_Y) * RIGHT + (
            z * self.ISO_Z + (x + y) * self.ISO_D
        ) * UP

    def _mark(self, point, current=False, radius=None):
        if radius is None:
            radius = self.MARK_R
        stroke = YELLOW if current else GREY_B
        width = 5.0 if current else 2.0
        circ = Circle(radius=radius, color=stroke, stroke_width=width)
        circ.set_fill(GREY_E, 0.70)
        circ.move_to(point)
        return circ

    def _fig_1d(
        self,
        visited=None,
        current=0,
        arrows=False,
        walk_marks=True,
        xmin=-3,
        xmax=3,
    ):
        if visited is None:
            visited = [0]
        axis = Line(self._pt1(xmin) + 0.18 * LEFT, self._pt1(xmax) + 0.18 * RIGHT, color=GREY_B, stroke_width=2.0)
        ticks = VGroup()
        labels = VGroup()
        marks = VGroup()
        for i in range(xmin, xmax + 1):
            p = self._pt1(i)
            ticks.add(Line(p + 0.12 * UP, p + 0.12 * DOWN, color=GREY_B, stroke_width=1.6))
            lab = MathTex(rf"{i}", font_size=18)
            lab.next_to(p, DOWN, buff=0.26)
            labels.add(lab)
            if walk_marks:
                marks.add(self._mark(p, current=(current is not None and i == current)))
            elif i == 0:
                marks.add(self._mark(p, current=False))
        path_parts = VGroup()
        if len(visited) >= 2:
            corners = [self._pt1(v) for v in visited]
            path = VMobject(color=ORANGE, stroke_width=4.0)
            path.set_points_as_corners(corners)
            path_parts.add(path)
        extras = VGroup()
        if arrows:
            origin = self._pt1(0)
            left_arr = Arrow(
                origin + 0.32 * LEFT + 0.42 * UP,
                origin + 1.20 * LEFT + 0.42 * UP,
                buff=0,
                color=BLUE_B,
                stroke_width=3.5,
                max_tip_length_to_length_ratio=0.22,
            )
            right_arr = Arrow(
                origin + 0.32 * RIGHT + 0.42 * UP,
                origin + 1.20 * RIGHT + 0.42 * UP,
                buff=0,
                color=BLUE_B,
                stroke_width=3.5,
                max_tip_length_to_length_ratio=0.22,
            )
            extras.add(left_arr, right_arr)
        if len(marks) > 0:
            y = marks[0].get_y()
            for mark in marks:
                mark.set_y(y)
        return VGroup(axis, ticks, path_parts, marks, extras, labels)

    def _fig_2d(self, path=None, current=None, n=2):
        if path is None:
            path = [(0, 0)]
        parts = VGroup()
        for i in range(-n, n + 1):
            parts.add(
                Line(
                    self._pt2(i, -n),
                    self._pt2(i, n),
                    color=GREY_D,
                    stroke_width=1.2,
                )
            )
            parts.add(
                Line(
                    self._pt2(-n, i),
                    self._pt2(n, i),
                    color=GREY_D,
                    stroke_width=1.2,
                )
            )
        if len(path) >= 2:
            poly = VMobject(color=ORANGE, stroke_width=4.0)
            poly.set_points_as_corners([self._pt2(x, y) for x, y in path])
            parts.add(poly)
        marks = VGroup()
        by_row = {}
        by_col = {}
        for x in range(-n, n + 1):
            for y in range(-n, n + 1):
                is_cur = current is not None and (x, y) == current
                mark = self._mark(self._pt2(x, y), current=is_cur)
                marks.add(mark)
                by_row.setdefault(y, []).append(mark)
                by_col.setdefault(x, []).append(mark)
        for row in by_row.values():
            y0 = row[0].get_y()
            for mark in row:
                mark.set_y(y0)
        for col in by_col.values():
            x0 = col[0].get_x()
            for mark in col:
                mark.set_x(x0)
        parts.add(marks)
        return parts

    def _fig_polyline(self):
        positions = [0, 1, 2, 3, 2, 1, 0]
        sx, sy = 0.70, 0.46

        def pt(t, y):
            return t * sx * RIGHT + y * sy * UP

        axis_t = Line(pt(-0.25, 0), pt(6.35, 0), color=GREY_B, stroke_width=2.0)
        axis_y = Line(pt(0, -0.25), pt(0, 3.45), color=GREY_B, stroke_width=2.0)
        t_labs = VGroup()
        for t in range(0, 7):
            tick = Line(pt(t, -0.08), pt(t, 0.08), color=GREY_B, stroke_width=1.4)
            lab = MathTex(rf"{t}", font_size=16)
            lab.next_to(pt(t, 0), DOWN, buff=0.22)
            t_labs.add(tick, lab)
        y_labs = VGroup()
        for y in range(0, 4):
            tick = Line(pt(-0.08, y), pt(0.08, y), color=GREY_B, stroke_width=1.4)
            lab = MathTex(rf"{y}", font_size=16)
            lab.next_to(pt(0, y), LEFT, buff=0.14)
            y_labs.add(tick, lab)
        lab_t = self.ja_text("歩数", font_size=14, color=GREY_B)
        lab_t.next_to(axis_t, RIGHT, buff=0.10)
        lab_y = self.ja_text("位置", font_size=14, color=GREY_B)
        lab_y.next_to(axis_y.get_top(), LEFT, buff=0.12)
        poly = VMobject(color=ORANGE, stroke_width=4.0)
        poly.set_points_as_corners([pt(t, y) for t, y in enumerate(positions)])
        marks = VGroup()
        by_height = {}
        for t, y in enumerate(positions):
            mark = self._mark(pt(t, y), current=(t == len(positions) - 1), radius=0.09)
            marks.add(mark)
            by_height.setdefault(y, []).append(mark)
        for row in by_height.values():
            y0 = row[0].get_y()
            for mark in row:
                mark.set_y(y0)
        return VGroup(axis_t, axis_y, t_labs, y_labs, lab_t, lab_y, poly, marks)

    def _fig_3d(self):
        parts = VGroup()
        for i in range(3):
            parts.add(Line(self._iso(0, i, 0), self._iso(2, i, 0), color=GREY_D, stroke_width=1.3))
            parts.add(Line(self._iso(i, 0, 0), self._iso(i, 2, 0), color=GREY_D, stroke_width=1.3))
        for x, y in ((1, 1), (2, 1), (2, 2), (1, 2)):
            parts.add(Line(self._iso(x, y, 0), self._iso(x, y, 1), color=GREY_D, stroke_width=1.2))
        top = [(1, 1), (2, 1), (2, 2), (1, 2), (1, 1)]
        for a, b in zip(top, top[1:]):
            parts.add(
                Line(
                    self._iso(a[0], a[1], 1),
                    self._iso(b[0], b[1], 1),
                    color=GREY_D,
                    stroke_width=1.2,
                )
            )
        path_coords = [(1, 1, 0), (2, 1, 0), (2, 2, 0), (2, 2, 1)]
        poly = VMobject(color=ORANGE, stroke_width=4.0)
        poly.set_points_as_corners([self._iso(*c) for c in path_coords])
        parts.add(poly)
        current = path_coords[-1]
        marks = VGroup()
        for x in range(3):
            for y in range(3):
                p = (x, y, 0)
                marks.add(self._mark(self._iso(*p), current=False, radius=0.08))
        for x, y in ((1, 1), (2, 1), (2, 2), (1, 2)):
            p = (x, y, 1)
            marks.add(self._mark(self._iso(*p), current=(p == current), radius=0.08))
        parts.add(marks)
        return parts

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
