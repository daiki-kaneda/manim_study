from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class AlgebraMap(JapaneseScene):
    """#97 代数の地図（約90秒）"""

    def construct(self):
        self.show_heading("代数の地図")
        self.show_cards()
        self.hold(1.4)

    def show_cards(self):
        items = [
            ("無理数", r"\sqrt{2}\notin\mathbb{Q}"),
            ("展開", r"(a+b)^2"),
            ("整数", r"a\equiv b"),
            ("組合せ", r"\binom{n}{k}"),
            ("論理", r"P\Rightarrow Q"),
        ]
        cards = VGroup()
        for jp, tex in items:
            title = self.ja_text(jp, font_size=24)
            body = MathTex(tex, font_size=28)
            card = VGroup(title, body).arrange(DOWN, buff=0.16)
            box = SurroundingRectangle(card, color=GREY, buff=0.22, corner_radius=0.08)
            cards.add(VGroup(box, card))
        cards.arrange_in_grid(rows=2, cols=3, buff=0.32)
        cards.scale(0.92).shift(DOWN * 0.15)
        for card in cards:
            self.play(FadeIn(card, shift=UP * 0.1), run_time=0.4)
            self.hold(0.25)
        foot = self.ja_text("構造を書く言葉", font_size=26)
        foot.to_edge(DOWN, buff=0.32)
        self.play(FadeIn(foot), run_time=0.5)
        self.hold(1.0)
