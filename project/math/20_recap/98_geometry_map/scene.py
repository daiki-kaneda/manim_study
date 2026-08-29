from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class GeometryMap(JapaneseScene):
    """#98 図形の地図（約90秒）"""

    def construct(self):
        self.show_heading("図形の地図")
        self.show_cards()
        self.hold(1.4)

    def show_cards(self):
        items = [
            ("ピタゴラス", r"a^2+b^2=c^2"),
            ("円", r"\theta=2\phi"),
            ("三角", r"\frac{a}{\sin A}"),
            ("不等式", r"\frac{a+b}{2}\ge\sqrt{ab}"),
            ("写像", r"z\mapsto 1/z"),
        ]
        cards = VGroup()
        for jp, tex in items:
            title = self.ja_text(jp, font_size=24)
            body = MathTex(tex, font_size=28)
            card = VGroup(title, body).arrange(DOWN, buff=0.16)
            box = SurroundingRectangle(card, color=GREY, buff=0.22, corner_radius=0.08)
            cards.add(VGroup(box, card))
        cards.arrange_in_grid(rows=2, cols=3, buff=0.3)
        cards.scale(0.9).shift(DOWN * 0.15)
        for card in cards:
            self.play(FadeIn(card, shift=UP * 0.1), run_time=0.4)
            self.hold(0.25)
        foot = self.ja_text("形を見る言葉", font_size=26)
        foot.to_edge(DOWN, buff=0.32)
        self.play(FadeIn(foot), run_time=0.5)
        self.hold(1.0)
