from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class JordanForm(PacedScene):
    """#189 ジョルダンは対角に λ、超対角に 1（約45秒）"""

    def construct(self):
        self.show_heading("ジョルダン標準形")
        self.draw_blocks()
        self.fill_ones()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_blocks(self):
        # 3x3 Jordan block visual as matrix entries
        entries = [
            [r"\lambda", "", ""],
            ["", r"\lambda", ""],
            ["", "", r"\mu"],
        ]
        self.mat = Matrix(entries, h_buff=1.15, v_buff=0.85).scale(0.95)
        self.mat.shift(UP * 0.15 + LEFT * 0.4)
        # highlight two blocks
        box1 = SurroundingRectangle(
            VGroup(self.mat.get_entries()[0], self.mat.get_entries()[1], self.mat.get_entries()[3], self.mat.get_entries()[4]),
            color=BLUE,
            buff=0.18,
            corner_radius=0.08,
        )
        box2 = SurroundingRectangle(self.mat.get_entries()[8], color=TEAL, buff=0.22, corner_radius=0.08)
        self.play(FadeIn(self.mat), run_time=1.4)
        note = self.ja_text("ブロック", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(Create(box1), Create(box2), FadeIn(note), run_time=1.5)
        self.read(0.35)
        self.note = note
        self.box1 = box1

    def fill_ones(self):
        # put 1 above diagonal in first block
        one = MathTex("1", color=ORANGE).scale(0.95)
        # position between (0,1) entry slot - use get_entries index 1 which is empty-ish
        target = self.mat.get_entries()[1].get_center()
        one.move_to(target)
        cap = self.ja_text("超対角に 1", font_size=24).move_to(self.note)
        self.play(FadeIn(one, scale=0.6), Transform(self.note, cap), run_time=1.4)
        self.read(0.35)
        cap2 = self.ja_text("連鎖", font_size=24).move_to(self.note)
        arrow = Arrow(
            self.mat.get_entries()[0].get_center() + DOWN * 0.35,
            self.mat.get_entries()[4].get_center() + UP * 0.35,
            buff=0.05,
            color=ORANGE,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.18,
        )
        self.play(GrowArrow(arrow), Transform(self.note, cap2), run_time=1.3)
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
        eq = MathTex(r"J").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"J=\mathrm{diag}(J_{\lambda_1},\ldots)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"J=\mathrm{diag}(J_{\lambda_1},\ldots)").scale(0.85)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
