from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class ChineseRemainder(JapaneseScene):
    """#44 中国剰余定理（約90秒）"""

    def construct(self):
        self.show_heading("中国剰余定理")
        self.show_system()
        self.scan_numbers()
        self.show_formula()
        self.hold(1.2)

    def show_system(self):
        sys_tex = VGroup(
            MathTex(r"n\equiv 2\pmod{3}", font_size=36),
            MathTex(r"n\equiv 3\pmod{5}", font_size=36),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        sys_tex.shift(UP * 1.85)
        self.play(Write(sys_tex[0]), run_time=0.55)
        self.play(Write(sys_tex[1]), run_time=0.55)
        self.hold(0.5)
        self.sys_tex = sys_tex

    def scan_numbers(self):
        # 0..14 を並べ、mod3=2 を青、mod5=3 を緑、両方を黄
        items = VGroup()
        origin = LEFT * 3.4 + UP * 0.55
        for k in range(15):
            row, col = divmod(k, 8)
            col_color = WHITE
            if k % 3 == 2 and k % 5 == 3:
                col_color = YELLOW
            elif k % 3 == 2:
                col_color = BLUE
            elif k % 5 == 3:
                col_color = GREEN
            t = MathTex(str(k), color=col_color, font_size=32)
            t.move_to(origin + DOWN * row * 0.85 + RIGHT * col * 0.9)
            items.add(t)
        self.play(LaggedStart(*[FadeIn(t) for t in items], lag_ratio=0.08), run_time=1.6)
        note = VGroup(
            self.ja_text("青: 3 で余り 2", font_size=22),
            self.ja_text("緑: 5 で余り 3", font_size=22),
            self.ja_text("黄: 両方", font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        note.to_edge(RIGHT, buff=0.4).shift(DOWN * 0.35)
        self.play(FadeIn(note), run_time=0.45)
        eight = items[8]
        self.play(Indicate(eight, color=YELLOW), run_time=0.7)
        self.hold(0.6)
        self.eight = eight

    def show_formula(self):
        formula = MathTex(r"n\equiv 8\pmod{15}").scale(1.15)
        formula.to_edge(DOWN, buff=0.38)
        self.play(Write(formula), run_time=0.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
