import importlib.util
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

_spec = importlib.util.spec_from_file_location("math_catalog", ROOT / "project/math/catalog.py")
_catalog = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
sys.modules[_spec.name] = _catalog
_spec.loader.exec_module(_catalog)
VIDEOS_101_125 = _catalog.VIDEOS_101_125
VIDEOS_126_137 = _catalog.VIDEOS_126_137
VIDEOS_138_149 = _catalog.VIDEOS_138_149
VIDEOS_150_161 = _catalog.VIDEOS_150_161
VIDEOS_162_173 = _catalog.VIDEOS_162_173
VIDEOS_174_185 = _catalog.VIDEOS_174_185
VIDEOS_186_197 = _catalog.VIDEOS_186_197
VIDEOS_198_209 = _catalog.VIDEOS_198_209
VIDEOS_210_221 = _catalog.VIDEOS_210_221
VIDEOS_222_233 = _catalog.VIDEOS_222_233
VIDEOS_234_245 = _catalog.VIDEOS_234_245


class CatalogTests(unittest.TestCase):
    def test_numbers_are_101_to_125(self):
        nums = [v.number for v in VIDEOS_101_125]
        self.assertEqual(nums, list(range(101, 126)))

    def test_numbers_are_126_to_137(self):
        nums = [v.number for v in VIDEOS_126_137]
        self.assertEqual(nums, list(range(126, 138)))

    def test_numbers_are_138_to_149(self):
        nums = [v.number for v in VIDEOS_138_149]
        self.assertEqual(nums, list(range(138, 150)))

    def test_numbers_are_150_to_161(self):
        nums = [v.number for v in VIDEOS_150_161]
        self.assertEqual(nums, list(range(150, 162)))

    def test_numbers_are_162_to_173(self):
        nums = [v.number for v in VIDEOS_162_173]
        self.assertEqual(nums, list(range(162, 174)))

    def test_numbers_are_174_to_185(self):
        nums = [v.number for v in VIDEOS_174_185]
        self.assertEqual(nums, list(range(174, 186)))

    def test_numbers_are_186_to_197(self):
        nums = [v.number for v in VIDEOS_186_197]
        self.assertEqual(nums, list(range(186, 198)))

    def test_numbers_are_198_to_209(self):
        nums = [v.number for v in VIDEOS_198_209]
        self.assertEqual(nums, list(range(198, 210)))

    def test_numbers_are_210_to_221(self):
        nums = [v.number for v in VIDEOS_210_221]
        self.assertEqual(nums, list(range(210, 222)))

    def test_numbers_are_222_to_233(self):
        nums = [v.number for v in VIDEOS_222_233]
        self.assertEqual(nums, list(range(222, 234)))

    def test_numbers_are_234_to_245(self):
        nums = [v.number for v in VIDEOS_234_245]
        self.assertEqual(nums, list(range(234, 246)))

    def test_each_scene_file_defines_the_class(self):
        for video in (
            *VIDEOS_101_125,
            *VIDEOS_126_137,
            *VIDEOS_138_149,
            *VIDEOS_150_161,
            *VIDEOS_162_173,
            *VIDEOS_174_185,
            *VIDEOS_186_197,
            *VIDEOS_198_209,
            *VIDEOS_210_221,
            *VIDEOS_222_233,
            *VIDEOS_234_245,
        ):
            path = ROOT / video.path
            self.assertTrue(path.is_file(), msg=video.path)
            text = path.read_text(encoding="utf-8")
            self.assertIn(f"class {video.scene}(", text)
            self.assertTrue("JapaneseScene" in text or "PacedScene" in text, msg=video.path)
            story = path.parent / "storyboard.md"
            self.assertTrue(story.is_file(), msg=str(story))


if __name__ == "__main__":
    unittest.main()
