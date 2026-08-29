from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class ChanceMap(JapaneseScene):
    """#99 偶然の地図（約90秒）"""

    def construct(self):
        self.show_heading("偶然の地図")
        self.show_cards()
        self.hold(1.4)

    def show_cards(self):
        items = [
            ("期待値", r"E[X]"),
            ("分散", r"V(X)"),
            ("ベイズ", r"P(A\mid B)"),
            ("中心極限", r"S_n"),
            ("回帰", r"\min\sum r_i^2"),
        ]
        cards = VGroup()
        for jp, tex in items:
            title = self.ja_text(jp, font_size=24)
            body = MathTex(tex, font_size=28)
            card = VGroup(title, body).arrange(DOWN, buff=0.16)
            box = SurroundingRectangle(card, color=GREY, buff=0.22, corner_radius=0.08)
            cards.add(VGroup(box, card))
        cards.arrange_in_grid(rows=2, cols=3, buff=0.32)
        cards.scale(0.95).shift(DOWN * 0.15)
        for card in cards:
            self.play(FadeIn(card, shift=UP * 0.1), run_time=0.4)
            self.hold(0.25)
        foot = self.ja_text("ばらつきを読む言葉", font_size=26)
        foot.to_edge(DOWN, buff=0.32)
        self.play(FadeIn(foot), run_time=0.5)
        self.hold(1.0)
