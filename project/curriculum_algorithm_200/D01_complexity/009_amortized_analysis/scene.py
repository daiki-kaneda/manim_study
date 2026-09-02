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
                "いちばん高い1回だけではなく、同じ操作を続けたときの合計で仕事を見る。",
                "その合計を回数で割った値が、1回あたりの償却コストです。",
                "たまに高いコピーがあっても、割り算のあとなら定数におさまることがあります。",
            ]
        )
        self._show_overview(
            [
                "STEP 1 … 配列がいっぱいになると、容量を2倍にして中身をコピーする",
                "STEP 2 … コピーが何回起きるかを、1, 2, 4, … と倍々で足す",
                "STEP 3 … 全部の仕事を、追加した回数で割って1回あたりにする",
                "STEP 4 … 最悪の1回の保証と、償却の1回あたりは別の見方",
            ],
            ["最後に、空の配列へ8回追加して、コピーと書き込みを最初から最後まで通します。"],
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
        q = VGroup(
            self.ja_text("いちばん高い1回の操作だけを見ると、「この操作は重い」と思えることがあります。", font_size=22),
            self.ja_text("でも、同じ操作を何回も続けると、高い回はまばらです。", font_size=22),
        ).arrange(DOWN, buff=0.12)
        q.next_to(self.header, DOWN, buff=0.28)
        q.set_x(0)
        self.play(FadeIn(q), run_time=0.55)
        self.wait(1.4)
        src = self._boxes([3, 1, 7, 2], side=0.58, font_size=24)
        src.next_to(q, DOWN, buff=0.2)
        src.set_x(0)
        full = self.ja_text("容量 4。満杯です。5個目を足そうとします。", font_size=20, color=GREY_B)
        full.next_to(src, DOWN, buff=0.12)
        self.play(FadeIn(src), FadeIn(full), run_time=0.5)
        self.wait(1.0)
        left = self._boxes([3, 1, 7, 2, 9], side=0.46, font_size=18)
        empty = VGroup(
            *[Square(side_length=0.46, color=GREY_B, stroke_width=2) for _ in range(3)]
        ).arrange(RIGHT, buff=0.12)
        nxt = VGroup(left, empty).arrange(RIGHT, buff=0.12)
        nxt.next_to(full, DOWN, buff=0.2)
        nxt.set_x(0)
        copy_note = self.ja_text("4個を新しい箱へコピーしてから、9 を置きます。この1回だけ見ると仕事は多いです。", font_size=18, color=ORANGE)
        copy_note.next_to(nxt, DOWN, buff=0.12)
        self.play(FadeIn(nxt), FadeIn(copy_note), run_time=0.55)
        self.wait(1.25)
        cap = self._caption(
            "コピーは、箱がいっぱいになったときだけ起きます。毎回4個コピーするわけではありません。",
            "今回は、追加を何回か続けたときの合計から、1回あたりを数え直します。",
        )
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.8)
        self._clear(VGroup(q, src, full, nxt, copy_note, cap))

    def step1_double(self):
        chip = self._chip("STEP 1  倍増")
        lead = VGroup(
            self.ja_text("配列へ1個足すとき、空きがあれば書く仕事は1回だけです。", font_size=20),
            self.ja_text("満杯なら、先に全部を新しい箱へコピーしてから書きます。容量を2倍にするので、倍増と呼びます。", font_size=20),
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        self.below_chip(lead, chip)
        self.play(FadeIn(lead), run_time=0.4)
        self.wait(1.35)
        r1 = self._slot_row([1], 1)
        self.stack_below(r1, lead, buff=0.2)
        self.play(FadeIn(r1), run_time=0.4)
        self.wait(0.9)
        r2 = self._slot_row([1, 2], 2)
        self.stack_below(r2, r1, buff=0.16)
        self.play(FadeIn(r2), run_time=0.4)
        self.wait(0.9)
        r3 = self._slot_row([1, 2, 3], 4)
        self.stack_below(r3, r2, buff=0.16)
        self.play(FadeIn(r3), run_time=0.4)
        self.wait(1.05)
        self.play(FadeOut(VGroup(r1, r2, r3)), run_time=0.3)
        rules = VGroup(
            self.ja_text("空きがあるときは、新しい値を1個書くだけです。仕事は 1 です。", font_size=22),
            self.ja_text("満杯のときは、いま入っている個数をコピーしてから、1 個書きます。", font_size=22),
            self.ja_text("そのときの仕事は、「コピーの個数 + 1」です。", font_size=22),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        self.stack_below(rules, lead, buff=0.28)
        for row in rules:
            self.play(FadeIn(row), run_time=0.35)
            self.wait(1.1)
        definition = self.ja_text(
            "倍増配列では、満杯の追加だけがコピーを伴います。空きがある追加は、書くだけで終わります。",
            font_size=18,
            color=YELLOW,
        )
        definition.to_edge(DOWN, buff=0.2)
        self.play(FadeIn(definition), run_time=0.45)
        self.linger(3.4)
        cap = self._caption("高い操作はあります。次は、そのコピーが何回起きるかを、全部足してみます。")
        self.play(FadeOut(definition), FadeIn(cap), run_time=0.4)
        self.wait(1.6)
        self.wipe(self.header)

    def step2_sum(self):
        chip = self._chip("STEP 2  合計")
        lead = VGroup(
            self.ja_text("n 回追加するあいだに、コピーが起きる大きさは 1, 2, 4, … と倍になります。", font_size=20),
            self.ja_text("満杯になるタイミングが、その間隔で来るからです。", font_size=20),
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        self.below_chip(lead, chip)
        self.play(FadeIn(lead), run_time=0.4)
        self.wait(1.3)
        self.play(FadeOut(lead), run_time=0.3)
        rows = self._formula_rows(
            [
                self.ja_text("n=8 なら、コピーは容量 1, 2, 4 のあとに起きます。", font_size=22),
                MathTex(r"1+2+4=7", font_size=32),
                self._mix(self.ja_text("一般には", font_size=20), MathTex(r"1+2+4+\cdots+n/2", font_size=28)),
                MathTex(r"1+2+\cdots+2^{k-1}=2^{k}-1", font_size=28),
                self._mix(
                    MathTex(r"2^{k}=n", font_size=26),
                    self.ja_text(" なら、コピー合計は", font_size=20),
                    MathTex(r"n-1", font_size=26),
                    self.ja_text("。n より小さいのがポイントです。", font_size=20),
                ),
                self._mix(self.ja_text("書き込みは毎回 1 なので", font_size=20), MathTex(r"n", font_size=26), self.ja_text(" 回。全部で", font_size=20), MathTex(r"(n-1)+n=2n-1", font_size=28, color=YELLOW)),
            ],
            chip,
            buff=0.18,
        )
        definition = VGroup(
            self._line(
                "n 回追加したときの仕事の合計は ",
                MathTex(r"2n-1", font_size=24, color=YELLOW),
                " です。",
                font_size=20,
                color=YELLOW,
            ),
            self.ja_text("いちばん高い1回は n に比例しえますが、コピーの合計は n より小さくなります。", font_size=18, color=YELLOW),
        ).arrange(DOWN, buff=0.08)
        definition.to_edge(DOWN, buff=0.16)
        definition.set_x(0)
        self.play(FadeIn(definition), run_time=0.45)
        self.linger(3.4)
        cap = self._caption("高い1回はあるのに、全部足すと 2n くらいにしかなりません。次は、これを回数で割ります。")
        self.play(FadeOut(definition), FadeIn(cap), run_time=0.4)
        self.wait(1.6)
        self.wipe(self.header)

    def step3_divide(self):
        chip = self._chip("STEP 3  割る")
        lead = VGroup(
            self.ja_text("合計だけだと「全部でどれだけ働いたか」です。", font_size=22),
            self.ja_text("1回の追加あたりに直すには、合計を追加した回数で割ります。この割った値を、償却コストと呼びます。", font_size=20),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        self.below_chip(lead, chip)
        self.play(FadeIn(lead), run_time=0.4)
        self.wait(1.35)
        self.play(FadeOut(lead), run_time=0.3)
        rows = self._formula_rows(
            [
                self._mix(self.ja_text("合計は", font_size=22), MathTex(r"2n-1", font_size=30)),
                self._mix(self.ja_text("割る数は、追加した回数", font_size=22), MathTex(r"n", font_size=30)),
                MathTex(r"(2n-1)/n=2-1/n", font_size=32, color=YELLOW),
                self._mix(MathTex(r"n=8", font_size=26), self.ja_text(" なら", font_size=20), MathTex(r"15/8=1.875", font_size=28), self.ja_text("。2 より小さいです。", font_size=20)),
                self.ja_text("n が大きくなっても、この値は 2 より小さく、2 に近づくだけです。", font_size=20),
                self._mix(
                    self.ja_text("だから1回あたりの型は", font_size=22),
                    MathTex(r"O(1)", font_size=32, color=YELLOW),
                    self.ja_text("。均した1回は定数のままです。", font_size=20),
                ),
            ],
            chip,
            buff=0.18,
        )
        definition = VGroup(
            self.ja_text("償却コストは、連続した操作の合計を、回数で割った1回あたりの量です。", font_size=20, color=YELLOW),
            self.ja_text("たまに来る高いコピーも、この割り算の中に均されます。", font_size=20, color=YELLOW),
        ).arrange(DOWN, buff=0.08)
        definition.to_edge(DOWN, buff=0.16)
        definition.set_x(0)
        self.play(FadeIn(definition), run_time=0.45)
        self.linger(3.5)
        cap = self._caption("たまにコピーが来ても、長い目で割ると定数に収まります。この見方を償却解析と呼びます。")
        self.play(FadeOut(definition), FadeIn(cap), run_time=0.4)
        self.wait(1.6)
        self.wipe(self.header)

    def step4_vs_worst(self):
        chip = self._chip("STEP 4  別物")
        lead = VGroup(
            self.ja_text("「1回あたり」と言っても、見方が3つあります。", font_size=22),
            self.ja_text("いちばん高い1回の保証と、合計を割った償却と、入力の確率で平均する話は、混ぜてはいけません。", font_size=20),
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        self.below_chip(lead, chip)
        self.play(FadeIn(lead), run_time=0.4)
        self.wait(1.25)
        table = self.aligned_table(
            [
                [
                    self.ja_text("見方", font_size=18, color=GREY_B),
                    self.ja_text("この倍増配列", font_size=18, color=GREY_B),
                    self.ja_text("何を保証しているか", font_size=18, color=GREY_B),
                ],
                [
                    self.ja_text("最悪の1回", font_size=20, color=RED),
                    MathTex(r"O(n)", font_size=24, color=RED),
                    self.ja_text("満杯のコピーが来た、その1回", font_size=18),
                ],
                [
                    self.ja_text("償却（n回）", font_size=20, color=YELLOW),
                    MathTex(r"O(1)", font_size=24, color=YELLOW),
                    self.ja_text("n 回続けた合計を、回数で割った値", font_size=18),
                ],
                [
                    self.ja_text("平均（確率）", font_size=20, color=ORANGE),
                    self.ja_text("別の話", font_size=18),
                    self.ja_text("どの入力が来やすいか、という確率", font_size=18),
                ],
            ],
            h_buff=0.32,
            v_buff=0.14,
        )
        table.scale(0.82)
        self.stack_below(table, lead, buff=0.18)
        table.set_x(0)
        self.reveal_table(table, row_wait=0.9)
        note = VGroup(
            self.ja_text("#4 の平均は、「どの入力が同じ確率で来るか」の話です。", font_size=18),
            self.ja_text("今回の償却は、入力をランダムにせず、同じ配列へ操作を続けたときの合計の話です。", font_size=18),
        ).arrange(DOWN, buff=0.08)
        note.next_to(table, DOWN, buff=0.14)
        note.set_x(0)
        self.play(FadeIn(note), run_time=0.35)
        self.wait(1.35)
        definition = VGroup(
            self.ja_text("償却は「連続した操作の合計の1回あたり」です。最悪の1回の代わりにはなりません。", font_size=18, color=YELLOW),
            self.ja_text("1回でも遅くては困るなら、最悪のほうを使います。", font_size=18, color=YELLOW),
        ).arrange(DOWN, buff=0.06)
        definition.to_edge(DOWN, buff=0.14)
        definition.set_x(0)
        self.play(FadeIn(definition), run_time=0.45)
        self.linger(3.4)
        cap = self._caption("1回の遅さが致命的なら最悪。続けて使うときの合計が知りたいなら償却。目的で使い分けます。")
        self.play(FadeOut(definition), FadeIn(cap), run_time=0.4)
        self.wait(1.7)
        self.wipe(self.header)

    def worked_example(self):
        chip = self._chip("実例  8回")
        lead = VGroup(
            self.ja_text("空の容量1から、1 から 8 まで順に足します。", font_size=22),
            self.ja_text("仕事の列は、「コピーした個数 + 新しく書いた 1」です。", font_size=20),
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        self.below_chip(lead, chip)
        self.play(FadeIn(lead), run_time=0.4)
        self.wait(1.1)
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
            v_buff=0.08,
        )
        table.scale(0.68)
        self.stack_below(table, lead, buff=0.14)
        table.set_x(0)
        self.reveal_table(table, row_wait=0.5)
        check = VGroup(
            MathTex(r"2\cdot 8-1=15", font_size=24),
            MathTex(r"15/8=1.875", font_size=24),
            self._mix(self.ja_text("2より小さいので型は", font_size=20), MathTex(r"O(1)", font_size=26, color=YELLOW)),
        ).arrange(RIGHT, buff=0.32)
        check.next_to(table, DOWN, buff=0.12)
        check.set_x(0)
        self.play(FadeIn(check), run_time=0.4)
        self.wait(1.4)
        cap = self._caption(
            "5回目だけ仕事が5で、そこだけ高く見えます。それでも8回の平均は2未満です。",
            "合計で見ると、1回あたりは定数です。",
        )
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.7)
        self.wipe(self.header)

    def summary(self):
        chip = self._chip("まとめ")
        items = VGroup(
            self.ja_text("1. 満杯の追加だけがコピーする。空きがある追加は、書くだけ。", font_size=22),
            self._line("2. コピー合計は ", MathTex(r"n-1", font_size=26), "。書き込みと合わせると全部で ", MathTex(r"2n-1", font_size=26), "。", font_size=20),
            self._line("3. 回数で割ると ", MathTex(r"O(1)", font_size=26, color=YELLOW), "。これが償却。最悪の1回 ", MathTex(r"O(n)", font_size=26), " とは別の見方。", font_size=20),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        self.below_chip(items, chip, buff=0.4)
        for row in items:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.35)
        cap = self._caption("高い1回があっても、起き方がまばらなら、合計を割ると小さく見えることがあります。それが償却です。")
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
            self.ja_text("今回は、操作を続けたときの1回あたりを見ました。", font_size=24),
            self.ja_text("次回は、答えを探す速さと、答えを確認する速さの", font_size=24),
            self.ja_text("違いから、P と NP に入ります。", font_size=24),
        ).arrange(DOWN, buff=0.24, aligned_edge=LEFT)
        self.stack_below(body, nxt, buff=0.36)
        for row in body:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.15)
        self.wait(1.3)
