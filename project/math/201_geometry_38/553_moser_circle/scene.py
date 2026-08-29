from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class MoserCircle(PacedScene):
    """#553 モザーの円：単位距離グラフの色分け（約45秒）"""

    def construct(self):
        self.show_heading("モザーの円")
        self.draw_spindle()
        self.chromatic()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_spindle(self):
        # Moser spindle: two rhombi
        pts_a = [ORIGIN, RIGHT * 1.2, RIGHT * 0.6 + UP * 1.04, LEFT * 0.6 + UP * 1.04]
        shift = RIGHT * 1.8 + UP * 0.5
        edges = VGroup()
        for base in [ORIGIN, shift]:
            verts = [base + p for p in [ORIGIN, RIGHT * 1.3, RIGHT * 0.65 + UP * 1.15, LEFT * 0.65 + UP * 1.15]]
            for i, j in [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]:
                edges.add(Line(verts[i], verts[j], color=BLUE, stroke_width=3))
            edges.add(*[Dot(v, color=YELLOW, radius=0.08) for v in verts])
        self.play(LaggedStart(*[Create(e) if isinstance(e, Line) else FadeIn(e) for e in edges], lag_ratio=0.03), run_time=1.5)
        note = self.ja_text("単位距離グラフ", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def chromatic(self):
        cap = self.ja_text("彩色数が4以上", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("平面色分け問題", font_size=24).move_to(self.note)
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
        formula = self.ja_text("モザースピンドル：χ≥4 の証拠", font_size=26)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
