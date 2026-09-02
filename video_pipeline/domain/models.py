from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class SceneSource:
    """What to generate. No Manim types here."""

    scene_file: Path
    scene_name: str
    quality: str = "l"  # l / m / h / k


@dataclass(frozen=True)
class PostProcessOptions:
    """Background and BGM. Paths are opaque; ffmpeg stays in the adapter."""

    background: Path | None = None
    bgm: Path | None = None
    volume: float = 0.18
    fade_seconds: float = 2.0
    mode: str = "colorkey"

    @property
    def enabled(self) -> bool:
        return self.background is not None or self.bgm is not None


@dataclass(frozen=True)
class PublishOptions:
    """Optional upload. YouTube specifics stay in the adapter."""

    title: str
    description: str = ""
    privacy: str = "unlisted"


@dataclass(frozen=True)
class BuildRequest:
    source: SceneSource
    output_dir: Path
    filename: str | None = None
    post_process: PostProcessOptions | None = None
    publish: PublishOptions | None = None

    @property
    def output_name(self) -> str:
        if self.filename:
            name = self.filename
        else:
            name = self.source.scene_name
        if not name.endswith(".mp4"):
            name = f"{name}.mp4"
        return name


@dataclass(frozen=True)
class BuildResult:
    local_path: Path
    upload_id: str | None = None
