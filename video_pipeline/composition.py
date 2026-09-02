from __future__ import annotations

import os
from pathlib import Path

from video_pipeline.adapters.ffmpeg_post_processor import FfmpegPostProcessor
from video_pipeline.adapters.local_storage import LocalStorage
from video_pipeline.adapters.manim_renderer import ManimRenderer
from video_pipeline.adapters.youtube_uploader import YouTubeUploader
from video_pipeline.application.use_cases.build_video import BuildVideoUseCase


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def build_use_case(root: Path | None = None) -> BuildVideoUseCase:
    """Wire real adapters. The only place that knows about Manim / ffmpeg / YouTube."""
    root = root or repo_root()
    token = os.environ.get("YOUTUBE_TOKEN_PATH")
    token_path = Path(token) if token else (root / "local" / "youtube_token.json")
    secrets = os.environ.get("YOUTUBE_CLIENT_SECRETS")
    secrets_path = Path(secrets) if secrets else None
    return BuildVideoUseCase(
        renderer=ManimRenderer(root),
        post_processor=FfmpegPostProcessor(root / "scripts" / "add_bg_bgm.sh"),
        storage=LocalStorage(),
        uploader=YouTubeUploader(token_path=token_path, client_secrets=secrets_path),
    )
