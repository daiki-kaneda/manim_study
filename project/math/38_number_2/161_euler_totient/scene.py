from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import math
from manim import *
from manim_math import PacedScene


class EulerTotient(PacedScene):
    """#161 オイラーの φ（約50秒）"""

    def construct(self):
        self.origin = LEFT * 2.15 + DOWN * 0.1
        self.show_heading("オイラーの φ")
        self.draw_clock()
        self.highlight_coprime()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_clock(self):
        n = 12
        r = 1.85
        ring = Circle(radius=r, color=GREY, stroke_width=3).move_to(self.origin)
        self.play(Create(ring), run_time=1.2)
        self.dots = VGroup()
        self.labs = VGroup()
        for k in range(n):
            ang = PI / 2 - k * TAU / n
            p = self.origin + RIGHT * (r * math.cos(ang)) + UP * (r * math.sin(ang))
            self.dots.add(Dot(p, radius=0.08, color=WHITE))
            self.labs.add(MathTex(str(k), font_size=22).move_to(p + 0.38 * (p - self.origin)))
        self.play(LaggedStart(*[FadeIn(d, scale=0.4) for d in self.dots], lag_ratio=0.06), run_time=1.4)
        self.play(FadeIn(self.labs), run_time=0.5)
        note = self.ja_text("12 個", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def highlight_coprime(self):
        good = {1, 5, 7, 11}
        cap = self.ja_text("素な点", font_size=24).move_to(self.note)
        anims = []
        for k, d in enumerate(self.dots):
            if k in good:
                anims.append(d.animate.set_color(YELLOW).scale(1.35))
                anims.append(self.labs[k].animate.set_color(YELLOW))
            else:
                anims.append(d.animate.set_opacity(0.25))
                anims.append(self.labs[k].animate.set_opacity(0.25))
        self.play(*anims, Transform(self.note, cap), run_time=0.95)
        self.read(0.3)
        count = MathTex(r"\varphi(12)=4", color=YELLOW, font_size=40)
        count.move_to(self.origin + RIGHT * 3.35 + DOWN * 0.35)
        cap2 = self.ja_text("4 個", font_size=24).move_to(self.note)
        self.play(FadeIn(count), Transform(self.note, cap2), run_time=0.85)
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
        eq = MathTex(r"\varphi(n)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\varphi(n)=n\prod_{p\mid n}\bigl(1-\tfrac{1}{p}\bigr)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\varphi(n)=n\prod_{p\mid n}\bigl(1-\tfrac{1}{p}\bigr)").scale(0.82)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=2.0)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
