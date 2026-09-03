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
MATH_150_005 = ROOT / "project" / "curriculum_math_150" / "005_ant_on_cube"
MATH_150_006 = ROOT / "project" / "curriculum_math_150" / "006_picks_theorem"
MATH_150_007 = ROOT / "project" / "curriculum_math_150" / "007_regions_from_lines"
MATH_150_008 = ROOT / "project" / "curriculum_math_150" / "008_pigeonhole"
MATH_150_009 = ROOT / "project" / "curriculum_math_150" / "009_birthday_paradox"
MATH_150_010 = ROOT / "project" / "curriculum_math_150" / "010_monty_hall"
MATH_150_011 = ROOT / "project" / "curriculum_math_150" / "011_false_positive_bayes"
MATH_150_012 = ROOT / "project" / "curriculum_math_150" / "012_central_limit_dice"
MATH_150_013 = ROOT / "project" / "curriculum_math_150" / "013_law_of_large_numbers"
MATH_150_014 = ROOT / "project" / "curriculum_math_150" / "014_buffons_needle"
MATH_150_015 = ROOT / "project" / "curriculum_math_150" / "015_random_walk_return"


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
        self.assertTrue(hasattr(LessonScene, "begin_step"))
        self.assertTrue(hasattr(LessonScene, "pause_new_screen"))
        self.assertTrue(hasattr(LessonScene, "pause_short_formula"))
        self.assertTrue(hasattr(LessonScene, "pause_rewrite"))
        self.assertTrue(hasattr(LessonScene, "pause_complex"))
        self.assertTrue(hasattr(LessonScene, "pause_conclusion"))
        self.assertTrue(hasattr(LessonScene, "pause_topic"))
        self.assertGreaterEqual(LessonScene.PAUSE_NEW_SCREEN, 0.5)
        self.assertLessEqual(LessonScene.PAUSE_NEW_SCREEN, 1.0)
        self.assertGreaterEqual(LessonScene.PAUSE_SHORT_FORMULA, 1.0)
        self.assertLessEqual(LessonScene.PAUSE_SHORT_FORMULA, 2.0)
        self.assertGreaterEqual(LessonScene.PAUSE_REWRITE, 0.5)
        self.assertLessEqual(LessonScene.PAUSE_REWRITE, 1.0)
        self.assertGreaterEqual(LessonScene.PAUSE_COMPLEX, 2.0)
        self.assertLessEqual(LessonScene.PAUSE_COMPLEX, 3.0)
        self.assertGreaterEqual(LessonScene.PAUSE_CONCLUSION, 2.0)
        self.assertLessEqual(LessonScene.PAUSE_CONCLUSION, 3.0)
        self.assertGreaterEqual(LessonScene.PAUSE_TOPIC, 0.5)
        self.assertLessEqual(LessonScene.PAUSE_TOPIC, 1.0)

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

    def test_math_150_005_has_storyboard_and_scene(self):
        story = (MATH_150_005 / "storyboard.md").read_text(encoding="utf-8")
        scene = (MATH_150_005 / "scene.py").read_text(encoding="utf-8")
        for part in ("問い", "試行", "工夫", "一般化", "まとめ"):
            self.assertIn(part, story)
        self.assertIn("STEP 1", story)
        self.assertIn("STEP 2", story)
        self.assertIn("STEP 3", story)
        self.assertIn("STEP 4", story)
        self.assertIn("実例", story)
        self.assertNotIn("今日のゴール", story)
        self.assertNotIn("今日", scene)
        self.assertIn("class AntOnCube(LessonScene)", scene)
        self.assertNotIn("PacedScene", scene)
        self.assertIn("self.below_chip(", scene)
        self.assertIn("self.stack_below(", scene)
        self.assertIn("self.aligned_table(", scene)
        self.assertIn("self.linger(3.", scene)
        self.assertIn(r"\sqrt{1^2+2^2}=\sqrt{5}", scene)
        self.assertIn(r"ST=\sqrt{1^2+2^2}=\sqrt{5}", scene)
        self.assertIn(r"s\sqrt{5}", scene)
        self._assert_no_japanese_in_mathtex(MATH_150_005 / "scene.py")
        self._assert_no_hardcoded_exponents_in_japanese(MATH_150_005 / "scene.py")

    def test_math_150_006_has_storyboard_and_scene(self):
        story = (MATH_150_006 / "storyboard.md").read_text(encoding="utf-8")
        scene = (MATH_150_006 / "scene.py").read_text(encoding="utf-8")
        for part in ("問い", "試行", "工夫", "一般化", "まとめ"):
            self.assertIn(part, story)
        self.assertIn("STEP 1", story)
        self.assertIn("STEP 2", story)
        self.assertIn("STEP 3", story)
        self.assertIn("STEP 4", story)
        self.assertIn("実例", story)
        self.assertNotIn("今日のゴール", story)
        self.assertNotIn("今日", scene)
        self.assertIn("class PicksTheorem(LessonScene)", scene)
        self.assertNotIn("PacedScene", scene)
        self.assertIn("self.below_chip(", scene)
        self.assertIn("self.stack_below(", scene)
        self.assertIn("self.aligned_table(", scene)
        self.assertIn("self.linger(3.", scene)
        self.assertIn(r"I+\dfrac{B}{2}-1", scene)
        self.assertIn(r"S=I+\dfrac{B}{2}-1", scene)
        self.assertIn(r"T=2I+B-2", scene)
        self.assertIn(r"6+5-1=10", scene)
        self.assertIn(r"V-E+F=1", scene)
        self.assertIn(r"V=I+B", scene)
        self.assertIn("とおく", scene)
        self.assertIn("方法", scene)
        self.assertNotIn("道", scene)
        step1 = scene[
            scene.index("def part_step1_primitive") : scene.index("def part_step2_splits")
        ]
        self.assertNotIn(r"I+\dfrac{B}{2}-1", step1)
        self.assertNotIn(r"T=2I+B-2", step1)
        self.assertIn("とおく", step1)
        self.assertIn(r"12-\dfrac{9}{2}", scene)
        self.assertIn(r"\dfrac{24}{2}-\dfrac{9}{2}=\dfrac{15}{2}", scene)
        self.assertNotIn(r"\dfrac{21}{2}", scene)
        self.assertIn("細長", scene)
        self.assertIn(r"3(2-1)+0(1-0)+1(0-2)", scene)
        self.assertIn(r"x_1(y_2-y_3)", scene)
        self.assertNotIn("多くの多角形", scene)
        self.assertNotIn("多くの多角形", story)
        self.assertIn("辺が交わらず穴もない", scene)
        self._assert_no_japanese_in_mathtex(MATH_150_006 / "scene.py")
        self._assert_no_hardcoded_exponents_in_japanese(MATH_150_006 / "scene.py")

    def test_math_150_007_has_storyboard_and_scene(self):
        story = (MATH_150_007 / "storyboard.md").read_text(encoding="utf-8")
        scene = (MATH_150_007 / "scene.py").read_text(encoding="utf-8")
        for part in ("問い", "試行", "工夫", "一般化", "まとめ"):
            self.assertIn(part, story)
        self.assertIn("STEP 1", story)
        self.assertIn("STEP 2", story)
        self.assertIn("STEP 3", story)
        self.assertIn("STEP 4", story)
        self.assertIn("実例", story)
        self.assertNotIn("今日のゴール", story)
        self.assertNotIn("今日", scene)
        self.assertIn("class RegionsFromLines(LessonScene)", scene)
        self.assertNotIn("PacedScene", scene)
        self.assertIn("self.below_chip(", scene)
        self.assertIn("self.stack_below(", scene)
        self.assertIn("self.aligned_table(", scene)
        self.assertIn("self.linger(3.", scene)
        self.assertIn("とおく", scene)
        self.assertIn("方法", scene)
        self.assertNotIn("道", scene)
        self.assertIn(r"R(n)=R(n-1)+n", scene)
        self.assertIn(r"R(n)=1+\dfrac{n(n+1)}{2}", scene)
        self.assertIn(r"1+\dfrac{4\cdot 5}{2}=1+10=11", scene)
        self.assertIn(r"R(k)+(k+1)=1+\dfrac{k(k+1)}{2}+(k+1)", scene)
        self.assertIn("帰納法", scene)
        step1 = scene[
            scene.index("def part_step1_count") : scene.index("def part_step2_maximize")
        ]
        self.assertNotIn(r"R(n)=1+\dfrac{n(n+1)}{2}", step1)
        self._assert_no_japanese_in_mathtex(MATH_150_007 / "scene.py")
        self._assert_no_hardcoded_exponents_in_japanese(MATH_150_007 / "scene.py")

    def test_math_150_008_has_storyboard_and_scene(self):
        story = (MATH_150_008 / "storyboard.md").read_text(encoding="utf-8")
        scene = (MATH_150_008 / "scene.py").read_text(encoding="utf-8")
        for part in ("問い", "試行", "工夫", "一般化", "まとめ"):
            self.assertIn(part, story)
        self.assertIn("STEP 1", story)
        self.assertIn("STEP 2", story)
        self.assertIn("STEP 3", story)
        self.assertIn("STEP 4", story)
        self.assertIn("実例", story)
        self.assertNotIn("今日のゴール", story)
        self.assertNotIn("今日", scene)
        self.assertIn("class Pigeonhole(LessonScene)", scene)
        self.assertNotIn("PacedScene", scene)
        self.assertIn("self.below_chip(", scene)
        self.assertIn("self.stack_below(", scene)
        self.assertIn("self.aligned_table(", scene)
        self.assertIn("self.linger(3.", scene)
        self.assertIn("とおく", scene)
        self.assertIn("方法", scene)
        self.assertNotIn("道", scene)
        self.assertNotIn("確率", scene)
        self.assertNotIn("割合", scene)
        self.assertNotIn("出やすい", scene)
        self.assertNotIn("あれは", scene)
        self.assertIn("鳩の巣", scene)
        self.assertIn(r"366", scene)
        self.assertIn(r"367", scene)
        self.assertIn(r"m=n+1", scene)
        self.assertIn(r"12+1=13", scene)
        self.assertIn(r"12\times 2=24", scene)
        self.assertIn(r"24+1=25", scene)
        self.assertIn(r"n(r-1)+1", scene)
        self.assertIn(r"3\cdot 1+1=4", scene)
        self.assertIn(r"3\cdot(3-1)+1=6+1=7", scene)
        self.assertIn(r"\left\lceil\dfrac{n+1}{n}\right\rceil=2", scene)
        self.assertIn(r"\left\lceil\dfrac{13}{12}\right\rceil=2", scene)
        step1 = scene[
            scene.index("def part_step1_boxes") : scene.index("def part_step2_worst")
        ]
        self.assertNotIn(r"m=n+1", step1)
        self.assertNotIn(r"n(r-1)+1", step1)
        example = scene[
            scene.index("def part_example") : scene.index("def part_generalize")
        ]
        self.assertNotIn("move_to(caption)", example)
        self.assertNotIn("Transform(caption", example)
        self.assertIn("stack_below(new_cap, nxt", example)
        self._assert_no_japanese_in_mathtex(MATH_150_008 / "scene.py")
        self._assert_no_hardcoded_exponents_in_japanese(MATH_150_008 / "scene.py")

    def test_math_150_009_has_storyboard_and_scene(self):
        story = (MATH_150_009 / "storyboard.md").read_text(encoding="utf-8")
        scene = (MATH_150_009 / "scene.py").read_text(encoding="utf-8")
        for part in ("問い", "試行", "工夫", "一般化", "まとめ"):
            self.assertIn(part, story)
        self.assertIn("STEP 1", story)
        self.assertIn("STEP 2", story)
        self.assertIn("STEP 3", story)
        self.assertIn("STEP 4", story)
        self.assertIn("実例", story)
        self.assertNotIn("今日のゴール", story)
        self.assertNotIn("今日", scene)
        self.assertIn("class BirthdayParadox(LessonScene)", scene)
        self.assertNotIn("PacedScene", scene)
        self.assertIn("self.below_chip(", scene)
        self.assertIn("self.stack_below(", scene)
        self.assertIn("self.aligned_table(", scene)
        self.assertIn("self.begin_step(", scene)
        self.assertIn("pause_conclusion", scene)
        self.assertIn("何人集まったとき", scene)
        self.assertIn("衝突する 2 人が生まれる", scene)
        self.assertIn("とおく", scene)
        self.assertIn("方法", scene)
        self.assertNotIn("道", scene)
        self.assertNotIn("あれは", scene)
        self.assertIn(r"\dfrac{365}{2}=182.5", scene)
        self.assertIn(r"\dfrac{6\cdot 5}{2}=15", scene)
        self.assertIn(r"\dfrac{33306}{2}=16653", scene)
        self.assertIn(r"\dfrac{5040}{10000}=0.504", scene)
        self.assertIn(r"0.504\times\dfrac{6}{10}=0.3024", scene)
        self.assertIn(r"\left(1-\dfrac{1}{m}\right)^{m}\approx\dfrac{1}{e}", scene)
        self.assertIn(r"1-x\approx e^{-x}", scene)
        self.assertIn(r"1+2+\cdots+(n-1)=\dfrac{(n-1)n}{2}", scene)
        self.assertIn(r"P(A)\approx 1-e^{-n(n-1)/(2d)}", scene)
        self.assertIn(r"n(n-1)=2d\ln 2", scene)
        self.assertIn(r"n\approx\sqrt{2d\ln 2}", scene)
        self.assertIn(r"22^{2}=484", scene)
        self.assertIn(r"22.5^{2}=506.25", scene)
        self.assertIn(r"22\cdot 21=462", scene)
        self.assertIn(r"23\cdot 22=506", scene)
        self.assertIn(r"1-e^{-462/730}\approx 0.469", scene)
        self.assertIn(r"1-e^{-506/730}\approx 0.500", scene)
        self.assertIn(r"10000", scene)
        self.assertIn(r"120", scene)
        step1 = scene[
            scene.index("def part_step1_complement") : scene.index("def part_step2_product")
        ]
        self.assertNotIn(r"n\approx\sqrt{2d\ln 2}", step1)
        self.assertNotIn("23 人", step1)
        self._assert_no_japanese_in_mathtex(MATH_150_009 / "scene.py")
        self._assert_no_hardcoded_exponents_in_japanese(MATH_150_009 / "scene.py")

    def test_math_150_010_has_storyboard_and_scene(self):
        story = (MATH_150_010 / "storyboard.md").read_text(encoding="utf-8")
        scene = (MATH_150_010 / "scene.py").read_text(encoding="utf-8")
        for part in ("問い", "試行", "工夫", "一般化", "まとめ"):
            self.assertIn(part, story)
        self.assertIn("STEP 1", story)
        self.assertIn("STEP 2", story)
        self.assertIn("STEP 3", story)
        self.assertIn("STEP 4", story)
        self.assertIn("実例", story)
        self.assertNotIn("今日のゴール", story)
        self.assertNotIn("今日", scene)
        self.assertIn("class MontyHall(LessonScene)", scene)
        self.assertNotIn("PacedScene", scene)
        self.assertIn("self.below_chip(", scene)
        self.assertIn("self.stack_below(", scene)
        self.assertIn("self.aligned_table(", scene)
        self.assertIn("self.begin_step(", scene)
        self.assertIn("pause_conclusion", scene)
        self.assertIn("とおく", scene)
        self.assertIn("方法", scene)
        self.assertNotIn("道", scene)
        self.assertNotIn("あれは", scene)
        self.assertIn(r"\dfrac{1}{2}", scene)
        self.assertIn(r"\dfrac{1}{3}", scene)
        self.assertIn(r"1-\dfrac{1}{3}=\dfrac{2}{3}", scene)
        self.assertIn(r"\dfrac{1}{3}+\dfrac{2}{3}=\dfrac{3}{3}=1", scene)
        self.assertIn(r"\dfrac{1}{3}+\dfrac{1}{3}=\dfrac{2}{3}", scene)
        self.assertIn(r"\dfrac{99}{100}", scene)
        self.assertIn(r"100", scene)
        self.assertIn(r"98", scene)
        self.assertIn("モンティ・ホール", scene)
        self.assertNotIn("P(A", scene)
        self.assertNotIn(r"P(A\mid", scene)
        step1 = scene[
            scene.index("def part_step1_rules") : scene.index("def part_step2_first_hit")
        ]
        self.assertNotIn(r"\dfrac{2}{3}", step1)
        example = scene[
            scene.index("def part_example") : scene.index("def part_generalize")
        ]
        self.assertNotIn("move_to(caption)", example)
        self.assertNotIn("Transform(caption", example)
        step3 = scene[
            scene.index("def part_step3_first_miss") : scene.index("def part_step4_combine")
        ]
        self.assertIn("new_restate", step3)
        self.assertIn("番号を扉の上", story)
        self.assertIn("numbers_above", scene)
        self._assert_no_japanese_in_mathtex(MATH_150_010 / "scene.py")
        self._assert_no_hardcoded_exponents_in_japanese(MATH_150_010 / "scene.py")

    def _assert_math_150_common(self, folder, class_name):
        story = (folder / "storyboard.md").read_text(encoding="utf-8")
        scene = (folder / "scene.py").read_text(encoding="utf-8")
        for part in ("問い", "試行", "工夫", "一般化", "まとめ"):
            self.assertIn(part, story)
        self.assertIn("STEP 1", story)
        self.assertIn("STEP 2", story)
        self.assertIn("STEP 3", story)
        self.assertIn("STEP 4", story)
        self.assertIn("実例", story)
        self.assertNotIn("今日のゴール", story)
        self.assertNotIn("今日", scene)
        self.assertIn(f"class {class_name}(LessonScene)", scene)
        self.assertNotIn("PacedScene", scene)
        self.assertIn("self.below_chip(", scene)
        self.assertIn("self.stack_below(", scene)
        self.assertIn("self.aligned_table(", scene)
        self.assertIn("self.begin_step(", scene)
        self.assertIn("pause_conclusion", scene)
        self.assertIn("とおく", scene)
        self.assertIn("方法", scene)
        self.assertNotIn("道", scene)
        self.assertNotIn("あれは", scene)
        self._assert_no_japanese_in_mathtex(folder / "scene.py")
        self._assert_no_hardcoded_exponents_in_japanese(folder / "scene.py")
        return story, scene

    def test_math_150_011_has_storyboard_and_scene(self):
        story, scene = self._assert_math_150_common(MATH_150_011, "FalsePositiveBayes")
        self.assertIn(r"P(A\mid B)", scene)
        self.assertIn(r"P(A\mid B)=\dfrac{P(B\mid A)\,P(A)}{P(B)}", scene)
        self.assertIn(r"\dfrac{99}{10098}", scene)
        self.assertIn(r"99+9999=10098", scene)
        self.assertIn(r"\dfrac{99}{99+99}=\dfrac{1}{2}", scene)
        self.assertIn("ベイズ", scene)
        self.assertIn("感度", scene)
        self.assertIn("特異度", scene)
        self.assertNotIn("事前が稀", scene)
        self.assertNotIn("事前が稀だと", story)
        self.assertIn("1 万人に 1 人だとします", scene)
        step1 = scene[
            scene.index("def part_step1_rules") : scene.index("def part_step2_prior")
        ]
        self.assertNotIn(r"P(B\mid A)", step1)
        self.assertNotIn("10098", step1)

    def test_math_150_012_has_storyboard_and_scene(self):
        story, scene = self._assert_math_150_common(MATH_150_012, "CentralLimitDice")
        self.assertIn("二つのサイコロを振って出る目の合計は、何が一番多いでしょうか", scene)
        self.assertIn("def _pips", scene)
        self.assertIn("場合の数", scene)
        self.assertIn("y_axis", scene)
        self.assertNotIn("しぼむ", scene)
        self.assertIn("ペースで小さく", scene)
        self.assertIn(r"6\cdot 6=36", scene)
        self.assertIn(r"6^{3}=216", scene)
        self.assertIn(r"\sqrt{n}", scene)
        self.assertIn(r"\dfrac{1}{\sqrt{n}}", scene)
        self.assertIn(r"2\cdot(1+2+3+4+5)+6", scene)
        self.assertIn(r"=30+6=36", scene)
        self.assertIn("中心極限", scene)
        step1 = scene[
            scene.index("def part_step1_pairs") : scene.index("def part_step2_sums")
        ]
        self.assertNotIn(r"\sqrt{n}", step1)
        self.assertNotIn("正規分布", step1)

    def test_math_150_013_has_storyboard_and_scene(self):
        story, scene = self._assert_math_150_common(MATH_150_013, "LawOfLargeNumbers")
        self.assertNotIn("しぼむ", scene)
        self.assertIn("ペースで小さく", scene)
        self.assertIn("記憶はありません", scene)
        self.assertIn(r"\dfrac{8}{10}", scene)
        self.assertIn(r"8-5=3", scene)
        self.assertIn(r"\dfrac{53}{100}", scene)
        self.assertIn(r"\dfrac{503}{1000}", scene)
        self.assertIn(r"\dfrac{55}{100}", scene)
        self.assertIn(r"\dfrac{520}{1000}", scene)
        self.assertIn(r"\dfrac{1}{\sqrt{n}}", scene)
        self.assertIn("大数の法則", scene)
        step1 = scene[
            scene.index("def part_step1_no_memory") : scene.index(
                "def part_step2_diff_vs_rate"
            )
        ]
        self.assertNotIn("大数の法則", step1)
        self.assertNotIn(r"\dfrac{1}{\sqrt{n}}", step1)

    def test_math_150_014_has_storyboard_and_scene(self):
        story, scene = self._assert_math_150_common(MATH_150_014, "BuffonsNeedle")
        q = scene[scene.index("def part_question") : scene.index("def part_trial_count")]
        self.assertIn(r"L=D", q)
        self.assertNotIn(r"L\le D", q)
        self.assertIn(r"\dfrac{2N}{C}", q)
        self.assertIn("長方形のどの小さな区画も同じ確からしさ", scene)
        self.assertIn(r"L<D", scene)
        self.assertIn(r"x\le\dfrac{L}{2}\sin\theta", scene)
        self.assertIn(r"\dfrac{2L}{\pi D}", scene)
        self.assertIn(r"\pi\approx\dfrac{2LN}{CD}", scene)
        self.assertIn("ビュフォン", scene)
        self.assertIn(r"\int_{0}^{\pi}", scene)
        self.assertIn(r"-\cos\pi-(-\cos 0)", scene)
        step1 = scene[
            scene.index("def part_step1_coords") : scene.index("def part_step2_hit")
        ]
        self.assertNotIn(r"\dfrac{2L}{\pi D}", step1)
        self.assertNotIn("ビュフォン", step1)

    def test_math_150_015_has_storyboard_and_scene(self):
        story, scene = self._assert_math_150_common(MATH_150_015, "RandomWalkReturn")
        self.assertNotIn("入口で再掲", scene)
        self.assertNotIn("観察で十分", scene)
        self.assertIn(r"p_{1}=p_{2}=1", scene)
        self.assertIn(r"p_{d}<1", scene)
        self.assertIn(r"\mathbb{Z}^{d}", scene)
        self.assertIn(r"2^{2}=4", scene)
        self.assertIn(r"2^{4}=16", scene)
        self.assertIn(r"\dbinom{4}{2}", scene)
        self.assertIn(r"\dfrac{6}{16}=\dfrac{3}{8}", scene)
        self.assertIn("ポリア", scene)
        step1 = scene[
            scene.index("def part_step1_two_steps") : scene.index(
                "def part_step2_must_cross"
            )
        ]
        self.assertNotIn("ポリア", step1)

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
