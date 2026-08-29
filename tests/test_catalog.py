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
VIDEOS_246_257 = _catalog.VIDEOS_246_257
VIDEOS_258_269 = _catalog.VIDEOS_258_269
VIDEOS_270_281 = _catalog.VIDEOS_270_281
VIDEOS_282_293 = _catalog.VIDEOS_282_293
VIDEOS_294_305 = _catalog.VIDEOS_294_305
VIDEOS_306_317 = _catalog.VIDEOS_306_317
VIDEOS_318_329 = _catalog.VIDEOS_318_329
VIDEOS_330_341 = _catalog.VIDEOS_330_341
VIDEOS_342_353 = _catalog.VIDEOS_342_353
VIDEOS_354_365 = _catalog.VIDEOS_354_365
VIDEOS_366_377 = _catalog.VIDEOS_366_377
VIDEOS_378_389 = _catalog.VIDEOS_378_389
VIDEOS_390_401 = _catalog.VIDEOS_390_401
VIDEOS_402_413 = _catalog.VIDEOS_402_413


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

    def test_numbers_are_246_to_257(self):
        nums = [v.number for v in VIDEOS_246_257]
        self.assertEqual(nums, list(range(246, 258)))

    def test_numbers_are_258_to_269(self):
        nums = [v.number for v in VIDEOS_258_269]
        self.assertEqual(nums, list(range(258, 270)))

    def test_numbers_are_270_to_281(self):
        nums = [v.number for v in VIDEOS_270_281]
        self.assertEqual(nums, list(range(270, 282)))

    def test_numbers_are_282_to_293(self):
        nums = [v.number for v in VIDEOS_282_293]
        self.assertEqual(nums, list(range(282, 294)))

    def test_numbers_are_294_to_305(self):
        nums = [v.number for v in VIDEOS_294_305]
        self.assertEqual(nums, list(range(294, 306)))

    def test_numbers_are_306_to_317(self):
        nums = [v.number for v in VIDEOS_306_317]
        self.assertEqual(nums, list(range(306, 318)))

    def test_numbers_are_318_to_329(self):
        nums = [v.number for v in VIDEOS_318_329]
        self.assertEqual(nums, list(range(318, 330)))

    def test_numbers_are_330_to_341(self):
        nums = [v.number for v in VIDEOS_330_341]
        self.assertEqual(nums, list(range(330, 342)))

    def test_numbers_are_342_to_353(self):
        nums = [v.number for v in VIDEOS_342_353]
        self.assertEqual(nums, list(range(342, 354)))

    def test_numbers_are_354_to_365(self):
        nums = [v.number for v in VIDEOS_354_365]
        self.assertEqual(nums, list(range(354, 366)))

    def test_numbers_are_366_to_377(self):
        nums = [v.number for v in VIDEOS_366_377]
        self.assertEqual(nums, list(range(366, 378)))

    def test_numbers_are_378_to_389(self):
        nums = [v.number for v in VIDEOS_378_389]
        self.assertEqual(nums, list(range(378, 390)))

    def test_numbers_are_390_to_401(self):
        nums = [v.number for v in VIDEOS_390_401]
        self.assertEqual(nums, list(range(390, 402)))

    def test_numbers_are_402_to_413(self):
        nums = [v.number for v in VIDEOS_402_413]
        self.assertEqual(nums, list(range(402, 414)))

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
            *VIDEOS_246_257,
            *VIDEOS_258_269,
            *VIDEOS_270_281,
            *VIDEOS_282_293,
            *VIDEOS_294_305,
            *VIDEOS_306_317,
            *VIDEOS_318_329,
            *VIDEOS_330_341,
            *VIDEOS_342_353,
            *VIDEOS_354_365,
            *VIDEOS_366_377,
            *VIDEOS_378_389,
            *VIDEOS_390_401,
            *VIDEOS_402_413,
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
