from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class PolarTriangle(PacedScene):
    """#578 極三角形：極と極線が双対な三角形（約45秒）"""

    def construct(self):
        self.show_heading("極三角形")
        self.draw_circ()
        self.polar_tri()
        self.show_formula()
        self.read(1.4)

    def draw_circ(self):
        circ = Circle(radius=1.7, color=BLUE, stroke_width=3).shift(UP * 0.15)
        self.play(Create(circ), run_time=1.1)
        note = self.ja_text("基準円", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def polar_tri(self):
        pts = [UP * 2.2, LEFT * 2.5 + DOWN * 1.3, RIGHT * 2.6 + DOWN * 1.2]
        tri = Polygon(*pts, color=ORANGE, stroke_width=3)
        dots = VGroup(*[Dot(p, color=YELLOW, radius=0.09) for p in pts])
        cap = self.ja_text("頂点と対辺が極対", font_size=24).move_to(self.note)
        self.play(Create(tri), FadeIn(dots), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("自己配極", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = self.ja_text("極三角形：各頂点の極線が対辺", font_size=26)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
