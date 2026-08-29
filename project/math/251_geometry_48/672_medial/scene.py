from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class MedialTriangle(PacedScene):
    """#672 中点三角形：各辺の中点を結ぶ（約45秒）"""

    def construct(self):
        self.show_heading("中点三角形")
        self.draw()
        self.relate()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        tri = Polygon(LEFT * 2.7 + DOWN * 1.1, RIGHT * 2.7 + DOWN * 1.1, UP * 1.8, color=BLUE, stroke_width=3)
        mid = Polygon(ORIGIN + DOWN * 1.1, RIGHT * 1.35 + UP * 0.35, LEFT * 1.35 + UP * 0.35, color=ORANGE, stroke_width=3)
        self.play(Create(tri), Create(mid), run_time=1.3)
        note = self.ja_text("中点三角形系", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def relate(self):
        cap = self.ja_text("辺の中点を結ぶ", font_size=22).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("相似の連鎖", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"[m]=\tfrac14[\triangle]").scale(0.85)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
