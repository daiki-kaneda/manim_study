from __future__ import annotations

import argparse
import os
from pathlib import Path

from video_pipeline.composition import build_use_case, repo_root
from video_pipeline.domain.errors import PipelineError
from video_pipeline.domain.models import BuildRequest, PostProcessOptions, PublishOptions, SceneSource


def _load_media_env(root: Path) -> None:
    env_file = Path(os.environ.get("MANIM_MEDIA_ENV", root / "local" / "media.env"))
    if not env_file.is_file():
        return
    for raw in env_file.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


def _parse_args(argv: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="シーンをビルドしてローカル保存し、任意で YouTube にアップロードする。"
    )
    parser.add_argument("--scene", required=True, help="scene.py へのパス")
    parser.add_argument("--name", required=True, help="Manim の Scene クラス名")
    parser.add_argument("--output-dir", default="out/videos", help="ローカル保存先ディレクトリ")
    parser.add_argument("--filename", default=None, help="保存ファイル名 (default: <name>.mp4)")
    parser.add_argument("--quality", choices=("l", "m", "h", "k"), default="l")
    parser.add_argument("--bg", default=None, help="背景画像または動画")
    parser.add_argument("--bgm", default=None, help="BGM 音声")
    parser.add_argument("--volume", type=float, default=None)
    parser.add_argument("--fade", type=float, default=None)
    parser.add_argument("--mode", default="colorkey", choices=("colorkey", "screen", "opaque"))
    parser.add_argument("--upload", action="store_true", help="YouTube にアップロードする")
    parser.add_argument("--title", default=None, help="YouTube タイトル (--upload 時)")
    parser.add_argument("--description", default="", help="YouTube 説明")
    parser.add_argument("--privacy", default="unlisted", choices=("private", "unlisted", "public"))
    return parser.parse_args(argv)


def request_from_args(args: argparse.Namespace) -> BuildRequest:
    bg = args.bg or os.environ.get("MANIM_BG_PATH") or None
    bgm = args.bgm or os.environ.get("MANIM_BGM_PATH") or None
    post = None
    if bg or bgm:
        post = PostProcessOptions(
            background=Path(bg).expanduser() if bg else None,
            bgm=Path(bgm).expanduser() if bgm else None,
            volume=args.volume if args.volume is not None else float(os.environ.get("MANIM_BGM_VOLUME", "0.18")),
            fade_seconds=args.fade if args.fade is not None else float(os.environ.get("MANIM_BGM_FADE", "2")),
            mode=args.mode,
        )

    publish = None
    if args.upload:
        title = args.title or args.name
        publish = PublishOptions(title=title, description=args.description, privacy=args.privacy)

    scene = Path(args.scene)
    return BuildRequest(
        source=SceneSource(scene_file=scene, scene_name=args.name, quality=args.quality),
        output_dir=Path(args.output_dir),
        filename=args.filename,
        post_process=post,
        publish=publish,
    )


def main(argv: list[str] | None = None) -> int:
    root = repo_root()
    _load_media_env(root)
    args = _parse_args(argv)
    request = request_from_args(args)
    try:
        result = build_use_case(root).execute(request)
    except PipelineError as exc:
        print(f"error: {exc}", flush=True)
        return 1
    print(f"saved: {result.local_path}")
    if result.upload_id:
        print(f"uploaded: {result.upload_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
