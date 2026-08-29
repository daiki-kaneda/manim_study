from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class IntegrationByParts(JapaneseScene):
    """#19 部分積分（約90秒）"""

    def construct(self):
        self.show_heading("部分積分")
        self.show_product_rule()
        self.reverse()
        self.hold(1.2)

    def show_product_rule(self):
        prod = MathTex(r"(uv)'=u'v+uv'").scale(1.3)
        prod.shift(UP * 1.6)
        cap = self.ja_text("積の微分", font_size=26).next_to(prod, DOWN, buff=0.3)
        self.play(Write(prod), run_time=0.9)
        self.play(FadeIn(cap), run_time=0.4)
        self.hold(0.8)
        self.prod, self.cap = prod, cap

    def reverse(self):
        integ = MathTex(r"uv=\int u'v\,dx+\int uv'\,dx").scale(1.05)
        integ.next_to(self.cap, DOWN, buff=0.55)
        self.play(Write(integ), run_time=1.0)
        note = self.ja_text("両辺を積分して移項", font_size=24)
        note.next_to(integ, DOWN, buff=0.3)
        self.play(FadeIn(note), run_time=0.4)
        self.hold(0.8)
        self.play(FadeOut(note), run_time=0.3)

        result = MathTex(r"\int u\,dv=uv-\int v\,du").scale(1.25)
        result.to_edge(DOWN, buff=0.5)
        self.play(Write(result), run_time=1.1)
        self.play(Indicate(result, color=BLUE), run_time=0.8)
        self.hold(1.3)
