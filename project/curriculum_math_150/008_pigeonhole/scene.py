from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import LessonScene


class Pigeonhole(LessonScene):
    """#8 13 人いれば同じ星座の 2 人がいるか（約8分）"""

    DOT_COLORS = [GOLD, ORANGE, TEAL, BLUE_B, GREEN, PURPLE, PINK, RED]

    def construct(self):
        self.header = self._open_header()
        self.part_question()
        self.part_trial_scatter()
        self.part_trial_average()
        self.part_step1_boxes()
        self.part_step2_worst()
        self.part_step3_one_more()
        self.part_step4_three()
        self.part_example()
        self.part_generalize()
        self.part_summary()

    def _open_header(self):
        title = self._line(
            MathTex(r"13", font_size=40),
            "人いれば同じ星座の",
            MathTex(r"2", font_size=40),
            "人がいるか",
            font_size=36,
        )
        self.play(FadeIn(title), run_time=0.8)
        self.linger(1.2)
        self.play(title.animate.scale(0.52).to_edge(UP, buff=0.16), run_time=0.5)
        title.set_x(0)
        return title

    def part_question(self):
        fig = self._bins([0] * 12)
        cap = self.ja_text("箱は星座です。12 個あります。", font_size=22)
        right = VGroup(cap).arrange(DOWN, buff=0.12)
        pair = VGroup(fig, right).arrange(RIGHT, buff=0.45, aligned_edge=UP)
        pair.next_to(self.header, DOWN, buff=0.32)
        pair.set_x(0)
        self._nudge(pair)
        self.play(FadeIn(fig), FadeIn(right), run_time=0.8)
        self.linger(3.2)

        q1 = self.ja_text(
            "同じ星座の人が少なくとも 2 人いることを、何人集まれば保証できるでしょう。",
            font_size=24,
        )
        q1.next_to(pair, DOWN, buff=0.28)
        q1.set_x(0)
        self._fit(q1, 13.0)
        q1.set_x(0)
        self.play(FadeIn(q1), run_time=0.45)
        self.linger(q1.text)

        q2 = self.ja_text("12 人では、足りないのでしょうか。", font_size=26)
        self.stack_below(q2, q1, buff=0.14)
        q2.set_x(0)
        self.play(FadeIn(q2), run_time=0.45)
        self.linger(q2.text, extra=0.35)

    def part_trial_scatter(self):
        self.wipe(self.header)
        chip = self.step_label("試行  ばらす")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("まず、12 人を、できるだけ違う星座に分けてみます。", font_size=22)
        self.below_chip(lead, chip, buff=0.18)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        counts = [0] * 12
        fig = self._bins(counts)
        notes = [
            self.ja_text("1 人目。箱 1 に 1 人。同じ星座の 2 人はまだいない。", font_size=18),
            self.ja_text("2 人目。箱 2 に 1 人。まだいない。", font_size=18),
            self.ja_text("3 人目。箱 3 に 1 人。まだいない。", font_size=18),
        ]
        block = VGroup(*notes).arrange(DOWN, buff=0.10, aligned_edge=LEFT)
        pair = VGroup(fig, block).arrange(RIGHT, buff=0.36, aligned_edge=UP)
        self.stack_below(pair, lead, buff=0.14)
        pair.set_x(0)
        self._nudge(pair)
        self.play(FadeIn(fig), run_time=0.55)

        for i, note in enumerate(notes):
            counts[i] = 1
            nxt = self._bins(counts)
            nxt.move_to(fig)
            self.play(FadeOut(fig), FadeIn(nxt), FadeIn(note), run_time=0.5)
            fig = nxt
            self.linger(3.2)

        rest = self.ja_text("残り 9 人も、空いている箱へ 1 人ずつ入れます。", font_size=18)
        self.stack_below(rest, block, buff=0.10)
        self.play(FadeIn(rest), run_time=0.35)
        self.linger(rest.text)
        filled = self._bins([1] * 12)
        filled.move_to(fig)
        self.play(FadeOut(fig), FadeIn(filled), run_time=0.55)
        fig = filled
        self.linger(3.2)

        eq = MathTex(r"1+1+\cdots+1=12", font_size=30, color=YELLOW)
        self.stack_below(eq, rest, buff=0.12)
        self.play(FadeIn(eq), run_time=0.4)
        self.linger(3.2)

        self.play(FadeOut(VGroup(fig, block, rest, eq)), run_time=0.3)
        close = [
            self.ja_text("12 人までなら、全員違う星座がありえます。", font_size=22),
            self.ja_text("同じ星座の 2 人は、この分け方では出ません。", font_size=22),
            self.ja_text("だから 12 人では、保証になりません。", font_size=22),
        ]
        shown = VGroup()
        for i, mob in enumerate(close):
            if i == 0:
                self.stack_below(mob, lead, buff=0.22)
            else:
                self.stack_below(mob, shown, buff=0.12)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.4)
            shown.add(mob)
            self.linger(3.2)

    def part_trial_average(self):
        self.wipe(self.header)
        chip = self.step_label("試行  平均")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("人数を箱の数で割って、平均で見てみます。", font_size=22)
        self.below_chip(lead, chip, buff=0.18)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        table = self.aligned_table(
            [
                [
                    self.ja_text("人数", font_size=16, color=GREY_B),
                    self.ja_text("平均", font_size=16, color=GREY_B),
                    self.ja_text("同じ星座の 2 人", font_size=16, color=GREY_B),
                ],
                [
                    MathTex(r"12", font_size=24),
                    MathTex(r"12\div 12=1", font_size=24),
                    self.ja_text("出ない配置がある", font_size=20),
                ],
                [
                    MathTex(r"13", font_size=24),
                    MathTex(r"13\div 12=1.083\ldots", font_size=22),
                    self.ja_text("平均は 1 を少し超える", font_size=20),
                ],
            ],
            h_buff=0.28,
            v_buff=0.12,
        )
        table.scale(0.82)
        self.stack_below(table, lead, buff=0.16)
        table.set_x(0)
        self.reveal_table(table, row_wait=0.72)

        notes = [
            self.ja_text("12 人の平均はぴったり 1 です。1 箱 1 人で割れます。", font_size=20),
            self.ja_text(
                "13 人の平均は 1 より大きい。少し超えただけなら、まだ全員違う配置が残るのでは、と思ってしまいます。",
                font_size=20,
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
            self.play(FadeIn(mob), run_time=0.4)
            shown.add(mob)
            self.linger(3.2)

        self.play(FadeOut(VGroup(table, shown)), run_time=0.3)
        fig = self._bins([1] * 12)
        extra = Dot(radius=0.12, color=YELLOW)
        lost = self.ja_text("13 人目。空の箱がない。", font_size=18)
        right = VGroup(extra, lost).arrange(DOWN, buff=0.16)
        pair = VGroup(fig, right).arrange(RIGHT, buff=0.40, aligned_edge=UP)
        self.stack_below(pair, lead, buff=0.14)
        pair.set_x(0)
        self._nudge(pair)
        self.play(FadeIn(fig), FadeIn(right), run_time=0.6)
        self.linger(3.4)

        close = [
            self.ja_text("全員違う星座にするには、箱が 13 個いります。", font_size=22),
            self.ja_text("箱は 12 個のままなので、平均の小数だけでは保証が見えません。", font_size=22),
        ]
        shown2 = VGroup()
        for i, mob in enumerate(close):
            if i == 0:
                self.stack_below(mob, pair, buff=0.16)
            else:
                self.stack_below(mob, shown2, buff=0.10)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.4)
            shown2.add(mob)
            self.linger(3.2)

    def part_step1_boxes(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 1  箱")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("保証を、箱と人数の言葉で書いておきます。", font_size=22)
        self.below_chip(lead, chip, buff=0.20)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        defs = [
            self._line(MathTex(r"n", font_size=28, color=YELLOW), "を、箱の個数とおく。星座なら", MathTex(r"n=12", font_size=28), font_size=22),
            self._line(MathTex(r"m", font_size=28, color=ORANGE), "を、人の人数とおく。", font_size=22),
            self.ja_text("「保証」を、どんな分け方でも、どれかの箱に 2 人以上いること、とおく。", font_size=20),
        ]
        self._formula_rows(defs, lead, buff=0.18)
        self.linger(3.4)

        notes = [
            self.ja_text("平均が 1 を超えることと、保証とは、まだ同じではありません。", font_size=22),
            self.ja_text("同じ星座が 2 人出ない配置を、どこまで長く保てるかを見ます。", font_size=22),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                mob.to_edge(DOWN, buff=0.70)
            else:
                self.stack_below(mob, shown, buff=0.10)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.4)
            shown.add(mob)
            self.linger(3.2)

    def part_step2_worst(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 2  最悪")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("同じ星座が 2 人出ないように、できるだけ大勢を置いてみます。", font_size=20)
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        restate = self._line(
            MathTex(r"n", font_size=24, color=YELLOW),
            "を箱の個数、",
            MathTex(r"m", font_size=24, color=ORANGE),
            "を人数とおく。",
            font_size=20,
        )
        self.stack_below(restate, lead, buff=0.10)
        restate.set_x(0)
        self.play(FadeIn(restate), run_time=0.4)
        self.linger(3.2)

        fig = self._bins([1] * 12)
        rows = [
            self.ja_text("どの箱も、高々 1 人まで。", font_size=18),
            self._line("箱は", MathTex(r"n", font_size=24, color=YELLOW), "個なので、置ける人数は高々", MathTex(r"n", font_size=24, color=YELLOW), "人。", font_size=18),
            MathTex(r"m\le n", font_size=32, color=YELLOW),
            MathTex(r"n=12 \Rightarrow m\le 12", font_size=28),
        ]
        block = VGroup(*rows).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        pair = VGroup(fig, block).arrange(RIGHT, buff=0.36, aligned_edge=UP)
        self.stack_below(pair, restate, buff=0.12)
        pair.set_x(0)
        self._nudge(pair)
        self.play(FadeIn(fig), run_time=0.55)
        for row in rows:
            self.play(FadeIn(row), run_time=0.35)
            self.linger(3.2)

        notes = [
            self.ja_text("これが、同じ星座の 2 人が出ない配置の、いちばん人数が多い場合です。", font_size=20),
            self.ja_text("これより 1 人多いと、上限 1 人が破れます。", font_size=20),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, pair, buff=0.14)
            else:
                self.stack_below(mob, shown, buff=0.08)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.4)
            shown.add(mob)
            self.linger(3.2)

    def part_step3_one_more(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 3  もう1人")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("最悪の配置に、もう 1 人足します。", font_size=22)
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        restate = self._line(
            MathTex(r"n", font_size=24, color=YELLOW),
            "を箱の個数とおく。いま",
            MathTex(r"m=n", font_size=24, color=ORANGE),
            "人まで置いた。",
            font_size=20,
        )
        self.stack_below(restate, lead, buff=0.10)
        restate.set_x(0)
        self._fit(restate, 13.0)
        restate.set_x(0)
        self.play(FadeIn(restate), run_time=0.4)
        self.linger(3.2)

        counts = [1] * 12
        fig = self._bins(counts)
        extra = Dot(radius=0.13, color=YELLOW)
        tag = self.ja_text("13 人目", font_size=18, color=YELLOW)
        pend = VGroup(tag, extra).arrange(DOWN, buff=0.10)
        pair = VGroup(fig, pend).arrange(RIGHT, buff=0.40, aligned_edge=UP)
        self.stack_below(pair, restate, buff=0.12)
        pair.set_x(0)
        self._nudge(pair)
        self.play(FadeIn(fig), FadeIn(pend), run_time=0.6)
        self.linger(3.2)

        empty = self.ja_text("空の箱はもうない。", font_size=20)
        self.stack_below(empty, pair, buff=0.12)
        empty.set_x(0)
        self.play(FadeIn(empty), run_time=0.35)
        self.linger(empty.text)

        counts[5] = 2
        nxt = self._bins(counts, highlight=5)
        nxt.move_to(fig)
        self.play(FadeOut(fig), FadeOut(pend), FadeIn(nxt), run_time=0.55)
        fig = nxt
        self.linger(3.4)

        rows = [
            self.ja_text("13 人目は、すでに 1 人いる箱に入る。その箱は 2 人になる。", font_size=20),
            MathTex(r"m=n+1", font_size=36, color=YELLOW),
            MathTex(r"12+1=13", font_size=32, color=GREEN),
        ]
        self.play(FadeOut(VGroup(fig, empty)), run_time=0.3)
        shown = VGroup()
        for i, mob in enumerate(rows):
            if i == 0:
                self.stack_below(mob, restate, buff=0.16)
            else:
                self.stack_below(mob, shown, buff=0.10)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.4)
            shown.add(mob)
            self.linger(3.2)

        close = [
            self.ja_text("12 個の星座なら、13 人集まれば、同じ星座が少なくとも 2 人います。", font_size=20),
            self.ja_text("これは起こりやすさの話ではなく、避けられない配置の話です。", font_size=20),
        ]
        shown2 = VGroup()
        for i, mob in enumerate(close):
            if i == 0:
                self.stack_below(mob, shown, buff=0.14)
            else:
                self.stack_below(mob, shown2, buff=0.08)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.4)
            shown2.add(mob)
            self.linger(3.2)

    def part_step4_three(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 4  3人以上")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("同じ星座が 3 人いることを保証するには、何人いればよいかを、同じ方法で見ます。", font_size=20)
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        first = [
            self._line(MathTex(r"n", font_size=24, color=YELLOW), "を箱の個数とおく。星座なら", MathTex(r"n=12", font_size=24), font_size=18),
            self._line(MathTex(r"r", font_size=24, color=TEAL), "を、同じ箱に集めたい人数の下限とおく。いま", MathTex(r"r=3", font_size=24, color=TEAL), font_size=18),
            self.ja_text("同じ星座が 3 人出ないようにする。どの箱も高々 2 人。", font_size=20),
            MathTex(r"12\times 2=24", font_size=32),
            MathTex(r"24+1=25", font_size=32, color=YELLOW),
        ]
        block = self._formula_rows(first, lead, buff=0.12)
        self.play(FadeOut(block), run_time=0.3)

        second = [
            self._line("どの箱も高々", MathTex(r"r-1", font_size=24), "人なら、人数は高々", MathTex(r"n(r-1)", font_size=26), font_size=18),
            self._line("もう 1 人足すと", MathTex(r"n(r-1)+1", font_size=28, color=YELLOW), font_size=20),
            MathTex(r"r=2 \Rightarrow n(2-1)+1=n+1", font_size=28),
            MathTex(r"r=3,\ n=12 \Rightarrow 12\cdot(3-1)+1=24+1=25", font_size=26, color=GREEN),
        ]
        block2 = self._formula_rows(second, lead, buff=0.12)
        self.linger(3.4)
        self.play(FadeOut(block2), run_time=0.3)

        table = self.aligned_table(
            [
                [
                    MathTex(r"n", font_size=22, color=YELLOW),
                    MathTex(r"r", font_size=22, color=TEAL),
                    self.ja_text("最悪", font_size=16, color=GREY_B),
                    self.ja_text("保証", font_size=16, color=GREY_B),
                ],
                [MathTex(r"12", font_size=24), MathTex(r"2", font_size=24), MathTex(r"12", font_size=24), MathTex(r"13", font_size=24, color=GREEN)],
                [MathTex(r"12", font_size=24), MathTex(r"3", font_size=24), MathTex(r"24", font_size=24), MathTex(r"25", font_size=24, color=GREEN)],
                [MathTex(r"3", font_size=24), MathTex(r"2", font_size=24), MathTex(r"3", font_size=24), MathTex(r"4", font_size=24, color=GREEN)],
            ],
            h_buff=0.32,
            v_buff=0.10,
        )
        table.scale(0.82)
        self.stack_below(table, lead, buff=0.14)
        table.set_x(0)
        self.reveal_table(table, row_wait=0.70)

        note = self.ja_text("避けたい上限いっぱいに詰めてから、1 人足す、というやり方です。", font_size=20)
        self.stack_below(note, table, buff=0.14)
        note.set_x(0)
        self._fit(note, 13.0)
        note.set_x(0)
        self.play(FadeIn(note), run_time=0.4)
        self.linger(note.text, extra=0.30)

    def part_example(self):
        self.wipe(self.header)
        chip = self.step_label("実例")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("箱が 3 つのときを、最初から最後まで数えます。", font_size=22)
        self.below_chip(lead, chip, buff=0.16)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        restate = self._line(
            MathTex(r"n=3", font_size=24, color=YELLOW),
            "、",
            MathTex(r"r=2", font_size=24, color=TEAL),
            "とおく。引き出しは 3 色。",
            font_size=20,
        )
        self.stack_below(restate, lead, buff=0.10)
        restate.set_x(0)
        self.play(FadeIn(restate), run_time=0.4)
        self.linger(3.2)

        sock_colors = [BLUE_B, GREEN, ORANGE]
        names = ["青", "緑", "橙"]
        counts = [0, 0, 0]
        fig = self._sock_bins(counts, sock_colors, names)
        steps = [
            ([1, 0, 0], "1 足目。青に 1。"),
            ([1, 1, 0], "2 足目。緑に 1。まだ同じ色が 2 足はない。"),
            ([1, 1, 1], "3 足目。橙に 1。どの引き出しも 1 足。これが最悪。"),
            ([2, 1, 1], "4 足目。空の引き出しはない。同じ色が 2 足になる。"),
        ]
        caption = self.ja_text(steps[0][1], font_size=18)
        pair = VGroup(fig, caption).arrange(RIGHT, buff=0.40, aligned_edge=UP)
        self.stack_below(pair, restate, buff=0.12)
        pair.set_x(0)
        self._nudge(pair)
        self.play(FadeIn(fig), FadeIn(caption), run_time=0.5)

        for counts, text in steps:
            nxt = self._sock_bins(
                counts,
                sock_colors,
                names,
                highlight=0 if counts[0] == 2 else None,
            )
            nxt.move_to(fig)
            new_cap = self.ja_text(text, font_size=18)
            new_cap.move_to(caption)
            self.play(FadeOut(fig), FadeIn(nxt), Transform(caption, new_cap), run_time=0.5)
            fig = nxt
            self.linger(3.2)

        eq = MathTex(r"n(r-1)+1=3\cdot 1+1=4", font_size=28, color=YELLOW)
        self.stack_below(eq, pair, buff=0.16)
        eq.set_x(0)
        self.play(FadeIn(eq), run_time=0.4)
        self.linger(3.4)

        self.play(FadeOut(VGroup(fig, caption, eq)), run_time=0.3)
        three = [
            self._line(MathTex(r"r=3", font_size=26, color=TEAL), "なら、最悪は各色 2 足で 6 足。", font_size=20),
            MathTex(r"3\cdot(3-1)+1=6+1=7", font_size=32, color=YELLOW),
            self.ja_text("3 色なら、4 足で同じ色が 2 足。7 足で同じ色が 3 足です。", font_size=20),
            self.ja_text("星座の 12 と 13 も、箱の数だけが違う同じ数え方です。", font_size=20),
        ]
        self._formula_rows(three, restate, buff=0.16)

    def part_generalize(self):
        self.wipe(self.header)
        chip = self.step_label("一般化")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("今やったことは、箱に物を入れるとき、最悪を先に詰める考え方でした。", font_size=20)
        self.below_chip(lead, chip, buff=0.18)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        first = [
            self._line(MathTex(r"n", font_size=24, color=YELLOW), "を箱の個数、", MathTex(r"m", font_size=24, color=ORANGE), "を物の個数とおく。", font_size=18),
            self._line(MathTex(r"r", font_size=24, color=TEAL), "を、どれかの箱に集めたい個数の下限とおく。", font_size=18),
            self.ja_text("鳩の巣原理と呼ばれます。箱を巣、物を鳩と見ます。", font_size=20),
            self._line(
                "どの箱も高々",
                MathTex(r"r-1", font_size=24),
                "個なら、全体は高々",
                MathTex(r"n(r-1)", font_size=26),
                "個。",
                font_size=20,
            ),
            MathTex(r"m=n(r-1)+1", font_size=36, color=YELLOW),
            self._line("このとき、どれかの箱に", MathTex(r"r", font_size=24, color=TEAL), "個以上。", font_size=20),
        ]
        block = self._formula_rows(first, lead, buff=0.12)
        self.linger(3.4)
        self.play(FadeOut(VGroup(lead, block)), run_time=0.3)

        name = self.ja_text("切り上げ", font_size=22, color=GREY_B)
        self.below_chip(name, chip, buff=0.18)
        self.play(FadeIn(name), run_time=0.35)
        self.linger(name.text)

        ceil_rows = [
            self._line(
                MathTex(r"m", font_size=24, color=ORANGE),
                "を",
                MathTex(r"n", font_size=24, color=YELLOW),
                "で割った商を、余りがあれば 1 つ上げた整数を、",
                MathTex(r"\lceil m/n \rceil", font_size=28),
                "とおく。",
                font_size=18,
            ),
            self.ja_text("いちばん多い箱の個数は、少なくともこの整数です。", font_size=20),
            MathTex(r"\dfrac{n+1}{n}=1+\dfrac{1}{n}", font_size=30),
            MathTex(r"0<\dfrac{1}{n}\le 1", font_size=28),
            MathTex(r"\left\lceil\dfrac{n+1}{n}\right\rceil=2", font_size=32, color=YELLOW),
            MathTex(r"n=12:\quad \left\lceil\dfrac{13}{12}\right\rceil=2", font_size=30, color=GREEN),
        ]
        block2 = self._formula_rows(ceil_rows, name, buff=0.10)
        self.linger(3.4)
        self.play(FadeOut(block2), run_time=0.3)

        close = [
            self.ja_text("平均が 1 を少し超える、の正体は、切り上げると 2 になることです。", font_size=20),
            self.ja_text("保証は、起こりやすさではなく、切り上げた整数で決まります。", font_size=20),
            self.ja_text("箱は有限個。1 つの物は、どれか 1 つの箱に入ります。", font_size=18, color=GREY_B),
        ]
        shown = VGroup()
        for i, mob in enumerate(close):
            if i == 0:
                self.stack_below(mob, name, buff=0.16)
            else:
                self.stack_below(mob, shown, buff=0.10)
            mob.set_x(0)
            self._fit(mob, 13.0)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.4)
            shown.add(mob)
            self.linger(3.2)

    def part_summary(self):
        self.wipe(self.header)
        chip = self.step_label("まとめ")
        self.play(FadeIn(chip), run_time=0.35)

        rows = [
            self.ja_text("12 人なら、全員違う星座がありうる", font_size=22),
            self.ja_text("13 人目は、空の星座がなく、どれかが 2 人になる", font_size=22),
            self.ja_text("最悪を先に詰めてから 1 人足す", font_size=22),
            self._line(
                MathTex(r"n", font_size=24, color=YELLOW),
                "個の箱に",
                MathTex(r"n(r-1)+1", font_size=26, color=YELLOW),
                "個入れると、どれかは",
                MathTex(r"r", font_size=24, color=TEAL),
                "個以上",
                font_size=20,
            ),
            self._line(
                "いちばん多い箱は少なくとも",
                MathTex(r"\lceil m/n \rceil", font_size=26, color=YELLOW),
                "個",
                font_size=20,
            ),
        ]
        shown = VGroup()
        for i, mob in enumerate(rows):
            if i == 0:
                self.below_chip(mob, chip, buff=0.28)
            else:
                self.stack_below(mob, shown, buff=0.16)
            self._fit_left(mob)
            self.play(FadeIn(mob), run_time=0.45)
            shown.add(mob)
            self.linger(3.2)

        trivia = self._line(
            "うるう年を入れて、箱を",
            MathTex(r"366", font_size=20, color=GREY_B),
            "日とおくと、",
            MathTex(r"367", font_size=20, color=GREY_B),
            "人いれば同じ誕生日の 2 人が必ずいる。",
            font_size=18,
            color=GREY_B,
        )
        self.stack_below(trivia, shown, buff=0.24)
        self._fit_left(trivia)
        self.play(FadeIn(trivia), run_time=0.45)
        self.linger(
            "うるう年を入れて、箱を 366 日とおくと、367 人いれば同じ誕生日の 2 人が必ずいる。",
            extra=0.40,
        )

    def _bins(self, counts, highlight=None, cols=4, box_w=0.78, box_h=0.78):
        cells = []
        n = len(counts)
        rows = (n + cols - 1) // cols
        for i, c in enumerate(counts):
            stroke = YELLOW if highlight == i else GREY_B
            width = 3.2 if highlight == i else 1.6
            rect = RoundedRectangle(
                width=box_w,
                height=box_h,
                corner_radius=0.08,
                color=stroke,
                stroke_width=width,
            )
            dots = VGroup()
            for j in range(c):
                dots.add(Dot(radius=0.08, color=self.DOT_COLORS[j % len(self.DOT_COLORS)]))
            if c:
                dots.arrange(DOWN, buff=0.05)
                dots.move_to(rect.get_center())
            lab = MathTex(rf"{i + 1}", font_size=14, color=GREY_B)
            lab.next_to(rect, DOWN, buff=0.03)
            cells.append(VGroup(rect, dots, lab))
        grid = VGroup(*cells).arrange_in_grid(rows=rows, cols=cols, buff=0.12)
        return grid

    def _sock_bins(self, counts, colors, names, highlight=None, box_w=1.35, box_h=1.55):
        cells = []
        for i, c in enumerate(counts):
            stroke = YELLOW if highlight == i else colors[i]
            rect = RoundedRectangle(
                width=box_w,
                height=box_h,
                corner_radius=0.10,
                color=stroke,
                stroke_width=3.0 if highlight == i else 2.0,
            )
            rect.set_fill(colors[i], 0.18)
            dots = VGroup()
            for j in range(c):
                dots.add(Dot(radius=0.11, color=WHITE))
            if c:
                dots.arrange(DOWN, buff=0.08)
                dots.move_to(rect.get_center())
            lab = self.ja_text(names[i], font_size=18, color=colors[i])
            lab.next_to(rect, DOWN, buff=0.08)
            cells.append(VGroup(rect, dots, lab))
        return VGroup(*cells).arrange(RIGHT, buff=0.28)

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
        block = VGroup(*rows).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
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
