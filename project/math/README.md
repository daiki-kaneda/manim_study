# 数学100本

1チャンネル・BGMのみ。新しい本は **30秒〜1分**（動きで稼ぐ。間で水増ししない）。

## 再生コマンド

リポジトリのルートで:

```bash
export PYTHONPATH=.
# 低画質プレビュー
manim -pql project/math/01_proofs_without_words/02_triangle_area/scene.py TriangleArea
manim -pql project/math/01_proofs_without_words/03_arithmetic_sum/scene.py ArithmeticSum
manim -pql project/math/01_proofs_without_words/05_sine_addition/scene.py SineAddition
manim -pql project/math/02_geometry/06_inscribed_angle/scene.py InscribedAngle
manim -pql project/math/03_algebra/12_binomial_square/scene.py BinomialSquare
manim -pql project/math/04_calculus/16_derivative_tangent/scene.py DerivativeTangent
manim -pql project/math/04_calculus/20_e_definition/scene.py EDefinition
manim -pql project/math/05_identities/21_euler_formula/scene.py EulerFormula
manim -pql project/math/06_classical/27_am_gm/scene.py AMGM
manim -pql project/math/07_linear_algebra/31_linear_map/scene.py LinearMap
manim -pql project/math/08_probability/36_expected_value/scene.py ExpectedValue
manim -pql project/math/10_combinatorics/50_midpoint_recap/scene.py MidpointRecap
manim -pql project/math/11_trig/51_law_of_sines/scene.py LawOfSines
manim -pql project/math/12_series/60_fourier_square/scene.py FourierSquare
manim -pql project/math/14_ode/66_slope_field/scene.py SlopeField
manim -pql project/math/16_optimization/76_cauchy_schwarz/scene.py CauchySchwarz
manim -pql project/math/17_graphs/81_euler_circuit/scene.py EulerCircuit
manim -pql project/math/18_stats/87_least_squares/scene.py LeastSquares
manim -pql project/math/19_synthesis/91_euler_identity/scene.py EulerIdentity
manim -pql project/math/20_recap/100_closing_map/scene.py ClosingMap
manim -pql project/math/21_vector_calculus/101_gradient/scene.py Gradient
manim -pql project/math/22_linear_algebra_2/108_rank_nullity/scene.py RankNullity
manim -pql project/math/23_analysis_2/111_mean_value/scene.py MeanValue
manim -pql project/math/24_geometry_2/116_euler_char/scene.py EulerCharacteristic
manim -pql project/math/25_info/125_monte_carlo_pi/scene.py MonteCarloPi
manim -pql project/math/26_analysis_3/126_arc_length/scene.py ArcLength
manim -pql project/math/28_geometry_3/131_ceva/scene.py Ceva
manim -pql project/math/29_probability_2/137_catalan/scene.py Catalan
manim -pql project/math/30_analysis_4/138_substitution/scene.py Substitution
manim -pql project/math/32_geometry_4/145_nine_point/scene.py NinePoint
manim -pql project/math/33_combinatorics_2/149_fibonacci/scene.py Fibonacci
manim -pql project/math/34_analysis_5/150_disk_method/scene.py DiskMethod
manim -pql project/math/36_geometry_5/156_napoleon/scene.py Napoleon
manim -pql project/math/38_number_2/161_euler_totient/scene.py EulerTotient
manim -pql project/math/39_analysis_6/162_surface_area/scene.py SurfaceOfRevolution
manim -pql project/math/41_geometry_6/169_morley/scene.py Morley
manim -pql project/math/43_combinatorics_3/173_stirling/scene.py Stirling
manim -pql project/math/44_analysis_7/175_fourier_transform/scene.py FourierTransform
manim -pql project/math/46_geometry_7/180_desargues/scene.py Desargues
manim -pql project/math/48_combinatorics_4/185_bell/scene.py BellNumbers

# 本番相当（1080p）
manim -pqh project/math/01_proofs_without_words/02_triangle_area/scene.py TriangleArea
```

ピタゴラス（#1）は従来のパスのまま:

```bash
manim -pqh project/proofs_without_words/pythagoras_theorem/pythagoras_theorem.py PythagorasTheorem
```

