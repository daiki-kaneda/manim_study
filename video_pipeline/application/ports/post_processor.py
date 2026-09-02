from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path

from video_pipeline.domain.models import PostProcessOptions


class PostProcessorPort(ABC):
    """Add background and/or BGM. Hides ffmpeg."""

    @abstractmethod
    def apply(self, video: Path, options: PostProcessOptions, dest: Path) -> Path:
        """Return the processed video path (usually ``dest``)."""
