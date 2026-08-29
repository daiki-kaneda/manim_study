from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class Sqrt2Irrational(JapaneseScene):
    """#11 √2 は無理数（代数テンプレ、約90–120秒）"""

    beat = 2.6

    def construct(self):
        self.title = self.show_heading("√2 は無理数", font_size=40)
        self.state_claim()
        self.show_proof()
        self.conclude()
        self.hold(1.3)

    def state_claim(self):
        claim = MathTex(r"\sqrt{2}\notin\mathbb{Q}").scale(1.3)
        claim.next_to(self.title, DOWN, buff=0.35)
        self.play(Write(claim), run_time=0.9)
        self.hold(0.7)
        self.claim = claim

    def _step(self, jp: str, math: str | None = None, font_size: int = 28):
        parts = [self.ja_text(jp, font_size=font_size)]
        if math is not None:
            parts.append(MathTex(math, font_size=font_size + 4))
        return VGroup(*parts).arrange(RIGHT, buff=0.18, aligned_edge=DOWN)

    def show_proof(self):
        steps = [
            VGroup(
                self.ja_text("仮定:", font_size=28),
                MathTex(r"\sqrt{2}=\dfrac{a}{b}", font_size=32),
                self.ja_text("（互いに素）", font_size=26),
            ).arrange(RIGHT, buff=0.15, aligned_edge=DOWN),
            self._step("二乗:", r"a^2=2b^2"),
            self._step("よって a は偶数。", r"a=2k"),
            self._step("代入:", r"4k^2=2b^2 \Rightarrow b^2=2k^2"),
            self._step("よって b も偶数。", None),
        ]

        lines = VGroup()
        for i, step in enumerate(steps):
            if len(lines) == 0:
                step.next_to(self.claim, DOWN, buff=0.55).to_edge(LEFT, buff=0.9)
            else:
                step.next_to(lines[-1], DOWN, aligned_edge=LEFT, buff=0.32)
            self.play(FadeIn(step, shift=DOWN * 0.15), run_time=0.45)
            self.hold(0.75 if i < 4 else 0.9)
            lines.add(step)
        self.lines = lines

    def conclude(self):
        contra = self.ja_text("a も b も偶数 → 互いに素に矛盾", font_size=30)
        contra.set_color(YELLOW)
        contra.to_edge(DOWN, buff=0.85)
        self.play(FadeIn(contra), run_time=0.6)
        self.hold(1.0)
        result = VGroup(
            MathTex(r"\therefore", font_size=44),
            MathTex(r"\sqrt{2}", font_size=44),
            self.ja_text("は無理数", font_size=34),
        ).arrange(RIGHT, buff=0.18)
        result.next_to(contra, UP, buff=0.3)
        self.play(Write(result), run_time=0.9)
        self.play(Indicate(result, color=BLUE), run_time=0.8)
        self.hold(1.2)
