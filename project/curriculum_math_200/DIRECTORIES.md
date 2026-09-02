# 数学 200本 ディレクトリ計画

ルート: `project/curriculum_math_200/`

パス: `project/curriculum_math_200/{A|B}{章2桁}_{章スラッグ}/{番号3桁}_{レッスンスラッグ}/`

## 命名規則

既存の短尺シリーズ `project/math/{章番号}_{章スラッグ}/{本番号}_{レッスンスラッグ}/` に合わせ、**章フォルダの下に本フォルダ**を置く。

- ディレクトリ名は **ASCII 小文字 + 数字 + アンダースコア** のみ（日本語は使わない）。
- スラッグは英語の短い名詞句（32文字以内）。シリーズ内で重複しない。
- 本番号は ROADMAP の `#` と一致する **3桁ゼロ埋め**。
- 各本フォルダには、実装時に `storyboard.md` と `scene.py` を置く（この計画ではまだ作らない）。

このファイルは計画表である。空ディレクトリの一括作成は次の作業とする。

## 章フォルダ

| コード | フォルダ | 内容 | 本番号 |
|---|---|---|---|
| A01 | `A01_algebra/` | 数と式 | #1–#10 |
| A02 | `A02_sets_logic/` | 集合と論理 | #11–#16 |
| A03 | `A03_quadratic/` | 二次関数 | #17–#24 |
| A04 | `A04_analytic_geometry/` | 図形と方程式 | #25–#32 |
| A05 | `A05_trigonometry/` | 三角比・三角関数 | #33–#44 |
| A06 | `A06_exp_log/` | 指数・対数関数 | #45–#52 |
| A07 | `A07_sequences/` | 数列 | #53–#64 |
| A08 | `A08_probability/` | 場合の数・確率 | #65–#74 |
| A09 | `A09_geometry/` | 平面図形・空間図形 | #75–#82 |
| A10 | `A10_integers/` | 整数の性質 | #83–#88 |
| A11 | `A11_vectors/` | ベクトル | #89–#98 |
| A12 | `A12_complex/` | 複素数平面 | #99–#104 |
| A13 | `A13_calculus/` | 極限・微分・積分 | #105–#116 |
| A14 | `A14_applications/` | 数学と社会・総合演習 | #117–#120 |
| B01 | `B01_analysis/` | 微分積分学 | #121–#128 |
| B02 | `B02_multivariable/` | 多変数の微分積分 | #129–#136 |
| B03 | `B03_linear_algebra/` | 線形代数 | #137–#150 |
| B04 | `B04_ode/` | 常微分方程式 | #151–#156 |
| B05 | `B05_probability_stats/` | 確率論・統計学 | #157–#168 |
| B06 | `B06_topology/` | 集合・位相・論理 | #169–#174 |
| B07 | `B07_number_theory/` | 数論・離散数学 | #175–#180 |
| B08 | `B08_complex_analysis/` | 複素解析入門 | #181–#186 |
| B09 | `B09_abstract_algebra/` | 代数学入門 | #187–#192 |
| B10 | `B10_advanced/` | 総合・発展トピック | #193–#200 |

## 本フォルダ（200）

