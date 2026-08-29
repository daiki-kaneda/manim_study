from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class RectangularHyperbola(PacedScene):
    """#576 直角双曲線：漸近線が直交（約45秒）"""

    def construct(self):
        self.show_heading("直角双曲線")
        self.draw_hyp()
        self.asymptotes()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_hyp(self):
        axes = Axes(x_range=[-3, 3, 1], y_range=[-2.2, 2.2, 1], x_length=6.5, y_length=3.2, tips=False,
                    axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.1)
        right = axes.plot(lambda x: 1.0 / x, x_range=[0.45, 2.8], color=BLUE, stroke_width=4)
        left = axes.plot(lambda x: 1.0 / x, x_range=[-2.8, -0.45], color=BLUE, stroke_width=4)
        self.play(Create(axes), Create(right), Create(left), run_time=1.4)
        note = self.ja_text("xy=c", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def asymptotes(self):
        a1 = DashedLine(LEFT * 3 + DOWN * 1.8, RIGHT * 3 + UP * 1.8, color=ORANGE, stroke_width=3)
        a2 = DashedLine(LEFT * 3 + UP * 1.8, RIGHT * 3 + DOWN * 1.8, color=ORANGE, stroke_width=3)
        # for xy=c asymptotes are axes - use axis-aligned
        a1 = DashedLine(LEFT * 3.2, RIGHT * 3.2, color=ORANGE, stroke_width=3).shift(UP * 0.1)
        a2 = DashedLine(DOWN * 2.0, UP * 2.0, color=ORANGE, stroke_width=3)
        cap = self.ja_text("漸近線が直交", font_size=24).move_to(self.note)
        self.play(Create(a1), Create(a2), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("直角双曲線", font_size=24).move_to(self.note)
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
        eq = MathTex(r"xy").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"xy=c\quad(a=b)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"xy=c\quad(a=b)").scale(0.9)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
