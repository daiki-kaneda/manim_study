from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class BanachFixedPoint(PacedScene):
    """#294 バナッハの不動点：縮小写像は一点へ（約45秒）"""

    def construct(self):
        self.show_heading("バナッハの不動点定理")
        self.draw_map()
        self.iterate()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_map(self):
        self.axes = Axes(
            x_range=[0, 4.2, 1],
            y_range=[0, 4.2, 1],
            x_length=5.2,
            y_length=5.2,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).scale(0.72).shift(LEFT * 0.8 + UP * 0.1)
        diag = self.axes.plot(lambda x: x, x_range=[0.2, 3.8], color=GREY, stroke_width=2)
        f = self.axes.plot(lambda x: 0.55 * x + 0.9, x_range=[0.2, 3.8], color=BLUE, stroke_width=4)
        self.play(Create(self.axes), Create(diag), run_time=1.0)
        self.play(Create(f), run_time=1.1)
        note = self.ja_text("縮小写像", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.f = f

    def iterate(self):
        # cobweb: x0 -> f -> diag -> f
        x = 0.6
        pts = []
        for _ in range(4):
            y = 0.55 * x + 0.9
            pts.append((x, y))
            x = y
        segs = VGroup()
        cur = 0.6
        for x, y in pts:
            p0 = self.axes.c2p(cur, 0.05) if False else self.axes.c2p(cur, cur if segs else 0.2)
            # vertical then horizontal cobweb
            a = self.axes.c2p(cur, cur if len(segs) else 0.15)
            b = self.axes.c2p(cur, y)
            c = self.axes.c2p(y, y)
            if not segs:
                a = self.axes.c2p(cur, 0.2)
            segs.add(Line(a, b, color=ORANGE, stroke_width=3))
            segs.add(Line(b, c, color=ORANGE, stroke_width=3))
            cur = y
        cap = self.ja_text("反復すると", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[Create(s) for s in segs], lag_ratio=0.08), Transform(self.note, cap), run_time=1.7)
        self.read(0.25)
        # fixed point of 0.55x+0.9 is x=2
        fix = Dot(self.axes.c2p(2.0, 2.0), color=YELLOW, radius=0.1)
        cap2 = self.ja_text("唯一の不動点", font_size=24).move_to(self.note)
        self.play(FadeIn(fix, scale=0.5), Transform(self.note, cap2), run_time=1.1)
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
        eq = MathTex(r"d(Tx,Ty)\le k\,d(x,y),\ k<1").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"d(Tx,Ty)\le k\,d(x,y),\ k<1").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"d(Tx,Ty)\le k\,d(x,y),\ k<1").scale(0.82)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
