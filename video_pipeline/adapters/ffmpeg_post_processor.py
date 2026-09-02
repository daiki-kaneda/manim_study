from __future__ import annotations

import subprocess
from pathlib import Path

from video_pipeline.application.ports.post_processor import PostProcessorPort
from video_pipeline.domain.errors import PostProcessError
from video_pipeline.domain.models import PostProcessOptions


class FfmpegPostProcessor(PostProcessorPort):
    """Calls ``scripts/add_bg_bgm.sh``. The use case never sees ffmpeg."""

    def __init__(self, script_path: Path) -> None:
        self._script = script_path

    def apply(self, video: Path, options: PostProcessOptions, dest: Path) -> Path:
        if not options.enabled:
            raise PostProcessError("背景も BGM も指定されていません")
        if not self._script.is_file():
            raise PostProcessError(f"後処理スクリプトがありません: {self._script}")
        dest.parent.mkdir(parents=True, exist_ok=True)

        cmd = [
            str(self._script),
            "--input",
            str(video),
            "--output",
            str(dest),
            "--volume",
            str(options.volume),
            "--fade",
            str(options.fade_seconds),
            "--mode",
            options.mode,
        ]
        if options.background is not None:
            cmd.extend(["--bg", str(options.background)])
        if options.bgm is not None:
            cmd.extend(["--bgm", str(options.bgm)])

        try:
            completed = subprocess.run(cmd, check=False, capture_output=True, text=True)
        except OSError as exc:
            raise PostProcessError(f"ffmpeg 後処理を起動できません: {exc}") from exc

        if completed.returncode != 0:
            detail = (completed.stderr or completed.stdout or "").strip()
            raise PostProcessError(f"後処理が失敗しました (exit {completed.returncode}): {detail[-2000:]}")
        if not dest.is_file():
            raise PostProcessError(f"後処理の出力がありません: {dest}")
        return dest
