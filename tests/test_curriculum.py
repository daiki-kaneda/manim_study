from pathlib import Path
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from manim_math.japanese import LessonScene, PacedScene


ALGO_001 = (
    ROOT
    / "project"
    / "curriculum_algorithm_200"
    / "D01_complexity"
    / "001_what_is_an_algorithm"
)


class CurriculumLessonTests(unittest.TestCase):
    def test_lesson_scene_is_not_paced(self):
        self.assertEqual(LessonScene.motion_scale, 1.0)
        self.assertGreater(PacedScene.motion_scale, 1.0)
        self.assertTrue(issubclass(LessonScene, PacedScene.__bases__[0]))

    def test_algo_001_has_storyboard_and_scene(self):
        story = (ALGO_001 / "storyboard.md").read_text(encoding="utf-8")
        scene = (ALGO_001 / "scene.py").read_text(encoding="utf-8")
        self.assertIn("フック", story)
        self.assertIn("今日のゴール", story)
        self.assertIn("全体像", story)
        self.assertIn("STEP 1", story)
        self.assertIn("実例", story)
        self.assertIn("まとめ", story)
        self.assertIn("次回予告", story)
        self.assertIn("class WhatIsAnAlgorithm(LessonScene)", scene)
        self.assertNotIn("PacedScene", scene)
        self.assertIn("7 は 3 より大きい", scene)
        self.assertIn("2 は 7 より小さい", scene)
        self.assertIn("9 は 7 より大きい", scene)
        self.assertIn("4 は 9 より小さい", scene)

    def test_algo_001_mathtex_has_no_japanese(self):
        scene = (ALGO_001 / "scene.py").read_text(encoding="utf-8")
        for kind in ("MathTex", "ja_tex"):
            for match in re.finditer(rf"{kind}\((.*?)\)", scene, flags=re.S):
                self.assertFalse(
                    re.search(r"[ぁ-んァ-ン一-龯]", match.group(1)),
                    msg=match.group(0)[:80],
                )


if __name__ == "__main__":
    unittest.main()
