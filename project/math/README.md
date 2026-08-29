# 数学100本

1チャンネル・BGMのみ・各本おおよそ 1〜2 分。まずはこのフォルダで数学100本を完走する。

## 再生コマンド

リポジトリのルートで:

```bash
export PYTHONPATH=.
# 低画質プレビュー
manim -pql project/math/01_proofs_without_words/02_triangle_area/scene.py TriangleArea
manim -pql project/math/01_proofs_without_words/03_arithmetic_sum/scene.py ArithmeticSum
manim -pql project/math/01_proofs_without_words/04_odd_squares/scene.py OddSquares

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

以降の番号は `PLAN.md` を参照。
