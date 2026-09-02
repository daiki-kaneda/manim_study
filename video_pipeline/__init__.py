"""Video build pipeline (clean architecture).

Layers:
- ``domain``: models and errors (no I/O)
- ``application``: ports and use cases
- ``adapters``: Manim / ffmpeg / filesystem / YouTube
- ``cli`` / ``composition``: wiring only
"""

from video_pipeline.application.use_cases.build_video import BuildVideoUseCase
from video_pipeline.domain.models import BuildRequest, BuildResult

__all__ = ["BuildRequest", "BuildResult", "BuildVideoUseCase"]
