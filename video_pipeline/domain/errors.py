"""Domain / application errors. Adapters map tool failures onto these."""


class PipelineError(Exception):
    """Base error for the video pipeline."""


class RenderError(PipelineError):
    """Video generation failed."""


class PostProcessError(PipelineError):
    """Background / BGM post-process failed."""


class StorageError(PipelineError):
    """Local save failed."""


class UploadError(PipelineError):
    """Upload failed."""
