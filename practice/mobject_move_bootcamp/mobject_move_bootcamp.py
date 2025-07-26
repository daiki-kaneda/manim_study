from manim import *

# Mobjectの移動のためのメソッド

# move_to...絶対位置に移動
# next_to...他のmobjectの相対位置に移動
# shift...Mobjectをシフトさせる(UP, DOWN, LEFT, RIGHT, ORIGINなどは、Manimにおいて大きさが1の方向を表す単位ベクトルで、shiftと相性がいい)

class MobjectMoveBootcamp(Scene):
    def construct(self):
        rect1 = Rectangle(color=RED,height=5).shift(ORIGIN)
        rect2 = Rectangle(color=ORANGE,height=3).shift(ORIGIN)
        rect3 = Rectangle(color=BLUE,width=5).shift(ORIGIN)
        isosceles = Polygon([-5, 1.5, 0], [-2, 1.5, 0], [-3.5, -2, 0]).move_to(ORIGIN) 
        self.add(rect1)
        self.add(rect2)
        self.add(rect3)
        self.add(isosceles)
        self.wait(duration=1.0)
        self.play(isosceles.animate.next_to(rect1))
        self.play(rect1.animate.shift(DOWN))
        self.wait(duration=1)
        self.play(rect2.animate.move_to(rect1.get_top()))

