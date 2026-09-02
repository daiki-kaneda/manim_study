from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path

from video_pipeline.domain.models import SceneSource


class VideoRendererPort(ABC):
    """Generate a video from a scene. Hides Manim."""

    @abstractmethod
    def render(self, source: SceneSource) -> Path:
        """Return the path of the raw generated video."""
