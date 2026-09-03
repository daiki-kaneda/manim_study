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
ALGO_D01 = ROOT / "project" / "curriculum_algorithm_200" / "D01_complexity"
ALGO_004 = ALGO_D01 / "004_best_worst_average"
ALGO_005 = ALGO_D01 / "005_omega_theta"
ALGO_006 = ALGO_D01 / "006_recursion_complexity"
ALGO_007 = ALGO_D01 / "007_recursion_tree"
MATH_150_001 = (
    ROOT / "project" / "curriculum_math_150" / "001_repeating_nines"
)
MATH_150_002 = ROOT / "project" / "curriculum_math_150" / "002_circle_area"
MATH_150_003 = ROOT / "project" / "curriculum_math_150" / "003_fixed_perimeter_rectangle"
MATH_150_004 = ROOT / "project" / "curriculum_math_150" / "004_reflection_shortest_path"


class CurriculumLessonTests(unittest.TestCase):
    def test_lesson_scene_is_not_paced(self):
        self.assertEqual(LessonScene.motion_scale, 1.0)
        self.assertGreater(PacedScene.motion_scale, 1.0)
        self.assertTrue(issubclass(LessonScene, PacedScene.__bases__[0]))
        self.assertTrue(hasattr(LessonScene, "linger"))
        self.assertTrue(hasattr(LessonScene, "wipe"))
        self.assertTrue(hasattr(LessonScene, "below_chip"))
        self.assertTrue(hasattr(LessonScene, "step_label"))
        self.assertTrue(hasattr(LessonScene, "stack_below"))

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

    def test_algo_004_to_007_have_storyboard_and_scene(self):
        specs = [
            (
                ALGO_004,
                "BestWorstAverage",
                "同じ手順でも、入力によって回数が全然違うことがある。",
                "#5 漸近記法",
            ),
            (
                ALGO_005,
                "OmegaTheta",
                "O と書くと上から抑えているだけなので、ゆるいことがある。",
                "#6 再帰と計算量の関係",
            ),
            (
                ALGO_006,
                "RecursionComplexity",
                "答えは同じなのに、呼び出しの積み方が違うことがある。",
                "#7 再帰木による計算量の見積もり",
            ),
            (
                ALGO_007,
                "RecursionTree",
                "一度に2つ呼び出すと、一本道ではなく、枝が分かれる。",
                "#8 マスター定理",
            ),
        ]
        for folder, cls, hook, nxt in specs:
            with self.subTest(folder=folder.name):
                story = (folder / "storyboard.md").read_text(encoding="utf-8")
                scene = (folder / "scene.py").read_text(encoding="utf-8")
                for part in ("フック", "今回のゴール", "全体像", "STEP 1", "実例", "まとめ", "次回予告"):
                    self.assertIn(part, story)
                self.assertNotIn("今日のゴール", story)
                self.assertNotIn("今日", scene)
                self.assertIn(hook, story)
                self.assertIn(hook, scene)
                self.assertIn(nxt, scene)
                self.assertIn(f"class {cls}(CurriculumScene)", scene)
                self.assertNotIn("PacedScene", scene)
                self.assertIn("self.stack_below(", scene)
                self.assertIn("self.below_chip(", scene)
                self.assertIn("self.linger(3.", scene)
                self._assert_no_japanese_in_mathtex(folder / "scene.py")
                self._assert_no_hardcoded_exponents_in_japanese(folder / "scene.py")

    def test_stack_below_keeps_long_line_on_screen(self):
        try:
            from manim import DOWN, LEFT, UP, config
            from manim_math.japanese import ja_text
        except ImportError:
            self.skipTest("manim is not installed")

        prev = ja_text("目標", font_size=24)
        prev.to_edge(UP, buff=1.4).to_edge(LEFT, buff=0.4)
        line = ja_text("T(4)=T(3)+1=T(2)+2=T(1)+3=4=n の長い式", font_size=28)
        frame_left = -config.frame_width / 2

        clipped = line.copy().next_to(prev, DOWN, buff=0.22)
        self.assertLess(
            clipped.get_left()[0],
            frame_left + 0.05,
            msg="sanity: next_to(DOWN) on a short prev must be the clipping case",
        )

        fixed = LessonScene.stack_below(line.copy(), prev, buff=0.22)
        self.assertGreaterEqual(fixed.get_left()[0], frame_left + 0.05)
        self.assertAlmostEqual(fixed.get_left()[0], prev.get_left()[0], places=5)

    def test_math_150_001_has_storyboard_and_scene(self):
        story = (MATH_150_001 / "storyboard.md").read_text(encoding="utf-8")
        scene = (MATH_150_001 / "scene.py").read_text(encoding="utf-8")
        for part in ("問い", "試行", "工夫", "一般化", "まとめ"):
            self.assertIn(part, story)
        self.assertIn("STEP 1", story)
        self.assertIn("STEP 2", story)
        self.assertIn("STEP 3", story)
        self.assertIn("STEP 4", story)
        self.assertIn("実例", story)
        self.assertNotIn("今日のゴール", story)
        self.assertNotIn("今日", scene)
        self.assertIn("class RepeatingNines(LessonScene)", scene)
        self.assertNotIn("PacedScene", scene)
        self.assertIn("self.below_chip(", scene)
        self.assertIn("self.stack_below(", scene)
        self.assertIn("self.aligned_table(", scene)
        self.assertIn("self.linger(3.", scene)
        self.assertIn(r"1-a_n=10^{-n}", scene)
        self.assertIn(r"10x-x=9.999\ldots-0.999\ldots", scene)
        self.assertIn(r"\dfrac{9}{10}\times\dfrac{10}{9}=1", scene)
        self._assert_no_japanese_in_mathtex(MATH_150_001 / "scene.py")
        self._assert_no_hardcoded_exponents_in_japanese(MATH_150_001 / "scene.py")

    def test_math_150_002_has_storyboard_and_scene(self):
        story = (MATH_150_002 / "storyboard.md").read_text(encoding="utf-8")
        scene = (MATH_150_002 / "scene.py").read_text(encoding="utf-8")
        for part in ("問い", "試行", "工夫", "一般化", "まとめ"):
            self.assertIn(part, story)
        self.assertIn("STEP 1", story)
        self.assertIn("STEP 2", story)
        self.assertIn("STEP 3", story)
        self.assertIn("STEP 4", story)
        self.assertIn("実例", story)
        self.assertNotIn("今日のゴール", story)
        self.assertNotIn("今日", scene)
        self.assertIn("class CircleArea(LessonScene)", scene)
        self.assertNotIn("PacedScene", scene)
        self.assertIn("self.below_chip(", scene)
        self.assertIn("self.stack_below(", scene)
        self.assertIn("self.aligned_table(", scene)
        self.assertIn("self.linger(3.", scene)
        self.assertIn(r"\pi=\dfrac{C}{2r}", scene)
        self.assertIn(r"(\pi r)\cdot r=\pi r^2", scene)
        self.assertIn(r"S=\dfrac{1}{2}r\cdot 2\pi r", scene)
        self.assertNotIn(r"2\pi r\cdot r=\pi r^2", scene)
        self._assert_no_japanese_in_mathtex(MATH_150_002 / "scene.py")
        self._assert_no_hardcoded_exponents_in_japanese(MATH_150_002 / "scene.py")

    def test_math_150_003_has_storyboard_and_scene(self):
        story = (MATH_150_003 / "storyboard.md").read_text(encoding="utf-8")
        scene = (MATH_150_003 / "scene.py").read_text(encoding="utf-8")
        for part in ("問い", "試行", "工夫", "一般化", "まとめ"):
            self.assertIn(part, story)
        self.assertIn("STEP 1", story)
        self.assertIn("STEP 2", story)
        self.assertIn("STEP 3", story)
        self.assertIn("STEP 4", story)
        self.assertIn("実例", story)
        self.assertNotIn("今日のゴール", story)
        self.assertNotIn("今日", scene)
        self.assertIn("class FixedPerimeterRectangle(LessonScene)", scene)
        self.assertNotIn("PacedScene", scene)
        self.assertIn("self.below_chip(", scene)
        self.assertIn("self.stack_below(", scene)
        self.assertIn("self.aligned_table(", scene)
        self.assertIn("self.linger(3.", scene)
        self.assertIn(r"S=xy=x(s-x)", scene)
        self.assertIn(r"S=\dfrac{s^2}{4}-(x-s/2)^2", scene)
        self.assertIn(r"25-24.75=0.25=(4.5-5)^2", scene)
        self.assertIn(r"\dfrac{x+y}{2}\ge\sqrt{xy}", scene)
        self._assert_no_japanese_in_mathtex(MATH_150_003 / "scene.py")
        self._assert_no_hardcoded_exponents_in_japanese(MATH_150_003 / "scene.py")

    def test_math_150_004_has_storyboard_and_scene(self):
        story = (MATH_150_004 / "storyboard.md").read_text(encoding="utf-8")
        scene = (MATH_150_004 / "scene.py").read_text(encoding="utf-8")
        for part in ("問い", "試行", "工夫", "一般化", "まとめ"):
            self.assertIn(part, story)
        self.assertIn("STEP 1", story)
        self.assertIn("STEP 2", story)
        self.assertIn("STEP 3", story)
        self.assertIn("STEP 4", story)
        self.assertIn("実例", story)
        self.assertNotIn("今日のゴール", story)
        self.assertNotIn("今日", scene)
        self.assertIn("class ReflectionShortestPath(LessonScene)", scene)
        self.assertNotIn("PacedScene", scene)
        self.assertIn("self.below_chip(", scene)
        self.assertIn("self.stack_below(", scene)
        self.assertIn("self.aligned_table(", scene)
        self.assertIn("self.linger(3.", scene)
        self.assertIn(r"BP=B'P", scene)
        self.assertIn(r"AP+PB'\ge AB'", scene)
        self.assertIn(r"6\sqrt{2}+2\sqrt{2}=8\sqrt{2}\approx 11.314", scene)
        self._assert_no_japanese_in_mathtex(MATH_150_004 / "scene.py")
        self._assert_no_hardcoded_exponents_in_japanese(MATH_150_004 / "scene.py")

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

    def _assert_no_hardcoded_exponents_in_japanese(self, path: Path):
        scene = path.read_text(encoding="utf-8")
        stripped = re.sub(
            r"(?:MathTex|ja_tex)\((?:[^()]|\([^()]*\))*\)",
            "",
            scene,
            flags=re.S,
        )
        match = re.search(
            r"n\^\{2\}|n\^2|2\^n|2\^\{n\}|log_\{2\}|O\(n\^",
            stripped,
        )
        self.assertIsNone(
            match,
            msg=f"{path.name}: hardcoded math in Japanese text: {match.group(0) if match else ''}",
        )


if __name__ == "__main__":
    unittest.main()
