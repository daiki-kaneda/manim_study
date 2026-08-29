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

VIDEOS_126_137: tuple[Video, ...] = (
    Video(126, "弧長", "project/math/26_analysis_3/126_arc_length/scene.py", "ArcLength"),
    Video(127, "連続", "project/math/26_analysis_3/127_epsilon_delta/scene.py", "EpsilonDelta"),
    Video(128, "トレース", "project/math/26_analysis_3/128_trace/scene.py", "MatrixTrace"),
    Video(129, "回転行列", "project/math/27_linear_3/129_rotation_matrix/scene.py", "RotationMatrix"),
    Video(130, "特異値", "project/math/27_linear_3/130_svd/scene.py", "SVDStretch"),
    Video(131, "チェバの定理", "project/math/28_geometry_3/131_ceva/scene.py", "Ceva"),
    Video(132, "内接円", "project/math/28_geometry_3/132_incircle/scene.py", "Incircle"),
    Video(133, "トレミーの定理", "project/math/28_geometry_3/133_ptolemy/scene.py", "Ptolemy"),
    Video(134, "幾何分布", "project/math/29_probability_2/134_geometric/scene.py", "GeometricDist"),
    Video(135, "ポアソン", "project/math/29_probability_2/135_poisson/scene.py", "Poisson"),
    Video(136, "母関数", "project/math/29_probability_2/136_generating_function/scene.py", "GeneratingFunction"),
    Video(137, "カタラン数", "project/math/29_probability_2/137_catalan/scene.py", "Catalan"),
)

VIDEOS_138_149: tuple[Video, ...] = (
    Video(138, "置換積分", "project/math/30_analysis_4/138_substitution/scene.py", "Substitution"),
    Video(139, "広義積分", "project/math/30_analysis_4/139_improper/scene.py", "ImproperIntegral"),
    Video(140, "偏微分", "project/math/30_analysis_4/140_partial/scene.py", "PartialDerivative"),
    Video(141, "線積分", "project/math/30_analysis_4/141_line_integral/scene.py", "LineIntegral"),
    Video(142, "直交化", "project/math/31_linear_4/142_gram_schmidt/scene.py", "GramSchmidt"),
    Video(143, "対角化", "project/math/31_linear_4/143_diagonalize/scene.py", "Diagonalize"),
    Video(144, "直交行列", "project/math/31_linear_4/144_orthogonal_matrix/scene.py", "OrthogonalMatrix"),
    Video(145, "九点円", "project/math/32_geometry_4/145_nine_point/scene.py", "NinePoint"),
    Video(146, "オイラー線", "project/math/32_geometry_4/146_euler_line/scene.py", "EulerLine"),
    Video(147, "メネラウスの定理", "project/math/32_geometry_4/147_menelaus/scene.py", "Menelaus"),
    Video(148, "角の二等分線", "project/math/32_geometry_4/148_angle_bisector/scene.py", "AngleBisector"),
    Video(149, "フィボナッチ", "project/math/33_combinatorics_2/149_fibonacci/scene.py", "Fibonacci"),
)

VIDEOS_150_161: tuple[Video, ...] = (
    Video(150, "回転体", "project/math/34_analysis_5/150_disk_method/scene.py", "DiskMethod"),
    Video(151, "ヤコビアン", "project/math/34_analysis_5/151_jacobian/scene.py", "Jacobian"),
    Video(152, "畳み込み", "project/math/34_analysis_5/152_convolution/scene.py", "Convolution"),
    Video(153, "スペクトル定理", "project/math/35_linear_5/153_spectral/scene.py", "SpectralTheorem"),
    Video(154, "消去法", "project/math/35_linear_5/154_elimination/scene.py", "GaussianElim"),
    Video(155, "クラメルの公式", "project/math/35_linear_5/155_cramer/scene.py", "Cramer"),
    Video(156, "ナポレオンの定理", "project/math/36_geometry_5/156_napoleon/scene.py", "Napoleon"),
    Video(157, "シムソン線", "project/math/36_geometry_5/157_simson/scene.py", "Simson"),
    Video(158, "ヴィヴィアニ", "project/math/36_geometry_5/158_viviani/scene.py", "Viviani"),
    Video(159, "指数分布", "project/math/37_probability_3/159_exponential/scene.py", "ExponentialDist"),
    Video(160, "チェビシェフ", "project/math/37_probability_3/160_chebyshev/scene.py", "Chebyshev"),
    Video(161, "オイラーのφ", "project/math/38_number_2/161_euler_totient/scene.py", "EulerTotient"),
)

