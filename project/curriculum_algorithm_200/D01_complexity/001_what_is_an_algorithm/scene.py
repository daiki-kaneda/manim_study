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
    """#1 アルゴリズムとは何か（約7分）"""

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
        self.linger("次回予告", extra=0.4)

    def part_hook(self):
        cards = self._fit(self._array(VALUES)).shift(UP * 0.55)
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.2) for c in cards], lag_ratio=0.2), run_time=1.6)
        q = self._stack(
            "この5つの数のうち、",
            "いちばん大きい数はどれでしょう。",
            size=30,
        )
        q.next_to(cards, DOWN, buff=0.45)
        self._reveal(q)
        self.play(Indicate(cards[3], color=YELLOW), run_time=0.9)
        self.linger("いちばん大きい数はどれでしょう。", extra=0.3)

        easy = self.ja_text("5個なら、目で見てわかります。", font_size=28)
        easy.next_to(q, DOWN, buff=0.35)
        self._reveal(easy)
        self.wipe(self.title)
        many = self._long_row()
        many.shift(UP * 0.35)
        hard = self._stack(
            "100個だと、目で追うのは大変です。",
            "だから、誰でも同じ答えに着く手順が要ります。",
            size=28,
        )
        hard.next_to(many, DOWN, buff=0.4)
        self.play(FadeIn(many), run_time=0.8)
        self._reveal(hard)

    def part_goal(self):
        self.wipe(self.title)
        lead = self.ja_text("今日おさえることは、つぎの4つです。", font_size=30)
        lead.to_edge(UP, buff=1.1)
        self._reveal(lead)
        items = [
            "1. アルゴリズムが何を指すか",
            "2. アルゴリズムが満たしてほしい性質",
            "3. ことば・流れ図・擬似コードでの書き方",
            "4. 小さな例を、最初から最後まで自分でたどること",
        ]
        group = VGroup(*[self.ja_text(line, font_size=28) for line in items])
        group.arrange(DOWN, aligned_edge=LEFT, buff=0.34)
        group.next_to(lead, DOWN, buff=0.5)
        self._fit(group, 12.6)
        for t in group:
            self.play(FadeIn(t, shift=RIGHT * 0.12), run_time=0.45)
            self.linger(t.text if hasattr(t, "text") else items[0], extra=0.15)

    def part_overview(self):
        self.wipe(self.title)
        boxes = VGroup(
            self._named_box("入力", BLUE),
            self._named_box("決まった手順", YELLOW),
            self._named_box("出力", GREEN),
        )
        boxes.arrange(RIGHT, buff=1.2).shift(UP * 1.2)
        self._fit(boxes, 12.8)
        arrows = VGroup(
            Arrow(boxes[0].get_right(), boxes[1].get_left(), buff=0.1, color=WHITE),
            Arrow(boxes[1].get_right(), boxes[2].get_left(), buff=0.1, color=WHITE),
        )
        self.play(FadeIn(boxes[0]), run_time=0.5)
        self.linger("入力")
        self.play(GrowArrow(arrows[0]), FadeIn(boxes[1]), run_time=0.7)
        self.linger("決まった手順")
        self.play(GrowArrow(arrows[1]), FadeIn(boxes[2]), run_time=0.7)
        self.linger("出力")
        explain = self._stack(
            "アルゴリズムは、入力を受け取って、",
            "決まった手順で処理して、出力を出します。",
            "今日は、この箱の中身を一つずつ見ていきます。",
            size=28,
        ).next_to(boxes, DOWN, buff=0.42)
        self._reveal(explain)
        path = self._stack(
            "STEP 1 定義  →  STEP 2 性質  →  STEP 3 書き方",
            "→  STEP 4 なぜ大事か  →  実例",
            size=24,
        ).next_to(explain, DOWN, buff=0.32)
        self._reveal(path)

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
        for i, text in enumerate(lines):
            t = self.ja_text(text, font_size=28)
            if i == 0:
                t.next_to(label, DOWN, buff=0.4).align_to(label, LEFT)
            else:
                t.next_to(shown[-1], DOWN, buff=0.24).align_to(shown[0], LEFT)
            self._fit_left(t)
            self.play(FadeIn(t), run_time=0.5)
            shown.add(t)
            self.linger(text)

        self.wipe(self.title, label)
        left = VGroup(
            self.ja_text("料理のレシピ", font_size=26, color=ORANGE),
            self._stack("塩少々", "弱火でしばらく", "味見して調整してよい", size=26),
        ).arrange(DOWN, buff=0.22)
        right = VGroup(
            self.ja_text("アルゴリズム", font_size=26, color=GREEN),
            self._stack("量があいまい", "終わりの条件があいまい", "各ステップは一つに決まる", size=26),
        ).arrange(DOWN, buff=0.22)
        cols = VGroup(left, right).arrange(RIGHT, buff=1.5, aligned_edge=UP)
        cols.next_to(label, DOWN, buff=0.45)
        self._fit(cols, 12.6)
        cols.set_x(0)
        self.play(FadeIn(left), run_time=0.6)
        self.linger("塩少々。弱火でしばらく。")
        self.play(FadeIn(right), run_time=0.6)
        self.linger("各ステップは一つに決まる")
        note = self._stack(
            "レシピは上手な省略が許されます。",
            "アルゴリズムでは、次に何をするかが",
            "一つに決まる必要があります。",
            size=26,
        ).to_edge(DOWN, buff=0.32)
        self._reveal(note)

        self.wipe(self.title, label)
        recap_title = self.ja_text("いまのところ、こう押さえます。", font_size=28)
        recap_title.next_to(label, DOWN, buff=0.4).align_to(label, LEFT)
        recap_lines = [
            "・問題がある",
            "・入力がある",
            "・有限個の明確な手順がある",
            "・出力が出て、そこで終わる",
        ]
        recap = self._stack(*recap_lines, size=30)
        recap.next_to(recap_title, DOWN, buff=0.32).align_to(recap_title, LEFT)
        self._reveal(recap_title)
        for line, src in zip(recap, recap_lines):
            self.play(FadeIn(line), run_time=0.4)
            self.linger(src)

    def part_step2(self):
        self.wipe(self.title)
        label = self._step_chip("STEP 2  性質")
        self.play(FadeIn(label), run_time=0.4)
        props = [
            ("1. 有限性", ["いつかは必ず終わります。", "無限に回り続ける手順は、アルゴリズムとは呼びません。"]),
            ("2. 明確性", ["各ステップの意味が一つに決まります。", "「うまくやる」だけでは手順になりません。"]),
            ("3. 入力と出力", ["何を受け取り、何を返すかが決まっています。"]),
            ("4. 有効性", ["各ステップは、紙と鉛筆でも実行できる具体的な操作です。"]),
        ]
        block = VGroup()
        for name, descs in props:
            head = self.ja_text(name, font_size=28, color=YELLOW)
            body = self._stack(*descs, size=24)
            block.add(VGroup(head, body).arrange(DOWN, aligned_edge=LEFT, buff=0.08))
        block.arrange(DOWN, aligned_edge=LEFT, buff=0.26)
        block.next_to(label, DOWN, buff=0.3).align_to(label, LEFT)
        self._fit_left(block)
        for pair, (_name, descs) in zip(block, props):
            self.play(FadeIn(pair), run_time=0.5)
            self.linger("".join(descs))

        self.wipe(self.title, label)
        bad_a = self.ja_text("悪い例 A   終わりの条件がない", font_size=28, color=RED)
        bad_a.next_to(label, DOWN, buff=0.35)
        self._reveal(bad_a)
        counter = self.ja_text("1", font_size=64)
        how = self.ja_text("1 を足して、また 1 を足して…", font_size=28)
        how.next_to(counter, DOWN, buff=0.45)
        self.play(FadeIn(counter), FadeIn(how), run_time=0.5)
        self.linger("1")
        for nxt in ("2", "3", "4"):
            nxt_t = self.ja_text(nxt, font_size=64).move_to(counter)
            self.play(Transform(counter, nxt_t), run_time=0.55)
            self.linger(nxt, extra=0.15)
        fail = self._stack(
            "終わりの条件がないので、この先もずっと続きます。",
            "これは有限性を満たしません。",
            size=28,
        ).to_edge(DOWN, buff=0.4)
        fail[-1].set_color(RED)
        self._reveal(fail)

        self.wipe(self.title, label)
        bad_b = self.ja_text("悪い例 B   指示があいまい", font_size=28, color=RED)
        bad_b.next_to(label, DOWN, buff=0.35)
        vague = self.ja_text("「大きな数を、うまく探してください。」", font_size=32)
        vague.shift(UP * 0.1)
        why = self._stack(
            "大きいの基準も、探す順番も書いてありません。",
            "これは明確性を満たしません。",
            size=28,
        ).to_edge(DOWN, buff=0.42)
        why[-1].set_color(RED)
        self._reveal(bad_b)
        self._reveal(vague)
        self._reveal(why)

        self.wipe(self.title, label)
        good = self.ja_text("同じ問題の、よい書き方", font_size=28, color=GREEN)
        good.next_to(label, DOWN, buff=0.4)
        good_body = self._stack(
            "左端から順に見て、",
            "今までの最大より大きければ書き換える。",
            "終わり方と、各ステップが決まっています。",
            size=30,
        )
        good_body.next_to(good, DOWN, buff=0.4)
        self._reveal(good)
        for line in good_body:
            self.play(FadeIn(line), run_time=0.45)
            self.linger(getattr(line, "text", "よい書き方"))

    def part_step3(self):
        self.wipe(self.title)
        label = self._step_chip("STEP 3  書き方")
        self.play(FadeIn(label), run_time=0.4)
        intro = self._stack(
            "同じ「いちばん大きい数を探す」を、",
            "3通りの書き方で見てみます。",
            size=28,
        )
        intro.next_to(label, DOWN, buff=0.35)
        cards = self._fit(self._array(VALUES, side=0.9, font_size=32))
        cards.next_to(intro, DOWN, buff=0.4)
        cards.set_x(0)
        self.play(FadeIn(intro), run_time=0.5)
        self.linger("3通りの書き方で見てみます。")
        self.play(FadeIn(cards), run_time=0.6)
        self.linger("3 7 2 9 4")

        self.wipe(self.title, label)
        way1 = self.ja_text("書き方 1   ことば", font_size=28, color=YELLOW)
        way1.next_to(label, DOWN, buff=0.28).align_to(label, LEFT)
        words = [
            "いちばん左の数を、候補にする。",
            "左から2番目から、右端まで順番に見る。",
            "今見ている数が候補より大きければ、",
            "候補をその数に書き換える。",
            "全部見終わったら、候補を答えとして出す。",
            "この列なら、答えは 9 になる。各比較はあとで一つずつ開きます。",
        ]
        self.play(FadeIn(way1), run_time=0.4)
        shown = VGroup()
        for i, text in enumerate(words):
            t = self.ja_text(text, font_size=26)
            if i == 0:
                t.next_to(way1, DOWN, buff=0.28).align_to(way1, LEFT)
            else:
                t.next_to(shown[-1], DOWN, buff=0.18).align_to(shown[0], LEFT)
            self._fit_left(t)
            self.play(FadeIn(t), run_time=0.4)
            shown.add(t)
            self.linger(text)

        self.wipe(self.title, label)
        way2 = self.ja_text("書き方 2   流れ図", font_size=28, color=YELLOW)
        way2.next_to(label, DOWN, buff=0.2).align_to(label, LEFT)
        self.play(FadeIn(way2), run_time=0.35)
        flow = self._build_flowchart()
        flow.scale(0.78).next_to(way2, DOWN, buff=0.12)
        flow.set_x(0)
        nodes, arrows = flow.nodes, flow.arrows
        self.play(FadeIn(nodes[0]), run_time=0.4)
        self.linger("はじめる")
        self.play(GrowArrow(arrows[0]), FadeIn(nodes[1]), run_time=0.55)
        self.linger("左端を候補にする")
        self.play(GrowArrow(arrows[1]), FadeIn(nodes[2]), run_time=0.55)
        self.linger("まだ見ていない数がある？")
        self.play(GrowArrow(arrows[2]), FadeIn(nodes[3]), FadeIn(nodes[7]), run_time=0.55)
        self.linger("いいえ")
        self.play(GrowArrow(arrows[3]), FadeIn(nodes[4]), run_time=0.5)
        self.linger("おわる")
        self.play(GrowArrow(arrows[4]), FadeIn(nodes[5]), FadeIn(nodes[8]), run_time=0.55)
        self.linger("はい。その数は候補より大きい？")
        self.play(GrowArrow(arrows[5]), FadeIn(nodes[6]), FadeIn(nodes[9]), run_time=0.55)
        self.linger("はい。候補を書き換える")
        self.play(Create(arrows[6]), FadeIn(nodes[10]), run_time=0.65)
        self.linger("次の数へ戻る")

        self.wipe(self.title, label)
        way3 = self.ja_text("書き方 3   擬似コード", font_size=28, color=YELLOW)
        way3.next_to(label, DOWN, buff=0.3).align_to(label, LEFT)
        self.play(FadeIn(way3), run_time=0.4)
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
            t.shift(RIGHT * 0.42 * indent)
            code.add(t)
        code.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        code.next_to(way3, DOWN, buff=0.35).align_to(way3, LEFT).shift(RIGHT * 0.1)
        for t, (_ind, text) in zip(code, code_lines):
            self.play(FadeIn(t), run_time=0.4)
            self.linger(text)
        close = self.ja_text("書き方が違っても、やっている操作は同じです。", font_size=28)
        close.to_edge(DOWN, buff=0.38)
        self._reveal(close)

    def part_step4(self):
        self.wipe(self.title)
        label = self._step_chip("STEP 4  なぜ大事か")
        self.play(FadeIn(label), run_time=0.4)

        messy_h = self.ja_text("場当たり", font_size=26, color=RED)
        neat_h = self.ja_text("左から順", font_size=26, color=GREEN)
        messy_cards = self._fit(self._array(VALUES, side=0.72, font_size=26), 6.2)
        neat_cards = self._fit(self._array(VALUES, side=0.72, font_size=26), 6.2)
        messy = VGroup(messy_h, messy_cards).arrange(DOWN, buff=0.18)
        neat = VGroup(neat_h, neat_cards).arrange(DOWN, buff=0.18)
        cols = VGroup(messy, neat).arrange(DOWN, buff=0.55, aligned_edge=LEFT)
        cols.next_to(label, DOWN, buff=0.35)
        cols.set_x(0)
        self.play(FadeIn(cols), run_time=0.7)
        self.linger("場当たりと、左から順")

        for idx in (0, 3, 1, 0, 4):
            self.play(Indicate(messy_cards[idx], color=ORANGE), run_time=0.42)
        miss = self.ja_text("同じカードを二度見たり、見落としたりします。", font_size=24)
        miss.next_to(cols, DOWN, buff=0.28)
        self._reveal(miss)
        for cell in neat_cards:
            self.play(Indicate(cell, color=GREEN), run_time=0.36)
        neat_n = self.ja_text("各カードを、一度だけ見ます。", font_size=24)
        neat_n.next_to(miss, DOWN, buff=0.18)
        self._reveal(neat_n)

        self.wipe(self.title, label)
        five = self.ja_text("5個なら、どちらでもなんとかなることが多いです。", font_size=28)
        five.next_to(label, DOWN, buff=0.35)
        small = self._fit(self._array(VALUES, side=0.78, font_size=28))
        small.next_to(five, DOWN, buff=0.3)
        small.set_x(0)
        self._reveal(five)
        self.play(FadeIn(small), run_time=0.55)
        self.linger("5個")
        many = self._long_row()
        many.next_to(small, DOWN, buff=0.4)
        hundred = self._stack(
            "100個だと、場当たりでは見落としが増えます。",
            "同じ手順でも、手間の大きさは入力の大きさで変わります。",
            "正しさだけでなく、手間も比べたくなります。",
            "それが次の回の話です。",
            size=26,
        ).to_edge(DOWN, buff=0.28)
        self.play(FadeIn(many), run_time=0.75)
        self._reveal(hundred)

    def part_example(self):
        self.wipe(self.title)
        label = self._step_chip("実例  最大値を探す")
        self.play(FadeIn(label), run_time=0.4)
        cards = self._fit(self._array(VALUES, side=1.15, font_size=40), 8.6)
        cards.move_to(UP * 1.35 + LEFT * 0.7)
        cand_box = RoundedRectangle(width=1.55, height=1.35, corner_radius=0.12, color=ORANGE, stroke_width=3)
        cand_title = self.ja_text("候補", font_size=22, color=ORANGE)
        cand_val = self.ja_text("？", font_size=38)
        cand_val.move_to(cand_box)
        cand_title.next_to(cand_box, UP, buff=0.1)
        cand = VGroup(cand_box, cand_title, cand_val)
        cand.next_to(cards, RIGHT, buff=0.55)
        self.play(FadeIn(cards), FadeIn(cand), run_time=0.75)
        self.linger("候補はまだ空です")

        history = VGroup()

        def add_history(text, color=WHITE):
            t = self.ja_text(text, font_size=20, color=color)
            if len(history) == 0:
                t.next_to(cand, DOWN, buff=0.28).align_to(cand, LEFT)
            else:
                t.next_to(history[-1], DOWN, buff=0.08).align_to(history[0], LEFT)
            history.add(t)
            self.play(FadeIn(t), run_time=0.28)

        def set_cand(num):
            nxt = self.ja_text(str(num), font_size=38).move_to(cand_box)
            self.play(Transform(cand_val, nxt), run_time=0.5)

        def paint(index, color):
            self.play(cards[index][0].animate.set_color(color), run_time=0.28)

        note = self.ja_text("最初の候補は、いちばん左の 3 です。", font_size=26)
        note.to_edge(DOWN, buff=0.28)
        self.play(FadeIn(note), run_time=0.45)
        paint(0, ORANGE)
        set_cand(3)
        add_history("候補を 3 にする")
        self.linger(note.text if hasattr(note, "text") else "最初の候補は 3")

        steps = [
            (1, 7, 3, True, "7 は 3 より大きい", "候補を 7 に書き換える"),
            (2, 2, 7, False, "2 は 7 より小さい", "候補はそのまま 7"),
            (3, 9, 7, True, "9 は 7 より大きい", "候補を 9 に書き換える"),
            (4, 4, 9, False, "4 は 9 より小さい", "候補はそのまま 9"),
        ]
        for idx, seen, prev, bigger, cmp_text, action in steps:
            self.play(FadeOut(note), run_time=0.2)
            paint(idx, YELLOW)
            left_n = self._mini_cell(seen, YELLOW).next_to(cards, DOWN, buff=0.55).shift(LEFT * 0.85)
            right_n = self._mini_cell(prev, ORANGE).next_to(left_n, RIGHT, buff=1.15)
            vs = self.ja_text("と", font_size=26).move_to((left_n.get_center() + right_n.get_center()) / 2)
            note = self.ja_text(f"{seen} と {prev} を比べます。", font_size=26)
            note.to_edge(DOWN, buff=0.28)
            self.play(FadeIn(left_n), FadeIn(vs), FadeIn(right_n), FadeIn(note), run_time=0.55)
            self.linger(f"{seen} と {prev} を比べます。")
            cmp = self.ja_text(cmp_text, font_size=28, color=YELLOW)
            cmp.next_to(note, UP, buff=0.16)
            self.play(FadeIn(cmp), run_time=0.4)
            self.linger(cmp_text)
            act = self.ja_text(action, font_size=26, color=GREEN if bigger else WHITE)
            act.next_to(cmp, UP, buff=0.1)
            self.play(FadeIn(act), run_time=0.35)
            self.linger(action)
            if bigger:
                set_cand(seen)
                paint(idx, ORANGE)
            else:
                paint(idx, BLUE)
            add_history(cmp_text, YELLOW if bigger else WHITE)
            self.play(FadeOut(left_n), FadeOut(vs), FadeOut(right_n), FadeOut(cmp), FadeOut(act), run_time=0.3)

        self.play(FadeOut(note), run_time=0.2)
        fin = self._stack(
            "もう見る数がないので、終わりです。",
            "答えは、候補の 9 です。",
            size=30,
        ).to_edge(DOWN, buff=0.28)
        self.play(FadeIn(fin), run_time=0.55)
        self.play(Indicate(cards[3], color=YELLOW), Indicate(cand, color=YELLOW), run_time=1.0)
        add_history("答えは 9", GREEN)
        self.linger("答えは、候補の 9 です。", extra=0.4)

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
                t.next_to(label, DOWN, buff=0.42).align_to(label, LEFT)
            else:
                t.next_to(shown[-1], DOWN, buff=0.28).align_to(shown[0], LEFT)
            self._fit_left(t)
            self.play(FadeIn(t), run_time=0.45)
            shown.add(t)
            self.linger(text)

    def part_next(self):
        nxt = self._stack(
            "次回は、この手順の手間を数える方法を見ます。",
            "タイトルは「計算量とビッグO記法」です。",
            size=28,
        )
        nxt.to_edge(DOWN, buff=0.38)
        self._reveal(nxt)

    def _reveal(self, mob):
        self.play(FadeIn(mob), run_time=0.55)
        texts = []
        for m in mob.get_family():
            if hasattr(m, "text") and isinstance(m.text, str) and m.text:
                texts.append(m.text)
        self.linger("".join(texts) if texts else " ")

    def _step_chip(self, text):
        t = self.ja_text(text, font_size=24, color=YELLOW)
        t.to_edge(UP, buff=1.02).to_edge(LEFT, buff=0.4)
        return t

    def _stack(self, *lines, size=28):
        group = VGroup(*[self.ja_text(line, font_size=size) for line in lines])
        group.arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        return group

    def _named_box(self, text, color):
        box = RoundedRectangle(width=3.0, height=1.25, corner_radius=0.14, color=color, stroke_width=3)
        label = self.ja_text(text, font_size=28)
        label.move_to(box)
        return VGroup(box, label)

    def _array(self, values, side=1.1, font_size=38):
        cells = VGroup()
        for value in values:
            box = RoundedRectangle(width=side, height=side, corner_radius=0.12, color=BLUE, stroke_width=3)
            label = self.ja_text(str(value), font_size=font_size)
            label.move_to(box)
            cells.add(VGroup(box, label))
        cells.arrange(RIGHT, buff=0.16)
        return cells

    def _mini_cell(self, value, color):
        box = RoundedRectangle(width=0.95, height=0.95, corner_radius=0.1, color=color, stroke_width=3)
        label = self.ja_text(str(value), font_size=34)
        label.move_to(box)
        return VGroup(box, label)

    def _long_row(self):
        vals = [3, 1, 8, 2, 6, 0, 0, 0, 0, 0, 0, 0, 4, 9]
        row = self._array(vals, side=0.48, font_size=16)
        for cell, val in zip(row, vals):
            if val == 0:
                cell[1].become(self.ja_text("・", font_size=16).move_to(cell[0]))
        return self._fit(row, 12.4)

    def _fit(self, mob, max_w=12.4):
        if mob.width > max_w:
            mob.scale_to_fit_width(max_w)
        return mob

    def _fit_left(self, mob, max_w=12.2):
        left = mob.get_left()
        self._fit(mob, max_w)
        mob.shift(left - mob.get_left())
        return mob

    def _flow_node(self, text, width, height, color=BLUE):
        box = RoundedRectangle(width=width, height=height, corner_radius=0.1, color=color, stroke_width=2)
        label = self.ja_text(text, font_size=18)
        if label.width > width - 0.2:
            label.scale_to_fit_width(width - 0.25)
        label.move_to(box)
        return VGroup(box, label)

    def _build_flowchart(self):
        start = self._flow_node("はじめる", 2.1, 0.5, GREEN)
        init = self._flow_node("左端を候補にする", 3.3, 0.5, BLUE)
        remain = self._flow_node("まだ見ていない数がある？", 4.3, 0.5, YELLOW)
        out = self._flow_node("候補を答えにする", 3.0, 0.5, GREEN)
        end = self._flow_node("おわる", 1.9, 0.48, GREEN)
        bigger = self._flow_node("その数は候補より大きい？", 4.3, 0.5, YELLOW)
        update = self._flow_node("候補を書き換える", 3.0, 0.5, ORANGE)

        start.shift(UP * 2.05)
        init.next_to(start, DOWN, buff=0.22)
        remain.next_to(init, DOWN, buff=0.22)
        bigger.next_to(remain, DOWN, buff=0.32)
        update.next_to(bigger, DOWN, buff=0.22)
        out.next_to(remain, RIGHT, buff=0.45)
        end.next_to(out, DOWN, buff=0.22)

        a0 = Arrow(start.get_bottom(), init.get_top(), buff=0.04, stroke_width=3)
        a1 = Arrow(init.get_bottom(), remain.get_top(), buff=0.04, stroke_width=3)
        a2 = Arrow(remain.get_right(), out.get_left(), buff=0.04, stroke_width=3)
        a3 = Arrow(out.get_bottom(), end.get_top(), buff=0.04, stroke_width=3)
        a4 = Arrow(remain.get_bottom(), bigger.get_top(), buff=0.04, stroke_width=3)
        a5 = Arrow(bigger.get_bottom(), update.get_top(), buff=0.04, stroke_width=3)
        a6 = Arrow(
            update.get_left() + LEFT * 0.02,
            remain.get_left() + LEFT * 0.02,
            path_arc=2.1,
            buff=0.06,
            stroke_width=3,
        )

        no_lbl = self.ja_text("いいえ", font_size=16, color=RED).next_to(a2, UP, buff=0.03)
        yes_lbl = self.ja_text("はい", font_size=16, color=GREEN).next_to(a4, RIGHT, buff=0.05)
        yes2 = self.ja_text("はい", font_size=16, color=GREEN).next_to(a5, RIGHT, buff=0.05)
        back = self.ja_text("次の数へ", font_size=16).next_to(a6, LEFT, buff=0.06)

        nodes = VGroup(start, init, remain, out, end, bigger, update, no_lbl, yes_lbl, yes2, back)
        arrows = VGroup(a0, a1, a2, a3, a4, a5, a6)
        group = VGroup(nodes, arrows)
        group.nodes = nodes
        group.arrows = arrows
        return group
