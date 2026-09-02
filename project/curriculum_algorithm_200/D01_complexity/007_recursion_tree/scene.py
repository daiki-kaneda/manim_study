from pathlib import Path
import sys

_D01 = Path(__file__).resolve().parent.parent
if str(_D01) not in sys.path:
    sys.path.insert(0, str(_D01))

from manim import *
from curriculum_scene import CurriculumScene


class RecursionTree(CurriculumScene):
    """#7 再帰木による計算量の見積もり（約9分）"""

    header_text = "#7  再帰木による計算量の見積もり"

    def construct(self):
        self.header = self._open_header()
        self.hook()
        self._show_goals(
            [
                "再帰木は、呼び出しをノード、子呼び出しを枝で描いた図。",
                "同じ段の仕事を足すと、よく同じ値になる。",
                "段数と、1段の仕事を掛けて、全体の T(n) を見積もる。",
            ]
        )
        self._show_overview(
            [
                "STEP 1 … 漸化式 T(n)=2T(n/2)+n を木にする",
                "STEP 2 … 各ノードの仕事を書き、段で足す",
                "STEP 3 … 半分にすると、段数は log_{2} n くらい",
                "STEP 4 … 段の合計 × 段数 で T(n) を出す",
            ],
            ["最後に n=8 の木を、根から葉まで15ノード全部通す。"],
        )
        self.step1_draw()
        self.step2_levels()
        self.step3_log()
        self.step4_sum()
        self.worked_example()
        self.summary()
        self.next_preview()

    def _node(self, text, radius=0.28, color=BLUE, font_size=22):
        circ = Circle(radius=radius, color=color, stroke_width=2, fill_opacity=0.15)
        lab = MathTex(str(text), font_size=font_size)
        lab.move_to(circ)
        g = VGroup(circ, lab)
        return g

    def _tree_positions(self):
        # 15 nodes, n=8 complete binary tree. y from 1.55 down to -2.05
        ys = [1.45, 0.55, -0.4, -1.4]
        xs = [
            [0],
            [-2.15, 2.15],
            [-3.25, -1.05, 1.05, 3.25],
            [-4.05, -2.9, -1.75, -0.6, 0.6, 1.75, 2.9, 4.05],
        ]
        vals = [[8], [4, 4], [2, 2, 2, 2], [1, 1, 1, 1, 1, 1, 1, 1]]
        nodes = []
        for y, xrow, vrow in zip(ys, xs, vals):
            level = []
            for x, v in zip(xrow, vrow):
                n = self._node(v, radius=0.26 if v > 1 else 0.22)
                n.move_to([x, y, 0])
                level.append(n)
            nodes.append(level)
        return nodes

    def _edges_for(self, levels):
        edges = VGroup()
        parents = [(0, 0, 1, 0), (0, 0, 1, 1)]
        parents += [(1, 0, 2, 0), (1, 0, 2, 1), (1, 1, 2, 2), (1, 1, 2, 3)]
        parents += [
            (2, 0, 3, 0), (2, 0, 3, 1),
            (2, 1, 3, 2), (2, 1, 3, 3),
            (2, 2, 3, 4), (2, 2, 3, 5),
            (2, 3, 3, 6), (2, 3, 3, 7),
        ]
        for a, i, b, j in parents:
            line = Line(
                levels[a][i].get_bottom(),
                levels[b][j].get_top(),
                color=GREY_B,
                stroke_width=1.5,
            )
            edges.add(line)
        return edges, parents

    def hook(self):
        q = self.ja_text("一度に2つ呼び出すと、一本道ではなく、枝が分かれる。", font_size=28)
        q.next_to(self.header, DOWN, buff=0.36)
        self.play(FadeIn(q), run_time=0.55)
        self.wait(1.3)
        boxes = self._boxes([1, 2, 3, 4, 5, 6, 7, 8], side=0.55, font_size=22)
        boxes.next_to(q, DOWN, buff=0.28)
        boxes.set_x(0)
        self.play(FadeIn(boxes), run_time=0.5)
        work = self.ja_text("自分の段で、箱の個数ぶんの仕事（8 回）。", font_size=22)
        work.next_to(boxes, DOWN, buff=0.2)
        self.play(FadeIn(work), run_time=0.35)
        self.wait(1.1)
        root = self._node(8, radius=0.32)
        root.next_to(work, DOWN, buff=0.35)
        left = self._node(4)
        right = self._node(4)
        kids = VGroup(left, right).arrange(RIGHT, buff=2.4)
        kids.next_to(root, DOWN, buff=0.55)
        e1 = Line(root.get_bottom(), left.get_top(), color=GREY_B)
        e2 = Line(root.get_bottom(), right.get_top(), color=GREY_B)
        self.play(FadeIn(root), run_time=0.35)
        self.play(Create(e1), Create(e2), FadeIn(left), FadeIn(right), run_time=0.6)
        self.wait(1.2)
        cap = self._caption("前回の sum は子が1つだった。今日は子が2つ。仕事の数え方を、木でやる。")
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.6)
        self._clear(VGroup(q, boxes, work, root, left, right, e1, e2, cap))

    def step1_draw(self):
        chip = self._chip("STEP 1  木に描く")
        lead = self.ja_text("入力 n のとき、自分で n 回仕事をして、半分の問題を2つ出す。", font_size=24)
        self.below_chip(lead, chip)
        self.play(FadeIn(lead), run_time=0.4)
        self.wait(1.15)
        rows = VGroup(
            self._mix(self.ja_text("ベース:", font_size=22), MathTex(r"T(1)=\Theta(1)", font_size=28)),
            self._mix(MathTex(r"n>1:", font_size=26), MathTex(r"T(n)=2T(n/2)+n", font_size=30)),
            self.ja_text("「2T(n/2)」が左右の子、「+n」が自分の仕事。", font_size=22),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        rows.next_to(lead, DOWN, buff=0.28)
        for row in rows:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.05)
        root = self._node(8, radius=0.32)
        left = self._node(4)
        right = self._node(4)
        root.next_to(rows, DOWN, buff=0.4)
        kids = VGroup(left, right).arrange(RIGHT, buff=2.2)
        kids.next_to(root, DOWN, buff=0.5)
        e1 = Line(root.get_bottom(), left.get_top(), color=GREY_B)
        e2 = Line(root.get_bottom(), right.get_top(), color=GREY_B)
        self.play(FadeIn(root), run_time=0.3)
        self.play(Create(e1), FadeIn(left), Create(e2), FadeIn(right), run_time=0.55)
        self.wait(1.1)
        definition = self.ja_text("再帰木は、1回の呼び出しを1つのノードにし、その中の再帰呼び出しを子ノードにした図。", font_size=20, color=YELLOW)
        definition.to_edge(DOWN, buff=0.2)
        self.play(FadeIn(definition), run_time=0.45)
        self.linger(3.4)
        cap = self._caption("木を先に描く。式の意味が、親子の形になる。")
        self.play(FadeOut(definition), FadeIn(cap), run_time=0.4)
        self.wait(1.5)
        self.wipe(self.header)

    def step2_levels(self):
        chip = self._chip("STEP 2  段の合計")
        levels = self._tree_positions()
        edges, _ = self._edges_for(levels)
        # shift tree down a bit under chip
        tree = VGroup(*[n for lv in levels for n in lv], *edges)
        tree.shift(DOWN * 0.15)
        sums = [
            MathTex(r"8", font_size=24, color=YELLOW),
            MathTex(r"4+4=8", font_size=24, color=YELLOW),
            MathTex(r"2+2+2+2=8", font_size=24, color=YELLOW),
            MathTex(r"1\times 8=8", font_size=24, color=YELLOW),
        ]
        self.play(FadeIn(levels[0][0]), run_time=0.35)
        sums[0].next_to(levels[0][0], RIGHT, buff=0.55)
        self.play(FadeIn(sums[0]), run_time=0.3)
        self.wait(0.85)
        for li in range(1, 4):
            parent_edges = [e for e, p in zip(edges, [
                (0, 0, 1, 0), (0, 0, 1, 1),
                (1, 0, 2, 0), (1, 0, 2, 1), (1, 1, 2, 2), (1, 1, 2, 3),
                (2, 0, 3, 0), (2, 0, 3, 1), (2, 1, 3, 2), (2, 1, 3, 3),
                (2, 2, 3, 4), (2, 2, 3, 5), (2, 3, 3, 6), (2, 3, 3, 7),
            ]) if p[2] == li]
            self.play(*[Create(e) for e in parent_edges], *[FadeIn(n) for n in levels[li]], run_time=0.55)
            sums[li].next_to(VGroup(*levels[li]), RIGHT, buff=0.25)
            self.play(FadeIn(sums[li]), run_time=0.3)
            self.wait(0.9)
        definition = self.ja_text("この木では、どの段の仕事の合計も n。今はどれも 8。", font_size=22, color=YELLOW)
        definition.to_edge(DOWN, buff=0.2)
        self.play(FadeIn(definition), run_time=0.45)
        self.linger(3.3)
        cap = self._caption("枝が2つに分かれるかわりに、1つのノードの仕事は半分。段の合計は n のまま。")
        self.play(FadeOut(definition), FadeIn(cap), run_time=0.4)
        self.wait(1.5)
        self.wipe(self.header)

    def step3_log(self):
        chip = self._chip("STEP 3  段数")
        lead = self.ja_text("n が半分、半分と減って 1 になると、葉に着く。", font_size=26)
        self.below_chip(lead, chip)
        self.play(FadeIn(lead), run_time=0.4)
        self.wait(1.15)
        rows = self._formula_rows(
            [
                MathTex(r"8", font_size=32),
                MathTex(r"4=8/2", font_size=30),
                MathTex(r"2=8/4", font_size=30),
                MathTex(r"1=8/8", font_size=30),
                MathTex(r"8=2^3", font_size=32),
                self._mix(self.ja_text("半分にする回数は", font_size=22), MathTex(r"3", font_size=28)),
                self._mix(self.ja_text("段の個数は", font_size=22), MathTex(r"3+1=4", font_size=28)),
                MathTex(r"k=\log_2 n,\quad k+1=\log_2 n+1", font_size=28),
                MathTex(r"n=8:\ \log_2 8+1=4", font_size=30, color=YELLOW),
            ],
            chip,
            buff=0.32,
        )
        cap = self._caption("半分ずつなら、段数は対数。n が2倍になると、段が1つ増える。")
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.6)
        self.wipe(self.header)

    def step4_sum(self):
        chip = self._chip("STEP 4  全部足す")
        lead = self.ja_text("全体の仕事は、段の合計を、段の個数ぶん足したもの。", font_size=24)
        self.below_chip(lead, chip)
        self.play(FadeIn(lead), run_time=0.4)
        self.wait(1.15)
        rows = self._formula_rows(
            [
                self._mix(self.ja_text("1段の合計は", font_size=22), MathTex(r"n", font_size=30)),
                self._mix(self.ja_text("段の個数は", font_size=22), MathTex(r"\log_2 n+1", font_size=30)),
                MathTex(r"T(n)=n\cdot(\log_2 n+1)", font_size=32),
                MathTex(r"=n\log_2 n+n", font_size=32),
                self._mix(self.ja_text("大きい項は", font_size=22), MathTex(r"n\log_2 n", font_size=30)),
                MathTex(r"T(n)=\Theta(n\log n)", font_size=34, color=YELLOW),
                MathTex(r"n=8:\ 8\cdot(3+1)=32", font_size=30),
                MathTex(r"8+8+8+8=32", font_size=30),
            ],
            chip,
            buff=0.28,
        )
        definition = self.ja_text("再帰木では、段の合計 × 段数 で T(n) を見積もる。今日は Θ(n log n)。", font_size=22, color=YELLOW)
        definition.to_edge(DOWN, buff=0.2)
        self.play(FadeIn(definition), run_time=0.45)
        self.linger(3.4)
        cap = self._caption("次回のマスター定理は、この足し算を場合分けして一気に出す道具。今日は手で足す。")
        self.play(FadeOut(definition), FadeIn(cap), run_time=0.4)
        self.wait(1.6)
        self.wipe(self.header)

    def worked_example(self):
        chip = self._chip("実例  n=8")
        levels = self._tree_positions()
        edges, parents = self._edges_for(levels)
        tree = VGroup(*[n for lv in levels for n in lv], *edges)
        tree.shift(DOWN * 0.2)
        total = self.ja_text("累計  0", font_size=22)
        total.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(total), run_time=0.25)
        running = 0
        order = []
        # root
        order.append((None, levels[0][0], 8))
        for a, i, b, j in parents:
            val = [8, 4, 2, 1][b]
            edge_idx = list(parents).index((a, i, b, j))
            order.append((edges[edge_idx], levels[b][j], val))
        for edge, node, val in order:
            anims = [FadeIn(node)]
            if edge is not None:
                anims.insert(0, Create(edge))
            self.play(*anims, run_time=0.28)
            running += val
            nxt = self.ja_text(f"累計  {running}", font_size=22)
            nxt.move_to(total)
            self.play(Transform(total, nxt), run_time=0.2)
            self.wait(0.35)
        self.wait(0.6)
        self.play(FadeOut(tree), FadeOut(total), FadeOut(chip), run_time=0.35)
        chip = self._chip("実例  n=8")
        table = self.aligned_table(
            [
                [
                    self.ja_text("段", font_size=20, color=GREY_B),
                    self.ja_text("ノード数", font_size=20, color=GREY_B),
                    self.ja_text("1ノード", font_size=20, color=GREY_B),
                    self.ja_text("段の合計", font_size=20, color=GREY_B),
                ],
                [MathTex(r"0", font_size=24), MathTex(r"1", font_size=24), MathTex(r"8", font_size=24), MathTex(r"8", font_size=24)],
                [MathTex(r"1", font_size=24), MathTex(r"2", font_size=24), MathTex(r"4", font_size=24), MathTex(r"8", font_size=24)],
                [MathTex(r"2", font_size=24), MathTex(r"4", font_size=24), MathTex(r"2", font_size=24), MathTex(r"8", font_size=24)],
                [MathTex(r"3", font_size=24), MathTex(r"8", font_size=24), MathTex(r"1", font_size=24), MathTex(r"8", font_size=24)],
                [self.ja_text("計", font_size=22), MathTex(r"15", font_size=24), self.ja_text(" ", font_size=20), MathTex(r"32", font_size=24, color=YELLOW)],
            ],
            h_buff=0.4,
            v_buff=0.16,
        )
        table.scale(0.88)
        self.below_chip(table, chip, buff=0.32)
        table.set_x(0)
        self.reveal_table(table, row_wait=0.8)
        cap = self._caption("15 個の呼び出し、仕事の合計 32。n log_{2} n + n = 8·3+8=32。")
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.7)
        self.wipe(self.header)

    def summary(self):
        chip = self._chip("まとめ")
        items = VGroup(
            self.ja_text("1. 再帰木は、呼び出しを親子で描いた図。", font_size=24),
            self.ja_text("2. 段の合計が同じなら、T(n) は（1段の仕事）×（段数）。", font_size=24),
            self._mix(self.ja_text("3.", font_size=24), MathTex(r"T(n)=2T(n/2)+n", font_size=28), self.ja_text("は", font_size=24), MathTex(r"\Theta(n\log n)", font_size=28, color=YELLOW)),
        ).arrange(DOWN, buff=0.32, aligned_edge=LEFT)
        self.below_chip(items, chip, buff=0.45)
        for row in items:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.35)
        cap = self._caption("枝が分かれたら、ノードを数え飛ばさず、段で束ねて足す。")
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.6)
        self.wipe(self.header)

    def next_preview(self):
        chip = self._chip("次回")
        nxt = self.ja_text("#8 マスター定理", font_size=32, color=YELLOW)
        self.below_chip(nxt, chip, buff=0.5)
        self.play(FadeIn(nxt), run_time=0.45)
        self.wait(1.15)
        body = VGroup(
            self.ja_text("今日は T(n)=2T(n/2)+n を手で足した。", font_size=26),
            self.ja_text("次回は、子の個数と、自分の仕事の増え方が変わっても、", font_size=26),
            self.ja_text("同じ見積もりを場合分けで出す。", font_size=26),
        ).arrange(DOWN, buff=0.26, aligned_edge=LEFT)
        body.next_to(nxt, DOWN, buff=0.4)
        body.align_to(nxt, LEFT)
        for row in body:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.15)
        self.wait(1.3)
