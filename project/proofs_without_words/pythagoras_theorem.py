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
        self.add(self.get_right_triangle())
        return
           
    #     """
    #     ピタゴラスの定理の代数的証明を Manim でアニメーション化するメインメソッドです。
    #     各ステップのメソッドを順に呼び出して証明を進行させます。
    #     """
    #     # 1. 定理の紹介
    #     self.introduce_theorem()
    #     self.wait(0.5) # シーン間の短いポーズ

    #     # 2. 大きな正方形の構築
    #     self.construct_large_square()
    #     self.wait(0.5)

    #     # 3. 直角三角形とc^2正方形の配置 (a+b)^2 = 2ab + c^2 を示す
    #     self.arrange_triangles_and_c_square()
    #     self.wait(0.5)

    #     # 4. 直角三角形を再配置して、a^2, b^2が現れる等式を導く (a+b)^2 = a^2 + b^2 + 2ab を示す
    #     self.rearrange_to_a_b_squares()
    #     self.wait(0.5)

    #     # 5. 結果の式を導く
    #     self.derive_final_equation()
    #     self.wait(0.5)

    #     # 6. まとめと結論
    #     self.summarize_and_conclude()
    #     self.wait(2) # 最後のポーズ
    def get_right_triangle(with_label:bool=False,color:ManimColor=ORANGE,a_val:int=4,b_val:int=3):
        if not with_label:
            return  Polygon(
            ORIGIN,
            RIGHT * a_val,
            UP * b_val,
            color=color, 
            )
        else:
            return  VGroup(
            Polygon(
            ORIGIN,
            RIGHT * a_val,
            UP * b_val,
            color=color, 
            ),
            MathTex("a"),
            MathTex("b"),
            MathTex("c"),
            )


    # def introduce_theorem(self):
    #     """
    #     辺にラベルがついた直角三角形を表示し、ピタゴラスの定理の内容を紹介します。
    #     """
    #     # 仮の辺の長さ。実際の比率で表示されます。
    #     a_val, b_val = 3, 4
        
    #     # 直角三角形を作成し、画面中央に配置
    #     triangle = Polygon(
    #         ORIGIN,
    #         RIGHT * a_val,
    #         UP * b_val,
    #         color=BLUE_C, # 三角形の色
    #         fill_opacity=0.7 # 塗りつぶしの透明度
    #     ).move_to(ORIGIN)

    #     # 辺のラベルを作成し、適切な位置に配置
    #     # a: 底辺
    #     label_a = MathTex("a").next_to(Line(ORIGIN, RIGHT * a_val), DOWN, buff=0.2).align_to(triangle, DOWN).shift(RIGHT * a_val / 2)
    #     # b: 高さ
    #     label_b = MathTex("b").next_to(Line(ORIGIN, UP * b_val), LEFT, buff=0.2).align_to(triangle, LEFT).shift(UP * b_val / 2)
    #     # c: 斜辺 (斜辺に沿って配置)
    #     c_line_dummy = Line(triangle.get_vertices()[1], triangle.get_vertices()[2]) # ラベル配置用の一時的な線
    #     label_c = MathTex("c").next_to(c_line_dummy, UP + RIGHT, buff=0.2).shift(LEFT * 0.1) 

    #     # 直角マークを作成
    #     right_angle = RightAngle(
    #         Line(triangle.get_vertices()[0],
    #         triangle.get_vertices()[1],),
    #         Line(triangle.get_vertices()[0],
    #         triangle.get_vertices()[2],),
    #         length=0.4, # 直角マークのサイズ
    #         stroke_width=2,
    #         color=WHITE
    #     )

    #     # ピタゴラスの定理の式と名前
    #     theorem_formula = MathTex("a^2 + b^2 = c^2").scale(1.5).next_to(triangle, DOWN, buff=1.0)
    #     theorem_name = Text("ピタゴラスの定理").next_to(theorem_formula, UP, buff=0.5).scale(0.8)

    #     # アニメーション: 三角形の作成、ラベルの表示、定理の表示
    #     self.play(Create(triangle), Create(right_angle))
    #     self.play(Write(label_a), Write(label_b), Write(label_c))
    #     self.play(Write(theorem_name), Write(theorem_formula))
    #     self.wait(2) # 2秒間表示
        
    #     # すべてのオブジェクトをフェードアウトして次のステップへ
    #     self.play(
    #         FadeOut(VGroup(triangle, right_angle, label_a, label_b, label_c, theorem_name, theorem_formula)),
    #         run_time=1.5
    #     )


    # def construct_large_square(self):
    #     """
    #     一辺の長さが (a+b) となる大きな正方形を作成し、その面積を示します。
    #     この正方形は、以降の証明の土台となります。
    #     """
    #     # 導入で使用した辺の長さの値を保持
    #     self.a_val, self.b_val = 3, 4
    #     self.side_length = self.a_val + self.b_val
        
    #     # 大きな正方形を作成し、画面中央に配置
    #     self.large_square_main = Square(side_length=self.side_length, color=YELLOW_B, fill_opacity=0.2).move_to(ORIGIN)
        
    #     # 面積のラベルを表示
    #     area_label = MathTex(f"\\text{{Area}} = (a+b)^2").next_to(self.large_square_main, DOWN, buff=0.5)
        
    #     # アニメーション: 正方形の作成と面積ラベルの表示
    #     self.play(Create(self.large_square_main))
    #     self.play(Write(area_label))
    #     self.wait(1.5)
        
    #     # 面積ラベルをフェードアウト（正方形は残す）
    #     self.play(FadeOut(area_label))


    # def arrange_triangles_and_c_square(self):
    #     """
    #     最初の大きな正方形の内部に、4つの直角三角形と1つの辺cの正方形を配置します。
    #     これにより、面積の表現 $ (a+b)^2 = 2ab + c^2 $ を示します。
    #     """
    #     # 大きな正方形を左に移動させ、第1の配置の場所を確保
    #     self.play(self.large_square_main.animate.shift(LEFT * (self.side_length / 2 + 1.5))) # 少し間隔を空ける

    #     # 基本となる直角三角形 (頂点 (0,0), (a,0), (0,b) で作成)
    #     base_triangle = Polygon(
    #         ORIGIN,
    #         RIGHT * self.a_val,
    #         UP * self.b_val,
    #         color=RED_C,
    #         fill_opacity=0.7
    #     )

    #     # 4つの三角形を large_square_main の角に合わせて配置
    #     triangles_group = VGroup()
        
    #     # 1. 左下 (アライメント後、移動なし)
    #     t1 = base_triangle.copy().align_to(self.large_square_main, DL)
    #     triangles_group.add(t1)

    #     # 2. 右下 (90度反時計回り回転、位置調整)
    #     t2 = base_triangle.copy().rotate(PI/2).align_to(self.large_square_main, DR).shift(LEFT * self.b_val)
    #     triangles_group.add(t2)

    #     # 3. 右上 (180度回転、位置調整)
    #     t3 = base_triangle.copy().rotate(PI).align_to(self.large_square_main, UR).shift(LEFT * self.a_val + DOWN * self.b_val)
    #     triangles_group.add(t3)

    #     # 4. 左上 (270度反時計回り回転、位置調整)
    #     t4 = base_triangle.copy().rotate(3*PI/2).align_to(self.large_square_main, UL).shift(DOWN * self.a_val)
    #     triangles_group.add(t4)
        
    #     # 中央の辺cの正方形
    #     c_val = np.sqrt(self.a_val**2 + self.b_val**2)
    #     self.c_square_obj = Square(side_length=c_val, color=GREEN_C, fill_opacity=0.7).move_to(self.large_square_main.get_center())

    #     # アニメーション: 三角形とc^2正方形の作成
    #     self.play(LaggedStart(*[Create(t) for t in triangles_group], run_time=2, lag_ratio=0.2)) # 順番に三角形を作成
    #     self.play(Create(self.c_square_obj))
    #     self.wait(1)

    #     # 面積の式を表示: (a+b)^2 の別の表現
    #     area_exp1_part1 = MathTex(f"(a+b)^2 = 4 \\times \\frac{{1}}{{2}}ab + c^2")
    #     area_exp1_part2 = MathTex(f"\\quad = 2ab + c^2")
        
    #     # 式を正方形の右隣に配置
    #     area_exp1_part1.next_to(self.large_square_main, RIGHT, buff=1.5).shift(UP * 1.5)
    #     area_exp1_part2.next_to(area_exp1_part1, DOWN)

    #     self.play(Write(area_exp1_part1))
    #     self.play(Write(area_exp1_part2))
    #     self.wait(2)
        
    #     # 後のステップでフェードアウトするためにグループ化して保持
    #     self.first_arrangement_objects = VGroup(triangles_group, self.c_square_obj, area_exp1_part1, area_exp1_part2)


    # def rearrange_to_a_b_squares(self):
    #     """
    #     同一の大きな正方形の別の配置として、2つの辺a, 辺bの正方形と
    #     4つの直角三角形（概念的に2つのab長方形を形成）を配置します。
    #     これにより、面積の表現 $(a+b)^2 = a^2 + b^2 + 2ab$ を示します。
    #     """
    #     # 最初の配置をフェードアウト
    #     self.play(FadeOut(self.first_arrangement_objects))

    #     # 2つ目の大きな正方形を、最初の正方形の右隣に作成
    #     # large_square_main が左にある状態から、その右に新しい正方形を表示
    #     self.large_square_alt = self.large_square_main.copy().shift(RIGHT * (self.side_length + 3)) # 最初の正方形から十分に離す
    #     self.play(Create(self.large_square_alt))

    #     # 辺aの正方形と辺bの正方形を作成し、新しい大きな正方形の内部に配置
    #     a_squared_obj = Square(side_length=self.a_val, color=BLUE_B, fill_opacity=0.7).align_to(self.large_square_alt, UL)
    #     b_squared_obj = Square(side_length=self.b_val, color=BLUE_E, fill_opacity=0.7).align_to(self.large_square_alt, DR)

    #     # 残りのスペースを埋める2つの長方形 (それぞれが2つの直角三角形で構成されることを示唆)
    #     # 1つ目の長方形 (幅b, 高さa)
    #     rect1_obj = Rectangle(width=self.b_val, height=self.a_val, color=RED_C, fill_opacity=0.7).align_to(a_squared_obj, DR)
    #     # 2つ目の長方形 (幅a, 高さb)
    #     rect2_obj = Rectangle(width=self.a_val, height=self.b_val, color=RED_C, fill_opacity=0.7).align_to(b_squared_obj, UL)

    #     # アニメーション: a^2, b^2 正方形と2つの長方形の作成
    #     self.play(Create(a_squared_obj), Create(b_squared_obj))
    #     self.play(Create(rect1_obj), Create(rect2_obj))
    #     self.wait(1)

    #     # 面積の式を表示
    #     area_exp3 = MathTex(f"(a+b)^2 = a^2 + b^2 + 2ab")
    #     area_exp3.next_to(self.large_square_alt, RIGHT, buff=1.5).shift(UP * 0.5)
        
    #     self.play(Write(area_exp3))
    #     self.wait(2)

    #     # この配置のオブジェクトを保持し、次のステップでフェードアウトする
    #     self.second_arrangement_objects = VGroup(
    #         self.large_square_main, # 最初の正方形もここで含めておく
    #         self.large_square_alt,
    #         a_squared_obj, b_squared_obj, rect1_obj, rect2_obj, area_exp3
    #     )


    # def derive_final_equation(self):
    #     """
    #     2つの異なる面積表現 (2ab + c^2 と a^2 + b^2 + 2ab) を比較し、
    #     最終的にピタゴラスの定理の式 $a^2 + b^2 = c^2$ を導きます。
    #     """
    #     # 前のステップのオブジェクトをすべてフェードアウトして、式を中央に表示する準備
    #     self.play(FadeOut(self.second_arrangement_objects))

    #     # 2つの面積の式を中央に表示
    #     eq1_final = MathTex("(a+b)^2 = 2ab + c^2").shift(UP * 1.5)
    #     eq2_final = MathTex("(a+b)^2 = a^2 + b^2 + 2ab").shift(DOWN * 1.5)

    #     self.play(Write(eq1_final))
    #     self.play(Write(eq2_final))
    #     self.wait(1)

    #     # 左辺が等しいことを強調
    #     self.play(
    #         Indicate(eq1_final.get_part_by_tex("(a+b)^2"), color=GREEN_C),
    #         Indicate(eq2_final.get_part_by_tex("(a+b)^2"), color=GREEN_C)
    #     )
    #     self.wait(1)

    #     # 左辺が等しいので、右辺同士を等式で結ぶ
    #     equated_rhs = MathTex("2ab + c^2 = a^2 + b^2 + 2ab")
    #     # `TransformMatchingTex` を使用して、前の2つの式から新しい式へ変換
    #     self.play(TransformMatchingTex(VGroup(eq1_final, eq2_final), equated_rhs))
    #     self.wait(1.5)

    #     # 両辺から共通項 2ab を消去するアニメーション
    #     # `get_part_by_tex` は同じ文字列が複数ある場合、リストで返します
    #     term_to_remove_left = equated_rhs.get_part_by_tex("2ab")[0]
    #     term_to_remove_right = equated_rhs.get_part_by_tex("2ab")[1]

    #     self.play(
    #         FadeOut(term_to_remove_left, shift=DOWN*0.5), # 下に少し移動させながらフェードアウト
    #         FadeOut(term_to_remove_right, shift=DOWN*0.5)
    #     )
    #     self.wait(0.5)

    #     # 最終的なピタゴラスの定理の式
    #     final_theorem_result = MathTex("c^2 = a^2 + b^2").move_to(equated_rhs.get_center())
    #     # `TransformMatchingTex` を使用して、古い式から新しい式へ変換
    #     self.play(TransformMatchingTex(equated_rhs, final_theorem_result))
    #     self.wait(2)
        
    #     # 最終結果をフェードアウト
    #     self.play(FadeOut(final_theorem_result))


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