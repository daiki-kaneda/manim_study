from __future__ import annotations

import unittest
from pathlib import Path

from video_pipeline.adapters.local_storage import LocalStorage
from video_pipeline.adapters.manim_renderer import ManimRenderer, find_rendered_video
from video_pipeline.application.ports.post_processor import PostProcessorPort
from video_pipeline.application.ports.renderer import VideoRendererPort
from video_pipeline.application.ports.uploader import UploaderPort
from video_pipeline.application.use_cases.build_video import BuildVideoUseCase
from video_pipeline.cli import request_from_args
from video_pipeline.domain.errors import RenderError, UploadError
from video_pipeline.domain.models import (
    BuildRequest,
    PostProcessOptions,
    PublishOptions,
    SceneSource,
)


class FakeRenderer(VideoRendererPort):
    def __init__(self, path: Path) -> None:
        self.path = path
        self.calls: list[SceneSource] = []

    def render(self, source: SceneSource) -> Path:
        self.calls.append(source)
        return self.path


class FakePost(PostProcessorPort):
    def __init__(self) -> None:
        self.calls: list[tuple[Path, PostProcessOptions, Path]] = []

    def apply(self, video: Path, options: PostProcessOptions, dest: Path) -> Path:
        self.calls.append((video, options, dest))
        dest.write_bytes(b"processed")
        return dest


class FakeUploader(UploaderPort):
    def __init__(self, upload_id: str = "yt_abc") -> None:
        self.upload_id = upload_id
        self.calls: list[tuple[Path, PublishOptions]] = []

    def upload(self, video: Path, options: PublishOptions) -> str:
        self.calls.append((video, options))
        return self.upload_id


class BuildVideoUseCaseTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(self._testMethodName + "_tmp")
        self.addCleanup(self._cleanup)
        self.tmp.mkdir(exist_ok=True)
        self.raw = self.tmp / "raw.mp4"
        self.raw.write_bytes(b"raw")
        self.renderer = FakeRenderer(self.raw)
        self.post = FakePost()
        self.uploader = FakeUploader()
        self.use_case = BuildVideoUseCase(
            self.renderer, self.post, LocalStorage(), self.uploader
        )

    def _cleanup(self) -> None:
        import shutil

        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_render_save_without_post_or_upload(self) -> None:
        out = self.tmp / "out"
        result = self.use_case.execute(
            BuildRequest(
                source=SceneSource(Path("scene.py"), "Demo"),
                output_dir=out,
            )
        )
        self.assertEqual(result.local_path, out / "Demo.mp4")
        self.assertTrue(result.local_path.is_file())
        self.assertEqual(result.local_path.read_bytes(), b"raw")
        self.assertIsNone(result.upload_id)
        self.assertEqual(self.post.calls, [])
        self.assertEqual(self.uploader.calls, [])

    def test_post_process_then_save(self) -> None:
        out = self.tmp / "out"
        result = self.use_case.execute(
            BuildRequest(
                source=SceneSource(Path("scene.py"), "Demo"),
                output_dir=out,
                post_process=PostProcessOptions(bgm=Path("bgm.mp3")),
            )
        )
        self.assertEqual(result.local_path.read_bytes(), b"processed")
        self.assertEqual(len(self.post.calls), 1)
        self.assertEqual(self.post.calls[0][0], self.raw)

    def test_upload_after_save(self) -> None:
        out = self.tmp / "out"
        result = self.use_case.execute(
            BuildRequest(
                source=SceneSource(Path("scene.py"), "Demo"),
                output_dir=out,
                filename="lesson.mp4",
                publish=PublishOptions(title="デモ", privacy="unlisted"),
            )
        )
        self.assertEqual(result.upload_id, "yt_abc")
        self.assertEqual(self.uploader.calls[0][0], out / "lesson.mp4")
        self.assertEqual(self.uploader.calls[0][1].title, "デモ")


class FindRenderedVideoTest(unittest.TestCase):
    def test_picks_newest(self) -> None:
        root = Path("find_rendered_tmp")
        self.addCleanup(lambda: __import__("shutil").rmtree(root, ignore_errors=True))
        older = root / "a" / "Demo.mp4"
        newer = root / "b" / "Demo.mp4"
        older.parent.mkdir(parents=True)
        newer.parent.mkdir(parents=True)
        older.write_bytes(b"old")
        newer.write_bytes(b"new")
        import os
        import time

        now = time.time()
        os.utime(older, (now - 10, now - 10))
        os.utime(newer, (now, now))
        self.assertEqual(find_rendered_video(root, "Demo"), newer)

    def test_missing(self) -> None:
        root = Path("find_rendered_empty")
        self.addCleanup(lambda: __import__("shutil").rmtree(root, ignore_errors=True))
        root.mkdir(exist_ok=True)
        with self.assertRaises(RenderError):
            find_rendered_video(root, "Missing")


class CliRequestTest(unittest.TestCase):
    def test_upload_and_post_flags(self) -> None:
        import argparse

        args = argparse.Namespace(
            scene="project/math/x/scene.py",
            name="TriangleArea",
            output_dir="out/videos",
            filename=None,
            quality="h",
            bg="/tmp/bg.png",
            bgm=None,
            volume=0.2,
            fade=1.5,
            mode="screen",
            upload=True,
            title="面積",
            description="説明",
            privacy="private",
        )
        req = request_from_args(args)
        self.assertEqual(req.source.scene_name, "TriangleArea")
        self.assertEqual(req.source.quality, "h")
        self.assertTrue(req.post_process and req.post_process.enabled)
        self.assertEqual(req.post_process.background, Path("/tmp/bg.png"))
        self.assertIsNotNone(req.publish)
        self.assertEqual(req.publish.title, "面積")
        self.assertEqual(req.output_name, "TriangleArea.mp4")


class ManimRendererGuardTest(unittest.TestCase):
    def test_bad_quality(self) -> None:
        renderer = ManimRenderer(Path("."))
        with self.assertRaises(RenderError):
            renderer.render(SceneSource(Path("nope.py"), "X", quality="z"))


class YouTubeUploaderGuardTest(unittest.TestCase):
    def test_missing_file(self) -> None:
        from video_pipeline.adapters.youtube_uploader import YouTubeUploader

        up = YouTubeUploader(token_path=Path("/no/such/token.json"))
        with self.assertRaises(UploadError):
            up.upload(Path("/no/video.mp4"), PublishOptions(title="x"))


if __name__ == "__main__":
    unittest.main()
