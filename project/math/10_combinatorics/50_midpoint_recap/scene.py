from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class MidpointRecap(JapaneseScene):
    """#50 前半の地図（約90秒）"""

    def construct(self):
        self.show_heading("ここまでの地図")
        self.show_cards()
        self.hold(1.4)

    def show_cards(self):
        items = [
            ("図形", r"a^2+b^2=c^2"),
            ("複素", r"e^{i\theta}=\cos\theta+i\sin\theta"),
            ("線形", r"Av=\lambda v"),
            ("確率", r"P(A\mid B)"),
            ("整数", r"a^{p-1}\equiv 1\pmod{p}"),
        ]
        cards = VGroup()
        for jp, tex in items:
            title = self.ja_text(jp, font_size=24)
            body = MathTex(tex, font_size=28)
            card = VGroup(title, body).arrange(DOWN, buff=0.18)
            box = SurroundingRectangle(card, color=GREY, buff=0.22, corner_radius=0.08)
            cards.add(VGroup(box, card))
        cards.arrange_in_grid(rows=3, cols=2, buff=0.28)
        cards.scale(0.95).shift(DOWN * 0.2)
        for card in cards:
            self.play(FadeIn(card, shift=UP * 0.1), run_time=0.4)
            self.hold(0.28)
        foot = self.ja_text("後半 #51 からは三角・級数・論理へ", font_size=24)
        foot.to_edge(DOWN, buff=0.32)
        self.play(FadeIn(foot), run_time=0.5)
        self.hold(1.0)
