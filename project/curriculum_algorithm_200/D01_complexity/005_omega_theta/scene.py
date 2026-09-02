from pathlib import Path
import sys

_D01 = Path(__file__).resolve().parent.parent
if str(_D01) not in sys.path:
    sys.path.insert(0, str(_D01))

from manim import *
from curriculum_scene import CurriculumScene


class OmegaTheta(CurriculumScene):
    """#5 漸近記法（Ω, Θ）の使い分け（約9分）"""

    header_text = "#5  漸近記法（Ω, Θ）の使い分け"

    def construct(self):
        self.header = self._open_header()
        self.hook()
        self._show_goals(
            [
                "O は上からの抑え。ゆるくても正しいことがある。",
                "Ω は下からの抑え。「少なくともこれくらいは増える」。",
                "Θ は O と Ω が同じ型のとき。増え方がその型そのもの。",
            ]
        )
        self._show_overview(
            [
                "STEP 1 … O の不等式をもう一度、定数倍まで",
                "STEP 2 … Ω は下から定数倍で抑える",
                "STEP 3 … Θ は両方つく、という意味",
                "STEP 4 … きつい型を書く。ゆるい O だけだと足りない",
            ],
            ["最後に、3n+5 を上からと下から、途中式を残して Θ(n) まで通す。"],
        )
        self.step1_big_o()
        self.step2_omega()
        self.step3_theta()
        self.step4_choose()
        self.worked_example()
        self.summary()
        self.next_preview()

    def hook(self):
        q = self.ja_text("O と書くと上から抑えているだけなので、ゆるいことがある。", font_size=28)
        q.next_to(self.header, DOWN, buff=0.38)
        self.play(FadeIn(q), run_time=0.55)
        self.wait(1.3)
        tline = self._mix(
            self.ja_text("左から n 回見る。回数は", font_size=24),
            MathTex(r"T(n)=n", font_size=32),
            self.ja_text("。", font_size=24),
        )
        tline.next_to(q, DOWN, buff=0.32)
        self.play(FadeIn(tline), run_time=0.4)
        self.wait(1.1)
        cards = VGroup(
            self._card("きつい抑え", "n と同じ速さ", MathTex(r"T(n)=O(n)", font_size=22, color=BLUE), BLUE, width=5.3, height=2.0),
            self._card(
                "ゆるい抑え",
                "式としては正しい",
                self._line(MathTex(r"T(n)=O(n^{2})", font_size=22, color=GREY_B), " もある", font_size=20, color=GREY_B),
                GREY_B,
                width=5.3,
                height=2.0,
            ),
        ).arrange(RIGHT, buff=0.4)
        cards.next_to(tline, DOWN, buff=0.32)
        cards.set_x(0)
        self.play(FadeIn(cards), run_time=0.7)
        self.wait(1.3)
        self.play(FadeOut(cards), run_time=0.3)
        table = self.aligned_table(
            [
                [
                    MathTex(r"n", font_size=24, color=GREY_B),
                    MathTex(r"T=n", font_size=24, color=BLUE),
                    MathTex(r"n^2", font_size=24),
                    MathTex(r"n\le n^2", font_size=22, color=GREY_B),
                ],
                [MathTex(r"2", font_size=28), MathTex(r"2", font_size=28), MathTex(r"4", font_size=28), self.ja_text("はい", font_size=22)],
                [MathTex(r"4", font_size=28), MathTex(r"4", font_size=28), MathTex(r"16", font_size=28), self.ja_text("はい", font_size=22)],
                [MathTex(r"8", font_size=28), MathTex(r"8", font_size=28), MathTex(r"64", font_size=28), self.ja_text("はい", font_size=22)],
            ],
            h_buff=0.42,
            v_buff=0.18,
        )
        table.scale(0.9)
        table.next_to(tline, DOWN, buff=0.28)
        table.set_x(0)
        self.reveal_table(table, row_wait=0.95)
        cap = self._caption(
            self._line(
                "n は ",
                MathTex(r"n^{2}", font_size=28),
                " より小さい。だから ",
                MathTex(r"O(n^{2})", font_size=28),
                " でも上から抑えられている。",
            ),
            "でも、実際の増え方は n のほう。今回はその使い分けをやる。",
        )
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.8)
        self._clear(VGroup(q, tline, table, cap))

    def step1_big_o(self):
        chip = self._chip("STEP 1  ビッグO")
        lead = self.ja_text("O は、「ある定数倍より上に出ない」という意味。", font_size=26)
        self.below_chip(lead, chip)
        self.play(FadeIn(lead), run_time=0.4)
        self.wait(1.15)
        rows = VGroup(
            MathTex(r"T(n)=n", font_size=32),
            self._mix(self.ja_text("定数", font_size=24), MathTex(r"C=1", font_size=30), self.ja_text("を取る。", font_size=24)),
            MathTex(r"n\le 1\cdot n\quad (n\ge 1)", font_size=30),
            MathTex(r"n=O(n)", font_size=34, color=BLUE),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        self.stack_below(rows, lead, buff=0.32)
        for row in rows:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.0)
        loose = VGroup(
            self.ja_text("もっと大きい型でも、上から抑えられる。", font_size=22),
            MathTex(r"n\le n^2\quad (n\ge 1)", font_size=30),
            MathTex(r"n=O(n^2)", font_size=32, color=GREY_B),
            self.ja_text("ただし、これはゆるい。", font_size=22, color=ORANGE),
        ).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        self.stack_below(loose, rows, buff=0.28)
        for row in loose:
            self.play(FadeIn(row), run_time=0.35)
            self.wait(1.0)
        definition = self.ja_text(
            "T(n)=O(f(n)) は、十分大きい n で T(n) ≤ C·f(n) となる定数 C がある、という意味。",
            font_size=22,
            color=YELLOW,
        )
        definition.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(definition), run_time=0.45)
        self.linger(3.5)
        cap = self._caption("O は「これより速くは増えない」。遅さの下限ではない。")
        self.play(FadeOut(definition), FadeIn(cap), run_time=0.4)
        self.wait(1.5)
        self.wipe(self.header)

    def step2_omega(self):
        chip = self._chip("STEP 2  オメガ")
        lead = self.ja_text("下からも抑えたいときは、Ω を使う。「少なくともこれくらいは増える」。", font_size=24)
        self.below_chip(lead, chip)
        self.play(FadeIn(lead), run_time=0.4)
        self.wait(1.2)
        rows = VGroup(
            MathTex(r"n\ge 1\cdot n\quad (n\ge 1)", font_size=32),
            MathTex(r"n=\Omega(n)", font_size=34, color=GREEN),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        self.stack_below(rows, lead, buff=0.32)
        for row in rows:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.05)
        self.play(FadeOut(rows), run_time=0.3)
        why = self._line("n は ", MathTex(r"n^{2}", font_size=30), " の下からは抑えられない。", font_size=24)
        self.stack_below(why, lead, buff=0.35)
        self.play(FadeIn(why), run_time=0.35)
        checks = VGroup(
            MathTex(r"n=10:\ 10\ge C\cdot 100 \Rightarrow C\le 0.1", font_size=28),
            MathTex(r"n=100:\ 100\ge C\cdot 10000 \Rightarrow C\le 0.01", font_size=28),
            self.ja_text("n を大きくすると、許される C はどんどん小さくなる。", font_size=22),
            self.ja_text("一つの固定した C では、いつまでも成り立たない。", font_size=22),
            MathTex(r"n \neq \Omega(n^2)", font_size=34, color=RED),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        self.stack_below(checks, why, buff=0.28)
        for row in checks:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.05)
        definition = self.ja_text(
            "T(n)=Ω(f(n)) は、十分大きい n で T(n) ≥ C·f(n) となる定数 C>0 がある、という意味。",
            font_size=22,
            color=YELLOW,
        )
        definition.to_edge(DOWN, buff=0.22)
        self.play(FadeIn(definition), run_time=0.45)
        self.linger(3.5)
        cap = self._caption("Ω は「これより遅くは増えない」。仕事が消えないことの下限。")
        self.play(FadeOut(definition), FadeIn(cap), run_time=0.4)
        self.wait(1.5)
        self.wipe(self.header)

    def step3_theta(self):
        chip = self._chip("STEP 3  シータ")
        lead = self.ja_text("上からも下からも、同じ型で抑えられるとき、Θ と書く。", font_size=26)
        self.below_chip(lead, chip)
        self.play(FadeIn(lead), run_time=0.4)
        self.wait(1.2)
        rows = self._formula_rows(
            [
                MathTex(r"n=O(n),\ n=\Omega(n)", font_size=32),
                MathTex(r"n=\Theta(n)", font_size=36, color=YELLOW),
                self._mix(self.ja_text("定数", font_size=24), MathTex(r"c_1=1,\ c_2=1", font_size=28), self.ja_text("を取る。", font_size=24)),
                MathTex(r"c_1\cdot n \le n \le c_2\cdot n", font_size=32),
            ],
            lead,
            buff=0.32,
        )
        definition = self.ja_text(
            "T(n)=Θ(f(n)) は、T(n)=O(f(n)) かつ T(n)=Ω(f(n)) のとき。増え方が f(n) の型そのもの。",
            font_size=22,
            color=YELLOW,
        )
        definition.next_to(rows, DOWN, buff=0.32)
        definition.set_x(0)
        self.play(FadeIn(definition), run_time=0.45)
        self.linger(3.5)
        cap = self._caption("Θ が書けるなら、O だけより情報が厚い。「その速さで増える」と言ってよい。")
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.5)
        self.wipe(self.header)

    def step4_choose(self):
        chip = self._chip("STEP 4  使い分け")
        table = self.aligned_table(
            [
                [
                    self.ja_text("書き方", font_size=20, color=GREY_B),
                    self.ja_text("意味", font_size=20, color=GREY_B),
                    self.ja_text("T=n の例", font_size=20, color=GREY_B),
                ],
                [MathTex(r"O(n)", font_size=26, color=BLUE), self.ja_text("上から n で抑える", font_size=20), self.ja_text("正しい（きつい）", font_size=20)],
                [MathTex(r"O(n^2)", font_size=26, color=GREY_B), self._line("上から ", MathTex(r"n^{2}", font_size=22), " で抑える", font_size=20), self.ja_text("正しい（ゆるい）", font_size=20)],
                [MathTex(r"\Omega(n)", font_size=26, color=GREEN), self.ja_text("下から n で抑える", font_size=20), self.ja_text("正しい", font_size=20)],
                [MathTex(r"\Theta(n)", font_size=26, color=YELLOW), self.ja_text("上下とも n", font_size=20), self.ja_text("正しい", font_size=20)],
                [MathTex(r"\Theta(n^2)", font_size=26, color=RED), self._line("上下とも ", MathTex(r"n^{2}", font_size=22), font_size=20), self.ja_text("正しくない", font_size=20)],
            ],
            h_buff=0.38,
            v_buff=0.16,
        )
        table.scale(0.82)
        self.below_chip(table, chip, buff=0.32)
        table.set_x(0)
        self.reveal_table(table, row_wait=0.85)
        note = self.ja_text("日常の「オーダーは n」は、だいたい Θ(n) のつもり。", font_size=22)
        note.next_to(table, DOWN, buff=0.22)
        self.play(FadeIn(note), run_time=0.35)
        self.wait(1.3)
        cap = self._caption("きつい型が分かるなら Θ。上だけしか言えないなら O。下だけなら Ω。")
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.6)
        self.wipe(self.header)

    def worked_example(self):
        chip = self._chip("実例  3n+5")
        target = self._mix(self.ja_text("対象", font_size=24), MathTex(r"T(n)=3n+5", font_size=32))
        self.below_chip(target, chip)
        self.play(FadeIn(target), run_time=0.4)
        self.wait(1.0)
        up_t = self.ja_text("上から（O）", font_size=24, color=BLUE)
        self.stack_below(up_t, target, buff=0.28)
        ups = VGroup(
            MathTex(r"3n+5 \le 3n+5n \quad (n\ge 1)", font_size=28),
            MathTex(r"=8n", font_size=28),
            MathTex(r"T(n)\le 8n", font_size=28),
            MathTex(r"T(n)=O(n)", font_size=32, color=BLUE),
        ).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        self.stack_below(ups, up_t, buff=0.16)
        self.play(FadeIn(up_t), run_time=0.3)
        for row in ups:
            self.play(FadeIn(row), run_time=0.35)
            self.wait(0.95)
        self.play(FadeOut(VGroup(up_t, ups)), run_time=0.3)
        lo_t = self.ja_text("下から（Ω）", font_size=24, color=GREEN)
        self.stack_below(lo_t, target, buff=0.28)
        los = VGroup(
            MathTex(r"3n+5 \ge 3n", font_size=28),
            MathTex(r"T(n)\ge 3n", font_size=28),
            MathTex(r"T(n)=\Omega(n)", font_size=32, color=GREEN),
        ).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        self.stack_below(los, lo_t, buff=0.16)
        self.play(FadeIn(lo_t), run_time=0.3)
        for row in los:
            self.play(FadeIn(row), run_time=0.35)
            self.wait(1.0)
        self.play(FadeOut(VGroup(lo_t, los, target)), run_time=0.3)
        both = VGroup(
            self.ja_text("両方（Θ）", font_size=24, color=YELLOW),
            MathTex(r"3n \le 3n+5 \le 8n \quad (n\ge 1)", font_size=30),
            MathTex(r"T(n)=\Theta(n)", font_size=36, color=YELLOW),
        ).arrange(DOWN, buff=0.2)
        self.below_chip(both, chip, buff=0.4)
        for row in both:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.1)
        self.linger(3.2)
        checks = VGroup(
            MathTex(r"n=1:\ 8,\quad 3\le 8\le 8", font_size=28),
            MathTex(r"n=4:\ 17,\quad 12\le 17\le 32", font_size=28),
        ).arrange(DOWN, buff=0.16)
        self.stack_below(checks, both, buff=0.28)
        for row in checks:
            self.play(FadeIn(row), run_time=0.35)
            self.wait(1.05)
        cap = self._caption("定数と小さい項を落としたあと、上下が同じ型なら Θ。前回の「落として O(n)」は、実は Θ(n) だった。")
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.7)
        self.wipe(self.header)

    def summary(self):
        chip = self._chip("まとめ")
        items = VGroup(
            self.ja_text("1. O は上から。ゆるくても正しいことがある。", font_size=24),
            self.ja_text("2. Ω は下から。少なくともその型では増える。", font_size=24),
            self.ja_text("3. Θ は両方。増え方がその型そのもの。", font_size=24),
        ).arrange(DOWN, buff=0.32, aligned_edge=LEFT)
        self.below_chip(items, chip, buff=0.45)
        for row in items:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.35)
        cap = self._caption(
            self._line(
                "「",
                MathTex(r"O(n^{2})", font_size=28),
                "」と見たら、本当に ",
                MathTex(r"n^{2}", font_size=28),
                " なのか、それともゆるいのかを疑う。",
            )
        )
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.6)
        self.wipe(self.header)

    def next_preview(self):
        chip = self._chip("次回")
        nxt = self.ja_text("#6 再帰と計算量の関係", font_size=32, color=YELLOW)
        self.below_chip(nxt, chip, buff=0.5)
        self.play(FadeIn(nxt), run_time=0.45)
        self.wait(1.15)
        body = VGroup(
            self.ja_text("今回は、増え方を上と下から挟んだ。", font_size=26),
            self.ja_text("次回は、自分自身を呼び出す手順で、", font_size=26),
            self.ja_text("回数とスタックがどう増えるかを見る。", font_size=26),
        ).arrange(DOWN, buff=0.26, aligned_edge=LEFT)
        self.stack_below(body, nxt, buff=0.4)
        for row in body:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.15)
        self.wait(1.3)
