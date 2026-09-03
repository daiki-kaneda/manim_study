from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import LessonScene


class MontyHall(LessonScene):
    """#10 残った扉を開けた方がよいか（約9分）"""

    def construct(self):
        self.header = self._open_header()
        self.part_question()
        self.part_trial_half()
        self.part_trial_few()
        self.part_step1_rules()
        self.part_step2_first_hit()
        self.part_step3_first_miss()
        self.part_step4_combine()
        self.part_example()
        self.part_generalize()
        self.part_summary()

    def _open_header(self):
        title = self.ja_text("残った扉を開けた方がよいか", font_size=36)
        self.play(FadeIn(title), run_time=0.8)
        self.pause_new_screen()
        self.linger(1.5)
        self.play(title.animate.scale(0.52).to_edge(UP, buff=0.16), run_time=0.5)
        title.set_x(0)
        return title

    def part_question(self):
        fig = self._doors()
        cap = self.ja_text(
            "扉は 3 枚とおく。当たりは、そのうち 1 枚のうしろにだけあります。",
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
            "あなたが 1 枚選んだあと、司会は外れの扉を 1 枚開けて、残った扉への乗り換えを勧めます。",
            font_size=20,
        )
        self.stack_below(q1, pair, buff=0.22)
        q1.set_x(0)
        self._fit(q1, 13.0)
        q1.set_x(0)
        self.play(FadeIn(q1), run_time=0.7)
        self.linger(q1.text)

        q2 = self.ja_text(
            "乗り換えた方がよいのでしょうか。それとも、最初に選んだ扉のままの方がよいのでしょうか。",
            font_size=20,
        )
        self.stack_below(q2, q1, buff=0.14)
        q2.set_x(0)
        self._fit(q2, 13.0)
        q2.set_x(0)
        self.play(FadeIn(q2), run_time=0.7)
        self.linger(q2.text, extra=0.35)

    def part_trial_half(self):
        chip = self.begin_step("試行  半分", self.header)

        lead = self.ja_text(
            "まず、司会が外れを開けたあとに残る扉が 2 枚であることに、目を向けてみます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        rows = [
            self.ja_text("最初、当たりは 3 枚のどれかへ、同じ確からしさで入る、とおく。", font_size=18),
            self._line("どの扉を選んでも、最初に当たる確率は", MathTex(r"\dfrac{1}{3}", font_size=28, color=YELLOW), "です。", font_size=18),
            self.ja_text("司会が外れを 1 枚開けたあと、閉まった扉は 2 枚です。", font_size=18),
            self._line(
                "残った 2 枚が同じように見えるので、当たる確率はどちらも",
                MathTex(r"\dfrac{1}{2}", font_size=28, color=YELLOW),
                "だと思ってしまいます。",
                font_size=16,
            ),
        ]
        block = self._formula_rows(rows, lead, buff=0.12, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(block), run_time=0.45)
        self.pause_topic()

        table = self.aligned_table(
            [
                [
                    self.ja_text("考え方", font_size=16, color=GREY_B),
                    self.ja_text("当たる確率", font_size=16, color=GREY_B),
                ],
                [
                    self.ja_text("残った 2 枚は同じ", font_size=20),
                    MathTex(r"\dfrac{1}{2}", font_size=28, color=YELLOW),
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
                "残った 2 枚が同じに見える、という考え方です。司会がどの扉を開けたのかは、まだ使っていません。",
                font_size=18,
            ),
            self.ja_text(
                "この問いが欲しいのは、残った枚数が 2 枚であることではなく、乗り換えたときに当たる確率です。",
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

    def part_trial_few(self):
        chip = self.begin_step("試行  少数回", self.header)

        lead = self.ja_text(
            "こんどは、同じルールで何回か遊んでみて、乗り換えと残留のどちらが当たるかを数えてみます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)
        self.play(FadeOut(lead), run_time=0.45)

        rounds = [
            (0, 1, 0, False, "1 回目。最初の扉のまま残ります。当たりです。"),
            (0, 2, 1, True, "2 回目。残った扉へ乗り換えます。当たりです。"),
            (0, 1, 0, True, "3 回目。残った扉へ乗り換えます。外れです。"),
        ]
        fig = self._doors(pick=rounds[0][0], opened=rounds[0][1], prize=rounds[0][2], show_prize=True)
        self.below_chip(fig, chip, buff=0.22)
        fig.set_x(0)
        cap = self.ja_text(rounds[0][4], font_size=18)
        self._fit(cap, 13.0)
        self.stack_below(cap, fig, buff=0.40)
        cap.set_x(0)
        self.play(FadeIn(fig), FadeIn(cap), run_time=0.7)
        self.pause_new_screen()
        self.linger(rounds[0][4])

        for pick, opened, prize, switched, text in rounds[1:]:
            nxt = self._doors(pick=pick, opened=opened, prize=prize, show_prize=True)
            nxt.move_to(fig)
            new_cap = self.ja_text(text, font_size=18)
            self._fit(new_cap, 13.0)
            self.stack_below(new_cap, nxt, buff=0.40)
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
                    self.ja_text("やり方", font_size=16, color=GREY_B),
                    self.ja_text("3 回のうち当たった回数", font_size=16, color=GREY_B),
                ],
                [
                    self.ja_text("最初の扉のまま", font_size=20),
                    MathTex(r"1", font_size=28),
                ],
                [
                    self.ja_text("残った扉へ乗り換え", font_size=20),
                    MathTex(r"1", font_size=28),
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
                "3 回だけだと、どちらがよいかはまだ決まりません。当たり外れが、回ごとに入れ替わります。",
                font_size=18,
            ),
            self.ja_text(
                "少数回の実験では、ばらつきが大きすぎて、本当の割合が見えません。",
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
        chip = self.begin_step("STEP 1  ルール", self.header)

        lead = self.ja_text(
            "乗り換えたときに当たる確率を出すために、ゲームの決まりを、先に言葉で書いておきます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        defs = [
            self._line("扉の枚数を", MathTex(r"3", font_size=26, color=YELLOW), "とおく。番号を", MathTex(r"1,2,3", font_size=26), "とおく。", font_size=18),
            self.ja_text("当たりは、3 枚のどれかへ、同じ確からしさで入る、とおく。", font_size=18),
            self.ja_text("あなたは、最初に扉を 1 枚選ぶ、とおく。あとで番号は 1 に固定します。", font_size=18),
            self.ja_text("司会は、あなたが選んでいない外れの扉を、必ず 1 枚開ける、とおく。", font_size=18),
            self.ja_text("司会は当たりの扉を開けない。あなたが選んだ扉も開けない、とおく。", font_size=18),
        ]
        block = self._formula_rows(defs, lead, buff=0.12)
        self.pause_conclusion()
        self.play(FadeOut(block), run_time=0.45)
        self.pause_topic()

        notes = [
            self.ja_text(
                "司会が開ける扉は、当たりの場所と、最初の選択によって決まります。",
                font_size=18,
            ),
            self.ja_text(
                "残った 2 枚が同じかどうかは、この決まりを使ってから判断します。",
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

    def part_step2_first_hit(self):
        chip = self.begin_step("STEP 2  最初に当たる", self.header)

        lead = self.ja_text("最初に選んだ扉が、当たりだった場合を、最後まで追います。", font_size=18)
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        restate = self._line(
            "当たりは 3 枚のどれかへ同じ確からしさ。最初に選ぶ扉を",
            MathTex(r"1", font_size=24, color=YELLOW),
            "とおく。",
            font_size=18,
        )
        self.stack_below(restate, lead, buff=0.10)
        restate.set_x(0)
        self.play(FadeIn(restate), run_time=0.55)
        self.pause_short_formula()
        self.linger("最初に選ぶ扉を 1 とおく。")
        self.play(FadeOut(lead), run_time=0.45)

        fig = self._doors(pick=0, opened=1, prize=0, show_prize=True)
        self.stack_below(fig, restate, buff=0.28)
        fig.set_x(0)
        cap = self.ja_text(
            "当たりも扉 1 です。司会は外れの扉 2 を開けます。残った扉 3 へ乗り換えると外れです。",
            font_size=18,
        )
        self._fit(cap, 13.0)
        self.stack_below(cap, fig, buff=0.40)
        cap.set_x(0)
        self.play(FadeIn(fig), FadeIn(cap), run_time=0.7)
        self.pause_new_screen()
        self.linger(cap.text)

        self.play(FadeOut(VGroup(fig, cap)), run_time=0.45)
        self.pause_topic()

        rows = [
            self._line("最初に当たる確率は", MathTex(r"\dfrac{1}{3}", font_size=30, color=YELLOW), "です。", font_size=20),
            self.ja_text("このとき、残った閉まった扉は外れです。", font_size=20),
            self.ja_text("だから、乗り換えると外れます。最初の扉のままだと当たります。", font_size=18),
        ]
        block = self._formula_rows(rows, restate, buff=0.14, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(block), run_time=0.45)
        self.pause_topic()

        notes = [
            self.ja_text("最初に当たりを選んでいるなら、乗り換えは負けです。", font_size=18),
            self.ja_text("この場合の割合は、まだ全体の一部です。外した場合も数えます。", font_size=18),
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

    def part_step3_first_miss(self):
        chip = self.begin_step("STEP 3  最初に外れる", self.header)

        lead = self.ja_text("こんどは、最初に選んだ扉が、外れだった場合を、最後まで追います。", font_size=18)
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        restate = self._line(
            "最初に選ぶ扉を",
            MathTex(r"1", font_size=24, color=YELLOW),
            "とおく。当たりは扉",
            MathTex(r"2", font_size=24, color=GREEN),
            "とします。",
            font_size=18,
        )
        self.stack_below(restate, lead, buff=0.10)
        restate.set_x(0)
        self.play(FadeIn(restate), run_time=0.55)
        self.pause_short_formula()
        self.linger("最初に選ぶ扉を 1 とおく。当たりは扉 2 とします。")
        self.play(FadeOut(lead), run_time=0.45)

        fig = self._doors(pick=0, opened=2, prize=1, show_prize=True)
        self.stack_below(fig, restate, buff=0.28)
        fig.set_x(0)
        cap = self.ja_text(
            "司会は外れの扉 3 しか開けられません。残った扉 2 へ乗り換えると当たりです。",
            font_size=18,
        )
        self._fit(cap, 13.0)
        self.stack_below(cap, fig, buff=0.40)
        cap.set_x(0)
        self.play(FadeIn(fig), FadeIn(cap), run_time=0.7)
        self.pause_new_screen()
        self.linger(cap.text)

        nxt = self._doors(pick=0, opened=1, prize=2, show_prize=True)
        nxt.move_to(fig)
        new_cap = self.ja_text(
            "当たりが扉 3 のときも、司会は扉 2 を開けます。扉 3 へ乗り換えると当たりです。",
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

        rows = [
            self._line("最初に外れる確率は", MathTex(r"1-\dfrac{1}{3}=\dfrac{2}{3}", font_size=28, color=GREEN), "です。", font_size=18),
            self.ja_text("当たりは、選んでいない 2 枚のうち 1 枚にあります。", font_size=18),
            self.ja_text("司会は、選んでいない外れを必ず開けるので、残った閉まった扉が当たりです。", font_size=18),
            self.ja_text("だから、乗り換えると当たります。", font_size=20),
        ]
        block = self._formula_rows(rows, restate, buff=0.12, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(block), run_time=0.45)
        self.pause_topic()

        notes = [
            self.ja_text("最初に外れを選んでいるなら、司会が残した扉が当たりです。乗り換えは勝ちです。", font_size=18),
            self.ja_text("この場合は、最初に当たる場合より多いです。", font_size=18),
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

    def part_step4_combine(self):
        chip = self.begin_step("STEP 4  合わせる", self.header)

        lead = self.ja_text("当たる場合と外れる場合を、場合を分けて数える方法で足します。", font_size=18)
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        restate = self._line(
            "最初に当たる確率は",
            MathTex(r"\dfrac{1}{3}", font_size=24, color=YELLOW),
            "。最初に外れる確率は",
            MathTex(r"\dfrac{2}{3}", font_size=24, color=GREEN),
            "。",
            font_size=18,
        )
        self.stack_below(restate, lead, buff=0.10)
        restate.set_x(0)
        self.play(FadeIn(restate), run_time=0.55)
        self.pause_short_formula()
        self.linger("最初に当たる確率は 1/3。最初に外れる確率は 2/3。")

        rows = [
            self.ja_text("乗り換えて当たるのは、最初に外れたときです。", font_size=18),
            self._line("その割合は", MathTex(r"\dfrac{2}{3}", font_size=30, color=GREEN), "です。", font_size=20),
            self.ja_text("最初の扉のままで当たるのは、最初に当たったときです。", font_size=18),
            self._line("その割合は", MathTex(r"\dfrac{1}{3}", font_size=30, color=YELLOW), "です。", font_size=20),
            MathTex(r"\dfrac{1}{3}+\dfrac{2}{3}=\dfrac{3}{3}=1", font_size=32, color=YELLOW),
        ]
        block = self._formula_rows(rows, restate, buff=0.10, hold=self.PAUSE_COMPLEX)
        self.play(FadeOut(block), run_time=0.45)
        self.pause_topic()

        table = self.aligned_table(
            [
                [
                    self.ja_text("やり方", font_size=16, color=GREY_B),
                    self.ja_text("当たる確率", font_size=16, color=GREY_B),
                ],
                [
                    self.ja_text("最初の扉のまま", font_size=20),
                    MathTex(r"\dfrac{1}{3}", font_size=26, color=YELLOW),
                ],
                [
                    self.ja_text("残った扉へ乗り換え", font_size=20),
                    MathTex(r"\dfrac{2}{3}", font_size=26, color=GREEN),
                ],
                [
                    self.ja_text("残った 2 枚は同じ、と思ったとき", font_size=18),
                    MathTex(r"\dfrac{1}{2}", font_size=26),
                ],
            ],
            h_buff=0.32,
            v_buff=0.08,
        )
        table.scale(0.82)
        self.stack_below(table, restate, buff=0.14)
        table.set_x(0)
        self.reveal_table(table, row_wait=1.20)

        notes = [
            self.ja_text(
                "残った 2 枚が同じに見える、という考え方は、司会が開けざるを得ない扉を無視しています。",
                font_size=18,
            ),
            self.ja_text(
                "乗り換えた方が、当たる確率は大きくなります。半分ではありません。",
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
            self.linger(mob.text)

    def part_example(self):
        chip = self.begin_step("実例", self.header)

        lead = self.ja_text(
            "当たりの場所を 1 枚ずつ動かして、最初の選択を扉 1 に固定し、3 通りを最後まで数えます。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)
        self.play(FadeOut(lead), run_time=0.45)

        cases = [
            (0, 1, 0, "当たりが扉 1。司会は扉 2 か 3 を開けます。乗り換えると外れです。"),
            (0, 2, 1, "当たりが扉 2。司会は扉 3 を開けます。扉 2 へ乗り換えると当たりです。"),
            (0, 1, 2, "当たりが扉 3。司会は扉 2 を開けます。扉 3 へ乗り換えると当たりです。"),
        ]
        fig = self._doors(pick=cases[0][0], opened=cases[0][1], prize=cases[0][2], show_prize=True)
        self.below_chip(fig, chip, buff=0.22)
        fig.set_x(0)
        cap = self.ja_text(cases[0][3], font_size=18)
        self._fit(cap, 13.0)
        self.stack_below(cap, fig, buff=0.40)
        cap.set_x(0)
        self.play(FadeIn(fig), FadeIn(cap), run_time=0.7)
        self.pause_new_screen()
        self.linger(cases[0][3])

        for pick, opened, prize, text in cases[1:]:
            nxt = self._doors(pick=pick, opened=opened, prize=prize, show_prize=True)
            nxt.move_to(fig)
            new_cap = self.ja_text(text, font_size=18)
            self._fit(new_cap, 13.0)
            self.stack_below(new_cap, nxt, buff=0.40)
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
                    self.ja_text("当たりの場所", font_size=14, color=GREY_B),
                    self.ja_text("司会が開ける扉", font_size=14, color=GREY_B),
                    self.ja_text("乗り換え先", font_size=14, color=GREY_B),
                    self.ja_text("乗り換え", font_size=14, color=GREY_B),
                ],
                [
                    MathTex(r"1", font_size=24),
                    self.ja_text("2 または 3", font_size=18),
                    self.ja_text("残り 1 枚", font_size=18),
                    self.ja_text("外れ", font_size=18),
                ],
                [
                    MathTex(r"2", font_size=24),
                    MathTex(r"3", font_size=24),
                    MathTex(r"2", font_size=24),
                    self.ja_text("当たり", font_size=18, color=GREEN),
                ],
                [
                    MathTex(r"3", font_size=24),
                    MathTex(r"2", font_size=24),
                    MathTex(r"3", font_size=24),
                    self.ja_text("当たり", font_size=18, color=GREEN),
                ],
            ],
            h_buff=0.22,
            v_buff=0.08,
        )
        table.scale(0.78)
        self.below_chip(table, chip, buff=0.18)
        table.set_x(0)
        self.reveal_table(table, row_wait=1.20)

        notes = [
            self._line(
                "3 通りは同じ確からしさです。乗り換えが当たりなのは 2 行。",
                MathTex(r"\dfrac{1}{3}+\dfrac{1}{3}=\dfrac{2}{3}", font_size=24, color=GREEN),
                font_size=16,
            ),
            self.ja_text(
                "当たりの場所が 3 通りあるとき、乗り換えが当たるのはそのうち 2 通りです。",
                font_size=18,
            ),
            self.ja_text(
                "残った 2 枚が同じ、という見方では、この 2 通りと 1 通りの差が見えません。",
                font_size=18,
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
                self.pause_conclusion()
            else:
                self.linger(mob.text)

    def part_generalize(self):
        chip = self.begin_step("一般化", self.header)

        lead = self.ja_text(
            "今やったことは、新しい情報のあとで、最初の場合分けの割合を付け替える考え方でした。",
            font_size=18,
        )
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.7)
        self.linger(lead.text)

        first = [
            self.ja_text("当たりは、最初は 3 枚のどれかへ同じ確からしさで入る、とおく。", font_size=18),
            self.ja_text("司会は、選んでいない外れを必ず開ける、とおく。", font_size=18),
            self.ja_text(
                "モンティ・ホール問題と呼ばれます。司会が外れを開けたあとでも、残った 2 枚の当たる確率は同じではありません。",
                font_size=16,
            ),
            self._line("最初に選んだ扉が当たりである確率は、あとも", MathTex(r"\dfrac{1}{3}", font_size=26, color=YELLOW), "のままです。", font_size=16),
            self._line("選んでいない側に載っていた", MathTex(r"\dfrac{2}{3}", font_size=26, color=GREEN), "は、司会が開けなかった 1 枚へ集まります。", font_size=16),
            self._line("だから、残った扉へ乗り換えると、当たる確率は", MathTex(r"\dfrac{2}{3}", font_size=28, color=GREEN), "です。", font_size=16),
        ]
        block = self._formula_rows(first, lead, buff=0.10, hold=self.PAUSE_CONCLUSION)
        self.play(FadeOut(VGroup(lead, block)), run_time=0.45)
        self.pause_topic()

        name = self.ja_text("司会は当たりを開けない。選んだ扉も開けない。", font_size=18, color=GREY_B)
        self.below_chip(name, chip, buff=0.16)
        self.play(FadeIn(name), run_time=0.55)
        self.linger(name.text)

        close = [
            self._line(
                "情報を得たあとも、最初の",
                MathTex(r"\dfrac{1}{3}", font_size=24, color=YELLOW),
                "は自分の扉に残ります。",
                font_size=18,
            ),
            self._line(
                "残りの",
                MathTex(r"\dfrac{2}{3}", font_size=24, color=GREEN),
                "は、開けられなかった扉へ移ります。",
                font_size=18,
            ),
            self.ja_text("場合の割合を、司会が開けたあとに付け替える、という方法です。", font_size=18, color=GREY_B),
        ]
        self._formula_rows(close, name, buff=0.12)

    def part_summary(self):
        chip = self.begin_step("まとめ", self.header)

        rows = [
            self.ja_text("残った 2 枚が同じに見える、という考え方は、司会が開けた扉の情報を使っていません", font_size=18),
            self._line("最初に当たりを選ぶ確率は", MathTex(r"\dfrac{1}{3}", font_size=24, color=YELLOW), "です。そのときは、乗り換えると外れます", font_size=16),
            self._line("最初に外れを選ぶ確率は", MathTex(r"\dfrac{2}{3}", font_size=24, color=GREEN), "です。そのときは、司会が残した扉が当たりです", font_size=16),
            self._line("だから、残った扉へ乗り換えると、当たる確率は", MathTex(r"\dfrac{2}{3}", font_size=24, color=GREEN), "です", font_size=16),
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
            "扉が",
            MathTex(r"100", font_size=20, color=GREY_B),
            "枚でも同じです。1 枚選んだあと、司会が外れを",
            MathTex(r"98", font_size=20, color=GREY_B),
            "枚開けると、残った 1 枚へ乗り換えたときに当たる確率は",
            MathTex(r"\dfrac{99}{100}", font_size=20, color=GREY_B),
            "です。",
            font_size=16,
            color=GREY_B,
        )
        self.stack_below(trivia, shown, buff=0.22)
        self._fit_left(trivia)
        self.play(FadeIn(trivia), run_time=0.70)
        self.linger(
            "扉が 100 枚でも同じです。1 枚選んだあと、司会が外れを 98 枚開けると、残った 1 枚へ乗り換えたときに当たる確率は 99/100 です。",
            extra=0.40,
        )
        self.pause_conclusion()

    def _doors(self, pick=None, opened=None, prize=None, show_prize=False):
        cells = VGroup()
        for i in range(3):
            stroke = YELLOW if pick == i else GREY_B
            width = 5.0 if pick == i else 2.0
            rect = RoundedRectangle(
                width=1.55,
                height=1.90,
                corner_radius=0.10,
                color=stroke,
                stroke_width=width,
            )
            rect.set_fill(GREY_E, 0.85)
            inner = VGroup()
            lab = MathTex(rf"{i + 1}", font_size=28)
            if opened == i:
                rect.set_fill(GREY_D, 0.35)
                blob = Circle(radius=0.22, color=GREY_B, fill_opacity=1.0)
                mark = self.ja_text("外れ", font_size=16, color=GREY_B)
                mark.next_to(blob, DOWN, buff=0.08)
                inner.add(blob, mark)
                lab.next_to(rect, UP, buff=0.08)
            elif show_prize and prize == i:
                star = Star(n=5, outer_radius=0.28, inner_radius=0.12, color=GOLD, fill_opacity=1.0)
                tag = self.ja_text("当たり", font_size=16, color=GOLD)
                tag.next_to(star, DOWN, buff=0.08)
                inner.add(star, tag)
                lab.next_to(rect, UP, buff=0.08)
            else:
                lab.move_to(rect.get_center())
            if inner:
                inner.move_to(rect.get_center() + DOWN * 0.12)
            cells.add(VGroup(rect, lab, inner))
        return cells.arrange(RIGHT, buff=0.35)

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
