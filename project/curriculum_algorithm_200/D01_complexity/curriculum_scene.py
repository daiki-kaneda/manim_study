"""Shared helpers for D01 curriculum lessons #4–#7."""

from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import LessonScene


class CurriculumScene(LessonScene):
    header_text = ""

    def wait(self, duration=1.0, **kwargs):
        if duration >= 1.0:
            duration *= 1.9
        elif duration >= 0.7:
            duration *= 1.4
        return super().wait(duration, **kwargs)

    def _open_header(self):
        title = self.ja_text(self.header_text, font_size=40)
        self.play(FadeIn(title), run_time=0.8)
        self.wait(0.7)
        self.play(title.animate.scale(0.55).to_edge(UP, buff=0.16), run_time=0.5)
        return title

    def _clear(self, group):
        if group is None:
            return
        self.play(FadeOut(group), run_time=0.4)

    def _caption(self, *lines, font_size=24):
        parts = VGroup()
        for line in lines:
            if isinstance(line, str):
                parts.add(self.ja_text(line, font_size=font_size))
            else:
                parts.add(line)
        parts.arrange(DOWN, buff=0.08)
        parts.to_edge(DOWN, buff=0.18)
        parts.set_x(0)
        return parts

    def _line(self, *chunks, font_size=24, color=None, buff=0.08):
        """One horizontal line: Japanese strings mixed with MathTex."""
        parts = []
        for chunk in chunks:
            if isinstance(chunk, str):
                kw = {"font_size": font_size}
                if color is not None:
                    kw["color"] = color
                parts.append(self.ja_text(chunk, **kw))
            else:
                parts.append(chunk)
        return self._mix(*parts, buff=buff)

    def _boxes(self, values, side=0.72, color=BLUE, font_size=30):
        group = VGroup()
        for value in values:
            sq = Square(side_length=side, color=color, stroke_width=2)
            lab = MathTex(str(value), font_size=font_size)
            group.add(VGroup(sq, lab))
        group.arrange(RIGHT, buff=0.16)
        return group

    def _index_labels(self, boxes):
        labels = VGroup()
        for i, box in enumerate(boxes, start=1):
            lab = MathTex(str(i), font_size=22, color=GREY_B)
            lab.next_to(box, DOWN, buff=0.1)
            labels.add(lab)
        return labels

    def _chip(self, text):
        label = self.step_label(text)
        self.play(FadeIn(label), run_time=0.4)
        return label

    def _card(self, title, body, extra, color, width=4.0, height=2.15):
        box = RoundedRectangle(
            width=width,
            height=height,
            corner_radius=0.12,
            color=color,
            stroke_width=3,
            fill_color=color,
            fill_opacity=0.18,
        )
        t = self.ja_text(title, font_size=24, color=color)
        b = body if not isinstance(body, str) else self.ja_text(body, font_size=20)
        if extra is None:
            col = VGroup(t, b)
        elif isinstance(extra, str):
            col = VGroup(t, b, self.ja_text(extra, font_size=20, color=color))
        else:
            col = VGroup(t, b, extra)
        col.arrange(DOWN, buff=0.12)
        col.move_to(box.get_center())
        return VGroup(box, col)

    def _as_line(self, line, font_size=26):
        if isinstance(line, str):
            return self.ja_text(line, font_size=font_size)
        return line

    def _show_goals(self, lines):
        heading = self.ja_text("今回のゴール", font_size=28)
        heading.next_to(self.header, DOWN, buff=0.32)
        self.play(FadeIn(heading), run_time=0.45)
        items = VGroup(*[self._as_line(line, font_size=26) for line in lines])
        items.arrange(DOWN, buff=0.36, aligned_edge=LEFT)
        items.next_to(heading, DOWN, buff=0.45)
        items.set_x(0)
        for t in items:
            self.play(FadeIn(t, shift=RIGHT * 0.1), run_time=0.45)
            self.wait(1.3)
        self.wait(0.5)
        self._clear(VGroup(heading, items))

    def _show_overview(self, cards, caption_lines):
        heading = self.ja_text("今回の流れ", font_size=28)
        heading.next_to(self.header, DOWN, buff=0.32)
        self.play(FadeIn(heading), run_time=0.4)
        group = VGroup()
        for i, text in enumerate(cards):
            color = BLUE if i < 2 else ORANGE
            box = RoundedRectangle(
                width=12.2,
                height=0.7,
                corner_radius=0.1,
                color=color,
                stroke_width=2,
                fill_opacity=0.12,
            )
            lab = self._as_line(text, font_size=24)
            lab.move_to(box)
            group.add(VGroup(box, lab))
        group.arrange(DOWN, buff=0.14)
        group.next_to(heading, DOWN, buff=0.28)
        group.set_x(0)
        for card in group:
            self.play(FadeIn(card, shift=UP * 0.08), run_time=0.4)
            self.wait(1.0)
        cap = self._caption(*caption_lines)
        self.play(FadeIn(cap), run_time=0.4)
        self.wait(1.5)
        self._clear(VGroup(heading, group, cap))

    def _formula_rows(self, rows, under, buff=0.4):
        """Stack formula rows under ``under`` (the previous body, not a second chip)."""
        block = VGroup(*rows).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        self.stack_below(block, under, buff=buff)
        for row in block:
            self.play(FadeIn(row), run_time=0.4)
            self.wait(1.0)
        return block

    def _mix(self, *parts, buff=0.1):
        return VGroup(*parts).arrange(RIGHT, buff=buff)
