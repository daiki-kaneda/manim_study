from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class Rigidity(PacedScene):
    """#506 剛性：辺長を保つ変形は合同のみ（約45秒）"""

    def construct(self):
        self.show_heading("剛性")
        self.draw_framework()
        self.flex()
        self.show_formula()
        self.read(1.4)

    def draw_framework(self):
        pts = [LEFT * 2.2 + UP * 1.0, RIGHT * 0.2 + UP * 1.3, RIGHT * 2.0 + UP * 0.2,
               RIGHT * 0.5 + DOWN * 1.3, LEFT * 2.0 + DOWN * 0.9]
        dots = VGroup(*[Dot(p, color=BLUE, radius=0.1) for p in pts])
        edges = VGroup(*[
            Line(pts[i], pts[j], color=GREY, stroke_width=3)
            for i, j in [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (0, 2), (1, 3)]
        ])
        self.play(LaggedStart(*[Create(e) for e in edges], lag_ratio=0.05), FadeIn(dots), run_time=1.4)
        note = self.ja_text("棒と関節", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def flex(self):
        lock = RegularPolygon(6, color=ORANGE, stroke_width=3).scale(0.55).shift(RIGHT * 2.6 + DOWN * 0.8)
        cap = self.ja_text("長さ固定", font_size=24).move_to(self.note)
        self.play(Create(lock), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("連続変形は剛体運動", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = self.ja_text("大域剛性：辺長が合同を決める", font_size=26)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
