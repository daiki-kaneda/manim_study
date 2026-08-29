from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class TreeGraph(JapaneseScene):
    """#83 木：閉路がなく連結（約90秒）"""

    def construct(self):
        self.show_heading("木")
        self.grow()
        self.show_formula()
        self.hold(1.2)

    def grow(self):
        c = DOWN * 0.05
        pts = [
            c + ORIGIN,
            c + LEFT * 2.1 + UP * 1.35,
            c + RIGHT * 2.2 + UP * 1.2,
            c + LEFT * 2.3 + DOWN * 1.4,
            c + RIGHT * 0.4 + DOWN * 1.55,
            c + RIGHT * 2.5 + DOWN * 0.35,
        ]
        parent = [None, 0, 0, 0, 1, 2]
        dots = []
        edges = VGroup()
        counter = self.ja_text("頂点 0　辺 0", font_size=24)
        counter.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(counter), run_time=0.25)
        for i, p in enumerate(pts):
            d = Dot(p, radius=0.1, color=BLUE)
            dots.append(d)
            anims = [FadeIn(d)]
            if parent[i] is not None:
                e = Line(pts[parent[i]], p, color=WHITE, stroke_width=3)
                edges.add(e)
                anims.append(Create(e))
            v, e_n = i + 1, i
            nxt = self.ja_text(f"頂点 {v}　辺 {e_n}", font_size=24).move_to(counter)
            anims.append(Transform(counter, nxt))
            self.play(*anims, run_time=0.5)
            self.hold(0.18)
        note = self.ja_text("閉路なし", font_size=24)
        note.next_to(counter, DOWN, buff=0.3)
        self.play(FadeIn(note), run_time=0.35)
        self.hold(0.65)
        self.counter = counter

    def show_formula(self):
        formula = MathTex(r"|V|=|E|+1").scale(1.2)
        formula.to_edge(DOWN, buff=0.38)
        self.play(Write(formula), run_time=0.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
