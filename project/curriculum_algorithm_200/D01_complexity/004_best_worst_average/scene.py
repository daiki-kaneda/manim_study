from pathlib import Path
import sys

_D01 = Path(__file__).resolve().parent.parent
if str(_D01) not in sys.path:
    sys.path.insert(0, str(_D01))

from manim import *
from curriculum_scene import CurriculumScene


VALUES = [3, 1, 7, 2]


class BestWorstAverage(CurriculumScene):
    """#4 最良・最悪・平均計算量（約9分）"""

    header_text = "#4  最良・最悪・平均計算量"

    def construct(self):
        self.header = self._open_header()
        self.hook()
        self._show_goals(
            [
                "最良は、いちばん回数が少ない入力での増え方。",
                "最悪は、いちばん回数が多い入力での増え方。",
                "平均は、入力が同じ確率で来るときの増え方。",
            ]
        )
        self._show_overview(
            [
                "STEP 1 … いちばん速い入力を、最良と呼ぶ",
                "STEP 2 … いちばん遅い入力を、最悪と呼ぶ",
                "STEP 3 … 位置が同じ確率なら、回数の平均を式にする",
                "STEP 4 … よく書くのは最悪。外れにくいから",
            ],
            [
                "最後に、同じ配列で線形探索を、",
                "最良・最悪・平均の3通り、最初から最後まで通す。",
            ],
        )
        self.step1_best()
        self.step2_worst()
        self.step3_avg()
        self.step4_why_worst()
        self.worked_example()
        self.summary()
        self.next_preview()

    def _search(self, boxes, values, target, stop_on_hit=True):
        last = None
        count = 0
        for i, value in enumerate(values):
            count += 1
            self.play(Indicate(boxes[i], color=YELLOW), run_time=0.4)
            same = value == target
            cmp_tex = MathTex(
                rf"{value}={target}" if same else rf"{value}\neq {target}",
                font_size=28,
            )
            ja = self.ja_text("同じ。止まる。" if same else "違う。", font_size=22)
            row = self._mix(cmp_tex, ja, buff=0.12)
            row.next_to(boxes, DOWN, buff=0.85)
            row.set_x(0)
            anims = [FadeIn(row)]
            if last is not None:
                anims.append(FadeOut(last))
            self.play(*anims, run_time=0.35)
            self.wait(0.75)
            last = row
            if same and stop_on_hit:
                break
        return count, last

    def hook(self):
        q = self.ja_text("同じ手順でも、入力によって回数が全然違うことがある。", font_size=28)
        q.next_to(self.header, DOWN, buff=0.38)
        self.play(FadeIn(q), run_time=0.55)
        self.wait(1.3)
        src = self._boxes(VALUES)
        src.next_to(q, DOWN, buff=0.28)
        src.set_x(0)
        note = self.ja_text("手順はどれも、左から順に探す。", font_size=22, color=GREY_B)
        note.next_to(src, DOWN, buff=0.16)
        self.play(FadeIn(src), FadeIn(note), run_time=0.5)
        self.wait(1.0)

        cards = VGroup(
            self._card("x = 3", "いちばん左", "比較 1 回", GREEN, width=3.7, height=1.9),
            self._card("x = 7", "3番目", "比較 3 回", ORANGE, width=3.7, height=1.9),
            self._card("x = 9", "配列にない", "比較 4 回", RED, width=3.7, height=1.9),
        ).arrange(RIGHT, buff=0.28)
        cards.next_to(note, DOWN, buff=0.28)
        cards.set_x(0)
        self.play(LaggedStart(*[FadeIn(c) for c in cards], lag_ratio=0.15), run_time=1.0)
        self.wait(1.4)
        cap = self._caption("手順は同じなのに、回数は 1 回、3 回、4 回。今回はこの違いをどう数えるかをやる。")
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.7)
        self._clear(VGroup(q, src, note, cards, cap))

    def step1_best(self):
        chip = self._chip("STEP 1  最良")
        lead = self.ja_text("いちばん運がいい入力では、最初の箱で見つかる。", font_size=26)
        self.below_chip(lead, chip)
        self.play(FadeIn(lead), run_time=0.4)
        self.wait(1.15)
        src = self._boxes(VALUES)
        src.next_to(lead, DOWN, buff=0.32)
        src.set_x(0)
        xlbl = self.ja_text("探す値 x = 3", font_size=22, color=GREEN)
        xlbl.next_to(src, DOWN, buff=0.16)
        self.play(FadeIn(src), FadeIn(xlbl), run_time=0.45)
        count, last = self._search(src, VALUES, 3)
        got = self.ja_text(f"比較は {count} 回。n が 1000 でも、先頭なら 1 回。", font_size=22)
        got.to_edge(DOWN, buff=0.22)
        self.play(FadeIn(got), run_time=0.35)
        self.wait(1.3)
        self.play(FadeOut(VGroup(lead, src, xlbl, last, got)), run_time=0.3)
        rows = self._formula_rows(
            [
                self._mix(self.ja_text("最良の回数を", font_size=26), MathTex(r"T_{\mathrm{best}}(n)", font_size=32), self.ja_text("と書く。", font_size=26)),
                self._mix(self.ja_text("今の手順では", font_size=26), MathTex(r"T_{\mathrm{best}}(n)=1", font_size=32), self.ja_text("。", font_size=26)),
                self._mix(self.ja_text("増え方の型は", font_size=26), MathTex(r"O(1)", font_size=34, color=GREEN), self.ja_text("。", font_size=26)),
            ],
            chip,
        )
        definition = self.ja_text("最良計算量は、いちばん回数が少ない入力に対する T(n) の増え方。", font_size=24, color=YELLOW)
        definition.next_to(rows, DOWN, buff=0.35)
        definition.set_x(0)
        self.play(FadeIn(definition), run_time=0.45)
        self.linger(3.4)
        cap = self._caption("「うまくいけばこれだけ」が最良。n が増えても、先頭なら増えない。")
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.5)
        self.wipe(self.header)

    def step2_worst(self):
        chip = self._chip("STEP 2  最悪")
        lead = self.ja_text("いちばん運が悪い入力では、最後まで見ても見つからない。", font_size=26)
        self.below_chip(lead, chip)
        self.play(FadeIn(lead), run_time=0.4)
        self.wait(1.15)
        src = self._boxes(VALUES)
        src.next_to(lead, DOWN, buff=0.3)
        src.set_x(0)
        xlbl = self.ja_text("探す値 x = 9（配列にない）", font_size=22, color=RED)
        xlbl.next_to(src, DOWN, buff=0.14)
        self.play(FadeIn(src), FadeIn(xlbl), run_time=0.45)
        count, last = self._search(src, VALUES, 9, stop_on_hit=False)
        none = self.ja_text("もう箱がない。なし。", font_size=22)
        none.next_to(last, DOWN, buff=0.16)
        self.play(FadeIn(none), run_time=0.3)
        self.wait(1.0)
        got = self.ja_text(f"n=4 なら {count} 回。一般には n 回。", font_size=22)
        got.to_edge(DOWN, buff=0.2)
        self.play(FadeIn(got), run_time=0.35)
        self.wait(1.2)
        self.play(FadeOut(VGroup(lead, src, xlbl, last, none, got)), run_time=0.3)
        rows = self._formula_rows(
            [
                self._mix(self.ja_text("最悪の回数を", font_size=26), MathTex(r"T_{\mathrm{worst}}(n)", font_size=32), self.ja_text("と書く。", font_size=26)),
                self._mix(self.ja_text("今の手順では", font_size=26), MathTex(r"T_{\mathrm{worst}}(n)=n", font_size=32), self.ja_text("。", font_size=26)),
                self._mix(self.ja_text("増え方の型は", font_size=26), MathTex(r"O(n)", font_size=34, color=RED), self.ja_text("。", font_size=26)),
            ],
            chip,
        )
        definition = self.ja_text("最悪計算量は、いちばん回数が多い入力に対する T(n) の増え方。", font_size=24, color=YELLOW)
        definition.next_to(rows, DOWN, buff=0.35)
        definition.set_x(0)
        self.play(FadeIn(definition), run_time=0.45)
        self.linger(3.4)
        cap = self._caption("「どれだけ遅くなりうるか」が最悪。保証を書くときは、こっちを見る。")
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.5)
        self.wipe(self.header)

    def step3_avg(self):
        chip = self._chip("STEP 3  平均")
        lead = self.ja_text("見つかる値だけを考える。どれの位置も同じ確率とする。", font_size=24)
        self.below_chip(lead, chip)
        self.play(FadeIn(lead), run_time=0.4)
        self.wait(1.2)
        table = self.aligned_table(
            [
                [
                    self.ja_text("位置", font_size=20, color=GREY_B),
                    self.ja_text("探す値", font_size=20, color=GREY_B),
                    self.ja_text("比較回数", font_size=20, color=GREY_B),
                ],
                [MathTex(r"1", font_size=28), MathTex(r"3", font_size=28), MathTex(r"1", font_size=28)],
                [MathTex(r"2", font_size=28), MathTex(r"1", font_size=28), MathTex(r"2", font_size=28)],
                [MathTex(r"3", font_size=28), MathTex(r"7", font_size=28), MathTex(r"3", font_size=28)],
                [MathTex(r"4", font_size=28), MathTex(r"2", font_size=28), MathTex(r"4", font_size=28)],
            ],
            h_buff=0.5,
            v_buff=0.18,
        )
        table.scale(0.88)
        table.next_to(lead, DOWN, buff=0.28)
        table.set_x(0)
        self.reveal_table(table, row_wait=0.85)
        avg_ja = self.ja_text("4通りが同じ確率なら、平均は足して 4 で割る。", font_size=22)
        avg_ja.next_to(table, DOWN, buff=0.22)
        self.play(FadeIn(avg_ja), run_time=0.35)
        self.wait(1.15)
        self.play(FadeOut(VGroup(lead, table, avg_ja)), run_time=0.3)
        rows = self._formula_rows(
            [
                MathTex(r"1+2+3+4=10", font_size=32),
                MathTex(r"10/4=2.5", font_size=32),
                MathTex(r"1+2+\cdots+n=\dfrac{n(n+1)}{2}", font_size=30),
                MathTex(r"T_{\mathrm{avg}}(n)=\dfrac{n(n+1)}{2}\cdot\dfrac{1}{n}=\dfrac{n+1}{2}", font_size=28),
                MathTex(r"n=4:\quad \dfrac{4+1}{2}=2.5", font_size=30),
                self._mix(self.ja_text("増え方の型は", font_size=24), MathTex(r"O(n)", font_size=32, color=ORANGE), self.ja_text("。", font_size=24)),
            ],
            chip,
            buff=0.32,
        )
        definition = self.ja_text("平均計算量は、入力が同じ確率で来るときの T(n) の期待値の増え方。", font_size=22, color=YELLOW)
        definition.next_to(rows, DOWN, buff=0.28)
        definition.set_x(0)
        self.play(FadeIn(definition), run_time=0.45)
        self.linger(3.4)
        cap = self._caption("見つからない場合を入れると平均はもっと n に近づく。今回は「見つかる」だけ。")
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.5)
        self.wipe(self.header)

    def step4_why_worst(self):
        chip = self._chip("STEP 4  なぜ最悪か")
        points = VGroup(
            self.ja_text("1. 最良は運がよすぎる。先頭にある保証はない。", font_size=24),
            self.ja_text("2. 平均は、確率の仮定が要る。偏るとずれる。", font_size=24),
            self.ja_text("3. 最悪は、「これ以上は遅くならない」という保証になる。", font_size=24),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        self.below_chip(points, chip, buff=0.4)
        for p in points:
            self.play(FadeIn(p), run_time=0.4)
            self.wait(1.2)
        trade = self.ja_text("よくビッグOで書くのは、最悪の増え方。外れにくいから。", font_size=24, color=YELLOW)
        trade.next_to(points, DOWN, buff=0.35)
        trade.set_x(0)
        self.play(FadeIn(trade), run_time=0.45)
        self.linger(3.3)
        self.play(FadeOut(points), FadeOut(trade), run_time=0.3)
        table = self.aligned_table(
            [
                [
                    self.ja_text("種類", font_size=20, color=GREY_B),
                    self.ja_text("この線形探索", font_size=20, color=GREY_B),
                    self.ja_text("よく書くか", font_size=20, color=GREY_B),
                ],
                [
                    self.ja_text("最良", font_size=22, color=GREEN),
                    MathTex(r"O(1)", font_size=26, color=GREEN),
                    self.ja_text("あまり書かない", font_size=22),
                ],
                [
                    self.ja_text("平均", font_size=22, color=ORANGE),
                    MathTex(r"O(n)", font_size=26, color=ORANGE),
                    self.ja_text("仮定つきなら書く", font_size=22),
                ],
                [
                    self.ja_text("最悪", font_size=22, color=RED),
                    MathTex(r"O(n)", font_size=26, color=RED),
                    self.ja_text("いちばんよく書く", font_size=22),
                ],
            ],
            h_buff=0.45,
            v_buff=0.2,
        )
        table.scale(0.9)
        self.below_chip(table, chip, buff=0.35)
        table.set_x(0)
        self.reveal_table(table, row_wait=0.95)
        cap = self._caption("平均と最悪が同じ型のこともある。そのときは「だいたい n に比例」と言ってよい。")
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.6)
        self.wipe(self.header)

    def worked_example(self):
        chip = self._chip("実例  3通り通す")
        q = self.ja_text("長さ n の配列を、左から順に探して、値 x があるかを知りたい。", font_size=24)
        self.below_chip(q, chip)
        self.play(FadeIn(q), run_time=0.4)
        self.wait(1.15)
        src = self._boxes(VALUES)
        src.next_to(q, DOWN, buff=0.28)
        src.set_x(0)
        idx = self._index_labels(src)
        self.play(FadeIn(src), FadeIn(idx), run_time=0.4)

        best_t = self.ja_text("最良  x = 3", font_size=22, color=GREEN)
        best_t.next_to(idx, DOWN, buff=0.2)
        self.play(FadeIn(best_t), run_time=0.3)
        count, last = self._search(src, VALUES, 3)
        tb = MathTex(r"T_{\mathrm{best}}(4)=1", font_size=28, color=GREEN)
        tb.next_to(best_t, RIGHT, buff=0.35)
        self.play(FadeIn(tb), run_time=0.3)
        self.wait(1.1)
        self.play(FadeOut(VGroup(best_t, last, tb)), run_time=0.25)

        worst_t = self.ja_text("最悪  x = 9", font_size=22, color=RED)
        worst_t.next_to(idx, DOWN, buff=0.2)
        self.play(FadeIn(worst_t), run_time=0.3)
        count, last = self._search(src, VALUES, 9, stop_on_hit=False)
        tw = MathTex(r"T_{\mathrm{worst}}(4)=4=n", font_size=28, color=RED)
        tw.next_to(worst_t, RIGHT, buff=0.3)
        self.play(FadeIn(tw), run_time=0.3)
        self.wait(1.1)
        self.play(FadeOut(VGroup(q, src, idx, worst_t, last, tw)), run_time=0.3)

        avg_t = self.ja_text("平均（見つかる4通り）", font_size=24, color=ORANGE)
        self.below_chip(avg_t, chip, buff=0.35)
        self.play(FadeIn(avg_t), run_time=0.3)
        formulas = VGroup(
            MathTex(r"\dfrac{1+2+3+4}{4}=\dfrac{10}{4}=2.5", font_size=32),
            MathTex(r"=\dfrac{4+1}{2}", font_size=32),
        ).arrange(DOWN, buff=0.2)
        self.stack_below(formulas, avg_t, buff=0.28)
        for row in formulas:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.05)
        self.play(FadeOut(VGroup(avg_t, formulas)), run_time=0.3)

        table = self.aligned_table(
            [
                [
                    self.ja_text(" ", font_size=20),
                    self.ja_text("n=4 の回数", font_size=20, color=GREY_B),
                    self.ja_text("増え方", font_size=20, color=GREY_B),
                ],
                [self.ja_text("最良", font_size=22, color=GREEN), MathTex(r"1", font_size=26), MathTex(r"O(1)", font_size=26, color=GREEN)],
                [self.ja_text("平均", font_size=22, color=ORANGE), MathTex(r"2.5", font_size=26), MathTex(r"O(n)", font_size=26, color=ORANGE)],
                [self.ja_text("最悪", font_size=22, color=RED), MathTex(r"4", font_size=26), MathTex(r"O(n)", font_size=26, color=RED)],
            ],
            h_buff=0.45,
            v_buff=0.2,
        )
        table.scale(0.92)
        self.below_chip(table, chip, buff=0.4)
        table.set_x(0)
        self.reveal_table(table, row_wait=1.0)
        cap = self._caption("同じ手順でも、どの入力で数えるかを先に決める。")
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.6)
        self.wipe(self.header)

    def summary(self):
        chip = self._chip("まとめ")
        items = VGroup(
            self.ja_text("1. 最良はいちばん少ない入力、最悪はいちばん多い入力。", font_size=24),
            self._mix(self.ja_text("2. 平均は同じ確率のときの期待値。この探索では", font_size=24), MathTex(r"\dfrac{n+1}{2}", font_size=28), self.ja_text("。", font_size=24)),
            self.ja_text("3. よく書くのは最悪。保証になるから。", font_size=24),
        ).arrange(DOWN, buff=0.32, aligned_edge=LEFT)
        self.below_chip(items, chip, buff=0.45)
        for row in items:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.35)
        cap = self._caption("「n に対して何回か」の前に、「どの入力の話か」を決める。")
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.6)
        self.wipe(self.header)

    def next_preview(self):
        chip = self._chip("次回")
        nxt = self.ja_text("#5 漸近記法（Ω, Θ）の使い分け", font_size=30, color=YELLOW)
        self.below_chip(nxt, chip, buff=0.5)
        self.play(FadeIn(nxt), run_time=0.45)
        self.wait(1.15)
        body = VGroup(
            self.ja_text("今回は、どの入力で数えるかを分けた。", font_size=26),
            self.ja_text("次回は、上から抑える O だけでなく、", font_size=26),
            self.ja_text("下から抑える Ω と、両方つく Θ を並べる。", font_size=26),
        ).arrange(DOWN, buff=0.26, aligned_edge=LEFT)
        self.stack_below(body, nxt, buff=0.4)
        for row in body:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.15)
        self.wait(1.3)
