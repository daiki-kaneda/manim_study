from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import LessonScene


class LawOfLargeNumbers(LessonScene):
    """#13 振り続けると表の割合は 1/2 に寄るか（約9分）"""

    def construct(self):
        self.header = self._open_header()
        self.part_question()
        self.part_trial_short()
        self.part_trial_next_tails()
        self.part_step1_no_memory()
        self.part_step2_diff_vs_rate()
        self.part_step3_grow_n()
        self.part_step4_shrink()
        self.part_example()
        self.part_generalize()
        self.part_summary()

    def _open_header(self):
        title = self._line(
            "振り続けると表の割合は",
            MathTex(r"\dfrac{1}{2}", font_size=40, color=YELLOW),
            "に寄るか",
            font_size=34,
        )
        self._fit(title, 13.2)
        title.set_x(0)
        self.play(FadeIn(title), run_time=0.8)
        self.pause_new_screen()
        self.linger(1.5)
        self.play(title.animate.scale(0.52).to_edge(UP, buff=0.16), run_time=0.5)
        title.set_x(0)
        return title

    def part_question(self):
        fig = self._coin(face=None, radius=0.62)
        cap = self._line(
            "公正なコインを、表が出る確率",
            MathTex(r"\dfrac{1}{2}", font_size=26, color=YELLOW),
            "とします。",
            font_size=18,
        )
        self._fit(cap, 13.0)
        pair = VGroup(fig, cap).arrange(DOWN, buff=0.28)
        pair.next_to(self.header, DOWN, buff=0.28)
        pair.set_x(0)
        self._nudge(pair)
        self.play(FadeIn(fig), FadeIn(cap), run_time=0.8)
        self.pause_new_screen()
        self.linger("公正なコインを、表が出る確率 1/2 とします。")

        q1 = self._line(
            "振り続けたとき、表の枚数を回数で割った割合は、必ず",
            MathTex(r"\dfrac{1}{2}", font_size=26, color=YELLOW),
            "に近づくのでしょうか。",
            font_size=18,
        )
        self.stack_below(q1, pair, buff=0.22)
        q1.set_x(0)
        self._fit(q1, 13.0)
        q1.set_x(0)
        self.play(FadeIn(q1), run_time=0.7)
        self.linger("振り続けたとき、表の枚数を回数で割った割合は、必ず 1/2 に近づくのでしょうか。")

        q2 = self.ja_text(
            "10 回連続で表が出たあとも、同じでしょうか。",
            font_size=20,
        )
        self.stack_below(q2, q1, buff=0.14)
        q2.set_x(0)
        self._fit(q2, 13.0)
        q2.set_x(0)
        self.play(FadeIn(q2), run_time=0.7)
        self.linger(q2.text, extra=0.35)

    def part_trial_short(self):
        chip = self.begin_step("試行  短い列", self.header)

        lead = self.ja_text(
            "まず、10 回だけ振った列を、そのまま数えてみます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)
        self.play(FadeOut(lead), run_time=0.45)

        faces = [True, True, True, False, True, True, True, False, True, True]
        fig = self._coins_row(faces, radius=0.28)
        self.below_chip(fig, chip, buff=0.28)
        fig.set_x(0)
        cap = self._line(
            "表が 8 回、裏が 2 回。割合",
            MathTex(r"\dfrac{8}{10}=\dfrac{4}{5}", font_size=26, color=YELLOW),
            "。",
            font_size=18,
        )
        self._fit(cap, 13.0)
        self.stack_below(cap, fig, buff=0.40)
        cap.set_x(0)
        self.play(FadeIn(fig), FadeIn(cap), run_time=0.7)
        self.pause_new_screen()
        self.linger("表が 8 回、裏が 2 回。割合 8/10=4/5。")

        self.play(FadeOut(VGroup(fig, cap)), run_time=0.45)
        self.pause_topic()

        table = self.aligned_table(
            [
                [
                    self.ja_text("回数", font_size=16, color=GREY_B),
                    self.ja_text("表の枚数", font_size=16, color=GREY_B),
                    self.ja_text("表の割合", font_size=16, color=GREY_B),
                ],
                [
                    MathTex(r"10", font_size=28),
                    MathTex(r"8", font_size=28),
                    MathTex(r"\dfrac{8}{10}", font_size=28, color=YELLOW),
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
            self._line(
                "10 回だけだと、割合は",
                MathTex(r"\dfrac{1}{2}", font_size=24, color=YELLOW),
                "から大きく外れます。",
                font_size=18,
            ),
            self.ja_text(
                "短い列を見ただけでは、振り続けたときのことは決まりません。",
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
            if i == 0:
                self.linger("10 回だけだと、割合は 1/2 から大きく外れます。")
            else:
                self.linger(mob.text)

    def part_trial_next_tails(self):
        chip = self.begin_step("試行  次は裏", self.header)

        lead = self.ja_text(
            "10 回続けて表が出たあと、次は裏が出やすい、と思ってみます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)
        self.play(FadeOut(lead), run_time=0.45)

        faces = [True] * 10 + ["next"]
        fig = self._coins_row(faces, radius=0.26)
        self.below_chip(fig, chip, buff=0.28)
        fig.set_x(0)
        captions = [
            "表が 10 回続いた。",
            "これまでの表が多すぎるので、あとで帳消しにしたい。",
            "だから、次の 1 回は裏の方が出やすい、と思ってしまいます。",
        ]
        cap = self.ja_text(captions[0], font_size=18)
        self._fit(cap, 13.0)
        self.stack_below(cap, fig, buff=0.40)
        cap.set_x(0)
        self.play(FadeIn(fig), FadeIn(cap), run_time=0.7)
        self.pause_new_screen()
        self.linger(captions[0])

        for text in captions[1:]:
            new_cap = self.ja_text(text, font_size=18)
            self._fit(new_cap, 13.0)
            self.stack_below(new_cap, fig, buff=0.40)
            new_cap.set_x(0)
            self.play(FadeOut(cap), run_time=0.45)
            cap = new_cap
            self.play(FadeIn(cap), run_time=0.55)
            self.linger(text)

        self.play(FadeOut(VGroup(fig, cap)), run_time=0.45)
        self.pause_topic()

        notes = [
            self.ja_text(
                "これまでの結果が、次の 1 回の出やすさを変える、という考え方です。",
                font_size=18,
            ),
            self.ja_text(
                "この問いが欲しいのは、次の 1 回の確率と、長い回数での割合です。この二つは別です。",
                font_size=18,
            ),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.below_chip(mob, chip, buff=0.22)
            else:
                self.stack_below(mob, shown, buff=0.10)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            shown.add(mob)
            self.linger(mob.text)

    def part_step1_no_memory(self):
        chip = self.begin_step("STEP 1  記憶はない", self.header)

        lead = self.ja_text(
            "次の 1 回の確率を出すために、コインの決まりを先に書きます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        defs = [
            self._line(
                "表が出る確率は",
                MathTex(r"\dfrac{1}{2}", font_size=26, color=YELLOW),
                "です。裏も",
                MathTex(r"\dfrac{1}{2}", font_size=26, color=YELLOW),
                "です。",
                font_size=18,
            ),
            self.ja_text(
                "各回は独立です。前の結果は、次の回の出やすさを変えません。",
                font_size=18,
            ),
            self._line(
                "だから、表が 10 回続いたあとも、次が表である確率は",
                MathTex(r"\dfrac{1}{2}", font_size=28, color=YELLOW),
                "。",
                font_size=18,
            ),
        ]
        block = self._formula_rows(defs, lead, buff=0.12)
        self.pause_conclusion()
        self.play(FadeOut(block), run_time=0.45)
        self.pause_topic()

        notes = [
            self.ja_text(
                "独立なので、コインに記憶はありません。",
                font_size=18,
            ),
            self.ja_text(
                "次の 1 回が裏に偏る、という補正は、この決まりには入っていません。",
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

    def part_step2_diff_vs_rate(self):
        chip = self.begin_step("STEP 2  差と割合", self.header)

        lead = self.ja_text(
            "表の枚数と回数の差と、表の割合を、分けて書きます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        restate = self._line(
            "回数を",
            MathTex(r"n", font_size=24, color=YELLOW),
            "、表の枚数を",
            MathTex(r"k", font_size=24, color=YELLOW),
            "とおく。",
            font_size=18,
        )
        self.stack_below(restate, lead, buff=0.10)
        restate.set_x(0)
        self.play(FadeIn(restate), run_time=0.55)
        self.pause_short_formula()
        self.linger("回数を n、表の枚数を k とおく。")

        rows = [
            self._line(
                "表の割合は",
                MathTex(r"\dfrac{k}{n}", font_size=30, color=YELLOW),
                "。",
                font_size=18,
            ),
            self._line(
                "表が半分から何枚多いかは",
                MathTex(r"k-\dfrac{n}{2}", font_size=30, color=ORANGE),
                "。",
                font_size=18,
            ),
            self._line(
                "10 回で表 8 なら、割合は",
                MathTex(r"\dfrac{8}{10}", font_size=26, color=YELLOW),
                "、差は",
                MathTex(r"8-5=3", font_size=26, color=ORANGE),
                "枚。",
                font_size=18,
            ),
        ]
        block = self._formula_rows(rows, restate, buff=0.12, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(block), run_time=0.45)
        self.pause_topic()

        table = self.aligned_table(
            [
                [
                    self.ja_text("量", font_size=16, color=GREY_B),
                    self.ja_text("値の例", font_size=16, color=GREY_B),
                ],
                [
                    self._line("割合", MathTex(r"\dfrac{k}{n}", font_size=22), font_size=16),
                    MathTex(r"\dfrac{8}{10}", font_size=26, color=YELLOW),
                ],
                [
                    self._line("差", MathTex(r"k-\dfrac{n}{2}", font_size=22), font_size=16),
                    MathTex(r"3", font_size=26, color=ORANGE),
                ],
            ],
            h_buff=0.40,
            v_buff=0.10,
        )
        table.scale(0.88)
        self.stack_below(table, restate, buff=0.14)
        table.set_x(0)
        self.reveal_table(table, row_wait=1.20)

        notes = [
            self._line(
                "差の枚数が残っていても、回数",
                MathTex(r"n", font_size=24, color=YELLOW),
                "で割れば割合は小さく見えます。",
                font_size=18,
            ),
            self.ja_text(
                "近づくかどうかを見るときは、差ではなく割合を見ます。",
                font_size=18,
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
                self.linger("差の枚数が残っていても、回数 n で割れば割合は小さく見えます。")
            else:
                self.linger(mob.text)

    def part_step3_grow_n(self):
        chip = self.begin_step("STEP 3  回数", self.header)

        lead = self.ja_text(
            "同じ差の 3 枚でも、回数を増やすと割合はどうなるかを計算します。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)
        self.play(FadeOut(lead), run_time=0.45)

        stages = [
            (
                10,
                0.8,
                r"n=10",
                r"\dfrac{5+3}{10}=\dfrac{8}{10}=0.8",
                "n=10、差 3 枚。",
            ),
            (
                100,
                0.53,
                r"n=100",
                r"\dfrac{50+3}{100}=\dfrac{53}{100}=0.53",
                "n=100、差 3 枚。",
            ),
            (
                1000,
                0.503,
                r"n=1000",
                r"\dfrac{500+3}{1000}=\dfrac{503}{1000}=0.503",
                "n=1000、差 3 枚。",
            ),
        ]
        colors = [ORANGE, TEAL, GREEN]
        fig, nl = self._rate_line([])
        self.below_chip(fig, chip, buff=0.28)
        fig.set_x(0)
        self._nudge(fig)
        self.play(FadeIn(fig), run_time=0.7)
        self.pause_new_screen()

        cap = None
        for i, (_n, rate, ntex, eq, speak) in enumerate(stages):
            color = colors[i]
            tag_dir = [UP, LEFT, RIGHT][i]
            mark = self._rate_mark(nl, rate, ntex, eq_color=color, tag_dir=tag_dir)
            eq_mob = self._line(
                MathTex(ntex, font_size=24, color=color),
                "、差 3 枚:",
                MathTex(eq, font_size=26, color=color),
                font_size=18,
            )
            self._fit(eq_mob, 13.0)
            self.stack_below(eq_mob, fig, buff=0.40)
            eq_mob.set_x(0)
            if cap is None:
                self.play(FadeIn(mark), FadeIn(eq_mob), run_time=0.7)
            else:
                self.play(FadeIn(mark), FadeOut(cap), run_time=0.65)
                self.play(FadeIn(eq_mob), run_time=0.55)
            cap = eq_mob
            self.linger(speak)
            self.pause_complex()

        self.play(FadeOut(cap), run_time=0.45)
        self.pause_topic()

        notes = [
            self._line(
                "差の枚数が同じでも、回数が多いほど、割合は",
                MathTex(r"\dfrac{1}{2}", font_size=24, color=YELLOW),
                "に近いです。",
                font_size=18,
            ),
            self._line(
                "短い列で外れて見えるのは、分母の",
                MathTex(r"n", font_size=24, color=YELLOW),
                "が小さいからです。",
                font_size=18,
            ),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, fig, buff=0.22)
            else:
                self.stack_below(mob, shown, buff=0.10)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            shown.add(mob)
            if i == 0:
                self.linger("差の枚数が同じでも、回数が多いほど、割合は 1/2 に近いです。")
            else:
                self.linger("短い列で外れて見えるのは、分母の n が小さいからです。")

    def part_step4_shrink(self):
        chip = self.begin_step("STEP 4  小さく", self.header)

        lead = self.ja_text(
            "割合のばらつきが、回数とともにどう小さくなっていくかを、絵で見ます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        restate = self._line(
            "1 回の表は",
            MathTex(r"0", font_size=24),
            "か",
            MathTex(r"1", font_size=24),
            "。平均",
            MathTex(r"\dfrac{1}{2}", font_size=24, color=YELLOW),
            "。",
            font_size=18,
        )
        self.stack_below(restate, lead, buff=0.10)
        restate.set_x(0)
        self.play(FadeIn(restate), run_time=0.55)
        self.pause_short_formula()
        self.linger("1 回の表は 0 か 1。平均 1/2。")
        self.play(FadeOut(lead), run_time=0.45)

        rows = [
            self._line(
                MathTex(r"n", font_size=24, color=YELLOW),
                "回の表の割合を",
                MathTex(r"\dfrac{k}{n}", font_size=28, color=YELLOW),
                "とします。",
                font_size=18,
            ),
            self._line(
                "この割合のばらつきの目安は、",
                MathTex(r"\dfrac{1}{n}", font_size=28, color=ORANGE),
                "に比例して小さくなっていきます。",
                font_size=18,
            ),
            self._line(
                "幅が",
                MathTex(r"\dfrac{1}{\sqrt{n}}", font_size=28, color=TEAL),
                "のペースで小さくなっていく絵を出します。",
                font_size=18,
            ),
        ]
        block = self._formula_rows(rows, restate, buff=0.12, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(VGroup(restate, block)), run_time=0.45)
        self.pause_topic()

        legend = self._line(
            MathTex(r"\dfrac{1}{n}", font_size=26, color=ORANGE),
            MathTex(r"\dfrac{1}{\sqrt{n}}", font_size=26, color=TEAL),
            font_size=16,
            buff=0.45,
        )
        bands = VGroup(
            self._width_band(10, 10 ** (-0.5), ORANGE),
            self._width_band(100, 0.10, TEAL),
            self._width_band(1000, 1000 ** (-0.5), GREEN),
        ).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        fig = VGroup(legend, bands).arrange(DOWN, buff=0.14)
        self.below_chip(fig, chip, buff=0.16)
        fig.set_x(0)
        self._nudge(fig)

        captions = [
            self._line(
                "ばらつきの目安は",
                MathTex(r"\dfrac{1}{n}", font_size=24, color=ORANGE),
                "に比例して小さくなっていきます。",
                font_size=18,
            ),
            self._line(
                "幅は",
                MathTex(r"\dfrac{1}{\sqrt{n}}", font_size=24, color=TEAL),
                "のペースで小さくなっていきます。",
                font_size=18,
            ),
            self._line(
                "回数が多いほど、",
                MathTex(r"\dfrac{1}{2}", font_size=24, color=YELLOW),
                "のまわりが細くなります。",
                font_size=18,
            ),
        ]
        cap = None
        for i, row in enumerate(bands):
            new_cap = captions[i]
            self._fit(new_cap, 13.0)
            self.stack_below(new_cap, fig, buff=0.24)
            new_cap.set_x(0)
            if cap is None:
                self.play(FadeIn(legend), FadeIn(row), FadeIn(new_cap), run_time=0.7)
            else:
                self.play(FadeIn(row), FadeOut(cap), run_time=0.65)
                self.play(FadeIn(new_cap), run_time=0.55)
            cap = new_cap
            self.pause_new_screen()
            if i == 0:
                self.linger("ばらつきの目安は 1/n に比例して小さくなっていきます。")
            elif i == 1:
                self.linger("幅は 1/sqrt(n) のペースで小さくなっていきます。")
            else:
                self.linger("回数が多いほど、1/2 のまわりが細くなります。")

        self.play(FadeOut(cap), run_time=0.45)
        self.pause_topic()

        notes = [
            self._line(
                "回数を増やすと、割合が",
                MathTex(r"\dfrac{1}{2}", font_size=24, color=YELLOW),
                "の近くに留まりやすくなります。",
                font_size=18,
            ),
            self._line(
                "差の枚数は",
                MathTex(r"\sqrt{n}", font_size=24, color=ORANGE),
                "の幅で揺れうるので、差そのものは",
                MathTex(r"0", font_size=24),
                "に張り付きません。",
                font_size=18,
            ),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, fig, buff=0.18)
            else:
                self.stack_below(mob, shown, buff=0.10)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            shown.add(mob)
            if i == 0:
                self.linger("回数を増やすと、割合が 1/2 の近くに留まりやすくなります。")
            else:
                self.linger("差の枚数は sqrt(n) の幅で揺れうるので、差そのものは 0 に張り付きません。")

    def part_example(self):
        chip = self.begin_step("実例", self.header)

        lead = self.ja_text(
            "表が 10 回続いたあと、さらに 90 回振る、という列を最後まで数えます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)
        self.play(FadeOut(lead), run_time=0.45)

        first = self._coins_row([True] * 10, radius=0.24)
        more = self._count_card()
        fig = VGroup(first, more).arrange(RIGHT, buff=0.45, aligned_edge=UP)
        self.below_chip(fig, chip, buff=0.22)
        fig.set_x(0)
        self._nudge(fig)

        cap = self._line(
            "最初の 10 回は表。",
            MathTex(r"k=10", font_size=22),
            "、",
            MathTex(r"n=10", font_size=22),
            "、割合",
            MathTex(r"1", font_size=24, color=YELLOW),
            "。",
            font_size=18,
        )
        self._fit(cap, 13.0)
        self.stack_below(cap, fig, buff=0.32)
        cap.set_x(0)
        self.play(FadeIn(first), FadeIn(cap), run_time=0.7)
        self.pause_new_screen()
        self.linger("最初の 10 回は表。k=10、n=10、割合 1。")

        cap2 = self.ja_text(
            "そのあと 90 回を、表 45、裏 45 とします。公正な平均の例です。",
            font_size=18,
        )
        self._fit(cap2, 13.0)
        self.stack_below(cap2, fig, buff=0.32)
        cap2.set_x(0)
        self.play(FadeIn(more), FadeOut(cap), run_time=0.65)
        self.play(FadeIn(cap2), run_time=0.55)
        self.linger(cap2.text)
        cap = cap2

        self.play(FadeOut(VGroup(fig, cap)), run_time=0.45)
        self.pause_topic()

        calc = [
            self._line("合計の表は", MathTex(r"10+45=55", font_size=28, color=YELLOW), font_size=18),
            self._line("合計の回数は", MathTex(r"10+90=100", font_size=28), font_size=18),
            self._line(
                "割合は",
                MathTex(r"\dfrac{55}{100}=\dfrac{11}{20}=0.55", font_size=28, color=YELLOW),
                font_size=18,
            ),
            self._line(
                "次の 1 回の確率は、途中でもずっと",
                MathTex(r"\dfrac{1}{2}", font_size=28, color=YELLOW),
                "。",
                font_size=18,
            ),
        ]
        block = self._formula_rows(calc, chip, buff=0.18, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(block), run_time=0.45)
        self.pause_topic()

        table = self.aligned_table(
            [
                [
                    self.ja_text("時点", font_size=14, color=GREY_B),
                    self.ja_text("表の枚数", font_size=14, color=GREY_B),
                    self.ja_text("回数", font_size=14, color=GREY_B),
                    self.ja_text("割合", font_size=14, color=GREY_B),
                ],
                [
                    self.ja_text("10 回表の直後", font_size=18),
                    MathTex(r"10", font_size=24),
                    MathTex(r"10", font_size=24),
                    MathTex(r"1", font_size=24, color=YELLOW),
                ],
                [
                    self.ja_text("さらに 90 回のあと", font_size=18),
                    MathTex(r"55", font_size=24),
                    MathTex(r"100", font_size=24),
                    MathTex(r"\dfrac{55}{100}", font_size=24, color=YELLOW),
                ],
            ],
            h_buff=0.28,
            v_buff=0.08,
        )
        table.scale(0.82)
        self.below_chip(table, chip, buff=0.18)
        table.set_x(0)
        self.reveal_table(table, row_wait=1.20)

        notes = [
            self._line(
                "最初の 10 回は残り続けますが、分母が増えるので、割合は 1 から",
                MathTex(r"\dfrac{1}{2}", font_size=22, color=YELLOW),
                "の側へ戻ります。",
                font_size=16,
            ),
            self._line(
                "戻るのは、次の回が裏に偏るからではありません。新しい回が",
                MathTex(r"\dfrac{1}{2}", font_size=22, color=YELLOW),
                "だからです。",
                font_size=16,
            ),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, table, buff=0.12)
            else:
                self.stack_below(mob, shown, buff=0.08)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            shown.add(mob)
            if i == 0:
                self.linger("最初の 10 回は残り続けますが、分母が増えるので、割合は 1 から 1/2 の側へ戻ります。")
            else:
                self.linger("戻るのは、次の回が裏に偏るからではありません。新しい回が 1/2 だからです。")

    def part_generalize(self):
        chip = self.begin_step("一般化", self.header)

        lead = self.ja_text(
            "今やったことは、独立な試行を繰り返すと、割合が平均へ寄る、という考え方でした。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        first = [
            self._line(
                "表の確率",
                MathTex(r"\dfrac{1}{2}", font_size=26, color=YELLOW),
                "。独立。",
                font_size=18,
            ),
            self._line(
                "大数の法則と呼ばれます。表の割合",
                MathTex(r"\dfrac{k}{n}", font_size=26, color=YELLOW),
                "は、回数",
                MathTex(r"n", font_size=24, color=YELLOW),
                "を大きくすると",
                MathTex(r"\dfrac{1}{2}", font_size=26, color=YELLOW),
                "に近づきます。",
                font_size=16,
            ),
        ]
        block = self._formula_rows(first, lead, buff=0.10, hold=self.PAUSE_CONCLUSION)
        self.play(FadeOut(VGroup(lead, block)), run_time=0.45)
        self.pause_topic()

        name = self._line(
            "表の割合",
            MathTex(r"\dfrac{k}{n}", font_size=24, color=YELLOW),
            "は、回数を大きくすると",
            MathTex(r"\dfrac{1}{2}", font_size=24, color=YELLOW),
            "に近づきます。",
            font_size=18,
            color=GREY_B,
        )
        self.below_chip(name, chip, buff=0.16)
        self._fit_left(name)
        self.play(FadeIn(name), run_time=0.55)
        self.linger("表の割合 k/n は、回数を大きくすると 1/2 に近づきます。")

        close = [
            self.ja_text("割合は寄ります。差ではなく割合を見る方法です。", font_size=18),
            self._line(
                "差",
                MathTex(r"k-\dfrac{n}{2}", font_size=24, color=ORANGE),
                "は、",
                MathTex(r"\sqrt{n}", font_size=24, color=ORANGE),
                "の幅で揺れうる。",
                font_size=18,
            ),
            self._line(
                "独立な試行に記憶はない。次の 1 回は、これまでと独立に",
                MathTex(r"\dfrac{1}{2}", font_size=26, color=YELLOW),
                "。",
                font_size=18,
            ),
            self._line(
                "必ず各回が帳消しになる、という意味ではありません。割る回数が増えて、外れの見え方が",
                MathTex(r"\dfrac{1}{\sqrt{n}}", font_size=20, color=TEAL),
                "のペースで小さくなっていく、という意味です。",
                font_size=16,
                color=GREY_B,
            ),
        ]
        self._formula_rows(close, name, buff=0.12)

    def part_summary(self):
        chip = self.begin_step("まとめ", self.header)

        rows = [
            self._line(
                "短い列では、表の割合は",
                MathTex(r"\dfrac{1}{2}", font_size=24, color=YELLOW),
                "から大きく外れます",
                font_size=18,
            ),
            self._line(
                "表が続いたあとも、次の 1 回が表である確率は",
                MathTex(r"\dfrac{1}{2}", font_size=24, color=YELLOW),
                "のままです。記憶はありません",
                font_size=16,
            ),
            self._line(
                "差の枚数と割合は別です。差が残っても、",
                MathTex(r"n", font_size=24, color=YELLOW),
                "で割れば割合は寄ります",
                font_size=16,
            ),
            self._line(
                "大数の法則は、割合",
                MathTex(r"\dfrac{k}{n}", font_size=24, color=YELLOW),
                "が平均へ寄ることです。ばらつきの幅は",
                MathTex(r"\dfrac{1}{\sqrt{n}}", font_size=24, color=TEAL),
                "のペースで小さくなっていきます",
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

        trivia = VGroup(
            self._line(
                "1000 回振って表が 520 回でも、差は 20 枚、割合は",
                MathTex(r"\dfrac{520}{1000}=0.52", font_size=20, color=GREY_B),
                "です。",
                font_size=16,
                color=GREY_B,
            ),
            self._line(
                "差は残っても、割合は",
                MathTex(r"\dfrac{1}{2}", font_size=20, color=GREY_B),
                "の近くです。",
                font_size=16,
                color=GREY_B,
            ),
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        self.stack_below(trivia, shown, buff=0.22)
        self._fit_left(trivia)
        self.play(FadeIn(trivia), run_time=0.70)
        self.linger(
            "1000 回振って表が 520 回でも、差は 20 枚、割合は 520/1000=0.52 です。差は残っても、割合は 1/2 の近くです。",
            extra=0.40,
        )
        self.pause_conclusion()

    def _coin(self, face=None, radius=0.30):
        if face is True:
            stroke, fill, opacity = GOLD, GOLD, 0.90
        elif face is False:
            stroke, fill, opacity = GREY_B, GREY_E, 0.90
        elif face == "next":
            stroke, fill, opacity = YELLOW, GREY_E, 0.35
        else:
            stroke, fill, opacity = YELLOW, GREY_E, 0.55
        circ = Circle(radius=radius, color=stroke, stroke_width=2.4)
        circ.set_fill(fill, opacity)
        label = None
        if face is True:
            label = self.ja_text("表", font_size=14, color=GOLD)
        elif face is False:
            label = self.ja_text("裏", font_size=14, color=GREY_B)
        elif face == "next":
            label = self.ja_text("次", font_size=14, color=YELLOW)
        parts = VGroup(circ)
        if label is not None:
            label.next_to(circ, DOWN, buff=0.06)
            parts.add(label)
        return parts

    def _coins_row(self, faces, radius=0.30):
        coins = [self._coin(face, radius=radius) for face in faces]
        slots = VGroup(*[Circle(radius=radius) for _ in faces]).arrange(RIGHT, buff=0.12)
        cells = VGroup()
        for coin, slot in zip(coins, slots):
            coin[0].move_to(slot.get_center())
            if len(coin) > 1:
                coin[1].next_to(coin[0], DOWN, buff=0.06)
            cells.add(coin)
        y = cells[0][0].get_y()
        for coin in cells:
            coin.shift(UP * (y - coin[0].get_y()))
        return cells

    def _count_card(self):
        box = RoundedRectangle(
            width=3.6,
            height=1.55,
            corner_radius=0.10,
            color=GREY_B,
            stroke_width=2.0,
        )
        box.set_fill(GREY_E, 0.55)
        title = self.ja_text("さらに 90 回", font_size=18)
        body = self._line(
            "表",
            MathTex(r"45", font_size=26, color=GOLD),
            "裏",
            MathTex(r"45", font_size=26, color=GREY_B),
            "です",
            font_size=16,
        )
        inner = VGroup(title, body).arrange(DOWN, buff=0.16)
        inner.move_to(box.get_center())
        return VGroup(box, inner)

    def _rate_line(self, marks):
        nl = NumberLine(
            x_range=[0.45, 0.85, 0.10],
            length=10.4,
            include_ticks=True,
            include_numbers=False,
            color=GREY_B,
            stroke_width=2.0,
        )
        dash = DashedLine(
            nl.n2p(0.5) + UP * 0.42,
            nl.n2p(0.5) + DOWN * 0.04,
            color=YELLOW,
            stroke_width=2.0,
        )
        half = MathTex(r"\dfrac{1}{2}", font_size=20, color=YELLOW)
        half.next_to(nl.n2p(0.5), DOWN, buff=0.22)
        group = VGroup(nl, dash, half)
        for rate, tex, color in marks:
            group.add(self._rate_mark(nl, rate, tex, eq_color=color))
        return group, nl

    def _rate_mark(self, nl, rate, ntex, eq_color=ORANGE, tag_dir=UP):
        dot = Dot(nl.n2p(rate), color=eq_color, radius=0.09)
        arm = Line(nl.n2p(0.5), nl.n2p(rate), color=eq_color, stroke_width=5)
        lab = MathTex(ntex, font_size=18, color=eq_color)
        near_half = abs(rate - 0.5) < 0.04
        tags = lab if near_half else VGroup(lab, MathTex(rf"{rate}", font_size=18, color=eq_color)).arrange(DOWN, buff=0.04)
        if tag_dir is UP:
            tags.next_to(dot, UP, buff=0.16)
        elif tag_dir is DOWN:
            tags.next_to(dot, DOWN, buff=0.28)
        elif tag_dir is LEFT:
            tags.next_to(dot, LEFT, buff=0.12)
            tags.shift(UP * 0.28)
        else:
            tags.next_to(dot, RIGHT, buff=0.14)
            tags.shift(UP * 0.28)
        return VGroup(arm, dot, tags)

    def _width_band(self, n, half_w, color):
        nl = NumberLine(
            x_range=[0, 1, 0.5],
            length=7.4,
            include_ticks=True,
            include_numbers=False,
            color=GREY_B,
            stroke_width=1.6,
        )
        lab0 = MathTex(r"0", font_size=16)
        lab1 = MathTex(r"1", font_size=16)
        labh = MathTex(r"\dfrac{1}{2}", font_size=16, color=YELLOW)
        lab0.next_to(nl.n2p(0.0), DOWN, buff=0.22)
        lab1.next_to(nl.n2p(1.0), DOWN, buff=0.22)
        labh.next_to(nl.n2p(0.5), DOWN, buff=0.22)
        width = abs(nl.n2p(0.5 + half_w)[0] - nl.n2p(0.5 - half_w)[0])
        rect = Rectangle(
            width=max(width, 0.10),
            height=0.20,
            color=color,
            stroke_width=1.4,
        )
        rect.set_fill(color, 0.35)
        rect.move_to(nl.n2p(0.5) + UP * 0.02)
        nlab = MathTex(rf"n={n}", font_size=18, color=color)
        vlab = MathTex(rf"\dfrac{{1}}{{{n}}}", font_size=16, color=ORANGE)
        wlab = MathTex(rf"\dfrac{{1}}{{\sqrt{{{n}}}}}", font_size=16, color=TEAL)
        left = VGroup(nlab, vlab, wlab).arrange(DOWN, buff=0.04, aligned_edge=RIGHT)
        line_group = VGroup(nl, rect, lab0, lab1, labh)
        row = VGroup(left, line_group).arrange(RIGHT, buff=0.28)
        return row

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
