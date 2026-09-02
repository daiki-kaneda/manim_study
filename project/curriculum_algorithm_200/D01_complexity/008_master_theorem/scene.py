from pathlib import Path
import sys

_D01 = Path(__file__).resolve().parent.parent
if str(_D01) not in sys.path:
    sys.path.insert(0, str(_D01))

from manim import *
from curriculum_scene import CurriculumScene


class MasterTheorem(CurriculumScene):
    """#8 マスター定理（約9分）"""

    header_text = "#8  マスター定理"

    def construct(self):
        self.header = self._open_header()
        self.hook()
        self._show_goals(
            [
                self._line(
                    "対象は ",
                    MathTex(r"T(n)=aT(n/b)+f(n)", font_size=28),
                    " の形。",
                    font_size=26,
                ),
                self._line(
                    "葉の仕事 ",
                    MathTex(r"n^{\log_b a}", font_size=28),
                    " と、自分の仕事 ",
                    MathTex(r"f(n)", font_size=28),
                    " を比べる。",
                    font_size=26,
                ),
                "3つの場合で、答えの型が決まる。",
            ]
        )
        self._show_overview(
            [
                self._line(
                    "STEP 1 … 形から ",
                    MathTex(r"a,\ b,\ f(n)", font_size=24),
                    " を読む",
                    font_size=24,
                ),
                self._line(
                    "STEP 2 … 葉の個数は ",
                    MathTex(r"n^{\log_b a}", font_size=24),
                    font_size=24,
                ),
                "STEP 3 … 小さい・同じ・大きい、の3つ",
                "STEP 4 … 多項式なら指数を比べる",
            ],
            [
                self._line(
                    "最後に、前回の ",
                    MathTex(r"T(n)=2T(n/2)+n", font_size=26),
                    " を、最初から最後まで当てはめる。",
                    font_size=24,
                )
            ],
        )
        self.step1_form()
        self.step2_leaves()
        self.step3_cases()
        self.step4_exponents()
        self.worked_example()
        self.summary()
        self.next_preview()

    def hook(self):
        q = self.ja_text("自分の仕事が変わると、木の足し算の答えも変わる。", font_size=28)
        q.next_to(self.header, DOWN, buff=0.38)
        self.play(FadeIn(q), run_time=0.55)
        self.wait(1.3)
        note = self.ja_text("子は2つ。大きさは半分。違うのは自分の仕事だけ。", font_size=22, color=GREY_B)
        note.next_to(q, DOWN, buff=0.28)
        note.set_x(0)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.1)
        cards = VGroup(
            self._card(
                "自分の仕事 n",
                "前回手で足した",
                MathTex(r"\Theta(n\log n)", font_size=22, color=BLUE),
                BLUE,
                width=5.4,
                height=2.05,
            ),
            self._card(
                "自分の仕事 1",
                "葉のほうが多い",
                self.ja_text("型は変わる", font_size=20, color=ORANGE),
                ORANGE,
                width=5.4,
                height=2.05,
            ),
        ).arrange(RIGHT, buff=0.4)
        cards.next_to(note, DOWN, buff=0.3)
        cards.set_x(0)
        self.play(FadeIn(cards), run_time=0.7)
        self.wait(1.3)
        cap = self._caption("毎回木を全部描き直さなくても、場合分けで型を出したい。今回はその道具をやる。")
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.7)
        self._clear(VGroup(q, note, cards, cap))

    def step1_form(self):
        chip = self._chip("STEP 1  形")
        lead = self.ja_text("マスター定理が使えるのは、だいたいこの形のとき。", font_size=24)
        self.below_chip(lead, chip)
        self.play(FadeIn(lead), run_time=0.4)
        self.wait(1.2)
        rows = self._formula_rows(
            [
                MathTex(r"T(n)=a\,T(n/b)+f(n)", font_size=34, color=YELLOW),
                self._mix(MathTex(r"a", font_size=28), self.ja_text(" は、子の個数。", font_size=24)),
                self._mix(MathTex(r"n/b", font_size=28), self.ja_text(" は、1つの子の大きさ。", font_size=24)),
                self._mix(MathTex(r"f(n)", font_size=28), self.ja_text(" は、自分の段の仕事。", font_size=24)),
            ],
            lead,
            buff=0.28,
        )
        self.play(FadeOut(rows), run_time=0.3)
        fit = VGroup(
            self.ja_text("前回の式に当てはめる。", font_size=22),
            MathTex(r"T(n)=2T(n/2)+n", font_size=32),
            MathTex(r"a=2,\quad b=2,\quad f(n)=n", font_size=30, color=YELLOW),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        self.stack_below(fit, lead, buff=0.3)
        for row in fit:
            self.play(FadeIn(row), run_time=0.35)
            self.wait(1.0)
        definition = self._line(
            "マスター定理の対象は、",
            MathTex(r"T(n)=aT(n/b)+f(n)", font_size=26, color=YELLOW),
            " の形の漸化式。",
            font_size=22,
            color=YELLOW,
        )
        definition.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(definition), run_time=0.45)
        self.linger(3.5)
        cap = self._caption("子の数、半分の仕方、自分の仕事。この3つを先に読む。")
        self.play(FadeOut(definition), FadeIn(cap), run_time=0.4)
        self.wait(1.5)
        self.wipe(self.header)

    def step2_leaves(self):
        chip = self._chip("STEP 2  葉")
        lead = self.ja_text("再帰木のいちばん下は、大きさ 1 の呼び出し。その個数が葉の数。", font_size=24)
        self.below_chip(lead, chip)
        self.play(FadeIn(lead), run_time=0.4)
        self.wait(1.2)
        self.play(FadeOut(lead), run_time=0.3)
        rows = self._formula_rows(
            [
                self._mix(self.ja_text("段0:", font_size=22), MathTex(r"1", font_size=28), self.ja_text(" 個、大きさ", font_size=22), MathTex(r"n", font_size=28)),
                self._mix(self.ja_text("段1:", font_size=22), MathTex(r"a", font_size=28), self.ja_text(" 個、大きさ", font_size=22), MathTex(r"n/b", font_size=28)),
                self._mix(self.ja_text("段", font_size=22), MathTex(r"k", font_size=28), self.ja_text(":", font_size=22), MathTex(r"a^{k}", font_size=28), self.ja_text(" 個、大きさ", font_size=22), MathTex(r"n/b^{k}", font_size=28)),
                self._mix(self.ja_text("葉は", font_size=22), MathTex(r"n/b^{k}=1", font_size=28), self.ja_text("、つまり", font_size=22), MathTex(r"k=\log_b n", font_size=28)),
                MathTex(r"a^{\log_b n}=n^{\log_b a}", font_size=32, color=YELLOW),
            ],
            chip,
            buff=0.22,
        )
        self.play(FadeOut(rows), run_time=0.3)
        plug = VGroup(
            MathTex(r"a=2,\ b=2", font_size=30),
            MathTex(r"\log_2 2=1", font_size=30),
            MathTex(r"n^{1}=n", font_size=32, color=YELLOW),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        self.below_chip(plug, chip, buff=0.35)
        for row in plug:
            self.play(FadeIn(row), run_time=0.35)
            self.wait(1.0)
        definition = self._line(
            "葉の仕事の合計は ",
            MathTex(r"\Theta(n^{\log_b a})", font_size=26, color=YELLOW),
            "。これを ",
            MathTex(r"f(n)", font_size=26, color=YELLOW),
            " と比べる。",
            font_size=22,
            color=YELLOW,
        )
        definition.to_edge(DOWN, buff=0.22)
        self.play(FadeIn(definition), run_time=0.45)
        self.linger(3.5)
        cap = self._caption("木の下の仕事と、根の仕事。どっちが勝つかで場合が分かれる。")
        self.play(FadeOut(definition), FadeIn(cap), run_time=0.4)
        self.wait(1.5)
        self.wipe(self.header)

    def step3_cases(self):
        chip = self._chip("STEP 3  場合")
        lead = self._line(
            MathTex(r"f(n)", font_size=28),
            " が葉より小さいか、同じくらいか、大きいか。",
            font_size=24,
        )
        self.below_chip(lead, chip)
        self.play(FadeIn(lead), run_time=0.4)
        self.wait(1.15)
        table = self.aligned_table(
            [
                [
                    self.ja_text("場合", font_size=20, color=GREY_B),
                    self.ja_text("f と葉", font_size=20, color=GREY_B),
                    self.ja_text("答え", font_size=20, color=GREY_B),
                ],
                [
                    MathTex(r"1", font_size=26, color=GREEN),
                    self.ja_text("葉のほうが大きい", font_size=20),
                    MathTex(r"\Theta(n^{\log_b a})", font_size=24, color=GREEN),
                ],
                [
                    MathTex(r"2", font_size=26, color=YELLOW),
                    self.ja_text("同じくらい", font_size=20),
                    MathTex(r"\Theta(n^{\log_b a}\log n)", font_size=22, color=YELLOW),
                ],
                [
                    MathTex(r"3", font_size=26, color=ORANGE),
                    self._line(MathTex(r"f", font_size=20), " のほうが大きい", font_size=20),
                    MathTex(r"\Theta(f(n))", font_size=24, color=ORANGE),
                ],
            ],
            h_buff=0.38,
            v_buff=0.16,
        )
        table.scale(0.82)
        self.stack_below(table, lead, buff=0.24)
        table.set_x(0)
        self.reveal_table(table, row_wait=0.9)
        note = self.ja_text("場合2は、どの段の合計もだいたい同じなので、段数が掛かる。前回手で足したやつ。", font_size=20)
        note.next_to(table, DOWN, buff=0.2)
        note.set_x(0)
        self.play(FadeIn(note), run_time=0.35)
        self.wait(1.3)
        self.play(FadeOut(VGroup(lead, table, note)), run_time=0.3)
        examples = VGroup(
            self._mix(MathTex(r"T(n)=2T(n/2)+1", font_size=26), self.ja_text("場合1", font_size=22), MathTex(r"\Theta(n)", font_size=26, color=GREEN), buff=0.22),
            self._mix(MathTex(r"T(n)=2T(n/2)+n", font_size=26), self.ja_text("場合2", font_size=22), MathTex(r"\Theta(n\log n)", font_size=26, color=YELLOW), buff=0.22),
            self._mix(MathTex(r"T(n)=2T(n/2)+n^{2}", font_size=26), self.ja_text("場合3", font_size=22), MathTex(r"\Theta(n^{2})", font_size=26, color=ORANGE), buff=0.22),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        self.below_chip(examples, chip, buff=0.4)
        for row in examples:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.15)
        definition = self._line(
            "マスター定理は、葉の仕事と ",
            MathTex(r"f(n)", font_size=24, color=YELLOW),
            " の大小で、",
            MathTex(r"T(n)", font_size=24, color=YELLOW),
            " の型を3つに分ける。",
            font_size=20,
            color=YELLOW,
        )
        definition.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(definition), run_time=0.45)
        self.linger(3.5)
        cap = self._caption(
            "場合3は、子の仕事の合計が自分よりちゃんと小さいとき、という条件がつく。",
            "今回はそこまで深く入らない。",
        )
        self.play(FadeOut(definition), FadeIn(cap), run_time=0.4)
        self.wait(1.6)
        self.wipe(self.header)

    def step4_exponents(self):
        chip = self._chip("STEP 4  比べ方")
        lead = self.ja_text("多項式どうしなら、指数を見れば足りる。", font_size=26)
        self.below_chip(lead, chip)
        self.play(FadeIn(lead), run_time=0.4)
        self.wait(1.15)
        rows = self._formula_rows(
            [
                self._mix(MathTex(r"f(n)=n^{c}", font_size=30), self.ja_text("、葉は", font_size=22), MathTex(r"n^{d}", font_size=30), self.ja_text("、", font_size=22), MathTex(r"d=\log_b a", font_size=30)),
                self._mix(MathTex(r"c<d", font_size=30, color=GREEN), self.ja_text(" なら場合1。", font_size=24)),
                self._mix(MathTex(r"c=d", font_size=30, color=YELLOW), self.ja_text(" なら場合2。", font_size=24)),
                self._mix(MathTex(r"c>d", font_size=30, color=ORANGE), self.ja_text(" なら場合3。", font_size=24)),
            ],
            lead,
            buff=0.28,
        )
        self.play(FadeOut(rows), run_time=0.3)
        checks = VGroup(
            self._mix(MathTex(r"+1", font_size=28), self.ja_text(" は", font_size=22), MathTex(r"c=0,\ d=1", font_size=28), self.ja_text("。場合1。", font_size=22)),
            self._mix(MathTex(r"+n", font_size=28), self.ja_text(" は", font_size=22), MathTex(r"c=1=d", font_size=28), self.ja_text("。場合2。", font_size=22)),
            self._mix(MathTex(r"+n^{2}", font_size=28), self.ja_text(" は", font_size=22), MathTex(r"c=2>1", font_size=28), self.ja_text("。場合3。", font_size=22)),
        ).arrange(DOWN, buff=0.24, aligned_edge=LEFT)
        self.below_chip(checks, chip, buff=0.4)
        for row in checks:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.1)
        cap = self._caption("指数が同じなら、段数が残る。違うなら、大きいほうの型になる。")
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.6)
        self.wipe(self.header)

    def worked_example(self):
        chip = self._chip("実例  前回の式")
        target = self._mix(self.ja_text("対象", font_size=24), MathTex(r"T(n)=2T(n/2)+n", font_size=32))
        self.below_chip(target, chip)
        self.play(FadeIn(target), run_time=0.4)
        self.wait(1.0)
        steps = VGroup(
            MathTex(r"a=2,\ b=2,\ f(n)=n", font_size=28),
            MathTex(r"d=\log_2 2=1", font_size=28),
            MathTex(r"n^{d}=n", font_size=28),
            MathTex(r"c=1=d", font_size=28),
            self._mix(self.ja_text("場合2。よって", font_size=22), MathTex(r"T(n)=\Theta(n\log n)", font_size=30, color=YELLOW)),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        self.stack_below(steps, target, buff=0.24)
        for row in steps:
            self.play(FadeIn(row), run_time=0.35)
            self.wait(1.0)
        self.play(FadeOut(VGroup(target, steps)), run_time=0.3)
        check = VGroup(
            self.ja_text("n=8 を、前回の手計算と照らす。", font_size=22),
            MathTex(r"\log_2 8=3", font_size=30),
            MathTex(r"8\cdot(3+1)=32", font_size=30),
            self._line("大きい項は ", MathTex(r"n\log n", font_size=28), "。定数倍や ", MathTex(r"+n", font_size=28), " は型に入る。", font_size=22),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        self.below_chip(check, chip, buff=0.35)
        for row in check:
            self.play(FadeIn(row), run_time=0.35)
            self.wait(1.05)
        definition = self.ja_text("前回手で足した答えと、マスター定理の場合2は同じ型。", font_size=22, color=YELLOW)
        definition.to_edge(DOWN, buff=0.22)
        self.play(FadeIn(definition), run_time=0.45)
        self.linger(3.4)
        cap = self._caption(
            self._line(
                "木を描かなくても、",
                MathTex(r"a,b,f", font_size=26),
                " を読んで場合を選べば、型は出る。",
                font_size=24,
            )
        )
        self.play(FadeOut(definition), FadeIn(cap), run_time=0.4)
        self.wait(1.6)
        self.wipe(self.header)

    def summary(self):
        chip = self._chip("まとめ")
        items = VGroup(
            self._line("1. 形は ", MathTex(r"T(n)=aT(n/b)+f(n)", font_size=26), "。", font_size=24),
            self._line("2. 葉 ", MathTex(r"n^{\log_b a}", font_size=26), " と ", MathTex(r"f(n)", font_size=26), " を比べる。", font_size=24),
            self.ja_text("3. 小さい・同じ・大きい、の3つで型が決まる。", font_size=24),
        ).arrange(DOWN, buff=0.32, aligned_edge=LEFT)
        self.below_chip(items, chip, buff=0.45)
        for row in items:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.35)
        cap = self._caption("前回の木の足し算は、場合2の「段数を掛ける」だった。")
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.6)
        self.wipe(self.header)

    def next_preview(self):
        chip = self._chip("次回")
        nxt = self.ja_text("#9 償却解析の考え方", font_size=32, color=YELLOW)
        self.below_chip(nxt, chip, buff=0.5)
        self.play(FadeIn(nxt), run_time=0.45)
        self.wait(1.15)
        body = VGroup(
            self.ja_text("今回は、1つの再帰の増え方を場合分けした。", font_size=26),
            self.ja_text("次回は、いちばん高い1回ではなく、", font_size=26),
            self.ja_text("連続した操作の合計で見る。", font_size=26),
        ).arrange(DOWN, buff=0.26, aligned_edge=LEFT)
        self.stack_below(body, nxt, buff=0.4)
        for row in body:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.15)
        self.wait(1.3)
