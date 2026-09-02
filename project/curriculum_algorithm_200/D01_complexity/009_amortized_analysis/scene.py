from pathlib import Path
import sys

_D01 = Path(__file__).resolve().parent.parent
if str(_D01) not in sys.path:
    sys.path.insert(0, str(_D01))

from manim import *
from curriculum_scene import CurriculumScene


class AmortizedAnalysis(CurriculumScene):
    """#9 償却解析の考え方（約9分）"""

    header_text = "#9  償却解析の考え方"

    def construct(self):
        self.header = self._open_header()
        self.hook()
        self._show_goals(
            [
                "いちばん高い1回ではなく、連続した操作の合計で見る。",
                "合計を回数で割ったものが、1回あたりの償却コスト。",
                "たまに高いコピーがあっても、償却は定数になりうる。",
            ]
        )
        self._show_overview(
            [
                "STEP 1 … 満杯になると、容量を2倍にしてコピーする",
                "STEP 2 … コピー回数を、倍々で足す",
                "STEP 3 … 合計を追加回数で割る",
                "STEP 4 … 最悪の1回と、償却は別物",
            ],
            ["最後に、空から8回追加して、コピーと書き込みを最初から最後まで通す。"],
        )
        self.step1_double()
        self.step2_sum()
        self.step3_divide()
        self.step4_vs_worst()
        self.worked_example()
        self.summary()
        self.next_preview()

    def _slot_row(self, values, cap, fill=BLUE):
        row = VGroup()
        for i in range(cap):
            sq = Square(side_length=0.62, color=GREY_B, stroke_width=2)
            if i < len(values):
                lab = MathTex(str(values[i]), font_size=26)
                cell = VGroup(sq, lab)
            else:
                cell = sq
            row.add(cell)
        row.arrange(RIGHT, buff=0.1)
        cap_lab = self._mix(self.ja_text("容量", font_size=18, color=GREY_B), MathTex(str(cap), font_size=22, color=GREY_B))
        cap_lab.next_to(row, UP, buff=0.12)
        cap_lab.align_to(row, LEFT)
        return VGroup(cap_lab, row)

    def hook(self):
        q = self.ja_text("いちばん高い1回だけ見ると、高く見えることがある。", font_size=28)
        q.next_to(self.header, DOWN, buff=0.36)
        self.play(FadeIn(q), run_time=0.55)
        self.wait(1.3)
        src = self._boxes([3, 1, 7, 2], side=0.62, font_size=24)
        src.next_to(q, DOWN, buff=0.28)
        src.set_x(0)
        full = self.ja_text("容量 4。満杯。", font_size=22, color=GREY_B)
        full.next_to(src, DOWN, buff=0.16)
        self.play(FadeIn(src), FadeIn(full), run_time=0.5)
        self.wait(1.0)
        left = self._boxes([3, 1, 7, 2, 9], side=0.5, font_size=20)
        empty = VGroup(
            *[Square(side_length=0.5, color=GREY_B, stroke_width=2) for _ in range(3)]
        ).arrange(RIGHT, buff=0.16)
        nxt = VGroup(left, empty).arrange(RIGHT, buff=0.16)
        nxt.next_to(full, DOWN, buff=0.28)
        nxt.set_x(0)
        copy_note = self.ja_text("4個をコピーしてから、9 を置く。", font_size=22, color=ORANGE)
        copy_note.next_to(nxt, DOWN, buff=0.16)
        self.play(FadeIn(nxt), FadeIn(copy_note), run_time=0.55)
        self.wait(1.2)
        cap = self._caption(
            "コピーは満杯のときだけ。毎回4回コピーするわけではない。",
            "今回は、連続した追加で数え直す。",
        )
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.7)
        self._clear(VGroup(q, src, full, nxt, copy_note, cap))

    def step1_double(self):
        chip = self._chip("STEP 1  倍増")
        lead = self.ja_text("配列の追加は、空きがあれば1回書くだけ。満杯なら、先に全部コピーする。", font_size=22)
        self.below_chip(lead, chip)
        self.play(FadeIn(lead), run_time=0.4)
        self.wait(1.2)
        r1 = self._slot_row([1], 1)
        self.stack_below(r1, lead, buff=0.22)
        self.play(FadeIn(r1), run_time=0.4)
        self.wait(0.85)
        r2 = self._slot_row([1, 2], 2)
        self.stack_below(r2, r1, buff=0.18)
        self.play(FadeIn(r2), run_time=0.4)
        self.wait(0.85)
        r3 = self._slot_row([1, 2, 3], 4)
        self.stack_below(r3, r2, buff=0.18)
        self.play(FadeIn(r3), run_time=0.4)
        self.wait(1.0)
        rule_a = self.ja_text("空きがある: 書く仕事は 1。", font_size=22)
        rule_a.next_to(r1, RIGHT, buff=0.5)
        rule_a.align_to(r1, UP)
        self.play(FadeIn(rule_a), run_time=0.35)
        self.wait(1.05)
        rule_b = self.ja_text("満杯: いま入っている個数をコピーしてから、1 を書く。", font_size=22)
        self.stack_below(rule_b, rule_a, buff=0.2)
        self.play(FadeIn(rule_b), run_time=0.35)
        self.wait(1.05)
        definition = self.ja_text("倍増配列では、満杯の追加だけがコピーを伴う。空きがある追加は書くだけ。", font_size=20, color=YELLOW)
        definition.to_edge(DOWN, buff=0.22)
        self.play(FadeIn(definition), run_time=0.45)
        self.linger(3.4)
        cap = self._caption("高い操作はある。次は、それが何回起きるかを足す。")
        self.play(FadeOut(definition), FadeIn(cap), run_time=0.4)
        self.wait(1.5)
        self.wipe(self.header)

    def step2_sum(self):
        chip = self._chip("STEP 2  合計")
        lead = self.ja_text("n 回追加するあいだに、コピーが起きる大きさは 1, 2, 4, … と倍になる。", font_size=22)
        self.below_chip(lead, chip)
        self.play(FadeIn(lead), run_time=0.4)
        self.wait(1.2)
        self.play(FadeOut(lead), run_time=0.3)
        rows = self._formula_rows(
            [
                self.ja_text("n=8 のコピーは、1 と 2 と 4。", font_size=24),
                MathTex(r"1+2+4=7", font_size=32),
                MathTex(r"1+2+4+\cdots+n/2", font_size=30),
                MathTex(r"1+2+\cdots+2^{k-1}=2^{k}-1", font_size=28),
                self._mix(MathTex(r"2^{k}=n", font_size=28), self.ja_text(" なら、コピー合計は", font_size=22), MathTex(r"n-1", font_size=28)),
                self._mix(self.ja_text("書き込みは毎回 1。", font_size=22), MathTex(r"n", font_size=28), self.ja_text(" 回。", font_size=22)),
                MathTex(r"(n-1)+n=2n-1", font_size=32, color=YELLOW),
            ],
            chip,
            buff=0.2,
        )
        definition = self._line(
            "n 回追加の仕事の合計は ",
            MathTex(r"2n-1", font_size=26, color=YELLOW),
            "。コピーの合計は n より小さい。",
            font_size=22,
            color=YELLOW,
        )
        definition.to_edge(DOWN, buff=0.2)
        self.play(FadeIn(definition), run_time=0.45)
        self.linger(3.4)
        cap = self._caption("いちばん高い1回は n に比例しうる。合計はそれでも 2n くらい。")
        self.play(FadeOut(definition), FadeIn(cap), run_time=0.4)
        self.wait(1.5)
        self.wipe(self.header)

    def step3_divide(self):
        chip = self._chip("STEP 3  割る")
        lead = self.ja_text("1回あたりに均すには、合計を回数で割る。", font_size=26)
        self.below_chip(lead, chip)
        self.play(FadeIn(lead), run_time=0.4)
        self.wait(1.2)
        rows = self._formula_rows(
            [
                MathTex(r"2n-1", font_size=32),
                MathTex(r"n", font_size=32),
                MathTex(r"(2n-1)/n=2-1/n", font_size=32, color=YELLOW),
                MathTex(r"n=8:\ 15/8=1.875", font_size=30),
                self.ja_text("n が大きくても 2 より小さい。", font_size=22),
                self._mix(self.ja_text("1回あたりの型は", font_size=24), MathTex(r"O(1)", font_size=34, color=YELLOW), self.ja_text("。", font_size=24)),
            ],
            lead,
            buff=0.22,
        )
        definition = self.ja_text("償却コストは、連続した操作の合計を、回数で割った1回あたりの量。", font_size=22, color=YELLOW)
        definition.to_edge(DOWN, buff=0.22)
        self.play(FadeIn(definition), run_time=0.45)
        self.linger(3.5)
        cap = self._caption("たまにコピーが来ても、均すと定数に収まる。これを償却という。")
        self.play(FadeOut(definition), FadeIn(cap), run_time=0.4)
        self.wait(1.5)
        self.wipe(self.header)

    def step4_vs_worst(self):
        chip = self._chip("STEP 4  別物")
        lead = self.ja_text("保証の書き方を混ぜない。", font_size=26)
        self.below_chip(lead, chip)
        self.play(FadeIn(lead), run_time=0.4)
        self.wait(1.1)
        table = self.aligned_table(
            [
                [
                    self.ja_text("見方", font_size=20, color=GREY_B),
                    self.ja_text("この倍増配列", font_size=20, color=GREY_B),
                    self.ja_text("意味", font_size=20, color=GREY_B),
                ],
                [
                    self.ja_text("最悪の1回", font_size=20, color=RED),
                    MathTex(r"O(n)", font_size=26, color=RED),
                    self.ja_text("満杯のコピー", font_size=20),
                ],
                [
                    self.ja_text("償却（n回）", font_size=20, color=YELLOW),
                    MathTex(r"O(1)", font_size=26, color=YELLOW),
                    self.ja_text("合計を割った値", font_size=20),
                ],
                [
                    self.ja_text("平均（確率）", font_size=20, color=ORANGE),
                    self.ja_text("別の話", font_size=20),
                    self.ja_text("どの入力が来るか", font_size=20),
                ],
            ],
            h_buff=0.4,
            v_buff=0.18,
        )
        table.scale(0.85)
        self.stack_below(table, lead, buff=0.24)
        table.set_x(0)
        self.reveal_table(table, row_wait=0.9)
        note = self.ja_text("#4 の平均は入力の確率。償却は、同じ構造に操作を続けたときの話。", font_size=20)
        note.next_to(table, DOWN, buff=0.18)
        note.set_x(0)
        self.play(FadeIn(note), run_time=0.35)
        self.wait(1.3)
        definition = self.ja_text("償却は「連続した操作の合計の1回あたり」。最悪の1回の代わりではない。", font_size=20, color=YELLOW)
        definition.to_edge(DOWN, buff=0.2)
        self.play(FadeIn(definition), run_time=0.45)
        self.linger(3.4)
        cap = self._caption("1回の保証が要るなら最悪。続けて使うなら償却。目的で使い分ける。")
        self.play(FadeOut(definition), FadeIn(cap), run_time=0.4)
        self.wait(1.6)
        self.wipe(self.header)

    def worked_example(self):
        chip = self._chip("実例  8回")
        lead = self.ja_text("空の容量1から、1 から 8 まで順に足す。", font_size=24)
        self.below_chip(lead, chip)
        self.play(FadeIn(lead), run_time=0.4)
        self.wait(1.0)
        table = self.aligned_table(
            [
                [
                    self.ja_text("回", font_size=18, color=GREY_B),
                    self.ja_text("コピー", font_size=18, color=GREY_B),
                    self.ja_text("仕事", font_size=18, color=GREY_B),
                ],
                [MathTex(r"1", font_size=22), MathTex(r"0", font_size=22), MathTex(r"1", font_size=22)],
                [MathTex(r"2", font_size=22), MathTex(r"1", font_size=22), MathTex(r"2", font_size=22)],
                [MathTex(r"3", font_size=22), MathTex(r"2", font_size=22), MathTex(r"3", font_size=22)],
                [MathTex(r"4", font_size=22), MathTex(r"0", font_size=22), MathTex(r"1", font_size=22)],
                [MathTex(r"5", font_size=22), MathTex(r"4", font_size=22, color=ORANGE), MathTex(r"5", font_size=22, color=ORANGE)],
                [MathTex(r"6", font_size=22), MathTex(r"0", font_size=22), MathTex(r"1", font_size=22)],
                [MathTex(r"7", font_size=22), MathTex(r"0", font_size=22), MathTex(r"1", font_size=22)],
                [MathTex(r"8", font_size=22), MathTex(r"0", font_size=22), MathTex(r"1", font_size=22)],
                [self.ja_text("計", font_size=20), MathTex(r"7", font_size=22), MathTex(r"15", font_size=22, color=YELLOW)],
            ],
            h_buff=0.45,
            v_buff=0.1,
        )
        table.scale(0.72)
        self.stack_below(table, lead, buff=0.18)
        table.set_x(0)
        self.reveal_table(table, row_wait=0.55)
        check = VGroup(
            MathTex(r"2\cdot 8-1=15", font_size=26),
            MathTex(r"15/8=1.875", font_size=26),
            self._mix(self.ja_text("型は", font_size=22), MathTex(r"O(1)", font_size=28, color=YELLOW)),
        ).arrange(RIGHT, buff=0.4)
        check.next_to(table, DOWN, buff=0.16)
        check.set_x(0)
        self.play(FadeIn(check), run_time=0.4)
        self.wait(1.4)
        cap = self._caption("5回目だけ仕事が5。それでも8回の平均は2未満。合計で見ると定数。")
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.7)
        self.wipe(self.header)

    def summary(self):
        chip = self._chip("まとめ")
        items = VGroup(
            self.ja_text("1. 満杯の追加だけがコピーする。空きなら書くだけ。", font_size=24),
            self._line("2. コピー合計は ", MathTex(r"n-1", font_size=28), "。全部で ", MathTex(r"2n-1", font_size=28), "。", font_size=24),
            self._line("3. 割ると ", MathTex(r"O(1)", font_size=28, color=YELLOW), "。これが償却。最悪の1回とは別。", font_size=24),
        ).arrange(DOWN, buff=0.32, aligned_edge=LEFT)
        self.below_chip(items, chip, buff=0.45)
        for row in items:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.35)
        cap = self._caption("高い1回があっても、起き方がまばらなら、均すと小さくなりうる。")
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.6)
        self.wipe(self.header)

    def next_preview(self):
        chip = self._chip("次回")
        nxt = self.ja_text("#10 P と NP の入門", font_size=32, color=YELLOW)
        self.below_chip(nxt, chip, buff=0.5)
        self.play(FadeIn(nxt), run_time=0.45)
        self.wait(1.15)
        body = VGroup(
            self.ja_text("今回は、操作を続けたときの1回あたりを見た。", font_size=26),
            self.ja_text("次回は、答えを探す速さと、答えを確認する速さの", font_size=26),
            self.ja_text("違いから、P と NP に入る。", font_size=26),
        ).arrange(DOWN, buff=0.26, aligned_edge=LEFT)
        self.stack_below(body, nxt, buff=0.4)
        for row in body:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.15)
        self.wait(1.3)
