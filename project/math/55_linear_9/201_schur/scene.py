from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class SchurForm(PacedScene):
    """#201 シューアはユニタリで上三角へ（約45秒）"""

    def construct(self):
        self.show_heading("シューア分解")
        self.draw_matrix()
        self.triangulate()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_matrix(self):
        entries = [[r"a", r"b", r"c"], [r"d", r"e", r"f"], [r"g", r"h", r"i"]]
        self.mat = Matrix(entries, h_buff=0.95, v_buff=0.75).scale(0.9)
        self.mat.shift(UP * 0.2 + LEFT * 0.5)
        self.play(FadeIn(self.mat), run_time=1.3)
        note = self.ja_text("一般の行列", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.35)
        self.note = note

    def triangulate(self):
        tri_entries = [[r"\lambda_1", r"*", r"*"], ["0", r"\lambda_2", r"*"], ["0", "0", r"\lambda_3"]]
        tri = Matrix(tri_entries, h_buff=0.95, v_buff=0.75).scale(0.9)
        tri.move_to(self.mat)
        # highlight lower triangle zeros
        zeros = VGroup(tri.get_entries()[3], tri.get_entries()[6], tri.get_entries()[7])
        cap = self.ja_text("上三角へ", font_size=24).move_to(self.note)
        self.play(Transform(self.mat, tri), Transform(self.note, cap), run_time=1.7)
        self.read(0.3)
        boxes = VGroup(*[SurroundingRectangle(z, color=TEAL, buff=0.12, corner_radius=0.05) for z in zeros])
        # After transform, entries may be the transformed ones - use self.mat
        # Safer: surround lower part conceptually with a triangle brace
        cap2 = self.ja_text("下は 0", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[Create(b) for b in boxes], lag_ratio=0.15), Transform(self.note, cap2), run_time=1.4)
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
        eq = MathTex(r"A").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"A=QUQ^{*}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"A=QUQ^{*}").scale(1.15)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.6)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
