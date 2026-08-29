from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class TriangleRigidity(PacedScene):
    """#530 三角形の剛性：3辺が形を一意に決める（約45秒）"""

    def construct(self):
        self.show_heading("三角形の剛性")
        self.draw_sss()
        self.lock()
        self.show_formula()
        self.read(1.4)

    def draw_sss(self):
        A, B, C = UP * 2.0, LEFT * 2.5 + DOWN * 1.3, RIGHT * 2.5 + DOWN * 1.3
        tri = Polygon(A, B, C, color=BLUE, stroke_width=3)
        labels = VGroup(
            MathTex("a", font_size=28).move_to((B + C) / 2 + DOWN * 0.35),
            MathTex("b", font_size=28).move_to((A + C) / 2 + RIGHT * 0.35),
            MathTex("c", font_size=28).move_to((A + B) / 2 + LEFT * 0.35),
        )
        self.play(Create(tri), FadeIn(labels), run_time=1.3)
        note = self.ja_text("三辺固定", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def lock(self):
        lock = RegularPolygon(6, color=ORANGE, stroke_width=3).scale(0.45).shift(RIGHT * 2.8 + DOWN * 0.6)
        cap = self.ja_text("合同まで決まる", font_size=24).move_to(self.note)
        self.play(Create(lock), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("枠組み剛性の原型", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = self.ja_text("SSS：三辺が合同を決める", font_size=26)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
