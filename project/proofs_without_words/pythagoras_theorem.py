from manim import *
# ピタゴラスの定理の証明解説の構成
# 1.IntroduceTheorem:辺にラベルがついた直角三角形を表示して定理の内容を紹介
# 2.ConstructLargeSquare:いっぺんの長さがa+bとなるような正方形を表示し、その面積を表示
# 3.ArrageTrianglesAndCSquares:対象の直角三角形4つを大きな正方形にうまく埋め込む
# 4.RearrageToABSquares:直角三角形を再配置して、a^2,b^2が現れる等式を導く
# 5.DriveFinalEquation:結果の式を導く
# 6.SummarizeAndConclude:まとめ


from manim import *

class PythagorasTheorem(Scene):
    def construct(self):
           
    #     """
    #     ピタゴラスの定理の代数的証明を Manim でアニメーション化するメインメソッドです。
    #     各ステップのメソッドを順に呼び出して証明を進行させます。
    #     """
        self.japanese_tex_template = japanese_tex_template = TexTemplate(
    tex_compiler='xelatex', # ★ xelatex を明示的に指定
    output_format='.xdv',    # ★ PDF 出力が最も安定
    documentclass='\\documentclass[preview]{standalone}',
    preamble=r"""
        \usepackage{amsmath}
        \usepackage{amssymb}
        \usepackage{fontspec}    % ★ システムフォントを使うためのパッケージ
        \setmainfont{HannariMincho-Regular} % ★★★ あなたの環境での正確なPostScript名をここに記述 ★★★
                                     % 例: HiraginoSans-W3 (Macのヒラギノ角ゴ)
                                     % 例: YuGo-Medium (游ゴシック Medium)
        % \usepackage{zxjatype}   % 日本語組版ルールが必要な場合は追加 (フォント問題解決後)
        % \usepackage{pxjahyper}  % 日本語PDFのしおりなどが必要な場合は追加 (フォント問題解決後)
    """
    )
        self.a_val=2.5
        self.b_val=3.5
        # 1. 定理の紹介
        self.introduce_theorem()
        self.wait(0.5) # シーン間の短いポーズ

    #     # 2. 大きな正方形の構築
        self.construct_large_square()
        self.wait(0.5)

        self.arrange_triangles_and_c_square()
        self.wait(0.5)


    #     # 3. 直角三角形とc^2正方形の配置 (a+b)^2 = 2ab + c^2 を示す
    #     self.arrange_triangles_and_c_square()
    #     self.wait(0.5)

    #     # 4. 直角三角形を再配置して、a^2, b^2が現れる等式を導く (a+b)^2 = a^2 + b^2 + 2ab を示す
        self.rearrange_to_a_b_squares()
        self.wait(0.5)

        # 5. 結果の式を導く
        # self.derive_final_equation()
        # self.wait(0.5)

    #     # 6. まとめと結論
    #     self.summarize_and_conclude()
    #     self.wait(2) # 最後のポーズ
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
            # ラベルの位置を調整するとより見やすくなります
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
        self.wait(2) # 2秒間表示
        
        # すべてのオブジェクトをフェードアウトして次のステップへ
        self.play(
            FadeOut(VGroup(triangle, theorem_name, theorem_formula)),
            run_time=1.5
        )


    def construct_large_square(self):
        """
        一辺の長さが (a+b) となる大きな正方形を作成し、その面積を示します。
        この正方形は、以降の証明の土台となります。
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
        self.wait(1.5)
        self.play(FadeOut(edge_label))


    def arrange_triangles_and_c_square(self):
        """
        最初の大きな正方形の内部に、4つの直角三角形と1つの辺cの正方形を配置します。
        これにより、面積の表現 $ (a+b)^2 = 2ab + c^2 $ を示します。
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
        self.play(AnimationGroup(Write(self.eq1_final),Create(self.blank_area1)))
        self.wait(1.5)



    def rearrange_to_a_b_squares(self):
        """
        同一の大きな正方形の別の配置として、2つの辺a, 辺bの正方形と
        4つの直角三角形（概念的に2つのab長方形を形成）を配置します。
        これにより、面積の表現 $(a+b)^2 = a^2 + b^2 + 2ab$ を示します。
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
            lag_ratio=0.3
        ))

        self.wait(0.5)
        self.blank_area2 = MathTex("a^2")
        self.blank_area3 = MathTex("b^2")
        self.play(AnimationGroup(
            Create(self.label_a.move_to(self.large_square_main.get_critical_point(LEFT)).shift(UP*self.b_val/2)),
            Create(self.label_a.move_to(self.large_square_main.get_critical_point(LEFT)).shift(DOWN*self.a_val/2)),
        ))



    def derive_final_equation(self):
        """
        2つの異なる面積表現 (2ab + c^2 と a^2 + b^2 + 2ab) を比較し、
        最終的にピタゴラスの定理の式 $a^2 + b^2 = c^2$ を導きます。
        """
        # 前のステップのオブジェクトをすべてフェードアウトして、式を中央に表示する準備


        # 2つの面積の式を中央に表示
        eq1_final = MathTex("(a+b)^2 = 2ab + c^2").shift(UP * 1.5)
        eq2_final = MathTex("(a+b)^2 = a^2 + b^2 + 2ab").shift(DOWN * 1.5)

        self.play(Write(eq1_final))
        self.play(Write(eq2_final))
        self.wait(1)

        # 左辺が等しいことを強調
        self.play(
            Indicate(eq1_final.get_part_by_tex("(a+b)^2"), color=GREEN_C),
            Indicate(eq2_final.get_part_by_tex("(a+b)^2"), color=GREEN_C)
        )
        self.wait(1)

        # 左辺が等しいので、右辺同士を等式で結ぶ
        equated_rhs = MathTex("2ab + c^2 = a^2 + b^2 + 2ab")
        # `TransformMatchingTex` を使用して、前の2つの式から新しい式へ変換
        self.play(TransformMatchingTex(VGroup(eq1_final, eq2_final), equated_rhs))
        self.wait(1.5)

        # 両辺から共通項 2ab を消去するアニメーション
        # `get_part_by_tex` は同じ文字列が複数ある場合、リストで返します
        term_to_remove_left = equated_rhs.get_part_by_tex("2ab")[0]
        term_to_remove_right = equated_rhs.get_part_by_tex("2ab")[1]

        self.play(
            FadeOut(term_to_remove_left, shift=DOWN*0.5), # 下に少し移動させながらフェードアウト
            FadeOut(term_to_remove_right, shift=DOWN*0.5)
        )
        self.wait(0.5)

        # 最終的なピタゴラスの定理の式
        final_theorem_result = MathTex("c^2 = a^2 + b^2").move_to(equated_rhs.get_center())
        # `TransformMatchingTex` を使用して、古い式から新しい式へ変換
        self.play(TransformMatchingTex(equated_rhs, final_theorem_result))
        self.wait(2)
        
        # 最終結果をフェードアウト
        self.play(FadeOut(final_theorem_result))


    # def summarize_and_conclude(self):
    #     """
    #     証明のまとめと結論を表示します。
    #     """
    #     conclusion_text = Text("これで、ピタゴラスの定理が証明されました！").scale(0.8)
    #     self.play(Write(conclusion_text))
    #     self.wait(1)
        
    #     # 再度定理の式を表示し、強調
    #     final_formula_display = MathTex("a^2 + b^2 = c^2").scale(1.8).next_to(conclusion_text, DOWN, buff=1.0)
    #     self.play(Write(final_formula_display))
    #     self.play(Indicate(final_formula_display, scale_factor=1.2, color=YELLOW_A)) # 明るい黄色で強調
    #     self.wait(3)
        
    #     # 全てのオブジェクトをフェードアウトしてアニメーションを終了
    #     self.play(FadeOut(VGroup(conclusion_text, final_formula_display)))