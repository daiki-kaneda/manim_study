from pathlib import Path
import sys

_D01 = Path(__file__).resolve().parent.parent
if str(_D01) not in sys.path:
    sys.path.insert(0, str(_D01))

from manim import *
from curriculum_scene import CurriculumScene


class PVsNPIntro(CurriculumScene):
    """#10 P と NP の入門（約9分）"""

    header_text = "#10  P と NP の入門"

    def construct(self):
        self.header = self._open_header()
        self.hook()
        self._show_goals(
            [
                "P は、多項式時間で解ける問題の集まり。",
                "NP は、正しい答えの証拠を多項式時間で確認できる問題の集まり。",
                "P と NP が同じかどうかは、まだ分かっていない。",
            ]
        )
        self._show_overview(
            [
                "STEP 1 … 多項式時間と、指数時間",
                "STEP 2 … 証拠を渡されて、速く確認できる",
                "STEP 3 … P は NP に入る。逆は未解決",
                "STEP 4 … NP完全は、NP の中でいちばん硬い",
            ],
            ["最後に、同じ4つの数で、探索の16通りと、確認の足し算を最初から最後まで通す。"],
        )
        self.step1_p()
        self.step2_np()
        self.step3_subset()
        self.step4_npc()
        self.worked_example()
        self.summary()
        self.next_preview()

    def hook(self):
        q = self.ja_text("答えを確認するのは速くて、答えを探すのは遅いことがある。", font_size=28)
        q.next_to(self.header, DOWN, buff=0.36)
        self.play(FadeIn(q), run_time=0.55)
        self.wait(1.3)
        src = self._boxes([3, 1, 7, 2], side=0.62, font_size=26)
        src.next_to(q, DOWN, buff=0.26)
        src.set_x(0)
        goal = self._mix(self.ja_text("目標", font_size=22), MathTex(r"10", font_size=28))
        goal.next_to(src, DOWN, buff=0.16)
        self.play(FadeIn(src), FadeIn(goal), run_time=0.5)
        self.wait(1.0)
        cards = VGroup(
            self._card(
                "探す",
                "部分集合を順に試す",
                MathTex(r"2^{4}=16", font_size=22, color=ORANGE),
                ORANGE,
                width=5.4,
                height=2.05,
            ),
            self._card(
                "確認する",
                "3 と 7 を足す",
                MathTex(r"3+7=10", font_size=22, color=BLUE),
                BLUE,
                width=5.4,
                height=2.05,
            ),
        ).arrange(RIGHT, buff=0.4)
        cards.next_to(goal, DOWN, buff=0.24)
        cards.set_x(0)
        self.play(FadeIn(cards), run_time=0.7)
        self.wait(1.3)
        cap = self._caption(
            "仕事は同じ「10 になる組があるか」。違うのは、探すか、証拠を見るか。",
            "今回はこの違いをクラスにする。",
        )
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.7)
        self._clear(VGroup(q, src, goal, cards, cap))

    def step1_p(self):
        chip = self._chip("STEP 1  P")
        lead = self.ja_text("入力の大きさ n に対して、n の多項式で終わる手順がある問題を、P に入れる。", font_size=22)
        self.below_chip(lead, chip)
        self.play(FadeIn(lead), run_time=0.4)
        self.wait(1.2)
        rows = VGroup(
            self._mix(MathTex(r"n^{2}", font_size=30), self.ja_text(" や ", font_size=22), MathTex(r"n^{3}", font_size=30), self.ja_text(" なら、多項式。", font_size=22)),
            self._mix(MathTex(r"2^{n}", font_size=30, color=ORANGE), self.ja_text(" は多項式ではない。", font_size=22)),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        self.stack_below(rows, lead, buff=0.28)
        for row in rows:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.05)
        table = self.aligned_table(
            [
                [
                    MathTex(r"n", font_size=22, color=GREY_B),
                    MathTex(r"n^{2}", font_size=22, color=BLUE),
                    MathTex(r"2^{n}", font_size=22, color=ORANGE),
                ],
                [MathTex(r"4", font_size=26), MathTex(r"16", font_size=26), MathTex(r"16", font_size=26)],
                [MathTex(r"8", font_size=26), MathTex(r"64", font_size=26), MathTex(r"256", font_size=26)],
                [MathTex(r"16", font_size=26), MathTex(r"256", font_size=26), MathTex(r"65536", font_size=26, color=ORANGE)],
            ],
            h_buff=0.5,
            v_buff=0.16,
        )
        table.scale(0.88)
        table.next_to(rows, DOWN, buff=0.24)
        table.set_x(0)
        self.reveal_table(table, row_wait=0.9)
        note = self.ja_text("ソートや線形探索は P 側。部分集合の全探索はこのやり方では P に入らない。", font_size=20)
        note.next_to(table, DOWN, buff=0.18)
        note.set_x(0)
        self.play(FadeIn(note), run_time=0.35)
        self.wait(1.2)
        definition = self.ja_text("P は、多項式時間で解ける判定問題の集まり。", font_size=24, color=YELLOW)
        definition.to_edge(DOWN, buff=0.2)
        self.play(FadeIn(definition), run_time=0.45)
        self.linger(3.5)
        cap = self._caption("「速い手順がある」が P。次は、「証拠を見れば速く判定できる」。")
        self.play(FadeOut(definition), FadeIn(cap), run_time=0.4)
        self.wait(1.5)
        self.wipe(self.header)

    def step2_np(self):
        chip = self._chip("STEP 2  NP")
        lead = self.ja_text("「はい」のときは、短い証拠を渡されて、それを多項式時間で確認できる問題を、NP に入れる。", font_size=20)
        self.below_chip(lead, chip)
        self.play(FadeIn(lead), run_time=0.4)
        self.wait(1.25)
        src = self._boxes([3, 1, 7, 2], side=0.58, font_size=24)
        self.stack_below(src, lead, buff=0.28)
        src.set_x(-3.2)
        self.play(FadeIn(src), run_time=0.4)
        self.wait(0.8)
        proof = VGroup(
            self.ja_text("証拠", font_size=22, color=BLUE),
            MathTex(r"\{3,7\}", font_size=32),
            MathTex(r"3+7=10", font_size=32, color=YELLOW),
            self.ja_text("目標と等しい。はい。", font_size=22),
            self._mix(self.ja_text("確認は", font_size=22), MathTex(r"O(n)", font_size=28, color=BLUE)),
        ).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        proof.next_to(src, RIGHT, buff=0.7)
        proof.align_to(src, UP)
        for row in proof:
            self.play(FadeIn(row), run_time=0.35)
            self.wait(0.95)
        search = self._mix(self.ja_text("全部探すと", font_size=22), MathTex(r"2^{n}", font_size=28, color=ORANGE), self.ja_text(" 通り。", font_size=22))
        search.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(search), run_time=0.35)
        self.wait(1.1)
        definition = self.ja_text("NP は、「はい」の証拠を多項式時間で確認できる判定問題の集まり。", font_size=20, color=YELLOW)
        definition.to_edge(DOWN, buff=0.18)
        self.play(FadeOut(search), FadeIn(definition), run_time=0.4)
        self.linger(3.5)
        self.play(FadeOut(definition), run_time=0.3)
        cap = self._caption("探す手順が遅くても、証拠さえあれば確認は速い、というのが NP。")
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.5)
        self.wipe(self.header)

    def step3_subset(self):
        chip = self._chip("STEP 3  包含")
        lead = self.ja_text("速い解き方があるなら、証拠の確認もできる。だから P は NP に入る。", font_size=22)
        self.below_chip(lead, chip)
        self.play(FadeIn(lead), run_time=0.4)
        self.wait(1.2)
        outer = Ellipse(width=6.4, height=3.4, color=ORANGE, stroke_width=3)
        inner = Ellipse(width=3.2, height=1.8, color=BLUE, stroke_width=3)
        inner.move_to(outer.get_center() + LEFT * 0.55)
        np_lab = MathTex(r"\mathrm{NP}", font_size=32, color=ORANGE)
        np_lab.move_to(outer.get_right() + LEFT * 1.15)
        p_lab = MathTex(r"\mathrm{P}", font_size=32, color=BLUE)
        p_lab.move_to(inner)
        diagram = VGroup(outer, inner, np_lab, p_lab)
        diagram.next_to(lead, DOWN, buff=0.35)
        diagram.set_x(0)
        self.play(Create(outer), run_time=0.5)
        self.play(Create(inner), FadeIn(np_lab), FadeIn(p_lab), run_time=0.55)
        self.wait(1.2)
        notes = VGroup(
            self._mix(MathTex(r"P\subseteq NP", font_size=30, color=YELLOW), self.ja_text(" は分かっている。", font_size=22)),
            self._mix(MathTex(r"NP\subseteq P", font_size=30), self.ja_text(" か、つまり探すのも速いか、は未解決。", font_size=22)),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        notes.next_to(diagram, DOWN, buff=0.28)
        notes.set_x(0)
        for row in notes:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.15)
        definition = self._mix(
            MathTex(r"P\subseteq NP", font_size=26, color=YELLOW),
            self.ja_text(" は分かっている。", font_size=22, color=YELLOW),
            MathTex(r"P=NP", font_size=26, color=YELLOW),
            self.ja_text(" かどうかは未解決。", font_size=22, color=YELLOW),
        )
        definition.to_edge(DOWN, buff=0.18)
        self.play(FadeIn(definition), run_time=0.45)
        self.linger(3.5)
        cap = self._caption("確認が速いからといって、探す手順があるとは限らない。そこが開いている。")
        self.play(FadeOut(definition), FadeIn(cap), run_time=0.4)
        self.wait(1.5)
        self.wipe(self.header)

    def step4_npc(self):
        chip = self._chip("STEP 4  完全")
        lead = self.ja_text("NP の中に、「これが速く解けたら、NP の全部が速く解ける」という問題がある。", font_size=22)
        self.below_chip(lead, chip)
        self.play(FadeIn(lead), run_time=0.4)
        self.wait(1.25)
        points = VGroup(
            self.ja_text("それらを NP完全と呼ぶ。", font_size=24),
            self.ja_text("部分集合和（判定版）も、その仲間に入る。", font_size=24),
            self._mix(self.ja_text("1つでも P に入れば、", font_size=24), MathTex(r"P=NP", font_size=30), self.ja_text(" になる。", font_size=24)),
            self.ja_text("だから「いちばん硬いグループ」と覚えてよい。", font_size=24),
        ).arrange(DOWN, buff=0.26, aligned_edge=LEFT)
        self.stack_below(points, lead, buff=0.32)
        for row in points:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.15)
        definition = self.ja_text("NP完全は、NP のどの問題もそれに帰着できる問題。1つが P なら、全部が P。", font_size=20, color=YELLOW)
        definition.to_edge(DOWN, buff=0.22)
        self.play(FadeIn(definition), run_time=0.45)
        self.linger(3.5)
        self.play(FadeOut(definition), run_time=0.3)
        cap = self._caption(
            "今回は証明しない。覚えるのは、",
            "確認は速いが探すのは難しそうな問題の、いちばん硬い層、ということ。",
        )
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.6)
        self.wipe(self.header)

    def worked_example(self):
        chip = self._chip("実例  目標10")
        target = self._mix(
            self.ja_text("対象", font_size=22),
            MathTex(r"\{3,1,7,2\}", font_size=30),
            self.ja_text("、目標", font_size=22),
            MathTex(r"10", font_size=30),
        )
        self.below_chip(target, chip)
        self.play(FadeIn(target), run_time=0.4)
        self.wait(1.0)
        count = VGroup(
            self.ja_text("探す。各箱は使う／使わないの2択。", font_size=22, color=ORANGE),
            MathTex(r"2\cdot 2\cdot 2\cdot 2=16", font_size=30),
        ).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        self.stack_below(count, target, buff=0.24)
        for row in count:
            self.play(FadeIn(row), run_time=0.35)
            self.wait(1.0)
        path = VGroup(
            self.ja_text("当たりの一つ。", font_size=22),
            MathTex(r"3\ \mathrm{yes},\ 1\ \mathrm{no},\ 7\ \mathrm{yes}", font_size=28),
            MathTex(r"3+7=10", font_size=30, color=YELLOW),
        ).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        self.stack_below(path, count, buff=0.22)
        for row in path:
            self.play(FadeIn(row), run_time=0.35)
            self.wait(0.95)
        self.play(FadeOut(VGroup(count, path)), run_time=0.3)
        verify = VGroup(
            self.ja_text("確認する。証拠は 3 と 7。", font_size=22, color=BLUE),
            self.ja_text("3 は配列にある。7 は配列にある。", font_size=22),
            MathTex(r"3+7=10", font_size=30, color=YELLOW),
            self.ja_text("はい。", font_size=24),
        ).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        self.stack_below(verify, target, buff=0.24)
        for row in verify:
            self.play(FadeIn(row), run_time=0.35)
            self.wait(0.95)
        self.play(FadeOut(verify), run_time=0.3)
        table = self.aligned_table(
            [
                [
                    self.ja_text("やり方", font_size=20, color=GREY_B),
                    self.ja_text("仕事の目安", font_size=20, color=GREY_B),
                    self.ja_text("クラス", font_size=20, color=GREY_B),
                ],
                [
                    self.ja_text("全探索で探す", font_size=20, color=ORANGE),
                    MathTex(r"2^{n}", font_size=26, color=ORANGE),
                    self.ja_text("この手順は P ではない", font_size=20),
                ],
                [
                    self.ja_text("証拠を確認", font_size=20, color=BLUE),
                    MathTex(r"O(n)", font_size=26, color=BLUE),
                    self.ja_text("NP の確認側", font_size=20),
                ],
            ],
            h_buff=0.38,
            v_buff=0.18,
        )
        table.scale(0.88)
        self.stack_below(table, target, buff=0.28)
        table.set_x(0)
        self.reveal_table(table, row_wait=0.95)
        cap = self._caption("同じ問いでも、探す仕事と確認の仕事は違う。P と NP は、その違いの入れ物。")
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.7)
        self.wipe(self.header)

    def summary(self):
        chip = self._chip("まとめ")
        items = VGroup(
            self.ja_text("1. P は多項式時間で解ける。", font_size=24),
            self.ja_text("2. NP は証拠の確認が多項式時間。", font_size=24),
            self._line("3. ", MathTex(r"P\subseteq NP", font_size=28), "。同じかどうかは未解決。NP完全はいちばん硬い層。", font_size=22),
        ).arrange(DOWN, buff=0.32, aligned_edge=LEFT)
        self.below_chip(items, chip, buff=0.45)
        for row in items:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.35)
        cap = self._caption("「確認は速い。探すのは速いか分からない」。それが P と NP の入り口。")
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.6)
        self.wipe(self.header)

    def next_preview(self):
        chip = self._chip("次回")
        nxt = self.ja_text("#11 配列とリスト", font_size=32, color=YELLOW)
        self.below_chip(nxt, chip, buff=0.5)
        self.play(FadeIn(nxt), run_time=0.45)
        self.wait(1.15)
        body = VGroup(
            self.ja_text("今回で、計算量の導入は一段落。", font_size=26),
            self.ja_text("次回から箱の並べ方に入る。", font_size=26),
            self.ja_text("配列とリストで、取り出しと挿入の速さを比べる。", font_size=26),
        ).arrange(DOWN, buff=0.26, aligned_edge=LEFT)
        self.stack_below(body, nxt, buff=0.4)
        for row in body:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.15)
        self.wait(1.3)
