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
                    "今回見るのは、",
                    MathTex(r"T(n)=aT(n/b)+f(n)", font_size=26),
                    " という形の再帰です。",
                    font_size=24,
                ),
                self._line(
                    "木のいちばん下（葉）の仕事 ",
                    MathTex(r"n^{\log_b a}", font_size=26),
                    " と、自分の段の仕事 ",
                    MathTex(r"f(n)", font_size=26),
                    " を比べます。",
                    font_size=22,
                ),
                "小さい・同じ・大きいの3通りで、答えの増え方の型が決まります。",
            ]
        )
        self._show_overview(
            [
                self._line(
                    "STEP 1 … 式から、子の数 ",
                    MathTex(r"a", font_size=22),
                    "、半分の仕方 ",
                    MathTex(r"b", font_size=22),
                    "、自分の仕事 ",
                    MathTex(r"f(n)", font_size=22),
                    " を読む",
                    font_size=20,
                ),
                self._line(
                    "STEP 2 … いちばん下の呼び出しが何個あるかを出す。それが ",
                    MathTex(r"n^{\log_b a}", font_size=22),
                    font_size=20,
                ),
                "STEP 3 … 葉の仕事と自分の仕事を、小さい・同じ・大きいの3つに分ける",
                "STEP 4 … 多項式どうしなら、指数を見るだけで大小が分かる",
            ],
            [
                self._line(
                    "最後に、前回の ",
                    MathTex(r"T(n)=2T(n/2)+n", font_size=24),
                    " を、最初から最後までこの場合分けに当てはめます。",
                    font_size=22,
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
        q = VGroup(
            self.ja_text("前回は、再帰の木を描いて、段ごとの仕事を足しました。", font_size=24),
            self.ja_text("自分の段の仕事が変わると、その足し算の答えの型も変わります。", font_size=24),
        ).arrange(DOWN, buff=0.14)
        q.next_to(self.header, DOWN, buff=0.32)
        q.set_x(0)
        self.play(FadeIn(q), run_time=0.55)
        self.wait(1.4)
        note = self.ja_text("子は2つ、大きさは半分。変えるのは自分の段の仕事だけです。", font_size=20, color=GREY_B)
        note.next_to(q, DOWN, buff=0.22)
        note.set_x(0)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.1)
        cards = VGroup(
            self._card(
                "自分の仕事が n",
                "前回、手で足した",
                MathTex(r"\Theta(n\log n)", font_size=22, color=BLUE),
                BLUE,
                width=5.4,
                height=2.05,
            ),
            self._card(
                "自分の仕事が 1",
                "下の葉の仕事のほうが多い",
                self.ja_text("答えの型は変わる", font_size=20, color=ORANGE),
                ORANGE,
                width=5.4,
                height=2.05,
            ),
        ).arrange(RIGHT, buff=0.4)
        cards.next_to(note, DOWN, buff=0.24)
        cards.set_x(0)
        self.play(FadeIn(cards), run_time=0.7)
        self.wait(1.3)
        cap = self._caption(
            "毎回木を全部描き直さなくても、場合分けで型を出したい。",
            "今回はそのための道具、マスター定理をやります。",
        )
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.8)
        self._clear(VGroup(q, note, cards, cap))

    def step1_form(self):
        chip = self._chip("STEP 1  形")
        lead = self.ja_text(
            "マスター定理は、どんな再帰にでも使えるわけではありません。だいたい次の形のときに使えます。",
            font_size=20,
        )
        self.below_chip(lead, chip)
        self.play(FadeIn(lead), run_time=0.4)
        self.wait(1.3)
        rows = self._formula_rows(
            [
                MathTex(r"T(n)=a\,T(n/b)+f(n)", font_size=34, color=YELLOW),
                self._mix(MathTex(r"a", font_size=28), self.ja_text(" は、1回の呼び出しが作る子の個数です。", font_size=22)),
                self._mix(
                    MathTex(r"n/b", font_size=28),
                    self.ja_text(" は、1つの子の入力の大きさです。", font_size=20),
                    MathTex(r"b=2", font_size=26),
                    self.ja_text(" なら半分。", font_size=20),
                ),
                self._mix(MathTex(r"f(n)", font_size=28), self.ja_text(" は、その段で自分自身がする仕事です。", font_size=22)),
            ],
            lead,
            buff=0.22,
        )
        self.play(FadeOut(VGroup(lead, rows)), run_time=0.3)
        fit = VGroup(
            self.ja_text("前回やった式は、ちょうどこの形です。3つの部品に分けます。", font_size=22),
            MathTex(r"T(n)=2T(n/2)+n", font_size=32),
            self._mix(self.ja_text("子は2つなので", font_size=22), MathTex(r"a=2", font_size=28), self.ja_text("。大きさは半分なので", font_size=22), MathTex(r"b=2", font_size=28), self.ja_text("。", font_size=22)),
            self._mix(self.ja_text("自分の仕事は", font_size=22), MathTex(r"n", font_size=28), self.ja_text(" なので", font_size=22), MathTex(r"f(n)=n", font_size=28), self.ja_text("。", font_size=22)),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        self.below_chip(fit, chip, buff=0.32)
        for row in fit:
            self.play(FadeIn(row), run_time=0.35)
            self.wait(1.05)
        definition = VGroup(
            self._line(
                "マスター定理の対象は、",
                MathTex(r"T(n)=aT(n/b)+f(n)", font_size=24, color=YELLOW),
                " の形の漸化式です。",
                font_size=20,
                color=YELLOW,
            ),
            self.ja_text("つまり、子の数・半分の仕方・自分の仕事が読める再帰です。", font_size=20, color=YELLOW),
        ).arrange(DOWN, buff=0.08)
        definition.to_edge(DOWN, buff=0.18)
        definition.set_x(0)
        self.play(FadeIn(definition), run_time=0.45)
        self.linger(3.5)
        cap = self._caption(
            "この3つが読めれば、あとは葉の仕事と比べるだけです。",
            "次で葉の個数を出します。",
        )
        self.play(FadeOut(definition), FadeIn(cap), run_time=0.4)
        self.wait(1.6)
        self.wipe(self.header)

    def step2_leaves(self):
        chip = self._chip("STEP 2  葉")
        lead = VGroup(
            self.ja_text("再帰の木を下へ進むと、いつか大きさ 1 の呼び出しに着きます。", font_size=22),
            self.ja_text("このいちばん下を「葉」と呼びます。葉が何個あるかが、下側の仕事の量です。", font_size=22),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        self.below_chip(lead, chip)
        self.play(FadeIn(lead), run_time=0.4)
        self.wait(1.4)
        self.play(FadeOut(lead), run_time=0.3)
        rows = self._formula_rows(
            [
                self._mix(self.ja_text("段0: ノードは", font_size=20), MathTex(r"1", font_size=28), self.ja_text(" 個、大きさは", font_size=20), MathTex(r"n", font_size=28)),
                self._mix(self.ja_text("段1: ノードは", font_size=20), MathTex(r"a", font_size=28), self.ja_text(" 個、大きさは", font_size=20), MathTex(r"n/b", font_size=28)),
                self._mix(self.ja_text("段", font_size=20), MathTex(r"k", font_size=28), self.ja_text(": ノードは", font_size=20), MathTex(r"a^{k}", font_size=28), self.ja_text(" 個、大きさは", font_size=20), MathTex(r"n/b^{k}", font_size=28)),
                self._mix(self.ja_text("葉は大きさが1の段。", font_size=20), MathTex(r"n/b^{k}=1", font_size=26), self.ja_text(" なので", font_size=20), MathTex(r"k=\log_b n", font_size=26)),
                self._mix(self.ja_text("葉の個数は", font_size=20), MathTex(r"a^{\log_b n}=n^{\log_b a}", font_size=30, color=YELLOW)),
            ],
            chip,
            buff=0.2,
        )
        self.play(FadeOut(rows), run_time=0.3)
        plug = VGroup(
            self.ja_text("前回の式なら、子が2つで半分なので、指数はこうなります。", font_size=22),
            MathTex(r"a=2,\ b=2", font_size=30),
            MathTex(r"\log_2 2=1", font_size=30),
            self._mix(self.ja_text("葉の個数は", font_size=22), MathTex(r"n^{1}=n", font_size=32, color=YELLOW)),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        self.below_chip(plug, chip, buff=0.32)
        for row in plug:
            self.play(FadeIn(row), run_time=0.35)
            self.wait(1.0)
        definition = VGroup(
            self._line(
                "葉の仕事の合計は ",
                MathTex(r"\Theta(n^{\log_b a})", font_size=24, color=YELLOW),
                " です。",
                font_size=20,
                color=YELLOW,
            ),
            self._line(
                "次は、この下側の仕事と、自分の段の仕事 ",
                MathTex(r"f(n)", font_size=24, color=YELLOW),
                " のどちらが大きいかを比べます。",
                font_size=20,
                color=YELLOW,
            ),
        ).arrange(DOWN, buff=0.08)
        definition.to_edge(DOWN, buff=0.16)
        definition.set_x(0)
        self.play(FadeIn(definition), run_time=0.45)
        self.linger(3.5)
        cap = self._caption(
            "下の仕事が勝つか、自分の仕事が勝つか、同じくらいか。",
            "この3つで場合が分かれます。",
        )
        self.play(FadeOut(definition), FadeIn(cap), run_time=0.4)
        self.wait(1.6)
        self.wipe(self.header)

    def step3_cases(self):
        chip = self._chip("STEP 3  場合")
        lead = self._line(
            "自分の段の仕事 ",
            MathTex(r"f(n)", font_size=26),
            " が、葉の仕事より小さいか、同じくらいか、大きいかで、答えの型が決まります。",
            font_size=20,
        )
        self.below_chip(lead, chip)
        self.play(FadeIn(lead), run_time=0.4)
        self.wait(1.25)
        table = self.aligned_table(
            [
                [
                    self.ja_text("場合", font_size=18, color=GREY_B),
                    self.ja_text("自分の仕事と葉", font_size=18, color=GREY_B),
                    self.ja_text("答えの型", font_size=18, color=GREY_B),
                ],
                [
                    MathTex(r"1", font_size=26, color=GREEN),
                    self.ja_text("葉の仕事のほうが大きい", font_size=20),
                    MathTex(r"\Theta(n^{\log_b a})", font_size=24, color=GREEN),
                ],
                [
                    MathTex(r"2", font_size=26, color=YELLOW),
                    self.ja_text("だいたい同じくらい", font_size=20),
                    MathTex(r"\Theta(n^{\log_b a}\log n)", font_size=22, color=YELLOW),
                ],
                [
                    MathTex(r"3", font_size=26, color=ORANGE),
                    self.ja_text("自分の仕事のほうが大きい", font_size=20),
                    MathTex(r"\Theta(f(n))", font_size=24, color=ORANGE),
                ],
            ],
            h_buff=0.32,
            v_buff=0.14,
        )
        table.scale(0.82)
        self.stack_below(table, lead, buff=0.2)
        table.set_x(0)
        self.reveal_table(table, row_wait=0.9)
        note = VGroup(
            self._line(
                "場合2は、どの段の仕事の合計もだいたい同じです。だから段の数 ",
                MathTex(r"\log n", font_size=22),
                " が答えに残ります。",
                font_size=18,
            ),
            self._line(
                "前回、手で足した ",
                MathTex(r"n\log n", font_size=22),
                " がこれです。",
                font_size=18,
            ),
        ).arrange(DOWN, buff=0.08)
        note.next_to(table, DOWN, buff=0.16)
        note.set_x(0)
        self.play(FadeIn(note), run_time=0.35)
        self.wait(1.4)
        self.play(FadeOut(VGroup(lead, table, note)), run_time=0.3)
        examples = VGroup(
            self._mix(
                MathTex(r"T(n)=2T(n/2)+1", font_size=24),
                self.ja_text("自分の仕事が小さい。場合1", font_size=20),
                MathTex(r"\Theta(n)", font_size=24, color=GREEN),
                buff=0.2,
            ),
            self._mix(
                MathTex(r"T(n)=2T(n/2)+n", font_size=24),
                self.ja_text("同じくらい。場合2", font_size=20),
                MathTex(r"\Theta(n\log n)", font_size=24, color=YELLOW),
                buff=0.2,
            ),
            self._mix(
                MathTex(r"T(n)=2T(n/2)+n^{2}", font_size=24),
                self.ja_text("自分の仕事が大きい。場合3", font_size=20),
                MathTex(r"\Theta(n^{2})", font_size=24, color=ORANGE),
                buff=0.2,
            ),
        ).arrange(DOWN, buff=0.26, aligned_edge=LEFT)
        self.below_chip(examples, chip, buff=0.38)
        for row in examples:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.15)
        definition = self._line(
            "マスター定理は、葉の仕事と ",
            MathTex(r"f(n)", font_size=22, color=YELLOW),
            " の大小で、",
            MathTex(r"T(n)", font_size=22, color=YELLOW),
            " の増え方の型を3つに分けます。",
            font_size=18,
            color=YELLOW,
        )
        definition.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(definition), run_time=0.45)
        self.linger(3.5)
        cap = self._caption(
            "場合3には、子の仕事の合計が自分よりちゃんと小さい、という追加の条件がつきます。",
            "今回は名前だけ覚えて、証明には入りません。",
        )
        self.play(FadeOut(definition), FadeIn(cap), run_time=0.4)
        self.wait(1.7)
        self.wipe(self.header)

    def step4_exponents(self):
        chip = self._chip("STEP 4  比べ方")
        lead = self.ja_text(
            "葉の仕事も自分の仕事も、どちらも n の何乗かという形なら、指数を見るだけで大小が分かります。",
            font_size=20,
        )
        self.below_chip(lead, chip)
        self.play(FadeIn(lead), run_time=0.4)
        self.wait(1.3)
        defs = self._formula_rows(
            [
                self._mix(
                    self.ja_text("自分の仕事を", font_size=20),
                    MathTex(r"f(n)=n^{c}", font_size=28),
                    self.ja_text(" と書きます。", font_size=20),
                ),
                self._mix(
                    self.ja_text("葉の仕事は", font_size=20),
                    MathTex(r"n^{d}", font_size=28),
                    self.ja_text("、指数は", font_size=20),
                    MathTex(r"d=\log_b a", font_size=28),
                    self.ja_text(" です。", font_size=20),
                ),
            ],
            lead,
            buff=0.32,
            row_buff=0.36,
        )
        self.play(FadeOut(VGroup(lead, defs)), run_time=0.3)
        cases = VGroup(
            self._mix(MathTex(r"c<d", font_size=30, color=GREEN), self.ja_text(" なら、葉のほうが大きい。場合1です。", font_size=22), buff=0.18),
            self._mix(MathTex(r"c=d", font_size=30, color=YELLOW), self.ja_text(" なら、同じくらい。場合2です。", font_size=22), buff=0.18),
            self._mix(MathTex(r"c>d", font_size=30, color=ORANGE), self.ja_text(" なら、自分の仕事のほうが大きい。場合3です。", font_size=22), buff=0.18),
        ).arrange(DOWN, buff=0.42, aligned_edge=LEFT)
        self.below_chip(cases, chip, buff=0.4)
        for row in cases:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.15)
        self.play(FadeOut(cases), run_time=0.3)
        intro = VGroup(
            self.ja_text("さっきの3つの式で、指数を確認します。", font_size=22),
            self.ja_text("どちらも子が2つで半分なので、葉の指数は 1 です。", font_size=22),
        ).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        self.below_chip(intro, chip, buff=0.36)
        self.play(FadeIn(intro), run_time=0.35)
        self.wait(1.2)
        checks = VGroup(
            self._mix(
                MathTex(r"+1", font_size=26),
                self.ja_text(" は定数です。指数は", font_size=20),
                MathTex(r"c=0", font_size=26),
                self.ja_text("。葉より小さいので場合1です。", font_size=20),
                buff=0.16,
            ),
            self._mix(
                MathTex(r"+n", font_size=26),
                self.ja_text(" は指数", font_size=20),
                MathTex(r"c=1", font_size=26),
                self.ja_text("。葉と同じなので場合2です。", font_size=20),
                buff=0.16,
            ),
            self._mix(
                MathTex(r"+n^{2}", font_size=26),
                self.ja_text(" は指数", font_size=20),
                MathTex(r"c=2", font_size=26),
                self.ja_text("。葉より大きいので場合3です。", font_size=20),
                buff=0.16,
            ),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        self.stack_below(checks, intro, buff=0.36)
        for row in checks:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.15)
        cap = self._caption(
            "指数が同じなら、どの段の仕事も同じくらいなので、段数が答えに残ります。",
            "指数が違うなら、大きいほうの仕事が全体の型になります。",
        )
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.7)
        self.wipe(self.header)

    def worked_example(self):
        chip = self._chip("実例  前回の式")
        target = self._mix(self.ja_text("対象", font_size=22), MathTex(r"T(n)=2T(n/2)+n", font_size=32))
        self.below_chip(target, chip)
        self.play(FadeIn(target), run_time=0.4)
        self.wait(1.0)
        steps = VGroup(
            self._mix(self.ja_text("形を読む。", font_size=20), MathTex(r"a=2,\ b=2,\ f(n)=n", font_size=26)),
            self._mix(self.ja_text("葉の指数。", font_size=20), MathTex(r"d=\log_2 2=1", font_size=26), self.ja_text("。葉の仕事は", font_size=20), MathTex(r"n^{1}=n", font_size=26)),
            self._mix(self.ja_text("自分の仕事も", font_size=20), MathTex(r"n^{1}", font_size=26), self.ja_text(" なので", font_size=20), MathTex(r"c=1=d", font_size=26)),
            self._mix(self.ja_text("同じくらいなので場合2。よって", font_size=20), MathTex(r"T(n)=\Theta(n\log n)", font_size=28, color=YELLOW)),
        ).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        self.stack_below(steps, target, buff=0.22)
        for row in steps:
            self.play(FadeIn(row), run_time=0.35)
            self.wait(1.05)
        self.play(FadeOut(VGroup(target, steps)), run_time=0.3)
        check = VGroup(
            self.ja_text("前回、n=8 の木を手で足すと 32 になりました。場合2の型と合うか見ます。", font_size=20),
            self._mix(MathTex(r"\log_2 8=3", font_size=28), self.ja_text(" です。段は 3 段下がって葉です。", font_size=20), buff=0.16),
            MathTex(r"8\cdot(3+1)=32", font_size=30),
            self._line(
                "いちばん大きい項が ",
                MathTex(r"n\log n", font_size=24),
                " です。定数倍や ",
                MathTex(r"+n", font_size=24),
                " は型に含まれます。",
                font_size=20,
            ),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        self.below_chip(check, chip, buff=0.32)
        for row in check:
            self.play(FadeIn(row), run_time=0.35)
            self.wait(1.05)
        definition = self.ja_text(
            "前回手で足した答えと、マスター定理の場合2は、同じ増え方の型です。",
            font_size=20,
            color=YELLOW,
        )
        definition.to_edge(DOWN, buff=0.2)
        self.play(FadeIn(definition), run_time=0.45)
        self.linger(3.4)
        cap = self._caption(
            self._line(
                "木を全部描かなくても、",
                MathTex(r"a,b,f", font_size=24),
                " を読んで場合を選べば、答えの型は出ます。",
                font_size=22,
            )
        )
        self.play(FadeOut(definition), FadeIn(cap), run_time=0.4)
        self.wait(1.6)
        self.wipe(self.header)

    def summary(self):
        chip = self._chip("まとめ")
        items = VGroup(
            self._line("1. 使える形は ", MathTex(r"T(n)=aT(n/b)+f(n)", font_size=24), "。子の数・半分の仕方・自分の仕事を先に読む。", font_size=20),
            self._line("2. 葉の仕事 ", MathTex(r"n^{\log_b a}", font_size=24), " と、自分の仕事 ", MathTex(r"f(n)", font_size=24), " の大小を比べる。", font_size=20),
            self.ja_text("3. 小さい・同じ・大きいの3つで、答えの型が決まる。", font_size=22),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        self.below_chip(items, chip, buff=0.4)
        for row in items:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.35)
        cap = self._caption(
            "前回の木の足し算は、場合2でした。",
            "どの段も同じなので、段数を掛ける、というやつです。",
        )
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
            self.ja_text("今回は、1つの再帰がどう増えるかを場合分けしました。", font_size=24),
            self.ja_text("次回は、いちばん高い1回だけではなく、", font_size=24),
            self.ja_text("同じ操作を続けたときの合計から、1回あたりの仕事を見ます。", font_size=24),
        ).arrange(DOWN, buff=0.24, aligned_edge=LEFT)
        self.stack_below(body, nxt, buff=0.36)
        for row in body:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.15)
        self.wait(1.3)
