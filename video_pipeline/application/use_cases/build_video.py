from __future__ import annotations

from video_pipeline.application.ports.post_processor import PostProcessorPort
from video_pipeline.application.ports.renderer import VideoRendererPort
from video_pipeline.application.ports.storage import StoragePort
from video_pipeline.application.ports.uploader import UploaderPort
from video_pipeline.domain.models import BuildRequest, BuildResult


class BuildVideoUseCase:
    """Build a video, save it locally, and optionally upload it.

    Orchestrates ports only. Manim, ffmpeg, and YouTube stay in adapters.
    """

    def __init__(
        self,
        renderer: VideoRendererPort,
        post_processor: PostProcessorPort,
        storage: StoragePort,
        uploader: UploaderPort,
    ) -> None:
        self._renderer = renderer
        self._post_processor = post_processor
        self._storage = storage
        self._uploader = uploader

    def execute(self, request: BuildRequest) -> BuildResult:
        raw = self._renderer.render(request.source)

        to_save = raw
        if request.post_process is not None and request.post_process.enabled:
            processed = request.output_dir / f".processed_{request.source.scene_name}.mp4"
            processed.parent.mkdir(parents=True, exist_ok=True)
            to_save = self._post_processor.apply(raw, request.post_process, processed)

        local_path = self._storage.save(to_save, request.output_dir, request.output_name)

        upload_id = None
        if request.publish is not None:
            upload_id = self._uploader.upload(local_path, request.publish)

        return BuildResult(local_path=local_path, upload_id=upload_id)
