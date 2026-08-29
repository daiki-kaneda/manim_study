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

以降の番号は `PLAN.md` を参照。
