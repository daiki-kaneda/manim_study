from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import LessonScene


class EuclideanAlgorithm(LessonScene):
    """#20 巨大な 2 数の最大公約数（約9分）"""

    def construct(self):
        self.header = self._open_header()
        self.part_question()
        self.part_trial_small()
        self.part_trial_subtract()
        self.part_step1_divisors()
        self.part_step2_diff()
        self.part_step3_remainder()
        self.part_step4_stop()
        self.part_example()
        self.part_generalize()
        self.part_summary()

    def _open_header(self):
        title = self._line(
            MathTex(r"1234567", font_size=34, color=YELLOW),
            "と",
            MathTex(r"891011", font_size=34, color=TEAL),
            "の最大公約数は、素因数分解せずに出るか",
            font_size=26,
        )
        self._fit(title, 13.4)
        title.set_x(0)
        self.play(FadeIn(title), run_time=0.8)
        self.pause_new_screen()
        self.linger(1.5)
        self.play(title.animate.scale(0.50).to_edge(UP, buff=0.16), run_time=0.5)
        title.set_x(0)
        return title

    def part_question(self):
        fig = VGroup(
            self._card(r"1234567", YELLOW),
            self._card(r"891011", TEAL),
        ).arrange(RIGHT, buff=0.55)
        cap = self.ja_text(
            "この 2 つの整数を、両方割り切る最大の正の整数を求めたいとします。",
            font_size=16,
        )
        self._fit(cap, 13.0)
        pair = VGroup(fig, cap).arrange(DOWN, buff=0.24)
        pair.next_to(self.header, DOWN, buff=0.24)
        pair.set_x(0)
        self._nudge(pair)
        self.play(FadeIn(fig), FadeIn(cap), run_time=0.8)
        self.pause_new_screen()
        self.linger(cap.text)

        q1 = self.ja_text("素因数分解せずに、求めたい。", font_size=20)
        self.stack_below(q1, pair, buff=0.16)
        q1.set_x(0)
        self.play(FadeIn(q1), run_time=0.7)
        self.linger(q1.text)

        q2 = self.ja_text(
            "割り算の余りを使うと、なぜそれで足りるのでしょうか。",
            font_size=18,
        )
        self.stack_below(q2, q1, buff=0.12)
        q2.set_x(0)
        self.play(FadeIn(q2), run_time=0.7)
        self.linger(q2.text, extra=0.35)

    def part_trial_small(self):
        chip = self.begin_step("試行  小さい数", self.header)

        lead = self.ja_text(
            "まず、小さい素数から順に、両方を割り切るか試します。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)
        self.play(FadeOut(lead), run_time=0.40)

        rows = [
            self._line(
                MathTex(r"2", font_size=24, color=YELLOW),
                "で割る。どちらも奇数なので外れます。",
                font_size=16,
            ),
            self._line(
                MathTex(r"3", font_size=24, color=ORANGE),
                "で割る。各位の和",
                MathTex(r"1+2+3+4+5+6+7=28", font_size=22, color=ORANGE),
                "。",
                MathTex(r"28", font_size=22),
                "は",
                MathTex(r"3", font_size=22, color=ORANGE),
                "で割れない。左は外れます。",
                font_size=14,
            ),
            self._line(
                MathTex(r"5", font_size=24, color=TEAL),
                "で割る。一の位が",
                MathTex(r"7", font_size=22),
                "と",
                MathTex(r"1", font_size=22),
                "なので外れます。",
                font_size=16,
            ),
            self._line(
                MathTex(r"11", font_size=24, color=GREEN),
                "で割る。右は",
                MathTex(r"891011\div 11=81001", font_size=22, color=GREEN),
                "。左は割り切れません。",
                font_size=14,
            ),
        ]
        block = self._formula_rows(rows, chip, buff=0.14, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(block), run_time=0.40)

        table = self.aligned_table(
            [
                [
                    self.ja_text("割る数", font_size=14, color=GREY_B),
                    MathTex(r"1234567", font_size=18, color=GREY_B),
                    MathTex(r"891011", font_size=18, color=GREY_B),
                ],
                [
                    MathTex(r"2", font_size=22),
                    self.ja_text("外れ", font_size=16),
                    self.ja_text("外れ", font_size=16),
                ],
                [
                    MathTex(r"3", font_size=22),
                    self.ja_text("外れ", font_size=16),
                    self.ja_text(" ", font_size=16),
                ],
                [
                    MathTex(r"5", font_size=22),
                    self.ja_text("外れ", font_size=16),
                    self.ja_text("外れ", font_size=16),
                ],
                [
                    MathTex(r"11", font_size=22, color=GREEN),
                    self.ja_text("外れ", font_size=16),
                    self.ja_text("割れる", font_size=16, color=GREEN),
                ],
            ],
            h_buff=0.32,
            v_buff=0.08,
        )
        table.scale(0.86)
        self.below_chip(table, chip, buff=0.14)
        table.set_x(0)
        self.play(FadeIn(table), run_time=0.7)
        self.pause_new_screen()

        notes = [
            self.ja_text("片方だけ割れる数では、公約数になりません。", font_size=16),
            self.ja_text(
                "巨大だと、素因数分解は辛く感じます。素因数が 100 を超えると、順に割る方法は現実的ではありません。小さい数から試せばすぐ出る、という予想は、この試しでは支えられません。",
                font_size=14,
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
            self.linger(mob.text)

    def part_trial_subtract(self):
        chip = self.begin_step("試行  引き算", self.header)

        lead = self.ja_text(
            "大きい方から小さい方を引く操作を、公約数を保ったまま繰り返してみます。",
            font_size=16,
        )
        self.below_chip(lead, chip, buff=0.14)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)
        self.play(FadeOut(lead), run_time=0.40)

        fig = self._subtract_bars()
        self.below_chip(fig, chip, buff=0.10)
        fig.set_x(0)
        self.play(FadeIn(fig), run_time=0.7)
        self.pause_new_screen()

        rows = [
            self._line(
                MathTex(r"48", font_size=24, color=YELLOW),
                "と",
                MathTex(r"18", font_size=24, color=TEAL),
                font_size=16,
            ),
            self._line(
                MathTex(r"48-18=30", font_size=24, color=YELLOW),
                "、",
                MathTex(r"30-18=12", font_size=24),
                font_size=16,
            ),
            self._line(
                MathTex(r"18-12=6", font_size=24, color=GREEN),
                "、",
                MathTex(r"12-6=6", font_size=24),
                "、",
                MathTex(r"6-6=0", font_size=24),
                font_size=16,
            ),
            self._line(
                "残った",
                MathTex(r"6", font_size=26, color=GOLD),
                "が、両方を割り切る最大です。",
                font_size=16,
            ),
        ]
        block = self._formula_rows(rows, fig, buff=0.10, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(VGroup(fig, block)), run_time=0.40)

        big = [
            self._line(
                MathTex(r"1234567-891011=343556", font_size=24, color=YELLOW),
                "。1 回で済みます。",
                font_size=16,
            ),
            self._line(
                "あとで出る段では、",
                MathTex(r"2785", font_size=22, color=ORANGE),
                "から",
                MathTex(r"11", font_size=22, color=TEAL),
                "を引く回数が",
                MathTex(r"253", font_size=24, color=ORANGE),
                "回です。",
                font_size=14,
            ),
        ]
        shown = self._formula_rows(big, chip, buff=0.16, hold=self.PAUSE_COMPLEX)

        notes = [
            self.ja_text(
                "引き算でも答えは出ますが、商が大きい段では回数が膨らみます。",
                font_size=16,
            ),
            self.ja_text(
                "同じ引き算をまとめて済ませる方法が、余りです。",
                font_size=16,
            ),
        ]
        extra = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, shown, buff=0.12)
            else:
                self.stack_below(mob, extra, buff=0.08)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            extra.add(mob)
            self.linger(mob.text)

    def part_step1_divisors(self):
        chip = self.begin_step("STEP 1  公約数", self.header)

        lead = self.ja_text(
            "両方を割り切る正の整数の、いちばん大きいものを記号にします。",
            font_size=16,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        rows = [
            self._line(
                "正の整数",
                MathTex(r"a", font_size=24, color=YELLOW),
                "と正の整数",
                MathTex(r"b", font_size=24, color=TEAL),
                "とおく。いま",
                MathTex(r"a\ge b", font_size=24),
                "とします。",
                font_size=16,
            ),
            self._line(
                MathTex(r"d", font_size=24, color=ORANGE),
                "が",
                MathTex(r"a", font_size=22, color=YELLOW),
                "も",
                MathTex(r"b", font_size=22, color=TEAL),
                "も割り切るとき、",
                MathTex(r"d", font_size=24, color=ORANGE),
                "を公約数とおく。",
                font_size=16,
            ),
            self._line(
                "そのような",
                MathTex(r"d", font_size=22, color=ORANGE),
                "のうち最大を、最大公約数とおく。記号は",
                MathTex(r"\gcd(a,b)", font_size=26, color=GOLD),
                font_size=16,
            ),
        ]
        block = self._formula_rows(rows, lead, buff=0.10, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(VGroup(lead, block)), run_time=0.40)

        back = [
            self._line(
                MathTex(r"18=2\cdot 3^{2}", font_size=24, color=TEAL),
                "、",
                MathTex(r"48=2^{4}\cdot 3", font_size=24, color=YELLOW),
                font_size=16,
            ),
            self._line(
                "共通の素因数は",
                MathTex(r"2", font_size=24),
                "と",
                MathTex(r"3", font_size=24),
                "。最大は",
                MathTex(r"2\cdot 3=6", font_size=26, color=GOLD),
                font_size=16,
            ),
            self._line(
                "だから",
                MathTex(r"\gcd(48,18)=6", font_size=28, color=GOLD),
                font_size=16,
            ),
        ]
        shown = self._formula_rows(back, chip, buff=0.16, hold=self.PAUSE_COMPLEX)

        notes = [
            self.ja_text("素因数がすぐ書けるときだけ、この確かめは簡単です。", font_size=16),
            self.ja_text(
                "巨大な 2 数では、素因数を先に出す必要がないやり方を次で見ます。",
                font_size=16,
            ),
        ]
        extra = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, shown, buff=0.12)
            else:
                self.stack_below(mob, extra, buff=0.08)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            extra.add(mob)
            self.linger(mob.text)

    def part_step2_diff(self):
        chip = self.begin_step("STEP 2  差", self.header)

        lead = self.ja_text(
            "公約数は、差も割り切ることを式で残します。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        restate = self._line(
            MathTex(r"d", font_size=24, color=ORANGE),
            "が",
            MathTex(r"a", font_size=22, color=YELLOW),
            "も",
            MathTex(r"b", font_size=22, color=TEAL),
            "も割り切るとします。",
            font_size=16,
        )
        self.stack_below(restate, lead, buff=0.10)
        restate.set_x(0)
        self.play(FadeIn(restate), run_time=0.55)
        self.linger("d が a も b も割り切るとします。")
        self.play(FadeOut(lead), run_time=0.40)

        rows = [
            self._line(
                MathTex(r"a=d\cdot m", font_size=24, color=YELLOW),
                "、",
                MathTex(r"b=d\cdot n", font_size=24, color=TEAL),
                "とおく。",
                MathTex(r"m,n", font_size=22),
                "は整数です。",
                font_size=16,
            ),
            self._line(
                MathTex(r"a-b=d\cdot m-d\cdot n=d(m-n)", font_size=26, color=GREEN),
                font_size=16,
            ),
            self._line(
                "だから",
                MathTex(r"d", font_size=24, color=ORANGE),
                "は",
                MathTex(r"a-b", font_size=24, color=GREEN),
                "も割り切る。",
                font_size=16,
            ),
            self._line(
                "同じ理由で、",
                MathTex(r"d", font_size=22, color=ORANGE),
                "は",
                MathTex(r"a-qb", font_size=24, color=GREEN),
                "も割り切る。",
                MathTex(r"q", font_size=22),
                "は整数です。",
                font_size=16,
            ),
            self._line(
                MathTex(r"48-18=30", font_size=22, color=YELLOW),
                "。",
                MathTex(r"6", font_size=22, color=GOLD),
                "は",
                MathTex(r"30", font_size=22),
                "も割り切る。",
                MathTex(r"30-18=12", font_size=22),
                "も同じです。",
                font_size=14,
            ),
        ]
        shown = self._formula_rows(rows, restate, buff=0.08, hold=self.PAUSE_COMPLEX)

        notes = [
            self.ja_text("共通の約数は、引いても消えません。", font_size=16),
            self.ja_text(
                "だから大きい方を小さい方に取り替えても、最大公約数は変わりません。",
                font_size=16,
            ),
        ]
        extra = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, shown, buff=0.10)
            else:
                self.stack_below(mob, extra, buff=0.08)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            extra.add(mob)
            self.linger(mob.text)

    def part_step3_remainder(self):
        chip = self.begin_step("STEP 3  余り", self.header)

        lead = self.ja_text(
            "引き算を何回もする代わりに、割り算の余りへ一気に替えます。",
            font_size=16,
        )
        self.below_chip(lead, chip, buff=0.14)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        rows = [
            self._line(
                MathTex(r"a", font_size=22, color=YELLOW),
                "を",
                MathTex(r"b", font_size=22, color=TEAL),
                "で割った商を",
                MathTex(r"q", font_size=22),
                "、余りを",
                MathTex(r"r", font_size=24, color=GREEN),
                "とおく。",
                font_size=16,
            ),
            self._line(
                MathTex(r"a=qb+r", font_size=28, color=YELLOW),
                "。余りは",
                MathTex(r"0\le r<b", font_size=24, color=GREEN),
                font_size=16,
            ),
            self._line(
                "STEP 2 より、",
                MathTex(r"d", font_size=22, color=ORANGE),
                "が",
                MathTex(r"a", font_size=20),
                "と",
                MathTex(r"b", font_size=20),
                "を割り切るなら、",
                MathTex(r"d", font_size=22),
                "は",
                MathTex(r"r=a-qb", font_size=22, color=GREEN),
                "も割り切る。",
                font_size=14,
            ),
            self._line(
                "逆に、",
                MathTex(r"d", font_size=22, color=ORANGE),
                "が",
                MathTex(r"b", font_size=20),
                "と",
                MathTex(r"r", font_size=20, color=GREEN),
                "を割り切るなら、",
                MathTex(r"d", font_size=22),
                "は",
                MathTex(r"a=qb+r", font_size=22, color=YELLOW),
                "も割り切る。",
                font_size=14,
            ),
            self._line(
                "だから",
                MathTex(r"\gcd(a,b)=\gcd(b,r)", font_size=28, color=GOLD),
                font_size=16,
            ),
        ]
        block = self._formula_rows(rows, lead, buff=0.08, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(VGroup(lead, block)), run_time=0.40)

        small = [
            self._line(
                MathTex(r"48=2\cdot 18+12", font_size=24, color=YELLOW),
                "。余り",
                MathTex(r"12", font_size=24, color=GREEN),
                font_size=16,
            ),
            self._line(
                MathTex(r"\gcd(48,18)=\gcd(18,12)", font_size=24, color=GOLD),
                font_size=16,
            ),
            self._line(
                MathTex(r"18=1\cdot 12+6", font_size=24),
                "、",
                MathTex(r"\gcd(18,12)=\gcd(12,6)", font_size=24, color=GOLD),
                font_size=16,
            ),
            self._line(
                MathTex(r"12=2\cdot 6+0", font_size=24),
                "。余り",
                MathTex(r"0", font_size=24),
                font_size=16,
            ),
        ]
        shown = self._formula_rows(small, chip, buff=0.12, hold=self.PAUSE_COMPLEX)

        notes = [
            self.ja_text(
                "余りへ替えても、最大公約数は同じです。情報が落ちる、という心配は、この等式では支えられません。",
                font_size=16,
            ),
            self._line(
                MathTex(r"a\equiv r\pmod{b}", font_size=24, color=TEAL),
                "と書くと、",
                MathTex(r"a", font_size=20),
                "と",
                MathTex(r"r", font_size=20),
                "は",
                MathTex(r"b", font_size=20),
                "で割った余りが同じ、という意味です。",
                font_size=14,
            ),
            self._line(
                "だから",
                MathTex(r"\gcd(a,b)=\gcd(b,a\bmod b)", font_size=26, color=GOLD),
                font_size=16,
            ),
        ]
        extra = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, shown, buff=0.10)
            else:
                self.stack_below(mob, extra, buff=0.08)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            extra.add(mob)
            self._read(mob)
            if i == 2:
                self.pause_conclusion()

    def part_step4_stop(self):
        chip = self.begin_step("STEP 4  停止", self.header)

        lead = self.ja_text(
            "余りが 0 になった直前の割る数が、最大公約数です。",
            font_size=16,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)
        self.play(FadeOut(lead), run_time=0.40)

        rows = [
            self._line(
                "組",
                MathTex(r"(a,b)", font_size=24, color=YELLOW),
                "を",
                MathTex(r"(b,r)", font_size=24, color=GREEN),
                "に替える。",
                font_size=16,
            ),
            self._line(
                MathTex(r"r=0", font_size=24),
                "なら、直前の",
                MathTex(r"b", font_size=24, color=TEAL),
                "が答えです。",
                font_size=16,
            ),
            self.ja_text("余りは毎回真に小さくなるので、いつか 0 に着きます。", font_size=16),
        ]
        block = self._formula_rows(rows, chip, buff=0.14, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(block), run_time=0.40)

        table = self.aligned_table(
            [
                [
                    MathTex(r"a", font_size=20, color=GREY_B),
                    MathTex(r"b", font_size=20, color=GREY_B),
                    MathTex(r"q", font_size=20, color=GREY_B),
                    MathTex(r"r", font_size=20, color=GREY_B),
                ],
                [
                    MathTex(r"48", font_size=24, color=YELLOW),
                    MathTex(r"18", font_size=24, color=TEAL),
                    MathTex(r"2", font_size=24),
                    MathTex(r"12", font_size=24, color=GREEN),
                ],
                [
                    MathTex(r"18", font_size=24),
                    MathTex(r"12", font_size=24),
                    MathTex(r"1", font_size=24),
                    MathTex(r"6", font_size=24, color=GOLD),
                ],
                [
                    MathTex(r"12", font_size=24),
                    MathTex(r"6", font_size=24, color=GOLD),
                    MathTex(r"2", font_size=24),
                    MathTex(r"0", font_size=24),
                ],
            ],
            h_buff=0.32,
            v_buff=0.10,
        )
        table.scale(0.88)
        self.below_chip(table, chip, buff=0.16)
        table.set_x(0)
        self.play(FadeIn(table), run_time=0.7)
        self.pause_new_screen()

        notes = [
            self._line(
                "最後に余り 0 を出した",
                MathTex(r"6", font_size=26, color=GOLD),
                "が、",
                MathTex(r"\gcd(48,18)", font_size=24, color=GOLD),
                "です。",
                font_size=16,
            ),
            self.ja_text("素因数分解を経由していません。", font_size=16),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, table, buff=0.14)
            else:
                self.stack_below(mob, shown, buff=0.08)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            shown.add(mob)
            self._read(mob)

    def part_example(self):
        chip = self.begin_step("実例", self.header)

        lead = self.ja_text(
            "問いの 2 数を、余りへ替える手順で最後まで通します。",
            font_size=16,
        )
        self.below_chip(lead, chip, buff=0.14)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)
        self.play(FadeOut(lead), run_time=0.40)

        batches = [
            [
                MathTex(r"1234567=1\cdot 891011+343556", font_size=22, color=YELLOW),
                MathTex(r"891011=2\cdot 343556+203899", font_size=22),
                MathTex(r"343556=1\cdot 203899+139657", font_size=22),
                MathTex(r"203899=1\cdot 139657+64242", font_size=22),
            ],
            [
                MathTex(r"139657=2\cdot 64242+11173", font_size=22),
                MathTex(r"64242=5\cdot 11173+8377", font_size=22),
                MathTex(r"11173=1\cdot 8377+2796", font_size=22),
                MathTex(r"8377=2\cdot 2796+2785", font_size=22),
            ],
            [
                MathTex(r"2796=1\cdot 2785+11", font_size=22, color=GREEN),
                MathTex(r"2785=253\cdot 11+2", font_size=24, color=ORANGE),
                MathTex(r"11=5\cdot 2+1", font_size=24, color=TEAL),
                MathTex(r"2=2\cdot 1+0", font_size=24, color=GOLD),
            ],
        ]
        prev = None
        for batch in batches:
            rows = [self._line(eq, font_size=14) for eq in batch]
            if prev is not None:
                self.play(FadeOut(prev), run_time=0.35)
            prev = self._formula_rows(rows, chip, buff=0.14, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(prev), run_time=0.40)

        end = self._line(
            "最後の 0 でない余りは",
            MathTex(r"1", font_size=28, color=GOLD),
            "。だから最大公約数は",
            MathTex(r"1", font_size=28, color=GOLD),
            "です。",
            font_size=16,
        )
        self.below_chip(end, chip, buff=0.12)
        end.set_x(0)
        self.play(FadeIn(end), run_time=0.6)
        self._read(end)
        self.pause_conclusion()
        self.play(FadeOut(end), run_time=0.35)

        table = self.aligned_table(
            [
                [
                    MathTex(r"a", font_size=18, color=GREY_B),
                    MathTex(r"b", font_size=18, color=GREY_B),
                    MathTex(r"q", font_size=18, color=GREY_B),
                    MathTex(r"r", font_size=18, color=GREY_B),
                ],
                [
                    MathTex(r"2796", font_size=20),
                    MathTex(r"2785", font_size=20),
                    MathTex(r"1", font_size=20),
                    MathTex(r"11", font_size=20, color=GREEN),
                ],
                [
                    MathTex(r"2785", font_size=20),
                    MathTex(r"11", font_size=20, color=GREEN),
                    MathTex(r"253", font_size=22, color=ORANGE),
                    MathTex(r"2", font_size=20),
                ],
                [
                    MathTex(r"11", font_size=20),
                    MathTex(r"2", font_size=20),
                    MathTex(r"5", font_size=20),
                    MathTex(r"1", font_size=22, color=GOLD),
                ],
                [
                    MathTex(r"2", font_size=20),
                    MathTex(r"1", font_size=22, color=GOLD),
                    MathTex(r"2", font_size=20),
                    MathTex(r"0", font_size=20),
                ],
            ],
            h_buff=0.28,
            v_buff=0.08,
        )
        table.scale(0.84)
        self.below_chip(table, chip, buff=0.12)
        table.set_x(0)
        self.play(FadeIn(table), run_time=0.7)
        self.pause_new_screen()

        notes = [
            self._line(
                "商",
                MathTex(r"253", font_size=22, color=ORANGE),
                "の段は、引き算なら 253 回です。余りなら 1 行です。",
                font_size=16,
            ),
            self.ja_text("2 数は互いに素です。共通の素因数はありません。", font_size=16),
            self._line(
                MathTex(r"1234567=127\times 9721", font_size=20, color=YELLOW),
                "、",
                MathTex(r"891011=11\times 81001", font_size=20, color=TEAL),
                font_size=14,
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
            self._read(mob)

    def part_generalize(self):
        chip = self.begin_step("一般化", self.header)

        lead = self.ja_text(
            "今やったことは、ユークリッドの互除法と呼ばれる手順でした。",
            font_size=16,
        )
        self.below_chip(lead, chip, buff=0.14)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)
        self.pause_conclusion()

        rows = [
            self._line(
                "正の整数",
                MathTex(r"a", font_size=20, color=YELLOW),
                "、",
                MathTex(r"b", font_size=20, color=TEAL),
                "とします。",
                font_size=14,
            ),
            self._line(
                MathTex(r"\gcd(a,b)=\gcd(b,a\bmod b)", font_size=28, color=GOLD),
                font_size=16,
            ),
            self._line(
                MathTex(r"a\bmod b=0", font_size=22),
                "なら",
                MathTex(r"\gcd(a,b)=b", font_size=24, color=TEAL),
                font_size=16,
            ),
            self.ja_text(
                "割り算の余りへ替える操作を、余り 0 まで繰り返します。",
                font_size=16,
            ),
        ]
        block = self._formula_rows(rows, lead, buff=0.08, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(VGroup(lead, block)), run_time=0.40)

        bez = [
            self._line(
                MathTex(r"\gcd(a,b)", font_size=22),
                "を",
                MathTex(r"d", font_size=24, color=ORANGE),
                "とおくと、整数",
                MathTex(r"x,y", font_size=22),
                "で",
                MathTex(r"ax+by=d", font_size=26, color=GREEN),
                "と書けるものがあります。",
                font_size=14,
            ),
            self._line(
                MathTex(r"48", font_size=22, color=YELLOW),
                "と",
                MathTex(r"18", font_size=22, color=TEAL),
                "なら",
                MathTex(r"d=6", font_size=24, color=GOLD),
                "。",
                MathTex(r"48\cdot(-1)+18\cdot 3=6", font_size=24, color=GREEN),
                font_size=14,
            ),
        ]
        shown = self._formula_rows(bez, chip, buff=0.14, hold=self.PAUSE_COMPLEX)

        notes = [
            self.ja_text(
                "巨大でも、余りが小さくなる方向へ進むので、素因数を先に書く必要はありません。",
                font_size=16,
            ),
            self._line(
                "互いに素、つまり",
                MathTex(r"\gcd(a,b)=1", font_size=22, color=GOLD),
                "なら、",
                MathTex(r"ax+by=1", font_size=22, color=GREEN),
                "となる整数",
                MathTex(r"x,y", font_size=20),
                "があります。",
                font_size=14,
            ),
        ]
        extra = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, shown, buff=0.10)
            else:
                self.stack_below(mob, extra, buff=0.08)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.55)
            extra.add(mob)
            self._read(mob)

    def part_summary(self):
        chip = self.begin_step("まとめ", self.header)

        rows = [
            self._line(
                "公約数は差も余りも割り切る。だから",
                MathTex(r"\gcd(a,b)=\gcd(b,a\bmod b)", font_size=22, color=GOLD),
                font_size=14,
            ),
            self.ja_text("余り 0 の直前の割る数が最大公約数", font_size=16),
            self._line(
                MathTex(r"1234567", font_size=20, color=YELLOW),
                "と",
                MathTex(r"891011", font_size=20, color=TEAL),
                "は、余りを 12 段たどると",
                MathTex(r"1", font_size=24, color=GOLD),
                font_size=14,
            ),
            self.ja_text("この手順をユークリッドの互除法とおく", font_size=16),
            self._line(
                MathTex(r"48\cdot(-1)+18\cdot 3=6", font_size=22, color=GREEN),
                "のように、最大公約数は 2 数の整数倍の和でも書けます。",
                font_size=14,
            ),
        ]
        shown = VGroup()
        for i, mob in enumerate(rows):
            if i == 0:
                self.below_chip(mob, chip, buff=0.20)
            else:
                self.stack_below(mob, shown, buff=0.12)
            self._fit_left(mob, 13.0)
            self.play(FadeIn(mob), run_time=0.55)
            shown.add(mob)
            self._read(mob)
            if i == 2:
                self.pause_conclusion()

    def _card(self, tex, color):
        body = RoundedRectangle(
            width=3.4,
            height=1.20,
            corner_radius=0.12,
            color=color,
            stroke_width=2.4,
        )
        body.set_fill("#2A2A2A", 0.95)
        lab = MathTex(tex, font_size=32, color=color)
        lab.move_to(body.get_center())
        return VGroup(body, lab)

    def _subtract_bars(self):
        unit = 0.055
        long_w = 48 * unit
        short_w = 18 * unit
        long_bar = Rectangle(width=long_w, height=0.32, color=YELLOW, stroke_width=1.4)
        long_bar.set_fill(YELLOW, 0.80)
        short_bar = Rectangle(width=short_w, height=0.32, color=TEAL, stroke_width=1.4)
        short_bar.set_fill(TEAL, 0.80)
        long_lab = MathTex(r"48", font_size=20, color=YELLOW)
        short_lab = MathTex(r"18", font_size=20, color=TEAL)
        long_lab.next_to(long_bar, LEFT, buff=0.12)
        short_lab.next_to(short_bar, LEFT, buff=0.12)
        long_row = VGroup(long_lab, long_bar)
        short_row = VGroup(short_lab, short_bar)
        group = VGroup(long_row, short_row).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        return group

    def _read(self, mob, extra=0.0):
        if hasattr(mob, "text"):
            self.linger(mob.text, extra=extra)
            return
        parts = [sub.text for sub in mob if hasattr(sub, "text")]
        self.linger("".join(parts) if parts else 2.0, extra=extra)

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
        block = VGroup(*rows).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
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
