from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class ClosingMap(JapaneseScene):
    """#100 100本の地図（約90秒）"""

    def construct(self):
        self.show_heading("100本の地図")
        self.show_grid()
        self.hold(1.4)

    def show_grid(self):
        names = [
            "図形", "代数", "微積", "恒等式", "古典",
            "線形", "確率", "整数", "組合せ", "三角",
            "級数", "論理", "方程", "複素", "最適化",
            "グラフ", "統計", "総合", "地図", "100",
        ]
        tiles = VGroup()
        for name in names:
            t = self.ja_text(name, font_size=22)
            box = SurroundingRectangle(t, color=GREY, buff=0.16, corner_radius=0.08)
            tiles.add(VGroup(box, t))
        tiles.arrange_in_grid(rows=4, cols=5, buff=0.22)
        tiles.scale(0.95).shift(DOWN * 0.12)
        last = tiles[-1]
        last[0].set_color(YELLOW)
        last[1].set_color(YELLOW)
        for tile in tiles:
            self.play(FadeIn(tile, shift=UP * 0.08), run_time=0.18)
        foot = self.ja_text("まずはこの100本", font_size=26)
        foot.to_edge(DOWN, buff=0.28)
        self.play(FadeIn(foot), run_time=0.5)
        self.play(Indicate(last, color=YELLOW), run_time=0.7)
        self.hold(1.0)
