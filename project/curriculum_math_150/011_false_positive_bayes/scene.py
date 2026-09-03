from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import LessonScene


class FalsePositiveBayes(LessonScene):
    """#11 陽性が出ても病気とは限らないのはなぜか（約9分）"""

    def construct(self):
        self.header = self._open_header()
        self.part_question()
        self.part_trial_almost()
        self.part_trial_people()
        self.part_step1_rules()
        self.part_step2_prior()
        self.part_step3_test()
        self.part_step4_posterior()
        self.part_example()
        self.part_generalize()
        self.part_summary()

    def _open_header(self):
        title = self.ja_text("陽性が出ても病気とは限らないのはなぜか", font_size=36)
        self.play(FadeIn(title), run_time=0.8)
        self.pause_new_screen()
        self.linger(1.5)
        self.play(title.animate.scale(0.52).to_edge(UP, buff=0.16), run_time=0.5)
        title.set_x(0)
        return title

    def part_question(self):
        fig = self._kit()
        cap = self.ja_text(
            "ある病気は、1 万人に 1 人の割合であるとおく。",
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

        q1 = self.ja_text(
            "検査は、病気の人にも、病気でない人にも、99 パーセント正しく判定するとおく。",
            font_size=20,
        )
        self.stack_below(q1, pair, buff=0.22)
        q1.set_x(0)
        self._fit(q1, 13.0)
        q1.set_x(0)
        self.play(FadeIn(q1), run_time=0.7)
        self.linger(q1.text)

        q2 = self.ja_text(
            "陽性が出た人が、本当にその病気である確率は、どれくらいでしょうか。",
            font_size=20,
        )
        self.stack_below(q2, q1, buff=0.14)
        q2.set_x(0)
        self._fit(q2, 13.0)
        q2.set_x(0)
        self.play(FadeIn(q2), run_time=0.7)
        self.linger(q2.text, extra=0.35)

    def part_trial_almost(self):
        chip = self.begin_step("試行  ほぼ病気", self.header)

        lead = self.ja_text(
            "まず、検査が 99 パーセント正しい、という数字だけに目を向けてみます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        rows = [
            self._line(
                "検査が正しい割合を",
                MathTex(r"99\%", font_size=28, color=YELLOW),
                "とおく。",
                font_size=18,
            ),
            self._line(
                "だから、陽性が出たら、病気である確率も",
                MathTex(r"99\%", font_size=28, color=YELLOW),
                "だと思ってしまいます。",
                font_size=18,
            ),
            self.ja_text(
                "1 万人に 1 人、という事前の稀さは、まだ使っていません。",
                font_size=18,
            ),
        ]
        block = self._formula_rows(rows, lead, buff=0.12, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(block), run_time=0.45)
        self.pause_topic()

        table = self.aligned_table(
            [
                [
                    self.ja_text("考え方", font_size=16, color=GREY_B),
                    self.ja_text("陽性のとき病気である確率", font_size=16, color=GREY_B),
                ],
                [
                    self.ja_text("検査が当たる割合と同じ", font_size=20),
                    MathTex(r"99\%", font_size=28, color=YELLOW),
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
            self.ja_text(
                "検査が当たる割合と、陽性の人が病気である割合を、同じものと見ています。",
                font_size=18,
            ),
            self.ja_text(
                "この問いが欲しいのは、陽性が出たという条件のもとで、本当に病気である確率です。",
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

    def part_trial_people(self):
        chip = self.begin_step("試行  1 万人", self.header)

        lead = self.ja_text(
            "こんどは、1 万人を人数のまま並べて、病気の人と病気でない人を数えてみます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)
        self.play(FadeOut(lead), run_time=0.45)

        fig = self._people_row(highlight="sick")
        self.below_chip(fig, chip, buff=0.22)
        fig.set_x(0)
        cap = self._line(
            "1 万人のうち、病気の人は",
            MathTex(r"1", font_size=26, color=YELLOW),
            "人",
            font_size=18,
        )
        self._fit(cap, 13.0)
        self.stack_below(cap, fig, buff=0.40)
        cap.set_x(0)
        self.play(FadeIn(fig), FadeIn(cap), run_time=0.7)
        self.pause_new_screen()
        self.linger("1 万人のうち、病気の人は 1 人")

        nxt = self._people_row(highlight="well")
        nxt.move_to(fig)
        new_cap = self._line(
            "病気でない人は",
            MathTex(r"10000-1=9999", font_size=28, color=ORANGE),
            "人",
            font_size=18,
        )
        self._fit(new_cap, 13.0)
        self.stack_below(new_cap, nxt, buff=0.40)
        new_cap.set_x(0)
        self.play(FadeOut(fig), FadeIn(nxt), FadeOut(cap), run_time=0.65)
        fig = nxt
        cap = new_cap
        self.play(FadeIn(cap), run_time=0.55)
        self.linger("病気でない人は 10000-1=9999 人")

        nxt = self._people_row(highlight=None)
        nxt.move_to(fig)
        new_cap = self.ja_text(
            "人数を見ただけでは、陽性が何人出るかはまだ分かりません。",
            font_size=18,
        )
        self._fit(new_cap, 13.0)
        self.stack_below(new_cap, nxt, buff=0.40)
        new_cap.set_x(0)
        self.play(FadeOut(fig), FadeIn(nxt), FadeOut(cap), run_time=0.65)
        fig = nxt
        cap = new_cap
        self.play(FadeIn(cap), run_time=0.55)
        self.linger(new_cap.text)

        self.play(FadeOut(VGroup(fig, cap)), run_time=0.45)
        self.pause_topic()

        table = self.aligned_table(
            [
                [
                    self.ja_text("グループ", font_size=16, color=GREY_B),
                    self.ja_text("人数", font_size=16, color=GREY_B),
                ],
                [
                    self.ja_text("病気", font_size=20),
                    MathTex(r"1", font_size=28, color=YELLOW),
                ],
                [
                    self.ja_text("病気でない", font_size=20),
                    MathTex(r"9999", font_size=28, color=ORANGE),
                ],
            ],
            h_buff=0.36,
            v_buff=0.10,
        )
        table.scale(0.88)
        self.below_chip(table, chip, buff=0.20)
        table.set_x(0)
        self.reveal_table(table, row_wait=1.20)

        notes = [
            self.ja_text(
                "病気の人は 1 人しかいません。病気でない人の方が、ずっと多いです。",
                font_size=18,
            ),
            self.ja_text(
                "検査の正しさを使う前に、この人数の差を残しておきます。",
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

    def part_step1_rules(self):
        chip = self.begin_step("STEP 1  決まり", self.header)

        lead = self.ja_text(
            "陽性が出たときに病気である確率を出すために、検査の決まりを、先に言葉で書いておきます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        defs = [
            self._line(
                "人数を",
                MathTex(r"10000", font_size=26, color=YELLOW),
                "人とおく。",
                font_size=18,
            ),
            self._line(
                "病気の人の人数を",
                MathTex(r"1", font_size=26, color=YELLOW),
                "とおく。病気でない人の人数を",
                MathTex(r"9999", font_size=26, color=ORANGE),
                "とおく。",
                font_size=18,
            ),
            self._line(
                "感度を、病気の人が陽性になる割合とおく。値は",
                MathTex(r"99\%=\dfrac{99}{100}", font_size=26, color=GREEN),
                font_size=16,
            ),
            self._line(
                "特異度を、病気でない人が陰性になる割合とおく。値は",
                MathTex(r"99\%=\dfrac{99}{100}", font_size=26, color=GREEN),
                font_size=16,
            ),
            self._line(
                "条件付き確率",
                MathTex(r"P(A\mid B)", font_size=26, color=YELLOW),
                "を、「",
                MathTex(r"B", font_size=24),
                "が起きたという条件のもとでの、",
                MathTex(r"A", font_size=24),
                "の割合」とおく。",
                font_size=16,
            ),
        ]
        block = self._formula_rows(defs, lead, buff=0.12)
        self.pause_conclusion()
        self.play(FadeOut(block), run_time=0.45)
        self.pause_topic()

        notes = [
            self.ja_text(
                "感度と特異度は、別の条件のもとでの正しさです。同じ 99 パーセントでも、分母になるグループが違います。",
                font_size=18,
            ),
            self.ja_text(
                "陽性の人が病気である割合は、まだ出していません。",
                font_size=18,
            ),
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

    def part_step2_prior(self):
        chip = self.begin_step("STEP 2  検査の前", self.header)

        lead = self.ja_text("検査をする前の人数を、表に残します。", font_size=18)
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        restate = self._line(
            "人数",
            MathTex(r"10000", font_size=24, color=YELLOW),
            "。病気",
            MathTex(r"1", font_size=24, color=YELLOW),
            "。病気でない",
            MathTex(r"9999", font_size=24, color=ORANGE),
            "。",
            font_size=18,
        )
        self.stack_below(restate, lead, buff=0.10)
        restate.set_x(0)
        self.play(FadeIn(restate), run_time=0.55)
        self.pause_short_formula()
        self.linger("人数 10000。病気 1。病気でない 9999。")
        self.play(FadeOut(lead), run_time=0.45)

        rows = [
            self._line(
                "病気である確率は",
                MathTex(r"\dfrac{1}{10000}", font_size=30, color=YELLOW),
                "です。",
                font_size=20,
            ),
            self._line(
                "病気でない確率は",
                MathTex(r"\dfrac{9999}{10000}", font_size=30, color=ORANGE),
                "です。",
                font_size=20,
            ),
        ]
        block = self._formula_rows(rows, restate, buff=0.14, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(block), run_time=0.45)
        self.pause_topic()

        table = self.aligned_table(
            [
                [
                    self.ja_text("グループ", font_size=16, color=GREY_B),
                    self.ja_text("人数", font_size=16, color=GREY_B),
                    self.ja_text("割合", font_size=16, color=GREY_B),
                ],
                [
                    self.ja_text("病気", font_size=20),
                    MathTex(r"1", font_size=26, color=YELLOW),
                    MathTex(r"\dfrac{1}{10000}", font_size=26, color=YELLOW),
                ],
                [
                    self.ja_text("病気でない", font_size=20),
                    MathTex(r"9999", font_size=26, color=ORANGE),
                    MathTex(r"\dfrac{9999}{10000}", font_size=26, color=ORANGE),
                ],
            ],
            h_buff=0.32,
            v_buff=0.10,
        )
        table.scale(0.86)
        self.stack_below(table, restate, buff=0.14)
        table.set_x(0)
        self.reveal_table(table, row_wait=1.20)

        notes = [
            self.ja_text("検査の前では、病気の人は 1 万人に 1 人です。", font_size=18),
            self.ja_text("この割合が、あとで陽性の人数の分母に効きます。", font_size=18),
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
            self.linger(mob.text)

    def part_step3_test(self):
        chip = self.begin_step("STEP 3  検査のあと", self.header)

        lead = self.ja_text(
            "感度と特異度を、人数に掛けて、陽性になる人を数えます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        restate = VGroup(
            self._line(
                "感度",
                MathTex(r"\dfrac{99}{100}", font_size=24, color=GREEN),
                "。特異度",
                MathTex(r"\dfrac{99}{100}", font_size=24, color=GREEN),
                "。",
                font_size=18,
            ),
            self._line(
                "病気でない人が陽性になる割合は",
                MathTex(r"1-\dfrac{99}{100}=\dfrac{1}{100}", font_size=26, color=ORANGE),
                font_size=18,
            ),
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        self.stack_below(restate, lead, buff=0.10)
        restate.set_x(0)
        self._fit(restate, 13.0)
        restate.set_x(0)
        self.play(FadeIn(restate), run_time=0.55)
        self.pause_short_formula()
        self.linger("病気でない人が陽性になる割合は 1-99/100=1/100")
        self.play(FadeOut(lead), run_time=0.45)

        first = [
            self._line(
                "病気の人で陽性になる人数は",
                MathTex(r"1\cdot\dfrac{99}{100}=\dfrac{99}{100}", font_size=28, color=YELLOW),
                font_size=18,
            ),
        ]
        block = self._formula_rows(first, restate, buff=0.12, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(block), run_time=0.45)
        self.pause_topic()

        switch = [
            self.ja_text(
                "表では人数を整数に揃えるため、1 万人のかわりに 100 万人で同じ割合を使う、とおく。",
                font_size=16,
            ),
            self._line(
                "病気の人は",
                MathTex(r"100", font_size=24, color=YELLOW),
                "人、病気でない人は",
                MathTex(r"999900", font_size=24, color=ORANGE),
                "人。",
                font_size=18,
            ),
            self._line(
                "真の陽性は",
                MathTex(r"100\cdot\dfrac{99}{100}=99", font_size=28, color=GREEN),
                "人。",
                font_size=18,
            ),
            self._line(
                "偽の陽性は",
                MathTex(r"999900\cdot\dfrac{1}{100}=9999", font_size=28, color=ORANGE),
                "人。",
                font_size=18,
            ),
        ]
        block2 = self._formula_rows(switch, restate, buff=0.12, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(VGroup(restate, block2)), run_time=0.45)
        self.pause_topic()

        fig = self._count_blocks()
        self.below_chip(fig, chip, buff=0.22)
        fig.set_x(0)
        cap = self.ja_text(
            "偽の陽性は 9999 人です。真の陽性の 99 人より、ずっと多いです。",
            font_size=18,
        )
        self._fit(cap, 13.0)
        self.stack_below(cap, fig, buff=0.40)
        cap.set_x(0)
        self.play(FadeIn(fig), FadeIn(cap), run_time=0.7)
        self.pause_new_screen()
        self.linger(cap.text)

        new_cap = self.ja_text(
            "陽性が出た人のほとんどは、病気でない側から来ています。",
            font_size=18,
        )
        self._fit(new_cap, 13.0)
        self.stack_below(new_cap, fig, buff=0.40)
        new_cap.set_x(0)
        self.play(FadeOut(cap), run_time=0.45)
        cap = new_cap
        self.play(FadeIn(cap), run_time=0.55)
        self.linger(cap.text)

    def part_step4_posterior(self):
        chip = self.begin_step("STEP 4  陽性のうち", self.header)

        lead = self.ja_text(
            "陽性が出た人だけを分母にして、そのうち病気の人の割合を出します。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        restate = self._line(
            "真の陽性",
            MathTex(r"99", font_size=24, color=GREEN),
            "。偽の陽性",
            MathTex(r"9999", font_size=24, color=ORANGE),
            "。",
            font_size=18,
        )
        self.stack_below(restate, lead, buff=0.10)
        restate.set_x(0)
        self.play(FadeIn(restate), run_time=0.55)
        self.pause_short_formula()
        self.linger("真の陽性 99。偽の陽性 9999。")
        self.play(FadeOut(lead), run_time=0.45)

        first = [
            self._line(
                "陽性の人の合計は",
                MathTex(r"99+9999=10098", font_size=28, color=YELLOW),
                font_size=18,
            ),
            self._line(
                "そのうち病気の人は",
                MathTex(r"99", font_size=28, color=GREEN),
                font_size=18,
            ),
            self._line(
                "陽性が出たという条件のもとで、病気である確率は",
                MathTex(r"\dfrac{99}{10098}", font_size=30, color=YELLOW),
                font_size=16,
            ),
        ]
        block = self._formula_rows(first, restate, buff=0.10, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(block), run_time=0.45)
        self.pause_topic()

        second = [
            MathTex(
                r"\dfrac{99}{10098}=\dfrac{99\div 99}{10098\div 99}=\dfrac{1}{102}",
                font_size=30,
                color=YELLOW,
            ),
            self._line(
                "パーセントにすると、約",
                MathTex(r"0.98\%", font_size=28, color=YELLOW),
                "。99 パーセントではありません。",
                font_size=18,
            ),
        ]
        block2 = self._formula_rows(second, restate, buff=0.12, hold=self.PAUSE_CONCLUSION)
        self.play(FadeOut(VGroup(restate, block2)), run_time=0.45)
        self.pause_topic()

        table = self.aligned_table(
            [
                [
                    self.ja_text("考え方", font_size=16, color=GREY_B),
                    self.ja_text("陽性のとき病気である確率", font_size=16, color=GREY_B),
                ],
                [
                    self.ja_text("検査が当たる割合と同じ、と思ったとき", font_size=18),
                    MathTex(r"99\%", font_size=26, color=GREY_B),
                ],
                [
                    self.ja_text("陽性の人数で割ったとき", font_size=18),
                    MathTex(r"\dfrac{99}{10098}", font_size=26, color=YELLOW),
                ],
            ],
            h_buff=0.32,
            v_buff=0.08,
        )
        table.scale(0.84)
        self.below_chip(table, chip, buff=0.18)
        table.set_x(0)
        self.reveal_table(table, row_wait=1.20)

        symbol = self._line(
            "A を病気、B を陽性、とおくと、",
            MathTex(r"P(A\mid B)=\dfrac{99}{10098}", font_size=28, color=YELLOW),
            "です。",
            font_size=18,
        )
        self.stack_below(symbol, table, buff=0.12)
        symbol.set_x(0)
        self._fit(symbol, 13.0)
        symbol.set_x(0)
        self.play(FadeIn(symbol), run_time=0.55)
        self.pause_conclusion()
        self.linger("A を病気、B を陽性、とおくと、P(A|B)=99/10098 です。")

        notes = [
            self.ja_text(
                "陽性が出た人 10098 人のうち、病気の人は 99 人です。",
                font_size=18,
            ),
            self.ja_text(
                "検査が 99 パーセント正しくても、事前が稀だと、陽性のほとんどは偽陽性です。",
                font_size=18,
            ),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, symbol, buff=0.12)
            else:
                self.stack_below(mob, shown, buff=0.10)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            shown.add(mob)
            self.linger(mob.text)

    def part_example(self):
        chip = self.begin_step("実例", self.header)

        lead = self.ja_text(
            "100 万人の表を、上から順に最後まで数えます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        restate = self._line(
            MathTex(r"N=1000000", font_size=24, color=YELLOW),
            "とおく。病気",
            MathTex(r"100", font_size=24, color=YELLOW),
            "人。感度",
            MathTex(r"\dfrac{99}{100}", font_size=24, color=GREEN),
            "。特異度",
            MathTex(r"\dfrac{99}{100}", font_size=24, color=GREEN),
            "。",
            font_size=16,
        )
        self.stack_below(restate, lead, buff=0.10)
        restate.set_x(0)
        self._fit(restate, 13.0)
        restate.set_x(0)
        self.play(FadeIn(restate), run_time=0.55)
        self.pause_short_formula()
        self.linger("N=1000000 とおく。病気 100 人。")
        self.play(FadeOut(lead), run_time=0.45)
        self.play(FadeOut(restate), run_time=0.45)

        table = self.aligned_table(
            [
                [
                    self.ja_text("グループ", font_size=14, color=GREY_B),
                    self.ja_text("人数", font_size=14, color=GREY_B),
                    self.ja_text("陽性", font_size=14, color=GREY_B),
                    self.ja_text("陰性", font_size=14, color=GREY_B),
                ],
                [
                    self.ja_text("病気", font_size=18),
                    MathTex(r"100", font_size=24),
                    MathTex(r"99", font_size=24, color=GREEN),
                    MathTex(r"1", font_size=24),
                ],
                [
                    self.ja_text("病気でない", font_size=18),
                    MathTex(r"999900", font_size=22),
                    MathTex(r"9999", font_size=24, color=ORANGE),
                    MathTex(r"989901", font_size=22),
                ],
                [
                    self.ja_text("合計", font_size=18),
                    MathTex(r"1000000", font_size=22),
                    MathTex(r"10098", font_size=24, color=YELLOW),
                    MathTex(r"989902", font_size=22),
                ],
            ],
            h_buff=0.22,
            v_buff=0.08,
        )
        table.scale(0.78)
        self.below_chip(table, chip, buff=0.18)
        table.set_x(0)
        self.reveal_table(table, row_wait=1.20)

        result = self._line(
            MathTex(r"\dfrac{99}{10098}", font_size=28, color=YELLOW),
            "。約",
            MathTex(r"0.98\%", font_size=28, color=YELLOW),
            "。",
            font_size=18,
        )
        self.stack_below(result, table, buff=0.12)
        result.set_x(0)
        self.play(FadeIn(result), run_time=0.55)
        self.pause_conclusion()
        self.linger("99/10098。約 0.98%。")

        notes = [
            self.ja_text(
                "陽性 10098 人のうち、病気は 99 人、病気でない人は 9999 人です。",
                font_size=18,
            ),
            self.ja_text(
                "99 パーセントという検査の正しさは、この表の各行の中での正しさです。陽性の列の中での正しさではありません。",
                font_size=16,
            ),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, result, buff=0.12)
            else:
                self.stack_below(mob, shown, buff=0.08)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            shown.add(mob)
            self.linger(mob.text)

    def part_generalize(self):
        chip = self.begin_step("一般化", self.header)

        lead = self.ja_text(
            "今やったことは、新しい情報のあとで、最初の人数の割合を付け替える考え方でした。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        first = [
            self._line(
                "事前の病気の割合を",
                MathTex(r"P(A)", font_size=26, color=YELLOW),
                "とおく。",
                font_size=18,
            ),
            self._line(
                "病気の人が陽性になる割合を",
                MathTex(r"P(B\mid A)", font_size=26, color=GREEN),
                "とおく。",
                font_size=18,
            ),
            self._line(
                "陽性が出る割合を",
                MathTex(r"P(B)", font_size=26, color=ORANGE),
                "とおく。",
                font_size=18,
            ),
            self.ja_text(
                "ベイズの定理と呼ばれます。陽性が出たという条件のもとで、病気である確率は次の式です。",
                font_size=16,
            ),
            MathTex(
                r"P(A\mid B)=\dfrac{P(B\mid A)\,P(A)}{P(B)}",
                font_size=34,
                color=YELLOW,
            ),
        ]
        block = self._formula_rows(first, lead, buff=0.10, hold=self.PAUSE_CONCLUSION)
        self.play(FadeOut(VGroup(lead, block)), run_time=0.45)
        self.pause_topic()

        name = self.ja_text(
            "A を病気、B を陽性、とおく。人数の割合を、検査のあとに付け替える、という方法です。",
            font_size=18,
            color=GREY_B,
        )
        self.below_chip(name, chip, buff=0.16)
        self._fit_left(name)
        self.play(FadeIn(name), run_time=0.55)
        self.linger(name.text)

        close = [
            self._line(
                MathTex(r"P(B)", font_size=24, color=ORANGE),
                "は、真の陽性と偽の陽性を足した割合です。",
                font_size=18,
            ),
            self._line(
                "感度",
                MathTex(r"P(B\mid A)", font_size=24, color=GREEN),
                "が高くても、",
                MathTex(r"P(A)", font_size=24, color=YELLOW),
                "が小さいと、",
                MathTex(r"P(A\mid B)", font_size=24, color=YELLOW),
                "は小さくなりえます。",
                font_size=16,
            ),
            self._line(
                "分母の",
                MathTex(r"P(B)", font_size=24, color=ORANGE),
                "に、病気でない人からの偽陽性が入ります。稀な病気では、この項が大きくなります。",
                font_size=16,
            ),
        ]
        self._formula_rows(close, name, buff=0.12)

    def part_summary(self):
        chip = self.begin_step("まとめ", self.header)

        rows = [
            self.ja_text(
                "検査が 99 パーセント正しいことと、陽性の人が病気であることは、同じ割合ではありません",
                font_size=18,
            ),
            self.ja_text(
                "感度は、病気の人のうち陽性になる割合です。特異度は、病気でない人のうち陰性になる割合です",
                font_size=16,
            ),
            self.ja_text(
                "陽性が出た人を分母にすると、偽陽性が本物より多いことがあります",
                font_size=18,
            ),
            self._line(
                MathTex(
                    r"P(A\mid B)=\dfrac{P(B\mid A)\,P(A)}{P(B)}",
                    font_size=24,
                    color=YELLOW,
                ),
                "。事前が稀だと、事後も小さくなりえます",
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
            "事前を 1 万人に 1 人ではなく、100 人に 1 人とすると、同じ検査でも真の陽性",
            MathTex(r"99", font_size=20, color=GREY_B),
            "人、偽の陽性",
            MathTex(r"99", font_size=20, color=GREY_B),
            "人となり、陽性のとき病気である確率は",
            MathTex(r"\dfrac{99}{99+99}=\dfrac{1}{2}", font_size=20, color=GREY_B),
            "まで上がります。",
            font_size=16,
            color=GREY_B,
        )
        self.stack_below(trivia, shown, buff=0.22)
        self._fit_left(trivia)
        self.play(FadeIn(trivia), run_time=0.70)
        self.linger(
            "事前を 1 万人に 1 人ではなく、100 人に 1 人とすると、同じ検査でも真の陽性 99 人、偽の陽性 99 人となり、陽性のとき病気である確率は 99/(99+99)=1/2 まで上がります。",
            extra=0.40,
        )
        self.pause_conclusion()

    def _kit(self):
        body = RoundedRectangle(
            width=2.70,
            height=1.65,
            corner_radius=0.12,
            color=GREY_B,
            stroke_width=2.2,
        )
        body.set_fill(GREY_E, 0.92)
        window = RoundedRectangle(
            width=1.55,
            height=0.50,
            corner_radius=0.04,
            color=GREY_A,
            stroke_width=1.2,
        )
        window.set_fill("#f4f1ea", 1.0)
        window.move_to(body.get_center() + UP * 0.12)
        c_line = Line(
            window.get_center() + LEFT * 0.38 + UP * 0.10,
            window.get_center() + LEFT * 0.38 + DOWN * 0.10,
            color=GREY_B,
            stroke_width=3.2,
        )
        t_line = Line(
            window.get_center() + RIGHT * 0.38 + UP * 0.10,
            window.get_center() + RIGHT * 0.38 + DOWN * 0.10,
            color=RED,
            stroke_width=3.2,
        )
        kit_lab = self.ja_text("検査キット", font_size=16, color=GREY_B)
        kit_lab.next_to(body, DOWN, buff=0.08)
        kit = VGroup(body, window, c_line, t_line, kit_lab)

        tag = RoundedRectangle(
            width=1.40,
            height=1.65,
            corner_radius=0.10,
            color=RED,
            stroke_width=3.0,
        )
        tag.set_fill(RED, 0.18)
        plus = self.ja_text("陽性", font_size=24, color=RED)
        plus.move_to(tag.get_center())
        tag_lab = self.ja_text("札", font_size=16, color=GREY_B)
        tag_lab.next_to(tag, DOWN, buff=0.08)
        card = VGroup(tag, plus, tag_lab)

        cells = VGroup(kit, card)
        cells.arrange(RIGHT, buff=0.55)
        rects = [body, tag]
        y = rects[0].get_y()
        for cell, rect in zip(cells, rects):
            cell.shift(UP * (y - rect.get_y()))
        return cells

    def _people_row(self, highlight=None):
        specs = [
            ("sick", "病気", GOLD, 1),
            ("well", "病気でない", GREY_B, 12),
        ]
        cells = VGroup()
        rects = []
        for key, title, color, n_dots in specs:
            active = highlight == key
            stroke = YELLOW if active else color
            width = 4.0 if active else 2.0
            rect = RoundedRectangle(
                width=2.70,
                height=1.70,
                corner_radius=0.10,
                color=stroke,
                stroke_width=width,
            )
            rect.set_fill(color, 0.18 if n_dots == 1 else 0.10)
            dots = VGroup()
            for i in range(n_dots):
                dots.add(Dot(radius=0.08 if n_dots > 1 else 0.14, color=color))
            if n_dots == 1:
                dots.move_to(rect.get_center())
            else:
                dots.arrange_in_grid(rows=3, cols=4, buff=0.10)
                dots.move_to(rect.get_center())
            lab = self.ja_text(title, font_size=16, color=color)
            lab.next_to(rect, DOWN, buff=0.08)
            cells.add(VGroup(rect, dots, lab))
            rects.append(rect)
        cells.arrange(RIGHT, buff=0.50)
        y = rects[0].get_y()
        for cell, rect in zip(cells, rects):
            cell.shift(UP * (y - rect.get_y()))
        return cells

    def _count_blocks(self):
        specs = [
            ("真の陽性", r"99", GREEN),
            ("偽の陽性", r"9999", ORANGE),
        ]
        cells = VGroup()
        rects = []
        for title, num, color in specs:
            rect = RoundedRectangle(
                width=2.90,
                height=1.70,
                corner_radius=0.10,
                color=color,
                stroke_width=3.0,
            )
            rect.set_fill(color, 0.22)
            inner = self._line(
                MathTex(num, font_size=36, color=color),
                "人",
                font_size=20,
                color=color,
            )
            inner.move_to(rect.get_center())
            lab = self.ja_text(title, font_size=18, color=color)
            lab.next_to(rect, DOWN, buff=0.10)
            cells.add(VGroup(rect, inner, lab))
            rects.append(rect)
        cells.arrange(RIGHT, buff=0.55)
        y = rects[0].get_y()
        for cell, rect in zip(cells, rects):
            cell.shift(UP * (y - rect.get_y()))
        return cells

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
