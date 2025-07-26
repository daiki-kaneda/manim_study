from manim import *

# manim -r 1920,1080 --format=mov --transparent パス名 Sceneの名前
# 上のコマンドでYoutubeのサイズで背景透過された状態でビルドされる
class WriteTex(Scene):
    def construct(self):
        formula = MathTex(r"E = mc^2")
        self.play(Write(formula))
        self.wait(1)

class WriteComplexTex(Scene):
    def construct(self):
        formula = MathTex(r"\sum{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}")
        self.play(Write(formula))
        self.wait(1)
