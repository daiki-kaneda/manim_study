from manim import *
# ピタゴラスの定理の証明解説の構成
# 1.辺にラベルがついた直角三角形を表示して定理の内容を紹介
# 2.いっぺんの長さがa+bとなるような正方形を表示する
# 3.対象の直角三角形4つを大きな正方形にうまく埋め込み,空欄の面積がc^2であることを示す
# 4.直角三角形を再配置して、a^2,b^2が現れる等式を導く
# 5.結果の式を導く
# (6.まとめ)


from manim import *

class PythagorasTheorem(Scene):
    def construct(self):
        self.japanese_tex_template = TexTemplate(
            tex_compiler='xelatex', 
            output_format='.xdv',    
            documentclass='\\documentclass[preview]{standalone}',
            preamble=r"""
            \usepackage{amsmath}
            \usepackage{amssymb}
            \usepackage{fontspec} 
            \setmainfont{HannariMincho-Regular} 
            """
    )
        self.a_val=2.5
        self.b_val=3.5
        # 1. 定理の紹介
        self.introduce_theorem()
        self.wait(0.5)
        
        # 2. 大きな正方形の構築
        self.construct_large_square()
        self.wait(0.5)

        # 3. 直角三角形とc^2正方形の配置
        self.arrange_triangles_and_c_square()
        self.wait(0.5)
        
         # 4. 直角三角形を再配置する
        self.rearrange_to_a_b_squares()
        self.wait(0.5)

        #5. 結果の式を導く
        self.derive_final_equation()
        self.wait(2.5)

    #     # 6. まとめと結論
    #     self.summarize_and_conclude()

    # 直角三角形を取得するためのutility
    def get_right_triangle(self,with_label:bool=False,color:ManimColor=BLUE,a_val:int=4,b_val:int=3,fill_opacity:float=0.75,show_angle:bool=False,angle_color:ManimColor=WHITE):
        triangle = Polygon(
            ORIGIN,
            RIGHT * a_val,
            UP * b_val,
            color=color, 
            fill_opacity = fill_opacity
        )

        vertices = triangle.get_vertices()
        right_angle = RightAngle(Line(vertices[0],vertices[1]), Line(vertices[0],vertices[2]),length=0.4,stroke_width=1,color=angle_color)

        right_triangle = VGroup(triangle)
        if show_angle:
            right_triangle.add(right_angle)

        if not with_label:
            return right_triangle
        else:
            label_a = MathTex("a").next_to(triangle.get_critical_point(DOWN), DOWN * 0.5)
            label_b = MathTex("b").next_to(triangle.get_critical_point(LEFT), LEFT * 0.5)
            
            hypotenuse_midpoint = (RIGHT * a_val + UP * b_val) / 2
            label_c = MathTex("c").move_to(hypotenuse_midpoint).shift(UP*0.3)

            label_A = MathTex("A").next_to(triangle.get_critical_point(UL), UL*0.5)
            label_B = MathTex("B").next_to(triangle.get_critical_point(DR), )
            label_C = MathTex("C").next_to(triangle.get_critical_point(DL),LEFT*1)
            
            return VGroup(
                right_triangle,
                label_a,
                label_b,
                label_c,
                label_A,
                label_B,
                label_C
            )


    def introduce_theorem(self):
        """
        辺にラベルがついた直角三角形を表示し、ピタゴラスの定理の内容を紹介します。
        """
        triangle = self.get_right_triangle(with_label=True,show_angle=True,a_val=self.a_val,b_val=self.b_val).move_to(LEFT*2)
        # ピタゴラスの定理の式と名前
        theorem_formula = MathTex("a^2 + b^2 = c^2").scale(1.5).next_to(triangle, RIGHT, buff=2.0)
        theorem_name = Text("ピタゴラスの定理").next_to(theorem_formula, UP, buff=0.5).scale(0.8)

        # アニメーション: 三角形の作成、ラベルの表示、定理の表示
        self.play(Create(triangle))
        self.play(Write(theorem_name), Write(theorem_formula))
        self.play(Indicate(theorem_formula,color=BLUE))
        self.wait(2) 
        
        # すべてのオブジェクトをフェードアウトして次のステップへ
        self.play(
            FadeOut(VGroup(triangle, theorem_name, theorem_formula)),
            run_time=1.5
        )


    def construct_large_square(self):
        """
        一辺の長さが (a+b) となる大きな正方形を作成する
        """
        # 導入で使用した辺の長さの値を保持
        self.side_length = self.a_val + self.b_val
        
        # 大きな正方形を作成し、画面中央に配置
        self.large_square_main = Square(side_length=self.side_length, color=GREEN, fill_opacity=0.2)
        self.main_group = VGroup(self.large_square_main)
        
        edge_label = MathTex("a+b").next_to(self.large_square_main.get_critical_point(DOWN),DOWN)
        
        # アニメーション: 正方形の作成
        self.play(Create(self.main_group))
        self.play(Write(edge_label))
        self.wait(3)
        self.play(FadeOut(edge_label))


    def arrange_triangles_and_c_square(self):
        """
        最初の大きな正方形の内部に、4つの直角三角形と1つの辺cの正方形を配置します。
        """
        right_triangle = self.get_right_triangle(a_val=self.a_val,b_val=self.b_val)
        self.triangle1 = right_triangle.copy().shift((-self.side_length/2,-self.side_length/2,0))
        self.triangle2 = self.triangle1.copy().rotate_about_origin(90*DEGREES)
        self.triangle3 = self.triangle1.copy().rotate_about_origin(180*DEGREES)
        self.triangle4 = self.triangle1.copy().rotate_about_origin(270*DEGREES)

        self.label_a = MathTex("a").next_to(self.triangle1.get_critical_point(DOWN), DOWN * 0.5)
        self.label_b = MathTex("b").next_to(self.triangle1.get_critical_point(LEFT), LEFT * 0.5)
        hypotenuse_midpoint = (-self.side_length/4,-self.side_length/4,0)
        self.label_c = MathTex("c").move_to(hypotenuse_midpoint).shift(UP*0.3)
        
        for triangle in [self.triangle1,
            self.triangle2,
            self.triangle3,
            self.triangle4,]:
            self.main_group.add(triangle)
            self.play(Create(triangle))

        self.wait(1)

        self.play(AnimationGroup(Create(self.label_a),Create(self.label_b),Create(self.label_c)))
        self.main_group.add(self.label_a,self.label_b,self.label_c)
        self.wait(1)
        self.play(self.main_group.animate.shift(LEFT*2.5))

        self.eq1_final = Tex("空欄の面積 = $c^2$",tex_template = self.japanese_tex_template).next_to(self.large_square_main.get_critical_point(UR),DR).shift(RIGHT)

        self.blank_area1 = MathTex("c^2").shift(LEFT*2.5)
        self.play(Create(self.blank_area1))
        self.wait(0.5)
        self.play(Write(self.eq1_final))
        self.wait(3)



    def rearrange_to_a_b_squares(self):
        """
        同一の大きな正方形の別の配置として、2つの辺a, 辺bの正方形と
        4つの直角三角形（概念的に2つのab長方形を形成）を配置します。
        """
        self.play(LaggedStart(
            AnimationGroup(
                FadeOut(self.label_a),
                FadeOut(self.label_b),
                FadeOut(self.label_c),
                FadeOut(self.blank_area1),
                self.triangle3.animate.shift((-self.b_val,-self.a_val,0))
            ),
            self.triangle2.animate.shift((0,self.b_val,0)),
            self.triangle4.animate.shift((self.a_val,0,0)),
            lag_ratio=1.0
        )),
        self.play(            
            AnimationGroup(
            Create(self.label_a.move_to(self.large_square_main.get_critical_point(LEFT)).shift(UP*self.b_val/2).shift(LEFT*0.2)),
            Create(self.label_b.move_to(self.large_square_main.get_critical_point(LEFT)).shift(DOWN*self.a_val/2).shift(LEFT*0.2)),
            ))

        self.wait(1.5)
        self.blank_area2 = MathTex("a^2")
        self.blank_area3 = MathTex("b^2")
        self.play(AnimationGroup(
            Create(self.blank_area2.move_to(self.large_square_main.get_critical_point(LEFT)).shift(UP*self.b_val/2).shift(RIGHT*self.a_val/2)),
            Create(self.blank_area3.move_to(self.large_square_main.get_critical_point(LEFT)).shift(DOWN*self.a_val/2).shift(RIGHT*(self.a_val+self.b_val/2)),
            )
        ))
        self.wait(1.5)
        self.eq2_final = Tex("空欄の面積 = $a^2 + b^2$",tex_template = self.japanese_tex_template).next_to(self.large_square_main.get_critical_point(UR),DR).shift(RIGHT).shift(DOWN)
        self.play(Write(self.eq2_final))



    def derive_final_equation(self):
        """
        2つの異なる空欄の面積表現を比較し、
        最終的にピタゴラスの定理の式 $a^2 + b^2 = c^2$ を導きます。
        """

        self.play(
            Indicate(self.eq1_final.get_part_by_tex("空欄の面積"), color=GREEN_C),
            Indicate(self.eq2_final.get_part_by_tex("空欄の面積"), color=GREEN_C),
        )
        self.wait(1.0)
        
        final_theorem_result = MathTex("a^2 + b^2 = c^2",).move_to(RIGHT*4)

        self.play(TransformMatchingTex(VGroup(self.eq1_final,self.eq2_final),final_theorem_result))
        self.play(Indicate(final_theorem_result,color=BLUE))


    def summarize_and_conclude(self):
        return