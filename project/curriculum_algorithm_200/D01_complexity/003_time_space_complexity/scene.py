from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import LessonScene


HOOK_VALUES = [2, 5, 1, 4]
STEP4_VALUES = [3, 1, 3]
EXAMPLE_VALUES = [4, 1, 4, 2]


class TimeSpaceComplexity(LessonScene):
    """#3 時間計算量と空間計算量（約9分）"""

    def wait(self, duration=1.0, **kwargs):
        if duration >= 1.0:
            duration *= 1.9
        elif duration >= 0.7:
            duration *= 1.4
        return super().wait(duration, **kwargs)

    def construct(self):
        self.header = self._open_header()
        self.hook()
        self.today_goal()
        self.overview()
        self.step1_time()
        self.step2_space()
        self.step3_extra()
        self.step4_tradeoff()
        self.worked_example()
        self.summary()
        self.next_preview()

    def _open_header(self):
        title = self.ja_text("#3  時間計算量と空間計算量", font_size=40)
        self.play(FadeIn(title), run_time=0.8)
        self.wait(0.7)
        self.play(title.animate.scale(0.55).to_edge(UP, buff=0.16), run_time=0.5)
        return title

    def _clear(self, group):
        if group is None:
            return
        self.play(FadeOut(group), run_time=0.4)

    def _caption(self, *lines, font_size=24):
        parts = VGroup(*[self.ja_text(line, font_size=font_size) for line in lines])
        parts.arrange(DOWN, buff=0.08)
        parts.to_edge(DOWN, buff=0.18)
        parts.set_x(0)
        return parts

    def _boxes(self, values, side=0.72, color=BLUE, font_size=30):
        group = VGroup()
        for value in values:
            sq = Square(side_length=side, color=color, stroke_width=2)
            lab = MathTex(str(value), font_size=font_size)
            group.add(VGroup(sq, lab))
        group.arrange(RIGHT, buff=0.16)
        return group

    def _index_labels(self, boxes):
        labels = VGroup()
        for i, box in enumerate(boxes, start=1):
            lab = MathTex(str(i), font_size=22, color=GREY_B)
            lab.next_to(box, DOWN, buff=0.1)
            labels.add(lab)
        return labels

    def _sum_cell(self, value="0", color=YELLOW):
        box = RoundedRectangle(
            width=1.35,
            height=1.05,
            corner_radius=0.1,
            color=color,
            stroke_width=3,
            fill_color=color,
            fill_opacity=0.18,
        )
        title = self.ja_text("合計", font_size=20, color=color)
        title.next_to(box, UP, buff=0.08)
        lab = MathTex(str(value), font_size=34)
        lab.move_to(box)
        return VGroup(box, title, lab)

    def _set_sum(self, cell, value):
        nxt = MathTex(str(value), font_size=34).move_to(cell[0])
        self.play(Transform(cell[2], nxt), run_time=0.35)

    def _mark_row(self, n=4):
        cells = VGroup()
        fills = []
        for i in range(1, n + 1):
            sq = Square(side_length=0.7, color=GREY_B, stroke_width=2)
            off = self.ja_text("オフ", font_size=16, color=GREY_B)
            off.move_to(sq)
            name = MathTex(str(i), font_size=22, color=GREY_B)
            name.next_to(sq, UP, buff=0.08)
            cell = VGroup(sq, off, name)
            cells.add(cell)
            fills.append(off)
        cells.arrange(RIGHT, buff=0.22)
        return cells, fills

    def _turn_on(self, cell, fill_slot):
        on = self.ja_text("オン", font_size=16, color=GREEN)
        on.move_to(cell[0])
        self.play(
            cell[0].animate.set_color(GREEN),
            Transform(fill_slot, on),
            run_time=0.35,
        )

    def _chip(self, text):
        label = self.step_label(text)
        self.play(FadeIn(label), run_time=0.4)
        return label

    def _program_card(self, title, body, extra, color):
        box = RoundedRectangle(
            width=5.5,
            height=2.2,
            corner_radius=0.12,
            color=color,
            stroke_width=3,
            fill_color=color,
            fill_opacity=0.18,
        )
        t = self.ja_text(title, font_size=26, color=color)
        b = self.ja_text(body, font_size=22)
        e = self.ja_text(extra, font_size=22, color=color)
        col = VGroup(t, b, e).arrange(DOWN, buff=0.14)
        col.move_to(box.get_center())
        return VGroup(box, col)

    def hook(self):
        question = self.ja_text(
            "答えは同じなのに、メモリの使い方が全然違うことがある。",
            font_size=28,
        )
        question.next_to(self.header, DOWN, buff=0.4)
        self.play(FadeIn(question), run_time=0.6)
        self.wait(1.4)

        src = self._boxes(HOOK_VALUES)
        src.next_to(question, DOWN, buff=0.32)
        src.set_x(0)
        src_name = self.ja_text("入力", font_size=22, color=GREY_B)
        src_name.next_to(src, LEFT, buff=0.22)
        self.play(FadeIn(src), FadeIn(src_name), run_time=0.5)
        self.wait(0.9)

        card_a = self._program_card(
            "手順A",
            "その場で、順番に足していく",
            "追加は合計用の 1 マス",
            BLUE,
        )
        card_b = self._program_card(
            "手順B",
            "先にコピーしてから、コピーを足す",
            "追加はコピー n マス＋合計 1 マス",
            ORANGE,
        )
        cards = VGroup(card_a, card_b).arrange(RIGHT, buff=0.45)
        cards.next_to(src, DOWN, buff=0.32)
        cards.set_x(0)
        self.play(FadeIn(card_a, shift=LEFT * 0.15), FadeIn(card_b, shift=RIGHT * 0.15), run_time=0.8)
        self.wait(1.4)

        self.play(FadeOut(cards), run_time=0.35)

        walk_title = self.ja_text("手順A  その場で足す", font_size=24, color=BLUE)
        walk_title.next_to(src, DOWN, buff=0.35)
        sum_a = self._sum_cell("0", BLUE)
        sum_a.next_to(walk_title, DOWN, buff=0.28)
        self.play(FadeIn(walk_title), FadeIn(sum_a), run_time=0.45)

        running = 0
        for i, value in enumerate(HOOK_VALUES):
            running += value
            self.play(Indicate(src[i], color=YELLOW), run_time=0.4)
            eq = MathTex(rf"{running - value}+{value}={running}", font_size=30)
            eq.next_to(sum_a, RIGHT, buff=0.35)
            extra_note = self.ja_text("追加は 1 マスのまま", font_size=22)
            extra_note.next_to(sum_a, DOWN, buff=0.22)
            self.play(FadeIn(eq), FadeIn(extra_note), run_time=0.3)
            self._set_sum(sum_a, running)
            self.wait(0.85)
            self.play(FadeOut(eq), FadeOut(extra_note), run_time=0.2)

        ans_a = self.ja_text("答えは 12。追加は最後まで 1 マス。", font_size=24, color=BLUE)
        ans_a.to_edge(DOWN, buff=0.22)
        self.play(FadeIn(ans_a), run_time=0.4)
        self.wait(1.3)

        self.play(FadeOut(walk_title), FadeOut(sum_a), FadeOut(ans_a), run_time=0.35)
        walk_b = self.ja_text("手順B  先にコピーする", font_size=24, color=ORANGE)
        walk_b.next_to(src, DOWN, buff=0.32)
        copy = self._boxes(HOOK_VALUES, color=ORANGE)
        copy.next_to(walk_b, DOWN, buff=0.28)
        copy.set_x(0)
        copy_name = self.ja_text("コピー", font_size=22, color=ORANGE)
        copy_name.next_to(copy, LEFT, buff=0.18)
        self.play(FadeIn(walk_b), FadeIn(copy_name), run_time=0.35)
        for i in range(len(HOOK_VALUES)):
            ghost = src[i].copy()
            self.play(ghost.animate.move_to(copy[i].get_center()), run_time=0.35)
            self.remove(ghost)
            self.play(FadeIn(copy[i]), run_time=0.2)
            self.wait(0.28)

        extra_b = self.ja_text("追加はコピー 4 マス。n=4 のとき。", font_size=22, color=ORANGE)
        extra_b.next_to(copy, DOWN, buff=0.22)
        self.play(FadeIn(extra_b), run_time=0.35)
        self.wait(0.9)

        sum_b = self._sum_cell("0", ORANGE)
        sum_b.next_to(extra_b, DOWN, buff=0.18)
        self.play(FadeIn(sum_b), run_time=0.3)
        running = 0
        for i, value in enumerate(HOOK_VALUES):
            running += value
            self.play(Indicate(copy[i], color=YELLOW), run_time=0.35)
            self._set_sum(sum_b, running)
            self.wait(0.55)

        both = self.ja_text("どちらも答えは 12。違うのは、途中で何マス余分に使うか。", font_size=24)
        both.to_edge(DOWN, buff=0.18)
        self.play(FadeOut(extra_b), FadeIn(both), run_time=0.4)
        self.wait(1.8)
        cap = self._caption("今日はその数え方をやる。")
        self.play(FadeOut(both), FadeIn(cap), run_time=0.35)
        self.wait(1.2)
        self._clear(
            VGroup(question, src, src_name, walk_b, copy, copy_name, sum_b, cap)
        )

    def today_goal(self):
        heading = self.ja_text("今日のゴール", font_size=28)
        heading.next_to(self.header, DOWN, buff=0.32)
        self.play(FadeIn(heading), run_time=0.45)
        lines = [
            "時間計算量は「入力の大きさ n に対して、何回仕事するか」。",
            "空間計算量は「入力の大きさ n に対して、メモリをどれだけ使うか」。",
            "入力そのものと、手順が追加で使うメモリは分けて数える。",
        ]
        items = VGroup(*[self.ja_text(line, font_size=26) for line in lines])
        items.arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        items.next_to(heading, DOWN, buff=0.5)
        items.set_x(0)
        for t, line in zip(items, lines):
            self.play(FadeIn(t, shift=RIGHT * 0.1), run_time=0.45)
            self.wait(1.35)
        self.wait(0.6)
        self._clear(VGroup(heading, items))

    def overview(self):
        heading = self.ja_text("今日の流れ", font_size=28)
        heading.next_to(self.header, DOWN, buff=0.32)
        self.play(FadeIn(heading), run_time=0.4)
        cards = [
            "STEP 1 … 前回の復習。時間計算量は操作回数の増え方",
            "STEP 2 … 空間計算量は、メモリのマスが増える様子",
            "STEP 3 … 入力の n マスと、追加で使うマスを分ける",
            "STEP 4 … 同じ問題でも、時間を減らすために空間を使うことがある",
        ]
        group = VGroup()
        for i, text in enumerate(cards):
            box = RoundedRectangle(
                width=12.2,
                height=0.72,
                corner_radius=0.1,
                color=BLUE if i < 2 else ORANGE,
                stroke_width=2,
                fill_opacity=0.12,
            )
            lab = self.ja_text(text, font_size=24)
            lab.move_to(box)
            group.add(VGroup(box, lab))
        group.arrange(DOWN, buff=0.16)
        group.next_to(heading, DOWN, buff=0.32)
        group.set_x(0)
        for card in group:
            self.play(FadeIn(card, shift=UP * 0.08), run_time=0.4)
            self.wait(1.05)
        cap = self._caption(
            "最後に、配列に同じ値が2つあるかを探す例で、",
            "時間と空間を最初から最後まで通す。",
        )
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.6)
        self._clear(VGroup(heading, group, cap))

    def step1_time(self):
        chip = self._chip("STEP 1  時間")
        lead = self.ja_text("前回やったとおり、秒数ではなく、操作の回数で比べる。", font_size=26)
        self.below_chip(lead, chip)
        self.play(FadeIn(lead), run_time=0.45)
        self.wait(1.2)

        src = self._boxes(HOOK_VALUES)
        src.next_to(lead, DOWN, buff=0.35)
        src.set_x(0)
        idx = self._index_labels(src)
        sum_cell = self._sum_cell("0")
        sum_cell.next_to(src, RIGHT, buff=0.55)
        self.play(FadeIn(src), FadeIn(idx), FadeIn(sum_cell), run_time=0.5)

        running = 0
        count = None
        for i, value in enumerate(HOOK_VALUES):
            running += value
            k = i + 1
            self.play(Indicate(src[i], color=YELLOW), run_time=0.4)
            eq = MathTex(rf"{running - value}+{value}={running}", font_size=28)
            eq.next_to(sum_cell, DOWN, buff=0.2)
            new_count = self.ja_text(f"操作  {k} 回目", font_size=24, color=YELLOW)
            new_count.next_to(idx, DOWN, buff=0.28)
            new_count.set_x(0)
            anims = [FadeIn(eq)]
            if count is None:
                anims.append(FadeIn(new_count))
            else:
                anims.append(Transform(count, new_count))
            self.play(*anims, run_time=0.35)
            self._set_sum(sum_cell, running)
            self.wait(0.9)
            self.play(FadeOut(eq), run_time=0.2)
            count = new_count if count is None else count

        note = self.ja_text("n=4 なら、箱を見る仕事は 4 回。一般には n 回。", font_size=24)
        note.next_to(count, DOWN, buff=0.22)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.3)

        self.play(
            FadeOut(VGroup(src, idx, sum_cell, count, note, lead)),
            run_time=0.35,
        )

        formulas = VGroup(
            VGroup(
                self.ja_text("入力の大きさを", font_size=26),
                MathTex(r"n", font_size=32),
                self.ja_text("と書く。", font_size=26),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                self.ja_text("操作回数を", font_size=26),
                MathTex(r"T(n)", font_size=32),
                self.ja_text("と書く。", font_size=26),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                self.ja_text("今の手順では", font_size=26),
                MathTex(r"T(n)=n", font_size=32),
                self.ja_text("。", font_size=26),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                self.ja_text("増え方の型は", font_size=26),
                MathTex(r"O(n)", font_size=34, color=YELLOW),
                self.ja_text("。", font_size=26),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        self.below_chip(formulas, chip, buff=0.4)
        for row in formulas:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.05)

        definition = self.ja_text(
            "時間計算量は、入力の大きさ n に対する操作回数 T(n) の増え方。",
            font_size=26,
            color=YELLOW,
        )
        definition.next_to(formulas, DOWN, buff=0.4)
        definition.set_x(0)
        self.play(FadeIn(definition), run_time=0.5)
        self.linger(3.4)

        cap = self._caption(
            "時計の秒数ではなく、",
            "「n が増えたとき、仕事が何回増えるか」が時間のほう。",
        )
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.6)
        self.wipe(self.header)

    def step2_space(self):
        chip = self._chip("STEP 2  空間")
        lead = self.ja_text(
            "同じ手順でも、画面の下に何マス置いたかを数えると、メモリの話になる。",
            font_size=26,
        )
        self.below_chip(lead, chip)
        self.play(FadeIn(lead), run_time=0.45)
        self.wait(1.25)

        src = self._boxes(HOOK_VALUES)
        src.next_to(lead, DOWN, buff=0.4)
        src.set_x(-1.4)
        src_lab = self.ja_text("入力  4 マス", font_size=22, color=BLUE)
        src_lab.next_to(src, UP, buff=0.12)
        plus = MathTex(r"+", font_size=36)
        plus.next_to(src, RIGHT, buff=0.35)
        extra = self._sum_cell("12")
        extra.next_to(plus, RIGHT, buff=0.35)
        extra_lab = self.ja_text("合計  1 マス", font_size=22, color=YELLOW)
        extra_lab.next_to(extra[0], DOWN, buff=0.28)
        self.play(FadeIn(src), FadeIn(src_lab), run_time=0.45)
        self.wait(0.9)
        self.play(FadeIn(plus), FadeIn(extra), FadeIn(extra_lab), run_time=0.45)
        self.wait(1.0)

        total = MathTex(r"4+1=5", font_size=36)
        total.next_to(VGroup(src, extra), DOWN, buff=0.55)
        total_ja = self.ja_text("いま画面にあるマスは、全部で 5。", font_size=24)
        total_ja.next_to(total, DOWN, buff=0.18)
        self.play(FadeIn(total), FadeIn(total_ja), run_time=0.4)
        self.wait(1.4)

        grow = self.ja_text(
            "n 個の入力なら、入力だけで n マスいる。合計用は n が増えても 1 マスのまま。",
            font_size=24,
        )
        grow.to_edge(DOWN, buff=0.22)
        self.play(FadeIn(grow), run_time=0.4)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(lead, src, src_lab, plus, extra, extra_lab, total, total_ja, grow)),
            run_time=0.35,
        )

        formulas = VGroup(
            VGroup(
                self.ja_text("使うマスの数を", font_size=26),
                MathTex(r"S(n)", font_size=32),
                self.ja_text("と書く。", font_size=26),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                self.ja_text("今の画面では", font_size=26),
                MathTex(r"S(n)=n+1", font_size=32),
                self.ja_text("。", font_size=26),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                self.ja_text("n が大きいとき、目立つのは", font_size=26),
                MathTex(r"n", font_size=32),
                self.ja_text("のほう。", font_size=26),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                self.ja_text("増え方の型は", font_size=26),
                MathTex(r"O(n)", font_size=34, color=YELLOW),
                self.ja_text("。", font_size=26),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        self.below_chip(formulas, chip, buff=0.4)
        for row in formulas:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.05)

        definition = self.ja_text(
            "空間計算量は、入力の大きさ n に対して使うメモリの増え方。",
            font_size=26,
            color=YELLOW,
        )
        definition.next_to(formulas, DOWN, buff=0.4)
        definition.set_x(0)
        self.play(FadeIn(definition), run_time=0.5)
        self.linger(3.4)

        cap = self._caption("時間は「何回動くか」。空間は「何マス置くか」。両方とも n の関数で書く。")
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.7)
        self.wipe(self.header)

    def step3_extra(self):
        chip = self._chip("STEP 3  追加メモリ")
        lead = self.ja_text(
            "入力の n マスは、問題を受け取った時点でもうある。",
            font_size=26,
        )
        self.below_chip(lead, chip)
        lead2 = self.ja_text(
            "手順の上手下手を見るときは、追加で何マス使うかを分ける。",
            font_size=26,
        )
        lead2.next_to(lead, DOWN, buff=0.18).align_to(lead, LEFT)
        self.play(FadeIn(lead), run_time=0.4)
        self.play(FadeIn(lead2), run_time=0.4)
        self.wait(1.4)

        src = self._boxes(HOOK_VALUES, side=0.62, font_size=26)
        src.next_to(lead2, DOWN, buff=0.3)
        src.set_x(0)
        same = self.ja_text("同じ配列。答えはどちらも 12。", font_size=22)
        same.next_to(src, DOWN, buff=0.16)
        self.play(FadeIn(src), FadeIn(same), run_time=0.45)
        self.wait(1.0)

        a_title = self.ja_text("手順A  その場で足す", font_size=24, color=BLUE)
        a_title.next_to(same, DOWN, buff=0.28)
        a_lines = VGroup(
            self.ja_text("合計用 1 マスだけ追加。コピーは作らない。", font_size=22),
            VGroup(
                self.ja_text("追加メモリ:", font_size=22),
                MathTex(r"1", font_size=28),
                self.ja_text("マス", font_size=22),
            ).arrange(RIGHT, buff=0.1),
            self.ja_text("n が増えても追加は 1 マスのまま。", font_size=22),
            VGroup(
                self.ja_text("追加の増え方は", font_size=22),
                MathTex(r"O(1)", font_size=30, color=BLUE),
                self.ja_text("。", font_size=22),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        a_lines.next_to(a_title, DOWN, buff=0.18)
        self.play(FadeIn(a_title), run_time=0.35)
        for row in a_lines:
            self.play(FadeIn(row), run_time=0.35)
            self.wait(0.95)

        self.play(FadeOut(VGroup(a_title, a_lines)), run_time=0.3)
        b_title = self.ja_text("手順B  コピーしてから足す", font_size=24, color=ORANGE)
        b_title.next_to(same, DOWN, buff=0.22)
        self.play(FadeIn(b_title), run_time=0.3)
        copy = self._boxes(HOOK_VALUES, side=0.58, color=ORANGE, font_size=24)
        copy.next_to(b_title, DOWN, buff=0.2)
        copy.set_x(0)
        for i in range(len(HOOK_VALUES)):
            ghost = src[i].copy()
            self.play(ghost.animate.move_to(copy[i].get_center()), run_time=0.3)
            self.remove(ghost)
            self.play(FadeIn(copy[i]), run_time=0.18)
            self.wait(0.28)

        b_lines = VGroup(
            VGroup(
                self.ja_text("追加メモリ: コピー", font_size=22),
                MathTex(r"n", font_size=26),
                self.ja_text("マス＋合計 1 マス", font_size=22),
            ).arrange(RIGHT, buff=0.08),
            VGroup(
                self.ja_text("追加の増え方は", font_size=22),
                MathTex(r"O(n)", font_size=30, color=ORANGE),
                self.ja_text("。", font_size=22),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        b_lines.next_to(copy, DOWN, buff=0.18)
        for row in b_lines:
            self.play(FadeIn(row), run_time=0.35)
            self.wait(1.0)

        self.play(
            FadeOut(VGroup(lead, lead2, src, same, b_title, copy, b_lines)),
            run_time=0.35,
        )

        definition = self.ja_text(
            "追加メモリ（補助空間）は、入力以外に手順が新しく置くマスの増え方。",
            font_size=26,
            color=YELLOW,
        )
        self.below_chip(definition, chip, buff=0.45)
        self.play(FadeIn(definition), run_time=0.5)
        self.linger(3.5)

        table = self.aligned_table(
            [
                [
                    self.ja_text("手順", font_size=22, color=GREY_B),
                    self.ja_text("答え", font_size=22, color=GREY_B),
                    self.ja_text("追加メモリ", font_size=22, color=GREY_B),
                ],
                [
                    self.ja_text("A その場", font_size=24, color=BLUE),
                    MathTex(r"12", font_size=28),
                    MathTex(r"O(1)", font_size=28, color=BLUE),
                ],
                [
                    self.ja_text("B コピー", font_size=24, color=ORANGE),
                    MathTex(r"12", font_size=28),
                    MathTex(r"O(n)", font_size=28, color=ORANGE),
                ],
            ],
            h_buff=0.55,
            v_buff=0.22,
        )
        table.scale(0.95)
        table.next_to(definition, DOWN, buff=0.35)
        table.set_x(0)
        self.reveal_table(table, row_wait=1.0)

        cap = self._caption("入力の n マスはどちらも使う。差がつくのは、追加のほう。")
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.7)
        self.wipe(self.header)

    def step4_tradeoff(self):
        chip = self._chip("STEP 4  トレードオフ")
        lead = self.ja_text(
            "同じ答えを出す手順でも、時間を減らすために、追加メモリを増やすことがある。",
            font_size=26,
        )
        self.below_chip(lead, chip)
        self.play(FadeIn(lead), run_time=0.45)
        self.wait(1.3)

        src = self._boxes(STEP4_VALUES, color=BLUE)
        src.next_to(lead, DOWN, buff=0.32)
        src.set_x(0)
        q = self.ja_text("値が 1 から 4 まで。同じ 3 が2つあるか。", font_size=22)
        q.next_to(src, DOWN, buff=0.16)
        self.play(FadeIn(src), FadeIn(q), run_time=0.45)
        self.wait(1.1)

        a_title = self.ja_text("遅いが追加が少ないやり方  すべてのペア", font_size=24, color=BLUE)
        a_title.next_to(q, DOWN, buff=0.24)
        self.play(FadeIn(a_title), run_time=0.35)

        pairs = [(0, 1), (0, 2), (1, 2)]
        count_txt = self.ja_text("比較  0 回", font_size=22)
        count_txt.next_to(a_title, DOWN, buff=0.18)
        self.play(FadeIn(count_txt), run_time=0.25)
        last_cmp = None
        lines = VGroup()
        for k, (i, j) in enumerate(pairs, start=1):
            line = Line(
                src[i].get_top() + UP * 0.08,
                src[j].get_top() + UP * 0.08,
                color=YELLOW if STEP4_VALUES[i] == STEP4_VALUES[j] else GREY_B,
                stroke_width=3,
            ).shift(UP * (0.1 * k))
            a, b = STEP4_VALUES[i], STEP4_VALUES[j]
            same = a == b
            cmp_tex = MathTex(rf"{a}={b}" if same else rf"{a}\neq {b}", font_size=28)
            cmp_tex.next_to(count_txt, RIGHT, buff=0.4)
            ja = self.ja_text("同じ。" if same else "違う。", font_size=22)
            ja.next_to(cmp_tex, RIGHT, buff=0.12)
            new_count = self.ja_text(f"比較  {k} 回", font_size=22)
            new_count.move_to(count_txt)
            anims = [Create(line), Transform(count_txt, new_count), FadeIn(cmp_tex), FadeIn(ja)]
            if last_cmp is not None:
                anims.append(FadeOut(last_cmp))
            self.play(*anims, run_time=0.4)
            self.wait(0.8)
            lines.add(line)
            last_cmp = VGroup(cmp_tex, ja)

        a_sum = VGroup(
            VGroup(
                self.ja_text("比較は 3 回。一般には", font_size=22),
                MathTex(r"\dfrac{n(n-1)}{2}", font_size=28),
                self.ja_text("回で", font_size=22),
                MathTex(r"O(n^2)", font_size=28, color=BLUE),
                self.ja_text("。", font_size=22),
            ).arrange(RIGHT, buff=0.08),
            VGroup(
                self.ja_text("追加は添字くらいで、", font_size=22),
                MathTex(r"O(1)", font_size=28, color=BLUE),
                self.ja_text("。", font_size=22),
            ).arrange(RIGHT, buff=0.08),
        ).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        a_sum.next_to(count_txt, DOWN, buff=0.22)
        for row in a_sum:
            self.play(FadeIn(row), run_time=0.35)
            self.wait(1.1)

        self.play(
            FadeOut(VGroup(a_title, count_txt, last_cmp, lines, a_sum)),
            run_time=0.3,
        )

        b_title = self.ja_text("追加のマスを使って、見る回数を減らす", font_size=24, color=ORANGE)
        b_title.next_to(q, DOWN, buff=0.2)
        marks, fills = self._mark_row(4)
        marks.next_to(b_title, DOWN, buff=0.28)
        marks.set_x(0)
        mark_lab = self.ja_text("印の箱。最初は全部オフ。", font_size=20, color=ORANGE)
        mark_lab.next_to(marks, DOWN, buff=0.12)
        self.play(FadeIn(b_title), FadeIn(marks), FadeIn(mark_lab), run_time=0.45)
        self.wait(1.0)

        steps_b = [
            (0, 3, False, "印の 3 はオフ → オンにする"),
            (1, 1, False, "印の 1 はオフ → オンにする"),
            (2, 3, True, "印の 3 はもうオン → 「ある」"),
        ]
        status = None
        for idx, value, found, text in steps_b:
            self.play(Indicate(src[idx], color=YELLOW), run_time=0.4)
            msg = self.ja_text(text, font_size=22)
            msg.next_to(mark_lab, DOWN, buff=0.18)
            if status is None:
                self.play(FadeIn(msg), run_time=0.3)
                status = msg
            else:
                self.play(Transform(status, msg), run_time=0.3)
            if not found:
                self._turn_on(marks[value - 1], fills[value - 1])
            else:
                self.play(Indicate(marks[value - 1], color=YELLOW), run_time=0.5)
            self.wait(0.95)

        b_sum = VGroup(
            VGroup(
                self.ja_text("配列は左から n 回見るだけ。時間は", font_size=22),
                MathTex(r"O(n)", font_size=28, color=ORANGE),
                self.ja_text("。", font_size=22),
            ).arrange(RIGHT, buff=0.08),
            VGroup(
                self.ja_text("印は値の種類の個数。値が 1 から n なら追加は", font_size=22),
                MathTex(r"O(n)", font_size=28, color=ORANGE),
                self.ja_text("。", font_size=22),
            ).arrange(RIGHT, buff=0.08),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        b_sum.next_to(status, DOWN, buff=0.18)
        for row in b_sum:
            self.play(FadeIn(row), run_time=0.35)
            self.wait(1.1)

        self.play(
            FadeOut(VGroup(lead, src, q, b_title, marks, mark_lab, status, b_sum)),
            run_time=0.35,
        )

        trade = VGroup(
            VGroup(
                self.ja_text("時間を", font_size=24),
                MathTex(r"O(n^2)", font_size=30, color=YELLOW),
                self.ja_text("から", font_size=24),
                MathTex(r"O(n)", font_size=30, color=YELLOW),
                self.ja_text("に落とすかわりに、", font_size=24),
            ).arrange(RIGHT, buff=0.08),
            VGroup(
                self.ja_text("追加メモリを", font_size=24),
                MathTex(r"O(1)", font_size=30, color=YELLOW),
                self.ja_text("から", font_size=24),
                MathTex(r"O(n)", font_size=30, color=YELLOW),
                self.ja_text("に増やす。", font_size=24),
            ).arrange(RIGHT, buff=0.08),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        self.below_chip(trade, chip, buff=0.5)
        self.play(FadeIn(trade), run_time=0.5)
        self.linger(3.3)

        cap = self._caption("どちらが正解、ではない。制約に合わせて、時間と空間のバランスを選ぶ。")
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.7)
        self.wipe(self.header)

    def worked_example(self):
        chip = self._chip("実例  同じ値があるか")
        q = self.ja_text(
            "長さ n の配列に、同じ値が2つ以上あるかどうかを知りたい。値は 1 から n まで。",
            font_size=24,
        )
        self.below_chip(q, chip)
        self.play(FadeIn(q), run_time=0.45)
        self.wait(1.3)

        src = self._boxes(EXAMPLE_VALUES)
        src.next_to(q, DOWN, buff=0.3)
        src.set_x(0)
        idx = self._index_labels(src)
        dup = self.ja_text("同じ 4 が2つある。", font_size=22, color=YELLOW)
        dup.next_to(src, RIGHT, buff=0.35)
        self.play(FadeIn(src), FadeIn(idx), FadeIn(dup), run_time=0.5)
        self.wait(1.0)

        a_title = self.ja_text("手順A  すべてのペアを比べる", font_size=24, color=BLUE)
        a_title.next_to(idx, DOWN, buff=0.22)
        extra_a = VGroup(
            self.ja_text("追加", font_size=18, color=BLUE),
            self._mini_index("i"),
            self._mini_index("j"),
        ).arrange(RIGHT, buff=0.12)
        extra_a.next_to(a_title, RIGHT, buff=0.35)
        self.play(FadeIn(a_title), FadeIn(extra_a), run_time=0.4)
        self.wait(0.9)

        pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
        count_txt = self.ja_text("ペア  0", font_size=22)
        count_txt.next_to(a_title, DOWN, buff=0.18)
        self.play(FadeIn(count_txt), run_time=0.25)
        last_cmp = None
        pair_lines = VGroup()
        for k, (i, j) in enumerate(pairs, start=1):
            line = Line(
                src[i].get_top() + UP * 0.08,
                src[j].get_top() + UP * 0.08,
                color=YELLOW if EXAMPLE_VALUES[i] == EXAMPLE_VALUES[j] else GREY_B,
                stroke_width=3,
            ).shift(UP * (0.07 * ((i + j) % 3)))
            a, b = EXAMPLE_VALUES[i], EXAMPLE_VALUES[j]
            same = a == b
            cmp_tex = MathTex(rf"{a}={b}" if same else rf"{a}\neq {b}", font_size=26)
            cmp_tex.next_to(count_txt, RIGHT, buff=0.35)
            ja = self.ja_text("同じ。" if same else "違う。", font_size=20)
            ja.next_to(cmp_tex, RIGHT, buff=0.1)
            new_count = self.ja_text(f"ペア  {k}", font_size=22)
            new_count.move_to(count_txt)
            anims = [Create(line), Transform(count_txt, new_count), FadeIn(cmp_tex), FadeIn(ja)]
            if last_cmp is not None:
                anims.append(FadeOut(last_cmp))
            self.play(*anims, run_time=0.4)
            self.wait(0.7)
            if same:
                found = self.ja_text(
                    "ここで「ある」と分かるが、最悪の回数を見るので数え切る。",
                    font_size=20,
                )
                found.next_to(count_txt, DOWN, buff=0.14)
                found.set_x(0)
                self.play(FadeIn(found), run_time=0.3)
                self.wait(1.15)
                self.play(FadeOut(found), run_time=0.2)
            pair_lines.add(line)
            last_cmp = VGroup(cmp_tex, ja)

        six = self.ja_text("n=4 のとき、ペアは 6 本。", font_size=22)
        six.next_to(a_title, DOWN, buff=0.55)
        self.play(FadeOut(count_txt), FadeOut(last_cmp), FadeIn(six), run_time=0.35)
        self.wait(1.0)

        self.play(
            FadeOut(VGroup(src, idx, dup, a_title, extra_a, pair_lines, six, q)),
            run_time=0.35,
        )

        formulas = VGroup(
            VGroup(
                self.ja_text("1番目は残り", font_size=24),
                MathTex(r"n-1", font_size=28),
                self.ja_text("個と比べる。", font_size=24),
            ).arrange(RIGHT, buff=0.08),
            VGroup(
                self.ja_text("2番目は残り", font_size=24),
                MathTex(r"n-2", font_size=28),
                self.ja_text("個と比べる。", font_size=24),
            ).arrange(RIGHT, buff=0.08),
            self.ja_text("……", font_size=24),
            self.ja_text("(n-1) 番目は残り 1 個と比べる。", font_size=24),
            MathTex(r"T(n)=(n-1)+(n-2)+\cdots+1", font_size=30),
            MathTex(r"T(n)=\dfrac{n(n-1)}{2}", font_size=32),
            MathTex(r"n=4:\quad \dfrac{4\cdot 3}{2}=6", font_size=30),
        ).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        self.below_chip(formulas, chip, buff=0.35)
        for row in formulas:
            self.play(FadeIn(row), run_time=0.35)
            self.wait(0.95)
        match = VGroup(
            self.ja_text("さっきの 6 本と一致する。大きい項は", font_size=22),
            MathTex(r"n^2", font_size=26),
            self.ja_text("なので時間は", font_size=22),
            MathTex(r"O(n^2)", font_size=26, color=BLUE),
            self.ja_text("。", font_size=22),
        ).arrange(RIGHT, buff=0.08)
        match.next_to(formulas, DOWN, buff=0.18)
        extra_line = VGroup(
            self.ja_text("追加のマスは n が増えても 2 個くらい →", font_size=22),
            MathTex(r"O(1)", font_size=28, color=BLUE),
        ).arrange(RIGHT, buff=0.1)
        extra_line.next_to(match, DOWN, buff=0.14)
        self.play(FadeIn(match), FadeIn(extra_line), run_time=0.4)
        self.wait(1.5)

        self.play(FadeOut(VGroup(formulas, match, extra_line)), run_time=0.3)

        b_title = self.ja_text("手順B  印の箱を使う", font_size=24, color=ORANGE)
        self.below_chip(b_title, chip, buff=0.32)
        src = self._boxes(EXAMPLE_VALUES, side=0.64)
        src.next_to(b_title, DOWN, buff=0.22)
        src.set_x(0)
        marks, fills = self._mark_row(4)
        marks.next_to(src, DOWN, buff=0.45)
        marks.set_x(0)
        mark_lab = self.ja_text("印  1 から 4。最初は全部オフ。", font_size=20, color=ORANGE)
        mark_lab.next_to(marks, DOWN, buff=0.1)
        self.play(FadeIn(b_title), FadeIn(src), FadeIn(marks), FadeIn(mark_lab), run_time=0.5)
        self.wait(1.0)

        b_steps = [
            (0, 4, False, "印の 4 はオフ → オン。まだ「なし」"),
            (1, 1, False, "印の 1 はオフ → オン。まだ「なし」"),
            (2, 4, True, "印の 4 はオン → 「ある」。ここで止めてよい"),
        ]
        status = None
        for idx_i, value, found, text in b_steps:
            self.play(Indicate(src[idx_i], color=YELLOW), run_time=0.4)
            msg = self.ja_text(text, font_size=22)
            msg.next_to(mark_lab, DOWN, buff=0.16)
            if status is None:
                self.play(FadeIn(msg), run_time=0.3)
                status = msg
            else:
                self.play(Transform(status, msg), run_time=0.3)
            if not found:
                self._turn_on(marks[value - 1], fills[value - 1])
            else:
                self.play(Indicate(marks[value - 1], color=YELLOW), run_time=0.55)
            self.wait(1.0)

        worst = self.ja_text("最悪を数えるなら最後まで見る。どちらにせよ n 回で終わる。", font_size=20)
        worst.next_to(status, DOWN, buff=0.16)
        self.play(FadeIn(worst), run_time=0.35)
        self.wait(1.2)

        b_form = VGroup(
            VGroup(
                self.ja_text("配列の各要素を 1 回見る →", font_size=22),
                MathTex(r"n", font_size=26),
                self.ja_text("回", font_size=22),
            ).arrange(RIGHT, buff=0.08),
            self.ja_text("印の箱を見る／付けるのも、1要素あたり定数回。", font_size=22),
            VGroup(
                self.ja_text("よって", font_size=22),
                MathTex(r"T(n)=O(n)", font_size=28, color=ORANGE),
                self.ja_text("。", font_size=22),
            ).arrange(RIGHT, buff=0.08),
            VGroup(
                self.ja_text("印の箱は n 個（値が 1 から n）→ 追加", font_size=22),
                MathTex(r"O(n)", font_size=28, color=ORANGE),
            ).arrange(RIGHT, buff=0.08),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        b_form.next_to(worst, DOWN, buff=0.16)
        for row in b_form:
            self.play(FadeIn(row), run_time=0.35)
            self.wait(1.0)

        self.play(
            FadeOut(VGroup(b_title, src, marks, mark_lab, status, worst, b_form)),
            run_time=0.35,
        )

        table = self.aligned_table(
            [
                [
                    self.ja_text("手順", font_size=20, color=GREY_B),
                    self.ja_text("時間", font_size=20, color=GREY_B),
                    self.ja_text("追加メモリ", font_size=20, color=GREY_B),
                    self.ja_text("n=4 の仕事", font_size=20, color=GREY_B),
                ],
                [
                    self.ja_text("A 全ペア", font_size=22, color=BLUE),
                    MathTex(r"O(n^2)", font_size=26, color=BLUE),
                    MathTex(r"O(1)", font_size=26, color=BLUE),
                    self.ja_text("比較 6 回", font_size=22),
                ],
                [
                    self.ja_text("B 印の箱", font_size=22, color=ORANGE),
                    MathTex(r"O(n)", font_size=26, color=ORANGE),
                    MathTex(r"O(n)", font_size=26, color=ORANGE),
                    self.ja_text("見る 4 回", font_size=22),
                ],
            ],
            h_buff=0.42,
            v_buff=0.2,
        )
        table.scale(0.92)
        self.below_chip(table, chip, buff=0.4)
        table.set_x(0)
        self.reveal_table(table, row_wait=1.05)

        cap = self._caption("答えはどちらも「ある」。時間を減らすなら、印のためのマスが要る。")
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.8)
        self.wipe(self.header)

    def _mini_index(self, name):
        sq = Square(side_length=0.48, color=BLUE, stroke_width=2)
        lab = MathTex(name, font_size=20)
        lab.move_to(sq)
        return VGroup(sq, lab)

    def summary(self):
        chip = self._chip("まとめ")
        items = VGroup(
            VGroup(
                MathTex(r"1.", font_size=28),
                self.ja_text("時間計算量は、n に対する操作回数", font_size=24),
                MathTex(r"T(n)", font_size=28),
                self.ja_text("の増え方。", font_size=24),
            ).arrange(RIGHT, buff=0.08),
            VGroup(
                MathTex(r"2.", font_size=28),
                self.ja_text("空間計算量は、n に対するメモリの増え方。入力と追加は分ける。", font_size=24),
            ).arrange(RIGHT, buff=0.08),
            VGroup(
                MathTex(r"3.", font_size=28),
                self.ja_text("同じ答えでも、時間と空間のバランスは手順で変わる。", font_size=24),
            ).arrange(RIGHT, buff=0.08),
        ).arrange(DOWN, buff=0.36, aligned_edge=LEFT)
        self.below_chip(items, chip, buff=0.5)
        for row in items:
            self.play(FadeIn(row), run_time=0.45)
            self.wait(1.4)
        cap = self._caption(
            "「何秒か」と「何バイトか」より先に、",
            "「n が増えたとき、回数とマスがどう増えるか」を見る。",
        )
        self.play(FadeIn(cap), run_time=0.45)
        self.wait(1.9)
        self.wipe(self.header)

    def next_preview(self):
        chip = self._chip("次回")
        nxt = self.ja_text("#4 最良・最悪・平均計算量", font_size=32, color=YELLOW)
        self.below_chip(nxt, chip, buff=0.5)
        self.play(FadeIn(nxt), run_time=0.5)
        self.wait(1.2)
        body = VGroup(
            self.ja_text("今日は、何を数えるか（時間と空間）を分けた。", font_size=26),
            self.ja_text("次回は、どの入力で数えるか。", font_size=26),
            self.ja_text("いちばん速いとき、いちばん遅いとき、平均を並べる。", font_size=26),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        body.next_to(nxt, DOWN, buff=0.45)
        body.align_to(nxt, LEFT)
        for row in body:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.2)
        self.wait(1.4)
