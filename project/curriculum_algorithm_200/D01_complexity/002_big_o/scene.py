from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import LessonScene


class BigO(LessonScene):
    """#2 計算量とビッグO記法（約9分）"""

    def construct(self):
        self.header = self._open_header()
        self.hook()
        self.today_goal()
        self.overview()
        self.step1_why_counts()
        self.step2_count_ops()
        self.step3_drop_terms()
        self.step4_common_orders()
        self.worked_example()
        self.summary()
        self.next_preview()

    def _open_header(self):
        title = self.ja_text("#2  計算量とビッグO記法", font_size=40)
        self.play(FadeIn(title), run_time=0.8)
        self.wait(0.7)
        self.play(title.animate.scale(0.55).to_edge(UP, buff=0.16), run_time=0.5)
        return title

    def _clear(self, group):
        if group is None:
            return
        self.play(FadeOut(group), run_time=0.4)

    def _section_title(self, text):
        title = self.ja_text(text, font_size=28)
        title.next_to(self.header, DOWN, buff=0.28)
        self.play(FadeIn(title), run_time=0.45)
        return title

    def _caption(self, text, font_size=26):
        cap = self.ja_text(text, font_size=font_size)
        cap.to_edge(DOWN, buff=0.28)
        return cap

    def _boxes(self, values, side=0.7, color=BLUE):
        group = VGroup()
        for value in values:
            sq = Square(side_length=side, color=color, stroke_width=2)
            lab = MathTex(str(value), font_size=30)
            group.add(VGroup(sq, lab))
        group.arrange(RIGHT, buff=0.16)
        return group

    def _index_labels(self, boxes):
        labels = VGroup()
        for i, box in enumerate(boxes, start=1):
            lab = MathTex(str(i), font_size=22, color=GREY_B)
            lab.next_to(box, DOWN, buff=0.12)
            labels.add(lab)
        return labels

    def hook(self):
        question = self.ja_text("答えが同じでも、遅さが全然違うことがある。", font_size=30)
        question.next_to(self.header, DOWN, buff=0.45)
        self.play(FadeIn(question), run_time=0.6)
        self.wait(1.4)

        card_a = self._program_card("プログラムA", "1 から n まで、順番に足す", r"T = n", BLUE)
        card_b = self._program_card("プログラムB", "二重ループでマスを全部塗る", r"T = n \times n", ORANGE)
        cards = VGroup(card_a, card_b).arrange(RIGHT, buff=0.7)
        cards.next_to(question, DOWN, buff=0.4)
        self.play(FadeIn(card_a, shift=LEFT * 0.2), FadeIn(card_b, shift=RIGHT * 0.2), run_time=0.8)
        self.wait(1.3)

        rows = VGroup()
        specs = [
            (r"n=5", r"5", r"5\times 5=25"),
            (r"n=10", r"10", r"10\times 10=100"),
            (r"n=1000", r"1000", r"1000\times 1000=1{,}000{,}000"),
        ]
        for n_tex, a_tex, b_tex in specs:
            n_lab = MathTex(n_tex, font_size=30)
            a_lab = MathTex(a_tex, font_size=30, color=BLUE)
            b_lab = MathTex(b_tex, font_size=30, color=ORANGE)
            row = VGroup(n_lab, a_lab, b_lab).arrange(RIGHT, buff=0.85)
            rows.add(row)
        rows.arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        rows.next_to(cards, DOWN, buff=0.35)
        for row in rows:
            self.play(FadeIn(row), run_time=0.45)
            self.wait(1.1)

        cap = self._caption("n を大きくすると、B の仕事だけが急に膨らむ。今日は、この増え方をどう書くかをやる。")
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(2.0)
        self._clear(VGroup(question, cards, rows, cap))

    def _program_card(self, title, body, formula, color):
        box = RoundedRectangle(width=5.4, height=2.15, corner_radius=0.12, color=color, stroke_width=2)
        t = self.ja_text(title, font_size=26, color=color)
        b = self.ja_text(body, font_size=22)
        f = MathTex(formula, font_size=32, color=color)
        col = VGroup(t, b, f).arrange(DOWN, buff=0.16)
        col.move_to(box.get_center())
        return VGroup(box, col)

    def today_goal(self):
        heading = self._section_title("今日のゴール")
        lines = [
            "計算量は「入力の大きさ n に対して、何回仕事するか」。",
            "細かい差は後回しにして、増え方の型を見る。",
            "その型をビッグO、たとえば O(n) や O(n^{2}) と書く。",
        ]
        items = VGroup()
        math_bits = [
            None,
            None,
            VGroup(
                self.ja_text("その型をビッグO、たとえば", font_size=28),
                MathTex(r"O(n)", font_size=34),
                self.ja_text("や", font_size=28),
                MathTex(r"O(n^2)", font_size=34),
                self.ja_text("と書く。", font_size=28),
            ).arrange(RIGHT, buff=0.12),
        ]
        texts = [
            self.ja_text(lines[0], font_size=28),
            self.ja_text(lines[1], font_size=28),
            math_bits[2],
        ]
        for i, mob in enumerate(texts, start=1):
            num = MathTex(rf"{i}.", font_size=30)
            row = VGroup(num, mob).arrange(RIGHT, buff=0.2)
            items.add(row)
        items.arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        items.next_to(heading, DOWN, buff=0.55)
        for row in items:
            self.play(FadeIn(row), run_time=0.5)
            self.wait(1.5)
        self.wait(0.6)
        self._clear(VGroup(heading, items))

    def overview(self):
        heading = self._section_title("今日の流れ")
        steps = [
            ("STEP 1", "時計の秒数ではなく、操作の回数で比べる理由"),
            ("STEP 2", "ループを1回ずつ追って、回数を式にする"),
            ("STEP 3", "3n+5 から定数と小さい項を落として O(n) にする"),
            ("STEP 4", "よく出るオーダーを、増え方の順に並べる"),
        ]
        cards = VGroup()
        for label, body in steps:
            lab = self.ja_text(label, font_size=24, color=YELLOW)
            txt = self.ja_text(body, font_size=26)
            row = VGroup(lab, txt).arrange(RIGHT, buff=0.3)
            cards.add(row)
        cards.arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        cards.next_to(heading, DOWN, buff=0.45)
        for row in cards:
            self.play(FadeIn(row), run_time=0.45)
            self.wait(1.15)
        cap = self._caption("最後に、配列に同じ値が2つあるかを探す例で、最初から最後まで通す。")
        self.play(FadeIn(cap), run_time=0.45)
        self.wait(1.8)
        self._clear(VGroup(heading, cards, cap))

    def step1_why_counts(self):
        heading = self._section_title("STEP 1  なぜ操作回数か")
        line1 = self.ja_text("同じプログラムでも、パソコンが速いと秒数は短くなる。", font_size=26)
        line1.next_to(heading, DOWN, buff=0.4)
        self.play(FadeIn(line1), run_time=0.45)
        self.wait(1.3)

        pc_a = self._pc_card("パソコンA", "1 秒", BLUE)
        pc_b = self._pc_card("パソコンB", "0.1 秒", TEAL)
        pcs = VGroup(pc_a, pc_b).arrange(RIGHT, buff=0.8)
        pcs.next_to(line1, DOWN, buff=0.35)
        same = MathTex(r"T=n", font_size=36)
        same.next_to(pcs, DOWN, buff=0.3)
        self.play(FadeIn(pcs), run_time=0.6)
        self.play(Write(same), run_time=0.6)
        self.wait(1.4)

        line2 = self.ja_text("「何秒かかったか」だけだと、機械のせいなのか、手順のせいなのかが分からない。", font_size=24)
        line2.next_to(same, DOWN, buff=0.32)
        self.play(FadeIn(line2), run_time=0.45)
        self.wait(1.8)

        self.play(FadeOut(VGroup(pcs, same, line2)), run_time=0.4)
        line3 = self.ja_text("そこで、入力の大きさ n を決めたときに、比較や足し算を何回やるかを数える。", font_size=24)
        line3.next_to(line1, DOWN, buff=0.45)
        self.play(FadeIn(line3), run_time=0.45)
        self.wait(1.5)

        eq1 = VGroup(
            self.ja_text("入力の大きさを", font_size=28),
            MathTex(r"n", font_size=36),
            self.ja_text("と書く。", font_size=28),
        ).arrange(RIGHT, buff=0.12)
        eq2 = VGroup(
            self.ja_text("操作回数を", font_size=28),
            MathTex(r"T(n)", font_size=36),
            self.ja_text("と書く。", font_size=28),
        ).arrange(RIGHT, buff=0.12)
        eq3 = VGroup(
            self.ja_text("この", font_size=28),
            MathTex(r"T(n)", font_size=36),
            self.ja_text("の増え方を、計算量と呼ぶ。", font_size=28),
        ).arrange(RIGHT, buff=0.12)
        eqs = VGroup(eq1, eq2, eq3).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        eqs.next_to(line3, DOWN, buff=0.4)
        for row in eqs:
            self.play(FadeIn(row), run_time=0.5)
            self.wait(1.3)

        cap = self._caption("秒数ではなく、「n が増えたとき、仕事がどう増えるか」を見る。")
        self.play(FadeIn(cap), run_time=0.45)
        self.wait(1.8)
        self._clear(VGroup(heading, line1, line3, eqs, cap))

    def _pc_card(self, name, seconds, color):
        box = RoundedRectangle(width=3.6, height=1.5, corner_radius=0.1, color=color, stroke_width=2)
        n = self.ja_text(name, font_size=24)
        s = self.ja_text(seconds, font_size=30, color=color)
        col = VGroup(n, s).arrange(DOWN, buff=0.14).move_to(box)
        return VGroup(box, col)

    def step2_count_ops(self):
        heading = self._section_title("STEP 2  回数を数える")
        intro = self.ja_text("左から順に見て、x と等しいか比べる。", font_size=26)
        intro.next_to(heading, DOWN, buff=0.32)
        self.play(FadeIn(intro), run_time=0.4)

        values = [3, 1, 7, 2]
        boxes = self._boxes(values)
        boxes.next_to(intro, DOWN, buff=0.35)
        idx = self._index_labels(boxes)
        x_lab = VGroup(
            MathTex(r"x=7", font_size=32, color=YELLOW),
        )
        x_lab.next_to(boxes, RIGHT, buff=0.55)
        self.play(FadeIn(boxes), FadeIn(idx), FadeIn(x_lab), run_time=0.6)
        self.wait(0.8)

        count_lab = self.ja_text("比較  0 回", font_size=26)
        count_lab.next_to(boxes, DOWN, buff=0.7)
        self.play(FadeIn(count_lab), run_time=0.3)

        found_at = 2
        for i, value in enumerate(values):
            rect = SurroundingRectangle(boxes[i], color=YELLOW, buff=0.06)
            cmp_tex = MathTex(rf"{value} \neq 7" if value != 7 else rf"{value} = 7", font_size=32)
            cmp_tex.next_to(count_lab, DOWN, buff=0.2)
            new_count = self.ja_text(f"比較  {i + 1} 回", font_size=26)
            new_count.move_to(count_lab)
            self.play(Create(rect), run_time=0.35)
            self.play(FadeIn(cmp_tex), Transform(count_lab, new_count), run_time=0.4)
            self.wait(0.9)
            if i == found_at:
                note = self.ja_text("ここで止まる。", font_size=24, color=YELLOW)
                note.next_to(cmp_tex, DOWN, buff=0.18)
                self.play(FadeIn(note), run_time=0.35)
                self.wait(1.1)
                self.play(FadeOut(rect), FadeOut(cmp_tex), FadeOut(note), run_time=0.3)
                break
            self.play(FadeOut(rect), FadeOut(cmp_tex), run_time=0.25)

        mid = self.ja_text("今回は3回で見つかった。一番重いのは、最後まで見つからないとき。", font_size=24)
        mid.next_to(count_lab, DOWN, buff=0.28)
        self.play(FadeIn(mid), run_time=0.45)
        self.wait(1.6)

        new_x = MathTex(r"x=9", font_size=32, color=YELLOW)
        new_x.move_to(x_lab)
        self.play(Transform(x_lab, new_x), FadeOut(mid), run_time=0.45)
        self.wait(0.4)

        last_cmp = None
        for i, value in enumerate(values):
            rect = SurroundingRectangle(boxes[i], color=ORANGE, buff=0.06)
            cmp_tex = MathTex(rf"{value} \neq 9", font_size=32)
            cmp_tex.next_to(count_lab, DOWN, buff=0.2)
            new_count = self.ja_text(f"比較  {i + 1} 回", font_size=26)
            new_count.move_to(count_lab)
            self.play(Create(rect), run_time=0.3)
            anims = [Transform(count_lab, new_count), FadeIn(cmp_tex)]
            if last_cmp is not None:
                anims.append(FadeOut(last_cmp))
            self.play(*anims, run_time=0.35)
            self.wait(0.7)
            self.play(FadeOut(rect), run_time=0.2)
            last_cmp = cmp_tex

        end_note = self.ja_text("配列の長さが 4 なので、ここで終わり。", font_size=24)
        end_note.next_to(count_lab, DOWN, buff=0.55)
        self.play(FadeIn(end_note), run_time=0.4)
        self.wait(1.2)

        self.play(
            FadeOut(VGroup(intro, boxes, idx, x_lab, count_lab, last_cmp, end_note)),
            run_time=0.4,
        )
        t_lin1 = VGroup(
            self.ja_text("長さ", font_size=28),
            MathTex(r"n", font_size=34),
            self.ja_text("なら、最悪で比較は", font_size=28),
            MathTex(r"n", font_size=34),
            self.ja_text("回。", font_size=28),
        ).arrange(RIGHT, buff=0.1)
        t_lin2 = MathTex(r"T(n) = n", font_size=40)
        t_lin = VGroup(t_lin1, t_lin2).arrange(DOWN, buff=0.28)
        t_lin.next_to(heading, DOWN, buff=0.55)
        self.play(FadeIn(t_lin1), run_time=0.45)
        self.wait(1.2)
        self.play(Write(t_lin2), run_time=0.7)
        self.wait(1.4)
        self._clear(t_lin)

        nest_intro = self.ja_text("次は、外側と内側のループが重なった場合。", font_size=26)
        nest_intro.next_to(heading, DOWN, buff=0.32)
        self.play(FadeIn(nest_intro), run_time=0.45)
        self.wait(1.2)

        n = 3
        grid = VGroup()
        for r in range(n):
            row = VGroup()
            for c in range(n):
                cell = Square(side_length=0.62, color=GREY_B, stroke_width=2)
                row.add(cell)
            row.arrange(RIGHT, buff=0.08)
            grid.add(row)
        grid.arrange(DOWN, buff=0.08)
        grid.next_to(nest_intro, DOWN, buff=0.3).shift(LEFT * 2.4)
        self.play(FadeIn(grid), run_time=0.5)

        total = Integer(0, font_size=36)
        total_row = VGroup(self.ja_text("ここまでの回数", font_size=24), total).arrange(RIGHT, buff=0.2)
        total_row.next_to(grid, RIGHT, buff=0.7)
        self.play(FadeIn(total_row), run_time=0.35)

        k = 0
        notes = VGroup()
        for r in range(n):
            for c in range(n):
                k += 1
                cell = grid[r][c]
                self.play(
                    cell.animate.set_fill(ORANGE, opacity=0.7).set_stroke(YELLOW),
                    total.animate.set_value(k),
                    run_time=0.28,
                )
            note = VGroup(
                self.ja_text(f"外側 i={r + 1} のとき、内側が 3 回。ここまで", font_size=22),
                MathTex(str((r + 1) * n), font_size=26),
            ).arrange(RIGHT, buff=0.1)
            notes.add(note)
        notes.arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        notes.next_to(total_row, DOWN, buff=0.35).align_to(total_row, LEFT)
        for note in notes:
            self.play(FadeIn(note), run_time=0.35)
            self.wait(0.9)

        self.play(FadeOut(VGroup(nest_intro, grid, total_row, notes)), run_time=0.4)
        formulas = VGroup(
            VGroup(self.ja_text("内側は毎回", font_size=28), MathTex(r"n", font_size=34), self.ja_text("回。", font_size=28)).arrange(RIGHT, buff=0.1),
            VGroup(self.ja_text("外側は", font_size=28), MathTex(r"n", font_size=34), self.ja_text("回ある。", font_size=28)).arrange(RIGHT, buff=0.1),
            VGroup(self.ja_text("だから全部で", font_size=28), MathTex(r"n \times n", font_size=34), self.ja_text("回。", font_size=28)).arrange(RIGHT, buff=0.1),
            MathTex(r"T(n) = n^2", font_size=42),
        ).arrange(DOWN, buff=0.24, aligned_edge=LEFT)
        formulas.next_to(heading, DOWN, buff=0.45)
        for row in formulas:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.05)

        cap = self._caption("同じ「ループ」でも、一段か二段かで増え方が変わる。")
        self.play(FadeIn(cap), run_time=0.45)
        self.wait(1.6)
        self._clear(VGroup(heading, formulas, cap))

    def step3_drop_terms(self):
        heading = self._section_title("STEP 3  ビッグOの落とし方")
        start = MathTex(r"T(n) = 3n + 5", font_size=40)
        start.next_to(heading, DOWN, buff=0.35)
        self.play(Write(start), run_time=0.7)
        self.wait(1.1)

        headers = VGroup(
            MathTex(r"n", font_size=28),
            MathTex(r"3n", font_size=28),
            MathTex(r"+5", font_size=28),
            MathTex(r"T(n)", font_size=28),
        ).arrange(RIGHT, buff=0.85)
        data = [
            (r"10", r"30", r"5", r"35"),
            (r"100", r"300", r"5", r"305"),
            (r"1000", r"3000", r"5", r"3005"),
        ]
        table_rows = VGroup()
        for row in data:
            table_rows.add(VGroup(*[MathTex(cell, font_size=28) for cell in row]).arrange(RIGHT, buff=0.7))
        table = VGroup(headers, *table_rows).arrange(DOWN, buff=0.18)
        table.next_to(start, DOWN, buff=0.35)
        self.play(FadeIn(headers), run_time=0.35)
        for row, (n, three, five, t) in zip(table_rows, data):
            self.play(FadeIn(row[0]), run_time=0.2)
            self.wait(0.25)
            self.play(FadeIn(row[1]), run_time=0.25)
            self.play(FadeIn(row[2]), run_time=0.25)
            self.play(FadeIn(row[3]), run_time=0.25)
            self.wait(0.7)

        note = self.ja_text("n が大きいと、足してある 5 はほとんど見えない。3 倍という定数も、「何倍で増えるか」には効かない。", font_size=22)
        note.to_edge(DOWN, buff=0.28)
        self.play(FadeIn(note), run_time=0.45)
        self.wait(2.0)
        self.play(FadeOut(table), FadeOut(note), run_time=0.4)

        defn = self.ja_text("「T(n) が O(g(n))」とは、ある定数 c と、ある番号 n0 があって、", font_size=24)
        defn2 = MathTex(r"n \ge n_0 \quad\Rightarrow\quad T(n)\le c\cdot g(n)", font_size=34)
        defn3 = self.ja_text("がいつも成り立つ、ということ。", font_size=24)
        defn_g = VGroup(defn, defn2, defn3).arrange(DOWN, buff=0.22)
        defn_g.next_to(start, DOWN, buff=0.4)
        for row in defn_g:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.2)

        self.play(FadeOut(defn_g), run_time=0.35)
        steps = VGroup(
            MathTex(r"n \ge 5 \ \Rightarrow\  5 \le n", font_size=32),
            MathTex(r"3n + 5 \le 3n + n", font_size=32),
            MathTex(r"3n + n = 4n", font_size=32),
            MathTex(r"n \ge 5 \ \Rightarrow\  T(n) \le 4n", font_size=32),
            MathTex(r"c=4,\quad g(n)=n,\quad n_0=5", font_size=32),
            MathTex(r"3n+5 = O(n)", font_size=40, color=YELLOW),
        ).arrange(DOWN, buff=0.18)
        steps.next_to(start, DOWN, buff=0.32)
        for row in steps:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.15)

        extra = VGroup(
            self.ja_text("3n+5 は", font_size=24),
            MathTex(r"O(n^2)", font_size=28),
            self.ja_text("でもある。上から抑えられてはいる。", font_size=24),
        ).arrange(RIGHT, buff=0.1)
        extra2 = self.ja_text("ただし普通は、ぴったりの型である O(n) のほうを書く。", font_size=24)
        extras = VGroup(extra, extra2).arrange(DOWN, buff=0.12)
        extras.to_edge(DOWN, buff=0.22)
        self.play(FadeIn(extras), run_time=0.45)
        self.wait(2.0)
        cap = self.ja_text("定数倍と、増えの遅い項は落とす。残るのがビッグOの中身。", font_size=24)
        cap.to_edge(DOWN, buff=0.22)
        self.play(FadeOut(extras), FadeIn(cap), run_time=0.45)
        self.wait(1.7)
        self._clear(VGroup(heading, start, steps, cap))

    def step4_common_orders(self):
        heading = self._section_title("STEP 4  よく出るオーダー")
        rows_spec = [
            (r"O(1)", "n が何倍でも、仕事の回数はほぼ同じ"),
            (r"O(\log n)", "n が2倍になると、仕事がだいたい 1 回増える"),
            (r"O(n)", "n が2倍になると、仕事も2倍"),
            (r"O(n\log n)", "ソートなどでよく出る。n 倍より少しだけ多い"),
            (r"O(n^2)", "n が2倍になると、仕事は4倍"),
            (r"O(2^n)", "n が1増えるだけで、仕事がだいたい2倍"),
        ]
        rows = VGroup()
        for tex, ja in rows_spec:
            left = MathTex(tex, font_size=30)
            right = self.ja_text(ja, font_size=22)
            row = VGroup(left, right).arrange(RIGHT, buff=0.28)
            rows.add(row)
        rows.arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        rows.next_to(heading, DOWN, buff=0.28)
        for row in rows:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.05)
        self.wait(0.4)
        self.play(FadeOut(rows), run_time=0.35)

        col_heads = [
            r"n",
            r"1",
            r"\log n",
            r"n",
            r"n\log n",
            r"n^2",
            r"2^n",
        ]
        data = [
            [r"2", r"1", r"1", r"2", r"2", r"4", r"4"],
            [r"4", r"1", r"2", r"4", r"8", r"16", r"16"],
            [r"8", r"1", r"3", r"8", r"24", r"64", r"256"],
            [r"16", r"1", r"4", r"16", r"64", r"256", r"65536"],
        ]
        header_row = VGroup(*[MathTex(h, font_size=26) for h in col_heads]).arrange(RIGHT, buff=0.42)
        table_rows = VGroup()
        for raw in data:
            table_rows.add(VGroup(*[MathTex(c, font_size=26) for c in raw]).arrange(RIGHT, buff=0.42))
        table = VGroup(header_row, *table_rows).arrange(DOWN, buff=0.16)
        table.next_to(heading, DOWN, buff=0.3)
        self.play(FadeIn(header_row), run_time=0.35)
        for row in table_rows:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(0.85)

        note = self.ja_text("n=16 のとき、2^n だけ桁が違う。", font_size=24)
        note.next_to(table, DOWN, buff=0.28)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(0.8)

        labels = [r"1", r"\log n", r"n", r"n\log n", r"n^2", r"2^n"]
        values = [1, 4, 16, 64, 256, 65536]
        unit = 2.4 / 256
        bars = VGroup()
        for lab, val, color in zip(
            labels,
            values,
            [GREY_B, BLUE, TEAL, GREEN, ORANGE, RED],
        ):
            height = min(val * unit, 3.6)
            rect = Rectangle(width=0.7, height=max(height, 0.12), color=color, fill_opacity=0.85, stroke_width=0)
            rect.align_to(ORIGIN, DOWN)
            name = MathTex(lab, font_size=20)
            name.next_to(rect, DOWN, buff=0.1)
            num = MathTex(str(val), font_size=18, color=color)
            num.next_to(rect, UP, buff=0.08)
            bars.add(VGroup(rect, name, num))
        bars.arrange(RIGHT, buff=0.28, aligned_edge=DOWN)
        bars.scale(0.72)
        bars.to_edge(DOWN, buff=0.22)
        self.play(FadeOut(note), FadeIn(bars), run_time=0.6)
        boom = self.ja_text("2^n の棒は、この画面では上に突き抜ける。", font_size=22, color=RED)
        boom.next_to(table, DOWN, buff=0.2)
        self.play(FadeIn(boom), run_time=0.4)
        self.wait(1.6)
        cap = self.ja_text("ビッグOは「このグループの増え方」を指す名前だと思ってよい。", font_size=24)
        cap.to_edge(DOWN, buff=0.18)
        self.play(FadeOut(bars), FadeOut(boom), FadeIn(cap), run_time=0.45)
        self.wait(1.7)
        self._clear(VGroup(heading, table, cap))

    def worked_example(self):
        heading = self._section_title("実例  同じ値が2つあるか")
        q = self.ja_text("長さ n の配列に、同じ値が2つ以上あるかどうかを知りたい。", font_size=24)
        q.next_to(heading, DOWN, buff=0.28)
        self.play(FadeIn(q), run_time=0.45)
        self.wait(1.3)

        values = [4, 1, 4, 2]
        boxes = self._boxes(values, color=BLUE)
        boxes.next_to(q, DOWN, buff=0.3)
        idx = self._index_labels(boxes)
        self.play(FadeIn(boxes), FadeIn(idx), run_time=0.5)
        dup = self.ja_text("同じ 4 が2つある。", font_size=24, color=YELLOW)
        dup.next_to(boxes, RIGHT, buff=0.4)
        self.play(FadeIn(dup), run_time=0.4)
        self.wait(1.1)

        method = self.ja_text("手順A  すべてのペアを比べる。自分より右の箱とだけ比べる。", font_size=24)
        method.next_to(idx, DOWN, buff=0.28)
        self.play(FadeIn(method), run_time=0.4)
        self.wait(1.2)

        pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
        pair_labels = VGroup()
        count_txt = self.ja_text("ペア  0", font_size=24)
        count_txt.next_to(method, DOWN, buff=0.22)
        self.play(FadeIn(count_txt), run_time=0.25)
        last_line = None
        last_cmp = None
        for k, (i, j) in enumerate(pairs, start=1):
            line = Line(
                boxes[i].get_top() + UP * 0.08,
                boxes[j].get_top() + UP * 0.08,
                color=YELLOW if values[i] == values[j] else GREY_B,
                stroke_width=3,
            ).shift(UP * (0.08 * ((i + j) % 3)))
            a, b = values[i], values[j]
            same = a == b
            cmp_tex = MathTex(rf"{a} = {b}" if same else rf"{a} \neq {b}", font_size=28)
            cmp_tex.next_to(count_txt, RIGHT, buff=0.45)
            ja = self.ja_text("同じ。" if same else "違う。", font_size=22)
            ja.next_to(cmp_tex, RIGHT, buff=0.15)
            new_count = self.ja_text(f"ペア  {k}", font_size=24)
            new_count.move_to(count_txt)
            anims = [Create(line), Transform(count_txt, new_count), FadeIn(cmp_tex), FadeIn(ja)]
            if last_cmp is not None:
                anims.append(FadeOut(last_cmp))
            self.play(*anims, run_time=0.45)
            self.wait(0.75)
            if same:
                found = self.ja_text("ここで「ある」と分かるが、最悪の回数を見るので数え切る。", font_size=20)
                found.next_to(count_txt, DOWN, buff=0.18).to_edge(LEFT, buff=0.7)
                self.play(FadeIn(found), run_time=0.35)
                self.wait(1.2)
                self.play(FadeOut(found), run_time=0.25)
            pair_labels.add(line)
            last_cmp = VGroup(cmp_tex, ja)

        six = self.ja_text("n=4 のとき、ペアは 6 本。", font_size=24)
        six.next_to(method, DOWN, buff=0.7)
        self.play(FadeOut(count_txt), FadeOut(last_cmp), FadeIn(six), run_time=0.4)
        self.wait(1.1)

        self.play(FadeOut(VGroup(boxes, idx, dup, method, pair_labels, six, q)), run_time=0.4)

        formulas = VGroup(
            VGroup(self.ja_text("1番目は残り", font_size=26), MathTex(r"n-1", font_size=30), self.ja_text("個と比べる。", font_size=26)).arrange(RIGHT, buff=0.1),
            VGroup(self.ja_text("2番目は残り", font_size=26), MathTex(r"n-2", font_size=30), self.ja_text("個と比べる。", font_size=26)).arrange(RIGHT, buff=0.1),
            self.ja_text("……", font_size=26),
            VGroup(self.ja_text("(n-1) 番目は残り 1 個と比べる。", font_size=26)).arrange(RIGHT, buff=0.1),
            MathTex(r"T(n)=(n-1)+(n-2)+\cdots+1", font_size=34),
            MathTex(r"T(n)=\dfrac{n(n-1)}{2}", font_size=36),
            MathTex(r"n=4:\quad \dfrac{4\cdot 3}{2}=6", font_size=34),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        formulas.next_to(heading, DOWN, buff=0.32)
        for row in formulas:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.0)
        match = self.ja_text("さっきの 6 本と一致する。", font_size=24)
        match.next_to(formulas, DOWN, buff=0.22)
        self.play(FadeIn(match), run_time=0.35)
        self.wait(1.2)

        self.play(FadeOut(formulas), FadeOut(match), run_time=0.35)
        expand = VGroup(
            MathTex(r"\dfrac{n(n-1)}{2}", font_size=36),
            MathTex(r"= \dfrac{n^2-n}{2}", font_size=36),
            MathTex(r"= \dfrac{1}{2}n^2 - \dfrac{1}{2}n", font_size=36),
        ).arrange(DOWN, buff=0.22)
        expand.next_to(heading, DOWN, buff=0.4)
        for row in expand:
            self.play(Write(row), run_time=0.7)
            self.wait(1.05)
        drop = VGroup(
            VGroup(self.ja_text("大きい項は", font_size=26), MathTex(r"\frac{1}{2}n^2", font_size=32)).arrange(RIGHT, buff=0.12),
            VGroup(
                self.ja_text("定数", font_size=26),
                MathTex(r"\frac{1}{2}", font_size=32),
                self.ja_text("と、小さい項", font_size=26),
                MathTex(r"\frac{1}{2}n", font_size=32),
                self.ja_text("を落とす。", font_size=26),
            ).arrange(RIGHT, buff=0.1),
            MathTex(r"O(n^2)", font_size=44, color=YELLOW),
        ).arrange(DOWN, buff=0.22)
        drop.next_to(expand, DOWN, buff=0.3)
        for row in drop:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.15)

        self.play(FadeOut(expand), FadeOut(drop), run_time=0.35)
        b_title = self.ja_text("手順B  回数だけ見る（並べ替えの中身は後の回）", font_size=26)
        b_title.next_to(heading, DOWN, buff=0.4)
        self.play(FadeIn(b_title), run_time=0.4)
        self.wait(1.0)
        b_lines = VGroup(
            VGroup(
                self.ja_text("並べ替えがだいたい", font_size=26),
                MathTex(r"O(n\log n)", font_size=32),
                self.ja_text("。", font_size=26),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                self.ja_text("隣同士の比較が", font_size=26),
                MathTex(r"O(n)", font_size=32),
                self.ja_text("。", font_size=26),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                self.ja_text("合わせると", font_size=26),
                MathTex(r"O(n\log n)", font_size=36, color=YELLOW),
                self.ja_text("。", font_size=26),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        b_lines.next_to(b_title, DOWN, buff=0.35)
        for row in b_lines:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.15)

        cmp16 = VGroup(
            self.ja_text("n=16 での回数の目安", font_size=24),
            MathTex(r"A:\ \dfrac{16\cdot 15}{2}=120", font_size=32),
            MathTex(r"B:\ 16\times 4=64\quad (n\log n)", font_size=32),
        ).arrange(DOWN, buff=0.2)
        cmp16.next_to(b_lines, DOWN, buff=0.35)
        for row in cmp16:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.05)

        cap = self._caption("同じ問題でも、手順を変えるとオーダーが変わる。だからビッグOで先に比べる。")
        self.play(FadeIn(cap), run_time=0.45)
        self.wait(1.9)
        self._clear(VGroup(heading, b_title, b_lines, cmp16, cap))

    def summary(self):
        heading = self._section_title("まとめ")
        items = VGroup(
            VGroup(
                MathTex(r"1.", font_size=30),
                self.ja_text("計算量は、n に対する操作回数", font_size=26),
                MathTex(r"T(n)", font_size=30),
                self.ja_text("の増え方。", font_size=26),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                MathTex(r"2.", font_size=30),
                self.ja_text("ビッグOは上からの抑え。定数倍と小さい項は落とす。", font_size=26),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                MathTex(r"3.", font_size=30),
                self.ja_text("よく使う型は", font_size=26),
                MathTex(r"O(1),\ O(\log n),\ O(n),", font_size=28),
            ).arrange(RIGHT, buff=0.1),
            MathTex(r"O(n\log n),\ O(n^2),\ O(2^n)", font_size=30),
        ).arrange(DOWN, buff=0.32, aligned_edge=LEFT)
        items.next_to(heading, DOWN, buff=0.5)
        for row in items:
            self.play(FadeIn(row), run_time=0.45)
            self.wait(1.4)
        cap = self._caption("「何秒か」より先に、「n が増えたとき何倍になるか」を見る。")
        self.play(FadeIn(cap), run_time=0.45)
        self.wait(1.8)
        self._clear(VGroup(heading, items, cap))

    def next_preview(self):
        heading = self._section_title("次回")
        nxt = self.ja_text("#3 時間計算量と空間計算量", font_size=32, color=YELLOW)
        nxt.next_to(heading, DOWN, buff=0.55)
        self.play(FadeIn(nxt), run_time=0.5)
        self.wait(1.2)
        body = VGroup(
            self.ja_text("今日は回数、つまり時間のほうを見た。", font_size=26),
            self.ja_text("次回は、同じ手順がメモリをどれだけ使うか、", font_size=26),
            self.ja_text("空間計算量を並べて見る。", font_size=26),
        ).arrange(DOWN, buff=0.28)
        body.next_to(nxt, DOWN, buff=0.45)
        for row in body:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.2)
        self.wait(1.4)
