from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class MobiusInversion(PacedScene):
    """#353 メビウス反転：束上で和を戻す（約45秒）"""

    def construct(self):
        self.show_heading("メビウス反転")
        self.draw_poset()
        self.invert()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_poset(self):
        # small diamond poset
        top = Dot(UP * 1.4, color=BLUE, radius=0.12)
        mid_l = Dot(LEFT * 1.4 + UP * 0.2, color=BLUE, radius=0.12)
        mid_r = Dot(RIGHT * 1.4 + UP * 0.2, color=BLUE, radius=0.12)
        bot = Dot(DOWN * 1.0, color=BLUE, radius=0.12)
        edges = VGroup(
            Line(bot.get_center(), mid_l.get_center(), color=GREY, stroke_width=3),
            Line(bot.get_center(), mid_r.get_center(), color=GREY, stroke_width=3),
            Line(mid_l.get_center(), top.get_center(), color=GREY, stroke_width=3),
            Line(mid_r.get_center(), top.get_center(), color=GREY, stroke_width=3),
        )
        self.play(Create(edges), FadeIn(VGroup(top, mid_l, mid_r, bot)), run_time=1.5)
        note = self.ja_text("半順序", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.nodes = VGroup(bot, mid_l, mid_r, top)

    def invert(self):
        g = MathTex(r"g", color=ORANGE, font_size=36).next_to(self.nodes[3], RIGHT, buff=0.3)
        f = MathTex(r"f", color=YELLOW, font_size=36).next_to(self.nodes[0], LEFT, buff=0.3)
        cap = self.ja_text("下からの和", font_size=24).move_to(self.note)
        self.play(FadeIn(g), Transform(self.note, cap), run_time=1.1)
        self.read(0.25)
        arrow = Arrow(g.get_bottom(), f.get_top(), buff=0.15, color=YELLOW, stroke_width=4)
        cap2 = self.ja_text("μ で戻す", font_size=24).move_to(self.note)
        self.play(GrowArrow(arrow), FadeIn(f), Transform(self.note, cap2), run_time=1.3)
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
        eq = MathTex(r"g(x)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"g(x)=\sum_{y\le x}f(y)\ \Rightarrow\ f=\mu*g").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"g(x)=\sum_{y\le x}f(y)\ \Rightarrow\ f=\mu*g").scale(0.8)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=2.0)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
