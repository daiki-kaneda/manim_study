from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class HookLength(PacedScene):
    """#209 フック長で標準盤の数（約45秒）"""

    def construct(self):
        self.show_heading("フック長公式")
        self.draw_shape()
        self.fill_hooks()
        self.show_formula()
        self.read(1.4)

    def _cell(self, i, j, origin, color=BLUE):
        sq = Square(side_length=0.72, color=color, fill_opacity=0.35, stroke_width=2)
        sq.move_to(origin + RIGHT * j * 0.78 + DOWN * i * 0.78)
        return sq

    def draw_shape(self):
        # shape (3,2,1)
        self.origin = LEFT * 3.0 + UP * 1.4
        self.rows = [3, 2, 1]
        self.cells = {}
        group = VGroup()
        for i, n in enumerate(self.rows):
            for j in range(n):
                sq = self._cell(i, j, self.origin)
                self.cells[(i, j)] = sq
                group.add(sq)
        self.play(LaggedStart(*[FadeIn(sq, scale=0.5) for sq in group], lag_ratio=0.08), run_time=1.7)
        note = self.ja_text("ヤング図", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def _hook(self, i, j):
        # arm + leg + 1
        arm = self.rows[i] - j - 1
        leg = sum(1 for r in self.rows[i + 1 :] if r > j)
        return arm + leg + 1

    def fill_hooks(self):
        hooks = {
            (0, 0): 5,
            (0, 1): 3,
            (0, 2): 1,
            (1, 0): 3,
            (1, 1): 1,
            (2, 0): 1,
        }
        labels = VGroup()
        for key, h in hooks.items():
            lab = MathTex(str(h), font_size=28).move_to(self.cells[key])
            labels.add(lab)
        # highlight one hook: (0,0) — right and down
        path = VGroup(
            self.cells[(0, 0)].copy().set_fill(ORANGE, opacity=0.55),
            self.cells[(0, 1)].copy().set_fill(ORANGE, opacity=0.35),
            self.cells[(0, 2)].copy().set_fill(ORANGE, opacity=0.35),
            self.cells[(1, 0)].copy().set_fill(ORANGE, opacity=0.35),
            self.cells[(2, 0)].copy().set_fill(ORANGE, opacity=0.35),
        )
        cap = self.ja_text("フック", font_size=24).move_to(self.note)
        self.play(FadeIn(path), Transform(self.note, cap), run_time=1.3)
        self.read(0.3)
        self.play(FadeOut(path), LaggedStart(*[FadeIn(l) for l in labels], lag_ratio=0.08), run_time=1.5)
        cap2 = self.ja_text("各マスに数", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.6)
        self.read(0.35)

    def show_formula(self):
        # f^{(3,2,1)} = 6! / (5·3·1·3·1·1) = 720/45 = 16
        formula = MathTex(r"f^{\lambda}=\frac{n!}{\prod h(u)}").scale(0.95)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
