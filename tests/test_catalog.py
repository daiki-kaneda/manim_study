import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

_spec = importlib.util.spec_from_file_location("math_catalog", ROOT / "project/math/catalog.py")
_catalog = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_catalog)
VIDEOS_101_125 = _catalog.VIDEOS_101_125


class CatalogTests(unittest.TestCase):
    def test_numbers_are_101_to_125(self):
        nums = [v.number for v in VIDEOS_101_125]
        self.assertEqual(nums, list(range(101, 126)))

    def test_each_scene_file_defines_the_class(self):
        for video in VIDEOS_101_125:
            path = ROOT / video.path
            self.assertTrue(path.is_file(), msg=video.path)
            text = path.read_text(encoding="utf-8")
            self.assertIn(f"class {video.scene}(", text)
            self.assertIn("JapaneseScene", text)
            story = path.parent / "storyboard.md"
            self.assertTrue(story.is_file(), msg=str(story))


if __name__ == "__main__":
    unittest.main()
