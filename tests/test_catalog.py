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

    def test_each_scene_file_defines_the_class(self):
        for video in (*VIDEOS_101_125, *VIDEOS_126_137, *VIDEOS_138_149, *VIDEOS_150_161):
            path = ROOT / video.path
            self.assertTrue(path.is_file(), msg=video.path)
            text = path.read_text(encoding="utf-8")
            self.assertIn(f"class {video.scene}(", text)
            self.assertTrue("JapaneseScene" in text or "PacedScene" in text, msg=video.path)
            story = path.parent / "storyboard.md"
            self.assertTrue(story.is_file(), msg=str(story))


if __name__ == "__main__":
    unittest.main()
