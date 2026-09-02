from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from video_pipeline.application.ports.renderer import VideoRendererPort
from video_pipeline.domain.errors import RenderError
from video_pipeline.domain.models import SceneSource

QUALITY_FLAGS = {
    "l": "-ql",
    "m": "-qm",
    "h": "-qh",
    "k": "-qk",
}


def find_rendered_video(media_root: Path, scene_name: str) -> Path:
    """Newest ``{scene_name}.mp4`` under Manim's media directory."""
    matches = [p for p in media_root.rglob(f"{scene_name}.mp4") if p.is_file()]
    if not matches:
        raise RenderError(f"生成動画が見つかりません: {scene_name}.mp4 under {media_root}")
    return max(matches, key=lambda p: p.stat().st_mtime)


class ManimRenderer(VideoRendererPort):
    """Runs Manim as a subprocess. The use case never imports manim."""

    def __init__(self, repo_root: Path, media_root: Path | None = None) -> None:
        self._repo_root = repo_root
        self._media_root = media_root or (repo_root / "media" / "videos")

    def render(self, source: SceneSource) -> Path:
        flag = QUALITY_FLAGS.get(source.quality)
        if flag is None:
            raise RenderError(f"不明な quality: {source.quality} (l/m/h/k)")

        scene_file = source.scene_file
        if not scene_file.is_absolute():
            scene_file = self._repo_root / scene_file
        if not scene_file.is_file():
            raise RenderError(f"シーンファイルがありません: {scene_file}")

        cmd = [sys.executable, "-m", "manim", flag, str(scene_file), source.scene_name]
        try:
            completed = subprocess.run(
                cmd,
                cwd=self._repo_root,
                check=False,
                capture_output=True,
                text=True,
            )
        except OSError as exc:
            raise RenderError(f"Manim を起動できません: {exc}") from exc

        if completed.returncode != 0:
            detail = (completed.stderr or completed.stdout or "").strip()
            raise RenderError(f"Manim が失敗しました (exit {completed.returncode}): {detail[-2000:]}")

        return find_rendered_video(self._media_root, source.scene_name)
