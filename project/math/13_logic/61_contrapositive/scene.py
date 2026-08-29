from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class Contrapositive(JapaneseScene):
    """#61 対偶（約90秒）"""

    def construct(self):
        self.show_heading("対偶")
        self.show_implication()
        self.flip()
        self.show_formula()
        self.hold(1.2)

    def show_implication(self):
        p = self.ja_text("雨が降る", font_size=30)
        q = self.ja_text("地面が濡れる", font_size=30)
        arrow = MathTex(r"\Rightarrow", font_size=44)
        row = VGroup(p, arrow, q).arrange(RIGHT, buff=0.35)
        row.shift(UP * 1.15)
        self.play(FadeIn(row), run_time=0.8)
        note = self.ja_text("P なら Q", font_size=26)
        note.next_to(row, DOWN, buff=0.4)
        self.play(FadeIn(note), run_time=0.4)
        self.hold(0.7)
        self.row, self.note = row, note

    def flip(self):
        np_ = self.ja_text("地面が濡れていない", font_size=28)
        nq = self.ja_text("雨は降っていない", font_size=28)
        arrow = MathTex(r"\Rightarrow", font_size=44)
        row2 = VGroup(np_, arrow, nq).arrange(RIGHT, buff=0.3)
        row2.next_to(self.note, DOWN, buff=0.7)
        self.play(FadeIn(row2), run_time=0.8)
        cap = self.ja_text("対偶も同じ意味", font_size=26)
        cap.next_to(row2, DOWN, buff=0.35)
        self.play(FadeIn(cap), run_time=0.4)
        self.hold(0.8)

    def show_formula(self):
        formula = MathTex(r"(P\Rightarrow Q)\;\Longleftrightarrow\;(\neg Q\Rightarrow\neg P)").scale(0.85)
        formula.to_edge(DOWN, buff=0.38)
        self.play(Write(formula), run_time=1.1)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
