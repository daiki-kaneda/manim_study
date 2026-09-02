from pathlib import Path
import sys

_D01 = Path(__file__).resolve().parent.parent
if str(_D01) not in sys.path:
    sys.path.insert(0, str(_D01))

from manim import *
from curriculum_scene import CurriculumScene


class RecursionComplexity(CurriculumScene):
    """#6 再帰と計算量の関係（約9分）"""

    header_text = "#6  再帰と計算量の関係"

    def construct(self):
        self.header = self._open_header()
        self.hook()
        self._show_goals(
            [
                "再帰は、同じ手順を、より小さい入力でもう一度使う。",
                "終わる条件（ベース）がないと、積み重ねが止まらない。",
                "回数は漸化式 T(n)=T(n-1)+定数 で書いて、ほどいて求める。",
            ]
        )
        self._show_overview(
            [
                "STEP 1 … ベースと再帰呼び出し",
                "STEP 2 … 待ちの枠が積まれる様子（追加メモリ）",
                "STEP 3 … 1回の仕事と、小さい呼び出しを式にする",
                "STEP 4 … 式を一段ずつほどいて T(n)=n にする",
            ],
            ["最後に、n=4 の合計を、呼び出しから戻りまで最初から最後まで通す。"],
        )
        self.step1_def()
        self.step2_stack()
        self.step3_recurrence()
        self.step4_unfold()
        self.worked_example()
        self.summary()
        self.next_preview()

    def _frame(self, label, body, color=ORANGE):
        box = RoundedRectangle(
            width=4.6,
            height=0.85,
            corner_radius=0.1,
            color=color,
            stroke_width=2.5,
            fill_opacity=0.16,
        )
        t = MathTex(label, font_size=28)
        b = self.ja_text(body, font_size=22)
        col = VGroup(t, b).arrange(RIGHT, buff=0.2)
        col.move_to(box)
        return VGroup(box, col)

    def hook(self):
        q = self.ja_text("答えは同じなのに、呼び出しの積み方が違うことがある。", font_size=28)
        q.next_to(self.header, DOWN, buff=0.36)
        self.play(FadeIn(q), run_time=0.55)
        self.wait(1.3)
        eq = MathTex(r"1+2+3+4=10", font_size=32)
        eq.next_to(q, DOWN, buff=0.28)
        self.play(FadeIn(eq), run_time=0.4)
        self.wait(1.0)
        cards = VGroup(
            self._card("手順A ループ", "合計マスを 1 個だけ置く", "追加は 1 マス", BLUE, width=5.4, height=2.05),
            self._card("手順B 再帰", "sum(4) が sum(3) を呼ぶ", "枠が 4 段積まれる", ORANGE, width=5.4, height=2.05),
        ).arrange(RIGHT, buff=0.4)
        cards.next_to(eq, DOWN, buff=0.3)
        cards.set_x(0)
        self.play(FadeIn(cards), run_time=0.7)
        self.wait(1.3)
        self.play(FadeOut(cards), run_time=0.3)
        labels = [
            (r"\mathrm{sum}(4)", "4 + ?"),
            (r"\mathrm{sum}(3)", "3 + ?"),
            (r"\mathrm{sum}(2)", "2 + ?"),
            (r"\mathrm{sum}(1)", "1"),
        ]
        frames = [self._frame(lab, body) for lab, body in labels]
        stack = VGroup(*frames).arrange(UP, buff=0.08)
        stack.next_to(eq, DOWN, buff=0.28)
        for fr in frames:
            self.play(FadeIn(fr, shift=UP * 0.1), run_time=0.35)
            self.wait(0.7)
        cap = self._caption("答えはどちらも 10。違うのは、待ちの枠が何段積まれるか。")
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.7)
        self._clear(VGroup(q, eq, stack, cap))

    def step1_def(self):
        chip = self._chip("STEP 1  再帰")
        lead = self.ja_text("再帰は、同じ手順の中で、もっと小さい同じ問題を解いてもらう書き方。", font_size=24)
        self.below_chip(lead, chip)
        self.play(FadeIn(lead), run_time=0.4)
        self.wait(1.2)
        rules = VGroup(
            self._mix(MathTex(r"n=1", font_size=28), self.ja_text("のとき、答えは 1。ここで終わる（ベース）。", font_size=22)),
            self._mix(MathTex(r"n\ge 2", font_size=28), self.ja_text("のとき、答えは n + sum(n-1)。", font_size=22)),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        rules.next_to(lead, DOWN, buff=0.3)
        for row in rules:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.1)
        unfold = VGroup(
            MathTex(r"\mathrm{sum}(4)=4+\mathrm{sum}(3)", font_size=30),
            MathTex(r"\mathrm{sum}(3)=3+\mathrm{sum}(2)", font_size=30),
            MathTex(r"\mathrm{sum}(2)=2+\mathrm{sum}(1)", font_size=30),
            MathTex(r"\mathrm{sum}(1)=1", font_size=30, color=GREEN),
        ).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        unfold.next_to(rules, DOWN, buff=0.28)
        for row in unfold:
            self.play(FadeIn(row), run_time=0.35)
            self.wait(0.95)
        definition = self.ja_text("再帰は、ベースで止まり、それ以外では自分をより小さい入力で呼び出す手順。", font_size=22, color=YELLOW)
        definition.to_edge(DOWN, buff=0.22)
        self.play(FadeIn(definition), run_time=0.45)
        self.linger(3.4)
        cap = self._caption("ベースがないと、n が減っていかず、呼び出しが終わらない。")
        self.play(FadeOut(definition), FadeIn(cap), run_time=0.4)
        self.wait(1.5)
        self.wipe(self.header)

    def step2_stack(self):
        chip = self._chip("STEP 2  スタック")
        lead = self.ja_text("呼び出しは、前の枠が答えを待つあいだ、画面に残る。これをスタックと呼ぶ。", font_size=24)
        self.below_chip(lead, chip)
        self.play(FadeIn(lead), run_time=0.4)
        self.wait(1.2)
        stack = VGroup()
        labels = [
            (r"\mathrm{sum}(4)", "4 + ?"),
            (r"\mathrm{sum}(3)", "3 + ?"),
            (r"\mathrm{sum}(2)", "2 + ?"),
            (r"\mathrm{sum}(1)", "1"),
        ]
        base_y = -1.6
        for i, (lab, body) in enumerate(labels):
            fr = self._frame(lab, body)
            fr.move_to(DOWN * (base_y - 0) + UP * (0.95 * i))
            fr.set_x(0)
            stack.add(fr)
            self.play(FadeIn(fr, shift=UP * 0.12), run_time=0.4)
            self.wait(0.75)
        note = self.ja_text("いちばん高く積まれた段数が、追加メモリの目安。今は 4 段。一般には n 段。", font_size=22)
        note.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(note), run_time=0.35)
        self.wait(1.3)
        extra = VGroup(
            self._mix(self.ja_text("追加の増え方は", font_size=24), MathTex(r"O(n)", font_size=32, color=ORANGE), self.ja_text("。", font_size=24)),
            self._mix(self.ja_text("ループの合計は追加 1 マスで", font_size=24), MathTex(r"O(1)", font_size=32, color=BLUE), self.ja_text("。", font_size=24)),
        ).arrange(DOWN, buff=0.18)
        extra.next_to(note, UP, buff=0.2)
        for row in extra:
            self.play(FadeIn(row), run_time=0.35)
            self.wait(1.1)
        cap = self._caption("時間だけでなく、待ちの枠の段数も n で増える。")
        self.play(FadeOut(note), FadeIn(cap), run_time=0.4)
        self.wait(1.5)
        self.wipe(self.header)

    def step3_recurrence(self):
        chip = self._chip("STEP 3  漸化式")
        lead = self.ja_text("1回の sum(n) で、自分の足し算はだいたい 1 回。あとは sum(n-1) に任せる。", font_size=24)
        self.below_chip(lead, chip)
        self.play(FadeIn(lead), run_time=0.4)
        self.wait(1.2)
        rows = self._formula_rows(
            [
                self._mix(self.ja_text("ベース:", font_size=24), MathTex(r"T(1)=1", font_size=32)),
                self._mix(MathTex(r"n\ge 2:", font_size=28), MathTex(r"T(n)=T(n-1)+1", font_size=32)),
                self.ja_text("「+1」は、戻ってきた値に n を足す仕事。", font_size=22),
            ],
            chip,
            buff=0.45,
        )
        definition = self.ja_text("再帰の回数は、T(n) を T(小さい入力) で書く漸化式になる。", font_size=24, color=YELLOW)
        definition.next_to(rows, DOWN, buff=0.4)
        definition.set_x(0)
        self.play(FadeIn(definition), run_time=0.45)
        self.linger(3.4)
        cap = self._caption("木に広がる再帰は次回。今日は、1段ずつ小さくなる一本道。")
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.5)
        self.wipe(self.header)

    def step4_unfold(self):
        chip = self._chip("STEP 4  ほどく")
        rows = self._formula_rows(
            [
                MathTex(r"T(n)=T(n-1)+1", font_size=32),
                MathTex(r"T(n-1)=T(n-2)+1", font_size=30),
                MathTex(r"T(n)=(T(n-2)+1)+1=T(n-2)+2", font_size=28),
                MathTex(r"T(n)=T(n-3)+3", font_size=30),
                MathTex(r"T(n)=T(n-k)+k", font_size=30),
                self._mix(self.ja_text("ベースは", font_size=22), MathTex(r"n-k=1", font_size=28), self.ja_text("、つまり", font_size=22), MathTex(r"k=n-1", font_size=28)),
                MathTex(r"T(n)=T(1)+(n-1)=1+(n-1)=n", font_size=30, color=YELLOW),
                MathTex(r"\Theta(n)", font_size=36, color=YELLOW),
            ],
            chip,
            buff=0.32,
        )
        cap = self._caption("一本道の再帰は、ほどくと足し算の列になる。段数も n なので、時間も追加も Θ(n)。")
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.7)
        self.wipe(self.header)

    def worked_example(self):
        chip = self._chip("実例  sum(4)")
        goal = self._mix(self.ja_text("目標", font_size=24), MathTex(r"1+2+3+4", font_size=30), self.ja_text("。答えは 10。", font_size=24))
        self.below_chip(goal, chip)
        self.play(FadeIn(goal), run_time=0.4)
        down = VGroup(
            self.ja_text("降りていく（積む）", font_size=22, color=ORANGE),
            MathTex(r"\mathrm{sum}(4)\to 4+\mathrm{sum}(3)", font_size=26),
            MathTex(r"\mathrm{sum}(3)\to 3+\mathrm{sum}(2)", font_size=26),
            MathTex(r"\mathrm{sum}(2)\to 2+\mathrm{sum}(1)", font_size=26),
            MathTex(r"\mathrm{sum}(1)\to 1", font_size=26, color=GREEN),
            self.ja_text("スタックは 4 段。呼び出しは 4 回。", font_size=22),
        ).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        down.next_to(goal, DOWN, buff=0.22)
        for row in down:
            self.play(FadeIn(row), run_time=0.35)
            self.wait(0.9)
        self.play(FadeOut(down), run_time=0.3)
        up = VGroup(
            self.ja_text("戻っていく（ほどく）", font_size=22, color=BLUE),
            MathTex(r"\mathrm{sum}(1)=1", font_size=26),
            MathTex(r"\mathrm{sum}(2)=2+1=3", font_size=26),
            MathTex(r"\mathrm{sum}(3)=3+3=6", font_size=26),
            MathTex(r"\mathrm{sum}(4)=4+6=10", font_size=26, color=YELLOW),
            MathTex(r"T(4)=T(3)+1=T(2)+2=T(1)+3=4=n", font_size=26),
        ).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        up.next_to(goal, DOWN, buff=0.22)
        for row in up:
            self.play(FadeIn(row), run_time=0.35)
            self.wait(0.95)
        cap = self._caption("答えは同じ 10。再帰は枠が n 段、ループは 1 マス。時間の型はどちらも Θ(n)。")
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.7)
        self.wipe(self.header)

    def summary(self):
        chip = self._chip("まとめ")
        items = VGroup(
            self.ja_text("1. 再帰はベースで止まり、小さい入力でもう一度自分を呼ぶ。", font_size=24),
            self.ja_text("2. 待ちの枠の段数は追加メモリ。一本道なら Θ(n)。", font_size=24),
            self.ja_text("3. 回数は漸化式をほどいて求める。今日は T(n)=n。", font_size=24),
        ).arrange(DOWN, buff=0.32, aligned_edge=LEFT)
        self.below_chip(items, chip, buff=0.45)
        for row in items:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.35)
        cap = self._caption("再帰を見たら、「何回呼ばれるか」と「何段積まれるか」の両方を数える。")
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.6)
        self.wipe(self.header)

    def next_preview(self):
        chip = self._chip("次回")
        nxt = self.ja_text("#7 再帰木による計算量の見積もり", font_size=30, color=YELLOW)
        self.below_chip(nxt, chip, buff=0.5)
        self.play(FadeIn(nxt), run_time=0.45)
        self.wait(1.15)
        body = VGroup(
            self.ja_text("今日は一本道だった。", font_size=26),
            self.ja_text("次回は、一度に2つ呼び出す木になる再帰で、", font_size=26),
            self.ja_text("段ごとの仕事を足して見積もる。", font_size=26),
        ).arrange(DOWN, buff=0.26, aligned_edge=LEFT)
        body.next_to(nxt, DOWN, buff=0.4)
        body.align_to(nxt, LEFT)
        for row in body:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.15)
        self.wait(1.3)
