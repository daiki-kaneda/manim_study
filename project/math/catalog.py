"""Machine-readable list of math shorts from #101 onward."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Video:
    number: int
    title: str
    path: str
    scene: str


VIDEOS_101_125: tuple[Video, ...] = (
    Video(101, "勾配", "project/math/21_vector_calculus/101_gradient/scene.py", "Gradient"),
    Video(102, "発散", "project/math/21_vector_calculus/102_divergence/scene.py", "Divergence"),
    Video(103, "回転", "project/math/21_vector_calculus/103_curl/scene.py", "Curl"),
    Video(104, "基本定理", "project/math/21_vector_calculus/104_ftc/scene.py", "FTC"),
    Video(105, "極座標の面積", "project/math/21_vector_calculus/105_polar_area/scene.py", "PolarArea"),
    Video(106, "像", "project/math/22_linear_algebra_2/106_image/scene.py", "ImageSpace"),
    Video(107, "核", "project/math/22_linear_algebra_2/107_nullspace/scene.py", "NullSpace"),
    Video(108, "階数と核", "project/math/22_linear_algebra_2/108_rank_nullity/scene.py", "RankNullity"),
    Video(109, "正射影", "project/math/22_linear_algebra_2/109_projection/scene.py", "OrthogonalProjection"),
    Video(110, "基底の取りかえ", "project/math/22_linear_algebra_2/110_change_of_basis/scene.py", "ChangeOfBasis"),
    Video(111, "平均値の定理", "project/math/23_analysis_2/111_mean_value/scene.py", "MeanValue"),
    Video(112, "ロピタル", "project/math/23_analysis_2/112_lhopital/scene.py", "LHopital"),
    Video(113, "はさみうち", "project/math/23_analysis_2/113_squeeze/scene.py", "Squeeze"),
    Video(114, "収束半径", "project/math/23_analysis_2/114_radius/scene.py", "RadiusOfConvergence"),
    Video(115, "デルタ関数", "project/math/23_analysis_2/115_dirac/scene.py", "DiracDelta"),
    Video(116, "多面体公式", "project/math/24_geometry_2/116_euler_char/scene.py", "EulerCharacteristic"),
    Video(117, "ヘロンの公式", "project/math/24_geometry_2/117_heron/scene.py", "Heron"),
    Video(118, "方べきの定理", "project/math/24_geometry_2/118_power_of_a_point/scene.py", "PowerOfAPoint"),
    Video(119, "反転", "project/math/24_geometry_2/119_inversion/scene.py", "CircleInversion"),
    Video(120, "立体射影", "project/math/24_geometry_2/120_stereographic/scene.py", "Stereographic"),
    Video(121, "誕生日", "project/math/25_info/121_birthday/scene.py", "Birthday"),
    Video(122, "ランダムウォーク", "project/math/25_info/122_random_walk/scene.py", "RandomWalk"),
    Video(123, "エントロピー", "project/math/25_info/123_entropy/scene.py", "Entropy"),
    Video(124, "マルコフ連鎖", "project/math/25_info/124_markov/scene.py", "MarkovChain"),
    Video(125, "モンテカルロの π", "project/math/25_info/125_monte_carlo_pi/scene.py", "MonteCarloPi"),
)
