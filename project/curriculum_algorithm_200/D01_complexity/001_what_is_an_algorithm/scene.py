from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import LessonScene


VALUES = [3, 7, 2, 9, 4]


class WhatIsAnAlgorithm(LessonScene):
    """#1 アルゴリズムとは何か（約8分）"""

    def construct(self):
        self.title = self.show_heading("アルゴリズムとは何か")
        self.part_hook()
        self.part_goal()
        self.part_overview()
        self.part_step1()
        self.part_step2()
        self.part_step3()
        self.part_step4()
        self.part_example()
        self.part_summary()
        self.part_next()
        self.read(1.2)

    def part_hook(self):
        cards = self._array(VALUES).shift(UP * 0.35)
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.2) for c in cards], lag_ratio=0.18), run_time=1.4)
        q = self._stack(
            "この5つの数のうち、",
            "いちばん大きい数はどれでしょう。",
            font_size=30,
        ).next_to(cards, DOWN, buff=0.55)
        self.play(FadeIn(q), run_time=0.7)
        self.read(1.0)
        self.play(Indicate(cards[3], color=YELLOW), run_time=0.8)
        self.read(0.7)
        self.hook_cards = cards
        self.hook_q = q

    def part_goal(self):
        self.wipe(self.title)
        lead = self.ja_text("今日おさえることは、つぎの4つです。", font_size=30)
        lead.to_edge(UP, buff=1.05)
        self.play(FadeIn(lead), run_time=0.55)
        self.read(0.6)
        items = [
            "1. アルゴリズムが何を指すか",
            "2. アルゴリズムが満たしてほしい性質",
            "3. ことば・流れ図・擬似コードでの書き方",
            "4. 小さな例を、最初から最後まで自分でたどること",
        ]
        group = VGroup()
        for i, line in enumerate(items):
            t = self.ja_text(line, font_size=28)
            group.add(t)
        group.arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        group.next_to(lead, DOWN, buff=0.45)
        for t in group:
            self.play(FadeIn(t, shift=RIGHT * 0.15), run_time=0.45)
            self.read(0.55)
        self.read(0.5)

    def part_overview(self):
        self.wipe(self.title)
        boxes = VGroup(
            self._named_box("入力", BLUE),
            self._named_box("決まった手順", YELLOW),
            self._named_box("出力", GREEN),
        )
        boxes.arrange(RIGHT, buff=1.35).shift(UP * 1.15)
        arrows = VGroup(
            Arrow(boxes[0].get_right(), boxes[1].get_left(), buff=0.12, color=WHITE),
            Arrow(boxes[1].get_right(), boxes[2].get_left(), buff=0.12, color=WHITE),
        )
        self.play(FadeIn(boxes[0]), run_time=0.45)
        self.play(GrowArrow(arrows[0]), FadeIn(boxes[1]), run_time=0.6)
        self.play(GrowArrow(arrows[1]), FadeIn(boxes[2]), run_time=0.6)
        explain = self._stack(
            "アルゴリズムは、入力を受け取って、",
            "決まった手順で処理して、出力を出します。",
            "今日は、この箱の中身を一つずつ見ていきます。",
            font_size=28,
        ).next_to(boxes, DOWN, buff=0.4)
        self.play(FadeIn(explain), run_time=0.65)
        self.read(1.0)
        path = self._stack(
            "STEP 1 定義  →  STEP 2 性質  →  STEP 3 書き方",
            "→  STEP 4 なぜ大事か  →  実例",
            font_size=24,
        )
        path.next_to(explain, DOWN, buff=0.32)
        self.play(FadeIn(path), run_time=0.55)
        self.read(0.9)

    def part_step1(self):
        self.wipe(self.title)
        label = self._step_chip("STEP 1  定義")
        self.play(FadeIn(label), run_time=0.4)
        lines = [
            "アルゴリズムは、問題を解くための手順です。",
            "ただし、なんとなくのやり方ではありません。",
            "有限個の、はっきりしたステップを、順番に実行します。",
            "同じ入力なら、誰がやっても同じ結果になります。",
        ]
        shown = VGroup()
        anchor = label.get_bottom() + DOWN * 0.35
        for i, text in enumerate(lines):
            t = self.ja_text(text, font_size=28)
            if i == 0:
                t.next_to(label, DOWN, buff=0.35).align_to(label, LEFT)
            else:
                t.next_to(shown[-1], DOWN, buff=0.22).align_to(shown[0], LEFT)
            self.play(FadeIn(t), run_time=0.45)
            shown.add(t)
            self.read(0.7)
        self.read(0.4)
        self.wipe(self.title, label)
        left_title = self.ja_text("料理のレシピ", font_size=26, color=ORANGE)
        right_title = self.ja_text("アルゴリズム", font_size=26, color=GREEN)
        left_body = self._stack("塩少々", "弱火でしばらく", "味見して調整してよい", font_size=26)
        right_body = self._stack("量があいまい", "終わりの条件があいまい", "各ステップは一つに決まる", font_size=26)
        left = VGroup(left_title, left_body).arrange(DOWN, buff=0.25)
        right = VGroup(right_title, right_body).arrange(DOWN, buff=0.25)
        cols = VGroup(left, right).arrange(RIGHT, buff=1.4, aligned_edge=UP)
        cols.next_to(label, DOWN, buff=0.4)
        self.play(FadeIn(left), run_time=0.55)
        self.read(0.6)
        self.play(FadeIn(right), run_time=0.55)
        self.read(0.7)
        note = self._stack(
            "レシピは上手な省略が許されます。",
            "アルゴリズムでは、次に何をするかが",
            "一つに決まる必要があります。",
            font_size=26,
        ).to_edge(DOWN, buff=0.32)
        self.play(FadeIn(note), run_time=0.55)
        self.read(1.0)
        self.wipe(self.title, label)
        recap_title = self.ja_text("いまのところ、こう押さえます。", font_size=28)
        recap_title.next_to(label, DOWN, buff=0.4).align_to(label, LEFT)
        recap = self._stack(
            "・問題がある",
            "・入力がある",
            "・有限個の明確な手順がある",
            "・出力が出て、そこで終わる",
            font_size=28,
        )
        recap.next_to(recap_title, DOWN, buff=0.3).align_to(recap_title, LEFT)
        self.play(FadeIn(recap_title), run_time=0.4)
        for line in recap:
            self.play(FadeIn(line), run_time=0.35)
            self.read(0.45)
        self.read(0.6)

    def part_step2(self):
        self.wipe(self.title)
        label = self._step_chip("STEP 2  性質")
        self.play(FadeIn(label), run_time=0.4)
        props = [
            (
                "1. 有限性",
                ["いつかは必ず終わります。", "無限に回り続ける手順は、アルゴリズムとは呼びません。"],
            ),
            (
                "2. 明確性",
                ["各ステップの意味が一つに決まります。", "「うまくやる」だけでは手順になりません。"],
            ),
            ("3. 入力と出力", ["何を受け取り、何を返すかが決まっています。"]),
            ("4. 有効性", ["各ステップは、紙と鉛筆でも実行できる具体的な操作です。"]),
        ]
        block = VGroup()
        for name, descs in props:
            head = self.ja_text(name, font_size=28, color=YELLOW)
            body = self._stack(*descs, font_size=24)
            pair = VGroup(head, body).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
            block.add(pair)
        block.arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        block.next_to(label, DOWN, buff=0.32).align_to(label, LEFT)
        for pair in block:
            self.play(FadeIn(pair), run_time=0.45)
            self.read(0.85)
        self.read(0.4)

        self.wipe(self.title, label)
        bad_a = self.ja_text("悪い例 A   終わりの条件がない", font_size=28, color=RED)
        bad_a.next_to(label, DOWN, buff=0.35)
        self.play(FadeIn(bad_a), run_time=0.4)
        counter = self.ja_text("1", font_size=64)
        counter.shift(UP * 0.15)
        self.play(FadeIn(counter), run_time=0.4)
        self.read(0.4)
        for nxt in ("2", "3"):
            nxt_t = self.ja_text(nxt, font_size=64).move_to(counter)
            self.play(Transform(counter, nxt_t), run_time=0.55)
            self.read(0.35)
        dots = self.ja_text("この先も、ずっと続きます。", font_size=28)
        dots.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(dots), run_time=0.45)
        mark = self.ja_text("これは有限性を満たしません。", font_size=28, color=RED)
        mark.next_to(dots, UP, buff=0.25)
        self.play(FadeIn(mark), run_time=0.45)
        self.read(0.9)

        self.wipe(self.title, label)
        bad_b = self.ja_text("悪い例 B   指示があいまい", font_size=28, color=RED)
        bad_b.next_to(label, DOWN, buff=0.35)
        vague = self.ja_text("「大きな数を、うまく探してください。」", font_size=32)
        vague.shift(UP * 0.15)
        why = self._stack(
            "大きいの基準も、探す順番も書いてありません。",
            "これは明確性を満たしません。",
            font_size=28,
        ).to_edge(DOWN, buff=0.45)
        why[-1].set_color(RED)
        self.play(FadeIn(bad_b), run_time=0.4)
        self.play(FadeIn(vague), run_time=0.5)
        self.read(0.7)
        self.play(FadeIn(why), run_time=0.5)
        self.read(0.9)

        self.wipe(self.title, label)
        good = self.ja_text("同じ問題の、よい書き方", font_size=28, color=GREEN)
        good.next_to(label, DOWN, buff=0.35)
        good_body = self._stack(
            "左端から順に見て、",
            "今までの最大より大きければ書き換える。",
            "終わり方と、各ステップが決まっています。",
            font_size=30,
        )
        good_body.next_to(good, DOWN, buff=0.4)
        self.play(FadeIn(good), run_time=0.4)
        for line in good_body:
            self.play(FadeIn(line), run_time=0.4)
            self.read(0.5)
        self.read(0.5)

    def part_step3(self):
        self.wipe(self.title)
        label = self._step_chip("STEP 3  書き方")
        self.play(FadeIn(label), run_time=0.4)
        intro = self._stack(
            "同じ「いちばん大きい数を探す」を、",
            "3通りの書き方で見てみます。",
            font_size=28,
        ).next_to(label, DOWN, buff=0.3)
        cards = self._array(VALUES, side=0.85, font_size=30).next_to(intro, DOWN, buff=0.35)
        self.play(FadeIn(intro), FadeIn(cards), run_time=0.7)
        self.read(0.8)

        self.wipe(self.title, label)
        way1 = self.ja_text("書き方 1   ことば", font_size=28, color=YELLOW)
        way1.next_to(label, DOWN, buff=0.3).align_to(label, LEFT)
        words = [
            "いちばん左の数を、候補にする。",
            "左から2番目から、右端まで順番に見る。",
            "今見ている数が候補より大きければ、",
            "候補をその数に書き換える。",
            "全部見終わったら、候補を答えとして出す。",
            "この列なら、答えは 9 になる。各比較はあとで一つずつ開きます。",
        ]
        shown = VGroup()
        self.play(FadeIn(way1), run_time=0.35)
        for i, text in enumerate(words):
            t = self.ja_text(text, font_size=26)
            if i == 0:
                t.next_to(way1, DOWN, buff=0.3).align_to(way1, LEFT)
            else:
                t.next_to(shown[-1], DOWN, buff=0.2).align_to(shown[0], LEFT)
            self.play(FadeIn(t), run_time=0.4)
            shown.add(t)
            self.read(0.65)

        self.wipe(self.title, label)
        way2 = self.ja_text("書き方 2   流れ図", font_size=28, color=YELLOW)
        way2.next_to(label, DOWN, buff=0.22).align_to(label, LEFT)
        self.play(FadeIn(way2), run_time=0.35)
        flow = self._build_flowchart()
        flow.scale(0.84).next_to(way2, DOWN, buff=0.18)
        flow.set_x(0)
        nodes = flow.nodes
        arrows = flow.arrows
        self.play(FadeIn(nodes[0]), run_time=0.35)
        self.play(GrowArrow(arrows[0]), FadeIn(nodes[1]), run_time=0.5)
        self.play(GrowArrow(arrows[1]), FadeIn(nodes[2]), run_time=0.5)
        self.read(0.45)
        self.play(GrowArrow(arrows[2]), FadeIn(nodes[3]), run_time=0.5)
        self.play(GrowArrow(arrows[3]), FadeIn(nodes[4]), run_time=0.45)
        self.read(0.45)
        self.play(GrowArrow(arrows[4]), FadeIn(nodes[5]), run_time=0.5)
        self.play(GrowArrow(arrows[5]), run_time=0.4)
        self.play(Create(arrows[6]), run_time=0.55)
        self.read(0.9)

        self.wipe(self.title, label)
        way3 = self.ja_text("書き方 3   擬似コード", font_size=28, color=YELLOW)
        way3.next_to(label, DOWN, buff=0.3).align_to(label, LEFT)
        self.play(FadeIn(way3), run_time=0.35)
        code_lines = [
            (0, "候補を、列の左端にする"),
            (0, "i を、左から2番目から右端まで動かす"),
            (1, "もし 列の i 番目が候補より大きいなら"),
            (2, "候補を、その数に書き換える"),
            (0, "答えを、候補にする"),
        ]
        code = VGroup()
        for indent, text in code_lines:
            t = self.ja_text(text, font_size=28)
            t.shift(RIGHT * 0.45 * indent)
            code.add(t)
        code.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        code.next_to(way3, DOWN, buff=0.35).align_to(way3, LEFT).shift(RIGHT * 0.15)
        for t in code:
            self.play(FadeIn(t), run_time=0.4)
            self.read(0.5)
        close = self.ja_text("書き方が違っても、やっている操作は同じです。", font_size=28)
        close.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(close), run_time=0.5)
        self.read(0.9)

    def part_step4(self):
        self.wipe(self.title)
        label = self._step_chip("STEP 4  なぜ大事か")
        self.play(FadeIn(label), run_time=0.4)
        left_h = self.ja_text("場当たり", font_size=26, color=RED)
        right_h = self.ja_text("左から順", font_size=26, color=GREEN)
        left_cards = self._array(VALUES, side=0.8, font_size=28)
        right_cards = self._array(VALUES, side=0.8, font_size=28)
        left_col = VGroup(left_h, left_cards).arrange(DOWN, buff=0.25)
        right_col = VGroup(right_h, right_cards).arrange(DOWN, buff=0.25)
        cols = VGroup(left_col, right_col).arrange(RIGHT, buff=1.3)
        cols.next_to(label, DOWN, buff=0.45)
        self.play(FadeIn(cols), run_time=0.6)
        self.read(0.5)

        messy_order = [0, 3, 1, 0, 4]
        for idx in messy_order:
            self.play(Indicate(left_cards[idx], color=ORANGE), run_time=0.4)
        miss = self.ja_text("同じカードを二度見たり、見落としたりします。", font_size=24)
        miss.next_to(left_col, DOWN, buff=0.25)
        self.play(FadeIn(miss), run_time=0.4)
        self.read(0.6)
        for cell in right_cards:
            self.play(Indicate(cell, color=GREEN), run_time=0.32)
        neat = self.ja_text("各カードを、一度だけ見ます。", font_size=24)
        neat.next_to(right_col, DOWN, buff=0.25)
        self.play(FadeIn(neat), run_time=0.4)
        self.read(0.8)

        self.wipe(self.title, label)
        five = self.ja_text("5個なら、どちらでもなんとかなることが多いです。", font_size=28)
        five.next_to(label, DOWN, buff=0.4)
        small = self._array(VALUES, side=0.75, font_size=26).next_to(five, DOWN, buff=0.35)
        self.play(FadeIn(five), FadeIn(small), run_time=0.6)
        self.read(0.7)
        many_vals = [1, 4, 8, 2, 6] + [0] * 7 + [9]
        many = self._array(many_vals, side=0.52, font_size=18)
        for cell, val in zip(many, many_vals):
            if val == 0:
                cell[1].become(self.ja_text("・", font_size=18).move_to(cell[0]))
        many.next_to(small, DOWN, buff=0.45)
        hundred = self._stack(
            "100個だと、場当たりでは見落としが増えます。",
            "同じ手順でも、手間の大きさは入力の大きさで変わります。",
            font_size=26,
        ).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(many), run_time=0.7)
        self.play(FadeIn(hundred), run_time=0.55)
        self.read(1.1)
        bridge = self._stack(
            "正しさだけでなく、手間も比べたくなります。",
            "それが次の回の話です。",
            font_size=26,
        )
        bridge.next_to(hundred, UP, buff=0.18)
        self.play(FadeIn(bridge), run_time=0.5)
        self.read(0.9)

    def part_example(self):
        self.wipe(self.title)
        label = self._step_chip("実例  最大値を探す")
        self.play(FadeIn(label), run_time=0.4)
        cards = self._array(VALUES, side=1.2, font_size=42)
        cards.shift(UP * 0.85)
        cand_box = RoundedRectangle(width=1.7, height=1.5, corner_radius=0.14, color=ORANGE, stroke_width=3)
        cand_title = self.ja_text("候補", font_size=22, color=ORANGE)
        cand_val = self.ja_text("？", font_size=40)
        cand_val.move_to(cand_box.get_center())
        cand_title.next_to(cand_box, UP, buff=0.12)
        cand = VGroup(cand_box, cand_title, cand_val)
        cand.next_to(cards, RIGHT, buff=0.7).shift(UP * 0.05)
        self.play(FadeIn(cards), FadeIn(cand), run_time=0.7)
        self.read(0.5)

        history = VGroup()
        history_anchor = LEFT * 5.7 + UP * 0.15

        def add_history(text, color=WHITE):
            t = self.ja_text(text, font_size=22, color=color)
            if len(history) == 0:
                t.move_to(history_anchor)
                t.align_to(history_anchor, LEFT)
            else:
                t.next_to(history[-1], DOWN, buff=0.1).align_to(history[0], LEFT)
            history.add(t)
            self.play(FadeIn(t), run_time=0.3)

        def set_cand(num):
            nxt = self.ja_text(str(num), font_size=40).move_to(cand_box.get_center())
            self.play(Transform(cand_val, nxt), run_time=0.45)

        def paint(index, color):
            self.play(cards[index][0].animate.set_color(color), run_time=0.3)

        # 1. 左端を候補に
        note = self.ja_text("最初の候補は、いちばん左の 3 です。", font_size=28)
        note.to_edge(DOWN, buff=0.35)
        self.play(FadeIn(note), run_time=0.4)
        paint(0, ORANGE)
        set_cand(3)
        add_history("候補を 3 にする")
        self.read(0.7)

        steps = [
            (1, 7, 3, True, "7 は 3 より大きい", "候補を 7 に書き換える"),
            (2, 2, 7, False, "2 は 7 より小さい", "候補はそのまま 7"),
            (3, 9, 7, True, "9 は 7 より大きい", "候補を 9 に書き換える"),
            (4, 4, 9, False, "4 は 9 より小さい", "候補はそのまま 9"),
        ]
        cand_now = 3
        for idx, seen, prev, bigger, cmp_text, action in steps:
            self.play(FadeOut(note), run_time=0.25)
            paint(idx, YELLOW)
            note = self.ja_text(f"{seen} と {prev} を比べます。", font_size=28)
            note.to_edge(DOWN, buff=0.35)
            self.play(FadeIn(note), run_time=0.4)
            self.read(0.55)
            cmp = self.ja_text(cmp_text, font_size=28)
            cmp.next_to(note, UP, buff=0.18)
            self.play(FadeIn(cmp), run_time=0.4)
            self.read(0.55)
            act = self.ja_text(action, font_size=26, color=GREEN if bigger else WHITE)
            act.next_to(cmp, UP, buff=0.12)
            self.play(FadeIn(act), run_time=0.35)
            if bigger:
                cand_now = seen
                set_cand(cand_now)
                paint(idx, ORANGE)
            else:
                paint(idx, BLUE)
            add_history(cmp_text, YELLOW if bigger else WHITE)
            self.read(0.55)
            self.play(FadeOut(cmp), FadeOut(act), run_time=0.25)

        self.play(FadeOut(note), run_time=0.25)
        fin = self._stack(
            "もう見る数がないので、終わりです。",
            "答えは、候補の 9 です。",
            font_size=30,
        ).to_edge(DOWN, buff=0.3)
        self.play(FadeIn(fin), run_time=0.55)
        self.play(
            Indicate(cards[3], color=YELLOW),
            Indicate(cand, color=YELLOW),
            run_time=0.9,
        )
        add_history("答えは 9")
        self.read(1.1)

    def part_summary(self):
        self.wipe(self.title)
        label = self._step_chip("まとめ")
        self.play(FadeIn(label), run_time=0.35)
        lines = [
            "アルゴリズムは、問題を解く有限で明確な手順です。",
            "有限性・明確性・入出力・有効性を満たしてほしい、",
            "というのが今日の性質です。",
            "ことば、流れ図、擬似コードは、同じ手順の別の書き方です。",
            "最大値の例では、左から順に比べて、候補を書き換えていきました。",
        ]
        shown = VGroup()
        for i, text in enumerate(lines):
            t = self.ja_text(text, font_size=26)
            if i == 0:
                t.next_to(label, DOWN, buff=0.45).align_to(label, LEFT)
            else:
                t.next_to(shown[-1], DOWN, buff=0.32).align_to(shown[0], LEFT)
            self.play(FadeIn(t), run_time=0.45)
            shown.add(t)
            self.read(0.75)
        self.summary_lines = shown
        self.summary_label = label

    def part_next(self):
        nxt = self._stack(
            "次回は、この手順の手間を数える方法を見ます。",
            "タイトルは「計算量とビッグO記法」です。",
            font_size=28,
        )
        nxt.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(nxt), run_time=0.6)
        self.read(1.1)

    def _step_chip(self, text):
        t = self.ja_text(text, font_size=24, color=YELLOW)
        t.to_edge(UP, buff=1.0).to_edge(LEFT, buff=0.45)
        return t

    def _stack(self, *lines, font_size=28):
        group = VGroup(*[self.ja_text(line, font_size=font_size) for line in lines])
        group.arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        return group

    def _named_box(self, text, color):
        box = RoundedRectangle(width=3.1, height=1.35, corner_radius=0.16, color=color, stroke_width=3)
        label = self.ja_text(text, font_size=30)
        label.move_to(box.get_center())
        return VGroup(box, label)

    def _array(self, values, side=1.15, font_size=40):
        cells = VGroup()
        for value in values:
            box = RoundedRectangle(
                width=side,
                height=side,
                corner_radius=0.12,
                color=BLUE,
                stroke_width=3,
            )
            label = self.ja_text(str(value), font_size=font_size)
            label.move_to(box.get_center())
            cells.add(VGroup(box, label))
        cells.arrange(RIGHT, buff=0.18)
        return cells

    def _flow_node(self, text, width, height, color=BLUE):
        box = RoundedRectangle(width=width, height=height, corner_radius=0.1, color=color, stroke_width=2)
        label = self.ja_text(text, font_size=20)
        label.move_to(box.get_center())
        return VGroup(box, label)

    def _build_flowchart(self):
        start = self._flow_node("はじめる", 2.2, 0.55, GREEN)
        init = self._flow_node("左端を候補にする", 3.4, 0.55, BLUE)
        remain = self._flow_node("まだ見ていない数がある？", 4.4, 0.55, YELLOW)
        out = self._flow_node("候補を答えにする", 3.2, 0.55, GREEN)
        end = self._flow_node("おわる", 2.0, 0.5, GREEN)
        bigger = self._flow_node("その数は候補より大きい？", 4.4, 0.55, YELLOW)
        update = self._flow_node("候補を書き換える", 3.2, 0.55, ORANGE)

        start.shift(UP * 2.15)
        init.next_to(start, DOWN, buff=0.28)
        remain.next_to(init, DOWN, buff=0.28)
        bigger.next_to(remain, DOWN, buff=0.38)
        update.next_to(bigger, DOWN, buff=0.28)
        out.next_to(remain, RIGHT, buff=0.55)
        end.next_to(out, DOWN, buff=0.28)

        a0 = Arrow(start.get_bottom(), init.get_top(), buff=0.05, stroke_width=3)
        a1 = Arrow(init.get_bottom(), remain.get_top(), buff=0.05, stroke_width=3)
        a2 = Arrow(remain.get_right(), out.get_left(), buff=0.05, stroke_width=3)
        a3 = Arrow(out.get_bottom(), end.get_top(), buff=0.05, stroke_width=3)
        a4 = Arrow(remain.get_bottom(), bigger.get_top(), buff=0.05, stroke_width=3)
        a5 = Arrow(bigger.get_bottom(), update.get_top(), buff=0.05, stroke_width=3)
        a6 = ArcBetweenPoints(
            update.get_left() + LEFT * 0.05,
            remain.get_left() + LEFT * 0.05,
            angle=1.4,
        )
        a6.add_tip()

        no_lbl = self.ja_text("いいえ", font_size=18, color=RED).next_to(a2, UP, buff=0.04)
        yes_lbl = self.ja_text("はい", font_size=18, color=GREEN).next_to(a4, RIGHT, buff=0.06)
        yes2 = self.ja_text("はい", font_size=18, color=GREEN).next_to(a5, RIGHT, buff=0.06)
        back = self.ja_text("次の数へ", font_size=18).next_to(a6, LEFT, buff=0.08)

        nodes = VGroup(start, init, remain, out, end, bigger, update, no_lbl, yes_lbl, yes2, back)
        arrows = VGroup(a0, a1, a2, a3, a4, a5, a6)
        group = VGroup(nodes, arrows)
        group.nodes = nodes
        group.arrows = arrows
        return group
