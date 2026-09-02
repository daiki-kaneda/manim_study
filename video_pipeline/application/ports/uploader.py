from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path

from video_pipeline.domain.models import PublishOptions


class UploaderPort(ABC):
    """Publish a local video. Hides YouTube."""

    @abstractmethod
    def upload(self, video: Path, options: PublishOptions) -> str:
        """Return an opaque upload id (YouTube video id in the real adapter)."""
