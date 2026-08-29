from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class InverseIteration(PacedScene):
    """#334 逆反復法：シフト近くの固有ベクトルへ（約45秒）"""

    def construct(self):
        self.show_heading("逆反復法")
        self.draw_line()
        self.iterate()
        self.show_formula()
        self.read(1.4)

    def draw_line(self):
        self.O = LEFT * 0.4 + DOWN * 0.2
        ax = Line(self.O + LEFT * 3.0, self.O + RIGHT * 3.2, color=GREY, stroke_width=2)
        self.mu = Dot(self.O + RIGHT * 1.2, color=ORANGE, radius=0.1)
        eigs = VGroup(*[Dot(self.O + RIGHT * x, color=BLUE, radius=0.09) for x in [-1.5, 0.2, 1.35]])
        self.play(Create(ax), FadeIn(eigs), FadeIn(self.mu), run_time=1.4)
        note = self.ja_text("シフト μ", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.eigs = eigs

    def iterate(self):
        # arrows shrinking toward nearest eig
        target = self.eigs[2]
        arrows = VGroup()
        pts = [self.O + UP * 1.6 + LEFT * 0.5, self.O + UP * 1.0 + RIGHT * 0.4, self.O + UP * 0.45 + RIGHT * 1.0]
        for i, p in enumerate(pts):
            nxt = pts[i + 1] if i + 1 < len(pts) else target.get_center() + UP * 0.25
            arrows.add(Arrow(p, nxt, buff=0.05, color=YELLOW, stroke_width=3))
        cap = self.ja_text("逆を反復", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.15), Transform(self.note, cap), run_time=1.5)
        self.read(0.25)
        cap2 = self.ja_text("近い固有対へ", font_size=24).move_to(self.note)
        self.play(Indicate(target, color=YELLOW), Transform(self.note, cap2), run_time=1.1)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"(A-\mu I)v_{k+1}=v_k").scale(0.95)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
