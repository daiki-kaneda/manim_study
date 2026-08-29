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
        self.derive()
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
        edge_list = [(1, 3), (2, 3), (3, 4), (3, 5)]
        self.edge_mobs = {
            frozenset(e): Line(positions[e[0]], positions[e[1]], color=GREY_B, stroke_width=3)
            for e in edge_list
        }
        self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in self.dots.values()], lag_ratio=0.1), run_time=1.3)
        self.play(
            FadeIn(VGroup(*self.labs.values())),
            LaggedStart(*[Create(l) for l in self.edge_mobs.values()], lag_ratio=0.08),
            run_time=1.2,
        )
        note = self.ja_text("木", font_size=24)
        note.to_edge(RIGHT, buff=0.6).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def encode(self):
        # remove 1→3, 2→3, 4→3 → code (3,3,3); leave 3—5
        code_slots = VGroup(*[MathTex(r"\_", font_size=36) for _ in range(3)])
        code_slots.arrange(RIGHT, buff=0.35).to_edge(DOWN, buff=1.15)
        self.play(FadeIn(code_slots), run_time=0.5)
        sequence = [(1, 3, 0), (2, 3, 1), (4, 3, 2)]
        for leaf, parent, idx in sequence:
            edge = self.edge_mobs[frozenset((leaf, parent))]
            self.play(self.dots[leaf].animate.set_color(RED), run_time=0.45)
            cap = self.ja_text("葉を落とす", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.35)
            num = MathTex(str(parent), color=ORANGE, font_size=36).move_to(code_slots[idx])
            self.play(
                FadeOut(self.dots[leaf]),
                FadeOut(self.labs[leaf]),
                FadeOut(edge),
                FadeIn(num),
                run_time=0.7,
            )
            code_slots[idx] = num
            self.read(0.15)
        cap2 = self.ja_text("長さ n-2", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.6)
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
        eq = MathTex(r"n^{n-2}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"n^{n-2}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"n^{n-2}").scale(1.3)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.6)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
