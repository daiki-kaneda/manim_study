from manim import *

class TexExample(Scene):
    def construct(self):
        # TeXで数式を作成
        tex = Tex(r"$\frac{d}{dx}e^x = e^x$")
        
        # 数式をアニメーションで表示
        self.play(Write(tex))
        self.wait(2)

        # 数式の色を変更
        self.play(tex.animate.set_color(RED))
        self.wait(2)

        # 数式を移動
        self.play(tex.animate.shift(UP))
        self.wait(2)
