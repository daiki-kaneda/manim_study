#!/usr/bin/env python3
"""Generate DIRECTORIES.md for the math and algorithm 200-lesson curricula."""

from __future__ import annotations

from pathlib import Path

from curriculum_catalog import (
    ALGO_CHAPTERS,
    ALGO_LESSONS,
    MATH_CHAPTERS,
    MATH_LESSONS,
    chapter_for,
    lesson_dir,
    validate,
)

ROOT = Path(__file__).resolve().parents[1]

NAMING = """## 命名規則

既存の短尺シリーズ `project/math/{章番号}_{章スラッグ}/{本番号}_{レッスンスラッグ}/` に合わせ、**章フォルダの下に本フォルダ**を置く。

- ディレクトリ名は **ASCII 小文字 + 数字 + アンダースコア** のみ（日本語は使わない）。
- スラッグは英語の短い名詞句（32文字以内）。シリーズ内で重複しない。
- 本番号は ROADMAP の `#` と一致する **3桁ゼロ埋め**。
- 各本フォルダには、実装時に `storyboard.md` と `scene.py` を置く（この計画ではまだ作らない）。
- 各動画は **必ず先に `storyboard.md` を書き、そのあと `scene.py` を実装する。**

このファイルは計画表である。空ディレクトリの一括作成は次の作業とする。
"""


def render(
    series: str,
    root: str,
    pattern: str,
    chapters: list,
    lessons: list,
) -> str:
    lines = [
        f"# {series} 200本 ディレクトリ計画",
        "",
        f"ルート: `{root}/`",
        "",
        f"パス: `{pattern}`",
        "",
        NAMING,
        "## 章フォルダ",
        "",
        "| コード | フォルダ | 内容 | 本番号 |",
        "|---|---|---|---|",
    ]
    for code, slug, title, lo, hi in chapters:
        lines.append(f"| {code} | `{code}_{slug}/` | {title} | #{lo}–#{hi} |")

    lines += [
        "",
        "## 本フォルダ（200）",
        "",
        "| # | タイトル | パス |",
        "|---|---|---|",
    ]
    for n, title, slug in lessons:
        code, ch_slug, _ = chapter_for(n, chapters)
        rel = lesson_dir(code, ch_slug, n, slug)
        lines.append(f"| {n} | {title} | `{rel}/` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    validate()
    math_md = render(
        "数学",
        "project/curriculum_math_200",
        "project/curriculum_math_200/{A|B}{章2桁}_{章スラッグ}/{番号3桁}_{レッスンスラッグ}/",
        MATH_CHAPTERS,
        MATH_LESSONS,
    )
    algo_md = render(
        "アルゴリズム",
        "project/curriculum_algorithm_200",
        "project/curriculum_algorithm_200/D{章2桁}_{章スラッグ}/{番号3桁}_{レッスンスラッグ}/",
        ALGO_CHAPTERS,
        ALGO_LESSONS,
    )
    (ROOT / "project/curriculum_math_200/DIRECTORIES.md").write_text(math_md, encoding="utf-8")
    (ROOT / "project/curriculum_algorithm_200/DIRECTORIES.md").write_text(algo_md, encoding="utf-8")
    print("wrote DIRECTORIES.md for math and algorithm")


if __name__ == "__main__":
    main()
