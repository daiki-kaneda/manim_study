from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class InfinitePrimes(JapaneseScene):
    """#26 素数は無限にある（ユークリッド、約90秒）"""

    beat = 2.6

    def construct(self):
        self.title = self.show_heading("素数は無限")
        self.state_claim()
        self.show_proof()
        self.conclude()
        self.hold(1.2)

    def state_claim(self):
        claim = self.ja_text("素数が有限個だと仮定する", font_size=30)
        claim.next_to(self.title, DOWN, buff=0.4)
        self.play(FadeIn(claim), run_time=0.6)
        self.hold(0.6)
        self.claim = claim

    def _line(self, *mobs):
        return VGroup(*mobs).arrange(RIGHT, buff=0.16, aligned_edge=DOWN)

    def show_proof(self):
        primes = MathTex(r"p_1,p_2,\ldots,p_k", font_size=36)
        primes.next_to(self.claim, DOWN, buff=0.5)
        self.play(Write(primes), run_time=0.7)
        self.hold(0.5)

        n_def = self._line(
            MathTex(r"N=", font_size=36),
            MathTex(r"p_1 p_2 \cdots p_k+1", font_size=36),
        )
        n_def.next_to(primes, DOWN, buff=0.4)
        self.play(FadeIn(n_def), run_time=0.6)
        self.hold(0.7)

        example = self._line(
            self.ja_text("例:", font_size=26),
            MathTex(r"2\cdot 3\cdot 5+1=31", font_size=32),
        )
        example.next_to(n_def, DOWN, buff=0.35)
        self.play(FadeIn(example), run_time=0.5)
        self.hold(0.8)

        not_div = self.ja_text("どの素数でも割り切れない", font_size=28)
        not_div.next_to(example, DOWN, buff=0.4)
        self.play(FadeIn(not_div), run_time=0.5)
        self.hold(0.8)
        self.not_div = not_div

    def conclude(self):
        extra = self.ja_text("N は新しい素数の因子を持つ → 矛盾", font_size=28)
        extra.set_color(YELLOW)
        extra.to_edge(DOWN, buff=0.95)
        self.play(FadeIn(extra), run_time=0.55)
        self.hold(0.8)
        result = self.ja_text("素数は無限個ある", font_size=36)
        result.next_to(extra, UP, buff=0.28)
        self.play(Write(result), run_time=0.8)
        self.play(Indicate(result, color=BLUE), run_time=0.7)
        self.hold(1.2)
