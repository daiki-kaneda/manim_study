from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class TangentChordRatio(PacedScene):
    """#529 接弦の長さ比：方べきと接線の関係（約45秒）"""

    def construct(self):
        self.show_heading("接弦の長さ比")
        self.draw_circle()
        self.tangent()
        self.show_formula()
        self.read(1.4)

    def draw_circle(self):
        circ = Circle(radius=1.6, color=BLUE, stroke_width=3).shift(LEFT * 0.8 + UP * 0.1)
        self.play(Create(circ), run_time=1.1)
        note = self.ja_text("円と弦", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.circ = circ

    def tangent(self):
        P = LEFT * 0.8 + UP * 0.1 + RIGHT * 2.6 + DOWN * 0.2
        T = LEFT * 0.8 + UP * 0.1 + RIGHT * 1.1 + UP * 1.15
        chord_a = LEFT * 0.8 + UP * 0.1 + LEFT * 0.3 + UP * 1.4
        chord_b = LEFT * 0.8 + UP * 0.1 + RIGHT * 1.2 + DOWN * 1.0
        tan = Line(P, T, color=ORANGE, stroke_width=3)
        sec = Line(P, chord_b, color=TEAL, stroke_width=3)
        dots = VGroup(Dot(P, color=YELLOW), Dot(T, color=YELLOW), Dot(chord_a, color=GREY), Dot(chord_b, color=GREY))
        cap = self.ja_text("接線と割線", font_size=24).move_to(self.note)
        self.play(Create(tan), Create(sec), FadeIn(dots), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("長さの二乗", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"PT^2=PA\cdot PB").scale(0.95)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
