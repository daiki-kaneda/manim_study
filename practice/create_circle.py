from manim import *


class CreateCircle(Scene):
    # Scene（アニメーションの動画を表すクラス）はconstructでMobjectの追加、削除、アニメーションを行う
    def construct(self):
        circle = Circle()  # 円（Mobject)のインスタンスを作成
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # Sceneのplayメソッド：Mobjectとアニメーションを指定してアニメーションを起こす