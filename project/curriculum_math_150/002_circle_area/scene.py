from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import LessonScene


class CircleArea(LessonScene):
    """#2 円の面積はなぜ πr² か（約6分）"""

    GRID_N = 7
    GRID_R = 3.0
    GRID_SIDE = 0.40

    def construct(self):
        self.header = self._open_header()
        self.part_question()
        self.part_trial_grid()
        self.part_trial_sectors()
        self.part_step1_pi()
        self.part_step2_similar()
        self.part_step3_refine()
        self.part_step4_triangles()
        self.part_example()
        self.part_generalize()
        self.part_summary()

    def _open_header(self):
        title = self._line("円の面積はなぜ", MathTex(r"\pi r^2", font_size=44), "か", font_size=40)
        self.play(FadeIn(title), run_time=0.8)
        self.linger(1.2)
        self.play(title.animate.scale(0.55).to_edge(UP, buff=0.16), run_time=0.5)
        return title

    def part_question(self):
        circ, r_line, r_lab = self._radius_circle(1.35, color=BLUE, label=r"r")
        left = VGroup(circ, r_line, r_lab)
        left.next_to(self.header, DOWN, buff=0.55)
        left.to_edge(LEFT, buff=0.7)
        self.play(Create(circ), run_time=0.8)
        self.play(Create(r_line), FadeIn(r_lab), run_time=0.5)
        self.play(ShowPassingFlash(circ.copy().set_color(ORANGE), time_width=0.45), run_time=1.1)
        self.linger(1.0)

        card_c = self._idea_card("周は", r"2\pi r", BLUE, extra_math=True)
        card_s = self._idea_card("面積は", r"?", GREY_B, extra_math=True)
        cards = VGroup(card_c, card_s).arrange(DOWN, buff=0.28)
        cards.next_to(left, RIGHT, buff=0.85)
        cards.set_y(left.get_y())
        self.play(FadeIn(card_c), run_time=0.5)
        self.linger("周は 2πr")
        self.play(FadeIn(card_s), run_time=0.5)
        self.linger(1.0)

        q1 = self._line("周には", MathTex(r"\pi", font_size=32), "が出てきます。", font_size=26)
        q1.next_to(VGroup(left, cards), DOWN, buff=0.4)
        q1.set_x(0)
        self.play(FadeIn(q1), run_time=0.5)
        self.linger("周には π が出てきます。")

        q2 = self._line(
            "面積が",
            MathTex(r"r^2", font_size=32),
            "に比例するとして、比例定数が同じ",
            MathTex(r"\pi", font_size=32),
            "なのはなぜでしょう。",
            font_size=26,
        )
        self.stack_below(q2, q1, buff=0.22)
        q2.set_x(0)
        self._fit(q2, 13.0)
        q2.set_x(0)
        self.play(FadeIn(q2), run_time=0.5)
        self.linger("比例定数が同じ π なのはなぜでしょう。", extra=0.4)

    def part_trial_grid(self):
        self.wipe(self.header)
        chip = self.step_label("試行  方眼")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("まず、方眼に円を載せて、マスを数えてみます。", font_size=26)
        self.below_chip(lead, chip, buff=0.3)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.5)
        self.linger(lead.text)

        grid, counts = self._grid_circle()
        self.stack_below(grid, lead, buff=0.28)
        grid.to_edge(LEFT, buff=0.55)
        self.play(FadeIn(grid.circle), FadeIn(grid.lines), run_time=0.6)
        self.linger(1.0)

        insides = [c for c in grid.cells if c.kind == "in"]
        edges = [c for c in grid.cells if c.kind == "edge"]
        self.play(*[c.animate.set_fill(GREEN, 0.45).set_stroke(GREEN, 1.2) for c in insides], run_time=0.9)
        self.linger(3.2)
        self.play(*[c.animate.set_fill(ORANGE, 0.4).set_stroke(ORANGE, 1.2) for c in edges], run_time=0.9)
        self.linger(3.2)

        nums = VGroup(
            self._line("内側  ", MathTex(str(counts["in"]), font_size=34, color=GREEN), font_size=26),
            self._line("境界  ", MathTex(str(counts["edge"]), font_size=34, color=ORANGE), font_size=26),
            self.ja_text("境界は半分とも言い切れません。", font_size=22, color=GREY_B),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        nums.next_to(grid, RIGHT, buff=0.55)
        nums.align_to(grid, UP)
        for row in nums:
            self.play(FadeIn(row), run_time=0.4)
            self.linger(1.6)

        note1 = self.ja_text("マスを数えても、境界が残るので近似にしかなりません。", font_size=24)
        note1.next_to(grid, DOWN, buff=0.32)
        note1.set_x(0)
        self.play(FadeIn(note1), run_time=0.45)
        self.linger(note1.text)

        note2 = self.ja_text("円を正方形で埋め尽くすやり方は、ここで破綻します。", font_size=24, color=ORANGE)
        self.stack_below(note2, note1, buff=0.16)
        note2.set_x(0)
        self.play(FadeIn(note2), run_time=0.45)
        self.linger(note2.text, extra=0.5)

    def part_trial_sectors(self):
        self.wipe(self.header)
        chip = self.step_label("試行  扇に切る")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("こんどは、円を同じ扇形に切って、互い違いに並べます。", font_size=26)
        self.below_chip(lead, chip, buff=0.3)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.5)
        self.linger(lead.text)

        n, r = 6, 1.25
        pieces = self._circle_pieces(n, r)
        pieces.next_to(lead, DOWN, buff=0.45)
        pieces.to_edge(LEFT, buff=0.7)
        r_line = Line(pieces.get_center(), pieces.get_center() + RIGHT * r, color=YELLOW, stroke_width=3)
        r_lab = MathTex(r"r", font_size=30, color=YELLOW).next_to(r_line, DOWN, buff=0.08)
        self.play(FadeIn(pieces), run_time=0.7)
        self.play(Create(r_line), FadeIn(r_lab), run_time=0.45)
        self.linger(3.2)

        arranged = self._arranged_pieces(n, r)
        arranged.next_to(pieces, RIGHT, buff=0.7)
        arranged.set_y(pieces.get_y() - 0.15)
        self.play(FadeOut(r_line), FadeOut(r_lab), run_time=0.25)
        self.play(TransformFromCopy(pieces, arranged), run_time=1.3)
        self.linger(3.2)

        note1 = self.ja_text("だいたい長方形に見えます。でも弧が残ります。", font_size=24, color=ORANGE)
        note1.next_to(VGroup(pieces, arranged), DOWN, buff=0.4)
        note1.set_x(0)
        self.play(FadeIn(note1), run_time=0.45)
        self.linger(note1.text)

        note2 = self.ja_text("この粗さのままでは、横の長さも縦の長さも、まだ言い切れません。", font_size=24)
        self.stack_below(note2, note1, buff=0.16)
        note2.set_x(0)
        self.play(FadeIn(note2), run_time=0.45)
        self.linger(note2.text, extra=0.3)

    def part_step1_pi(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 1  円周率")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self._line("周に出ていた", MathTex(r"\pi", font_size=32), "を、先に言葉で置きます。", font_size=26)
        self.below_chip(lead, chip, buff=0.32)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.5)
        self.linger("周に出ていた π を、先に言葉で置きます。")

        rows = [
            self._line("直径を", MathTex(r"2r", font_size=34), "、周を", MathTex(r"C", font_size=34), "と書く", font_size=26),
            self._line(MathTex(r"\pi", font_size=34), "は、周を直径で割った比", font_size=26),
            MathTex(r"\pi=\dfrac{C}{2r}", font_size=42, color=YELLOW),
            MathTex(r"C=2\pi r", font_size=42, color=GREEN),
        ]
        self._formula_rows(rows, lead, buff=0.3)
        self.linger(3.4)

        note = self.ja_text("どの半径でも、この比は同じです。今回はこれを使います。", font_size=24)
        note.to_edge(DOWN, buff=0.42)
        note.set_x(0)
        self.play(FadeIn(note), run_time=0.4)
        self.linger(note.text, extra=0.3)

    def part_step2_similar(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 2  相似")
        self.play(FadeIn(chip), run_time=0.4)

        small, s_line, s_lab = self._radius_circle(0.70, color=BLUE, label=r"1")
        big, b_line, b_lab = self._radius_circle(1.40, color=TEAL, label=r"r")
        left = VGroup(small, s_line, s_lab)
        right = VGroup(big, b_line, b_lab)
        mid = self._line(MathTex(r"r", font_size=30, color=YELLOW), "倍に拡大", font_size=22)
        pair = VGroup(left, mid, right).arrange(RIGHT, buff=0.42, aligned_edge=DOWN)
        self.below_chip(pair, chip, buff=0.28)
        pair.set_x(0)
        mid.align_to(left, UP).shift(DOWN * 0.55)

        s_area = self._line("面積", MathTex(r"c", font_size=30, color=YELLOW), font_size=22)
        s_area.next_to(left, DOWN, buff=0.14)
        b_area = self._line("面積", MathTex(r"c r^2", font_size=30, color=YELLOW), font_size=22)
        b_area.next_to(right, DOWN, buff=0.14)

        self.play(FadeIn(left), run_time=0.55)
        self.linger(3.2)

        line1 = self._line(
            "半径",
            MathTex(r"1", font_size=30),
            "の円の面積を、",
            MathTex(r"c", font_size=30),
            "とおきます。",
            font_size=24,
        )
        line1.to_edge(DOWN, buff=0.38)
        line1.set_x(0)
        self.play(FadeIn(line1), FadeIn(s_area), run_time=0.5)
        self.linger("半径 1 の円の面積を、c とおきます。")

        line2 = self._line(
            "この円を",
            MathTex(r"r", font_size=30),
            "倍に拡大します。半径は",
            MathTex(r"r", font_size=30),
            "になります。",
            font_size=24,
        )
        line2.move_to(line1)
        self.play(FadeOut(line1), FadeIn(line2), FadeIn(mid), FadeIn(right), run_time=0.7)
        self.linger("この円を r 倍に拡大します。半径は r になります。")

        line3 = self._line(
            "相似なので、長さは",
            MathTex(r"r", font_size=30),
            "倍、面積は",
            MathTex(r"r^2", font_size=30),
            "倍です。",
            font_size=24,
        )
        line3.move_to(line2)
        self.play(FadeOut(line2), FadeIn(line3), run_time=0.5)
        self.linger("相似なので、長さは r 倍、面積は r² 倍です。")

        line4 = self._line(
            "だから拡大あとの面積は",
            MathTex(r"c r^2", font_size=32),
            "です。",
            font_size=24,
        )
        line4.move_to(line3)
        result = MathTex(r"S=c\,r^2", font_size=42, color=YELLOW)
        self.stack_below(result, pair, buff=0.22)
        result.set_x(0)
        # keep clear of area labels
        if result.get_top()[1] > s_area.get_bottom()[1] - 0.12:
            result.next_to(VGroup(s_area, b_area), DOWN, buff=0.22)
            result.set_x(0)
        self.play(FadeOut(line3), FadeIn(line4), FadeIn(b_area), FadeIn(result), run_time=0.55)
        self.linger(3.4)

        note = self._line(
            "残る問いは、定数",
            MathTex(r"c", font_size=28),
            "が",
            MathTex(r"\pi", font_size=28),
            "と同じかどうかです。",
            font_size=24,
        )
        note.move_to(line4)
        self.play(FadeOut(line4), FadeIn(note), run_time=0.45)
        self.linger("残る問いは、定数 c が π と同じかどうかです。", extra=0.35)

        self.play(
            FadeOut(pair),
            FadeOut(s_area),
            FadeOut(b_area),
            FadeOut(result),
            FadeOut(note),
            run_time=0.35,
        )
        circ = Circle(radius=1.15, color=BLUE, stroke_width=3)
        outer = Square(side_length=2.3, color=ORANGE, stroke_width=2)
        inner = Square(side_length=1.15 * np.sqrt(2), color=GREEN, stroke_width=2).rotate(PI / 4)
        fig = VGroup(outer, circ, inner)
        self.below_chip(fig, chip, buff=0.4)
        fig.to_edge(LEFT, buff=0.6)
        self.play(Create(outer), Create(circ), Create(inner), run_time=1.0)
        self.linger(3.2)
        bounds = [
            MathTex(r"(2r)^2=4r^2", font_size=32, color=ORANGE),
            self._line("内接は対角線", MathTex(r"2r", font_size=30), "なので", MathTex(r"2r^2", font_size=30), font_size=24),
            MathTex(r"2r^2<S<4r^2", font_size=32),
            MathTex(r"2<c<4", font_size=36, color=YELLOW),
            self._line(MathTex(r"\pi", font_size=30), "はこのあいだにある", font_size=24),
        ]
        block = VGroup(*bounds).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        block.next_to(fig, RIGHT, buff=0.55)
        block.align_to(fig, UP)
        for row in bounds:
            self.play(FadeIn(row), run_time=0.45)
            self.linger(3.2)

    def part_step3_refine(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 3  細く並べる")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("試行の扇を、枚数だけ増やします。", font_size=26)
        self.below_chip(lead, chip, buff=0.28)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        r = 1.15
        arranged = None
        dim_lab = None
        for n, wait in ((4, 3.2), (8, 3.2), (16, 3.2)):
            nxt = self._arranged_pieces(n, r)
            self.stack_below(nxt, lead, buff=0.4)
            nxt.set_x(-1.4)
            w = n * r * np.sin(PI / n)
            h = r * np.cos(PI / n)
            w_tex = MathTex(rf"n={n}", font_size=28, color=YELLOW)
            h_tex = MathTex(r"\approx r\cos(\pi/n)", font_size=26, color=YELLOW)
            wd_tex = MathTex(r"\approx nr\sin(\pi/n)", font_size=26, color=ORANGE)
            labs = VGroup(w_tex, h_tex, wd_tex).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
            labs.next_to(nxt, RIGHT, buff=0.45)
            if arranged is None:
                self.play(FadeIn(nxt), FadeIn(labs), run_time=0.7)
                arranged = nxt
                dim_lab = labs
            else:
                self.play(FadeOut(arranged), FadeIn(nxt), Transform(dim_lab, labs), run_time=0.85)
                arranged = nxt
            self.linger(wait)

        result = [
            self._line("横", MathTex(r"nr\sin(\pi/n)\to\pi r", font_size=34), font_size=26),
            self._line("縦", MathTex(r"r\cos(\pi/n)\to r", font_size=34), font_size=26),
            MathTex(r"(\pi r)\cdot r=\pi r^2", font_size=40, color=GREEN),
        ]
        block = VGroup(*result).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        block.next_to(arranged, DOWN, buff=0.32)
        block.set_x(0)
        for row in result:
            self.play(FadeIn(row), run_time=0.4)
            self.linger(3.2)

        alt = self.ja_text(
            "同じ向きに並べると、横が周、縦が半径の半分の長方形にも見えます。どちらも面積は同じです。",
            font_size=20,
            color=GREY_B,
        )
        alt.to_edge(DOWN, buff=0.22)
        alt.set_x(0)
        self._fit(alt, 13.0)
        alt.set_x(0)
        self.play(FadeIn(alt), run_time=0.4)
        self.linger(alt.text, extra=0.25)

    def part_step4_triangles(self):
        self.wipe(self.header)
        chip = self.step_label("STEP 4  三角形")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("中心から切った細い三角形の面積を、足しても同じ式になります。", font_size=24)
        self.below_chip(lead, chip, buff=0.3)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.5)
        self.linger(lead.text)

        tri_fig = self._thin_triangles(8, 1.2)
        self.stack_below(tri_fig, lead, buff=0.28)
        tri_fig.to_edge(LEFT, buff=0.55)
        self.play(FadeIn(tri_fig), run_time=0.7)
        self.linger(3.2)

        rows = [
            MathTex(r"\dfrac{1}{2}r\,\Delta s", font_size=34),
            self._line("弧を全部足すと周", MathTex(r"C=2\pi r", font_size=32), font_size=24),
            MathTex(r"S=\dfrac{1}{2}r\cdot 2\pi r", font_size=36),
            MathTex(r"S=\pi r^2", font_size=42, color=GREEN),
        ]
        block = VGroup(*rows).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        block.next_to(tri_fig, RIGHT, buff=0.55)
        block.align_to(tri_fig, UP)
        for row in rows:
            self.play(FadeIn(row), run_time=0.45)
            self.linger(3.2)

        check = self._line(
            "検算: 横",
            MathTex(r"2\pi r", font_size=28),
            "、縦",
            MathTex(r"r/2", font_size=28),
            "の長方形と同じ面積",
            font_size=22,
        )
        check.to_edge(DOWN, buff=0.38)
        check.set_x(0)
        self.play(FadeIn(check), run_time=0.4)
        self.linger("検算: 横 2πr、縦 r/2 の長方形と同じ面積", extra=0.35)

    def part_example(self):
        self.wipe(self.header)
        chip = self.step_label("実例")
        self.play(FadeIn(chip), run_time=0.4)

        lead = self.ja_text("半径 1 の円で、並べたあとの横と縦を、枚数ごとに計算します。", font_size=24)
        self.below_chip(lead, chip, buff=0.3)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        calc = [
            MathTex(r"4\sin(\pi/4)=2\sqrt{2}\approx 2.828", font_size=32),
            MathTex(r"\cos(\pi/4)=\dfrac{\sqrt{2}}{2}\approx 0.707", font_size=32),
            MathTex(r"2.828\times 0.707=2.000", font_size=32, color=YELLOW),
        ]
        calc_block = self._formula_rows(calc, lead, buff=0.26)
        self.play(FadeOut(calc_block), run_time=0.3)
        calc8 = [
            MathTex(r"8\sin(\pi/8)\approx 3.061", font_size=32),
            MathTex(r"\cos(\pi/8)\approx 0.924", font_size=32),
            MathTex(r"3.061\times 0.924=2.828", font_size=32, color=YELLOW),
        ]
        calc8_block = self._formula_rows(calc8, lead, buff=0.26)
        self.play(FadeOut(calc8_block), run_time=0.35)

        table = self.aligned_table(
            [
                [
                    MathTex(r"n", font_size=26, color=GREY_B),
                    MathTex(r"n\sin(\pi/n)", font_size=24, color=GREY_B),
                    MathTex(r"\cos(\pi/n)", font_size=24, color=GREY_B),
                    self.ja_text("積", font_size=20, color=GREY_B),
                ],
                [
                    MathTex(r"4", font_size=28),
                    MathTex(r"2.828", font_size=28),
                    MathTex(r"0.707", font_size=28),
                    MathTex(r"2.000", font_size=28),
                ],
                [
                    MathTex(r"8", font_size=28),
                    MathTex(r"3.061", font_size=28),
                    MathTex(r"0.924", font_size=28),
                    MathTex(r"2.828", font_size=28),
                ],
                [
                    MathTex(r"16", font_size=28),
                    MathTex(r"3.121", font_size=28),
                    MathTex(r"0.981", font_size=28),
                    MathTex(r"3.061", font_size=28),
                ],
                [
                    MathTex(r"\infty", font_size=28, color=GREEN),
                    MathTex(r"\pi", font_size=28, color=GREEN),
                    MathTex(r"1", font_size=28, color=GREEN),
                    MathTex(r"\pi", font_size=28, color=GREEN),
                ],
            ],
            h_buff=0.42,
            v_buff=0.16,
        )
        table.scale(0.82)
        self.stack_below(table, lead, buff=0.26)
        table.set_x(0)
        self.reveal_table(table, row_wait=0.95)

        notes = [
            self._line("有限の", MathTex(r"n", font_size=26), "では、積は", MathTex(r"\pi", font_size=26), "より小さい。", font_size=22),
            self._line("枚数を増やすと、弧の余りが消えて、積は", MathTex(r"\pi", font_size=26), "に近づきます。", font_size=22),
            self._line("半径 1 の面積が", MathTex(r"\pi", font_size=26), "なら、一般の半径では", MathTex(r"\pi r^2", font_size=26), "です。", font_size=22),
        ]
        shown = VGroup()
        for i, mob in enumerate(notes):
            if i == 0:
                self.stack_below(mob, table, buff=0.24)
            else:
                self.stack_below(mob, shown, buff=0.14)
            mob.set_x(0)
            self.play(FadeIn(mob), run_time=0.4)
            shown.add(mob)
            self.linger(3.2)

    def part_generalize(self):
        self.wipe(self.header)
        chip = self.step_label("一般化")
        self.play(FadeIn(chip), run_time=0.4)

        lines = [
            self.ja_text("今やったことは、取り尽くしと呼ばれる考え方でした。", font_size=26),
            self.ja_text("有限のマスや太い扇では、境界や弧が残ります。", font_size=26),
            self.ja_text("分割を細かくする極限で、残りは消えます。", font_size=26),
            self._line(
                "残った長方形の横が",
                MathTex(r"\pi r", font_size=30),
                "、縦が",
                MathTex(r"r", font_size=30),
                "なので、面積は",
                MathTex(r"\pi r^2", font_size=30),
                "です。",
                font_size=24,
            ),
        ]
        linger_texts = [
            "今やったことは、取り尽くしと呼ばれる考え方でした。",
            "有限のマスや太い扇では、境界や弧が残ります。",
            "分割を細かくする極限で、残りは消えます。",
            "残った長方形の横が πr、縦が r なので、面積は πr² です。",
        ]
        shown = VGroup()
        for i, (mob, text) in enumerate(zip(lines, linger_texts)):
            if i == 0:
                self.below_chip(mob, chip, buff=0.34)
            else:
                self.stack_below(mob, shown, buff=0.24)
            self._fit_left(mob)
            self.play(FadeIn(mob), run_time=0.5)
            shown.add(mob)
            self.linger(text)

        self.play(FadeOut(shown), run_time=0.35)

        lead = self.ja_text("横と縦の極限を、途中式で書きます。", font_size=26)
        self.below_chip(lead, chip, buff=0.30)
        self._fit_left(lead)
        self.play(FadeIn(lead), run_time=0.45)
        self.linger(lead.text)

        sub_rows = [
            MathTex(r"x=\dfrac{\pi}{n}", font_size=36, color=YELLOW),
            self._line(
                MathTex(r"n\to\infty", font_size=32),
                "のとき",
                MathTex(r"x\to 0", font_size=32),
                font_size=24,
            ),
            MathTex(r"n=\dfrac{\pi}{x}", font_size=34),
            MathTex(r"n\sin\dfrac{\pi}{n}=n\sin x", font_size=34),
            MathTex(r"n\sin x=\dfrac{\pi}{x}\sin x=\pi\cdot\dfrac{\sin x}{x}", font_size=34),
        ]
        sub_block = self._formula_rows(sub_rows, lead, buff=0.24)

        self.play(FadeOut(sub_block), run_time=0.3)
        lim_rows = [
            MathTex(r"\lim_{x\to 0}\dfrac{\sin x}{x}=1", font_size=36, color=YELLOW),
            self._line(
                "よって",
                MathTex(r"\lim_{n\to\infty}n\sin\dfrac{\pi}{n}=\pi", font_size=32),
                font_size=24,
            ),
            MathTex(r"\cos\dfrac{\pi}{n}=\cos x\to\cos 0=1", font_size=34),
        ]
        lim_block = self._formula_rows(lim_rows, lead, buff=0.24)

        self.play(FadeOut(lim_block), run_time=0.3)
        close_rows = [
            self._line("横", MathTex(r"r\cdot n\sin\dfrac{\pi}{n}\to\pi r", font_size=32), font_size=24),
            self._line("縦", MathTex(r"r\cos\dfrac{\pi}{n}\to r", font_size=32), font_size=24),
            MathTex(
                r"S=\lim_{n\to\infty}nr\sin\dfrac{\pi}{n}\cdot r\cos\dfrac{\pi}{n}",
                font_size=32,
            ),
            MathTex(r"=(\pi r)\cdot r=\pi r^2", font_size=40, color=GREEN),
        ]
        close_block = self._formula_rows(close_rows, lead, buff=0.22)
        self.linger(3.6)

    def part_summary(self):
        self.wipe(self.header)
        chip = self.step_label("まとめ")
        self.play(FadeIn(chip), run_time=0.35)

        rows = [
            self._line(
                MathTex(r"\pi", font_size=28),
                "は周を直径で割った比。だから周は",
                MathTex(r"2\pi r", font_size=28),
                font_size=24,
            ),
            self.ja_text("方眼や太い扇では、境界や弧が残って近似で止まる", font_size=24),
            self._line(
                "扇を細く並べると、横",
                MathTex(r"\pi r", font_size=28),
                "、縦",
                MathTex(r"r", font_size=28),
                "の長方形に近づく",
                font_size=24,
            ),
            self._line("だから円の面積は", MathTex(r"\pi r^2", font_size=30), font_size=24),
        ]
        shown = VGroup()
        for i, mob in enumerate(rows):
            if i == 0:
                self.below_chip(mob, chip, buff=0.36)
            else:
                self.stack_below(mob, shown, buff=0.26)
            self._fit_left(mob)
            self.play(FadeIn(mob), run_time=0.5)
            shown.add(mob)
            self.linger(3.2)

        related = self.ja_text("極座標で細い扇を足す話も、同じ取り尽くしで閉じます。", font_size=22, color=GREY_B)
        self.stack_below(related, shown, buff=0.36)
        self._fit_left(related)
        self.play(FadeIn(related), run_time=0.45)
        self.linger(related.text, extra=0.45)

    def _radius_circle(self, radius, color=BLUE, label=r"r"):
        circ = Circle(radius=radius, color=color, stroke_width=4)
        r_line = Line(circ.get_center(), circ.get_center() + RIGHT * radius, color=YELLOW, stroke_width=3)
        r_lab = MathTex(label, font_size=28, color=YELLOW)
        r_lab.next_to(r_line, DOWN, buff=0.08)
        return circ, r_line, r_lab

    def _grid_circle(self):
        n, r, side = self.GRID_N, self.GRID_R, self.GRID_SIDE
        cells = VGroup()
        counts = {"in": 0, "edge": 0, "out": 0}
        for i in range(n):
            for j in range(n):
                cx = (j - (n - 1) / 2) * side
                cy = (i - (n - 1) / 2) * side
                kind = self._cell_kind(j, i, n, r)
                counts[kind] += 1
                sq = Square(side_length=side * 0.92, color=GREY_B, stroke_width=1.1)
                sq.move_to([cx, cy, 0])
                sq.kind = kind
                if kind == "out":
                    sq.set_stroke(GREY_D, 0.8)
                    sq.set_fill(GREY_E, 0.15)
                cells.add(sq)
        circle = Circle(radius=r * side, color=WHITE, stroke_width=3)
        lines = VGroup()
        half = n * side / 2
        for k in range(n + 1):
            x = -half + k * side
            lines.add(Line([x, -half, 0], [x, half, 0], color=GREY_D, stroke_width=0.8))
            lines.add(Line([-half, x, 0], [half, x, 0], color=GREY_D, stroke_width=0.8))
        group = VGroup(lines, cells, circle)
        group.cells = cells
        group.circle = circle
        group.lines = lines
        return group, counts

    @staticmethod
    def _cell_kind(j, i, n, r):
        cx = j - (n - 1) / 2
        cy = i - (n - 1) / 2
        d2 = [(cx + dx) ** 2 + (cy + dy) ** 2 for dx in (-0.5, 0.5) for dy in (-0.5, 0.5)]
        if max(d2) <= r * r + 1e-9:
            return "in"
        if min(d2) >= r * r - 1e-9:
            return "out"
        return "edge"

    def _wedge(self, n, radius, color):
        return AnnularSector(
            inner_radius=0,
            outer_radius=radius,
            angle=TAU / n,
            start_angle=-TAU / (2 * n),
            color=color,
            fill_opacity=0.82,
            stroke_width=1.1,
            stroke_color=WHITE,
        )

    def _circle_pieces(self, n, radius):
        colors = [BLUE, TEAL]
        pieces = VGroup()
        for i in range(n):
            sec = self._wedge(n, radius, colors[i % 2])
            sec.rotate(PI / 2 + i * TAU / n, about_point=ORIGIN)
            pieces.add(sec)
        return pieces

    def _arranged_pieces(self, n, radius):
        colors = [BLUE, TEAL]
        chord = 2 * radius * np.sin(PI / n)
        h = radius * np.cos(PI / n)
        origin = np.array([0.0, 0.0, 0.0])
        pieces = VGroup()
        for i in range(n):
            sec = self._wedge(n, radius, colors[i % 2])
            x = origin[0] + i * chord / 2
            if i % 2 == 0:
                sec.rotate(PI / 2, about_point=ORIGIN)
                sec.shift(np.array([x, origin[1], 0.0]))
            else:
                sec.rotate(-PI / 2, about_point=ORIGIN)
                sec.shift(np.array([x, origin[1] + h, 0.0]))
            pieces.add(sec)
        return pieces

    def _thin_triangles(self, n, radius):
        colors = [BLUE, TEAL]
        pieces = self._circle_pieces(n, radius)
        for i, sec in enumerate(pieces):
            sec.set_fill(colors[i % 2], 0.55)
        r_line = Line(pieces.get_center(), pieces.get_center() + RIGHT * radius, color=YELLOW, stroke_width=3)
        r_lab = MathTex(r"r", font_size=26, color=YELLOW).next_to(r_line, DOWN, buff=0.06)
        arc = Arc(radius=radius, start_angle=0.15, angle=0.7, color=ORANGE, stroke_width=4)
        arc.move_arc_center_to(pieces.get_center())
        ds = MathTex(r"\Delta s", font_size=24, color=ORANGE)
        ds.next_to(arc, UR, buff=0.08)
        return VGroup(pieces, r_line, r_lab, arc, ds)

    def _idea_card(self, title, body, color, extra_math=False):
        box = RoundedRectangle(
            width=4.6,
            height=1.55,
            corner_radius=0.12,
            color=color,
            stroke_width=3,
            fill_color=color,
            fill_opacity=0.16,
        )
        t = self.ja_text(title, font_size=22, color=color)
        if extra_math:
            b = MathTex(body, font_size=36, color=color)
        else:
            b = self.ja_text(body, font_size=24)
        col = VGroup(t, b).arrange(DOWN, buff=0.16)
        col.move_to(box)
        return VGroup(box, col)

    def _line(self, *chunks, font_size=24, color=None, buff=0.08):
        parts = []
        for chunk in chunks:
            if isinstance(chunk, str):
                kw = {"font_size": font_size}
                if color is not None:
                    kw["color"] = color
                parts.append(self.ja_text(chunk, **kw))
            else:
                parts.append(chunk)
        return VGroup(*parts).arrange(RIGHT, buff=buff)

    def _formula_rows(self, rows, under, buff=0.36):
        block = VGroup(*rows).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        self.stack_below(block, under, buff=buff)
        block.set_x(0)
        self._fit(block, 12.6)
        block.set_x(0)
        for row in block:
            self.play(FadeIn(row), run_time=0.45)
            self.linger(3.2)
        return block

    def _fit(self, mob, max_w=12.4):
        if mob.width > max_w:
            mob.scale_to_fit_width(max_w)
        return mob

    def _fit_left(self, mob, max_w=12.2):
        left = mob.get_left().copy()
        self._fit(mob, max_w)
        mob.shift(left - mob.get_left())
        return mob
