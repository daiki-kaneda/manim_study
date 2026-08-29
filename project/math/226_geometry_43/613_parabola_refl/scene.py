from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class ParabolaReflection(PacedScene):
    """#613 放物線の反射：軸平行入射が焦点へ集まる（約45秒）"""

    def construct(self):
        self.show_heading("放物線の反射")
        self.draw_mirror()
        self.rays()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_mirror(self):
        axes = Axes(x_range=[-0.2, 2.5, 1], y_range=[-2, 2, 1], x_length=4.0, y_length=3.2,
                    tips=False, axis_config={"stroke_width": 1, "include_ticks": False}).shift(LEFT * 0.6 + UP * 0.1)
        pts = [axes.c2p(0.45 * (t ** 2), t) for t in [-1.8 + i * 0.1 for i in range(37)]]
        para = VMobject(color=BLUE, stroke_width=4).set_points_as_corners(pts)
        focus = Dot(axes.c2p(0.45, 0), color=YELLOW, radius=0.1)
        self.play(Create(axes), Create(para), FadeIn(focus), run_time=1.3)
        note = self.ja_text("鏡面反射", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.axes = axes
        self.focus = focus

    def rays(self):
        rays = VGroup()
        for y in [-1.2, -0.5, 0.5, 1.2]:
            hit = self.axes.c2p(0.45 * (y ** 2), y)
            incoming = Arrow(hit + RIGHT * 2.2, hit, buff=0.02, color=ORANGE, stroke_width=3, max_tip_length_to_length_ratio=0.12)
            to_f = Arrow(hit, self.focus.get_center(), buff=0.05, color=TEAL, stroke_width=3, max_tip_length_to_length_ratio=0.15)
            rays.add(incoming, to_f)
        cap = self.ja_text("平行光が焦点へ", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[GrowArrow(r) for r in rays], lag_ratio=0.05), Transform(self.note, cap), run_time=1.5)
        self.read(0.25)
        cap2 = self.ja_text("接線の二等分", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"\ell\parallel\mathrm{axis}\ \Rightarrow\ \rightarrow F").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\ell\parallel\mathrm{axis}\ \Rightarrow\ \rightarrow F").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\ell\parallel\mathrm{axis}\ \Rightarrow\ \rightarrow F").scale(0.8)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
