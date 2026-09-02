from __future__ import annotations

import unittest
from pathlib import Path
from unittest.mock import patch

from video_pipeline.adapters.ffmpeg_post_processor import FfmpegPostProcessor
from video_pipeline.domain.errors import PostProcessError
from video_pipeline.domain.models import PostProcessOptions


class FfmpegPostProcessorTest(unittest.TestCase):
    def test_builds_script_args(self) -> None:
        tmp = Path("ffmpeg_adapter_tmp")
        self.addCleanup(lambda: __import__("shutil").rmtree(tmp, ignore_errors=True))
        tmp.mkdir()
        script = tmp / "add_bg_bgm.sh"
        script.write_text("#!/bin/sh\n", encoding="utf-8")
        video = tmp / "in.mp4"
        video.write_bytes(b"v")
        dest = tmp / "out.mp4"
        options = PostProcessOptions(background=Path("bg.png"), bgm=Path("a.mp3"), volume=0.3)

        class _Done:
            returncode = 0
            stdout = ""
            stderr = ""

        def fake_run(cmd, **_kwargs):
            dest.write_bytes(b"mux")
            self.cmd = cmd
            return _Done()

        with patch("video_pipeline.adapters.ffmpeg_post_processor.subprocess.run", fake_run):
            out = FfmpegPostProcessor(script).apply(video, options, dest)

        self.assertEqual(out, dest)
        self.assertIn("--bg", self.cmd)
        self.assertIn("--bgm", self.cmd)
        self.assertIn("0.3", self.cmd)

    def test_rejects_empty_options(self) -> None:
        with self.assertRaises(PostProcessError):
            FfmpegPostProcessor(Path("missing.sh")).apply(
                Path("in.mp4"), PostProcessOptions(), Path("out.mp4")
            )


if __name__ == "__main__":
    unittest.main()
