from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class SpiralSimilarity(PacedScene):
    """#266 螺旋相似は回転と拡大（約45秒）"""

    def construct(self):
        self.O = LEFT * 2.4 + DOWN * 0.8
        self.show_heading("螺旋相似")
        self.draw_shape()
        self.spiral_map()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_shape(self):
        self.shape = Polygon(
            self.O,
            self.O + RIGHT * 1.6,
            self.O + RIGHT * 1.2 + UP * 1.0,
            color=BLUE,
            stroke_width=3,
        )
        self.play(Create(self.shape), FadeIn(Dot(self.O, color=YELLOW, radius=0.09)), run_time=1.4)
        note = self.ja_text("図形", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def spiral_map(self):
        # rotate 50° and scale 1.55 about O
        mapped = self.shape.copy().set_color(ORANGE)
        mapped.rotate(0.9, about_point=self.O)
        mapped.scale(1.55, about_point=self.O)
        arc = Arc(radius=0.7, start_angle=0.1, angle=0.9, arc_center=self.O, color=GREY_B, stroke_width=2)
        cap = self.ja_text("回して拡大", font_size=24).move_to(self.note)
        self.play(Create(arc), TransformFromCopy(self.shape, mapped), Transform(self.note, cap), run_time=1.8)
        self.read(0.3)
        # ray from O through a vertex
        tip = mapped.get_vertices()[1]
        ray = DashedLine(self.O, tip, color=YELLOW, stroke_width=2)
        cap2 = self.ja_text("同じ中心", font_size=24).move_to(self.note)
        self.play(Create(ray), Transform(self.note, cap2), run_time=1.1)
        self.read(0.4)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"\cdots").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\Rightarrow").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = self.ja_text("回転と相似の合成", font_size=28)
        formula.move_to(self.proof_eq)
        self.play(FadeIn(formula), run_time=1.2)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
