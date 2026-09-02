# Manim 日本語数学動画

数学の定理・証明を日本語で短尺（1〜2分）にする練習および本番用リポジトリ。

- 共有ライブラリ: `manim_math/`（日本語 TeX / Text、幾何ヘルパー）
- 本番シーン: `project/`
- 数学動画の進捗: `project/math/PLAN.md`（#126 以降は 30秒〜1分、`PacedScene`）
- 数学・アルゴリズム 200本カリキュラム（高校〜大学レベル、1本5〜10分）のロードマップ: `project/curriculum_200/ROADMAP.md`

```bash
pip install -e .
export PYTHONPATH=.
manim -pql project/math/01_proofs_without_words/02_triangle_area/scene.py TriangleArea
```

日本語フォントは環境変数 `MANIM_JAPANESE_FONT` で指定できる（未設定なら Hannari Mincho を優先）。
