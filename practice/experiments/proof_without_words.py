from manim import *

class SquareOutline(Scene):
    def __init__(self,**keywords):
        super().__init__(**keywords)

    def construct(self):
        square = Square(fill_opacity=0)
        self.play(FadeIn(square))

class Triangle(Scene):
    def __init__(self,**keywords):
        super().__init__(**keywords)

    def construct(self):
        triangle = Polygon([-1, 0, 0], [-2, 1.5, 0], [-3.5, -2, 0])
        self.play(FadeIn(triangle))
