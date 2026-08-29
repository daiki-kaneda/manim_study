from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class AnalysisMap(JapaneseScene):
    """#96 解析の地図（約90秒）"""

    def construct(self):
        self.show_heading("解析の地図")
        self.show_cards()
        self.hold(1.4)

    def show_cards(self):
        items = [
            ("微分", r"f'(x)"),
            ("積分", r"\int f"),
            ("級数", r"\sum a_n"),
            ("微分方程式", r"y'=ky"),
            ("複素", r"e^{i\theta}"),
        ]
        cards = VGroup()
        for jp, tex in items:
            title = self.ja_text(jp, font_size=24)
            body = MathTex(tex, font_size=30)
            card = VGroup(title, body).arrange(DOWN, buff=0.16)
            box = SurroundingRectangle(card, color=GREY, buff=0.22, corner_radius=0.08)
            cards.add(VGroup(box, card))
        cards.arrange_in_grid(rows=2, cols=3, buff=0.32)
        cards.scale(0.95).shift(DOWN * 0.15)
        for card in cards:
            self.play(FadeIn(card, shift=UP * 0.1), run_time=0.4)
            self.hold(0.25)
        foot = self.ja_text("変化を測る言葉", font_size=26)
        foot.to_edge(DOWN, buff=0.32)
        self.play(FadeIn(foot), run_time=0.5)
        self.hold(1.0)