VIDEOS_162_173: tuple[Video, ...] = (
    Video(162, "回転面", "project/math/39_analysis_6/162_surface_area/scene.py", "SurfaceOfRevolution"),
    Video(163, "ラプラシアン", "project/math/39_analysis_6/163_laplacian/scene.py", "Laplacian"),
    Video(164, "フビニの定理", "project/math/39_analysis_6/164_fubini/scene.py", "Fubini"),
    Video(165, "LU 分解", "project/math/40_linear_6/165_lu/scene.py", "LUDecomposition"),
    Video(166, "正規方程式", "project/math/40_linear_6/166_least_squares_geom/scene.py", "NormalEquations"),
    Video(167, "擬似逆", "project/math/40_linear_6/167_pseudoinverse/scene.py", "Pseudoinverse"),
    Video(168, "ファン・オーベル", "project/math/41_geometry_6/168_van_obel/scene.py", "VanAubel"),
    Video(169, "モーリーの定理", "project/math/41_geometry_6/169_morley/scene.py", "Morley"),
    Video(170, "ブラフマグプタ", "project/math/41_geometry_6/170_brahmagupta/scene.py", "Brahmagupta"),
    Video(171, "確率の木", "project/math/42_probability_4/171_bayes_tree/scene.py", "ProbabilityTree"),
    Video(172, "モーメント", "project/math/42_probability_4/172_moment/scene.py", "Moments"),
    Video(173, "スターリング数", "project/math/43_combinatorics_3/173_stirling/scene.py", "Stirling"),
)

VIDEOS_174_185: tuple[Video, ...] = (
    Video(174, "テイラー余り", "project/math/44_analysis_7/174_taylor_remainder/scene.py", "TaylorRemainder"),
    Video(175, "フーリエ変換", "project/math/44_analysis_7/175_fourier_transform/scene.py", "FourierTransform"),
    Video(176, "留数", "project/math/44_analysis_7/176_residue/scene.py", "Residue"),
    Video(177, "ハウスホルダー", "project/math/45_linear_7/177_householder/scene.py", "Householder"),
    Video(178, "QR 分解", "project/math/45_linear_7/178_qr/scene.py", "QRFactorization"),
    Video(179, "条件数", "project/math/45_linear_7/179_condition/scene.py", "ConditionNumber"),
    Video(180, "デザルグの定理", "project/math/46_geometry_7/180_desargues/scene.py", "Desargues"),
    Video(181, "パスカルの定理", "project/math/46_geometry_7/181_pascal_hexagon/scene.py", "PascalHexagon"),
    Video(182, "バタフライ定理", "project/math/46_geometry_7/182_butterfly/scene.py", "Butterfly"),
    Video(183, "ハザード", "project/math/47_probability_5/183_hazard/scene.py", "HazardRate"),
    Video(184, "同時分布", "project/math/47_probability_5/184_joint/scene.py", "JointDensity"),
    Video(185, "ベル数", "project/math/48_combinatorics_4/185_bell/scene.py", "BellNumbers"),
)

VIDEOS_186_197: tuple[Video, ...] = (
    Video(186, "ロルの定理", "project/math/49_analysis_8/186_rolle/scene.py", "Rolle"),
    Video(187, "一様収束", "project/math/49_analysis_8/187_uniform/scene.py", "UniformConvergence"),
    Video(188, "熱方程式", "project/math/49_analysis_8/188_heat/scene.py", "HeatEquation"),
    Video(189, "ジョルダン標準形", "project/math/50_linear_8/189_jordan/scene.py", "JordanForm"),
    Video(190, "行列の指数関数", "project/math/50_linear_8/190_matrix_exp/scene.py", "MatrixExponential"),
    Video(191, "レイリー商", "project/math/50_linear_8/191_rayleigh/scene.py", "RayleighQuotient"),
    Video(192, "ブリアンションの定理", "project/math/51_geometry_8/192_brianchon/scene.py", "Brianchon"),
    Video(193, "ミケルの定理", "project/math/51_geometry_8/193_miquel/scene.py", "Miquel"),
    Video(194, "アポロニウスの円", "project/math/51_geometry_8/194_apollonius/scene.py", "Apollonius"),
    Video(195, "共分散", "project/math/52_probability_6/195_covariance/scene.py", "Covariance"),
    Video(196, "条件付き期待値", "project/math/52_probability_6/196_conditional_expectation/scene.py", "ConditionalExpectation"),
    Video(197, "分割数", "project/math/53_combinatorics_5/197_partition/scene.py", "PartitionNumbers"),
)

VIDEOS_198_209: tuple[Video, ...] = (
    Video(198, "部分積分", "project/math/54_analysis_9/198_parts/scene.py", "IntegrationByParts"),
    Video(199, "陰関数", "project/math/54_analysis_9/199_implicit/scene.py", "ImplicitCurve"),
    Video(200, "波動方程式", "project/math/54_analysis_9/200_wave/scene.py", "WaveEquation"),
    Video(201, "シューア分解", "project/math/55_linear_9/201_schur/scene.py", "SchurForm"),
    Video(202, "行列ノルム", "project/math/55_linear_9/202_matrix_norm/scene.py", "MatrixNorm"),
    Video(203, "グラム行列", "project/math/55_linear_9/203_gram/scene.py", "GramMatrix"),
    Video(204, "フェルマー点", "project/math/56_geometry_9/204_fermat_point/scene.py", "FermatPoint"),
    Video(205, "傍接円", "project/math/56_geometry_9/205_excircle/scene.py", "Excircle"),
    Video(206, "接弦定理", "project/math/56_geometry_9/206_tangent_chord/scene.py", "TangentChord"),
    Video(207, "マルコフ不等式", "project/math/57_probability_7/207_markov_ineq/scene.py", "MarkovInequality"),
    Video(208, "特性関数", "project/math/57_probability_7/208_characteristic/scene.py", "CharacteristicFunction"),
    Video(209, "フック長公式", "project/math/58_combinatorics_6/209_hook_length/scene.py", "HookLength"),
)
