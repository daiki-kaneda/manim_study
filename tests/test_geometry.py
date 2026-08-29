from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from manim_math.geometry import odd_layer_cells, odd_square_layers, polar, staircase_cells
from manim_math.japanese import get_japanese_font
from manim_math.path_setup import add_repo_root_to_syspath


class GeometryTests(unittest.TestCase):
    def test_staircase_counts_triangular_numbers(self):
        for n in range(1, 8):
            cells = staircase_cells(n)
            self.assertEqual(len(cells), n * (n + 1) // 2)
            self.assertEqual(len(set(cells)), len(cells))

    def test_odd_layers_tile_a_square(self):
        n = 4
        layers = odd_square_layers(n)
        sizes = [len(layer) for layer in layers]
        self.assertEqual(sizes, [1, 3, 5, 7])
        tiled = [cell for layer in layers for cell in layer]
        self.assertEqual(len(tiled), n * n)
        self.assertEqual(len(set(tiled)), n * n)
        self.assertEqual(set(tiled), {(c, r) for c in range(n) for r in range(n)})

    def test_polar_quarter_turn(self):
        x, y, z = polar(2.0, 0.0)
        self.assertAlmostEqual(x, 2.0)
        self.assertAlmostEqual(y, 0.0)
        self.assertAlmostEqual(z, 0.0)
        x, y, z = polar(2.0, 3.141592653589793 / 2)
        self.assertAlmostEqual(x, 0.0, places=6)
        self.assertAlmostEqual(y, 2.0, places=6)

    def test_odd_layer_rejects_invalid_k(self):
        with self.assertRaises(ValueError):
            odd_layer_cells(0)


class PathAndFontTests(unittest.TestCase):
    def test_repo_root_detection(self):
        root = add_repo_root_to_syspath()
        self.assertTrue((root / "manim_math" / "__init__.py").is_file())

    def test_japanese_font_is_nonempty(self):
        font = get_japanese_font()
        self.assertTrue(isinstance(font, str) and len(font) > 0)


if __name__ == "__main__":
    unittest.main()
