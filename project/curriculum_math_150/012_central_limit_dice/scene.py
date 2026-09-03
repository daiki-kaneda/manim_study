from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import LessonScene


class CentralLimitDice(LessonScene):
    """#12 サイコロを足すと釣鐘になるのはなぜか（約9分）"""

    TWO_COUNTS = (1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1)
    THREE_COUNTS = (1, 3, 6, 10, 15, 21, 25, 27, 27, 25, 21, 15, 10, 6, 3, 1)

    def construct(self):
        self.header = self._open_header()
        self.part_question()
        self.part_trial_one()
        self.part_trial_two_flat()
        self.part_step1_pairs()
        self.part_step2_sums()
        self.part_step3_three()
        self.part_step4_spread()
        self.part_example()
        self.part_generalize()
        self.part_summary()

    def _open_header(self):
        title = self.ja_text("サイコロを足すと釣鐘になるのはなぜか", font_size=36)
        self.play(FadeIn(title), run_time=0.8)
        self.pause_new_screen()
        self.linger(1.5)
        self.play(title.animate.scale(0.52).to_edge(UP, buff=0.16), run_time=0.5)
        title.set_x(0)
        return title

    def part_question(self):
        fig = self._die()
        cap = self.ja_text(
            "サイコロは 1 個だと、1 から 6 まで同じ確からしさです。",
            font_size=20,
        )
        self._fit(cap, 13.0)
        pair = VGroup(fig, cap).arrange(DOWN, buff=0.28)
        pair.next_to(self.header, DOWN, buff=0.28)
        pair.set_x(0)
        self._nudge(pair)
        self.play(FadeIn(fig), FadeIn(cap), run_time=0.8)
        self.pause_new_screen()
        self.linger(cap.text)

        q2 = self.ja_text(
            "何個もの目を足した合計は、なぜ端が少なく、真ん中が膨らむのでしょうか。",
            font_size=20,
        )
        self.stack_below(q2, pair, buff=0.22)
        q2.set_x(0)
        self._fit(q2, 13.0)
        q2.set_x(0)
        self.play(FadeIn(q2), run_time=0.7)
        self.linger(q2.text, extra=0.35)

    def part_trial_one(self):
        chip = self.begin_step("試行  1 個", self.header)

        lead = self.ja_text(
            "まず、サイコロ 1 個の目の出方を、最後まで数えます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)
        self.play(FadeOut(lead), run_time=0.45)

        chart = self._bar_chart(
            [1, 1, 1, 1, 1, 1],
            [1, 2, 3, 4, 5, 6],
            color=BLUE_B,
            unit=0.72,
            bar_w=0.55,
            gap=0.16,
        )
        self.below_chip(chart, chip, buff=0.22)
        chart.set_x(0)
        self._play_bars(chart)
        cap = self.ja_text("1 から 6 まで、どれも 1 通りです。棒の高さは同じです。", font_size=18)
        self._fit(cap, 13.0)
        self.stack_below(cap, chart, buff=0.22)
        cap.set_x(0)
        self.play(FadeIn(cap), run_time=0.55)
        self.linger(cap.text)

        self.play(FadeOut(VGroup(chart, cap)), run_time=0.45)
        self.pause_topic()

        table = self.aligned_table(
            [
                [
                    self.ja_text("目", font_size=16, color=GREY_B),
                    self.ja_text("場合の数", font_size=16, color=GREY_B),
                ],
                [
                    self._line(
                        MathTex(r"1", font_size=24),
                        "から",
                        MathTex(r"6", font_size=24),
                        "のどれ",
                        font_size=18,
                    ),
                    MathTex(r"1", font_size=28, color=YELLOW),
                ],
            ],
            h_buff=0.40,
            v_buff=0.12,
        )
        table.scale(0.90)
        self.below_chip(table, chip, buff=0.20)
        table.set_x(0)
        self.reveal_table(table, row_wait=1.20)

        note = self.ja_text(
            "1 個だけなら、分布は平坦です。真ん中が特別に多い、ということはありません。",
            font_size=18,
        )
        self.stack_below(note, table, buff=0.14)
        note.set_x(0)
        self._fit(note, 13.0)
        note.set_x(0)
        self.play(FadeIn(note), run_time=0.55)
        self.linger(note.text)

    def part_trial_two_flat(self):
        chip = self.begin_step("試行  2 個？", self.header)

        lead = self.ja_text(
            "2 個にすると、合計も 2 から 12 まで同じ個数で並ぶ、と思ってみます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        rows = [
            self._line(
                "最小の合計は",
                MathTex(r"1+1=2", font_size=28, color=YELLOW),
                "です。",
                font_size=18,
            ),
            self._line(
                "最大の合計は",
                MathTex(r"6+6=12", font_size=28, color=YELLOW),
                "です。",
                font_size=18,
            ),
            self._line(
                "合計の種類は",
                MathTex(r"11", font_size=28, color=YELLOW),
                "通りなので、どれも同じ個数だと思ってしまいます。",
                font_size=18,
            ),
        ]
        block = self._formula_rows(rows, lead, buff=0.14, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(block), run_time=0.45)
        self.pause_topic()

        notes = [
            self.ja_text(
                "合計が取りうる値の種類を数えただけで、各合計が何通りあるかはまだ数えていません。",
                font_size=18,
            ),
            self.ja_text(
                "この問いが欲しいのは、合計ごとの場合の数です。",
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

    def part_step1_pairs(self):
        chip = self.begin_step("STEP 1  2 個の目", self.header)

        lead = self.ja_text(
            "2 個のサイコロの出方を、先に全部の組として書きます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        defs = [
            self._line(
                "サイコロの個数を",
                MathTex(r"2", font_size=26, color=YELLOW),
                "とおく。目を",
                MathTex(r"1", font_size=26),
                "から",
                MathTex(r"6", font_size=26),
                "とおく。",
                font_size=18,
            ),
            self._line(
                "組の総数は",
                MathTex(r"6\cdot 6=36", font_size=30, color=YELLOW),
                "です。",
                font_size=18,
            ),
            self.ja_text("どの組も同じ確からしさ、とおく。", font_size=18),
        ]
        block = self._formula_rows(defs, lead, buff=0.12)
        self.pause_conclusion()
        self.play(FadeOut(VGroup(lead, block)), run_time=0.45)
        self.pause_topic()

        fig = self._pair_grid()
        self.below_chip(fig, chip, buff=0.18)
        fig.set_x(0)
        self._nudge(fig)
        self.play(FadeIn(fig), run_time=0.8)
        self.pause_new_screen()
        cap = self.ja_text(
            "たて 6、よこ 6 の格子です。マスの大きさはどれも同じです。",
            font_size=18,
        )
        self._fit(cap, 13.0)
        self.stack_below(cap, fig, buff=0.18)
        cap.set_x(0)
        self.play(FadeIn(cap), run_time=0.55)
        self.linger(cap.text)

        note = self.ja_text(
            "36 通りの組が、あとで合計ごとに何個あるかを数える材料です。",
            font_size=18,
        )
        self.stack_below(note, cap, buff=0.12)
        note.set_x(0)
        self._fit(note, 13.0)
        note.set_x(0)
        self.play(FadeIn(note), run_time=0.55)
        self.linger(note.text)

    def part_step2_sums(self):
        chip = self.begin_step("STEP 2  合計", self.header)

        lead = self.ja_text(
            "合計が 2 の組から、合計が 7 の組まで、場合の数を一段ずつ数えます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        restate = self._line(
            "組は",
            MathTex(r"36", font_size=26, color=YELLOW),
            "通りです。",
            font_size=18,
        )
        self.stack_below(restate, lead, buff=0.10)
        restate.set_x(0)
        self.play(FadeIn(restate), run_time=0.55)
        self.pause_short_formula()
        self.linger("組は 36 通りです。")

        low = [
            self._line(
                "合計",
                MathTex(r"2", font_size=24, color=YELLOW),
                r":",
                MathTex(r"(1,1)", font_size=24),
                "の 1 通り。",
                font_size=18,
            ),
            self._line(
                "合計",
                MathTex(r"3", font_size=24, color=YELLOW),
                r":",
                MathTex(r"(1,2),(2,1)", font_size=24),
                "の 2 通り。",
                font_size=18,
            ),
            self._line(
                "合計",
                MathTex(r"4", font_size=24, color=YELLOW),
                ":",
                MathTex(r"3", font_size=26),
                "通り。",
                font_size=18,
            ),
            self._line(
                "合計",
                MathTex(r"5", font_size=24, color=YELLOW),
                ":",
                MathTex(r"4", font_size=26),
                "通り。",
                font_size=18,
            ),
            self._line(
                "合計",
                MathTex(r"6", font_size=24, color=YELLOW),
                ":",
                MathTex(r"5", font_size=26),
                "通り。",
                font_size=18,
            ),
            self._line(
                "合計",
                MathTex(r"7", font_size=24, color=GOLD),
                ":",
                MathTex(r"6", font_size=26, color=GOLD),
                "通り。",
                font_size=18,
            ),
        ]
        block_low = self._formula_rows(low, restate, buff=0.10, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(block_low), run_time=0.45)
        self.pause_topic()

        high = [
            self._line(
                "対称で、合計",
                MathTex(r"8", font_size=24, color=YELLOW),
                "は",
                MathTex(r"5", font_size=26),
                "通りです。",
                font_size=18,
            ),
            self._line(
                "合計",
                MathTex(r"9", font_size=24, color=YELLOW),
                "は",
                MathTex(r"4", font_size=26),
                "通りです。",
                font_size=18,
            ),
            self._line(
                "合計",
                MathTex(r"10", font_size=24, color=YELLOW),
                "は",
                MathTex(r"3", font_size=26),
                "通りです。",
                font_size=18,
            ),
            self._line(
                "合計",
                MathTex(r"11", font_size=24, color=YELLOW),
                "は",
                MathTex(r"2", font_size=26),
                "通りです。",
                font_size=18,
            ),
            self._line(
                "合計",
                MathTex(r"12", font_size=24, color=YELLOW),
                "は",
                MathTex(r"1", font_size=26),
                "通りです。",
                font_size=18,
            ),
        ]
        block_high = self._formula_rows(high, restate, buff=0.10, hold=self.PAUSE_SHORT_FORMULA)
        self.play(FadeOut(VGroup(lead, restate, block_high)), run_time=0.45)
        self.pause_topic()

        colors = [BLUE_B, BLUE_B, BLUE_B, TEAL, TEAL, GOLD, TEAL, TEAL, BLUE_B, BLUE_B, BLUE_B]
        chart = self._bar_chart(
            list(self.TWO_COUNTS),
            list(range(2, 13)),
            colors=colors,
            unit=0.28,
            bar_w=0.46,
            gap=0.10,
        )
        self.below_chip(chart, chip, buff=0.22)
        chart.set_x(0)
        self._play_bars(chart)
        cap = self.ja_text(
            "合計 2 から 12。棒の高さは場合の数です。番号は棒の下に揃えています。",
            font_size=18,
        )
        self._fit(cap, 13.0)
        self.stack_below(cap, chart, buff=0.20)
        cap.set_x(0)
        self.play(FadeIn(cap), run_time=0.55)
        self.linger(cap.text)

        notes = [
            self.ja_text(
                "端の合計は経路が少なく、真ん中の合計は経路が多いです。",
                font_size=18,
            ),
            self.ja_text(
                "2 個にしただけで、もう平坦ではありません。",
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

    def part_step3_three(self):
        chip = self.begin_step("STEP 3  3 個", self.header)

        lead = self.ja_text(
            "3 個のときも、端と真ん中で経路の数が違うことを、小さい合計で確かめます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        restate = self._line(
            "組の総数は",
            MathTex(r"6\cdot 6\cdot 6=216", font_size=28, color=YELLOW),
            r"。つまり",
            MathTex(r"6^{3}=216", font_size=28, color=YELLOW),
            "です。",
            font_size=18,
        )
        self.stack_below(restate, lead, buff=0.10)
        restate.set_x(0)
        self._fit(restate, 13.0)
        restate.set_x(0)
        self.play(FadeIn(restate), run_time=0.55)
        self.pause_complex()
        self.linger("組の総数は 6・6・6=216。つまり 6^3=216 です。")

        low = [
            self._line(
                "合計",
                MathTex(r"3", font_size=24, color=YELLOW),
                r":",
                MathTex(r"(1,1,1)", font_size=24),
                "の 1 通り。",
                font_size=18,
            ),
            self._line(
                "合計",
                MathTex(r"4", font_size=24, color=YELLOW),
                ":",
                MathTex(r"3", font_size=26),
                "通り。",
                font_size=18,
            ),
            self.ja_text("合計 10 付近は、もっと多くなります。", font_size=18),
        ]
        block_low = self._formula_rows(low, restate, buff=0.10, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(VGroup(lead, block_low)), run_time=0.45)
        self.pause_topic()

        parts_lead = self.ja_text(
            "3 個で合計 10 を作る分け方を、いくつか書きます。",
            font_size=18,
        )
        self.stack_below(parts_lead, restate, buff=0.12)
        parts_lead.set_x(0)
        self.play(FadeIn(parts_lead), run_time=0.55)
        self.linger(parts_lead.text)

        parts = [
            MathTex(r"(1,3,6),\ (1,4,5),\ (2,2,6),\ (2,3,5)", font_size=26),
            MathTex(r"(2,4,4),\ (3,3,4)", font_size=26),
            self._line(
                "並べ替えを全部数えると、合計 10 は",
                MathTex(r"27", font_size=30, color=GOLD),
                "通りです。",
                font_size=18,
            ),
        ]
        block_parts = self._formula_rows(parts, parts_lead, buff=0.10, hold=self.PAUSE_COMPLEX)
        self.pause_conclusion()
        self.play(FadeOut(VGroup(restate, parts_lead, block_parts)), run_time=0.45)
        self.pause_topic()

        chart = self._bar_chart(
            list(self.THREE_COUNTS),
            list(range(3, 19)),
            colors=self._three_colors(),
            unit=0.055,
            bar_w=0.32,
            gap=0.06,
            label_size=12,
        )
        self.below_chip(chart, chip, buff=0.20)
        chart.set_x(0)
        self._play_bars(chart)
        cap = self.ja_text(
            "3 個の合計 3 から 18。端は低く、合計 10 付近がいちばん高いです。",
            font_size=18,
        )
        self._fit(cap, 13.0)
        self.stack_below(cap, chart, buff=0.18)
        cap.set_x(0)
        self.play(FadeIn(cap), run_time=0.55)
        self.linger(cap.text)

        note = self.ja_text(
            "3 個でも、端は少なく真ん中は多いです。膨らみは 2 個のときより目立ちます。",
            font_size=18,
        )
        self.stack_below(note, cap, buff=0.12)
        note.set_x(0)
        self._fit(note, 13.0)
        note.set_x(0)
        self.play(FadeIn(note), run_time=0.55)
        self.linger(note.text)

    def part_step4_spread(self):
        chip = self.begin_step("STEP 4  広がり", self.header)

        lead = self.ja_text(
            "個数を増やすと、合計の平均は比例して伸び、ばらつきの幅はそれよりゆっくり伸びます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        restate = self._line(
            "1 個の平均は",
            MathTex(r"\dfrac{1+2+3+4+5+6}{6}=\dfrac{21}{6}=\dfrac{7}{2}", font_size=26, color=YELLOW),
            "です。",
            font_size=16,
        )
        self.stack_below(restate, lead, buff=0.10)
        restate.set_x(0)
        self._fit(restate, 13.0)
        restate.set_x(0)
        self.play(FadeIn(restate), run_time=0.55)
        self.pause_complex()
        self.linger("1 個の平均は (1+2+3+4+5+6)/6=21/6=7/2 です。")

        rows = [
            self._line(
                MathTex(r"n", font_size=24, color=YELLOW),
                "個の合計の平均は",
                MathTex(r"n\cdot\dfrac{7}{2}", font_size=28, color=YELLOW),
                "です。",
                font_size=18,
            ),
            self._line(
                "ばらつきの幅の目安は、個数",
                MathTex(r"n", font_size=24),
                "そのものではなく",
                MathTex(r"\sqrt{n}", font_size=28, color=GOLD),
                "に比例します。",
                font_size=16,
            ),
            self._line(
                "平均で割る方法で見ると、相対的なばらつきは",
                MathTex(r"\dfrac{\sqrt{n}}{n}=\dfrac{1}{\sqrt{n}}", font_size=28, color=GOLD),
                "でしぼみます。",
                font_size=16,
            ),
        ]
        block = self._formula_rows(rows, restate, buff=0.10, hold=self.PAUSE_COMPLEX)
        self.pause_conclusion()
        self.play(FadeOut(VGroup(lead, block)), run_time=0.45)
        self.pause_topic()

        chart = self._bar_chart(
            list(self.TWO_COUNTS),
            list(range(2, 13)),
            colors=[BLUE_B, BLUE_B, BLUE_B, TEAL, TEAL, GOLD, TEAL, TEAL, BLUE_B, BLUE_B, BLUE_B],
            unit=0.26,
            bar_w=0.44,
            gap=0.10,
        )
        self.stack_below(chart, restate, buff=0.18)
        chart.set_x(0)
        self._play_bars(chart)
        envelope = self._envelope(chart.bars)
        self.play(Create(envelope), run_time=0.90)
        chart.add(envelope)
        cap = self.ja_text(
            "棒の頂点を滑らかにつないだ包絡が、釣鐘の形です。",
            font_size=18,
        )
        self._fit(cap, 13.0)
        self.stack_below(cap, chart, buff=0.18)
        cap.set_x(0)
        self.play(FadeIn(cap), run_time=0.55)
        self.linger(cap.text)

        name = self.ja_text(
            "この形には、正規分布という名前がつきます。密度の式は形の名前です。",
            font_size=16,
            color=GREY_B,
        )
        self.stack_below(name, cap, buff=0.10)
        name.set_x(0)
        self._fit(name, 13.0)
        name.set_x(0)
        self.play(FadeIn(name), run_time=0.55)
        self.linger(name.text)

        note = self.ja_text(
            "足すほど、真ん中に寄って見えるのは、経路の数の差と、相対的な幅がしぼむからです。",
            font_size=18,
        )
        self.stack_below(note, name, buff=0.10)
        note.set_x(0)
        self._fit(note, 13.0)
        note.set_x(0)
        self.play(FadeIn(note), run_time=0.55)
        self.linger(note.text)

    def part_example(self):
        chip = self.begin_step("実例", self.header)

        lead = self.ja_text(
            "2 個の合計 2 から 12 まで、場合の数を表で最後まで数えます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)
        self.play(FadeOut(lead), run_time=0.45)

        header_row = [
            self.ja_text("合計", font_size=14, color=GREY_B),
            self.ja_text("場合の数", font_size=14, color=GREY_B),
        ]
        data = [
            (2, 1, False),
            (3, 2, False),
            (4, 3, False),
            (5, 4, False),
            (6, 5, False),
            (7, 6, True),
            (8, 5, False),
            (9, 4, False),
            (10, 3, False),
            (11, 2, False),
            (12, 1, False),
        ]
        rows = [header_row]
        for total, count, peak in data:
            color = GOLD if peak else WHITE
            rows.append(
                [
                    MathTex(rf"{total}", font_size=20, color=color),
                    MathTex(rf"{count}", font_size=20, color=color),
                ]
            )
        table = self.aligned_table(rows, h_buff=0.36, v_buff=0.05)
        table.scale(0.72)
        self.below_chip(table, chip, buff=0.14)
        table.set_x(-3.15)
        self.reveal_table(table, row_wait=0.85)

        verify = VGroup(
            self._line(
                "合計は",
                MathTex(r"1+2+\cdots+1=36", font_size=24, color=YELLOW),
                "です。",
                font_size=16,
            ),
            self._line(
                "検算は",
                MathTex(r"2\cdot(1+2+3+4+5)+6", font_size=22, color=YELLOW),
                font_size=16,
            ),
            MathTex(r"=30+6=36", font_size=26, color=YELLOW),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        verify.next_to(table, RIGHT, buff=0.42)
        verify.align_to(table, UP)
        self._nudge(verify)
        for row in verify:
            self.play(FadeIn(row), run_time=0.55)
            super().wait(self.PAUSE_COMPLEX)

        notes = [
            self.ja_text(
                "36 通りのうち、合計 7 は 6 通り、合計 2 は 1 通りです。",
                font_size=18,
            ),
            self.ja_text(
                "値が取りうる種類が 11 個あることと、各種類の場合の数が同じことは、別です。",
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

    def part_generalize(self):
        chip = self.begin_step("一般化", self.header)

        lead = self.ja_text(
            "今やったことは、独立なゆらぎを足すと、合計の分布が釣鐘に近づく、という考え方でした。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        first = [
            self.ja_text("各サイコロは独立です。", font_size=18),
            self._line(
                "1 個の平均は",
                MathTex(r"\dfrac{7}{2}", font_size=26, color=YELLOW),
                "です。",
                font_size=18,
            ),
            self._line(
                "中心極限定理の直感と呼ばれます。足す個数",
                MathTex(r"n", font_size=22, color=YELLOW),
                "が大きいと、合計の分布は正規分布の形に近づきます。",
                font_size=16,
            ),
        ]
        block = self._formula_rows(first, lead, buff=0.10, hold=self.PAUSE_CONCLUSION)
        self.play(FadeOut(VGroup(lead, block)), run_time=0.45)
        self.pause_topic()

        name = self._line(
            "各サイコロは独立。平均は",
            MathTex(r"\dfrac{7}{2}", font_size=22, color=YELLOW),
            "。",
            font_size=18,
            color=GREY_B,
        )
        self.below_chip(name, chip, buff=0.16)
        self.play(FadeIn(name), run_time=0.55)
        self.linger("各サイコロは独立。平均は 7/2。")

        shape = [
            self._line(
                "平均は",
                MathTex(r"n\cdot\dfrac{7}{2}", font_size=28, color=YELLOW),
                "です。",
                font_size=18,
            ),
            self._line(
                "幅の目安は",
                MathTex(r"\sqrt{n}", font_size=28, color=GOLD),
                "に比例します。",
                font_size=18,
            ),
            self.ja_text(
                "正規分布の密度の式は、形として出します。積分して出す手順は使いません。",
                font_size=16,
            ),
        ]
        block2 = self._formula_rows(shape, name, buff=0.12, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(block2), run_time=0.45)
        self.pause_topic()

        formula = MathTex(
            r"\dfrac{1}{\sqrt{2\pi}\,\sigma}\exp\left(-\dfrac{(x-\mu)^{2}}{2\sigma^{2}}\right)",
            font_size=30,
            color=GREY_A,
        )
        self.stack_below(formula, name, buff=0.18)
        formula.set_x(0)
        self.play(FadeIn(formula), run_time=0.70)
        self.pause_conclusion()

        close = self.ja_text(
            "1 個が平坦でも、足すと経路の多い真ん中が膨らみます。それが釣鐘に見える理由です。",
            font_size=18,
        )
        self.stack_below(close, formula, buff=0.16)
        close.set_x(0)
        self._fit(close, 13.0)
        close.set_x(0)
        self.play(FadeIn(close), run_time=0.55)
        self.linger(close.text)

    def part_summary(self):
        chip = self.begin_step("まとめ", self.header)

        rows = [
            self.ja_text("1 個のサイコロの目は平坦です", font_size=18),
            self._line(
                "2 個の合計では、端の経路が少なく、真ん中の経路が多いです。場合の数は",
                MathTex(r"36", font_size=24, color=YELLOW),
                "通り",
                font_size=16,
            ),
            self._line(
                "個数",
                MathTex(r"n", font_size=22, color=YELLOW),
                "を増やすと、相対的なばらつきは",
                MathTex(r"\dfrac{1}{\sqrt{n}}", font_size=24, color=GOLD),
                "でしぼみます",
                font_size=16,
            ),
            self.ja_text(
                "独立なゆらぎを足すと、分布は釣鐘（正規分布の形）に近づきます",
                font_size=18,
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
            "コインの表を",
            MathTex(r"1", font_size=20, color=GREY_B),
            "、裏を",
            MathTex(r"0", font_size=20, color=GREY_B),
            "とおいて足しても、同じように真ん中が膨らみます。サイコロである必要はありません。",
            font_size=16,
            color=GREY_B,
        )
        self.stack_below(trivia, shown, buff=0.22)
        self._fit_left(trivia)
        self.play(FadeIn(trivia), run_time=0.70)
        self.linger(
            "コインの表を 1、裏を 0 とおいて足しても、同じように真ん中が膨らみます。サイコロである必要はありません。",
            extra=0.40,
        )
        self.pause_conclusion()

    def _die(self, size=1.80):
        s = size
        dx = 0.38 * s
        dy = 0.26 * s
        fl = LEFT * (s / 2) + DOWN * (s / 2)
        fr = RIGHT * (s / 2) + DOWN * (s / 2)
        ur = RIGHT * (s / 2) + UP * (s / 2)
        ul = LEFT * (s / 2) + UP * (s / 2)
        off = RIGHT * dx + UP * dy
        front = Polygon(fl, fr, ur, ul, color=GREY_B, stroke_width=2.4)
        front.set_fill(GREY_A, 0.95)
        top = Polygon(ul, ur, ur + off, ul + off, color=GREY_B, stroke_width=2.0)
        top.set_fill("#E2E2E2", 0.95)
        side = Polygon(fr, fr + off, ur + off, ur, color=GREY_B, stroke_width=2.0)
        side.set_fill(GREY_C, 0.92)
        inset = RoundedRectangle(
            width=s * 0.72,
            height=s * 0.72,
            corner_radius=0.10,
            color=GREY_B,
            stroke_width=1.2,
        )
        inset.set_fill(WHITE, 0.08)
        inset.move_to(front.get_center())
        return VGroup(top, side, front, inset)

    def _pair_grid(self, cell=0.48, buff=0.05):
        rects = []
        for _a in range(6):
            for _b in range(6):
                rect = RoundedRectangle(
                    width=cell,
                    height=cell,
                    corner_radius=0.05,
                    color=GREY_B,
                    stroke_width=1.4,
                )
                rect.set_fill(GREY_E, 0.70)
                rects.append(rect)
        grid = VGroup(*rects).arrange_in_grid(rows=6, cols=6, buff=buff)
        labels = VGroup()
        for i in range(6):
            for j in range(6):
                lab = MathTex(rf"{i + 1},{j + 1}", font_size=11, color=GREY_A)
                lab.move_to(rects[i * 6 + j].get_center())
                labels.add(lab)
        col_labs = VGroup()
        for j in range(6):
            hl = MathTex(rf"{j + 1}", font_size=16, color=YELLOW)
            hl.next_to(rects[j], UP, buff=0.08)
            col_labs.add(hl)
        row_labs = VGroup()
        for i in range(6):
            hl = MathTex(rf"{i + 1}", font_size=16, color=YELLOW)
            hl.next_to(rects[i * 6], LEFT, buff=0.08)
            row_labs.add(hl)
        top_name = self.ja_text("2 個目", font_size=14, color=GREY_B)
        top_name.next_to(col_labs, UP, buff=0.08)
        top_name.set_x(grid.get_x())
        left_name = self.ja_text("1 個目", font_size=14, color=GREY_B)
        left_name.next_to(row_labs, LEFT, buff=0.10)
        left_name.set_y(grid.get_y())
        return VGroup(grid, labels, col_labs, row_labs, top_name, left_name)

    def _bar_chart(
        self,
        heights,
        labels,
        color=BLUE_B,
        colors=None,
        unit=0.30,
        bar_w=0.46,
        gap=0.10,
        label_size=16,
    ):
        n = len(heights)
        if colors is None:
            colors = [color] * n
        bars = VGroup()
        labs = VGroup()
        stride = bar_w + gap
        width = n * bar_w + (n - 1) * gap
        x0 = -width / 2 + bar_w / 2
        y0 = 0.0
        label_y = y0 - 0.28
        for i, (h, text) in enumerate(zip(heights, labels)):
            col = colors[i]
            height = max(h * unit, 0.10)
            bar = Rectangle(
                width=bar_w,
                height=height,
                color=col,
                stroke_width=1.2,
            )
            bar.set_fill(col, 0.85)
            x = x0 + i * stride
            bar.move_to([x, y0 + height / 2, 0])
            lab = MathTex(rf"{text}", font_size=label_size)
            lab.move_to([x, label_y, 0])
            bars.add(bar)
            labs.add(lab)
        left = bars[0].get_left()[0] - 0.12
        right = bars[-1].get_right()[0] + 0.12
        baseline = Line([left, y0, 0], [right, y0, 0], color=GREY_B, stroke_width=1.6)
        chart = VGroup(baseline, bars, labs)
        chart.bars = bars
        chart.labels = labs
        chart.baseline = baseline
        return chart

    def _play_bars(self, chart):
        self.add(chart.baseline)
        self.play(
            LaggedStart(
                *[GrowFromEdge(bar, DOWN) for bar in chart.bars],
                lag_ratio=0.08,
            ),
            FadeIn(chart.labels),
            run_time=1.35,
        )
        self.pause_new_screen()

    def _envelope(self, bars, color=ORANGE):
        left = bars[0].get_corner(DL) + LEFT * 0.18
        right = bars[-1].get_corner(DR) + RIGHT * 0.18
        pts = [left]
        for bar in bars:
            pts.append(bar.get_top() + UP * 0.08)
        pts.append(right)
        curve = VMobject(color=color, stroke_width=4)
        curve.set_points_smoothly(pts)
        return curve

    def _three_colors(self):
        colors = []
        for h in self.THREE_COUNTS:
            if h >= 27:
                colors.append(GOLD)
            elif h >= 21:
                colors.append(TEAL)
            else:
                colors.append(BLUE_B)
        return colors

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
