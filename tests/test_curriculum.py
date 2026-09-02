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
ALGO_003 = (
    ROOT
    / "project"
    / "curriculum_algorithm_200"
    / "D01_complexity"
    / "003_time_space_complexity"
)


class CurriculumLessonTests(unittest.TestCase):
    def test_lesson_scene_is_not_paced(self):
        self.assertEqual(LessonScene.motion_scale, 1.0)
        self.assertGreater(PacedScene.motion_scale, 1.0)
        self.assertTrue(issubclass(LessonScene, PacedScene.__bases__[0]))
        self.assertTrue(hasattr(LessonScene, "linger"))
        self.assertTrue(hasattr(LessonScene, "wipe"))
        self.assertTrue(hasattr(LessonScene, "below_chip"))
        self.assertTrue(hasattr(LessonScene, "step_label"))

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
        self.assertIn("self.below_chip(bad_a", scene)
        self.assertIn("self.below_chip(bad_b", scene)
        self.assertIn("self.below_chip(five", scene)

    def test_below_chip_keeps_long_line_on_screen(self):
        try:
            from manim import DOWN, LEFT, UP, config
            from manim_math.japanese import ja_text
        except ImportError:
            self.skipTest("manim is not installed")

        chip = ja_text("STEP 2  性質", font_size=24)
        chip.to_edge(UP, buff=1.02).to_edge(LEFT, buff=0.4)
        line = ja_text("悪い例 A   終わりの条件がない", font_size=28)
        frame_left = -config.frame_width / 2

        clipped = line.copy().next_to(chip, DOWN, buff=0.35)
        self.assertLess(
            clipped.get_left()[0],
            frame_left + 0.05,
            msg="sanity: next_to(DOWN) on a left chip must be the clipping case",
        )

        fixed = LessonScene.below_chip(line.copy(), chip, buff=0.35)
        self.assertGreaterEqual(fixed.get_left()[0], frame_left + 0.05)
        self.assertAlmostEqual(fixed.get_left()[0], chip.get_left()[0], places=5)

    def test_algo_003_has_storyboard_and_scene(self):
        story = (ALGO_003 / "storyboard.md").read_text(encoding="utf-8")
        scene = (ALGO_003 / "scene.py").read_text(encoding="utf-8")
        self.assertIn("フック", story)
        self.assertIn("今日のゴール", story)
        self.assertIn("全体像", story)
        self.assertIn("STEP 1", story)
        self.assertIn("STEP 2", story)
        self.assertIn("STEP 3", story)
        self.assertIn("STEP 4", story)
        self.assertIn("実例", story)
        self.assertIn("まとめ", story)
        self.assertIn("次回予告", story)
        self.assertIn("答えは同じなのに、メモリの使い方が全然違うことがある。", story)
        self.assertIn("追加メモリ", story)
        self.assertIn("#4 最良・最悪・平均計算量", story)
        self.assertIn("class TimeSpaceComplexity(LessonScene)", scene)
        self.assertNotIn("PacedScene", scene)
        self.assertIn("self.below_chip(", scene)
        self.assertIn("self.step_label(", scene)
        self.assertIn("self.aligned_table(", scene)
        self.assertIn("self.linger(3.", scene)
        self.assertIn("答えは同じなのに、メモリの使い方が全然違うことがある。", scene)
        self.assertIn("#4 最良・最悪・平均計算量", scene)

    def test_algo_001_mathtex_has_no_japanese(self):
        self._assert_no_japanese_in_mathtex(ALGO_001 / "scene.py")

    def test_algo_003_mathtex_has_no_japanese(self):
        self._assert_no_japanese_in_mathtex(ALGO_003 / "scene.py")

    def _assert_no_japanese_in_mathtex(self, path: Path):
        scene = path.read_text(encoding="utf-8")
        for kind in ("MathTex", "ja_tex"):
            for match in re.finditer(rf"{kind}\((.*?)\)", scene, flags=re.S):
                self.assertFalse(
                    re.search(r"[ぁ-んァ-ン一-龯]", match.group(1)),
                    msg=match.group(0)[:80],
                )


if __name__ == "__main__":
    unittest.main()
