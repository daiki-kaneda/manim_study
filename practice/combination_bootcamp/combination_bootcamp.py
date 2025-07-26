# AnimationGroup...与えられた複数のアニメーションを同時に実行する
# LaggedStart...与えられた複数のアニメーションを順番に時間差(lag_ratio)で実行する
# Succession...与えられた複数のアニメーションを順番に前のアニメーションの完了を待って、実行する
from manim import *

class AnimationGroupBootcamp(Scene):
    def construct(self):
        square = Square(color=RED).shift(LEFT * 2)
        circle = Circle(color=BLUE).shift(RIGHT * 2)
        triangle = Triangle(color=GREEN).shift(UP * 2)

        self.add(square, circle, triangle)
        self.wait(0.5)

        self.play(AnimationGroup(
            square.animate.shift(RIGHT * 4),    
            circle.animate.shift(LEFT * 4),    
            triangle.animate.shift(DOWN * 4)    
        ))
        self.wait(1)

class LaggedStartBootcamp(Scene):
    def construct(self):
        rect1 = Rectangle(color=RED)
        rect2 = Rectangle(color=YELLOW)
        rect3 = Rectangle(color=PURPLE)
        
        self.add(rect1,rect2,rect3)
        rect1.shift(LEFT*2)
        rect2.shift(RIGHT*2)
        rect3.shift(DOWN*2)

        self.play(LaggedStart(
            rect1.animate.move_to(ORIGIN),
            rect2.animate.move_to(ORIGIN),
            rect3.animate.move_to(ORIGIN),
            lag_ratio=0.25
        ))

class SuccessionBootcamp(Scene):
    def construct(self):
        eq1 = MathTex("a^2 + b^2").to_edge(UP)
        self.play(Write(eq1))

        eq2 = MathTex("= (a+b)^2 - 2ab").next_to(eq1, DOWN)
        self.play(Succession(
            TransformMatchingTex(eq1, eq2), # 式の変換アニメーション
            Indicate(eq2, scale_factor=1.1)  # 変換後の強調アニメーション
        ))
        self.wait(1)
        
        eq3 = MathTex("= a^2 + 2ab + b^2 - 2ab").next_to(eq2, DOWN)
        self.play(TransformMatchingTex(eq2, eq3))
        self.wait(1)