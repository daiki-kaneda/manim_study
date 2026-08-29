# 数学100本

1チャンネル・BGMのみ・各本おおよそ 1〜2 分。まずはこのフォルダで数学100本を完走する。

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

# 本番相当（1080p）
manim -pqh project/math/01_proofs_without_words/02_triangle_area/scene.py TriangleArea
```

ピタゴラス（#1）は従来のパスのまま:

```bash
manim -pqh project/proofs_without_words/pythagoras_theorem/pythagoras_theorem.py PythagorasTheorem
```

日本語フォントは `MANIM_JAPANESE_FONT` で上書きできる。未設定なら Hannari Mincho を優先し、なければ Noto / 文泉驛などにフォールバックする。

尺は `JapaneseScene.beat`（デフォルト 3 秒）で調整する。`beat = 3` だと #2〜#4 はおよそ 40〜50 秒。90 秒に近づけたいときはシーン側で `beat = 5` にする。

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

以降の番号は `PLAN.md` を参照。
