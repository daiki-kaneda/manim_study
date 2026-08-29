from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class PascalTriangle(JapaneseScene):
    """#46 パスカルの三角形（約90秒）"""

    def construct(self):
        self.show_heading("パスカルの三角形")
        self.draw_triangle()
        self.highlight_rule()
        self.show_formula()
        self.hold(1.2)

    def draw_triangle(self):
        rows = [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1],
        ]
        self.cells = []
        origin = UP * 1.55
        gap_x, gap_y = 0.7, 0.72
        for r, row in enumerate(rows):
            line = []
            width = (len(row) - 1) * gap_x
            for c, val in enumerate(row):
                t = MathTex(str(val), font_size=32)
                t.move_to(origin + DOWN * r * gap_y + RIGHT * (c * gap_x - width / 2))
                line.append(t)
            self.cells.append(line)
        for r, line in enumerate(self.cells):
            self.play(LaggedStart(*[FadeIn(t) for t in line], lag_ratio=0.08), run_time=0.45)
            self.hold(0.2)
        self.hold(0.4)

    def highlight_rule(self):
        # 3+3=6 を強調（row 3 の 3,3 と row 4 の 6）
        a = self.cells[3][1]
        b = self.cells[3][2]
        s = self.cells[4][2]
        self.play(a.animate.set_color(BLUE), b.animate.set_color(BLUE), run_time=0.4)
        self.play(s.animate.set_color(YELLOW), run_time=0.4)
        note = self.ja_text("上の 2 つを足す", font_size=26)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 0.2)
        self.play(FadeIn(note), run_time=0.4)
        self.hold(0.8)

    def show_formula(self):
        formula = MathTex(r"\binom{n}{k}=\binom{n-1}{k-1}+\binom{n-1}{k}").scale(0.9)
        formula.to_edge(DOWN, buff=0.38)
        self.play(Write(formula), run_time=1.05)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
