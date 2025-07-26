# VGroup...複数のMobjectをひとつのグループとして扱うためのMobject.コードの簡略化に役立つ.buffはアイテム館のスペースを表す
from manim import *

class VGroupBootcamp1(Scene):
    def construct(self):
        rect1 = Square(color=RED, side_length=0.8)
        rect1_label = Text("Item 1").next_to(rect1, DOWN, buff=0.1)
        labeled_rect1 = VGroup(rect1,rect1_label)

        rect2 = Square(color=BLUE, side_length=0.8)
        rect2_label = Text("Item 2").next_to(rect2, DOWN, buff=0.1)
        labeled_rect2 = VGroup(rect2,rect2_label)

        circle = Circle(color=ORANGE,)
        circle_label = Text("Item 3").next_to(circle, DOWN, buff=0.1)
        labeled_circle = VGroup(circle,circle_label)

        shapes = VGroup(labeled_rect1,labeled_rect2,labeled_circle).arrange(RIGHT)
        self.play(Create(shapes))
        self.wait(duration=1.0)
    