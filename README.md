# Manim 日本語数学動画

数学の定理・証明を日本語で短尺（1〜2分）にする練習および本番用リポジトリ。

- 共有ライブラリ: `manim_math/`（日本語 TeX / Text、幾何ヘルパー。長尺は `LessonScene`）
- 本番シーン: `project/`
- 数学動画の進捗: `project/math/PLAN.md`（#126 以降は 30秒〜1分、`PacedScene`）
- 数学 200本カリキュラム（高校〜大学レベル、1本5〜10分）のロードマップ: `project/curriculum_math_200/ROADMAP.md`
- アルゴリズム 200本カリキュラム（高校〜大学レベル、1本5〜10分）のロードマップ: `project/curriculum_algorithm_200/ROADMAP.md`
- 200本ディレクトリ計画: `project/curriculum_math_200/DIRECTORIES.md` / `project/curriculum_algorithm_200/DIRECTORIES.md`
- Cursor プロジェクトルール: `.cursor/rules/curriculum-roadmaps.mdc`（数学200本とアルゴリズム200本を独立シリーズとして扱う）

```bash
pip install -e .
export PYTHONPATH=.
manim -pql project/math/01_proofs_without_words/02_triangle_area/scene.py TriangleArea
```

日本語フォントは環境変数 `MANIM_JAPANESE_FONT` で指定できる（未設定なら Hannari Mincho を優先）。

動画のビルド（生成 → 任意で背景/BGM → ローカル保存 → 任意で YouTube）はクリーンアーキテクチャのユースケース `video_pipeline` 経由。Manim / ffmpeg / YouTube はポートの向こうに隠す。

```bash
# ローカル保存のみ
python -m video_pipeline --scene project/math/01_proofs_without_words/02_triangle_area/scene.py \
  --name TriangleArea --output-dir out/videos --quality l

# 背景・BGM を載せて保存（パスはフラグまたは local/media.env）
python -m video_pipeline --scene .../scene.py --name TriangleArea \
  --bg /path/to/bg.png --bgm /path/to/bgm.mp3 --output-dir out/videos

# YouTube へも上げる（local/youtube_token.json、pip install -e '.[youtube]'）
python -m video_pipeline --scene .../scene.py --name TriangleArea \
  --upload --title "三角形の面積" --privacy unlisted
```

ffmpeg を直接叩く場合:

```bash
cp local/media.env.example local/media.env
scripts/add_bg_bgm.sh --input media/videos/.../TriangleArea.mp4 \
  --bg /path/to/bg.png --bgm /path/to/bgm.mp3
```