| # | タイトル | パス |
|---|---|---|
| 1 | 整式の展開と因数分解 | `A01_algebra/001_expand_and_factor/` |
| 2 | 因数分解の応用（複雑な式） | `A01_algebra/002_factoring_advanced/` |
| 3 | 平方根と分母の有理化 | `A01_algebra/003_square_roots_rationalize/` |
| 4 | 絶対値を含む方程式・不等式 | `A01_algebra/004_absolute_value_eq_ineq/` |
| 5 | 多項式の割り算 | `A01_algebra/005_polynomial_division/` |
| 6 | 剰余の定理と因数定理 | `A01_algebra/006_remainder_factor_theorem/` |
| 7 | 恒等式と係数比較 | `A01_algebra/007_identities_coefficients/` |
| 8 | 部分分数分解 | `A01_algebra/008_partial_fractions/` |
| 9 | 相加平均・相乗平均の関係 | `A01_algebra/009_am_gm/` |
| 10 | 不等式の証明技法 | `A01_algebra/010_inequality_proofs/` |
| 11 | 集合の基本演算（和集合・共通部分・補集合） | `A02_sets_logic/011_set_operations/` |
| 12 | ド・モルガンの法則 | `A02_sets_logic/012_de_morgan/` |
| 13 | 命題と条件 | `A02_sets_logic/013_propositions/` |
| 14 | 必要条件・十分条件 | `A02_sets_logic/014_necessary_sufficient/` |
| 15 | 対偶と背理法 | `A02_sets_logic/015_contrapositive_contradiction/` |
| 16 | 数学的帰納法の基本 | `A02_sets_logic/016_mathematical_induction/` |
| 17 | 二次関数の平行移動と頂点 | `A03_quadratic/017_quadratic_shift_vertex/` |
| 18 | 二次関数の最大値・最小値 | `A03_quadratic/018_quadratic_max_min/` |
| 19 | 二次方程式と判別式 | `A03_quadratic/019_quadratic_discriminant/` |
| 20 | 二次不等式の解き方 | `A03_quadratic/020_quadratic_inequalities/` |
| 21 | 解と係数の関係 | `A03_quadratic/021_vieta_formulas/` |
| 22 | 二次関数と二次方程式の融合問題 | `A03_quadratic/022_quadratic_mixed/` |
| 23 | 放物線と直線の共有点 | `A03_quadratic/023_parabola_line/` |
| 24 | 二次関数の応用（最適化問題） | `A03_quadratic/024_quadratic_optimization/` |
| 25 | 直線の方程式と傾き | `A04_analytic_geometry/025_line_equation_slope/` |
| 26 | 円の方程式 | `A04_analytic_geometry/026_circle_equation/` |
| 27 | 点と直線の距離 | `A04_analytic_geometry/027_point_line_distance/` |
| 28 | 二直線の位置関係（平行・垂直） | `A04_analytic_geometry/028_parallel_perpendicular/` |
| 29 | 円と直線の位置関係 | `A04_analytic_geometry/029_circle_and_line/` |
| 30 | 軌跡と方程式 | `A04_analytic_geometry/030_locus/` |
| 31 | 不等式の表す領域 | `A04_analytic_geometry/031_inequality_regions/` |
| 32 | 領域における最大・最小（線形計画法） | `A04_analytic_geometry/032_linear_programming/` |
| 33 | 三角比の定義（sin, cos, tan） | `A05_trigonometry/033_trig_ratios/` |
| 34 | 正弦定理 | `A05_trigonometry/034_law_of_sines/` |
| 35 | 余弦定理 | `A05_trigonometry/035_law_of_cosines/` |
| 36 | 三角形の面積公式 | `A05_trigonometry/036_triangle_area/` |
| 37 | 弧度法と単位円 | `A05_trigonometry/037_radians_unit_circle/` |
| 38 | 三角関数のグラフ | `A05_trigonometry/038_trig_graphs/` |
| 39 | 加法定理 | `A05_trigonometry/039_addition_formulas/` |
| 40 | 三角関数の合成 | `A05_trigonometry/040_trig_synthesis/` |
| 41 | 積和公式・和積公式 | `A05_trigonometry/041_product_sum_formulas/` |
| 42 | 三角方程式・三角不等式 | `A05_trigonometry/042_trig_eq_ineq/` |
| 43 | 三角関数の最大・最小 | `A05_trigonometry/043_trig_max_min/` |
| 44 | 三角関数の応用（周期現象のモデル化） | `A05_trigonometry/044_trig_periodic_models/` |
| 45 | 指数法則と指数関数 | `A06_exp_log/045_exponential_laws/` |
| 46 | 対数の定義と性質 | `A06_exp_log/046_log_definition/` |
| 47 | 対数関数のグラフ | `A06_exp_log/047_log_graphs/` |
| 48 | 指数方程式・対数方程式 | `A06_exp_log/048_exp_log_equations/` |
| 49 | 指数不等式・対数不等式 | `A06_exp_log/049_exp_log_inequalities/` |
| 50 | 常用対数と桁数の問題 | `A06_exp_log/050_common_log_digits/` |
| 51 | 指数関数的な増加・減少モデル | `A06_exp_log/051_exponential_growth/` |
| 52 | ネイピア数 e の直感的な導入 | `A06_exp_log/052_napier_e/` |
| 53 | 等差数列 | `A07_sequences/053_arithmetic_sequence/` |
| 54 | 等比数列 | `A07_sequences/054_geometric_sequence/` |
| 55 | 数列の和（シグマ記号） | `A07_sequences/055_sequence_sums_sigma/` |
| 56 | シグマ公式の導出 | `A07_sequences/056_sigma_formulas/` |
| 57 | 階差数列 | `A07_sequences/057_difference_sequence/` |
| 58 | 漸化式の基本 | `A07_sequences/058_recurrence/` |
| 59 | 連立漸化式 | `A07_sequences/059_simultaneous_recurrence/` |
| 60 | 数学的帰納法による証明（数列） | `A07_sequences/060_induction_sequences/` |
| 61 | 無限級数の基礎 | `A07_sequences/061_infinite_series_intro/` |
| 62 | 群数列 | `A07_sequences/062_grouped_sequences/` |
| 63 | 漸化式と数列の応用問題 | `A07_sequences/063_recurrence_applications/` |
| 64 | 数列と関数の融合問題 | `A07_sequences/064_sequence_function_mixed/` |
| 65 | 順列 | `A08_probability/065_permutations/` |
| 66 | 円順列・重複順列 | `A08_probability/066_circular_permutations/` |
| 67 | 組合せ | `A08_probability/067_combinations/` |
| 68 | 二項定理 | `A08_probability/068_binomial_theorem/` |
| 69 | 確率の基本 | `A08_probability/069_probability_basics/` |
| 70 | 余事象の確率 | `A08_probability/070_complementary_probability/` |
| 71 | 条件付き確率 | `A08_probability/071_conditional_probability/` |
| 72 | 独立な試行の確率 | `A08_probability/072_independent_trials/` |
| 73 | 期待値 | `A08_probability/073_expected_value/` |
| 74 | 漸化式を用いた確率の計算 | `A08_probability/074_recurrence_probability/` |
| 75 | 三角形の重心・内心・外心 | `A09_geometry/075_triangle_centers/` |
| 76 | 円に内接する四角形の性質 | `A09_geometry/076_cyclic_quadrilateral/` |
| 77 | メネラウスの定理とチェバの定理 | `A09_geometry/077_menelaus_ceva/` |
| 78 | 円と接線・接弦定理 | `A09_geometry/078_tangent_chord/` |
| 79 | 相似と面積比・体積比 | `A09_geometry/079_similarity_ratios/` |
| 80 | 空間図形の基本（多面体） | `A09_geometry/080_polyhedra/` |
| 81 | 空間図形の切断 | `A09_geometry/081_solid_sections/` |
| 82 | 立体の展開図と最短経路 | `A09_geometry/082_nets_shortest_path/` |
| 83 | 約数と倍数 | `A10_integers/083_divisors_multiples/` |
| 84 | ユークリッドの互除法 | `A10_integers/084_euclidean_algorithm/` |
| 85 | 合同式（mod）の基本 | `A10_integers/085_modular_arithmetic/` |
| 86 | 一次不定方程式の整数解 | `A10_integers/086_linear_diophantine/` |
| 87 | n進法 | `A10_integers/087_base_n/` |
| 88 | 整数問題の総合演習 | `A10_integers/088_integer_problems/` |
| 89 | 平面ベクトルの基本演算 | `A11_vectors/089_plane_vectors/` |
| 90 | ベクトルの内積 | `A11_vectors/090_inner_product/` |
| 91 | 位置ベクトルと図形への応用 | `A11_vectors/091_position_vectors/` |
| 92 | 内分点・外分点とベクトル | `A11_vectors/092_internal_external_division/` |
| 93 | 空間ベクトルの基本 | `A11_vectors/093_space_vectors/` |
| 94 | 空間における直線・平面の方程式 | `A11_vectors/094_lines_planes_space/` |
| 95 | 法線ベクトルと平面 | `A11_vectors/095_normal_vector/` |
| 96 | ベクトル方程式 | `A11_vectors/096_vector_equations/` |
| 97 | ベクトルを用いた図形の証明 | `A11_vectors/097_vector_proofs/` |
| 98 | 空間図形とベクトルの応用 | `A11_vectors/098_space_vector_apps/` |
| 99 | 複素数の四則演算 | `A12_complex/099_complex_arithmetic/` |
| 100 | 複素数平面と極形式 | `A12_complex/100_complex_polar/` |
| 101 | ド・モアブルの定理 | `A12_complex/101_de_moivre/` |
| 102 | 複素数と図形問題 | `A12_complex/102_complex_geometry/` |
| 103 | 複素数の回転と拡大 | `A12_complex/103_complex_rotation/` |
| 104 | 複素数のn乗根 | `A12_complex/104_complex_nth_roots/` |
| 105 | 数列の極限 | `A13_calculus/105_sequence_limits/` |
| 106 | 関数の極限 | `A13_calculus/106_function_limits/` |
| 107 | 微分係数と導関数の定義 | `A13_calculus/107_derivative_definition/` |
| 108 | 導関数の基本公式（積・商・合成関数） | `A13_calculus/108_derivative_rules/` |
| 109 | 三角関数・指数関数・対数関数の微分 | `A13_calculus/109_trig_exp_log_derivatives/` |
| 110 | 接線と法線の方程式 | `A13_calculus/110_tangent_normal/` |
| 111 | 関数の増減とグラフの作成 | `A13_calculus/111_increase_decrease_graphs/` |
| 112 | 不定積分の基本 | `A13_calculus/112_indefinite_integral/` |
| 113 | 定積分と面積 | `A13_calculus/113_definite_integral_area/` |
| 114 | 置換積分・部分積分（高校範囲） | `A13_calculus/114_substitution_parts/` |
| 115 | 回転体の体積 | `A13_calculus/115_solids_of_revolution/` |
| 116 | 微分・積分の応用（速度・近似） | `A13_calculus/116_calc_applications/` |
| 117 | 統計的な推測の基礎（高校範囲） | `A14_applications/117_statistical_inference/` |
| 118 | データの分析（分散・標準偏差・相関係数） | `A14_applications/118_data_analysis/` |
| 119 | 数学的モデリングの考え方 | `A14_applications/119_mathematical_modeling/` |
| 120 | 高校数学の総合演習（複数分野の融合問題） | `A14_applications/120_hs_comprehensive/` |
| 121 | ε–δ論法と極限の厳密な定義 | `B01_analysis/121_epsilon_delta/` |
| 122 | 連続関数と中間値の定理 | `B01_analysis/122_continuity_ivt/` |
| 123 | 平均値の定理 | `B01_analysis/123_mean_value_theorem/` |
| 124 | テイラー展開とマクローリン展開 | `B01_analysis/124_taylor_maclaurin/` |
| 125 | 広義積分（収束・発散） | `B01_analysis/125_improper_integrals/` |
| 126 | 級数の収束判定法 | `B01_analysis/126_series_tests/` |
| 127 | 一様収束 | `B01_analysis/127_uniform_convergence/` |
| 128 | 微分方程式入門（変数分離形） | `B01_analysis/128_separable_ode/` |
| 129 | 多変数関数と偏微分 | `B02_multivariable/129_partial_derivatives/` |
| 130 | 全微分と接平面 | `B02_multivariable/130_total_differential/` |
| 131 | 陰関数定理 | `B02_multivariable/131_implicit_function/` |
| 132 | 多変数のテイラー展開 | `B02_multivariable/132_multivariable_taylor/` |
| 133 | 極値問題とヘッセ行列 | `B02_multivariable/133_extrema_hessian/` |
| 134 | ラグランジュの未定乗数法 | `B02_multivariable/134_lagrange_multipliers/` |
| 135 | 重積分（累次積分） | `B02_multivariable/135_multiple_integrals/` |
| 136 | 変数変換とヤコビアン | `B02_multivariable/136_jacobian/` |
| 137 | ベクトル空間の基本 | `B03_linear_algebra/137_vector_spaces/` |
| 138 | 一次独立・一次従属と基底 | `B03_linear_algebra/138_linear_independence_basis/` |
| 139 | 行列の演算と基本変形 | `B03_linear_algebra/139_matrix_operations/` |
| 140 | 連立一次方程式と掃き出し法 | `B03_linear_algebra/140_gaussian_elimination/` |
| 141 | 行列式の定義と性質 | `B03_linear_algebra/141_determinants/` |
| 142 | 逆行列とその求め方 | `B03_linear_algebra/142_inverse_matrix/` |
| 143 | 一次変換と行列 | `B03_linear_algebra/143_linear_transformations/` |
| 144 | 固有値と固有ベクトル | `B03_linear_algebra/144_eigenvalues/` |
| 145 | 対角化 | `B03_linear_algebra/145_diagonalization/` |
| 146 | 内積空間と正規直交基底 | `B03_linear_algebra/146_inner_product_spaces/` |
| 147 | グラム・シュミットの直交化 | `B03_linear_algebra/147_gram_schmidt/` |
| 148 | 対称行列と直交対角化 | `B03_linear_algebra/148_orthogonal_diagonalization/` |
| 149 | 線形写像の階数・次元定理 | `B03_linear_algebra/149_rank_nullity/` |
| 150 | ジョルダン標準形の直感 | `B03_linear_algebra/150_jordan_form/` |
| 151 | 一階線形微分方程式 | `B04_ode/151_first_order_linear_ode/` |
| 152 | 二階線形微分方程式（定数係数・斉次） | `B04_ode/152_second_order_homogeneous/` |
| 153 | 二階線形微分方程式（非斉次） | `B04_ode/153_second_order_nonhomogeneous/` |
| 154 | 連立微分方程式と行列 | `B04_ode/154_systems_of_ode/` |
| 155 | ラプラス変換の基礎 | `B04_ode/155_laplace_transform/` |
| 156 | 微分方程式の応用（振動・減衰） | `B04_ode/156_ode_oscillation/` |
| 157 | 確率空間と確率変数 | `B05_probability_stats/157_probability_space/` |
| 158 | 期待値と分散 | `B05_probability_stats/158_expectation_variance/` |
| 159 | 二項分布 | `B05_probability_stats/159_binomial_distribution/` |
| 160 | ポアソン分布 | `B05_probability_stats/160_poisson_distribution/` |
| 161 | 正規分布 | `B05_probability_stats/161_normal_distribution/` |
| 162 | 中心極限定理 | `B05_probability_stats/162_central_limit_theorem/` |
| 163 | 大数の法則 | `B05_probability_stats/163_law_of_large_numbers/` |
| 164 | 標本平均と推定 | `B05_probability_stats/164_sample_mean_estimation/` |
| 165 | 仮説検定の基礎 | `B05_probability_stats/165_hypothesis_testing/` |
| 166 | 相関と回帰分析 | `B05_probability_stats/166_correlation_regression/` |
| 167 | マルコフ連鎖の基礎 | `B05_probability_stats/167_markov_chains/` |
| 168 | ベイズ統計の基礎 | `B05_probability_stats/168_bayesian_statistics/` |
| 169 | 集合論の基礎（濃度・可算集合） | `B06_topology/169_set_theory_cardinality/` |
| 170 | 写像と全射・単射・全単射 | `B06_topology/170_maps_injective_surjective/` |
| 171 | 距離空間の基本 | `B06_topology/171_metric_spaces/` |
| 172 | 開集合・閉集合 | `B06_topology/172_open_closed_sets/` |
| 173 | コンパクト性の直感 | `B06_topology/173_compactness/` |
| 174 | 論理と証明の技法（数学的帰納法の一般化） | `B06_topology/174_proof_techniques/` |
| 175 | 素数と素因数分解 | `B07_number_theory/175_primes_factorization/` |
| 176 | オイラーの定理とフェルマーの小定理 | `B07_number_theory/176_euler_fermat/` |
| 177 | 中国剰余定理 | `B07_number_theory/177_chinese_remainder/` |
| 178 | グラフ理論の基礎（大学レベル） | `B07_number_theory/178_graph_theory_intro/` |
| 179 | 組合せ論（鳩の巣原理・包除原理） | `B07_number_theory/179_combinatorics_php_pie/` |
| 180 | 生成関数の基礎 | `B07_number_theory/180_generating_functions/` |
| 181 | 複素関数の基礎 | `B08_complex_analysis/181_complex_functions/` |
| 182 | コーシー・リーマンの方程式 | `B08_complex_analysis/182_cauchy_riemann/` |
| 183 | コーシーの積分定理 | `B08_complex_analysis/183_cauchy_integral/` |
| 184 | 留数定理入門 | `B08_complex_analysis/184_residue_theorem/` |
| 185 | 等角写像の基礎 | `B08_complex_analysis/185_conformal_maps/` |
| 186 | 複素関数の応用（流体・電磁場のモデル化） | `B08_complex_analysis/186_complex_applications/` |
| 187 | 群の定義と具体例 | `B09_abstract_algebra/187_groups/` |
| 188 | 部分群と巡回群 | `B09_abstract_algebra/188_subgroups_cyclic/` |
| 189 | 環と体の基礎 | `B09_abstract_algebra/189_rings_fields/` |
| 190 | 剰余環の考え方 | `B09_abstract_algebra/190_quotient_rings/` |
| 191 | 準同型写像と同型定理 | `B09_abstract_algebra/191_homomorphisms/` |
| 192 | ガロア理論への入り口 | `B09_abstract_algebra/192_galois_preview/` |
| 193 | フーリエ級数の基礎 | `B10_advanced/193_fourier_series/` |
| 194 | フーリエ変換の基礎 | `B10_advanced/194_fourier_transform/` |
| 195 | 変分法の初歩 | `B10_advanced/195_calculus_of_variations/` |
| 196 | 測度論の直感（ルベーグ積分入門） | `B10_advanced/196_measure_theory/` |
| 197 | 位相空間論の初歩（連続写像の一般化） | `B10_advanced/197_topology_intro/` |
| 198 | 数値解析の基礎（ニュートン法・数値積分） | `B10_advanced/198_numerical_analysis/` |
| 199 | 最適化理論の基礎（凸関数と最適化） | `B10_advanced/199_convex_optimization/` |
| 200 | 大学数学の総合演習（複数分野の融合問題） | `B10_advanced/200_university_comprehensive/` |
