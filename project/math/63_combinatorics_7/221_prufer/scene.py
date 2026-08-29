from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class PruferCode(PacedScene):
    """#221 プリューファーは木を数列にする（約45秒）"""

    def construct(self):
        self.show_heading("プリューファーコード")
        self.draw_tree()
        self.encode()
        self.show_formula()
        self.read(1.4)

    def draw_tree(self):
        # star-ish tree on 5 vertices: 1-3-2, 3-4, 3-5
        positions = {
            1: LEFT * 2.8 + UP * 1.2,
            2: RIGHT * 2.8 + UP * 1.2,
            3: ORIGIN + UP * 0.2,
            4: LEFT * 1.6 + DOWN * 1.5,
            5: RIGHT * 1.6 + DOWN * 1.5,
        }
        self.dots = {i: Dot(p, radius=0.14, color=WHITE) for i, p in positions.items()}
        self.labs = {i: MathTex(str(i), font_size=26).next_to(self.dots[i], UP, buff=0.08) for i in positions}
        edges = [(1, 3), (2, 3), (3, 4), (3, 5)]
        self.lines = VGroup(*[Line(positions[a], positions[b], color=GREY_B, stroke_width=3) for a, b in edges])
        self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in self.dots.values()], lag_ratio=0.1), run_time=1.3)
        self.play(FadeIn(VGroup(*self.labs.values())), Create(self.lines), run_time=1.2)
        note = self.ja_text("木", font_size=24)
        note.to_edge(RIGHT, buff=0.6).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def encode(self):
        # Prüfer for this tree: repeatedly remove smallest leaf
        # leaves initially {1,2,4,5}; remove 1 record 3; remove 2 record 3; remove 4 record 3 → code (3,3,3)
        code_slots = VGroup(*[MathTex(r"\_", font_size=36) for _ in range(3)])
        code_slots.arrange(RIGHT, buff=0.35).to_edge(DOWN, buff=1.15)
        self.play(FadeIn(code_slots), run_time=0.5)
        sequence = [(1, 3, 0), (2, 3, 1), (4, 3, 2)]
        for leaf, parent, idx in sequence:
            self.play(self.dots[leaf].animate.set_color(RED), run_time=0.45)
            cap = self.ja_text("葉を落とす", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.35)
            num = MathTex(str(parent), color=ORANGE, font_size=36).move_to(code_slots[idx])
            self.play(
                FadeOut(self.dots[leaf]),
                FadeOut(self.labs[leaf]),
                FadeIn(num),
                run_time=0.7,
            )
            code_slots[idx] = num
            self.read(0.15)
        cap2 = self.ja_text("長さ n-2", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.6)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"n^{n-2}").scale(1.3)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.6)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