日本語フォントは `MANIM_JAPANESE_FONT` で上書きできる。未設定なら Hannari Mincho を優先し、なければ Noto / 文泉驛などにフォールバックする。

尺の目安は 30秒〜1分。#126 以降は `PacedScene` でアニメーションを約2.5倍にし、静止の待ちは `read(秒)` で短くする。古いシーンの `JapaneseScene.beat` / `hold` はそのまま。

## 番号

| # | タイトル | パス |
|---|---|---|
| 1 | ピタゴラスの定理 | `project/proofs_without_words/pythagoras_theorem/` |
| 2 | 三角形の面積 | `project/math/01_proofs_without_words/02_triangle_area/` |
| 3 | 等差数列の和 | `project/math/01_proofs_without_words/03_arithmetic_sum/` |
| 4 | 奇数の和は平方数 | `project/math/01_proofs_without_words/04_odd_squares/` |
| 5 | 加法定理 | `project/math/01_proofs_without_words/05_sine_addition/` |
| 6 | 円周角の定理 | `project/math/02_geometry/06_inscribed_angle/` |
| 7 | AA 相似 | `project/math/02_geometry/07_aa_similarity/` |
| 8 | 中点連結定理 | `project/math/02_geometry/08_midpoint_theorem/` |
| 9 | 接線と弦 | `project/math/02_geometry/09_tangent_chord/` |
| 10 | ベクトルの加法 | `project/math/02_geometry/10_vector_parallelogram/` |
| 11 | √2 は無理数 | `project/math/03_algebra/11_sqrt2_irrational/` |
| 12 | (a+b)² の展開 | `project/math/03_algebra/12_binomial_square/` |
| 13 | 等比数列の和 | `project/math/03_algebra/13_geometric_series/` |
| 14 | a³+b³ の因数分解 | `project/math/03_algebra/14_sum_of_cubes/` |
| 15 | 判別式 | `project/math/03_algebra/15_discriminant/` |
| 16 | 微分 | `project/math/04_calculus/16_derivative_tangent/` |
| 17 | 積分 | `project/math/04_calculus/17_integral_area/` |
| 18 | 合成関数の微分 | `project/math/04_calculus/18_chain_rule/` |
| 19 | 部分積分 | `project/math/04_calculus/19_integration_by_parts/` |
| 20 | e の定義 | `project/math/04_calculus/20_e_definition/` |
| 21 | オイラーの公式 | `project/math/05_identities/21_euler_formula/` |
| 22 | ド・モアブルの定理 | `project/math/05_identities/22_de_moivre/` |
| 23 | sin²+cos²=1 | `project/math/05_identities/23_pythagorean_identity/` |
| 24 | sin のテイラー | `project/math/05_identities/24_taylor_sin/` |
| 25 | ベイズの定理 | `project/math/05_identities/25_bayes/` |
| 26 | 素数は無限 | `project/math/06_classical/26_infinite_primes/` |
| 27 | 相加相乗平均 | `project/math/06_classical/27_am_gm/` |
| 28 | 内角の和 | `project/math/06_classical/28_triangle_angle_sum/` |
| 29 | 円の面積 | `project/math/06_classical/29_circle_area/` |
| 30 | 中間値の定理 | `project/math/06_classical/30_intermediate_value/` |
| 31 | 線形変換 | `project/math/07_linear_algebra/31_linear_map/` |
| 32 | 行列式 | `project/math/07_linear_algebra/32_determinant_area/` |
| 33 | 固有ベクトル | `project/math/07_linear_algebra/33_eigenvectors/` |
| 34 | 行列の積 | `project/math/07_linear_algebra/34_matrix_composition/` |
| 35 | 逆行列 | `project/math/07_linear_algebra/35_inverse_matrix/` |
| 36 | 期待値 | `project/math/08_probability/36_expected_value/` |
| 37 | 分散 | `project/math/08_probability/37_variance/` |
| 38 | 独立 | `project/math/08_probability/38_independence/` |
| 39 | 大数の法則 | `project/math/08_probability/39_law_of_large_numbers/` |
| 40 | 中心極限定理 | `project/math/08_probability/40_central_limit/` |
| 41 | 互除法 | `project/math/09_number_theory/41_euclid_gcd/` |
| 42 | 合同式 | `project/math/09_number_theory/42_modular_clock/` |
| 43 | 素因数分解 | `project/math/09_number_theory/43_unique_factorization/` |
| 44 | 中国剰余定理 | `project/math/09_number_theory/44_chinese_remainder/` |
| 45 | フェルマー小定理 | `project/math/09_number_theory/45_fermat_little/` |
| 46 | パスカル | `project/math/10_combinatorics/46_pascal_triangle/` |
| 47 | 二項定理 | `project/math/10_combinatorics/47_binomial_coefficients/` |
| 48 | 包除原理 | `project/math/10_combinatorics/48_inclusion_exclusion/` |
| 49 | 鳩の巣原理 | `project/math/10_combinatorics/49_pigeonhole/` |
| 50 | 前半の地図 | `project/math/10_combinatorics/50_midpoint_recap/` |
| 51 | 正弦定理 | `project/math/11_trig/51_law_of_sines/` |
| 52 | 余弦定理 | `project/math/11_trig/52_law_of_cosines/` |
| 53 | 二倍角 | `project/math/11_trig/53_double_angle/` |
| 54 | 余弦の加法 | `project/math/11_trig/54_cosine_addition/` |
| 55 | 面積と正弦 | `project/math/11_trig/55_triangle_area_sine/` |
| 56 | 調和級数 | `project/math/12_series/56_harmonic_series/` |
| 57 | ライプニッツの π | `project/math/12_series/57_leibniz_pi/` |
| 58 | バーゼル問題 | `project/math/12_series/58_basel_problem/` |
| 59 | e^x のテイラー | `project/math/12_series/59_taylor_exp/` |
| 60 | フーリエ矩形波 | `project/math/12_series/60_fourier_square/` |
| 61 | 対偶 | `project/math/13_logic/61_contrapositive/` |
| 62 | ド・モルガン | `project/math/13_logic/62_de_morgan/` |
| 63 | 単射と全射 | `project/math/13_logic/63_injective_surjective/` |
| 64 | 量化子の順 | `project/math/13_logic/64_quantifier_order/` |
| 65 | 必要十分 | `project/math/13_logic/65_iff/` |
| 66 | 傾き場 | `project/math/14_ode/66_slope_field/` |
| 67 | 指数成長 | `project/math/14_ode/67_exponential_growth/` |
| 68 | 単振動 | `project/math/14_ode/68_harmonic_oscillator/` |
| 69 | ロジスティック | `project/math/14_ode/69_logistic_growth/` |
| 70 | 重ね合わせ | `project/math/14_ode/70_linear_superposition/` |
| 71 | 複素数の積 | `project/math/15_complex/71_complex_multiply/` |
| 72 | e^z | `project/math/15_complex/72_exp_map/` |
| 73 | 回転数 | `project/math/15_complex/73_winding_number/` |
| 74 | 1/z | `project/math/15_complex/74_one_over_z/` |
| 75 | 等角写像 | `project/math/15_complex/75_conformal/` |
| 76 | コーシー・シュワルツ | `project/math/16_optimization/76_cauchy_schwarz/` |
| 77 | 凸とイェンゼン | `project/math/16_optimization/77_jensen/` |
| 78 | 同じ周なら正方形 | `project/math/16_optimization/78_isoperimetric/` |
| 79 | 三角不等式 | `project/math/16_optimization/79_triangle_inequality/` |
| 80 | 極値 | `project/math/16_optimization/80_critical_point/` |
| 81 | 一筆書き | `project/math/17_graphs/81_euler_circuit/` |
| 82 | 握手補題 | `project/math/17_graphs/82_handshake/` |
| 83 | 木 | `project/math/17_graphs/83_tree/` |
| 84 | 彩色 | `project/math/17_graphs/84_graph_coloring/` |
| 85 | 最短路 | `project/math/17_graphs/85_shortest_path/` |
| 86 | 相関 | `project/math/18_stats/86_correlation/` |
| 87 | 最小二乗 | `project/math/18_stats/87_least_squares/` |
| 88 | 二項分布 | `project/math/18_stats/88_binomial/` |
| 89 | 信頼区間 | `project/math/18_stats/89_confidence_interval/` |
| 90 | 68–95–99.7 | `project/math/18_stats/90_empirical_rule/` |
| 91 | オイラーの等式 | `project/math/19_synthesis/91_euler_identity/` |
| 92 | ガウス積分 | `project/math/19_synthesis/92_gaussian_integral/` |
| 93 | 黄金比 | `project/math/19_synthesis/93_golden_ratio/` |
| 94 | グリーンの定理 | `project/math/19_synthesis/94_green/` |
| 95 | スケール | `project/math/19_synthesis/95_scaling/` |
| 96 | 解析の地図 | `project/math/20_recap/96_analysis_map/` |
| 97 | 代数の地図 | `project/math/20_recap/97_algebra_map/` |
| 98 | 図形の地図 | `project/math/20_recap/98_geometry_map/` |
| 99 | 偶然の地図 | `project/math/20_recap/99_chance_map/` |
| 100 | 100本の地図 | `project/math/20_recap/100_closing_map/` |
| 101 | 勾配 | `project/math/21_vector_calculus/101_gradient/` |
| 102 | 発散 | `project/math/21_vector_calculus/102_divergence/` |
| 103 | 回転 | `project/math/21_vector_calculus/103_curl/` |
| 104 | 基本定理 | `project/math/21_vector_calculus/104_ftc/` |
| 105 | 極座標の面積 | `project/math/21_vector_calculus/105_polar_area/` |
| 106 | 像 | `project/math/22_linear_algebra_2/106_image/` |
| 107 | 核 | `project/math/22_linear_algebra_2/107_nullspace/` |
| 108 | 階数と核 | `project/math/22_linear_algebra_2/108_rank_nullity/` |
| 109 | 正射影 | `project/math/22_linear_algebra_2/109_projection/` |
| 110 | 基底の取りかえ | `project/math/22_linear_algebra_2/110_change_of_basis/` |
| 111 | 平均値の定理 | `project/math/23_analysis_2/111_mean_value/` |
| 112 | ロピタル | `project/math/23_analysis_2/112_lhopital/` |
| 113 | はさみうち | `project/math/23_analysis_2/113_squeeze/` |
| 114 | 収束半径 | `project/math/23_analysis_2/114_radius/` |
| 115 | デルタ関数 | `project/math/23_analysis_2/115_dirac/` |
| 116 | 多面体公式 | `project/math/24_geometry_2/116_euler_char/` |
| 117 | ヘロンの公式 | `project/math/24_geometry_2/117_heron/` |
| 118 | 方べきの定理 | `project/math/24_geometry_2/118_power_of_a_point/` |
| 119 | 反転 | `project/math/24_geometry_2/119_inversion/` |
| 120 | 立体射影 | `project/math/24_geometry_2/120_stereographic/` |
| 121 | 誕生日 | `project/math/25_info/121_birthday/` |
| 122 | ランダムウォーク | `project/math/25_info/122_random_walk/` |
| 123 | エントロピー | `project/math/25_info/123_entropy/` |
| 124 | マルコフ連鎖 | `project/math/25_info/124_markov/` |
| 125 | モンテカルロの π | `project/math/25_info/125_monte_carlo_pi/` |
| 126 | 弧長 | `project/math/26_analysis_3/126_arc_length/` |
| 127 | 連続 | `project/math/26_analysis_3/127_epsilon_delta/` |
| 128 | トレース | `project/math/26_analysis_3/128_trace/` |
| 129 | 回転行列 | `project/math/27_linear_3/129_rotation_matrix/` |
| 130 | 特異値 | `project/math/27_linear_3/130_svd/` |
| 131 | チェバの定理 | `project/math/28_geometry_3/131_ceva/` |
| 132 | 内接円 | `project/math/28_geometry_3/132_incircle/` |
| 133 | トレミーの定理 | `project/math/28_geometry_3/133_ptolemy/` |
| 134 | 幾何分布 | `project/math/29_probability_2/134_geometric/` |
| 135 | ポアソン | `project/math/29_probability_2/135_poisson/` |
| 136 | 母関数 | `project/math/29_probability_2/136_generating_function/` |
| 137 | カタラン数 | `project/math/29_probability_2/137_catalan/` |
| 138 | 置換積分 | `project/math/30_analysis_4/138_substitution/` |
| 139 | 広義積分 | `project/math/30_analysis_4/139_improper/` |
| 140 | 偏微分 | `project/math/30_analysis_4/140_partial/` |
| 141 | 線積分 | `project/math/30_analysis_4/141_line_integral/` |
| 142 | 直交化 | `project/math/31_linear_4/142_gram_schmidt/` |
| 143 | 対角化 | `project/math/31_linear_4/143_diagonalize/` |
| 144 | 直交行列 | `project/math/31_linear_4/144_orthogonal_matrix/` |
| 145 | 九点円 | `project/math/32_geometry_4/145_nine_point/` |
| 146 | オイラー線 | `project/math/32_geometry_4/146_euler_line/` |
| 147 | メネラウスの定理 | `project/math/32_geometry_4/147_menelaus/` |
| 148 | 角の二等分線 | `project/math/32_geometry_4/148_angle_bisector/` |
| 149 | フィボナッチ | `project/math/33_combinatorics_2/149_fibonacci/` |
| 150 | 回転体 | `project/math/34_analysis_5/150_disk_method/` |
| 151 | ヤコビアン | `project/math/34_analysis_5/151_jacobian/` |
| 152 | 畳み込み | `project/math/34_analysis_5/152_convolution/` |
| 153 | スペクトル定理 | `project/math/35_linear_5/153_spectral/` |
| 154 | 消去法 | `project/math/35_linear_5/154_elimination/` |
| 155 | クラメルの公式 | `project/math/35_linear_5/155_cramer/` |
| 156 | ナポレオンの定理 | `project/math/36_geometry_5/156_napoleon/` |
| 157 | シムソン線 | `project/math/36_geometry_5/157_simson/` |
| 158 | ヴィヴィアニ | `project/math/36_geometry_5/158_viviani/` |
| 159 | 指数分布 | `project/math/37_probability_3/159_exponential/` |
| 160 | チェビシェフ | `project/math/37_probability_3/160_chebyshev/` |
| 161 | オイラーの φ | `project/math/38_number_2/161_euler_totient/` |
| 162 | 回転面 | `project/math/39_analysis_6/162_surface_area/` |
| 163 | ラプラシアン | `project/math/39_analysis_6/163_laplacian/` |
| 164 | フビニの定理 | `project/math/39_analysis_6/164_fubini/` |
| 165 | LU 分解 | `project/math/40_linear_6/165_lu/` |
| 166 | 正規方程式 | `project/math/40_linear_6/166_least_squares_geom/` |
| 167 | 擬似逆 | `project/math/40_linear_6/167_pseudoinverse/` |
| 168 | ファン・オーベル | `project/math/41_geometry_6/168_van_obel/` |
| 169 | モーリーの定理 | `project/math/41_geometry_6/169_morley/` |
| 170 | ブラフマグプタ | `project/math/41_geometry_6/170_brahmagupta/` |
| 171 | 確率の木 | `project/math/42_probability_4/171_bayes_tree/` |
| 172 | モーメント | `project/math/42_probability_4/172_moment/` |
| 173 | スターリング数 | `project/math/43_combinatorics_3/173_stirling/` |
| 174 | テイラー余り | `project/math/44_analysis_7/174_taylor_remainder/` |
| 175 | フーリエ変換 | `project/math/44_analysis_7/175_fourier_transform/` |
| 176 | 留数 | `project/math/44_analysis_7/176_residue/` |
| 177 | ハウスホルダー | `project/math/45_linear_7/177_householder/` |
| 178 | QR 分解 | `project/math/45_linear_7/178_qr/` |
| 179 | 条件数 | `project/math/45_linear_7/179_condition/` |
| 180 | デザルグの定理 | `project/math/46_geometry_7/180_desargues/` |
| 181 | パスカルの定理 | `project/math/46_geometry_7/181_pascal_hexagon/` |
| 182 | バタフライ定理 | `project/math/46_geometry_7/182_butterfly/` |
| 183 | ハザード | `project/math/47_probability_5/183_hazard/` |
| 184 | 同時分布 | `project/math/47_probability_5/184_joint/` |
| 185 | ベル数 | `project/math/48_combinatorics_4/185_bell/` |
