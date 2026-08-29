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

VIDEOS_210_221: tuple[Video, ...] = (
    Video(210, "グリーンの恒等式", "project/math/59_analysis_10/210_green_identity/scene.py", "GreenIdentity"),
    Video(211, "平面のストークス", "project/math/59_analysis_10/211_stokes_2d/scene.py", "Stokes2D"),
    Video(212, "ディリクレ原理", "project/math/59_analysis_10/212_dirichlet/scene.py", "DirichletPrinciple"),
    Video(213, "ランク 1 更新", "project/math/60_linear_10/213_rank_one/scene.py", "RankOneUpdate"),
    Video(214, "シャーマン・モリソン", "project/math/60_linear_10/214_woodbury/scene.py", "ShermanMorrison"),
    Video(215, "正定値", "project/math/60_linear_10/215_positive_def/scene.py", "PositiveDefinite"),
    Video(216, "デカルトの円定理", "project/math/61_geometry_10/216_descartes/scene.py", "DescartesCircle"),
    Video(217, "オイラーの距離公式", "project/math/61_geometry_10/217_euler_distance/scene.py", "EulerDistance"),
    Video(218, "等角共役", "project/math/61_geometry_10/218_isogonal/scene.py", "IsogonalConjugate"),
    Video(219, "チェルノフ界", "project/math/62_probability_8/219_chernoff/scene.py", "ChernoffBound"),
    Video(220, "エントロピー率", "project/math/62_probability_8/220_entropy_rate/scene.py", "EntropyRate"),
    Video(221, "プリューファーコード", "project/math/63_combinatorics_7/221_prufer/scene.py", "PruferCode"),
)

VIDEOS_222_233: tuple[Video, ...] = (
    Video(222, "フーリエ級数", "project/math/64_analysis_11/222_fourier_series/scene.py", "FourierSeries"),
    Video(223, "ラプラス変換", "project/math/64_analysis_11/223_laplace/scene.py", "LaplaceTransform"),
    Video(224, "変分法", "project/math/64_analysis_11/224_calculus_variations/scene.py", "CalculusOfVariations"),
    Video(225, "クロネッカー積", "project/math/65_linear_11/225_kronecker/scene.py", "KroneckerProduct"),
    Video(226, "低ランク近似", "project/math/65_linear_11/226_low_rank/scene.py", "LowRankApprox"),
    Video(227, "ペロン・フロベニウス", "project/math/65_linear_11/227_perron/scene.py", "PerronFrobenius"),
    Video(228, "パップスの定理", "project/math/66_geometry_11/228_pappus/scene.py", "Pappus"),
    Video(229, "球面過剰", "project/math/66_geometry_11/229_spherical_excess/scene.py", "SphericalExcess"),
    Video(230, "ファン・シューテン", "project/math/66_geometry_11/230_van_schooten/scene.py", "VanSchooten"),
    Video(231, "ワルドの等式", "project/math/67_probability_9/231_wald/scene.py", "WaldEquation"),
    Video(232, "経験分布関数", "project/math/67_probability_9/232_empirical_cdf/scene.py", "EmpiricalCDF"),
    Video(233, "バーンサイドの補題", "project/math/68_combinatorics_8/233_burnside/scene.py", "Burnside"),
)

VIDEOS_234_245: tuple[Video, ...] = (
    Video(234, "最大値原理", "project/math/69_analysis_12/234_maximum_principle/scene.py", "MaximumPrinciple"),
    Video(235, "ルジャンドル変換", "project/math/69_analysis_12/235_legendre/scene.py", "LegendreTransform"),
    Video(236, "グリーン関数", "project/math/69_analysis_12/236_green_function/scene.py", "GreensFunction"),
    Video(237, "ゲルシュゴリン", "project/math/70_linear_12/237_gershgorin/scene.py", "Gershgorin"),
    Video(238, "クリロフ部分空間", "project/math/70_linear_12/238_krylov/scene.py", "Krylov"),
    Video(239, "冪乗法", "project/math/70_linear_12/239_power_iteration/scene.py", "PowerIteration"),
    Video(240, "垂足三角形", "project/math/71_geometry_12/240_orthic/scene.py", "OrthicTriangle"),
    Video(241, "接線の長さ", "project/math/71_geometry_12/241_tangent_lengths/scene.py", "TangentLengths"),
    Video(242, "根軸", "project/math/71_geometry_12/242_radical_axis/scene.py", "RadicalAxis"),
    Video(243, "クーポンコレクター", "project/math/72_probability_10/243_coupon/scene.py", "CouponCollector"),
    Video(244, "停止時刻", "project/math/72_probability_10/244_stopping_time/scene.py", "StoppingTime"),
    Video(245, "共役分割", "project/math/73_combinatorics_9/245_conjugate_partition/scene.py", "ConjugatePartition"),
)

VIDEOS_246_257: tuple[Video, ...] = (
    Video(246, "平均値の性質", "project/math/74_analysis_13/246_mean_value_prop/scene.py", "MeanValueProperty"),
    Video(247, "ポアソン方程式", "project/math/74_analysis_13/247_poisson_eq/scene.py", "PoissonEquation"),
    Video(248, "オーダー記号", "project/math/74_analysis_13/248_big_o/scene.py", "BigO"),
    Video(249, "コレスキー分解", "project/math/75_linear_13/249_cholesky/scene.py", "Cholesky"),
    Video(250, "ヤコビ反復", "project/math/75_linear_13/250_jacobi/scene.py", "JacobiIteration"),
    Video(251, "ノルムの同値", "project/math/75_linear_13/251_norm_equiv/scene.py", "NormEquivalence"),
    Video(252, "アポロニウスの定理", "project/math/76_geometry_13/252_apollonius_median/scene.py", "ApolloniusMedian"),
    Video(253, "重心座標", "project/math/76_geometry_13/253_barycentric/scene.py", "Barycentric"),
    Video(254, "フォイエルバッハの定理", "project/math/76_geometry_13/254_feuerbach/scene.py", "Feuerbach"),
    Video(255, "ポアソン過程", "project/math/77_probability_11/255_poisson_process/scene.py", "PoissonProcess"),
    Video(256, "M/M/1 待ち行列", "project/math/77_probability_11/256_mm1/scene.py", "MM1Queue"),
    Video(257, "スターリング第一種", "project/math/78_combinatorics_10/257_stirling_first/scene.py", "StirlingFirstKind"),
)

VIDEOS_258_269: tuple[Video, ...] = (
    Video(258, "ヘルダーの不等式", "project/math/79_analysis_14/258_holder/scene.py", "HolderInequality"),
    Video(259, "ヤングの不等式", "project/math/79_analysis_14/259_young/scene.py", "YoungInequality"),
    Video(260, "弱い収束", "project/math/79_analysis_14/260_weak_convergence/scene.py", "WeakConvergence"),
    Video(261, "フロベニウスノルム", "project/math/80_linear_14/261_frobenius/scene.py", "FrobeniusNorm"),
    Video(262, "スペクトル半径", "project/math/80_linear_14/262_spectral_radius/scene.py", "SpectralRadius"),
    Video(263, "アダマールの不等式", "project/math/80_linear_14/263_hadamard/scene.py", "HadamardInequality"),
    Video(264, "余弦定理", "project/math/81_geometry_14/264_law_of_cosines/scene.py", "LawOfCosines"),
    Video(265, "円に内接する四角形", "project/math/81_geometry_14/265_cyclic_quad/scene.py", "CyclicQuad"),
    Video(266, "螺旋相似", "project/math/81_geometry_14/266_spiral_sim/scene.py", "SpiralSimilarity"),
    Video(267, "分散の加法性", "project/math/82_probability_12/267_variance_add/scene.py", "VarianceAdditivity"),
    Video(268, "尤度関数", "project/math/82_probability_12/268_likelihood/scene.py", "Likelihood"),
    Video(269, "パスカルの恒等式", "project/math/83_combinatorics_11/269_pascal_identity/scene.py", "PascalIdentity"),
)

VIDEOS_270_281: tuple[Video, ...] = (
    Video(270, "ミンコフスキーの不等式", "project/math/84_analysis_15/270_minkowski/scene.py", "MinkowskiInequality"),
    Video(271, "ベッセルの不等式", "project/math/84_analysis_15/271_bessel/scene.py", "BesselInequality"),
    Video(272, "パーセバルの等式", "project/math/84_analysis_15/272_parseval/scene.py", "ParsevalIdentity"),
    Video(273, "ガウス・ザイデル法", "project/math/85_linear_15/273_gauss_seidel/scene.py", "GaussSeidel"),
    Video(274, "ケーリー・ハミルトン", "project/math/85_linear_15/274_cayley_hamilton/scene.py", "CayleyHamilton"),
    Video(275, "数値域", "project/math/85_linear_15/275_numerical_range/scene.py", "NumericalRange"),
    Video(276, "ヴァリニョンの定理", "project/math/86_geometry_15/276_varignon/scene.py", "Varignon"),
    Video(277, "ピトーの定理", "project/math/86_geometry_15/277_pitot/scene.py", "Pitot"),
    Video(278, "英国旗定理", "project/math/86_geometry_15/278_british_flag/scene.py", "BritishFlag"),
    Video(279, "イェンセンの不等式", "project/math/87_probability_13/279_jensen/scene.py", "JensenInequality"),
    Video(280, "全分散の法則", "project/math/87_probability_13/280_total_variance/scene.py", "TotalVariance"),
    Video(281, "ホッケースティック恒等式", "project/math/88_combinatorics_12/281_hockey_stick/scene.py", "HockeyStick"),
)

VIDEOS_282_293: tuple[Video, ...] = (
    Video(282, "ワイエルシュトラスの M 判定", "project/math/89_analysis_16/282_weierstrass_m/scene.py", "WeierstrassMTest"),
    Video(283, "ファトゥの補題", "project/math/89_analysis_16/283_fatou/scene.py", "FatouLemma"),
    Video(284, "優収束定理", "project/math/89_analysis_16/284_dominated/scene.py", "DominatedConvergence"),
    Video(285, "SOR 法", "project/math/90_linear_16/285_sor/scene.py", "SORMethod"),
    Video(286, "共役勾配法", "project/math/90_linear_16/286_cg/scene.py", "ConjugateGradient"),
    Video(287, "行列式補題", "project/math/90_linear_16/287_matrix_det_lemma/scene.py", "MatrixDetLemma"),
    Video(288, "ジェルゴンヌ点", "project/math/91_geometry_16/288_gergonne/scene.py", "Gergonne"),
    Video(289, "ナーゲル点", "project/math/91_geometry_16/289_nagel/scene.py", "NagelPoint"),
    Video(290, "ルモワーヌ点", "project/math/91_geometry_16/290_lemoine/scene.py", "Lemoine"),
    Video(291, "ヘフディングの不等式", "project/math/92_probability_14/291_hoeffding/scene.py", "Hoeffding"),
    Video(292, "KL ダイバージェンス", "project/math/92_probability_14/292_kl/scene.py", "KLDivergence"),
    Video(293, "ヴァンデルモンドの恒等式", "project/math/93_combinatorics_13/293_vandermonde/scene.py", "Vandermonde"),
)

VIDEOS_294_305: tuple[Video, ...] = (
    Video(294, "バナッハの不動点定理", "project/math/94_analysis_17/294_banach_fixed/scene.py", "BanachFixedPoint"),
    Video(295, "一様有界性原理", "project/math/94_analysis_17/295_uniform_boundedness/scene.py", "UniformBoundedness"),
    Video(296, "開写像定理", "project/math/94_analysis_17/296_open_mapping/scene.py", "OpenMapping"),
    Video(297, "ワイルの不等式", "project/math/95_linear_17/297_weyl/scene.py", "WeylInequality"),
    Video(298, "ミニマックス定理", "project/math/95_linear_17/298_min_max/scene.py", "MinMaxTheorem"),
    Video(299, "レゾルベント", "project/math/95_linear_17/299_resolvent/scene.py", "Resolvent"),
    Video(300, "三線座標", "project/math/96_geometry_17/300_trilinear/scene.py", "Trilinear"),
    Video(301, "スピーカー中心", "project/math/96_geometry_17/301_spieker/scene.py", "Spieker"),
    Video(302, "ブローカル点", "project/math/96_geometry_17/302_brocard/scene.py", "Brocard"),
    Video(303, "全変動距離", "project/math/97_probability_15/303_total_variation/scene.py", "TotalVariation"),
    Video(304, "反射原理", "project/math/97_probability_15/304_reflection/scene.py", "ReflectionPrinciple"),
    Video(305, "包除原理", "project/math/98_combinatorics_14/305_inclusion_exclusion/scene.py", "InclusionExclusion"),
)

VIDEOS_306_317: tuple[Video, ...] = (
    Video(306, "閉グラフ定理", "project/math/99_analysis_18/306_closed_graph/scene.py", "ClosedGraph"),
    Video(307, "リースの補題", "project/math/99_analysis_18/307_riesz_lemma/scene.py", "RieszLemma"),
    Video(308, "ストーン・ワイエルシュトラス", "project/math/99_analysis_18/308_stone_weierstrass/scene.py", "StoneWeierstrass"),
    Video(309, "シューア補元", "project/math/100_linear_18/309_schur_complement/scene.py", "SchurComplement"),
    Video(310, "コンパニオン行列", "project/math/100_linear_18/310_companion/scene.py", "CompanionMatrix"),
    Video(311, "トープリッツ行列", "project/math/100_linear_18/311_toeplitz/scene.py", "Toeplitz"),
    Video(312, "カルノーの定理", "project/math/101_geometry_18/312_carnot/scene.py", "Carnot"),
    Video(313, "ニュートン・ガウス線", "project/math/101_geometry_18/313_newton_gauss/scene.py", "NewtonGauss"),
    Video(314, "ポンセレの定理", "project/math/101_geometry_18/314_poncelet/scene.py", "Poncelet"),
    Video(315, "グリベンコ・カンテリ", "project/math/102_probability_16/315_glivenko/scene.py", "GlivenkoCantelli"),
    Video(316, "ブートストラップ", "project/math/102_probability_16/316_bootstrap/scene.py", "Bootstrap"),
    Video(317, "星と棒", "project/math/103_combinatorics_15/317_stars_and_bars/scene.py", "StarsAndBars"),
)

VIDEOS_318_329: tuple[Video, ...] = (
    Video(318, "アスコリ・アルツェラ", "project/math/104_analysis_19/318_ascoli/scene.py", "AscoliArzela"),
    Video(319, "ディニの定理", "project/math/104_analysis_19/319_dini/scene.py", "DiniTheorem"),
    Video(320, "アーベル総和法", "project/math/104_analysis_19/320_abel_sum/scene.py", "AbelSummation"),
    Video(321, "リアプノフ方程式", "project/math/105_linear_19/321_lyapunov/scene.py", "LyapunovEquation"),
    Video(322, "シルベスター方程式", "project/math/105_linear_19/322_sylvester/scene.py", "SylvesterEquation"),
    Video(323, "ケイリー変換", "project/math/105_linear_19/323_cayley_transform/scene.py", "CayleyTransform"),
    Video(324, "三線極線", "project/math/106_geometry_19/324_trilinear_polar/scene.py", "TrilinearPolar"),
    Video(325, "等力点", "project/math/106_geometry_19/325_isodynamic/scene.py", "Isodynamic"),
    Video(326, "垂足軸", "project/math/106_geometry_19/326_orthic_axis/scene.py", "OrthicAxis"),
    Video(327, "ベネットの不等式", "project/math/107_probability_17/327_bennett/scene.py", "BennettInequality"),
    Video(328, "DKW 不等式", "project/math/107_probability_17/328_dvoretzky/scene.py", "DKWInequality"),
    Video(329, "バロット定理", "project/math/108_combinatorics_16/329_ballot/scene.py", "BallotTheorem"),
)

VIDEOS_330_341: tuple[Video, ...] = (
    Video(330, "ハーン・バナッハの定理", "project/math/109_analysis_20/330_hahn_banach/scene.py", "HahnBanach"),
    Video(331, "ベールの範疇定理", "project/math/109_analysis_20/331_baire/scene.py", "BaireCategory"),
    Video(332, "アラオグルの定理", "project/math/109_analysis_20/332_alaoglu/scene.py", "Alaoglu"),
    Video(333, "ヘッセンベルグ形", "project/math/110_linear_20/333_hessenberg/scene.py", "Hessenberg"),
    Video(334, "逆反復法", "project/math/110_linear_20/334_inverse_iteration/scene.py", "InverseIteration"),
    Video(335, "核ノルム", "project/math/110_linear_20/335_nuclear_norm/scene.py", "NuclearNorm"),
    Video(336, "内心", "project/math/111_geometry_20/336_incenter/scene.py", "Incenter"),
    Video(337, "傍心", "project/math/111_geometry_20/337_excenter/scene.py", "Excenter"),
    Video(338, "タルボットの定理", "project/math/111_geometry_20/338_talbot/scene.py", "Talbot"),
    Video(339, "チャップマン・コロモゴロフ", "project/math/112_probability_18/339_chapman/scene.py", "ChapmanKolmogorov"),
    Video(340, "経験過程", "project/math/112_probability_18/340_empirical_process/scene.py", "EmpiricalProcess"),
    Video(341, "リュカの定理", "project/math/113_combinatorics_17/341_lucas/scene.py", "LucasTheorem"),
)

VIDEOS_342_353: tuple[Video, ...] = (
    Video(342, "フレシェ微分", "project/math/114_analysis_21/342_frechet/scene.py", "FrechetDerivative"),
    Video(343, "ゲートー微分", "project/math/114_analysis_21/343_gateaux/scene.py", "GateauxDerivative"),
    Video(344, "ソボレフの不等式", "project/math/114_analysis_21/344_sobolev/scene.py", "SobolevInequality"),
    Video(345, "作用素ノルム", "project/math/115_linear_21/345_operator_norm/scene.py", "OperatorNorm"),
    Video(346, "フォン・ノイマンの内積", "project/math/115_linear_21/346_von_neumann/scene.py", "VonNeumann"),
    Video(347, "ブロッホ球", "project/math/115_linear_21/347_bloch/scene.py", "BlochSphere"),
    Video(348, "接線三角形", "project/math/116_geometry_21/348_tangential_triangle/scene.py", "TangentialTriangle"),
    Video(349, "接点三角形", "project/math/116_geometry_21/349_intouch_triangle/scene.py", "IntouchTriangle"),
    Video(350, "オイラー反射点", "project/math/116_geometry_21/350_euler_reflection/scene.py", "EulerReflection"),
    Video(351, "ファインマン・カッツ", "project/math/117_probability_19/351_feynman_kac/scene.py", "FeynmanKac"),
    Video(352, "パーコレーション", "project/math/117_probability_19/352_percolation/scene.py", "Percolation"),
    Video(353, "メビウス反転", "project/math/118_combinatorics_18/353_mobius/scene.py", "MobiusInversion"),
)

VIDEOS_354_365: tuple[Video, ...] = (
    Video(354, "ヒルベルト空間", "project/math/119_analysis_22/354_hilbert/scene.py", "HilbertSpace"),
    Video(355, "リースの表現定理", "project/math/119_analysis_22/355_riesz_rep/scene.py", "RieszRepresentation"),
    Video(356, "ラックス・ミルグラム", "project/math/119_analysis_22/356_lax_milgram/scene.py", "LaxMilgram"),
    Video(357, "極分解", "project/math/120_linear_22/357_polar_decomp/scene.py", "PolarDecomposition"),
    Video(358, "CS 分解", "project/math/120_linear_22/358_cs_decomp/scene.py", "CSDecomposition"),
    Video(359, "数値半径", "project/math/120_linear_22/359_numerical_radius/scene.py", "NumericalRadius"),
    Video(360, "傍心三角形", "project/math/121_geometry_22/360_excentral/scene.py", "ExcentralTriangle"),
    Video(361, "接線四角形", "project/math/121_geometry_22/361_tangential_quad/scene.py", "TangentialQuad"),
    Video(362, "両心四角形", "project/math/121_geometry_22/362_bicentric/scene.py", "BicentricQuad"),
    Video(363, "大偏差原理", "project/math/122_probability_20/363_large_dev/scene.py", "LargeDeviations"),
    Video(364, "サノフの定理", "project/math/122_probability_20/364_sanov/scene.py", "SanovTheorem"),
    Video(365, "ゼッケンドルフの定理", "project/math/123_combinatorics_19/365_zeckendorf/scene.py", "Zeckendorf"),
)

VIDEOS_366_377: tuple[Video, ...] = (
    Video(366, "自己共役作用素", "project/math/124_analysis_23/366_self_adjoint/scene.py", "SelfAdjoint"),
    Video(367, "ユニタリ群", "project/math/124_analysis_23/367_unitary_group/scene.py", "UnitaryGroup"),
    Video(368, "フレドホルムの択一", "project/math/124_analysis_23/368_fredholm/scene.py", "FredholmAlternative"),
    Video(369, "行列対数", "project/math/125_linear_23/369_matrix_log/scene.py", "MatrixLogarithm"),
    Video(370, "パデ近似", "project/math/125_linear_23/370_pade/scene.py", "PadeApproximation"),
    Video(371, "GMRES", "project/math/125_linear_23/371_gmres/scene.py", "GMRES"),
    Video(372, "共円五点", "project/math/126_geometry_23/372_cocircular5/scene.py", "CocircularFive"),
    Video(373, "反相似", "project/math/126_geometry_23/373_antisimilarity/scene.py", "Antisimilarity"),
    Video(374, "ポンスレ・スタイナー", "project/math/126_geometry_23/374_poncelet_steiner/scene.py", "PonceletSteiner"),
    Video(375, "エルゴード定理", "project/math/127_probability_21/375_ergodic/scene.py", "ErgodicTheorem"),
    Video(376, "マルチンゲール収束", "project/math/127_probability_21/376_martingale/scene.py", "MartingaleConvergence"),
    Video(377, "ベル多項式", "project/math/128_combinatorics_20/377_bell_poly/scene.py", "BellPolynomials"),
)

VIDEOS_378_389: tuple[Video, ...] = (
    Video(378, "コンパクト作用素", "project/math/129_analysis_24/378_compact_op/scene.py", "CompactOperator"),
    Video(379, "関数カリキュラス", "project/math/129_analysis_24/379_functional_calc/scene.py", "FunctionalCalculus"),
    Video(380, "フレドホルム指数", "project/math/129_analysis_24/380_fredholm_index/scene.py", "FredholmIndex"),
    Video(381, "アダマール積", "project/math/130_linear_24/381_hadamard_product/scene.py", "HadamardProduct"),
    Video(382, "行列平方根", "project/math/130_linear_24/382_matrix_square_root/scene.py", "MatrixSquareRoot"),
    Video(383, "固有値の条件数", "project/math/130_linear_24/383_condition_eig/scene.py", "EigenCondition"),
    Video(384, "五点ミケル", "project/math/131_geometry_24/384_miquel_five/scene.py", "MiquelFive"),
    Video(385, "調和共役", "project/math/131_geometry_24/385_harmonic_conjugate/scene.py", "HarmonicConjugate"),
    Video(386, "モルレーの定理", "project/math/131_geometry_24/386_morley/scene.py", "Morley"),
    Video(387, "分岐過程", "project/math/132_probability_22/387_branching/scene.py", "BranchingProcess"),
    Video(388, "再生過程", "project/math/132_probability_22/388_renewal/scene.py", "RenewalProcess"),
    Video(389, "スターリング第二種", "project/math/133_combinatorics_21/389_stirling2/scene.py", "StirlingSecond"),
)

VIDEOS_390_401: tuple[Video, ...] = (
    Video(390, "本質スペクトル", "project/math/134_analysis_25/390_essential_spec/scene.py", "EssentialSpectrum"),
    Video(391, "ゲルファント表現", "project/math/134_analysis_25/391_gelfand/scene.py", "Gelfand"),
    Video(392, "弱作用素位相", "project/math/134_analysis_25/392_wot/scene.py", "WeakOperatorTopology"),
    Video(393, "アーノルディ法", "project/math/135_linear_25/393_arnoldi/scene.py", "Arnoldi"),
    Video(394, "ランチョス法", "project/math/135_linear_25/394_lanczos/scene.py", "Lanczos"),
    Video(395, "擬逆行列", "project/math/135_linear_25/395_pseudoinverse/scene.py", "Pseudoinverse"),
    Video(396, "日本の定理", "project/math/136_geometry_25/396_japanese_thm/scene.py", "JapaneseTheorem"),
    Video(397, "クロス比", "project/math/136_geometry_25/397_cross_ratio/scene.py", "CrossRatio"),
    Video(398, "トムセンの図形", "project/math/136_geometry_25/398_thomsen/scene.py", "Thomsen"),
    Video(399, "結合法", "project/math/137_probability_23/399_coupling/scene.py", "Coupling"),
    Video(400, "ブラウン運動", "project/math/137_probability_23/400_brownian/scene.py", "BrownianMotion"),
    Video(401, "モツキン数", "project/math/138_combinatorics_22/401_motzkin/scene.py", "Motzkin"),
)

VIDEOS_402_413: tuple[Video, ...] = (
    Video(402, "スペクトル測度", "project/math/139_analysis_26/402_spectral_measure/scene.py", "SpectralMeasure"),
    Video(403, "ダンフォード積分", "project/math/139_analysis_26/403_dunford/scene.py", "DunfordCalculus"),
    Video(404, "ボホナー積分", "project/math/139_analysis_26/404_bochner/scene.py", "BochnerIntegral"),
    Video(405, "ギブンス回転", "project/math/140_linear_26/405_givens/scene.py", "GivensRotation"),
    Video(406, "二対角化", "project/math/140_linear_26/406_bidiagonal/scene.py", "Bidiagonalization"),
    Video(407, "トレースクラス", "project/math/140_linear_26/407_trace_class/scene.py", "TraceClass"),
    Video(408, "パスカルの蝸牛線", "project/math/141_geometry_26/408_limacon/scene.py", "Limacon"),
    Video(409, "ソディの円", "project/math/141_geometry_26/409_soddy/scene.py", "SoddyCircles"),
    Video(410, "スチュワートの定理", "project/math/141_geometry_26/410_stewart/scene.py", "StewartTheorem"),
    Video(411, "大数の法則", "project/math/142_probability_24/411_lln/scene.py", "LawOfLargeNumbers"),
    Video(412, "中心極限定理", "project/math/142_probability_24/412_clt/scene.py", "CentralLimitTheorem"),
    Video(413, "ナラヤナ数", "project/math/143_combinatorics_23/413_narayana/scene.py", "Narayana"),
)

VIDEOS_414_425: tuple[Video, ...] = (
    Video(414, "スペクトル写像", "project/math/144_analysis_27/414_spectral_mapping/scene.py", "SpectralMapping"),
    Video(415, "カルキン代数", "project/math/144_analysis_27/415_calkin/scene.py", "CalkinAlgebra"),
    Video(416, "トーエプリッツ・ハウスドルフ", "project/math/144_analysis_27/416_toeplitz_hausdorff/scene.py", "ToeplitzHausdorff"),
    Video(417, "LSQR", "project/math/145_linear_27/417_lsqr/scene.py", "LSQR"),
    Video(418, "リッジ回帰", "project/math/145_linear_27/418_ridge/scene.py", "RidgeRegression"),
    Video(419, "特異値のワイル", "project/math/145_linear_27/419_weyl_svd/scene.py", "WeylSingular"),
    Video(420, "ファニャーノの問題", "project/math/146_geometry_27/420_fagnano/scene.py", "Fagnano"),
    Video(421, "共焦点", "project/math/146_geometry_27/421_confocal/scene.py", "Confocal"),
    Video(422, "正弦法則", "project/math/146_geometry_27/422_law_of_sines/scene.py", "LawOfSines"),
    Video(423, "任意停止定理", "project/math/147_probability_25/423_optional_stopping/scene.py", "OptionalStopping"),
    Video(424, "スコロホッド表現", "project/math/147_probability_25/424_skorokhod/scene.py", "Skorokhod"),
    Video(425, "デランノワ数", "project/math/148_combinatorics_24/425_delannoy/scene.py", "Delannoy"),
)

VIDEOS_426_437: tuple[Video, ...] = (
    Video(426, "スペクトル射影", "project/math/149_analysis_28/426_spectral_proj/scene.py", "SpectralProjection"),
    Video(427, "リゾルベント恒等式", "project/math/149_analysis_28/427_resolvent_id/scene.py", "ResolventIdentity"),
    Video(428, "ノルム位相", "project/math/149_analysis_28/428_norm_topology/scene.py", "NormTopology"),
    Video(429, "勾配降下", "project/math/150_linear_28/429_gradient_descent/scene.py", "GradientDescent"),
    Video(430, "ニュートン法", "project/math/150_linear_28/430_newton_opt/scene.py", "NewtonOptimization"),
    Video(431, "準ニュートン法", "project/math/150_linear_28/431_quasi_newton/scene.py", "QuasiNewton"),
    Video(432, "オイラーの四角形", "project/math/151_geometry_28/432_euler_quad/scene.py", "EulerQuadrilateral"),
    Video(433, "トレミーの不等式", "project/math/151_geometry_28/433_ptolemy_ineq/scene.py", "PtolemyInequality"),
    Video(434, "正弦面積", "project/math/151_geometry_28/434_sine_area/scene.py", "SineArea"),
    Video(435, "エルゴード分解", "project/math/152_probability_26/435_ergodic_decomp/scene.py", "ErgodicDecomposition"),
    Video(436, "ガウス過程", "project/math/152_probability_26/436_gaussian_process/scene.py", "GaussianProcess"),
    Video(437, "ラホール数", "project/math/153_combinatorics_25/437_lah/scene.py", "LahNumbers"),
)

VIDEOS_438_449: tuple[Video, ...] = (
    Video(438, "強作用素位相", "project/math/154_analysis_29/438_strong_op/scene.py", "StrongOperatorTopology"),
    Video(439, "コンパクトレゾルベント", "project/math/154_analysis_29/439_compact_resolvent/scene.py", "CompactResolvent"),
    Video(440, "スペクトルギャップ", "project/math/154_analysis_29/440_spectral_gap/scene.py", "SpectralGap"),
    Video(441, "ネステロフ加速", "project/math/155_linear_29/441_nesterov/scene.py", "Nesterov"),
    Video(442, "Adam", "project/math/155_linear_29/442_adam/scene.py", "Adam"),
    Video(443, "低ランク SVD", "project/math/155_linear_29/443_low_rank_svd/scene.py", "LowRankSVD"),
    Video(444, "余弦面積", "project/math/156_geometry_29/444_cosine_area/scene.py", "CosineArea"),
    Video(445, "ミケル枢軸", "project/math/156_geometry_29/445_miquel_pivot/scene.py", "MiquelPivot"),
    Video(446, "円内接の対角", "project/math/156_geometry_29/446_cyclic_diag/scene.py", "CyclicDiagonals"),
    Video(447, "ウィーナー測度", "project/math/157_probability_27/447_wiener/scene.py", "WienerMeasure"),
    Video(448, "ポアソン点過程", "project/math/157_probability_27/448_poisson_point/scene.py", "PoissonPointProcess"),
    Video(449, "シュレーダー数", "project/math/158_combinatorics_26/449_schroeder/scene.py", "Schroeder"),
)

VIDEOS_450_461: tuple[Video, ...] = (
    Video(450, "近似点スペクトル", "project/math/159_analysis_30/450_approx_point_spec/scene.py", "ApproxPointSpectrum"),
    Video(451, "フリードリヒス拡張", "project/math/159_analysis_30/451_friedrichs/scene.py", "FriedrichsExtension"),
    Video(452, "連続スペクトル", "project/math/159_analysis_30/452_continuous_spec/scene.py", "ContinuousSpectrum"),
    Video(453, "RMSProp", "project/math/160_linear_30/453_rmsprop/scene.py", "RMSProp"),
    Video(454, "ソフト閾値", "project/math/160_linear_30/454_soft_threshold/scene.py", "SoftThreshold"),
    Video(455, "行列モーメント", "project/math/160_linear_30/455_matrix_moments/scene.py", "MatrixMoments"),
    Video(456, "外接円半径", "project/math/161_geometry_30/456_circumradius/scene.py", "Circumradius"),
    Video(457, "オイラーの不等式", "project/math/161_geometry_30/457_euler_ineq/scene.py", "EulerInequality"),
    Video(458, "角の二等分線の長さ", "project/math/161_geometry_30/458_angle_bisector_len/scene.py", "AngleBisectorLength"),
    Video(459, "カプランマイヤー", "project/math/162_probability_28/459_kaplan_meier/scene.py", "KaplanMeier"),
    Video(460, "累積ハザード", "project/math/162_probability_28/460_cum_hazard/scene.py", "CumulativeHazard"),
    Video(461, "カッシーニの恒等式", "project/math/163_combinatorics_27/461_cassini/scene.py", "CassiniIdentity"),
)

VIDEOS_462_473: tuple[Video, ...] = (
    Video(462, "本質ノルム", "project/math/164_analysis_31/462_essential_norm/scene.py", "EssentialNorm"),
    Video(463, "Weyl列", "project/math/164_analysis_31/463_weyl_sequence/scene.py", "WeylSequence"),
    Video(464, "スペクトル族", "project/math/164_analysis_31/464_spectral_family/scene.py", "SpectralFamily"),
    Video(465, "L-BFGS", "project/math/165_linear_31/465_lbfgs/scene.py", "LBFGS"),
    Video(466, "座標降下", "project/math/165_linear_31/466_coord_descent/scene.py", "CoordinateDescent"),
    Video(467, "特異値縮小", "project/math/165_linear_31/467_svt/scene.py", "SingularValueThresholding"),
    Video(468, "中点三角形", "project/math/166_geometry_31/468_medial/scene.py", "MedialTriangle"),
    Video(469, "傍接円半径", "project/math/166_geometry_31/469_exradius/scene.py", "Exradius"),
    Video(470, "投影公式", "project/math/166_geometry_31/470_projection_formula/scene.py", "ProjectionFormula"),
    Video(471, "ワイブル分布", "project/math/167_probability_29/471_weibull/scene.py", "Weibull"),
    Video(472, "対数ランク検定", "project/math/167_probability_29/472_logrank/scene.py", "LogRank"),
    Video(473, "カタラン三角", "project/math/168_combinatorics_28/473_catalan_triangle/scene.py", "CatalanTriangle"),
)

VIDEOS_474_485: tuple[Video, ...] = (
    Video(474, "リゾルベント集合", "project/math/169_analysis_32/474_resolvent_set/scene.py", "ResolventSet"),
    Video(475, "ヒルベルト・シュミット", "project/math/169_analysis_32/475_hilbert_schmidt/scene.py", "HilbertSchmidt"),
    Video(476, "正規作用素", "project/math/169_analysis_32/476_normal_op/scene.py", "NormalOperator"),
    Video(477, "ADMM", "project/math/170_linear_32/477_admm/scene.py", "ADMM"),
    Video(478, "近接勾配", "project/math/170_linear_32/478_prox_grad/scene.py", "ProximalGradient"),
    Video(479, "行列補完", "project/math/170_linear_32/479_matrix_completion/scene.py", "MatrixCompletion"),
    Video(480, "ヴァン・オーベル", "project/math/171_geometry_32/480_van_obel/scene.py", "VanObel"),
    Video(481, "ブロシャール点", "project/math/171_geometry_32/481_brocard/scene.py", "BrocardPoint"),
    Video(482, "垂心三角形", "project/math/171_geometry_32/482_orthic/scene.py", "OrthicTriangle"),
    Video(483, "比例ハザード", "project/math/172_probability_30/483_prop_hazards/scene.py", "ProportionalHazards"),
    Video(484, "競合リスク", "project/math/172_probability_30/484_competing_risks/scene.py", "CompetingRisks"),
    Video(485, "ケイリーの公式", "project/math/173_combinatorics_29/485_cayley/scene.py", "CayleyFormula"),
)

VIDEOS_486_497: tuple[Video, ...] = (
    Video(486, "超弱作用素位相", "project/math/174_analysis_33/486_ultraweak/scene.py", "UltraweakTopology"),
    Video(487, "ストーンの定理", "project/math/174_analysis_33/487_stone/scene.py", "StonesTheorem"),
    Video(488, "ヒレ・吉田の定理", "project/math/174_analysis_33/488_hille_yosida/scene.py", "HilleYosida"),
    Video(489, "フランク・ウォルフェ", "project/math/175_linear_33/489_frank_wolfe/scene.py", "FrankWolfe"),
    Video(490, "鏡面降下", "project/math/175_linear_33/490_mirror_descent/scene.py", "MirrorDescent"),
    Video(491, "パワー法", "project/math/175_linear_33/491_power_method/scene.py", "PowerMethod"),
    Video(492, "シャールの定理", "project/math/176_geometry_33/492_chasles/scene.py", "ChaslesTheorem"),
    Video(493, "ナーゲル三角形", "project/math/176_geometry_33/493_nagel_tri/scene.py", "NagelTriangle"),
    Video(494, "ジェルゴンヌ三角形", "project/math/176_geometry_33/494_gergonne_tri/scene.py", "GergonneTriangle"),
    Video(495, "コックスモデル", "project/math/177_probability_31/495_cox/scene.py", "CoxModel"),
    Video(496, "フィルトレーション", "project/math/177_probability_31/496_filtration/scene.py", "Filtration"),
    Video(497, "包含排除原理", "project/math/178_combinatorics_30/497_inclusion_exclusion/scene.py", "InclusionExclusion"),
)

VIDEOS_498_509: tuple[Video, ...] = (
    Video(498, "フォンノイマン代数", "project/math/179_analysis_34/498_von_neumann/scene.py", "VonNeumannAlgebra"),
    Video(499, "ソボレフ埋蔵", "project/math/179_analysis_34/499_sobolev_embed/scene.py", "SobolevEmbedding"),
    Video(500, "カールソンの定理", "project/math/179_analysis_34/500_carleson/scene.py", "CarlesonTheorem"),
    Video(501, "CMA-ES", "project/math/180_linear_34/501_cmaes/scene.py", "CMAES"),
    Video(502, "部分空間反復", "project/math/180_linear_34/502_subspace_iter/scene.py", "SubspaceIteration"),
    Video(503, "ブロック座標", "project/math/180_linear_34/503_block_coord/scene.py", "BlockCoordinate"),
    Video(504, "パスカル線", "project/math/181_geometry_34/504_pascal_line/scene.py", "PascalLine"),
    Video(505, "チェバの拡張", "project/math/181_geometry_34/505_ceva_ext/scene.py", "CevaExtension"),
    Video(506, "剛性", "project/math/181_geometry_34/506_rigidity/scene.py", "Rigidity"),
    Video(507, "ネルソン・アーレン", "project/math/182_probability_32/507_nelson_aalen/scene.py", "NelsonAalen"),
    Video(508, "生存関数", "project/math/182_probability_32/508_survival/scene.py", "SurvivalFunction"),
    Video(509, "リュカ数", "project/math/183_combinatorics_31/509_lucas/scene.py", "LucasNumbers"),
)

VIDEOS_510_521: tuple[Video, ...] = (
    Video(510, "冨田竹崎", "project/math/184_analysis_35/510_tomita_takesaki/scene.py", "TomitaTakesaki"),
    Video(511, "モジュラー理論", "project/math/184_analysis_35/511_modular/scene.py", "ModularTheory"),
    Video(512, "リース・ソーリン", "project/math/184_analysis_35/512_riesz_thorin/scene.py", "RieszThorin"),
    Video(513, "MINRES", "project/math/185_linear_35/513_minres/scene.py", "MINRES"),
    Video(514, "BiCGSTAB", "project/math/185_linear_35/514_bicgstab/scene.py", "BiCGSTAB"),
    Video(515, "ヘッセフリー", "project/math/185_linear_35/515_hessian_free/scene.py", "HessianFree"),
    Video(516, "メネラウスの拡張", "project/math/186_geometry_35/516_menelaus_ext/scene.py", "MenelausExtension"),
    Video(517, "等長変形", "project/math/186_geometry_35/517_isometric/scene.py", "IsometricDeformation"),
    Video(518, "等角共役三角形", "project/math/186_geometry_35/518_isogonic/scene.py", "IsogonalTriangle"),
    Video(519, "強度関数", "project/math/187_probability_33/519_intensity/scene.py", "IntensityFunction"),
    Video(520, "ガウス測度", "project/math/187_probability_33/520_gaussian_measure/scene.py", "GaussianMeasure"),
    Video(521, "フェラーズ図", "project/math/188_combinatorics_32/521_ferrers/scene.py", "FerrersDiagram"),
)

VIDEOS_522_533: tuple[Video, ...] = (
    Video(522, "II1因子", "project/math/189_analysis_36/522_ii1/scene.py", "II1Factor"),
    Video(523, "弱収束", "project/math/189_analysis_36/523_weak_conv/scene.py", "WeakConvergence"),
    Video(524, "マルチンケヴィッチ", "project/math/189_analysis_36/524_marcinkiewicz/scene.py", "Marcinkiewicz"),
    Video(525, "共役残差", "project/math/190_linear_36/525_conjugate_residual/scene.py", "ConjugateResidual"),
    Video(526, "自然勾配法", "project/math/190_linear_36/526_natural_grad/scene.py", "NaturalGradient"),
    Video(527, "逆冪乗法", "project/math/190_linear_36/527_inverse_power/scene.py", "InversePower"),
    Video(528, "パスカルの六角形", "project/math/191_geometry_36/528_pascal_hex/scene.py", "PascalHexagon"),
    Video(529, "接弦の長さ比", "project/math/191_geometry_36/529_tangent_chord_ratio/scene.py", "TangentChordRatio"),
    Video(530, "三角形の剛性", "project/math/191_geometry_36/530_triangle_rigidity/scene.py", "TriangleRigidity"),
    Video(531, "累積強度", "project/math/192_probability_34/531_cum_intensity/scene.py", "CumulativeIntensity"),
    Video(532, "点過程強度", "project/math/192_probability_34/532_pp_intensity/scene.py", "PointProcessIntensity"),
    Video(533, "トリボナッチ", "project/math/193_combinatorics_33/533_tribonacci/scene.py", "Tribonacci"),
)

VIDEOS_534_545: tuple[Video, ...] = (
    Video(534, "強収束", "project/math/194_analysis_37/534_strong_conv/scene.py", "StrongConvergence"),
    Video(535, "カルデロン・ジグムント", "project/math/194_analysis_37/535_calderon/scene.py", "CalderonZygmund"),
    Video(536, "特異積分", "project/math/194_analysis_37/536_singular_integral/scene.py", "SingularIntegral"),
    Video(537, "前処理付きCG", "project/math/195_linear_37/537_pcg/scene.py", "PreconditionedCG"),
    Video(538, "多グリッド", "project/math/195_linear_37/538_multigrid/scene.py", "Multigrid"),
    Video(539, "CGS", "project/math/195_linear_37/539_cgs/scene.py", "CGS"),
    Video(540, "ブリアンション六角形", "project/math/196_geometry_37/540_brianchon_hex/scene.py", "BrianchonHexagon"),
    Video(541, "垂心六角形", "project/math/196_geometry_37/541_orthic_hex/scene.py", "OrthicHexagon"),
    Video(542, "共円条件", "project/math/196_geometry_37/542_concyclic/scene.py", "ConcyclicCondition"),
    Video(543, "ホーケス過程", "project/math/197_probability_35/543_hawkes/scene.py", "HawkesProcess"),
    Video(544, "自己励起過程", "project/math/197_probability_35/544_self_exciting/scene.py", "SelfExciting"),
    Video(545, "パッドヴァン", "project/math/198_combinatorics_34/545_padovan/scene.py", "Padovan"),
)

VIDEOS_546_557: tuple[Video, ...] = (
    Video(546, "バナッハ極限", "project/math/199_analysis_38/546_banach_limit/scene.py", "BanachLimit"),
    Video(547, "極大関数", "project/math/199_analysis_38/547_maximal/scene.py", "MaximalFunction"),
    Video(548, "リトルウッド・ペイリー", "project/math/199_analysis_38/548_littlewood_paley/scene.py", "LittlewoodPaley"),
    Video(549, "GMRES再スタート", "project/math/200_linear_38/549_gmres_restart/scene.py", "GMRESRestart"),
    Video(550, "領域分割", "project/math/200_linear_38/550_domain_decomp/scene.py", "DomainDecomposition"),
    Video(551, "多色SOR", "project/math/200_linear_38/551_multicolor_sor/scene.py", "MulticolorSOR"),
    Video(552, "トレミーの一般化", "project/math/201_geometry_38/552_ptolemy_gen/scene.py", "PtolemyGeneral"),
    Video(553, "モザーの円", "project/math/201_geometry_38/553_moser_circle/scene.py", "MoserCircle"),
    Video(554, "極と極線", "project/math/201_geometry_38/554_pole_polar/scene.py", "PolePolar"),
    Video(555, "補償マルチンゲール", "project/math/202_probability_36/555_compensated/scene.py", "CompensatedMartingale"),
    Video(556, "ハフ変換", "project/math/202_probability_36/556_hough/scene.py", "HoughTransform"),
    Video(557, "平面木", "project/math/203_combinatorics_35/557_plane_trees/scene.py", "PlaneTrees"),
)

VIDEOS_558_569: tuple[Video, ...] = (
    Video(558, "BMO空間", "project/math/204_analysis_39/558_bmo/scene.py", "BMOSpace"),
    Video(559, "振幅作用素", "project/math/204_analysis_39/559_amplitude/scene.py", "AmplitudeOperator"),
    Video(560, "パラプロダクト", "project/math/204_analysis_39/560_paraproduct/scene.py", "Paraproduct"),
    Video(561, "不完全コレスキー", "project/math/205_linear_39/561_ichol/scene.py", "IncompleteCholesky"),
    Video(562, "ヤコビ前処理", "project/math/205_linear_39/562_jacobi_pre/scene.py", "JacobiPreconditioner"),
    Video(563, "代数的多重グリッド", "project/math/205_linear_39/563_amg/scene.py", "AlgebraicMultigrid"),
    Video(564, "共役直径", "project/math/206_geometry_39/564_conjugate_diameters/scene.py", "ConjugateDiameters"),
    Video(565, "焦点弦", "project/math/206_geometry_39/565_focal_chord/scene.py", "FocalChord"),
    Video(566, "配景の中心", "project/math/206_geometry_39/566_perspector/scene.py", "Perspector"),
    Video(567, "コックス過程", "project/math/207_probability_37/567_cox_process/scene.py", "CoxProcess"),
    Video(568, "マーク付き点過程", "project/math/207_probability_37/568_marked_pp/scene.py", "MarkedPointProcess"),
    Video(569, "整数の分割", "project/math/208_combinatorics_36/569_integer_partitions/scene.py", "IntegerPartitions"),
)

VIDEOS_570_581: tuple[Video, ...] = (
    Video(570, "ハードスペース", "project/math/209_analysis_40/570_hardy/scene.py", "HardySpace"),
    Video(571, "T1定理", "project/math/209_analysis_40/571_t1/scene.py", "T1Theorem"),
    Video(572, "ウェーブレット", "project/math/209_analysis_40/572_wavelet/scene.py", "Wavelet"),
    Video(573, "ILU", "project/math/210_linear_40/573_ilu/scene.py", "ILU"),
    Video(574, "SSOR", "project/math/210_linear_40/574_ssor/scene.py", "SSOR"),
    Video(575, "ガウス・ザイデル前処理", "project/math/210_linear_40/575_gs_pre/scene.py", "GaussSeidelPre"),
    Video(576, "直角双曲線", "project/math/211_geometry_40/576_rect_hyperbola/scene.py", "RectangularHyperbola"),
    Video(577, "配景軸", "project/math/211_geometry_40/577_perspective_axis/scene.py", "PerspectiveAxis"),
    Video(578, "極三角形", "project/math/211_geometry_40/578_polar_triangle/scene.py", "PolarTriangle"),
    Video(579, "決定点過程", "project/math/212_probability_38/579_determinantal/scene.py", "DeterminantalPP"),
    Video(580, "クラスター点過程", "project/math/212_probability_38/580_cluster_pp/scene.py", "ClusterPointProcess"),
    Video(581, "根付き木", "project/math/213_combinatorics_37/581_rooted_trees/scene.py", "RootedTrees"),
)

VIDEOS_582_593: tuple[Video, ...] = (
    Video(582, "カルデロン交換子", "project/math/214_analysis_41/582_calderon_comm/scene.py", "CalderonCommutator"),
    Video(583, "擬微分作用素", "project/math/214_analysis_41/583_pdo/scene.py", "Pseudodifferential"),
    Video(584, "ベゾフ空間", "project/math/214_analysis_41/584_besov/scene.py", "BesovSpace"),
    Video(585, "シューア補完反復", "project/math/215_linear_41/585_schur_iter/scene.py", "SchurComplementIter"),
    Video(586, "クレイロフ再利用", "project/math/215_linear_41/586_krylov_recycle/scene.py", "KrylovRecycling"),
    Video(587, "領域分解前処理", "project/math/215_linear_41/587_dd_pre/scene.py", "DomainDecompPre"),
    Video(588, "双曲線の焦点", "project/math/216_geometry_41/588_hyperbola_foci/scene.py", "HyperbolaFoci"),
    Video(589, "楕円の導円", "project/math/216_geometry_41/589_director_circle/scene.py", "DirectorCircle"),
    Video(590, "準線", "project/math/216_geometry_41/590_directrix/scene.py", "Directrix"),
    Video(591, "ギッブス過程", "project/math/217_probability_39/591_gibbs/scene.py", "GibbsProcess"),
    Video(592, "ストリング過程", "project/math/217_probability_39/592_string/scene.py", "StringProcess"),
    Video(593, "モザー数", "project/math/218_combinatorics_38/593_moser_number/scene.py", "MoserNumber"),
)

VIDEOS_594_605: tuple[Video, ...] = (
    Video(594, "フーリエ積分作用素", "project/math/219_analysis_42/594_fio/scene.py", "FourierIntegralOp"),
    Video(595, "波動前線", "project/math/219_analysis_42/595_wavefront/scene.py", "WavefrontSet"),
    Video(596, "ミクロローカル", "project/math/219_analysis_42/596_microlocal/scene.py", "Microlocal"),
    Video(597, "拘束付きCG", "project/math/220_linear_42/597_constrained_cg/scene.py", "ConstrainedCG"),
    Video(598, "射影法", "project/math/220_linear_42/598_projection_method/scene.py", "ProjectionMethod"),
    Video(599, "ブロックILU", "project/math/220_linear_42/599_block_ilu/scene.py", "BlockILU"),
    Video(600, "離心率", "project/math/221_geometry_42/600_eccentricity/scene.py", "Eccentricity"),
    Video(601, "楕円のパラメータ", "project/math/221_geometry_42/601_ellipse_param/scene.py", "EllipseParam"),
    Video(602, "双曲線の漸近線", "project/math/221_geometry_42/602_hyperbola_asymp/scene.py", "HyperbolaAsymptotes"),
    Video(603, "ショットノイズ", "project/math/222_probability_40/603_shot_noise/scene.py", "ShotNoise"),
    Video(604, "マーク強度", "project/math/222_probability_40/604_mark_intensity/scene.py", "MarkIntensity"),
    Video(605, "セット分割", "project/math/223_combinatorics_39/605_set_partitions/scene.py", "SetPartitions"),
)

VIDEOS_606_617: tuple[Video, ...] = (
    Video(606, "可制御性", "project/math/224_analysis_43/606_controllability/scene.py", "Controllability"),
    Video(607, "可観測性", "project/math/224_analysis_43/607_observability/scene.py", "Observability"),
    Video(608, "一意接続性", "project/math/224_analysis_43/608_unique_cont/scene.py", "UniqueContinuation"),
    Video(609, "BFGS", "project/math/225_linear_43/609_bfgs/scene.py", "BFGS"),
    Video(610, "DFP法", "project/math/225_linear_43/610_dfp/scene.py", "DFP"),
    Video(611, "信頼領域法", "project/math/225_linear_43/611_trust_region/scene.py", "TrustRegion"),
    Video(612, "放物線の定義", "project/math/226_geometry_43/612_parabola_def/scene.py", "ParabolaDefinition"),
    Video(613, "放物線の反射", "project/math/226_geometry_43/613_parabola_refl/scene.py", "ParabolaReflection"),
    Video(614, "通径", "project/math/226_geometry_43/614_latus_rectum/scene.py", "LatusRectum"),
    Video(615, "パーム分布", "project/math/227_probability_41/615_palm/scene.py", "PalmDistribution"),
    Video(616, "キャンベル公式", "project/math/227_probability_41/616_campbell/scene.py", "CampbellFormula"),
    Video(617, "順序ベル数", "project/math/228_combinatorics_40/617_ordered_bell/scene.py", "OrderedBell"),
)

VIDEOS_618_629: tuple[Video, ...] = (
    Video(618, "可安定化", "project/math/229_analysis_44/618_stabilizability/scene.py", "Stabilizability"),
    Video(619, "可検出性", "project/math/229_analysis_44/619_detectability/scene.py", "Detectability"),
    Video(620, "LQR", "project/math/229_analysis_44/620_lqr/scene.py", "LQR"),
    Video(621, "ドッグレッグ", "project/math/230_linear_44/621_dogleg/scene.py", "Dogleg"),
    Video(622, "ガウス・ニュートン", "project/math/230_linear_44/622_gauss_newton/scene.py", "GaussNewton"),
    Video(623, "ウルフ条件", "project/math/230_linear_44/623_wolfe/scene.py", "WolfeConditions"),
    Video(624, "楕円の反射", "project/math/231_geometry_44/624_ellipse_refl/scene.py", "EllipseReflection"),
    Video(625, "双曲線の反射", "project/math/231_geometry_44/625_hyperbola_refl/scene.py", "HyperbolaReflection"),
    Video(626, "補助円", "project/math/231_geometry_44/626_aux_circle/scene.py", "AuxiliaryCircle"),
    Video(627, "リプリーのK", "project/math/232_probability_42/627_ripley/scene.py", "RipleyK"),
    Video(628, "ペア相関", "project/math/232_probability_42/628_pair_corr/scene.py", "PairCorrelation"),
    Video(629, "電話番号", "project/math/233_combinatorics_41/629_telephone/scene.py", "TelephoneNumbers"),
)

VIDEOS_630_641: tuple[Video, ...] = (
    Video(630, "ポントリャーギン", "project/math/234_analysis_45/630_pontryagin/scene.py", "Pontryagin"),
    Video(631, "ハミルトン・ヤコビ", "project/math/234_analysis_45/631_hjb/scene.py", "HJB"),
    Video(632, "ベルマン最適性", "project/math/234_analysis_45/632_bellman/scene.py", "BellmanOpt"),
    Video(633, "レーベンバーグ", "project/math/235_linear_45/633_levenberg/scene.py", "LevenbergMarquardt"),
    Video(634, "非線形CG", "project/math/235_linear_45/634_nlcg/scene.py", "NonlinearCG"),
    Video(635, "バルジライ・ボーウェイン", "project/math/235_linear_45/635_bb/scene.py", "BarzilaiBorwein"),
    Video(636, "円の反転", "project/math/236_geometry_45/636_inversion/scene.py", "CircleInversion"),
    Video(637, "ホモセティ", "project/math/236_geometry_45/637_homothety/scene.py", "Homothety"),
    Video(638, "相似の中心", "project/math/236_geometry_45/638_similitude/scene.py", "CenterOfSimilitude"),
    Video(639, "ボイド確率", "project/math/237_probability_43/639_void/scene.py", "VoidProbability"),
    Video(640, "空き空間関数", "project/math/237_probability_43/640_empty_space/scene.py", "EmptySpaceF"),
    Video(641, "リオルダン数", "project/math/238_combinatorics_42/641_riordan/scene.py", "RiordanNumbers"),
)

VIDEOS_642_653: tuple[Video, ...] = (
    Video(642, "粘性解", "project/math/239_analysis_46/642_viscosity/scene.py", "ViscositySolution"),
    Video(643, "比較原理", "project/math/239_analysis_46/643_comparison/scene.py", "ComparisonPrinciple"),
    Video(644, "クランダル・ライオンズ", "project/math/239_analysis_46/644_crandall/scene.py", "CrandallLions"),
    Video(645, "ヘビーボール", "project/math/240_linear_46/645_heavy_ball/scene.py", "HeavyBall"),
    Video(646, "モーメンタム", "project/math/240_linear_46/646_momentum/scene.py", "MomentumSGD"),
    Video(647, "AdaGrad", "project/math/240_linear_46/647_adagrad/scene.py", "AdaGrad"),
    Video(648, "シュタイナー楕円", "project/math/241_geometry_46/648_steiner_ell/scene.py", "SteinerEllipse"),
    Video(649, "マンダール楕円", "project/math/241_geometry_46/649_mandart/scene.py", "MandartInellipse"),
    Video(650, "傍接点三角形", "project/math/241_geometry_46/650_extouch/scene.py", "ExtouchTriangle"),
    Video(651, "最近傍関数", "project/math/242_probability_44/651_nn_g/scene.py", "NearestNeighborG"),
    Video(652, "J関数", "project/math/242_probability_44/652_j_func/scene.py", "JFunction"),
    Video(653, "オイラーアリアン数", "project/math/243_combinatorics_43/653_eulerian/scene.py", "EulerianNumbers"),
)

VIDEOS_654_665: tuple[Video, ...] = (
    Video(654, "エヴァンス・クリロフ", "project/math/244_analysis_47/654_evans_krylov/scene.py", "EvansKrylov"),
    Video(655, "アイザック方程式", "project/math/244_analysis_47/655_isaacs/scene.py", "IsaacsEquation"),
    Video(656, "平均場ゲーム", "project/math/244_analysis_47/656_mfg/scene.py", "MeanFieldGame"),
    Video(657, "AdamW", "project/math/245_linear_47/657_adamw/scene.py", "AdamW"),
    Video(658, "Lookahead", "project/math/245_linear_47/658_lookahead/scene.py", "Lookahead"),
    Video(659, "SAM", "project/math/245_linear_47/659_sam/scene.py", "SAM"),
    Video(660, "シュピーカー中心", "project/math/246_geometry_47/660_spieker/scene.py", "SpiekerCenter"),
    Video(661, "ミッテンプンクト", "project/math/246_geometry_47/661_mittenpunkt/scene.py", "Mittenpunkt"),
    Video(662, "類似中線点", "project/math/246_geometry_47/662_symmedian/scene.py", "SymmedianPoint"),
    Video(663, "L関数", "project/math/247_probability_45/663_l_func/scene.py", "LFunction"),
    Video(664, "マーク相関", "project/math/247_probability_45/664_mark_corr/scene.py", "MarkCorrelation"),
    Video(665, "交替順列", "project/math/248_combinatorics_44/665_alternating/scene.py", "AlternatingPermutations"),
)

VIDEOS_666_677: tuple[Video, ...] = (
    Video(666, "平均曲率流", "project/math/249_analysis_48/666_mcf/scene.py", "MeanCurvatureFlow"),
    Video(667, "リッチ流", "project/math/249_analysis_48/667_ricci/scene.py", "RicciFlow"),
    Video(668, "ヤマベ問題", "project/math/249_analysis_48/668_yamabe/scene.py", "YamabeProblem"),
    Video(669, "Lion", "project/math/250_linear_48/669_lion/scene.py", "LionOptimizer"),
    Video(670, "学習率スケジュール", "project/math/250_linear_48/670_lr_schedule/scene.py", "LRSchedule"),
    Video(671, "ウォームアップ", "project/math/250_linear_48/671_warmup/scene.py", "Warmup"),
    Video(672, "第二等角中心", "project/math/251_geometry_48/672_second_isogonic/scene.py", "SecondIsogonicCenter"),
    Video(673, "外心中点三角形", "project/math/251_geometry_48/673_circummedial/scene.py", "CircummedialTriangle"),
    Video(674, "第一等角中心", "project/math/251_geometry_48/674_first_isogonic/scene.py", "FirstIsogonicCenter"),
    Video(675, "積密度", "project/math/252_probability_46/675_product_density/scene.py", "ProductDensity"),
    Video(676, "階乗モーメント測度", "project/math/252_probability_46/676_factorial_moment/scene.py", "FactorialMoment"),
    Video(677, "エントリンガー数", "project/math/253_combinatorics_45/677_entringer/scene.py", "EntringerNumbers"),
)

VIDEOS_678_689: tuple[Video, ...] = (
    Video(678, "調和写像", "project/math/254_analysis_49/678_harmonic_map/scene.py", "HarmonicMap"),
    Video(679, "ヤン・ミルズ", "project/math/254_analysis_49/679_yang_mills/scene.py", "YangMills"),
    Video(680, "ゲージ理論", "project/math/254_analysis_49/680_gauge/scene.py", "GaugeTheory"),
    Video(681, "勾配クリッピング", "project/math/255_linear_49/681_grad_clip/scene.py", "GradientClipping"),
    Video(682, "スケジュールフリー", "project/math/255_linear_49/682_schedule_free/scene.py", "ScheduleFree"),
    Video(683, "SWA", "project/math/255_linear_49/683_swa/scene.py", "SWA"),
    Video(684, "ブロカール点", "project/math/256_geometry_49/684_brocard/scene.py", "BrocardPoint"),
    Video(685, "ブロカール角", "project/math/256_geometry_49/685_brocard_angle/scene.py", "BrocardAngle"),
    Video(686, "ブロカール円", "project/math/256_geometry_49/686_brocard_circle/scene.py", "BrocardCircle"),
    Video(687, "生成汎関数", "project/math/257_probability_47/687_pgf/scene.py", "GeneratingFunctional"),
    Video(688, "ラプラス汎関数", "project/math/257_probability_47/688_laplace_func/scene.py", "LaplaceFunctional"),
    Video(689, "セイデル数", "project/math/258_combinatorics_46/689_seidel/scene.py", "SeidelNumbers"),
)

VIDEOS_690_701: tuple[Video, ...] = (
    Video(690, "チャーン・サイモンズ", "project/math/259_analysis_50/690_chern_simons/scene.py", "ChernSimons"),
    Video(691, "インスタントン", "project/math/259_analysis_50/691_instanton/scene.py", "Instanton"),
    Video(692, "ヒッグス機構", "project/math/259_analysis_50/692_higgs/scene.py", "HiggsMechanism"),
    Video(693, "EMA", "project/math/260_linear_50/693_ema/scene.py", "EMA"),
    Video(694, "ポリアック平均", "project/math/260_linear_50/694_polyak_avg/scene.py", "PolyakAveraging"),
    Video(695, "モデルスープ", "project/math/260_linear_50/695_model_soup/scene.py", "ModelSoup"),
    Video(696, "第二ブロカール点", "project/math/261_geometry_50/696_second_brocard/scene.py", "SecondBrocardPoint"),
    Video(697, "ブロカール三角形", "project/math/261_geometry_50/697_brocard_tri/scene.py", "BrocardTriangle"),
    Video(698, "ブロカールのポリズム", "project/math/261_geometry_50/698_brocard_porism/scene.py", "BrocardPorism"),
    Video(699, "キャンベル・メッケ", "project/math/262_probability_48/699_campbell_mecke/scene.py", "CampbellMecke"),
    Video(700, "確率母関数", "project/math/262_probability_48/700_pgf/scene.py", "PGF"),
    Video(701, "ジェノッキ数", "project/math/263_combinatorics_47/701_genocchi/scene.py", "GenocchiNumbers"),
)

VIDEOS_702_713: tuple[Video, ...] = (
    Video(702, "ドナルドソン理論", "project/math/264_analysis_51/702_donaldson/scene.py", "DonaldsonTheory"),
    Video(703, "サイバーグ・ウィッテン", "project/math/264_analysis_51/703_seiberg_witten/scene.py", "SeibergWitten"),
    Video(704, "フローアホモロジー", "project/math/264_analysis_51/704_floer/scene.py", "FloerHomology"),
    Video(705, "RAdam", "project/math/265_linear_51/705_radam/scene.py", "RAdam"),
    Video(706, "AdaBelief", "project/math/265_linear_51/706_adabelief/scene.py", "AdaBelief"),
    Video(707, "DiffGrad", "project/math/265_linear_51/707_diffgrad/scene.py", "DiffGrad"),
    Video(708, "ルモワーヌ円", "project/math/266_geometry_51/708_lemoine_circle/scene.py", "LemoineCircle"),
    Video(709, "内側ナポレオン", "project/math/266_geometry_51/709_inner_napoleon/scene.py", "InnerNapoleon"),
    Video(710, "ブロカール中点", "project/math/266_geometry_51/710_brocard_mid/scene.py", "BrocardMidpoint"),
    Video(711, "特性汎関数", "project/math/267_probability_49/711_char_func/scene.py", "CharacteristicFunctional"),
    Video(712, "モーメント母汎関数", "project/math/267_probability_49/712_mgf_func/scene.py", "MomentGeneratingFunctional"),
    Video(713, "スプリンガー数", "project/math/268_combinatorics_48/713_springer/scene.py", "SpringerNumbers"),
)

VIDEOS_714_725: tuple[Video, ...] = (
    Video(714, "グロモフ・ウィッテン", "project/math/269_analysis_52/714_gromov_witten/scene.py", "GromovWitten"),
    Video(715, "深谷圏", "project/math/269_analysis_52/715_fukaya/scene.py", "FukayaCategory"),
    Video(716, "ミラー対称性", "project/math/269_analysis_52/716_mirror/scene.py", "MirrorSymmetry"),
    Video(717, "LAMB", "project/math/270_linear_52/717_lamb/scene.py", "LAMB"),
    Video(718, "AdaBound", "project/math/270_linear_52/718_adabound/scene.py", "AdaBound"),
    Video(719, "Yogi", "project/math/270_linear_52/719_yogi/scene.py", "Yogi"),
    Video(720, "外側ナポレオン", "project/math/271_geometry_52/720_outer_napoleon/scene.py", "OuterNapoleon"),
    Video(721, "テーラー円", "project/math/271_geometry_52/721_taylor_circle/scene.py", "TaylorCircle"),
    Video(722, "余弦円", "project/math/271_geometry_52/722_cosine_circle/scene.py", "CosineCircle"),
    Video(723, "ヤノッシ密度", "project/math/272_probability_50/723_janossy/scene.py", "JanossyDensity"),
    Video(724, "縮小パーム", "project/math/272_probability_50/724_reduced_palm/scene.py", "ReducedPalm"),
    Video(725, "ウィソフ配列", "project/math/273_combinatorics_49/725_wythoff/scene.py", "WythoffArray"),
)

VIDEOS_726_737: tuple[Video, ...] = (
    Video(726, "ホモロジカルミラー", "project/math/274_analysis_53/726_homological_mirror/scene.py", "HomologicalMirror"),
    Video(727, "SYZ予想", "project/math/274_analysis_53/727_syz/scene.py", "SYZConjecture"),
    Video(728, "量子コホモロジー", "project/math/274_analysis_53/728_quantum_cohomology/scene.py", "QuantumCohomology"),
    Video(729, "Prodigy", "project/math/275_linear_53/729_prodigy/scene.py", "Prodigy"),
    Video(730, "NovoGrad", "project/math/275_linear_53/730_novograd/scene.py", "NovoGrad"),
    Video(731, "Ranger", "project/math/275_linear_53/731_ranger/scene.py", "Ranger"),
    Video(732, "ジョンソン円", "project/math/276_geometry_53/732_johnson/scene.py", "JohnsonCircle"),
    Video(733, "第2ルモワーヌ円", "project/math/276_geometry_53/733_second_lemoine/scene.py", "SecondLemoineCircle"),
    Video(734, "三重比円", "project/math/276_geometry_53/734_triplicate/scene.py", "TriplicateRatioCircle"),
    Video(735, "パパンゲルー強度", "project/math/277_probability_51/735_papangelou/scene.py", "PapangelouIntensity"),
    Video(736, "相関ヒストグラム", "project/math/277_probability_51/736_correlation_hist/scene.py", "CorrelationHistogram"),
    Video(737, "ホフスタッター数列", "project/math/278_combinatorics_50/737_hofstadter/scene.py", "HofstadterSequence"),
)

VIDEOS_738_749: tuple[Video, ...] = (
    Video(738, "導来圏", "project/math/279_analysis_54/738_derived_cat/scene.py", "DerivedCategory"),
    Video(739, "ブリッジランド安定性", "project/math/279_analysis_54/739_bridgeland/scene.py", "BridgelandStability"),
    Video(740, "t構造の心", "project/math/279_analysis_54/740_heart/scene.py", "HeartOfTStructure"),
    Video(741, "Sophia", "project/math/280_linear_54/741_sophia/scene.py", "Sophia"),
    Video(742, "AdaFactor", "project/math/280_linear_54/742_adafactor/scene.py", "AdaFactor"),
    Video(743, "MADGRAD", "project/math/280_linear_54/743_madgrad/scene.py", "MADGRAD"),
    Video(744, "ベヴァン点", "project/math/281_geometry_54/744_bevan/scene.py", "BevanPoint"),
    Video(745, "シュピーカー円", "project/math/281_geometry_54/745_spieker_circle/scene.py", "SpiekerCircle"),
    Video(746, "マンダール円", "project/math/281_geometry_54/746_mandart_circle/scene.py", "MandartCircle"),
    Video(747, "端補正", "project/math/282_probability_52/747_edge_correction/scene.py", "EdgeCorrection"),
    Video(748, "縮小二次モーメント", "project/math/282_probability_52/748_reduced_second/scene.py", "ReducedSecondMoment"),
    Video(749, "ペル数", "project/math/283_combinatorics_51/749_pell/scene.py", "PellNumbers"),
)

VIDEOS_750_761: tuple[Video, ...] = (
    Video(750, "傾き安定性", "project/math/284_analysis_55/750_tilt/scene.py", "TiltStability"),
    Video(751, "DT不変量", "project/math/284_analysis_55/751_dt/scene.py", "DTInvariant"),
    Video(752, "ドナルドソン・トーマス", "project/math/284_analysis_55/752_donaldson_thomas/scene.py", "DonaldsonThomas"),
    Video(753, "LARS", "project/math/285_linear_55/753_lars/scene.py", "LARS"),
    Video(754, "Fromage", "project/math/285_linear_55/754_fromage/scene.py", "Fromage"),
    Video(755, "Apollo", "project/math/285_linear_55/755_apollo/scene.py", "Apollo"),
    Video(756, "コンウェイ円", "project/math/286_geometry_55/756_conway_circle/scene.py", "ConwayCircle"),
    Video(757, "イフ中心", "project/math/286_geometry_55/757_yff/scene.py", "YffCenter"),
    Video(758, "等脚中線点", "project/math/286_geometry_55/758_isoscelizers/scene.py", "IsoscelizersPoint"),
    Video(759, "ハードコア過程", "project/math/287_probability_53/759_hard_core/scene.py", "HardCoreProcess"),
    Video(760, "ソフトコア過程", "project/math/287_probability_53/760_soft_core/scene.py", "SoftCoreProcess"),
    Video(761, "ペル・リュカ数", "project/math/288_combinatorics_52/761_pell_lucas/scene.py", "PellLucasNumbers"),
)

VIDEOS_762_773: tuple[Video, ...] = (
    Video(762, "PT不変量", "project/math/289_analysis_56/762_pt/scene.py", "PTInvariant"),
    Video(763, "ゴパクマール・ヴァーファ", "project/math/289_analysis_56/763_gv/scene.py", "GopakumarVafa"),
    Video(764, "GW-DT対応", "project/math/289_analysis_56/764_gwdt/scene.py", "GWDTCorrespondence"),
    Video(765, "Shampoo", "project/math/290_linear_56/765_shampoo/scene.py", "Shampoo"),
    Video(766, "Adai", "project/math/290_linear_56/766_adai/scene.py", "Adai"),
    Video(767, "Padam", "project/math/290_linear_56/767_padam/scene.py", "Padam"),
    Video(768, "モーリー三角形", "project/math/291_geometry_56/768_morley/scene.py", "MorleyTriangle"),
    Video(769, "コスニタ点", "project/math/291_geometry_56/769_kosnita/scene.py", "KosnitaPoint"),
    Video(770, "エクセター点", "project/math/291_geometry_56/770_exeter/scene.py", "ExeterPoint"),
    Video(771, "シュトラウス過程", "project/math/292_probability_54/771_strauss/scene.py", "StraussProcess"),
    Video(772, "面積相互作用", "project/math/292_probability_54/772_area_interaction/scene.py", "AreaInteraction"),
    Video(773, "怠惰な料理人", "project/math/293_combinatorics_53/773_lazy_caterer/scene.py", "LazyCaterer"),
)

VIDEOS_774_785: tuple[Video, ...] = (
    Video(774, "安定写像", "project/math/294_analysis_57/774_stable_maps/scene.py", "StableMaps"),
    Video(775, "仮想基本類", "project/math/294_analysis_57/775_virtual_class/scene.py", "VirtualClass"),
    Video(776, "安定対", "project/math/294_analysis_57/776_stable_pairs/scene.py", "StablePairs"),
    Video(777, "ASAM", "project/math/295_linear_57/777_asam/scene.py", "ASAM"),
    Video(778, "Muon", "project/math/295_linear_57/778_muon/scene.py", "Muon"),
    Video(779, "SOAP", "project/math/295_linear_57/779_soap/scene.py", "SOAP"),
    Video(780, "シュピーカー点", "project/math/296_geometry_57/780_spieker/scene.py", "SpiekerCenter"),
    Video(781, "フォイエルバッハ点", "project/math/296_geometry_57/781_feuerbach/scene.py", "FeuerbachPoint"),
    Video(782, "デロングシャン点", "project/math/296_geometry_57/782_delongchamps/scene.py", "DeLongchampsPoint"),
    Video(783, "ギブス点過程", "project/math/297_probability_55/783_gibbs/scene.py", "GibbsPointProcess"),
    Video(784, "パーマネント過程", "project/math/297_probability_55/784_permanental/scene.py", "PermanentalProcess"),
    Video(785, "ケーキ数", "project/math/298_combinatorics_54/785_cake/scene.py", "CakeNumbers"),
)

VIDEOS_786_797: tuple[Video, ...] = (
    Video(786, "相対GW", "project/math/299_analysis_58/786_relative_gw/scene.py", "RelativeGW"),
    Video(787, "開GW", "project/math/299_analysis_58/787_open_gw/scene.py", "OpenGW"),
    Video(788, "ログGW", "project/math/299_analysis_58/788_log_gw/scene.py", "LogGW"),
    Video(789, "Schedule-Free", "project/math/300_linear_58/789_schedule_free/scene.py", "ScheduleFree"),
    Video(790, "Adopt", "project/math/300_linear_58/790_adopt/scene.py", "Adopt"),
    Video(791, "MARS", "project/math/300_linear_58/791_mars/scene.py", "MARS"),
    Video(792, "タルボット点", "project/math/301_geometry_58/792_talbot/scene.py", "TalbotPoint"),
    Video(793, "アポロニウス点", "project/math/301_geometry_58/793_apollonius/scene.py", "ApolloniusPoint"),
    Video(794, "ベバン点", "project/math/301_geometry_58/794_bevan/scene.py", "BevanPoint"),
    Video(795, "ネーマン・スコット", "project/math/302_probability_56/795_neyman_scott/scene.py", "NeymanScott"),
    Video(796, "マターン過程", "project/math/302_probability_56/796_matern/scene.py", "MaternProcess"),
    Video(797, "中央二項係数", "project/math/303_combinatorics_55/797_central_binom/scene.py", "CentralBinomial"),
)

VIDEOS_798_809: tuple[Video, ...] = (
    Video(798, "フロベニウス多様体", "project/math/304_analysis_59/798_frobenius/scene.py", "FrobeniusManifold"),
    Video(799, "ミラー写像", "project/math/304_analysis_59/799_mirror_map/scene.py", "MirrorMap"),
    Video(800, "ヤコビ環", "project/math/304_analysis_59/800_jacobi_ring/scene.py", "JacobiRing"),
    Video(801, "NAdam", "project/math/305_linear_59/801_nadam/scene.py", "NAdam"),
    Video(802, "Adamax", "project/math/305_linear_59/802_adamax/scene.py", "Adamax"),
    Video(803, "Lamb", "project/math/305_linear_59/803_lamb/scene.py", "Lamb"),
    Video(804, "シュタイナー点", "project/math/306_geometry_59/804_steiner/scene.py", "SteinerPoint"),
    Video(805, "アイゼンシュタイン三点", "project/math/306_geometry_59/805_eisenstein/scene.py", "EisensteinTriple"),
    Video(806, "第一ナポレオン", "project/math/306_geometry_59/806_napoleon1/scene.py", "FirstNapoleon"),
    Video(807, "トーマス過程", "project/math/307_probability_57/807_thomas/scene.py", "ThomasProcess"),
    Video(808, "ホークス過程", "project/math/307_probability_57/808_hawkes/scene.py", "HawkesProcess"),
    Video(809, "デラノワ数", "project/math/308_combinatorics_56/809_delannoy/scene.py", "DelannoyNumbers"),
)

VIDEOS_810_821: tuple[Video, ...] = (
    Video(810, "陳類", "project/math/309_analysis_60/810_chern/scene.py", "ChernClass"),
    Video(811, "超平面配置", "project/math/309_analysis_60/811_arrangement/scene.py", "HyperplaneArrangement"),
    Video(812, "交点数", "project/math/309_analysis_60/812_intersection/scene.py", "IntersectionNumber"),
    Video(813, "Kron", "project/math/310_linear_60/813_kron/scene.py", "Kron"),
    Video(814, "SM3", "project/math/310_linear_60/814_sm3/scene.py", "SM3"),
    Video(815, "K-FAC", "project/math/310_linear_60/815_kfac/scene.py", "KFAC"),
    Video(816, "第二ナポレオン", "project/math/311_geometry_60/816_napoleon2/scene.py", "SecondNapoleon"),
    Video(817, "キーペルト点", "project/math/311_geometry_60/817_kiepert/scene.py", "KiepertPoint"),
    Video(818, "コンウェイ点", "project/math/311_geometry_60/818_conway/scene.py", "ConwayPoint"),
    Video(819, "クラスター過程", "project/math/312_probability_58/819_cluster/scene.py", "ClusterProcess"),
    Video(820, "バートレット過程", "project/math/312_probability_58/820_bartlett/scene.py", "BartlettProcess"),
    Video(821, "ファイン数", "project/math/313_combinatorics_57/821_fine/scene.py", "FineNumbers"),
)

VIDEOS_822_833: tuple[Video, ...] = (
    Video(822, "クンマー曲面", "project/math/314_analysis_61/822_kummer/scene.py", "KummerSurface"),
    Video(823, "カラビ・ヤウ", "project/math/314_analysis_61/823_calabi_yau/scene.py", "CalabiYau"),
    Video(824, "特異点解消", "project/math/314_analysis_61/824_resolution/scene.py", "ResolutionOfSingularities"),
    Video(825, "NaturalGrad", "project/math/315_linear_61/825_natural_grad/scene.py", "NaturalGrad"),
    Video(826, "SWATS", "project/math/315_linear_61/826_swats/scene.py", "SWATS"),
    Video(827, "Gravity", "project/math/315_linear_61/827_gravity/scene.py", "Gravity"),
    Video(828, "シュライフラ点", "project/math/316_geometry_61/828_schiffler/scene.py", "SchifflerPoint"),
    Video(829, "グレブ点", "project/math/316_geometry_61/829_grebe/scene.py", "GrebePoint"),
    Video(830, "ミッケル点", "project/math/316_geometry_61/830_miquel/scene.py", "MiquelPoint"),
    Video(831, "フォック空間過程", "project/math/317_probability_59/831_fock/scene.py", "FockSpaceProcess"),
    Video(832, "ガウス過程回帰", "project/math/317_probability_59/832_gpr/scene.py", "GaussianProcessRegression"),
    Video(833, "大きなシュレーダー", "project/math/318_combinatorics_58/833_large_schroeder/scene.py", "LargeSchroeder"),
)

VIDEOS_834_845: tuple[Video, ...] = (
    Video(834, "ワイル指標", "project/math/319_analysis_62/834_weyl_character/scene.py", "WeylCharacter"),
    Video(835, "ヒルツェブルフ", "project/math/319_analysis_62/835_hirzebruch/scene.py", "Hirzebruch"),
    Video(836, "トーリック多様体", "project/math/319_analysis_62/836_toric/scene.py", "ToricVariety"),
    Video(837, "Adagrad", "project/math/320_linear_62/837_adagrad/scene.py", "Adagrad"),
    Video(838, "Lars", "project/math/320_linear_62/838_lars/scene.py", "Lars"),
    Video(839, "AdaSmooth", "project/math/320_linear_62/839_adasmooth/scene.py", "AdaSmooth"),
    Video(840, "九点円中心", "project/math/321_geometry_62/840_nine_point/scene.py", "NinePointCenter"),
    Video(841, "クローソン点", "project/math/321_geometry_62/841_clawson/scene.py", "ClawsonPoint"),
    Video(842, "イソトミカル共役", "project/math/321_geometry_62/842_isotomic/scene.py", "IsotomicConjugate"),
    Video(843, "ウィーナー過程", "project/math/322_probability_60/843_wiener/scene.py", "WienerProcess"),
    Video(844, "ブラウン橋", "project/math/322_probability_60/844_brownian_bridge/scene.py", "BrownianBridge"),
    Video(845, "シュレーダー・ヒップ", "project/math/323_combinatorics_59/845_schroeder_hipparchus/scene.py", "SchroederHipparchus"),
)

VIDEOS_846_857: tuple[Video, ...] = (
    Video(846, "モース理論", "project/math/324_analysis_63/846_morse/scene.py", "MorseTheory"),
    Video(847, "ハミルトン系", "project/math/324_analysis_63/847_hamiltonian/scene.py", "HamiltonianSystem"),
    Video(848, "ホッジ理論", "project/math/324_analysis_63/848_hodge/scene.py", "HodgeTheory"),
    Video(849, "AdaDelta", "project/math/325_linear_63/849_adadelta/scene.py", "AdaDelta"),
    Video(850, "QHAdam", "project/math/325_linear_63/850_qhadam/scene.py", "QHAdam"),
    Video(851, "AdamP", "project/math/325_linear_63/851_adamp/scene.py", "AdamP"),
    Video(852, "トリリニア極", "project/math/326_geometry_63/852_trilinear_pole/scene.py", "TrilinearPole"),
    Video(853, "シュタイナー楕円中心", "project/math/326_geometry_63/853_steiner_ellipse/scene.py", "SteinerEllipseCenter"),
    Video(854, "内心三角形", "project/math/326_geometry_63/854_intouch/scene.py", "IntouchTriangle"),
    Video(855, "オルンシュタイン・ウーレンベック", "project/math/327_probability_61/855_ou/scene.py", "OrnsteinUhlenbeck"),
    Video(856, "拡散過程", "project/math/327_probability_61/856_diffusion/scene.py", "DiffusionProcess"),
    Video(857, "スーパーカタラン", "project/math/328_combinatorics_60/857_super_catalan/scene.py", "SuperCatalan"),
)

VIDEOS_858_869: tuple[Video, ...] = (
    Video(858, "ケーラー多様体", "project/math/329_analysis_64/858_kahler/scene.py", "KahlerManifold"),
    Video(859, "シンプレクティック", "project/math/329_analysis_64/859_symplectic/scene.py", "SymplecticGeometry"),
    Video(860, "リーマン・ロッホ", "project/math/329_analysis_64/860_rr/scene.py", "RiemannRoch"),
    Video(861, "SGDP", "project/math/330_linear_64/861_sgdp/scene.py", "SGDP"),
    Video(862, "YellowFin", "project/math/330_linear_64/862_yellowfin/scene.py", "YellowFin"),
    Video(863, "AggMo", "project/math/330_linear_64/863_aggmo/scene.py", "AggMo"),
    Video(864, "共軸点", "project/math/331_geometry_64/864_coaxal/scene.py", "CoaxalPoint"),
    Video(865, "ペダル三角形", "project/math/331_geometry_64/865_pedal/scene.py", "PedalTriangle"),
    Video(866, "カールトン点", "project/math/331_geometry_64/866_carlton/scene.py", "CarltonPoint"),
    Video(867, "ジャンプ拡散", "project/math/332_probability_62/867_jump_diffusion/scene.py", "JumpDiffusion"),
    Video(868, "レヴィ過程", "project/math/332_probability_62/868_levy/scene.py", "LevyProcess"),
    Video(869, "ベルヌーイ数", "project/math/333_combinatorics_61/869_bernoulli/scene.py", "BernoulliNumbers"),
)

VIDEOS_870_881: tuple[Video, ...] = (
    Video(870, "セール双対", "project/math/334_analysis_65/870_serre/scene.py", "SerreDuality"),
    Video(871, "ド・ラーム", "project/math/334_analysis_65/871_de_rham/scene.py", "DeRham"),
    Video(872, "アティヤ・シンガー", "project/math/334_analysis_65/872_atiyah_singer/scene.py", "AtiyahSinger"),
    Video(873, "Fire", "project/math/335_linear_65/873_fire/scene.py", "Fire"),
    Video(874, "Pid", "project/math/335_linear_65/874_pid/scene.py", "Pid"),
    Video(875, "AccSGD", "project/math/335_linear_65/875_accsgd/scene.py", "AccSGD"),
    Video(876, "等距離点", "project/math/336_geometry_65/876_equidistant/scene.py", "EquidistantPoint"),
    Video(877, "共円点", "project/math/336_geometry_65/877_concyclic/scene.py", "ConcyclicPoints"),
    Video(878, "ピボット定理", "project/math/336_geometry_65/878_pivot/scene.py", "PivotTheorem"),
    Video(879, "安定過程", "project/math/337_probability_63/879_stable/scene.py", "StableProcess"),
    Video(880, "従属過程", "project/math/337_probability_63/880_subordinator/scene.py", "Subordinator"),
    Video(881, "オイラー数", "project/math/338_combinatorics_62/881_euler_numbers/scene.py", "EulerNumbers"),
)

VIDEOS_882_893: tuple[Video, ...] = (
    Video(882, "チャーン・ヴェイユ", "project/math/339_analysis_66/882_chern_weil/scene.py", "ChernWeil"),
    Video(883, "グロタンディーク", "project/math/339_analysis_66/883_grothendieck/scene.py", "Grothendieck"),
    Video(884, "指数指標", "project/math/339_analysis_66/884_chern_character/scene.py", "ChernCharacter"),
    Video(885, "AMSGrad", "project/math/340_linear_66/885_amsgrad/scene.py", "AMSGrad"),
    Video(886, "AdaMod", "project/math/340_linear_66/886_adamod/scene.py", "AdaMod"),
    Video(887, "AdaHessian", "project/math/340_linear_66/887_adahessian/scene.py", "AdaHessian"),
    Video(888, "イソゴナル共役", "project/math/341_geometry_66/888_isogonal/scene.py", "IsogonalConjugate"),
    Video(889, "エクセントリック", "project/math/341_geometry_66/889_eccentric/scene.py", "Eccentric"),
    Video(890, "シムソン線点", "project/math/341_geometry_66/890_simson_point/scene.py", "SimsonPoint"),
    Video(891, "加法過程", "project/math/342_probability_64/891_additive/scene.py", "AdditiveProcess"),
    Video(892, "セミマルチンゲール", "project/math/342_probability_64/892_semimartingale/scene.py", "Semimartingale"),
    Video(893, "セグル数列", "project/math/343_combinatorics_63/893_segner/scene.py", "SegnerNumbers"),
)

VIDEOS_894_905: tuple[Video, ...] = (
    Video(894, "トートロジカル類", "project/math/344_analysis_67/894_tautological/scene.py", "TautologicalClass"),
    Video(895, "チャーン数", "project/math/344_analysis_67/895_chern_number/scene.py", "ChernNumber"),
    Video(896, "交叉理論", "project/math/344_analysis_67/896_intersection/scene.py", "IntersectionTheory"),
    Video(897, "AdaShift", "project/math/345_linear_67/897_adashift/scene.py", "AdaShift"),
    Video(898, "Eve", "project/math/345_linear_67/898_eve/scene.py", "Eve"),
    Video(899, "SWAG", "project/math/345_linear_67/899_swag/scene.py", "SWAG"),
    Video(900, "等距離中心", "project/math/346_geometry_67/900_equidistant_center/scene.py", "EquidistantCenter"),
    Video(901, "第一等角共役", "project/math/346_geometry_67/901_first_isogonal/scene.py", "FirstIsogonal"),
    Video(902, "第二等角共役", "project/math/346_geometry_67/902_second_isogonal/scene.py", "SecondIsogonal"),
    Video(903, "マルチンゲール", "project/math/347_probability_65/903_martingale/scene.py", "Martingale"),
    Video(904, "局所時間", "project/math/347_probability_65/904_local_time/scene.py", "LocalTime"),
    Video(905, "フィボナッチ多項式", "project/math/348_combinatorics_64/905_fib_poly/scene.py", "FibonacciPolynomials"),
)

VIDEOS_906_917: tuple[Video, ...] = (
    Video(906, "仮想類", "project/math/349_analysis_68/906_virtual_class_short/scene.py", "VirtualClassShort"),
    Video(907, "GW不変量", "project/math/349_analysis_68/907_gw_invariant/scene.py", "GWInvariant"),
    Video(908, "量子リーマン・ロッホ", "project/math/349_analysis_68/908_quantum_rr/scene.py", "QuantumRR"),
    Video(909, "GSAM", "project/math/350_linear_68/909_gsam/scene.py", "GSAM"),
    Video(910, "ESAM", "project/math/350_linear_68/910_esam/scene.py", "ESAM"),
    Video(911, "MadGrad", "project/math/350_linear_68/911_madgrad/scene.py", "MadGradOpt"),
    Video(912, "配極", "project/math/351_geometry_68/912_polarity/scene.py", "Polarity"),
    Video(913, "三点共線", "project/math/351_geometry_68/913_collinear/scene.py", "ThreeCollinear"),
    Video(914, "ポンスレの定理", "project/math/351_geometry_68/914_poncelet/scene.py", "PonceletTheorem"),
    Video(915, "二次変分", "project/math/352_probability_66/915_quadratic_variation/scene.py", "QuadraticVariation"),
    Video(916, "ドレアゼ分解", "project/math/352_probability_66/916_doob_meyer/scene.py", "DoobMeyer"),
    Video(917, "ゼッケンドルフ", "project/math/353_combinatorics_65/917_zeckendorf/scene.py", "Zeckendorf"),
)

VIDEOS_918_929: tuple[Video, ...] = (
    Video(918, "仮想構造層", "project/math/354_analysis_69/918_virtual_structure/scene.py", "VirtualStructureSheaf"),
    Video(919, "グロタンディークRR", "project/math/354_analysis_69/919_grr/scene.py", "GrothendieckRR"),
    Video(920, "安定写像空間", "project/math/354_analysis_69/920_stable_map_space/scene.py", "StableMapSpace"),
    Video(921, "AdaX", "project/math/355_linear_69/921_adax/scene.py", "AdaX"),
    Video(922, "PowerSign", "project/math/355_linear_69/922_powersign/scene.py", "PowerSign"),
    Video(923, "AddSign", "project/math/355_linear_69/923_addsign/scene.py", "AddSign"),
    Video(924, "三線合流", "project/math/356_geometry_69/924_concurrent/scene.py", "ThreeConcurrent"),
    Video(925, "メネラウス比", "project/math/356_geometry_69/925_menelaus_ratio/scene.py", "MenelausRatio"),
    Video(926, "パスカル線点", "project/math/356_geometry_69/926_pascal_point/scene.py", "PascalLinePoint"),
    Video(927, "伊藤積分", "project/math/357_probability_67/927_ito/scene.py", "ItoIntegral"),
    Video(928, "ギラサノフ", "project/math/357_probability_67/928_girsanov/scene.py", "Girsanov"),
    Video(929, "メタフィボナッチ", "project/math/358_combinatorics_66/929_metafib/scene.py", "MetaFibonacci"),
)

VIDEOS_930_941: tuple[Video, ...] = (
    Video(930, "フィノ写像", "project/math/359_analysis_70/930_fino/scene.py", "FanoMap"),
    Video(931, "モジュライ積み", "project/math/359_analysis_70/931_moduli_stack/scene.py", "ModuliStack"),
    Video(932, "障害理論", "project/math/359_analysis_70/932_obstruction/scene.py", "ObstructionTheory"),
    Video(933, "QHM", "project/math/360_linear_70/933_qhm/scene.py", "QHM"),
    Video(934, "LaProp", "project/math/360_linear_70/934_laprop/scene.py", "LaProp"),
    Video(935, "AdaNorm", "project/math/360_linear_70/935_adanorm/scene.py", "AdaNorm"),
    Video(936, "共円条件点", "project/math/361_geometry_70/936_concyclic_cond/scene.py", "ConcyclicConditionPoint"),
    Video(937, "等角共役軸", "project/math/361_geometry_70/937_isogonal_axis/scene.py", "IsogonalAxis"),
    Video(938, "シムソン族", "project/math/361_geometry_70/938_simson_family/scene.py", "SimsonFamily"),
    Video(939, "ストラスノヴィッチ", "project/math/362_probability_68/939_stratonovich/scene.py", "Stratonovich"),
    Video(940, "田中公式", "project/math/362_probability_68/940_tanaka/scene.py", "TanakaFormula"),
    Video(941, "リュカ多項式", "project/math/363_combinatorics_67/941_lucas_poly/scene.py", "LucasPolynomials"),
)

VIDEOS_942_953: tuple[Video, ...] = (
    Video(942, "完全障害", "project/math/364_analysis_71/942_perfect_obstruction/scene.py", "PerfectObstruction"),
    Video(943, "仮想次元", "project/math/364_analysis_71/943_virtual_dim/scene.py", "VirtualDimension"),
    Video(944, "ファノ多様体", "project/math/364_analysis_71/944_fano/scene.py", "FanoVariety"),
    Video(945, "DemonAdam", "project/math/365_linear_71/945_demon/scene.py", "DemonAdam"),
    Video(946, "AdaPlus", "project/math/365_linear_71/946_adaplus/scene.py", "AdaPlus"),
    Video(947, "NadamW", "project/math/365_linear_71/947_nadamw/scene.py", "NadamW"),
    Video(948, "内心反射", "project/math/366_geometry_71/948_incenter_reflect/scene.py", "IncenterReflection"),
    Video(949, "五点共円", "project/math/366_geometry_71/949_five_concyclic/scene.py", "FiveConcyclic"),
    Video(950, "外接円弧", "project/math/366_geometry_71/950_circumarc/scene.py", "CircumArc"),
    Video(951, "確率積分", "project/math/367_probability_69/951_stochastic_integral/scene.py", "StochasticIntegral"),
    Video(952, "占有時間", "project/math/367_probability_69/952_occupation_time/scene.py", "OccupationTime"),
    Video(953, "ペル多項式", "project/math/368_combinatorics_68/953_pell_poly/scene.py", "PellPolynomials"),
)

VIDEOS_954_965: tuple[Video, ...] = (
    Video(954, "有理曲線", "project/math/369_analysis_72/954_rational_curve/scene.py", "RationalCurve"),
    Video(955, "森理論", "project/math/369_analysis_72/955_mori/scene.py", "MoriTheory"),
    Video(956, "旗多様体", "project/math/369_analysis_72/956_flag/scene.py", "FlagVariety"),
    Video(957, "AdaGO", "project/math/370_linear_72/957_adago/scene.py", "AdaGO"),
    Video(958, "AdaBeliefW", "project/math/370_linear_72/958_adabeliefw/scene.py", "AdaBeliefW"),
    Video(959, "EveW", "project/math/370_linear_72/959_evew/scene.py", "EveW"),
    Video(960, "内心三角形辺", "project/math/371_geometry_72/960_intouch_side/scene.py", "IntouchSide"),
    Video(961, "傍心円", "project/math/371_geometry_72/961_excircle/scene.py", "ExcircleCenterCircle"),
    Video(962, "角の二等分線長", "project/math/371_geometry_72/962_bisector_length/scene.py", "BisectorLength"),
    Video(963, "ブラウン局所時間", "project/math/372_probability_70/963_brownian_local/scene.py", "BrownianLocalTime"),
    Video(964, "反射ブラウン", "project/math/372_probability_70/964_reflected_bm/scene.py", "ReflectedBM"),
    Video(965, "カタラン多項式", "project/math/373_combinatorics_69/965_catalan_poly/scene.py", "CatalanPolynomials"),
)

VIDEOS_966_977: tuple[Video, ...] = (
    Video(966, "シューベルト類", "project/math/374_analysis_73/966_schubert_class/scene.py", "SchubertClass"),
    Video(967, "シューベルト多様体", "project/math/374_analysis_73/967_schubert_var/scene.py", "SchubertVariety"),
    Video(968, "量子シューベルト", "project/math/374_analysis_73/968_quantum_schubert/scene.py", "QuantumSchubert"),
    Video(969, "LionW", "project/math/375_linear_73/969_lionw/scene.py", "LionW"),
    Video(970, "SophiaW", "project/math/375_linear_73/970_sophiaw/scene.py", "SophiaW"),
    Video(971, "MuonW", "project/math/375_linear_73/971_muonw/scene.py", "MuonW"),
    Video(972, "接線長公式", "project/math/376_geometry_73/972_tangent_lengths/scene.py", "TangentLengths"),
    Video(973, "半周長公式", "project/math/376_geometry_73/973_semiperimeter/scene.py", "Semiperimeter"),
    Video(974, "角二等分定理", "project/math/376_geometry_73/974_angle_bisector/scene.py", "AngleBisectorTheorem"),
    Video(975, "スカロホッド", "project/math/377_probability_71/975_skorokhod/scene.py", "Skorokhod"),
    Video(976, "首回到達", "project/math/377_probability_71/976_hitting_time/scene.py", "HittingTime"),
    Video(977, "モツキン多項式", "project/math/378_combinatorics_70/977_motzkin_poly/scene.py", "MotzkinPolynomials"),
)

VIDEOS_978_989: tuple[Video, ...] = (
    Video(978, "ピカール群", "project/math/379_analysis_74/978_picard/scene.py", "PicardGroup"),
    Video(979, "ネロン・セヴェリ", "project/math/379_analysis_74/979_ns/scene.py", "NeronSeveri"),
    Video(980, "標準束", "project/math/379_analysis_74/980_canonical/scene.py", "CanonicalBundle"),
    Video(981, "SophiaH", "project/math/380_linear_74/981_sophiah/scene.py", "SophiaH"),
    Video(982, "MuonClip", "project/math/380_linear_74/982_muonclip/scene.py", "MuonClip"),
    Video(983, "SOAPClip", "project/math/380_linear_74/983_soapclip/scene.py", "SOAPClip"),
    Video(984, "余弦法則", "project/math/381_geometry_74/984_cosine_law/scene.py", "CosineLaw"),
    Video(985, "方べきの逆", "project/math/381_geometry_74/985_power_inverse/scene.py", "PowerInverse"),
    Video(986, "オイラー距離", "project/math/381_geometry_74/986_euler_distance/scene.py", "EulerDistance"),
    Video(987, "キリング時間", "project/math/382_probability_72/987_killing_time/scene.py", "KillingTime"),
    Video(988, "局所時押し出し", "project/math/382_probability_72/988_local_push/scene.py", "LocalTimePush"),
    Video(989, "シュレーダー多項式", "project/math/383_combinatorics_71/989_schroeder_poly/scene.py", "SchroederPolynomials"),
)

VIDEOS_990_1001: tuple[Video, ...] = (
    Video(990, "反標準束", "project/math/384_analysis_75/990_anticanonical/scene.py", "AnticanonicalBundle"),
    Video(991, "線束", "project/math/384_analysis_75/991_line_bundle/scene.py", "LineBundle"),
    Video(992, "豊富性", "project/math/384_analysis_75/992_ampleness/scene.py", "Ampleness"),
    Video(993, "ScheduleFreeW", "project/math/385_linear_75/993_sfw/scene.py", "ScheduleFreeW"),
    Video(994, "ProdigyW", "project/math/385_linear_75/994_prodigyw/scene.py", "ProdigyW"),
    Video(995, "AdaFactorW", "project/math/385_linear_75/995_adafactorw/scene.py", "AdaFactorW"),
    Video(996, "トレミー比", "project/math/386_geometry_75/996_ptolemy_ratio/scene.py", "PtolemyRatio"),
    Video(997, "正弦余弦辺", "project/math/386_geometry_75/997_sine_cosine_side/scene.py", "SineCosineSide"),
    Video(998, "外接半径公式", "project/math/386_geometry_75/998_circumradius/scene.py", "CircumradiusFormula"),
    Video(999, "首回到達時間", "project/math/387_probability_73/999_hitting_time_dist/scene.py", "HittingTimeDistribution"),
    Video(1000, "反射原理ブラウン", "project/math/387_probability_73/1000_reflection_bm/scene.py", "ReflectionPrincipleBM"),
    Video(1001, "ナラヤナ多項式", "project/math/388_combinatorics_72/1001_narayana_poly/scene.py", "NarayanaPolynomials"),
)

VIDEOS_1002_1013: tuple[Video, ...] = (
    Video(1002, "数値的効果", "project/math/389_analysis_76/1002_numerical_effect/scene.py", "NumericalEffectivity"),
    Video(1003, "交叉形式", "project/math/389_analysis_76/1003_intersection_form/scene.py", "IntersectionForm"),
    Video(1004, "ビッグ錐", "project/math/389_analysis_76/1004_big_cone/scene.py", "BigCone"),
    Video(1005, "PadamW", "project/math/390_linear_76/1005_padamw/scene.py", "PadamW"),
    Video(1006, "AdaiW", "project/math/390_linear_76/1006_adaiw/scene.py", "AdaiW"),
    Video(1007, "ShampooW", "project/math/390_linear_76/1007_shampoow/scene.py", "ShampooW"),
    Video(1008, "内心半径公式", "project/math/391_geometry_76/1008_inradius/scene.py", "InradiusFormula"),
    Video(1009, "傍心半径公式", "project/math/391_geometry_76/1009_exradius/scene.py", "ExradiusFormula"),
    Video(1010, "面積ヘロン", "project/math/391_geometry_76/1010_heron_area/scene.py", "HeronArea"),
    Video(1011, "最大過程", "project/math/392_probability_74/1011_maximum_process/scene.py", "MaximumProcess"),
    Video(1012, "ブラウン橋分布", "project/math/392_probability_74/1012_bb_law/scene.py", "BrownianBridgeLaw"),
    Video(1013, "ファイン多項式", "project/math/393_combinatorics_73/1013_fine_poly/scene.py", "FinePolynomials"),
)

VIDEOS_1014_1025: tuple[Video, ...] = (
    Video(1014, "有効錐", "project/math/394_analysis_77/1014_effective_cone/scene.py", "EffectiveCone"),
    Video(1015, "ネフ錐", "project/math/394_analysis_77/1015_nef_cone/scene.py", "NefCone"),
    Video(1016, "ムービング錐", "project/math/394_analysis_77/1016_moving_cone/scene.py", "MovingCone"),
    Video(1017, "AdoptW", "project/math/395_linear_77/1017_adoptw/scene.py", "AdoptW"),
    Video(1018, "KronW", "project/math/395_linear_77/1018_kronw/scene.py", "KronW"),
    Video(1019, "SOAPW", "project/math/395_linear_77/1019_soapw/scene.py", "SOAPW"),
    Video(1020, "ヘロン変形", "project/math/396_geometry_77/1020_heron_variant/scene.py", "HeronVariant"),
    Video(1021, "オイラー三角形公式", "project/math/396_geometry_77/1021_euler_triangle/scene.py", "EulerTriangleFormula"),
    Video(1022, "角面積公式", "project/math/396_geometry_77/1022_angle_area/scene.py", "AngleAreaFormula"),
    Video(1023, "最小過程", "project/math/397_probability_75/1023_minimum_process/scene.py", "MinimumProcess"),
    Video(1024, "劣マルチンゲール", "project/math/397_probability_75/1024_submartingale/scene.py", "Submartingale"),
    Video(1025, "デラノワ多項式", "project/math/398_combinatorics_74/1025_delannoy_poly/scene.py", "DelannoyPolynomials"),
)

VIDEOS_1026_1037: tuple[Video, ...] = (
    Video(1026, "クレマン錐", "project/math/399_analysis_78/1026_kleiman/scene.py", "KleimanCone"),
    Video(1027, "数値同値", "project/math/399_analysis_78/1027_numerical_equiv/scene.py", "NumericalEquivalence"),
    Video(1028, "線形同値", "project/math/399_analysis_78/1028_linear_equiv/scene.py", "LinearEquivalence"),
    Video(1029, "RangerW", "project/math/400_linear_78/1029_rangerw/scene.py", "RangerW"),
    Video(1030, "ApolloW", "project/math/400_linear_78/1030_apollow/scene.py", "ApolloW"),
    Video(1031, "AdaiClip", "project/math/400_linear_78/1031_adaiclip/scene.py", "AdaiClip"),
    Video(1032, "傍接半径", "project/math/401_geometry_78/1032_exradius_short/scene.py", "ExradiusShort"),
    Video(1033, "内接半径", "project/math/401_geometry_78/1033_inradius_short/scene.py", "InradiusShort"),
    Video(1034, "正弦面積半", "project/math/401_geometry_78/1034_sine_area_half/scene.py", "SineAreaHalf"),
    Video(1035, "優マルチンゲール", "project/math/402_probability_76/1035_supermartingale/scene.py", "Supermartingale"),
    Video(1036, "任意停止", "project/math/402_probability_76/1036_optional_stopping/scene.py", "OptionalStopping"),
    Video(1037, "切手問題", "project/math/403_combinatorics_75/1037_postage/scene.py", "PostageStamp"),
)

VIDEOS_1038_1049: tuple[Video, ...] = (
    Video(1038, "飯高次元", "project/math/404_analysis_79/1038_iitaka/scene.py", "IitakaDimension"),
    Video(1039, "小平次元", "project/math/404_analysis_79/1039_kodaira/scene.py", "KodairaDimension"),
    Video(1040, "体積関数", "project/math/404_analysis_79/1040_volume/scene.py", "VolumeFunction"),
    Video(1041, "LionClip", "project/math/405_linear_79/1041_lionclip/scene.py", "LionClip"),
    Video(1042, "SophiaClip", "project/math/405_linear_79/1042_sophiaclip/scene.py", "SophiaClip"),
    Video(1043, "MuonSoft", "project/math/405_linear_79/1043_muonsoft/scene.py", "MuonSoft"),
    Video(1044, "三辺面積比", "project/math/406_geometry_79/1044_side_area_ratio/scene.py", "SideAreaRatio"),
    Video(1045, "オイラー線分比", "project/math/406_geometry_79/1045_euler_ratio/scene.py", "EulerLineRatio"),
    Video(1046, "九点円半径", "project/math/406_geometry_79/1046_nine_point_r/scene.py", "NinePointRadius"),
    Video(1047, "ドゥーブ不等式", "project/math/407_probability_77/1047_doob/scene.py", "DoobInequality"),
    Video(1048, "アズーマ不等式", "project/math/407_probability_77/1048_azuma/scene.py", "AzumaInequality"),
    Video(1049, "フロベニウス数", "project/math/408_combinatorics_76/1049_frobenius_number/scene.py", "FrobeniusNumber"),
)

VIDEOS_1050_1061: tuple[Video, ...] = (
    Video(1050, "漸近リーマンロッホ", "project/math/409_analysis_80/1050_asymptotic_rr/scene.py", "AsymptoticRR"),
    Video(1051, "乗法イデアル", "project/math/409_analysis_80/1051_multiplier/scene.py", "MultiplierIdeal"),
    Video(1052, "対数的閾値", "project/math/409_analysis_80/1052_lct/scene.py", "LogCanonicalThreshold"),
    Video(1053, "SOAPSoft", "project/math/410_linear_80/1053_soapsoft/scene.py", "SOAPSoft"),
    Video(1054, "ShampooClip", "project/math/410_linear_80/1054_shampooclip/scene.py", "ShampooClip"),
    Video(1055, "AdoptClip", "project/math/410_linear_80/1055_adoptclip/scene.py", "AdoptClip"),
    Video(1056, "傍心距離", "project/math/411_geometry_80/1056_excenter_dist/scene.py", "ExcenterDistance"),
    Video(1057, "九点円中心線", "project/math/411_geometry_80/1057_nine_point_line/scene.py", "NinePointLine"),
    Video(1058, "外心内心距離", "project/math/411_geometry_80/1058_oi_distance/scene.py", "OIDistance"),
    Video(1059, "ホフディング", "project/math/412_probability_78/1059_hoeffding/scene.py", "Hoeffding"),
    Video(1060, "バーンスタイン不等式", "project/math/412_probability_78/1060_bernstein/scene.py", "BernsteinInequality"),
    Video(1061, "硬貨問題", "project/math/413_combinatorics_77/1061_coin_problem/scene.py", "CoinProblem"),
)

VIDEOS_1062_1073: tuple[Video, ...] = (
    Video(1062, "対数解消", "project/math/414_analysis_81/1062_log_resolution/scene.py", "LogResolution"),
    Video(1063, "単純正規交叉", "project/math/414_analysis_81/1063_snc/scene.py", "SimpleNormalCrossings"),
    Video(1064, "跳躍数", "project/math/414_analysis_81/1064_jumping_numbers/scene.py", "JumpingNumbers"),
    Video(1065, "KronClip", "project/math/415_linear_81/1065_kronclip/scene.py", "KronClip"),
    Video(1066, "LaPropW", "project/math/415_linear_81/1066_lapropw/scene.py", "LaPropW"),
    Video(1067, "QHMClip", "project/math/415_linear_81/1067_qhmclip/scene.py", "QHMClip"),
    Video(1068, "内心外心線", "project/math/416_geometry_81/1068_oi_line/scene.py", "OILine"),
    Video(1069, "垂心外心比", "project/math/416_geometry_81/1069_ho_ratio/scene.py", "HORatio"),
    Video(1070, "傍心内心距離", "project/math/416_geometry_81/1070_ii_distance/scene.py", "IIADistance"),
    Video(1071, "オプションサンプリング", "project/math/417_probability_79/1071_optional_sampling/scene.py", "OptionalSampling"),
    Video(1072, "ワルド等式", "project/math/417_probability_79/1072_wald/scene.py", "WaldIdentity"),
    Video(1073, "ナラヤナ三角形", "project/math/418_combinatorics_78/1073_narayana_triangle/scene.py", "NarayanaTriangle"),
)

VIDEOS_1074_1085: tuple[Video, ...] = (
    Video(1074, "川又・フィーベック", "project/math/419_analysis_82/1074_kawamata_viehweg/scene.py", "KawamataViehweg"),
    Video(1075, "Nadel消滅", "project/math/419_analysis_82/1075_nadel/scene.py", "NadelVanishing"),
    Video(1076, "端末特異点", "project/math/419_analysis_82/1076_terminal/scene.py", "TerminalSingularities"),
    Video(1077, "AdaSmoothClip", "project/math/420_linear_82/1077_adasmoothclip/scene.py", "AdaSmoothClip"),
    Video(1078, "LionSoft", "project/math/420_linear_82/1078_lionsoft/scene.py", "LionSoft"),
    Video(1079, "SophiaSoft", "project/math/420_linear_82/1079_sophiasoft/scene.py", "SophiaSoft"),
    Video(1080, "オイラー距離比", "project/math/421_geometry_82/1080_euler_dist_ratio/scene.py", "EulerDistRatio"),
    Video(1081, "内心傍心比", "project/math/421_geometry_82/1081_in_ex_ratio/scene.py", "InExRatio"),
    Video(1082, "外接内接比", "project/math/421_geometry_82/1082_circum_in_ratio/scene.py", "CircumInRatio"),
    Video(1083, "マクディアミド", "project/math/422_probability_80/1083_mcdiarmid/scene.py", "McDiarmid"),
    Video(1084, "ブールの不等式", "project/math/422_probability_80/1084_boole/scene.py", "BooleInequality"),
    Video(1085, "整数分割多項式", "project/math/423_combinatorics_79/1085_partition_poly/scene.py", "PartitionPolynomials"),
)

VIDEOS_1086_1097: tuple[Video, ...] = (
    Video(1086, "川又対数端末", "project/math/424_analysis_83/1086_klt/scene.py", "KLT"),
    Video(1087, "正準特異点", "project/math/424_analysis_83/1087_canonical_sing/scene.py", "CanonicalSingularities"),
    Video(1088, "消滅定理", "project/math/424_analysis_83/1088_vanishing/scene.py", "VanishingTheorem"),
    Video(1089, "MuonHard", "project/math/425_linear_83/1089_muonhard/scene.py", "MuonHard"),
    Video(1090, "SOAPHard", "project/math/425_linear_83/1090_soaphard/scene.py", "SOAPHard"),
    Video(1091, "ShampooSoft", "project/math/425_linear_83/1091_shampoosoft/scene.py", "ShampooSoft"),
    Video(1092, "傍心外心距離", "project/math/426_geometry_83/1092_ex_o_dist/scene.py", "ExODistance"),
    Video(1093, "九点円垂心", "project/math/426_geometry_83/1093_nine_orthocenter/scene.py", "NineOrthocenter"),
    Video(1094, "内心外心比", "project/math/426_geometry_83/1094_io_ratio/scene.py", "IORatio"),
    Video(1095, "ユニオンバウンド", "project/math/427_probability_81/1095_union_bound/scene.py", "UnionBound"),
    Video(1096, "マクディアミド差", "project/math/427_probability_81/1096_mcdiarmid_diff/scene.py", "McDiarmidDiff"),
    Video(1097, "カタラン三角形細分", "project/math/428_combinatorics_80/1097_catalan_triangle_ref/scene.py", "CatalanTriangleRefine"),
)

VIDEOS_1098_1109: tuple[Video, ...] = (
    Video(1098, "食い違い係数", "project/math/429_analysis_84/1098_discrepancy/scene.py", "Discrepancy"),
    Video(1099, "標準環", "project/math/429_analysis_84/1099_canonical_ring/scene.py", "CanonicalRing"),
    Video(1100, "極小モデル", "project/math/429_analysis_84/1100_minimal_model/scene.py", "MinimalModel"),
    Video(1101, "AdaNormClip", "project/math/430_linear_84/1101_adanormclip/scene.py", "AdaNormClip"),
    Video(1102, "QHMSoft", "project/math/430_linear_84/1102_qhmsoft/scene.py", "QHMSoft"),
    Video(1103, "LaPropClip", "project/math/430_linear_84/1103_lapropclip/scene.py", "LaPropClip"),
    Video(1104, "垂心内心距離", "project/math/431_geometry_84/1104_hi_distance/scene.py", "HIDistance"),
    Video(1105, "重心外心距離", "project/math/431_geometry_84/1105_go_distance/scene.py", "GODistance"),
    Video(1106, "九点円外接比", "project/math/431_geometry_84/1106_nine_circum_ratio/scene.py", "NineCircumRatio"),
    Video(1107, "ブール上界", "project/math/432_probability_82/1107_boole_bound/scene.py", "BooleBound"),
    Video(1108, "有界差不等式", "project/math/432_probability_82/1108_bounded_diff/scene.py", "BoundedDifferences"),
    Video(1109, "モツキン三角形", "project/math/433_combinatorics_81/1109_motzkin_triangle/scene.py", "MotzkinTriangle"),
)

VIDEOS_1110_1121: tuple[Video, ...] = (
    Video(1110, "フリップ", "project/math/434_analysis_85/1110_flip/scene.py", "Flip"),
    Video(1111, "フリップ収縮", "project/math/434_analysis_85/1111_flip_contraction/scene.py", "FlipContraction"),
    Video(1112, "アバンダンス", "project/math/434_analysis_85/1112_abundance/scene.py", "Abundance"),
    Video(1113, "AdaBoundClip", "project/math/435_linear_85/1113_adaboundclip/scene.py", "AdaBoundClip"),
    Video(1114, "LionHard", "project/math/435_linear_85/1114_lionhard/scene.py", "LionHard"),
    Video(1115, "SophiaBound", "project/math/435_linear_85/1115_sophiabound/scene.py", "SophiaBound"),
    Video(1116, "内心九点距離", "project/math/436_geometry_85/1116_in_nine_dist/scene.py", "InNineDistance"),
    Video(1117, "傍心垂心距離", "project/math/436_geometry_85/1117_ex_ortho_dist/scene.py", "ExOrthoDistance"),
    Video(1118, "重心内心距離", "project/math/436_geometry_85/1118_g_in_dist/scene.py", "GInDistance"),
    Video(1119, "チェルノフ積", "project/math/437_probability_83/1119_chernoff_prod/scene.py", "ChernoffProduct"),
    Video(1120, "ヘフディング和", "project/math/437_probability_83/1120_hoeffding_sum/scene.py", "HoeffdingSum"),
    Video(1121, "シュレーダー三角形", "project/math/438_combinatorics_82/1121_schroeder_triangle/scene.py", "SchroederTriangle"),
)

VIDEOS_1122_1133: tuple[Video, ...] = (
    Video(1122, "端末フリップ", "project/math/439_analysis_86/1122_terminal_flip/scene.py", "TerminalFlip"),
    Video(1123, "対数フリップ", "project/math/439_analysis_86/1123_log_flip/scene.py", "LogFlip"),
    Video(1124, "相対極小モデル", "project/math/439_analysis_86/1124_relative_mmp/scene.py", "RelativeMMP"),
    Video(1125, "AdoptHard", "project/math/440_linear_86/1125_adopthard/scene.py", "AdoptHard"),
    Video(1126, "KronSoft", "project/math/440_linear_86/1126_kronsoft/scene.py", "KronSoft"),
    Video(1127, "AdaGradClip", "project/math/440_linear_86/1127_adagradclip/scene.py", "AdaGradClip"),
    Video(1128, "垂心傍心距離", "project/math/441_geometry_86/1128_h_ex_dist/scene.py", "HExDistance"),
    Video(1129, "外心九点距離", "project/math/441_geometry_86/1129_o_nine_dist/scene.py", "ONineDistance"),
    Video(1130, "内心重心比", "project/math/441_geometry_86/1130_ig_ratio/scene.py", "IGRatio"),
    Video(1131, "マルコフ積", "project/math/442_probability_84/1131_markov_prod/scene.py", "MarkovProduct"),
    Video(1132, "チェビシェフ積", "project/math/442_probability_84/1132_chebyshev_prod/scene.py", "ChebyshevProduct"),
    Video(1133, "デラノイ三角形", "project/math/443_combinatorics_83/1133_delannoy_triangle/scene.py", "DelannoyTriangle"),
)

VIDEOS_1134_1145: tuple[Video, ...] = (
    Video(1134, "擬有効錐", "project/math/444_analysis_87/1134_psef_cone/scene.py", "PsefCone"),
    Video(1135, "数値的次元", "project/math/444_analysis_87/1135_numerical_dim/scene.py", "NumericalDimension"),
    Video(1136, "標準モデル", "project/math/444_analysis_87/1136_canonical_model/scene.py", "CanonicalModel"),
    Video(1137, "MuonBound", "project/math/445_linear_87/1137_muonbound/scene.py", "MuonBound"),
    Video(1138, "SOAPBound", "project/math/445_linear_87/1138_soapbound/scene.py", "SOAPBound"),
    Video(1139, "ShampooHard", "project/math/445_linear_87/1139_shampoohard/scene.py", "ShampooHard"),
    Video(1140, "傍心重心距離", "project/math/446_geometry_87/1140_ex_g_dist/scene.py", "ExGDistance"),
    Video(1141, "垂心重心距離", "project/math/446_geometry_87/1141_h_g_dist/scene.py", "HGDistance"),
    Video(1142, "外心傍心比", "project/math/446_geometry_87/1142_o_ex_ratio/scene.py", "OExRatio"),
    Video(1143, "アズーマ差", "project/math/447_probability_85/1143_azuma_diff/scene.py", "AzumaDiff"),
    Video(1144, "ドゥーブ上界", "project/math/447_probability_85/1144_doob_bound/scene.py", "DoobBound"),
    Video(1145, "小さなシュレーダー", "project/math/448_combinatorics_84/1145_small_schroeder/scene.py", "SmallSchroeder"),
)

VIDEOS_1146_1157: tuple[Video, ...] = (
    Video(1146, "飯高ファイバー", "project/math/449_analysis_88/1146_iitaka_fiber/scene.py", "IitakaFiber"),
    Video(1147, "小平ファイバー", "project/math/449_analysis_88/1147_kodaira_fiber/scene.py", "KodairaFiber"),
    Video(1148, "標準ファイバー", "project/math/449_analysis_88/1148_canonical_fiber/scene.py", "CanonicalFiber"),
    Video(1149, "AdaDeltaClip", "project/math/450_linear_88/1149_adadeltaclip/scene.py", "AdaDeltaClip"),
    Video(1150, "LionBound", "project/math/450_linear_88/1150_lionbound/scene.py", "LionBound"),
    Video(1151, "SophiaHard", "project/math/450_linear_88/1151_sophiahard/scene.py", "SophiaHard"),
    Video(1152, "九点内心比", "project/math/451_geometry_88/1152_nine_in_ratio/scene.py", "NineInRatio"),
    Video(1153, "垂心九点比", "project/math/451_geometry_88/1153_h_nine_ratio/scene.py", "HNineRatio"),
    Video(1154, "重心九点距離", "project/math/451_geometry_88/1154_g_nine_dist/scene.py", "GNineDistance"),
    Video(1155, "ペティ不等式", "project/math/452_probability_86/1155_petty/scene.py", "PettyInequality"),
    Video(1156, "フリードマン不等式", "project/math/452_probability_86/1156_freedman/scene.py", "FreedmanInequality"),
    Video(1157, "ルカ数列", "project/math/453_combinatorics_85/1157_lucas/scene.py", "LucasSequence"),
)

VIDEOS_1158_1169: tuple[Video, ...] = (
    Video(1158, "移動補題", "project/math/454_analysis_89/1158_moving_lemma/scene.py", "MovingLemma"),
    Video(1159, "基底軌跡", "project/math/454_analysis_89/1159_base_locus/scene.py", "BaseLocus"),
    Video(1160, "安定基点自由", "project/math/454_analysis_89/1160_stable_basepoint/scene.py", "StableBasepointFree"),
    Video(1161, "AdoptSoft", "project/math/455_linear_89/1161_adoptsoft/scene.py", "AdoptSoft"),
    Video(1162, "KronHard", "project/math/455_linear_89/1162_kronhard/scene.py", "KronHard"),
    Video(1163, "NAdamClip", "project/math/455_linear_89/1163_nadamclip/scene.py", "NAdamClip"),
    Video(1164, "傍心九点距離", "project/math/456_geometry_89/1164_ex_nine_dist/scene.py", "ExNineDistance"),
    Video(1165, "内心外心線比", "project/math/456_geometry_89/1165_io_line_ratio/scene.py", "IOLineRatio"),
    Video(1166, "垂心外心距離比", "project/math/456_geometry_89/1166_ho_dist_ratio/scene.py", "HODistRatio"),
    Video(1167, "カントロジ不等式", "project/math/457_probability_87/1167_kantorovich/scene.py", "KantorovichInequality"),
    Video(1168, "ピネリス不等式", "project/math/457_probability_87/1168_pinelis/scene.py", "PinelisInequality"),
    Video(1169, "エルミート三角形", "project/math/458_combinatorics_86/1169_hermite_triangle/scene.py", "HermiteTriangle"),
)

VIDEOS_1170_1181: tuple[Video, ...] = (
    Video(1170, "数値的引き算", "project/math/459_analysis_90/1170_numerical_pullback/scene.py", "NumericalPullback"),
    Video(1171, "数値的押し出し", "project/math/459_analysis_90/1171_numerical_pushforward/scene.py", "NumericalPushforward"),
    Video(1172, "交点数公式", "project/math/459_analysis_90/1172_intersection_number/scene.py", "IntersectionNumber"),
    Video(1173, "QHMBound", "project/math/460_linear_90/1173_qhmbound/scene.py", "QHMBound"),
    Video(1174, "LaPropBound", "project/math/460_linear_90/1174_lapropbound/scene.py", "LaPropBound"),
    Video(1175, "AdaSmoothHard", "project/math/460_linear_90/1175_adasmoothhard/scene.py", "AdaSmoothHard"),
    Video(1176, "内心傍心線", "project/math/461_geometry_90/1176_in_ex_line/scene.py", "InExLine"),
    Video(1177, "重心傍心比", "project/math/461_geometry_90/1177_g_ex_ratio/scene.py", "GExRatio"),
    Video(1178, "九点傍心比", "project/math/461_geometry_90/1178_nine_ex_ratio/scene.py", "NineExRatio"),
    Video(1179, "ブール積", "project/math/462_probability_88/1179_boole_prod/scene.py", "BooleProduct"),
    Video(1180, "ヘフディング積", "project/math/462_probability_88/1180_hoeffding_prod/scene.py", "HoeffdingProduct"),
    Video(1181, "オイラー三角形", "project/math/463_combinatorics_87/1181_euler_triangle/scene.py", "EulerTriangle"),
)

VIDEOS_1182_1193: tuple[Video, ...] = (
    Video(1182, "自己交差", "project/math/464_analysis_91/1182_self_intersection/scene.py", "SelfIntersection"),
    Video(1183, "ネフ閾値", "project/math/464_analysis_91/1183_nef_threshold/scene.py", "NefThreshold"),
    Video(1184, "対数標準環", "project/math/464_analysis_91/1184_log_canonical_ring/scene.py", "LogCanonicalRing"),
    Video(1185, "RAdamClip", "project/math/465_linear_91/1185_radamclip/scene.py", "RAdamClip"),
    Video(1186, "AdaMaxClip", "project/math/465_linear_91/1186_adamaxclip/scene.py", "AdaMaxClip"),
    Video(1187, "DemonClip", "project/math/465_linear_91/1187_demonclip/scene.py", "DemonClip"),
    Video(1188, "内心傍心外心", "project/math/466_geometry_91/1188_in_ex_circum/scene.py", "InExCircum"),
    Video(1189, "オイラー線比", "project/math/466_geometry_91/1189_euler_line_ratio/scene.py", "EulerLineRatio"),
    Video(1190, "九点円垂心比", "project/math/466_geometry_91/1190_nine_h_ratio/scene.py", "NineHRatio"),
    Video(1191, "ベネット積", "project/math/467_probability_89/1191_bennett_prod/scene.py", "BennettProduct"),
    Video(1192, "アズーマ積", "project/math/467_probability_89/1192_azuma_prod/scene.py", "AzumaProduct"),
    Video(1193, "スティルチェス三角形", "project/math/468_combinatorics_88/1193_stieltjes_triangle/scene.py", "StieltjesTriangle"),
)

VIDEOS_1194_1205: tuple[Video, ...] = (
    Video(1194, "相対標準環", "project/math/469_analysis_92/1194_relative_canonical_ring/scene.py", "RelativeCanonicalRing"),
    Video(1195, "飯高写像再訪", "project/math/469_analysis_92/1195_iitaka_map/scene.py", "IitakaMapRevisit"),
    Video(1196, "豊富閾値", "project/math/469_analysis_92/1196_ample_threshold/scene.py", "AmpleThreshold"),
    Video(1197, "DiffGradSoft", "project/math/470_linear_92/1197_diffgradsoft/scene.py", "DiffGradSoft"),
    Video(1198, "YogiSoft", "project/math/470_linear_92/1198_yogisoft/scene.py", "YogiSoft"),
    Video(1199, "YHClip", "project/math/470_linear_92/1199_yhclip/scene.py", "YHClip"),
    Video(1200, "傍心三角形辺", "project/math/471_geometry_92/1200_ex_tri_side/scene.py", "ExTriSide"),
    Video(1201, "垂心三角形比", "project/math/471_geometry_92/1201_ortho_tri_ratio/scene.py", "OrthoTriRatio"),
    Video(1202, "内心三角形比", "project/math/471_geometry_92/1202_in_tri_ratio/scene.py", "InTriRatio"),
    Video(1203, "ドゥーブ最大", "project/math/472_probability_90/1203_doob_max/scene.py", "DoobMax"),
    Video(1204, "ワルド積", "project/math/472_probability_90/1204_wald_prod/scene.py", "WaldProduct"),
    Video(1205, "アペル多項式", "project/math/473_combinatorics_89/1205_appel_poly/scene.py", "AppelPolynomials"),
)

VIDEOS_1206_1217: tuple[Video, ...] = (
    Video(1206, "交点理論積", "project/math/474_analysis_93/1206_intersection_product/scene.py", "IntersectionProduct"),
    Video(1207, "数値的同値", "project/math/474_analysis_93/1207_numerical_equivalence/scene.py", "NumericalEquivalence"),
    Video(1208, "線形同値差", "project/math/474_analysis_93/1208_linear_equiv_diff/scene.py", "LinearEquivDiff"),
    Video(1209, "AdaFactorClip", "project/math/475_linear_93/1209_adafactorclip/scene.py", "AdaFactorClip"),
    Video(1210, "LAMBClip", "project/math/475_linear_93/1210_lambclip/scene.py", "LAMBClip"),
    Video(1211, "LARSClip", "project/math/475_linear_93/1211_larsclip/scene.py", "LARSClip"),
    Video(1212, "ジェルゴンヌ比", "project/math/476_geometry_93/1212_gergonne_ratio/scene.py", "GergonneRatio"),
    Video(1213, "ナーゲル比", "project/math/476_geometry_93/1213_nagel_ratio/scene.py", "NagelRatio"),
    Video(1214, "シュピカー比", "project/math/476_geometry_93/1214_spieker_ratio/scene.py", "SpiekerRatio"),
    Video(1215, "オプション停止", "project/math/477_probability_91/1215_optional_stopping/scene.py", "OptionalStoppingRevisit"),
    Video(1216, "集中半径", "project/math/477_probability_91/1216_concentration_radius/scene.py", "ConcentrationRadius"),
    Video(1217, "ラグランジュ多項式", "project/math/478_combinatorics_90/1217_lagrange_poly/scene.py", "LagrangePolynomials"),
)

VIDEOS_1218_1229: tuple[Video, ...] = (
    Video(1218, "カルティエ除数", "project/math/479_analysis_94/1218_cartier/scene.py", "CartierDivisor"),
    Video(1219, "ヴェイユ除数", "project/math/479_analysis_94/1219_weil/scene.py", "WeilDivisor"),
    Video(1220, "Q因子", "project/math/479_analysis_94/1220_q_divisor/scene.py", "QDivisor"),
    Video(1221, "AdamWClip", "project/math/480_linear_94/1221_adamwclip/scene.py", "AdamWClip"),
    Video(1222, "SGDMClip", "project/math/480_linear_94/1222_sgdmclip/scene.py", "SGDMClip"),
    Video(1223, "RMSClip", "project/math/480_linear_94/1223_rmsclip/scene.py", "RMSClip"),
    Video(1224, "ミッテンプンクト比", "project/math/481_geometry_94/1224_mittenpunkt_ratio/scene.py", "MittenpunktRatio"),
    Video(1225, "類似重心比", "project/math/481_geometry_94/1225_symmedian_g_ratio/scene.py", "SymmedianGRatio"),
    Video(1226, "類似内心比", "project/math/481_geometry_94/1226_symmedian_i_ratio/scene.py", "SymmedianIRatio"),
    Video(1227, "リプシッツ集中", "project/math/482_probability_92/1227_lipschitz_conc/scene.py", "LipschitzConcentration"),
    Video(1228, "測度集中", "project/math/482_probability_92/1228_measure_conc/scene.py", "MeasureConcentration"),
    Video(1229, "タッチャード多項式", "project/math/483_combinatorics_91/1229_touchard/scene.py", "TouchardPolynomials"),
)

VIDEOS_1230_1241: tuple[Video, ...] = (
    Video(1230, "R因子", "project/math/484_analysis_95/1230_r_divisor/scene.py", "RDivisor"),
    Video(1231, "数値的次元再訪", "project/math/484_analysis_95/1231_num_dim_revisit/scene.py", "NumDimRevisit"),
    Video(1232, "体積多項式", "project/math/484_analysis_95/1232_volume_poly/scene.py", "VolumePolynomial"),
    Video(1233, "AdaBeliefClip", "project/math/485_linear_95/1233_adabeliefclip/scene.py", "AdaBeliefClip"),
    Video(1234, "LookaheadClip", "project/math/485_linear_95/1234_lookaheadclip/scene.py", "LookaheadClip"),
    Video(1235, "SWAClip", "project/math/485_linear_95/1235_swaclip/scene.py", "SWAClip"),
    Video(1236, "類似外心比", "project/math/486_geometry_95/1236_sym_o_ratio/scene.py", "SymORatio"),
    Video(1237, "類似垂心比", "project/math/486_geometry_95/1237_sym_h_ratio/scene.py", "SymHRatio"),
    Video(1238, "ブローカール比", "project/math/486_geometry_95/1238_brocard_ratio/scene.py", "BrocardRatio"),
    Video(1239, "対数ソボレフ", "project/math/487_probability_93/1239_log_sobolev/scene.py", "LogSobolev"),
    Video(1240, "輸送不等式", "project/math/487_probability_93/1240_transport/scene.py", "TransportInequality"),
    Video(1241, "フォア多角形", "project/math/488_combinatorics_92/1241_fuss/scene.py", "FussPolygons"),
)

VIDEOS_1242_1253: tuple[Video, ...] = (
    Video(1242, "ビッグ錐境界", "project/math/489_analysis_96/1242_big_cone_boundary/scene.py", "BigConeBoundary"),
    Video(1243, "移動錐", "project/math/489_analysis_96/1243_movable_cone/scene.py", "MovableCone"),
    Video(1244, "正値錐", "project/math/489_analysis_96/1244_positive_cone/scene.py", "PositiveCone"),
    Video(1245, "ProdigyClip", "project/math/490_linear_96/1245_prodigyclip/scene.py", "ProdigyClip"),
    Video(1246, "ScheduleFreeClip", "project/math/490_linear_96/1246_schedulefreeclip/scene.py", "ScheduleFreeClip"),
    Video(1247, "MuonSoftClip", "project/math/490_linear_96/1247_muonsoftclip/scene.py", "MuonSoftClip"),
    Video(1248, "類似九点比", "project/math/491_geometry_96/1248_sym_nine_ratio/scene.py", "SymNineRatio"),
    Video(1249, "類似傍心比", "project/math/491_geometry_96/1249_sym_ex_ratio/scene.py", "SymExRatio"),
    Video(1250, "類似重心線", "project/math/491_geometry_96/1250_sym_g_line/scene.py", "SymGLine"),
    Video(1251, "ポアンカレ不等式再訪", "project/math/492_probability_94/1251_poincare_revisit/scene.py", "PoincareRevisit"),
    Video(1252, "ガウス型集中", "project/math/492_probability_94/1252_gaussian_conc/scene.py", "GaussianConcentration"),
    Video(1253, "モツキン路細分", "project/math/493_combinatorics_93/1253_motzkin_path_ref/scene.py", "MotzkinPathRefine"),
)

VIDEOS_1254_1265: tuple[Video, ...] = (
    Video(1254, "丸めダウン", "project/math/494_analysis_97/1254_round_down/scene.py", "RoundDown"),
    Video(1255, "丸めアップ", "project/math/494_analysis_97/1255_round_up/scene.py", "RoundUp"),
    Video(1256, "小数部", "project/math/494_analysis_97/1256_fractional_part/scene.py", "FractionalPart"),
    Video(1257, "AdamWSoft", "project/math/495_linear_97/1257_adamwsoft/scene.py", "AdamWSoft"),
    Video(1258, "SGDMSoft", "project/math/495_linear_97/1258_sgdmsoft/scene.py", "SGDMSoft"),
    Video(1259, "RMSSoft", "project/math/495_linear_97/1259_rmssoft/scene.py", "RMSSoft"),
    Video(1260, "類似重心外心", "project/math/496_geometry_97/1260_sym_g_o/scene.py", "SymGO"),
    Video(1261, "ブローカール点比", "project/math/496_geometry_97/1261_brocard_point_ratio/scene.py", "BrocardPointRatio"),
    Video(1262, "第一等角比", "project/math/496_geometry_97/1262_first_isogonic_ratio/scene.py", "FirstIsogonicRatio"),
    Video(1263, "劣ガウス集中", "project/math/497_probability_95/1263_subgaussian/scene.py", "SubgaussianConcentration"),
    Video(1264, "劣指数集中", "project/math/497_probability_95/1264_subexp/scene.py", "SubexponentialConcentration"),
    Video(1265, "ヘッケ三角形", "project/math/498_combinatorics_94/1265_hecke_triangle/scene.py", "HeckeTriangle"),
)

VIDEOS_1266_1277: tuple[Video, ...] = (
    Video(1266, "異なる食い違い", "project/math/499_analysis_98/1266_diff_discrepancy/scene.py", "DifferentDiscrepancy"),
    Video(1267, "最小食い違い", "project/math/499_analysis_98/1267_min_discrepancy/scene.py", "MinDiscrepancy"),
    Video(1268, "対数端末閾値", "project/math/499_analysis_98/1268_lct_revisit/scene.py", "LCTRevisit"),
    Video(1269, "AdaBeliefSoft", "project/math/500_linear_98/1269_adabeliefsoft/scene.py", "AdaBeliefSoft"),
    Video(1270, "LookaheadSoft", "project/math/500_linear_98/1270_lookaheadsoft/scene.py", "LookaheadSoft"),
    Video(1271, "SWASoft", "project/math/500_linear_98/1271_swasoft/scene.py", "SWASoft"),
    Video(1272, "第二等角比", "project/math/501_geometry_98/1272_second_isogonic_ratio/scene.py", "SecondIsogonicRatio"),
    Video(1273, "等角共役比", "project/math/501_geometry_98/1273_isogonal_conj_ratio/scene.py", "IsogonalConjRatio"),
    Video(1274, "等長共役比", "project/math/501_geometry_98/1274_isotomic_conj_ratio/scene.py", "IsotomicConjRatio"),
    Video(1275, "ヘフディング補題再訪", "project/math/502_probability_96/1275_hoeffding_lemma/scene.py", "HoeffdingLemmaRevisit"),
    Video(1276, "チェルノフ法再訪", "project/math/502_probability_96/1276_chernoff_method/scene.py", "ChernoffMethodRevisit"),
    Video(1277, "ガウス三角形", "project/math/503_combinatorics_95/1277_gauss_triangle/scene.py", "GaussTriangle"),
)

VIDEOS_1278_1289: tuple[Video, ...] = (
    Video(1278, "乗法イデアル跳躍", "project/math/504_analysis_99/1278_multiplier_jump/scene.py", "MultiplierJump"),
    Video(1279, "対数解消再訪", "project/math/504_analysis_99/1279_log_res_revisit/scene.py", "LogResRevisit"),
    Video(1280, "単純正規交叉再訪", "project/math/504_analysis_99/1280_snc_revisit/scene.py", "SNCRevisit"),
    Video(1281, "ProdigySoft", "project/math/505_linear_99/1281_prodigysoft/scene.py", "ProdigySoft"),
    Video(1282, "ScheduleFreeSoft", "project/math/505_linear_99/1282_schedulefreesoft/scene.py", "ScheduleFreeSoft"),
    Video(1283, "MuonBoundClip", "project/math/505_linear_99/1283_muonboundclip/scene.py", "MuonBoundClip"),
    Video(1284, "等角線分比", "project/math/506_geometry_99/1284_isogonal_seg_ratio/scene.py", "IsogonalSegRatio"),
    Video(1285, "等長線分比", "project/math/506_geometry_99/1285_isotomic_seg_ratio/scene.py", "IsotomicSegRatio"),
    Video(1286, "チェバ比積", "project/math/506_geometry_99/1286_ceva_ratio_prod/scene.py", "CevaRatioProd"),
    Video(1287, "モーメント母関数再訪", "project/math/507_probability_97/1287_mgf_revisit/scene.py", "MGFRevisit"),
    Video(1288, "キュムラント母関数", "project/math/507_probability_97/1288_cgf/scene.py", "CumulantGenerating"),
    Video(1289, "スターリング三角形細分", "project/math/508_combinatorics_96/1289_stirling_tri_ref/scene.py", "StirlingTriangleRefine"),
)

VIDEOS_1290_1301: tuple[Video, ...] = (
    Video(1290, "端末閾値", "project/math/509_analysis_100/1290_terminal_threshold/scene.py", "TerminalThreshold"),
    Video(1291, "正準閾値", "project/math/509_analysis_100/1291_canonical_threshold/scene.py", "CanonicalThreshold"),
    Video(1292, "klt閾値", "project/math/509_analysis_100/1292_klt_threshold/scene.py", "KLTThreshold"),
    Video(1293, "AdamWHard", "project/math/510_linear_100/1293_adamwhard/scene.py", "AdamWHard"),
    Video(1294, "SGDMHard", "project/math/510_linear_100/1294_sgdmhard/scene.py", "SGDMHard"),
    Video(1295, "RMSHard", "project/math/510_linear_100/1295_rmshard/scene.py", "RMSHard"),
    Video(1296, "メネラウス比積", "project/math/511_geometry_100/1296_menelaus_prod/scene.py", "MenelausProd"),
    Video(1297, "ヴァンオーベル比", "project/math/511_geometry_100/1297_van_obel/scene.py", "VanObelRatio"),
    Video(1298, "ルモワーヌ比", "project/math/511_geometry_100/1298_lemoine_ratio/scene.py", "LemoineRatio"),
    Video(1299, "ラデマッハー複雑度", "project/math/512_probability_98/1299_rademacher/scene.py", "RademacherComplexity"),
    Video(1300, "経験ラデマッハー", "project/math/512_probability_98/1300_empirical_rademacher/scene.py", "EmpiricalRademacher"),
    Video(1301, "フィボナッチ三角形", "project/math/513_combinatorics_97/1301_fib_triangle/scene.py", "FibTriangle"),
)

VIDEOS_1302_1313: tuple[Video, ...] = (
    Video(1302, "plt閾値", "project/math/514_analysis_101/1302_plt_threshold/scene.py", "PLTThreshold"),
    Video(1303, "dlt閾値", "project/math/514_analysis_101/1303_dlt_threshold/scene.py", "DLTThreshold"),
    Video(1304, "lc閾値", "project/math/514_analysis_101/1304_lc_threshold/scene.py", "LCThreshold"),
    Video(1305, "AdaBeliefHard", "project/math/515_linear_101/1305_adabeliefhard/scene.py", "AdaBeliefHard"),
    Video(1306, "LookaheadHard", "project/math/515_linear_101/1306_lookaheadhard/scene.py", "LookaheadHard"),
    Video(1307, "SWAHard", "project/math/515_linear_101/1307_swahard/scene.py", "SWAHard"),
    Video(1308, "類似中線比", "project/math/516_geometry_101/1308_symmedian_ratio/scene.py", "SymmedianRatio"),
    Video(1309, "第一ブロカール比", "project/math/516_geometry_101/1309_first_brocard_ratio/scene.py", "FirstBrocardRatio"),
    Video(1310, "第二ブロカール比", "project/math/516_geometry_101/1310_second_brocard_ratio/scene.py", "SecondBrocardRatio"),
    Video(1311, "一様偏差", "project/math/517_probability_99/1311_uniform_dev/scene.py", "UniformDeviation"),
    Video(1312, "ダドリーエントロピー", "project/math/517_probability_99/1312_dudley/scene.py", "DudleyEntropy"),
    Video(1313, "リュカ三角形", "project/math/518_combinatorics_98/1313_lucas_triangle/scene.py", "LucasTriangle"),
)

VIDEOS_1314_1325: tuple[Video, ...] = (
    Video(1314, "純端末閾値", "project/math/519_analysis_102/1314_pure_terminal/scene.py", "PureTerminalThreshold"),
    Video(1315, "半対数端末", "project/math/519_analysis_102/1315_semi_log_terminal/scene.py", "SemiLogTerminal"),
    Video(1316, "ε対数端末", "project/math/519_analysis_102/1316_eps_log_terminal/scene.py", "EpsLogTerminal"),
    Video(1317, "ProdigyHard", "project/math/520_linear_102/1317_prodigyhard/scene.py", "ProdigyHard"),
    Video(1318, "ScheduleFreeHard", "project/math/520_linear_102/1318_schedulefreehard/scene.py", "ScheduleFreeHard"),
    Video(1319, "MuonSoftBound", "project/math/520_linear_102/1319_muonsoftbound/scene.py", "MuonSoftBound"),
    Video(1320, "チェバ線分比", "project/math/521_geometry_102/1320_ceva_seg_ratio/scene.py", "CevaSegRatio"),
    Video(1321, "メネラウス線分比", "project/math/521_geometry_102/1321_menelaus_seg_ratio/scene.py", "MenelausSegRatio"),
    Video(1322, "スチュワート比", "project/math/521_geometry_102/1322_stewart_ratio/scene.py", "StewartRatio"),
    Video(1323, "チェイニング", "project/math/522_probability_100/1323_chaining/scene.py", "Chaining"),
    Video(1324, "被覆数再訪", "project/math/522_probability_100/1324_covering_revisit/scene.py", "CoveringRevisit"),
    Video(1325, "ペル三角形", "project/math/523_combinatorics_99/1325_pell_triangle/scene.py", "PellTriangle"),
)

VIDEOS_1326_1337: tuple[Video, ...] = (
    Video(1326, "因子的端末", "project/math/524_analysis_103/1326_factorial_terminal/scene.py", "FactorialTerminal"),
    Video(1327, "因子的正準", "project/math/524_analysis_103/1327_factorial_canonical/scene.py", "FactorialCanonical"),
    Video(1328, "因子的klt", "project/math/524_analysis_103/1328_factorial_klt/scene.py", "FactorialKLT"),
    Video(1329, "LionWClip", "project/math/525_linear_103/1329_lionwclip/scene.py", "LionWClip"),
    Video(1330, "SophiaWClip", "project/math/525_linear_103/1330_sophiawclip/scene.py", "SophiaWClip"),
    Video(1331, "MuonWClip", "project/math/525_linear_103/1331_muonwclip/scene.py", "MuonWClip"),
    Video(1332, "スチュワート中線", "project/math/526_geometry_103/1332_stewart_median/scene.py", "StewartMedian"),
    Video(1333, "アポロニウス比", "project/math/526_geometry_103/1333_apollonius_ratio/scene.py", "ApolloniusRatio"),
    Video(1334, "ピタゴラス比拡張", "project/math/526_geometry_103/1334_pythagoras_ext/scene.py", "PythagorasExt"),
    Video(1335, "PAC学習界", "project/math/527_probability_101/1335_pac_bound/scene.py", "PACBound"),
    Video(1336, "VC次元再訪", "project/math/527_probability_101/1336_vc_revisit/scene.py", "VCRevisit"),
    Video(1337, "カタラン細分路", "project/math/528_combinatorics_100/1337_catalan_path_ref/scene.py", "CatalanPathRefine"),
)

VIDEOS_1338_1349: tuple[Video, ...] = (
    Video(1338, "因子的plt", "project/math/529_analysis_104/1338_factorial_plt/scene.py", "FactorialPLT"),
    Video(1339, "因子的dlt", "project/math/529_analysis_104/1339_factorial_dlt/scene.py", "FactorialDLT"),
    Video(1340, "因子的lc", "project/math/529_analysis_104/1340_factorial_lc/scene.py", "FactorialLC"),
    Video(1341, "SOAPWClip", "project/math/530_linear_104/1341_soapwclip/scene.py", "SOAPWClip"),
    Video(1342, "ShampooWClip", "project/math/530_linear_104/1342_shampoowclip/scene.py", "ShampooWClip"),
    Video(1343, "QHMWClip", "project/math/530_linear_104/1343_qhmwclip/scene.py", "QHMWClip"),
    Video(1344, "ヘロン比", "project/math/531_geometry_104/1344_heron_ratio/scene.py", "HeronRatio"),
    Video(1345, "ブレッチナイダー比", "project/math/531_geometry_104/1345_bretschneider/scene.py", "BretschneiderRatio"),
    Video(1346, "カラノイ比", "project/math/531_geometry_104/1346_carnot_ratio/scene.py", "CarnotRatio"),
    Video(1347, "ショック数", "project/math/532_probability_102/1347_shattering/scene.py", "ShatteringNumber"),
    Video(1348, "成長関数", "project/math/532_probability_102/1348_growth_func/scene.py", "GrowthFunction"),
    Video(1349, "ナラヤナ細分", "project/math/533_combinatorics_101/1349_narayana_ref/scene.py", "NarayanaRefine"),
)

VIDEOS_1350_1361: tuple[Video, ...] = (
    Video(1350, "サウアーの補題", "project/math/534_analysis_105/1350_sauer/scene.py", "SauerLemma"),
    Video(1351, "パック数再訪", "project/math/534_analysis_105/1351_packing_revisit/scene.py", "PackingRevisit"),
    Video(1352, "計量エントロピー", "project/math/534_analysis_105/1352_metric_entropy/scene.py", "MetricEntropy"),
    Video(1353, "LionWSoft", "project/math/535_linear_105/1353_lionwsoft/scene.py", "LionWSoft"),
    Video(1354, "SophiaWSoft", "project/math/535_linear_105/1354_sophiawsoft/scene.py", "SophiaWSoft"),
    Video(1355, "MuonWSoft", "project/math/535_linear_105/1355_muonwsoft/scene.py", "MuonWSoft"),
    Video(1356, "キャヴァリエリ比", "project/math/536_geometry_105/1356_cavalieri_ratio/scene.py", "CavalieriRatio"),
    Video(1357, "相似比面積", "project/math/536_geometry_105/1357_sim_area_ratio/scene.py", "SimAreaRatio"),
    Video(1358, "相似比体積", "project/math/536_geometry_105/1358_sim_vol_ratio/scene.py", "SimVolRatio"),
    Video(1359, "経験過程集中", "project/math/537_probability_103/1359_emp_process/scene.py", "EmpiricalProcessConc"),
    Video(1360, "汎化ギャップ", "project/math/537_probability_103/1360_gen_gap/scene.py", "GeneralizationGap"),
    Video(1361, "デラノイ細分", "project/math/538_combinatorics_102/1361_delannoy_ref/scene.py", "DelannoyRefine"),
)

VIDEOS_1362_1373: tuple[Video, ...] = (
    Video(1362, "QQ因子", "project/math/539_analysis_106/1362_qq_divisor/scene.py", "QQDivisor"),
    Video(1363, "RR因子", "project/math/539_analysis_106/1363_rr_divisor/scene.py", "RRDivisor"),
    Video(1364, "混合因子", "project/math/539_analysis_106/1364_mixed_divisor/scene.py", "MixedDivisor"),
    Video(1365, "SOAPWSoft", "project/math/540_linear_106/1365_soapwsoft/scene.py", "SOAPWSoft"),
    Video(1366, "ShampooWSoft", "project/math/540_linear_106/1366_shampoowsoft/scene.py", "ShampooWSoft"),
    Video(1367, "QHMWSoft", "project/math/540_linear_106/1367_qhmwsoft/scene.py", "QHMWSoft"),
    Video(1368, "九点円弦比", "project/math/541_geometry_106/1368_nine_chord_ratio/scene.py", "NineChordRatio"),
    Video(1369, "内心傍接比", "project/math/541_geometry_106/1369_in_excircle_ratio/scene.py", "InExcircleRatio"),
    Video(1370, "傍心外接比", "project/math/541_geometry_106/1370_ex_circum_ratio/scene.py", "ExCircumRatio"),
    Video(1371, "ホフディング再訪", "project/math/542_probability_104/1371_hoeffding_revisit/scene.py", "HoeffdingRevisit"),
    Video(1372, "バーンスタイン再訪", "project/math/542_probability_104/1372_bernstein_revisit/scene.py", "BernsteinRevisit"),
    Video(1373, "大きなカタラン細分", "project/math/543_combinatorics_103/1373_large_catalan_ref/scene.py", "LargeCatalanRefine"),
)

VIDEOS_1374_1385: tuple[Video, ...] = (
    Video(1374, "対数ペア", "project/math/544_analysis_107/1374_log_pair/scene.py", "LogPair"),
    Video(1375, "相対対数ペア", "project/math/544_analysis_107/1375_rel_log_pair/scene.py", "RelLogPair"),
    Video(1376, "準対数端末", "project/math/544_analysis_107/1376_quasi_log/scene.py", "QuasiLogTerminal"),
    Video(1377, "AdaGradSoft", "project/math/545_linear_107/1377_adagradsoft/scene.py", "AdaGradSoft"),
    Video(1378, "NAdamSoft", "project/math/545_linear_107/1378_nadamsoft/scene.py", "NAdamSoft"),
    Video(1379, "RAdamSoft", "project/math/545_linear_107/1379_radamsoft/scene.py", "RAdamSoft"),
    Video(1380, "垂心中線比", "project/math/546_geometry_107/1380_h_median_ratio/scene.py", "HMedianRatio"),
    Video(1381, "重心中線比", "project/math/546_geometry_107/1381_g_median_ratio/scene.py", "GMedianRatio"),
    Video(1382, "内心中線比", "project/math/546_geometry_107/1382_i_median_ratio/scene.py", "IMedianRatio"),
    Video(1383, "ベネット再訪", "project/math/547_probability_105/1383_bennett_revisit/scene.py", "BennettRevisit"),
    Video(1384, "アズーマ再訪", "project/math/547_probability_105/1384_azuma_revisit/scene.py", "AzumaRevisit"),
    Video(1385, "モツキン細分路", "project/math/548_combinatorics_104/1385_motzkin_path_ref2/scene.py", "MotzkinPathRef2"),
)

VIDEOS_1386_1397: tuple[Video, ...] = (
    Video(1386, "スネイドペア", "project/math/549_analysis_108/1386_snc_pair/scene.py", "SNCPair"),
    Video(1387, "純対数ペア", "project/math/549_analysis_108/1387_plt_pair/scene.py", "PLTPair"),
    Video(1388, "端末ペア", "project/math/549_analysis_108/1388_terminal_pair/scene.py", "TerminalPair"),
    Video(1389, "SOAPWHard", "project/math/550_linear_108/1389_soapwhard/scene.py", "SOAPWHard"),
    Video(1390, "ShampooWHard", "project/math/550_linear_108/1390_shampoowhard/scene.py", "ShampooWHard"),
    Video(1391, "QHMWHard", "project/math/550_linear_108/1391_qhmwhard/scene.py", "QHMWHard"),
    Video(1392, "外心中線比", "project/math/551_geometry_108/1392_o_median_ratio/scene.py", "OMedianRatio"),
    Video(1393, "九点中線比", "project/math/551_geometry_108/1393_n_median_ratio/scene.py", "NMedianRatio"),
    Video(1394, "傍心中線比", "project/math/551_geometry_108/1394_ex_median_ratio/scene.py", "ExMedianRatio"),
    Video(1395, "マクディアミド再訪", "project/math/552_probability_106/1395_mcdiarmid_revisit/scene.py", "McDiarmidRevisit"),
    Video(1396, "ブール再訪", "project/math/552_probability_106/1396_boole_revisit/scene.py", "BooleRevisit"),
    Video(1397, "シュレーダー細分", "project/math/553_combinatorics_105/1397_schroeder_ref/scene.py", "SchroederRefine"),
)

VIDEOS_1398_1409: tuple[Video, ...] = (
    Video(1398, "乗法イデアル対", "project/math/554_analysis_109/1398_multiplier_pair/scene.py", "MultiplierPair"),
    Video(1399, "跳躍イデアル対", "project/math/554_analysis_109/1399_jumping_pair/scene.py", "JumpingPair"),
    Video(1400, "対数的閾値対", "project/math/554_analysis_109/1400_lct_pair/scene.py", "LCTPair"),
    Video(1401, "AdaDeltaSoft", "project/math/555_linear_109/1401_adadeltasoft/scene.py", "AdaDeltaSoft"),
    Video(1402, "AdamaxSoft", "project/math/555_linear_109/1402_adamaxsoft/scene.py", "AdamaxSoft"),
    Video(1403, "DemonSoft", "project/math/555_linear_109/1403_demonsoft/scene.py", "DemonSoft"),
    Video(1404, "中線面積比", "project/math/556_geometry_109/1404_median_area_ratio/scene.py", "MedianAreaRatio"),
    Video(1405, "角二等分比", "project/math/556_geometry_109/1405_angle_bisector_ratio/scene.py", "AngleBisectorRatio"),
    Video(1406, "傍接弦比", "project/math/556_geometry_109/1406_ex_tangent_ratio/scene.py", "ExTangentRatio"),
    Video(1407, "経験ラデマッハー再訪", "project/math/557_probability_107/1407_emp_rad_revisit/scene.py", "EmpRadRevisit"),
    Video(1408, "PACベイズ", "project/math/557_probability_107/1408_pac_bayes/scene.py", "PACBayes"),
    Video(1409, "ベル三角形細分", "project/math/558_combinatorics_106/1409_bell_tri_ref/scene.py", "BellTriangleRefine"),
)

VIDEOS_1410_1421: tuple[Video, ...] = (
    Video(1410, "乗法イデアル濾過", "project/math/559_analysis_110/1410_multiplier_filtration/scene.py", "MultiplierFiltration"),
    Video(1411, "跳躍数列", "project/math/559_analysis_110/1411_jumping_sequence/scene.py", "JumpingSequence"),
    Video(1412, "相対LCT", "project/math/559_analysis_110/1412_relative_lct/scene.py", "RelativeLCT"),
    Video(1413, "DiffGradHard", "project/math/560_linear_110/1413_diffgradhard/scene.py", "DiffGradHard"),
    Video(1414, "YogiHard", "project/math/560_linear_110/1414_yogihard/scene.py", "YogiHard"),
    Video(1415, "YHSoft", "project/math/560_linear_110/1415_yhsoft/scene.py", "YHSoft"),
    Video(1416, "接点弦比", "project/math/561_geometry_110/1416_contact_chord_ratio/scene.py", "ContactChordRatio"),
    Video(1417, "垂足弦比", "project/math/561_geometry_110/1417_pedal_chord_ratio/scene.py", "PedalChordRatio"),
    Video(1418, "中点弦比", "project/math/561_geometry_110/1418_midpoint_chord_ratio/scene.py", "MidpointChordRatio"),
    Video(1419, "マージン界", "project/math/562_probability_108/1419_margin_bound/scene.py", "MarginBound"),
    Video(1420, "局所ラデマッハー", "project/math/562_probability_108/1420_local_rademacher/scene.py", "LocalRademacher"),
    Video(1421, "オイラー細分", "project/math/563_combinatorics_107/1421_euler_refine/scene.py", "EulerRefine"),
)

VIDEOS_1422_1433: tuple[Video, ...] = (
    Video(1422, "Nadelイデアル対", "project/math/564_analysis_111/1422_nadel_pair/scene.py", "NadelPair"),
    Video(1423, "川又対", "project/math/564_analysis_111/1423_kawamata_pair/scene.py", "KawamataPair"),
    Video(1424, "端末対の体積", "project/math/564_analysis_111/1424_terminal_volume/scene.py", "TerminalVolume"),
    Video(1425, "AdaFactorSoft", "project/math/565_linear_111/1425_adafactorsoft/scene.py", "AdaFactorSoft"),
    Video(1426, "LAMBSoft", "project/math/565_linear_111/1426_lambsoft/scene.py", "LAMBSoft"),
    Video(1427, "LARSSoft", "project/math/565_linear_111/1427_larssoft/scene.py", "LARSSoft"),
    Video(1428, "角二等分長", "project/math/566_geometry_111/1428_bisector_length/scene.py", "BisectorLength"),
    Video(1429, "中線長比", "project/math/566_geometry_111/1429_median_length_ratio/scene.py", "MedianLengthRatio"),
    Video(1430, "高さ比", "project/math/566_geometry_111/1430_altitude_ratio/scene.py", "AltitudeRatio"),
    Video(1431, "安定性汎化", "project/math/567_probability_109/1431_stability_gen/scene.py", "StabilityGeneralization"),
    Video(1432, "アルゴリズム安定性", "project/math/567_probability_109/1432_alg_stability/scene.py", "AlgorithmicStability"),
    Video(1433, "エルミート細分", "project/math/568_combinatorics_108/1433_hermite_refine/scene.py", "HermiteRefine"),
)

VIDEOS_1434_1445: tuple[Video, ...] = (
    Video(1434, "豊富対", "project/math/569_analysis_112/1434_ample_pair/scene.py", "AmplePair"),
    Video(1435, "ネフ対", "project/math/569_analysis_112/1435_nef_pair/scene.py", "NefPair"),
    Video(1436, "ビッグ対", "project/math/569_analysis_112/1436_big_pair/scene.py", "BigPair"),
    Video(1437, "ProdigySoftClip", "project/math/570_linear_112/1437_prodigysoftclip/scene.py", "ProdigySoftClip"),
    Video(1438, "ScheduleFreeSoftClip", "project/math/570_linear_112/1438_schedulefreesoftclip/scene.py", "ScheduleFreeSoftClip"),
    Video(1439, "MuonSoftHard", "project/math/570_linear_112/1439_muonsofthard/scene.py", "MuonSoftHard"),
    Video(1440, "内心角二等分比", "project/math/571_geometry_112/1440_in_bisector_ratio/scene.py", "InBisectorRatio"),
    Video(1441, "傍心角二等分比", "project/math/571_geometry_112/1441_ex_bisector_ratio/scene.py", "ExBisectorRatio"),
    Video(1442, "外心角二等分比", "project/math/571_geometry_112/1442_o_bisector_ratio/scene.py", "OBisectorRatio"),
    Video(1443, "VCサウアー再訪", "project/math/572_probability_110/1443_vc_sauer_revisit/scene.py", "VCSauerRevisit"),
    Video(1444, "粉砕係数", "project/math/572_probability_110/1444_shattering_coef/scene.py", "ShatteringCoef"),
    Video(1445, "タッチャード細分", "project/math/573_combinatorics_109/1445_touchard_refine/scene.py", "TouchardRefine"),
)

VIDEOS_1446_1457: tuple[Video, ...] = (
    Video(1446, "擬有効対", "project/math/574_analysis_113/1446_psef_pair/scene.py", "PsefPair"),
    Video(1447, "移動対", "project/math/574_analysis_113/1447_movable_pair/scene.py", "MovablePair"),
    Video(1448, "正値対", "project/math/574_analysis_113/1448_positive_pair/scene.py", "PositivePair"),
    Video(1449, "AdaBoundSoft", "project/math/575_linear_113/1449_adaboundsoft/scene.py", "AdaBoundSoft"),
    Video(1450, "LionBoundSoft", "project/math/575_linear_113/1450_lionboundsoft/scene.py", "LionBoundSoft"),
    Video(1451, "SophiaBoundSoft", "project/math/575_linear_113/1451_sophiaboundsoft/scene.py", "SophiaBoundSoft"),
    Video(1452, "垂心角二等分比", "project/math/576_geometry_113/1452_h_bisector_ratio/scene.py", "HBisectorRatio"),
    Video(1453, "重心角二等分比", "project/math/576_geometry_113/1453_g_bisector_ratio/scene.py", "GBisectorRatio"),
    Video(1454, "九点角二等分比", "project/math/576_geometry_113/1454_n_bisector_ratio/scene.py", "NBisectorRatio"),
    Video(1455, "成長多項式", "project/math/577_probability_111/1455_growth_poly/scene.py", "GrowthPolynomial"),
    Video(1456, "ネット近似", "project/math/577_probability_111/1456_net_approx/scene.py", "NetApproximation"),
    Video(1457, "フォア細分", "project/math/578_combinatorics_110/1457_fuss_refine/scene.py", "FussRefine"),
)

VIDEOS_1458_1469: tuple[Video, ...] = (
    Video(1458, "体積対", "project/math/579_analysis_114/1458_volume_pair/scene.py", "VolumePair"),
    Video(1459, "数値的次元対", "project/math/579_analysis_114/1459_num_dim_pair/scene.py", "NumDimPair"),
    Video(1460, "飯高次元対", "project/math/579_analysis_114/1460_iitaka_pair/scene.py", "IitakaPair"),
    Video(1461, "AdaBoundHard", "project/math/580_linear_114/1461_adaboundhard/scene.py", "AdaBoundHard"),
    Video(1462, "LionBoundHard", "project/math/580_linear_114/1462_lionboundhard/scene.py", "LionBoundHard"),
    Video(1463, "SophiaBoundHard", "project/math/580_linear_114/1463_sophiaboundhard/scene.py", "SophiaBoundHard"),
    Video(1464, "内心高さ比", "project/math/581_geometry_114/1464_in_altitude_ratio/scene.py", "InAltitudeRatio"),
    Video(1465, "傍心高さ比", "project/math/581_geometry_114/1465_ex_altitude_ratio/scene.py", "ExAltitudeRatio"),
    Video(1466, "外心高さ比", "project/math/581_geometry_114/1466_o_altitude_ratio/scene.py", "OAltitudeRatio"),
    Video(1467, "イプシロンネット", "project/math/582_probability_112/1467_epsilon_net/scene.py", "EpsilonNet"),
    Video(1468, "チャイニング再訪", "project/math/582_probability_112/1468_chaining_revisit/scene.py", "ChainingRevisit"),
    Video(1469, "アペル細分", "project/math/583_combinatorics_111/1469_appel_refine/scene.py", "AppelRefine"),
)

VIDEOS_1470_1481: tuple[Video, ...] = (
    Video(1470, "相対豊富対", "project/math/584_analysis_115/1470_rel_ample_pair/scene.py", "RelAmplePair"),
    Video(1471, "相対ネフ対", "project/math/584_analysis_115/1471_rel_nef_pair/scene.py", "RelNefPair"),
    Video(1472, "相対ビッグ対", "project/math/584_analysis_115/1472_rel_big_pair/scene.py", "RelBigPair"),
    Video(1473, "NAdamSoftClip", "project/math/585_linear_115/1473_nadamsoftclip/scene.py", "NAdamSoftClip"),
    Video(1474, "NAdamHardClip", "project/math/585_linear_115/1474_nadamhardclip/scene.py", "NAdamHardClip"),
    Video(1475, "NAdamSoftHard", "project/math/585_linear_115/1475_nadamsofthard/scene.py", "NAdamSoftHard"),
    Video(1476, "内心類似中線比", "project/math/586_geometry_115/1476_in_symmedian_ratio/scene.py", "InSymmedianRatio"),
    Video(1477, "傍心類似中線比", "project/math/586_geometry_115/1477_ex_symmedian_ratio/scene.py", "ExSymmedianRatio"),
    Video(1478, "外心類似中線比", "project/math/586_geometry_115/1478_o_symmedian_ratio/scene.py", "OSymmedianRatio"),
    Video(1479, "ラデマッハ再訪", "project/math/587_probability_113/1479_rademacher_revisit/scene.py", "RademacherRevisit"),
    Video(1480, "ガウス複雑度", "project/math/587_probability_113/1480_gaussian_complexity/scene.py", "GaussianComplexity"),
    Video(1481, "ラグランジュ細分", "project/math/588_combinatorics_112/1481_lagrange_refine/scene.py", "LagrangeRefine"),
)

VIDEOS_1482_1493: tuple[Video, ...] = (
    Video(1482, "純端末対", "project/math/589_analysis_116/1482_plt_pair/scene.py", "PltPair"),
    Video(1483, "純標準対", "project/math/589_analysis_116/1483_klt_pair/scene.py", "KltPair"),
    Video(1484, "カノニカル対", "project/math/589_analysis_116/1484_canonical_pair/scene.py", "CanonicalPair"),
    Video(1485, "LARSSoftClip", "project/math/590_linear_116/1485_larssoftclip/scene.py", "LARSSoftClip"),
    Video(1486, "LARSHardClip", "project/math/590_linear_116/1486_larshardclip/scene.py", "LARSHardClip"),
    Video(1487, "LAMBSoftClip", "project/math/590_linear_116/1487_lambsoftclip/scene.py", "LAMBSoftClip"),
    Video(1488, "垂心類似中線比", "project/math/591_geometry_116/1488_h_symmedian_ratio/scene.py", "HSymmedianRatio"),
    Video(1489, "重心類似中線比", "project/math/591_geometry_116/1489_g_symmedian_ratio/scene.py", "GSymmedianRatio"),
    Video(1490, "九点類似中線比", "project/math/591_geometry_116/1490_n_symmedian_ratio/scene.py", "NSymmedianRatio"),
    Video(1491, "ダドリー積分", "project/math/592_probability_114/1491_dudley_integral/scene.py", "DudleyIntegral"),
    Video(1492, "経験被覆数", "project/math/592_probability_114/1492_empirical_covering/scene.py", "EmpiricalCovering"),
    Video(1493, "ナーラヤナ細分", "project/math/593_combinatorics_113/1493_narayana_refine/scene.py", "NarayanaRefine"),
)

VIDEOS_1494_1505: tuple[Video, ...] = (
    Video(1494, "フリップ対", "project/math/594_analysis_117/1494_flip_pair/scene.py", "FlipPair"),
    Video(1495, "フロップ対", "project/math/594_analysis_117/1495_flop_pair/scene.py", "FlopPair"),
    Video(1496, "収縮対", "project/math/594_analysis_117/1496_contraction_pair/scene.py", "ContractionPair"),
    Video(1497, "ApolloSoft", "project/math/595_linear_117/1497_apollosoft/scene.py", "ApolloSoft"),
    Video(1498, "ApolloHard", "project/math/595_linear_117/1498_apollohard/scene.py", "ApolloHard"),
    Video(1499, "ApolloClip", "project/math/595_linear_117/1499_apolloclip/scene.py", "ApolloClip"),
    Video(1500, "内心傍接円比", "project/math/596_geometry_117/1500_in_excircle_ratio/scene.py", "InExcircleRatio"),
    Video(1501, "傍心傍接円比", "project/math/596_geometry_117/1501_ex_excircle_ratio/scene.py", "ExExcircleRatio"),
    Video(1502, "外心傍接円比", "project/math/596_geometry_117/1502_o_excircle_ratio/scene.py", "OExcircleRatio"),
    Video(1503, "局所被覆数", "project/math/597_probability_115/1503_local_covering/scene.py", "LocalCovering"),
    Video(1504, "一様エントロピー", "project/math/597_probability_115/1504_uniform_entropy/scene.py", "UniformEntropy"),
    Video(1505, "フィボナッチ細分", "project/math/598_combinatorics_114/1505_fibonacci_refine/scene.py", "FibonacciRefine"),
)

VIDEOS_1506_1517: tuple[Video, ...] = (
    Video(1506, "相対純端末対", "project/math/599_analysis_118/1506_rel_plt_pair/scene.py", "RelPltPair"),
    Video(1507, "相対純標準対", "project/math/599_analysis_118/1507_rel_klt_pair/scene.py", "RelKltPair"),
    Video(1508, "相対カノニカル対", "project/math/599_analysis_118/1508_rel_canonical_pair/scene.py", "RelCanonicalPair"),
    Video(1509, "ScheduleFreeBound", "project/math/600_linear_118/1509_schedulefreebound/scene.py", "ScheduleFreeBound"),
    Video(1510, "ProdigyBound", "project/math/600_linear_118/1510_prodigybound/scene.py", "ProdigyBound"),
    Video(1511, "ProdigyHardClip", "project/math/600_linear_118/1511_prodigyhardclip/scene.py", "ProdigyHardClip"),
    Video(1512, "垂心傍接円比", "project/math/601_geometry_118/1512_h_excircle_ratio/scene.py", "HExcircleRatio"),
    Video(1513, "重心傍接円比", "project/math/601_geometry_118/1513_g_excircle_ratio/scene.py", "GExcircleRatio"),
    Video(1514, "九点傍接円比", "project/math/601_geometry_118/1514_n_excircle_ratio/scene.py", "NExcircleRatio"),
    Video(1515, "劣ガウス再訪", "project/math/602_probability_116/1515_subgaussian_revisit/scene.py", "SubgaussianRevisit"),
    Video(1516, "ヘフディング再訪", "project/math/602_probability_116/1516_hoeffding_revisit/scene.py", "HoeffdingRevisit"),
    Video(1517, "リュカ細分", "project/math/603_combinatorics_115/1517_lucas_refine/scene.py", "LucasRefine"),
)

VIDEOS_1518_1529: tuple[Video, ...] = (
    Video(1518, "対数端末対", "project/math/604_analysis_119/1518_log_terminal_pair/scene.py", "LogTerminalPair"),
    Video(1519, "対数標準対", "project/math/604_analysis_119/1519_log_canonical_pair/scene.py", "LogCanonicalPair"),
    Video(1520, "対数カノニカル対", "project/math/604_analysis_119/1520_log_can_pair/scene.py", "LogCanPair"),
    Video(1521, "MuonHardClip", "project/math/605_linear_119/1521_muonhardclip/scene.py", "MuonHardClip"),
    Video(1522, "SamHardClip", "project/math/605_linear_119/1522_samhardclip/scene.py", "SamHardClip"),
    Video(1523, "AdamWHardClip", "project/math/605_linear_119/1523_adamwhardclip/scene.py", "AdamWHardClip"),
    Video(1524, "内心ジェルゴンヌ比", "project/math/606_geometry_119/1524_in_gergonne_ratio/scene.py", "InGergonneRatio"),
    Video(1525, "傍心ナーゲル比", "project/math/606_geometry_119/1525_ex_nagel_ratio/scene.py", "ExNagelRatio"),
    Video(1526, "外心ミッテン比", "project/math/606_geometry_119/1526_o_mitten_ratio/scene.py", "OMittenRatio"),
    Video(1527, "アズラ再訪", "project/math/607_probability_117/1527_azuma_revisit/scene.py", "AzumaRevisit"),
    Video(1528, "タルラール再訪", "project/math/607_probability_117/1528_talagrand_revisit/scene.py", "TalagrandRevisit"),
    Video(1529, "ペル細分", "project/math/608_combinatorics_116/1529_pell_refine/scene.py", "PellRefine"),
)

VIDEOS_1530_1541: tuple[Video, ...] = (
    Video(1530, "相対フリップ対", "project/math/609_analysis_120/1530_rel_flip_pair/scene.py", "RelFlipPair"),
    Video(1531, "相対フロップ対", "project/math/609_analysis_120/1531_rel_flop_pair/scene.py", "RelFlopPair"),
    Video(1532, "相対収縮対", "project/math/609_analysis_120/1532_rel_contraction_pair/scene.py", "RelContractionPair"),
    Video(1533, "AdamWSoftClip", "project/math/610_linear_120/1533_adamwsoftclip/scene.py", "AdamWSoftClip"),
    Video(1534, "LionWHard", "project/math/610_linear_120/1534_lionwhard/scene.py", "LionWHard"),
    Video(1535, "AdaFactorHard", "project/math/610_linear_120/1535_adafactorhard/scene.py", "AdaFactorHard"),
    Video(1536, "内心スピーカー比", "project/math/611_geometry_120/1536_in_spieker_ratio/scene.py", "InSpiekerRatio"),
    Video(1537, "傍心スピーカー比", "project/math/611_geometry_120/1537_ex_spieker_ratio/scene.py", "ExSpiekerRatio"),
    Video(1538, "外心スピーカー比", "project/math/611_geometry_120/1538_o_spieker_ratio/scene.py", "OSpiekerRatio"),
    Video(1539, "パッキング数", "project/math/612_probability_118/1539_packing_number/scene.py", "PackingNumber"),
    Video(1540, "メトリックエントロピー", "project/math/612_probability_118/1540_metric_entropy/scene.py", "MetricEntropy"),
    Video(1541, "ゼッケンドルフ細分", "project/math/613_combinatorics_117/1541_zeckendorf_refine/scene.py", "ZeckendorfRefine"),
)

VIDEOS_1542_1553: tuple[Video, ...] = (
    Video(1542, "端末対", "project/math/614_analysis_121/1542_terminal_pair/scene.py", "TerminalPair"),
    Video(1543, "標準対", "project/math/614_analysis_121/1543_canonical_sing_pair/scene.py", "CanonicalSingPair"),
    Video(1544, "ログ豊富対", "project/math/614_analysis_121/1544_log_ample_pair/scene.py", "LogAmplePair"),
    Video(1545, "SAMSoftClip", "project/math/615_linear_121/1545_samsoftclip/scene.py", "SAMSoftClip"),
    Video(1546, "SAMSoftHard", "project/math/615_linear_121/1546_samsofthard/scene.py", "SAMSoftHard"),
    Video(1547, "LookaheadSoftClip", "project/math/615_linear_121/1547_lookaheadsoftclip/scene.py", "LookaheadSoftClip"),
    Video(1548, "垂心スピーカー比", "project/math/616_geometry_121/1548_h_spieker_ratio/scene.py", "HSpiekerRatio"),
    Video(1549, "重心スピーカー比", "project/math/616_geometry_121/1549_g_spieker_ratio/scene.py", "GSpiekerRatio"),
    Video(1550, "九点スピーカー比", "project/math/616_geometry_121/1550_n_spieker_ratio/scene.py", "NSpiekerRatio"),
    Video(1551, "マッカーサー再訪", "project/math/617_probability_119/1551_mcdiarmid_revisit/scene.py", "McDiarmidRevisit"),
    Video(1552, "経験エントロピー", "project/math/617_probability_119/1552_empirical_entropy/scene.py", "EmpiricalEntropy"),
    Video(1553, "トリボナッチ細分", "project/math/618_combinatorics_118/1553_tribonacci_refine/scene.py", "TribonacciRefine"),
)

VIDEOS_1554_1565: tuple[Video, ...] = (
    Video(1554, "ログネフ対", "project/math/619_analysis_122/1554_log_nef_pair/scene.py", "LogNefPair"),
    Video(1555, "ログビッグ対", "project/math/619_analysis_122/1555_log_big_pair/scene.py", "LogBigPair"),
    Video(1556, "ログ擬有効対", "project/math/619_analysis_122/1556_log_psef_pair/scene.py", "LogPsefPair"),
    Video(1557, "LAMBHardClip", "project/math/620_linear_122/1557_lambhardclip/scene.py", "LAMBHardClip"),
    Video(1558, "LARSBound", "project/math/620_linear_122/1558_larsbound/scene.py", "LARSBound"),
    Video(1559, "MuonBoundSoft", "project/math/620_linear_122/1559_muonboundsoft/scene.py", "MuonBoundSoft"),
    Video(1560, "内心シュタイナー比", "project/math/621_geometry_122/1560_in_steiner_ratio/scene.py", "InSteinerRatio"),
    Video(1561, "傍心シュタイナー比", "project/math/621_geometry_122/1561_ex_steiner_ratio/scene.py", "ExSteinerRatio"),
    Video(1562, "外心シュタイナー比", "project/math/621_geometry_122/1562_o_steiner_ratio/scene.py", "OSteinerRatio"),
    Video(1563, "局所ラデマッハ再訪", "project/math/622_probability_120/1563_local_rademacher_revisit/scene.py", "LocalRademacherRevisit"),
    Video(1564, "鎖状エントロピー", "project/math/622_probability_120/1564_chaining_entropy/scene.py", "ChainingEntropy"),
    Video(1565, "テトラナッチ細分", "project/math/623_combinatorics_119/1565_tetranacci_refine/scene.py", "TetranacciRefine"),
)

VIDEOS_1566_1577: tuple[Video, ...] = (
    Video(1566, "相対端末対", "project/math/624_analysis_123/1566_rel_terminal_pair/scene.py", "RelTerminalPair"),
    Video(1567, "相対標準対", "project/math/624_analysis_123/1567_rel_can_sing_pair/scene.py", "RelCanSingPair"),
    Video(1568, "相対ログ豊富対", "project/math/624_analysis_123/1568_rel_log_ample_pair/scene.py", "RelLogAmplePair"),
    Video(1569, "ProdigySoftHard", "project/math/625_linear_123/1569_prodigysofthard/scene.py", "ProdigySoftHard"),
    Video(1570, "ScheduleFreeHardClip", "project/math/625_linear_123/1570_schedulefreehardclip/scene.py", "ScheduleFreeHardClip"),
    Video(1571, "SophiaWHard", "project/math/625_linear_123/1571_sophiawhard/scene.py", "SophiaWHard"),
    Video(1572, "垂心ジェルゴンヌ比", "project/math/626_geometry_123/1572_h_gergonne_ratio/scene.py", "HGergonneRatio"),
    Video(1573, "重心ナーゲル比", "project/math/626_geometry_123/1573_g_nagel_ratio/scene.py", "GNagelRatio"),
    Video(1574, "九点ミッテン比", "project/math/626_geometry_123/1574_n_mitten_ratio/scene.py", "NMittenRatio"),
    Video(1575, "双対被覆数", "project/math/627_probability_121/1575_dual_covering/scene.py", "DualCovering"),
    Video(1576, "スケール敏感度", "project/math/627_probability_121/1576_scale_sensitivity/scene.py", "ScaleSensitivity"),
    Video(1577, "大きなフィボナッチ細分", "project/math/628_combinatorics_120/1577_large_fib_refine/scene.py", "LargeFibRefine"),
)

VIDEOS_1578_1589: tuple[Video, ...] = (
    Video(1578, "ログ移動対", "project/math/629_analysis_124/1578_log_movable_pair/scene.py", "LogMovablePair"),
    Video(1579, "ログ正値対", "project/math/629_analysis_124/1579_log_positive_pair/scene.py", "LogPositivePair"),
    Video(1580, "ログ体積対", "project/math/629_analysis_124/1580_log_volume_pair/scene.py", "LogVolumePair"),
    Video(1581, "RMSSoftClip", "project/math/630_linear_124/1581_rmssoftclip/scene.py", "RMSSoftClip"),
    Video(1582, "RMSHardClip", "project/math/630_linear_124/1582_rmshardclip/scene.py", "RMSHardClip"),
    Video(1583, "LionSoftHard", "project/math/630_linear_124/1583_lionsofthard/scene.py", "LionSoftHard"),
    Video(1584, "垂心シュタイナー比", "project/math/631_geometry_124/1584_h_steiner_ratio/scene.py", "HSteinerRatio"),
    Video(1585, "重心シュタイナー比", "project/math/631_geometry_124/1585_g_steiner_ratio/scene.py", "GSteinerRatio"),
    Video(1586, "九点シュタイナー比", "project/math/631_geometry_124/1586_n_steiner_ratio/scene.py", "NSteinerRatio"),
    Video(1587, "ベンネット再訪", "project/math/632_probability_122/1587_bennett_revisit/scene.py", "BennettRevisit"),
    Video(1588, "ブールガンディ再訪", "project/math/632_probability_122/1588_bousquet_revisit/scene.py", "BousquetRevisit"),
    Video(1589, "ツリー細分", "project/math/633_combinatorics_121/1589_tree_refine/scene.py", "TreeRefine"),
)

VIDEOS_1590_1601: tuple[Video, ...] = (
    Video(1590, "相対ログネフ対", "project/math/634_analysis_125/1590_rel_log_nef_pair/scene.py", "RelLogNefPair"),
    Video(1591, "相対ログビッグ対", "project/math/634_analysis_125/1591_rel_log_big_pair/scene.py", "RelLogBigPair"),
    Video(1592, "相対ログ擬有効対", "project/math/634_analysis_125/1592_rel_log_psef_pair/scene.py", "RelLogPsefPair"),
    Video(1593, "AdaFactorBound", "project/math/635_linear_125/1593_adafactorbound/scene.py", "AdaFactorBound"),
    Video(1594, "NAdamBound", "project/math/635_linear_125/1594_nadambound/scene.py", "NAdamBound"),
    Video(1595, "LookaheadHardClip", "project/math/635_linear_125/1595_lookaheadhardclip/scene.py", "LookaheadHardClip"),
    Video(1596, "内心類似ジェルゴンヌ比", "project/math/636_geometry_125/1596_in_sym_gergonne_ratio/scene.py", "InSymGergonneRatio"),
    Video(1597, "傍心類似ナーゲル比", "project/math/636_geometry_125/1597_ex_sym_nagel_ratio/scene.py", "ExSymNagelRatio"),
    Video(1598, "外心類似ミッテン比", "project/math/636_geometry_125/1598_o_sym_mitten_ratio/scene.py", "OSymMittenRatio"),
    Video(1599, "経験パッキング", "project/math/637_probability_123/1599_empirical_packing/scene.py", "EmpiricalPacking"),
    Video(1600, "局所エントロピー", "project/math/637_probability_123/1600_local_entropy/scene.py", "LocalEntropy"),
    Video(1601, "森細分", "project/math/638_combinatorics_122/1601_forest_refine/scene.py", "ForestRefine"),
)

VIDEOS_1602_1613: tuple[Video, ...] = (
    Video(1602, "ログ数値次元対", "project/math/639_analysis_126/1602_log_num_dim_pair/scene.py", "LogNumDimPair"),
    Video(1603, "ログ飯高次元対", "project/math/639_analysis_126/1603_log_iitaka_pair/scene.py", "LogIitakaPair"),
    Video(1604, "相対ログ移動対", "project/math/639_analysis_126/1604_rel_log_movable_pair/scene.py", "RelLogMovablePair"),
    Video(1605, "MuonBoundHard", "project/math/640_linear_126/1605_muonboundhard/scene.py", "MuonBoundHard"),
    Video(1606, "ProdigyBoundSoft", "project/math/640_linear_126/1606_prodigyboundsoft/scene.py", "ProdigyBoundSoft"),
    Video(1607, "ScheduleFreeSoftHard", "project/math/640_linear_126/1607_schedulefreesofthard/scene.py", "ScheduleFreeSoftHard"),
    Video(1608, "内心オイラー比", "project/math/641_geometry_126/1608_in_euler_ratio/scene.py", "InEulerRatio"),
    Video(1609, "傍心オイラー比", "project/math/641_geometry_126/1609_ex_euler_ratio/scene.py", "ExEulerRatio"),
    Video(1610, "外心オイラー比", "project/math/641_geometry_126/1610_o_euler_ratio/scene.py", "OEulerRatio"),
    Video(1611, "一様被覆数", "project/math/642_probability_124/1611_uniform_covering/scene.py", "UniformCovering"),
    Video(1612, "ピネリス再訪", "project/math/642_probability_124/1612_pinelis_revisit/scene.py", "PinelisRevisit"),
    Video(1613, "平面木細分", "project/math/643_combinatorics_123/1613_plane_tree_refine/scene.py", "PlaneTreeRefine"),
)

VIDEOS_1614_1625: tuple[Video, ...] = (
    Video(1614, "相対ログ正値対", "project/math/644_analysis_127/1614_rel_log_positive_pair/scene.py", "RelLogPositivePair"),
    Video(1615, "相対ログ体積対", "project/math/644_analysis_127/1615_rel_log_volume_pair/scene.py", "RelLogVolumePair"),
    Video(1616, "ログ収縮対", "project/math/644_analysis_127/1616_log_contraction_pair/scene.py", "LogContractionPair"),
    Video(1617, "AdamWBoundSoft", "project/math/645_linear_127/1617_adamwboundsoft/scene.py", "AdamWBoundSoft"),
    Video(1618, "LionBoundClip", "project/math/645_linear_127/1618_lionboundclip/scene.py", "LionBoundClip"),
    Video(1619, "SophiaBoundClip", "project/math/645_linear_127/1619_sophiaboundclip/scene.py", "SophiaBoundClip"),
    Video(1620, "垂心オイラー比", "project/math/646_geometry_127/1620_h_euler_ratio/scene.py", "HEulerRatio"),
    Video(1621, "重心オイラー比", "project/math/646_geometry_127/1621_g_euler_ratio/scene.py", "GEulerRatio"),
    Video(1622, "九点オイラー比", "project/math/646_geometry_127/1622_n_euler_ratio/scene.py", "NEulerRatio"),
    Video(1623, "経験チャイニング", "project/math/647_probability_125/1623_empirical_chaining/scene.py", "EmpiricalChaining"),
    Video(1624, "局所パッキング", "project/math/647_probability_125/1624_local_packing/scene.py", "LocalPacking"),
    Video(1625, "ホフスタッター細分", "project/math/648_combinatorics_124/1625_hofstadter_refine/scene.py", "HofstadterRefine"),
)

VIDEOS_1626_1637: tuple[Video, ...] = (
    Video(1626, "相対ログ数値次元対", "project/math/649_analysis_128/1626_rel_log_num_dim/scene.py", "RelLogNumDim"),
    Video(1627, "相対ログ飯高次元対", "project/math/649_analysis_128/1627_rel_log_iitaka/scene.py", "RelLogIitaka"),
    Video(1628, "ログフリップ対", "project/math/649_analysis_128/1628_log_flip_pair/scene.py", "LogFlipPair"),
    Video(1629, "AdaFactorSoftHard", "project/math/650_linear_128/1629_adafactorsofthard/scene.py", "AdaFactorSoftHard"),
    Video(1630, "NAdamSoftBound", "project/math/650_linear_128/1630_nadamsoftbound/scene.py", "NAdamSoftBound"),
    Video(1631, "RMSBoundSoft", "project/math/650_linear_128/1631_rmsboundsoft/scene.py", "RMSBoundSoft"),
    Video(1632, "内心類似スピーカー比", "project/math/651_geometry_128/1632_in_sym_spieker_ratio/scene.py", "InSymSpiekerRatio"),
    Video(1633, "傍心類似スピーカー比", "project/math/651_geometry_128/1633_ex_sym_spieker_ratio/scene.py", "ExSymSpiekerRatio"),
    Video(1634, "外心類似スピーカー比", "project/math/651_geometry_128/1634_o_sym_spieker_ratio/scene.py", "OSymSpiekerRatio"),
    Video(1635, "一様パッキング", "project/math/652_probability_126/1635_uniform_packing/scene.py", "UniformPacking"),
    Video(1636, "劣指数再訪", "project/math/652_probability_126/1636_subexp_revisit/scene.py", "SubexpRevisit"),
    Video(1637, "ディセクト細分", "project/math/653_combinatorics_125/1637_dissect_refine/scene.py", "DissectRefine"),
)

VIDEOS_1638_1649: tuple[Video, ...] = (
    Video(1638, "相対ログ収縮対", "project/math/654_analysis_129/1638_rel_log_contraction/scene.py", "RelLogContraction"),
    Video(1639, "相対ログフリップ対", "project/math/654_analysis_129/1639_rel_log_flip/scene.py", "RelLogFlip"),
    Video(1640, "ログフロップ対", "project/math/654_analysis_129/1640_log_flop_pair/scene.py", "LogFlopPair"),
    Video(1641, "AdamWSoftHard", "project/math/655_linear_129/1641_adamwsofthard/scene.py", "AdamWSoftHard"),
    Video(1642, "LookaheadBound", "project/math/655_linear_129/1642_lookaheadbound/scene.py", "LookaheadBound"),
    Video(1643, "SAMBoundSoft", "project/math/655_linear_129/1643_samboundsoft/scene.py", "SAMBoundSoft"),
    Video(1644, "垂心類似スピーカー比", "project/math/656_geometry_129/1644_h_sym_spieker_ratio/scene.py", "HSymSpiekerRatio"),
    Video(1645, "重心類似スピーカー比", "project/math/656_geometry_129/1645_g_sym_spieker_ratio/scene.py", "GSymSpiekerRatio"),
    Video(1646, "九点類似スピーカー比", "project/math/656_geometry_129/1646_n_sym_spieker_ratio/scene.py", "NSymSpiekerRatio"),
    Video(1647, "有界差再訪", "project/math/657_probability_127/1647_bounded_diff_revisit/scene.py", "BoundedDiffRevisit"),
    Video(1648, "ベクトル集中再訪", "project/math/657_probability_127/1648_vector_conc_revisit/scene.py", "VectorConcRevisit"),
    Video(1649, "カータラン路細分", "project/math/658_combinatorics_126/1649_catalan_path_refine/scene.py", "CatalanPathRefine"),
)

VIDEOS_1650_1661: tuple[Video, ...] = (
    Video(1650, "相対ログフロップ対", "project/math/659_analysis_130/1650_rel_log_flop/scene.py", "RelLogFlop"),
    Video(1651, "ログ極小モデル対", "project/math/659_analysis_130/1651_log_mmp_pair/scene.py", "LogMmpPair"),
    Video(1652, "相対ログ極小モデル対", "project/math/659_analysis_130/1652_rel_log_mmp/scene.py", "RelLogMmp"),
    Video(1653, "LionWSoftClip", "project/math/660_linear_130/1653_lionwsoftclip/scene.py", "LionWSoftClip"),
    Video(1654, "SophiaWSoftClip", "project/math/660_linear_130/1654_sophiawsoftclip/scene.py", "SophiaWSoftClip"),
    Video(1655, "AdaFactorHardClip", "project/math/660_linear_130/1655_adafactorhardclip/scene.py", "AdaFactorHardClip"),
    Video(1656, "内心フォイエルバッハ比", "project/math/661_geometry_130/1656_in_feuerbach_ratio/scene.py", "InFeuerbachRatio"),
    Video(1657, "傍心フォイエルバッハ比", "project/math/661_geometry_130/1657_ex_feuerbach_ratio/scene.py", "ExFeuerbachRatio"),
    Video(1658, "外心フォイエルバッハ比", "project/math/661_geometry_130/1658_o_feuerbach_ratio/scene.py", "OFeuerbachRatio"),
    Video(1659, "経験劣ガウス", "project/math/662_probability_128/1659_empirical_subgauss/scene.py", "EmpiricalSubgauss"),
    Video(1660, "局所チャイニング", "project/math/662_probability_128/1660_local_chaining/scene.py", "LocalChaining"),
    Video(1661, "根つき木細分", "project/math/663_combinatorics_127/1661_rooted_tree_refine/scene.py", "RootedTreeRefine"),
)

VIDEOS_1662_1673: tuple[Video, ...] = (
    Video(1662, "ログ終端対", "project/math/664_analysis_131/1662_log_terminal_model/scene.py", "LogTerminalModel"),
    Video(1663, "相対ログ終端対", "project/math/664_analysis_131/1663_rel_log_terminal_model/scene.py", "RelLogTerminalModel"),
    Video(1664, "ログ安定対", "project/math/664_analysis_131/1664_log_stable_pair/scene.py", "LogStablePair"),
    Video(1665, "NAdamBoundHard", "project/math/665_linear_131/1665_nadamboundhard/scene.py", "NAdamBoundHard"),
    Video(1666, "RMSBoundHard", "project/math/665_linear_131/1666_rmsboundhard/scene.py", "RMSBoundHard"),
    Video(1667, "LookaheadSoftHard", "project/math/665_linear_131/1667_lookaheadsofthard/scene.py", "LookaheadSoftHard"),
    Video(1668, "垂心フォイエルバッハ比", "project/math/666_geometry_131/1668_h_feuerbach_ratio/scene.py", "HFeuerbachRatio"),
    Video(1669, "重心フォイエルバッハ比", "project/math/666_geometry_131/1669_g_feuerbach_ratio/scene.py", "GFeuerbachRatio"),
    Video(1670, "九点フォイエルバッハ比", "project/math/666_geometry_131/1670_n_feuerbach_ratio/scene.py", "NFeuerbachRatio"),
    Video(1671, "一様チャイニング", "project/math/667_probability_129/1671_uniform_chaining/scene.py", "UniformChaining"),
    Video(1672, "スケールエントロピー", "project/math/667_probability_129/1672_scale_entropy/scene.py", "ScaleEntropy"),
    Video(1673, "二分木細分", "project/math/668_combinatorics_128/1673_binary_tree_refine/scene.py", "BinaryTreeRefine"),
)

VIDEOS_1674_1685: tuple[Video, ...] = (
    Video(1674, "ログ半安定対", "project/math/669_analysis_132/1674_log_semistable_pair/scene.py", "LogSemistablePair"),
    Video(1675, "相対ログ安定対", "project/math/669_analysis_132/1675_rel_log_stable_pair/scene.py", "RelLogStablePair"),
    Video(1676, "ログ簡約対", "project/math/669_analysis_132/1676_log_slc_pair/scene.py", "LogSlcPair"),
    Video(1677, "SAMBoundHard", "project/math/670_linear_132/1677_samboundhard/scene.py", "SAMBoundHard"),
    Video(1678, "ProdigyBoundHard", "project/math/670_linear_132/1678_prodigyboundhard/scene.py", "ProdigyBoundHard"),
    Video(1679, "MuonWSoftClip", "project/math/670_linear_132/1679_muonwsoftclip/scene.py", "MuonWSoftClip"),
    Video(1680, "内心フォイエル接点比", "project/math/671_geometry_132/1680_in_feuerbach_touch/scene.py", "InFeuerbachTouch"),
    Video(1681, "傍心フォイエル接点比", "project/math/671_geometry_132/1681_ex_feuerbach_touch/scene.py", "ExFeuerbachTouch"),
    Video(1682, "外心フォイエル接点比", "project/math/671_geometry_132/1682_o_feuerbach_touch/scene.py", "OFeuerbachTouch"),
    Video(1683, "半径敏感度", "project/math/672_probability_130/1683_radius_sensitivity/scene.py", "RadiusSensitivity"),
    Video(1684, "標本依存複雑度", "project/math/672_probability_130/1684_sample_complexity/scene.py", "SampleComplexity"),
    Video(1685, "順序木細分", "project/math/673_combinatorics_129/1685_ordered_tree_refine/scene.py", "OrderedTreeRefine"),
)

VIDEOS_1686_1697: tuple[Video, ...] = (
    Video(1686, "相対ログ簡約対", "project/math/674_analysis_133/1686_rel_log_slc/scene.py", "RelLogSlc"),
    Video(1687, "ログ平坦対", "project/math/674_analysis_133/1687_log_flat_pair/scene.py", "LogFlatPair"),
    Video(1688, "相対ログ平坦対", "project/math/674_analysis_133/1688_rel_log_flat/scene.py", "RelLogFlat"),
    Video(1689, "LAMBBoundSoft", "project/math/675_linear_133/1689_lambboundsoft/scene.py", "LAMBBoundSoft"),
    Video(1690, "ApolloBound", "project/math/675_linear_133/1690_apollobound/scene.py", "ApolloBound"),
    Video(1691, "ApolloSoftHard", "project/math/675_linear_133/1691_apollosofthard/scene.py", "ApolloSoftHard"),
    Video(1692, "垂心フォイエル接点比", "project/math/676_geometry_133/1692_h_feuerbach_touch/scene.py", "HFeuerbachTouch"),
    Video(1693, "重心フォイエル接点比", "project/math/676_geometry_133/1693_g_feuerbach_touch/scene.py", "GFeuerbachTouch"),
    Video(1694, "九点フォイエル接点比", "project/math/676_geometry_133/1694_n_feuerbach_touch/scene.py", "NFeuerbachTouch"),
    Video(1695, "経験スケール敏感度", "project/math/677_probability_131/1695_emp_scale_sens/scene.py", "EmpScaleSens"),
    Video(1696, "局所スケールエントロピー", "project/math/677_probability_131/1696_local_scale_entropy/scene.py", "LocalScaleEntropy"),
    Video(1697, "シュレーダー路細分", "project/math/678_combinatorics_130/1697_schroeder_path_refine/scene.py", "SchroederPathRefine"),
)

VIDEOS_1698_1709: tuple[Video, ...] = (
    Video(1698, "ログ正規対", "project/math/679_analysis_134/1698_log_normal_pair/scene.py", "LogNormalPair"),
    Video(1699, "相対ログ正規対", "project/math/679_analysis_134/1699_rel_log_normal/scene.py", "RelLogNormal"),
    Video(1700, "ログクッション対", "project/math/679_analysis_134/1700_log_cushion_pair/scene.py", "LogCushionPair"),
    Video(1701, "LionWHardClip", "project/math/680_linear_134/1701_lionwhardclip/scene.py", "LionWHardClip"),
    Video(1702, "SophiaWHardClip", "project/math/680_linear_134/1702_sophiawhardclip/scene.py", "SophiaWHardClip"),
    Video(1703, "AdaFactorBoundSoft", "project/math/680_linear_134/1703_adafactorboundsoft/scene.py", "AdaFactorBoundSoft"),
    Video(1704, "内心類似フォイエル比", "project/math/681_geometry_134/1704_in_sym_feuerbach/scene.py", "InSymFeuerbach"),
    Video(1705, "傍心類似フォイエル比", "project/math/681_geometry_134/1705_ex_sym_feuerbach/scene.py", "ExSymFeuerbach"),
    Video(1706, "外心類似フォイエル比", "project/math/681_geometry_134/1706_o_sym_feuerbach/scene.py", "OSymFeuerbach"),
    Video(1707, "一様半径敏感度", "project/math/682_probability_132/1707_uniform_radius_sens/scene.py", "UniformRadiusSens"),
    Video(1708, "データ依存チャイニング", "project/math/682_probability_132/1708_data_chaining/scene.py", "DataChaining"),
    Video(1709, "モツキン三角形細分", "project/math/683_combinatorics_131/1709_motzkin_tri_refine/scene.py", "MotzkinTriRefine"),
)

VIDEOS_1710_1721: tuple[Video, ...] = (
    Video(1710, "相対ログクッション対", "project/math/684_analysis_135/1710_rel_log_cushion/scene.py", "RelLogCushion"),
    Video(1711, "ログ平滑対", "project/math/684_analysis_135/1711_log_smooth_pair/scene.py", "LogSmoothPair"),
    Video(1712, "相対ログ平滑対", "project/math/684_analysis_135/1712_rel_log_smooth/scene.py", "RelLogSmooth"),
    Video(1713, "NAdamHardBound", "project/math/685_linear_135/1713_nadamhardbound/scene.py", "NAdamHardBound"),
    Video(1714, "RMSSoftBound", "project/math/685_linear_135/1714_rmssoftbound/scene.py", "RMSSoftBound"),
    Video(1715, "LAMBSoftHard", "project/math/685_linear_135/1715_lambsofthard/scene.py", "LAMBSoftHard"),
    Video(1716, "垂心類似フォイエル比", "project/math/686_geometry_135/1716_h_sym_feuerbach/scene.py", "HSymFeuerbach"),
    Video(1717, "重心類似フォイエル比", "project/math/686_geometry_135/1717_g_sym_feuerbach/scene.py", "GSymFeuerbach"),
    Video(1718, "九点類似フォイエル比", "project/math/686_geometry_135/1718_n_sym_feuerbach/scene.py", "NSymFeuerbach"),
    Video(1719, "標本被覆数", "project/math/687_probability_133/1719_sample_covering/scene.py", "SampleCovering"),
    Video(1720, "標本パッキング数", "project/math/687_probability_133/1720_sample_packing/scene.py", "SamplePacking"),
    Video(1721, "大きなナラヤナ細分", "project/math/688_combinatorics_132/1721_large_narayana_refine/scene.py", "LargeNarayanaRefine"),
)

VIDEOS_1722_1733: tuple[Video, ...] = (
    Video(1722, "ログ単純対", "project/math/689_analysis_136/1722_log_simple_pair/scene.py", "LogSimplePair"),
    Video(1723, "相対ログ単純対", "project/math/689_analysis_136/1723_rel_log_simple/scene.py", "RelLogSimple"),
    Video(1724, "ログ純交対", "project/math/689_analysis_136/1724_log_snc_pair/scene.py", "LogSncPair"),
    Video(1725, "ApolloHardClip", "project/math/690_linear_136/1725_apollohardclip/scene.py", "ApolloHardClip"),
    Video(1726, "ApolloBoundSoft", "project/math/690_linear_136/1726_apolloboundsoft/scene.py", "ApolloBoundSoft"),
    Video(1727, "LARSSoftHard", "project/math/690_linear_136/1727_larssofthard/scene.py", "LARSSoftHard"),
    Video(1728, "内心類似フォイエル接点比", "project/math/691_geometry_136/1728_in_sym_feuer_touch/scene.py", "InSymFeuerTouch"),
    Video(1729, "傍心類似フォイエル接点比", "project/math/691_geometry_136/1729_ex_sym_feuer_touch/scene.py", "ExSymFeuerTouch"),
    Video(1730, "外心類似フォイエル接点比", "project/math/691_geometry_136/1730_o_sym_feuer_touch/scene.py", "OSymFeuerTouch"),
    Video(1731, "経験半径敏感度", "project/math/692_probability_134/1731_emp_radius_sens/scene.py", "EmpRadiusSens"),
    Video(1732, "局所標本複雑度", "project/math/692_probability_134/1732_local_sample_comp/scene.py", "LocalSampleComp"),
    Video(1733, "平面二分木細分", "project/math/693_combinatorics_133/1733_plane_bintree_refine/scene.py", "PlaneBinTreeRefine"),
)

VIDEOS_1734_1745: tuple[Video, ...] = (
    Video(1734, "相対ログ純交対", "project/math/694_analysis_137/1734_rel_log_snc/scene.py", "RelLogSnc"),
    Video(1735, "ログ余次元対", "project/math/694_analysis_137/1735_log_codim_pair/scene.py", "LogCodimPair"),
    Video(1736, "相対ログ余次元対", "project/math/694_analysis_137/1736_rel_log_codim/scene.py", "RelLogCodim"),
    Video(1737, "LAMBBoundHard", "project/math/695_linear_137/1737_lambboundhard/scene.py", "LAMBBoundHard"),
    Video(1738, "MuonWHardClip", "project/math/695_linear_137/1738_muonwhardclip/scene.py", "MuonWHardClip"),
    Video(1739, "SamSoftBound", "project/math/695_linear_137/1739_samsoftbound/scene.py", "SamSoftBound"),
    Video(1740, "垂心類似フォイエル接点比", "project/math/696_geometry_137/1740_h_sym_feuer_touch/scene.py", "HSymFeuerTouch"),
    Video(1741, "重心類似フォイエル接点比", "project/math/696_geometry_137/1741_g_sym_feuer_touch/scene.py", "GSymFeuerTouch"),
    Video(1742, "九点類似フォイエル接点比", "project/math/696_geometry_137/1742_n_sym_feuer_touch/scene.py", "NSymFeuerTouch"),
    Video(1743, "一様標本複雑度", "project/math/697_probability_135/1743_uniform_sample_comp/scene.py", "UniformSampleComp"),
    Video(1744, "データ依存被覆", "project/math/697_probability_135/1744_data_covering/scene.py", "DataCovering"),
    Video(1745, "増加木細分", "project/math/698_combinatorics_134/1745_increasing_tree_refine/scene.py", "IncreasingTreeRefine"),
)

VIDEOS_1746_1757: tuple[Video, ...] = (
    Video(1746, "ログ境界対", "project/math/699_analysis_138/1746_log_boundary_pair/scene.py", "LogBoundaryPair"),
    Video(1747, "相対ログ境界対", "project/math/699_analysis_138/1747_rel_log_boundary/scene.py", "RelLogBoundary"),
    Video(1748, "ログ純度対", "project/math/699_analysis_138/1748_log_purity_pair/scene.py", "LogPurityPair"),
    Video(1749, "AdamWBoundHard", "project/math/700_linear_138/1749_adamwboundhard/scene.py", "AdamWBoundHard"),
    Video(1750, "LionWBoundSoft", "project/math/700_linear_138/1750_lionwboundsoft/scene.py", "LionWBoundSoft"),
    Video(1751, "SophiaWBoundSoft", "project/math/700_linear_138/1751_sophiawboundsoft/scene.py", "SophiaWBoundSoft"),
    Video(1752, "内心フォイエル弦比", "project/math/701_geometry_138/1752_in_feuer_chord/scene.py", "InFeuerChord"),
    Video(1753, "傍心フォイエル弦比", "project/math/701_geometry_138/1753_ex_feuer_chord/scene.py", "ExFeuerChord"),
    Video(1754, "外心フォイエル弦比", "project/math/701_geometry_138/1754_o_feuer_chord/scene.py", "OFeuerChord"),
    Video(1755, "データ依存パッキング", "project/math/702_probability_136/1755_data_packing/scene.py", "DataPacking"),
    Video(1756, "経験一様エントロピー", "project/math/702_probability_136/1756_emp_uniform_entropy/scene.py", "EmpUniformEntropy"),
    Video(1757, "ヒープ細分", "project/math/703_combinatorics_135/1757_heap_refine/scene.py", "HeapRefine"),
)

VIDEOS_1758_1769: tuple[Video, ...] = (
    Video(1758, "相対ログ純度対", "project/math/704_analysis_139/1758_rel_log_purity/scene.py", "RelLogPurity"),
    Video(1759, "ログクエンチ対", "project/math/704_analysis_139/1759_log_quench_pair/scene.py", "LogQuenchPair"),
    Video(1760, "相対ログクエンチ対", "project/math/704_analysis_139/1760_rel_log_quench/scene.py", "RelLogQuench"),
    Video(1761, "LookaheadBoundSoft", "project/math/705_linear_139/1761_lookaheadboundsoft/scene.py", "LookaheadBoundSoft"),
    Video(1762, "ProdigySoftBound", "project/math/705_linear_139/1762_prodigysoftbound/scene.py", "ProdigySoftBound"),
    Video(1763, "ScheduleFreeBoundSoft", "project/math/705_linear_139/1763_schedulefreeboundsoft/scene.py", "ScheduleFreeBoundSoft"),
    Video(1764, "垂心フォイエル弦比", "project/math/706_geometry_139/1764_h_feuer_chord/scene.py", "HFeuerChord"),
    Video(1765, "重心フォイエル弦比", "project/math/706_geometry_139/1765_g_feuer_chord/scene.py", "GFeuerChord"),
    Video(1766, "九点フォイエル弦比", "project/math/706_geometry_139/1766_n_feuer_chord/scene.py", "NFeuerChord"),
    Video(1767, "局所一様エントロピー", "project/math/707_probability_137/1767_local_uniform_entropy/scene.py", "LocalUniformEntropy"),
    Video(1768, "経験局所被覆", "project/math/707_probability_137/1768_emp_local_covering/scene.py", "EmpLocalCovering"),
    Video(1769, "根つき森細分", "project/math/708_combinatorics_136/1769_rooted_forest_refine/scene.py", "RootedForestRefine"),
)

VIDEOS_1770_1781: tuple[Video, ...] = (
    Video(1770, "ログ支持対", "project/math/709_analysis_140/1770_log_support_pair/scene.py", "LogSupportPair"),
    Video(1771, "相対ログ支持対", "project/math/709_analysis_140/1771_rel_log_support/scene.py", "RelLogSupport"),
    Video(1772, "ログ係数対", "project/math/709_analysis_140/1772_log_coeff_pair/scene.py", "LogCoeffPair"),
    Video(1773, "AdamWSoftBound", "project/math/710_linear_140/1773_adamwsoftbound/scene.py", "AdamWSoftBound"),
    Video(1774, "LionHardBound", "project/math/710_linear_140/1774_lionhardbound/scene.py", "LionHardBound"),
    Video(1775, "SophiaHardBound", "project/math/710_linear_140/1775_sophiahardbound/scene.py", "SophiaHardBound"),
    Video(1776, "内心類似フォイエル弦比", "project/math/711_geometry_140/1776_in_sym_feuer_chord/scene.py", "InSymFeuerChord"),
    Video(1777, "傍心類似フォイエル弦比", "project/math/711_geometry_140/1777_ex_sym_feuer_chord/scene.py", "ExSymFeuerChord"),
    Video(1778, "外心類似フォイエル弦比", "project/math/711_geometry_140/1778_o_sym_feuer_chord/scene.py", "OSymFeuerChord"),
    Video(1779, "経験局所パッキング", "project/math/712_probability_138/1779_emp_local_packing/scene.py", "EmpLocalPacking"),
    Video(1780, "スケール標本複雑度", "project/math/712_probability_138/1780_scale_sample_comp/scene.py", "ScaleSampleComp"),
    Video(1781, "ラベル木細分", "project/math/713_combinatorics_137/1781_labeled_tree_refine/scene.py", "LabeledTreeRefine"),
)

VIDEOS_1782_1793: tuple[Video, ...] = (
    Video(1782, "相対ログ係数対", "project/math/714_analysis_141/1782_rel_log_coeff/scene.py", "RelLogCoeff"),
    Video(1783, "ログ重み対", "project/math/714_analysis_141/1783_log_weight_pair/scene.py", "LogWeightPair"),
    Video(1784, "相対ログ重み対", "project/math/714_analysis_141/1784_rel_log_weight/scene.py", "RelLogWeight"),
    Video(1785, "NAdamSoftHardBound", "project/math/715_linear_141/1785_nadamsofthardbound/scene.py", "NAdamSoftHardBound"),
    Video(1786, "RMSHardBound", "project/math/715_linear_141/1786_rmshardbound/scene.py", "RMSHardBound"),
    Video(1787, "LARSBoundSoft", "project/math/715_linear_141/1787_larsboundsoft/scene.py", "LARSBoundSoft"),
    Video(1788, "垂心類似フォイエル弦比", "project/math/716_geometry_141/1788_h_sym_feuer_chord/scene.py", "HSymFeuerChord"),
    Video(1789, "重心類似フォイエル弦比", "project/math/716_geometry_141/1789_g_sym_feuer_chord/scene.py", "GSymFeuerChord"),
    Video(1790, "九点類似フォイエル弦比", "project/math/716_geometry_141/1790_n_sym_feuer_chord/scene.py", "NSymFeuerChord"),
    Video(1791, "半径被覆数", "project/math/717_probability_139/1791_radius_covering/scene.py", "RadiusCovering"),
    Video(1792, "半径パッキング数", "project/math/717_probability_139/1792_radius_packing/scene.py", "RadiusPacking"),
    Video(1793, "ケイリー細分", "project/math/718_combinatorics_138/1793_cayley_refine/scene.py", "CayleyRefine"),
)

VIDEOS_1794_1805: tuple[Video, ...] = (
    Video(1794, "ログ多重度対", "project/math/719_analysis_142/1794_log_mult_pair/scene.py", "LogMultPair"),
    Video(1795, "相対ログ多重度対", "project/math/719_analysis_142/1795_rel_log_mult/scene.py", "RelLogMult"),
    Video(1796, "ログ交点数対", "project/math/719_analysis_142/1796_log_intersect_pair/scene.py", "LogIntersectPair"),
    Video(1797, "ApolloBoundHard", "project/math/720_linear_142/1797_apolloboundhard/scene.py", "ApolloBoundHard"),
    Video(1798, "MuonSoftBoundClip", "project/math/720_linear_142/1798_muonsoftboundclip/scene.py", "MuonSoftBoundClip"),
    Video(1799, "SamHardBound", "project/math/720_linear_142/1799_samhardbound/scene.py", "SamHardBound"),
    Video(1800, "内心フォイエル弧比", "project/math/721_geometry_142/1800_in_feuer_arc/scene.py", "InFeuerArc"),
    Video(1801, "傍心フォイエル弧比", "project/math/721_geometry_142/1801_ex_feuer_arc/scene.py", "ExFeuerArc"),
    Video(1802, "外心フォイエル弧比", "project/math/721_geometry_142/1802_o_feuer_arc/scene.py", "OFeuerArc"),
    Video(1803, "局所半径被覆", "project/math/722_probability_140/1803_local_radius_covering/scene.py", "LocalRadiusCovering"),
    Video(1804, "局所半径パッキング", "project/math/722_probability_140/1804_local_radius_packing/scene.py", "LocalRadiusPacking"),
    Video(1805, "増加森細分", "project/math/723_combinatorics_139/1805_inc_forest_refine/scene.py", "IncForestRefine"),
)

VIDEOS_1806_1817: tuple[Video, ...] = (
    Video(1806, "相対ログ交点数対", "project/math/724_analysis_143/1806_rel_log_intersect/scene.py", "RelLogIntersect"),
    Video(1807, "ログ次数対", "project/math/724_analysis_143/1807_log_degree_pair/scene.py", "LogDegreePair"),
    Video(1808, "相対ログ次数対", "project/math/724_analysis_143/1808_rel_log_degree/scene.py", "RelLogDegree"),
    Video(1809, "AdaFactorSoftBound", "project/math/725_linear_143/1809_adafactorsoftbound/scene.py", "AdaFactorSoftBound"),
    Video(1810, "NAdamHardSoft", "project/math/725_linear_143/1810_nadamhardsoft/scene.py", "NAdamHardSoft"),
    Video(1811, "LAMBHardBound", "project/math/725_linear_143/1811_lambhardbound/scene.py", "LAMBHardBound"),
    Video(1812, "垂心フォイエル弧比", "project/math/726_geometry_143/1812_h_feuer_arc/scene.py", "HFeuerArc"),
    Video(1813, "重心フォイエル弧比", "project/math/726_geometry_143/1813_g_feuer_arc/scene.py", "GFeuerArc"),
    Video(1814, "九点フォイエル弧比", "project/math/726_geometry_143/1814_n_feuer_arc/scene.py", "NFeuerArc"),
    Video(1815, "経験半径被覆", "project/math/727_probability_141/1815_emp_radius_covering/scene.py", "EmpRadiusCovering"),
    Video(1816, "経験半径パッキング", "project/math/727_probability_141/1816_emp_radius_packing/scene.py", "EmpRadiusPacking"),
    Video(1817, "減少木細分", "project/math/728_combinatorics_140/1817_dec_tree_refine/scene.py", "DecTreeRefine"),
)

VIDEOS_1818_1829: tuple[Video, ...] = (
    Video(1818, "ログ体積多項式対", "project/math/729_analysis_144/1818_log_vol_poly_pair/scene.py", "LogVolPolyPair"),
    Video(1819, "相対ログ体積多項式対", "project/math/729_analysis_144/1819_rel_log_vol_poly/scene.py", "RelLogVolPoly"),
    Video(1820, "ログ自己交対", "project/math/729_analysis_144/1820_log_self_intersect/scene.py", "LogSelfIntersect"),
    Video(1821, "LookaheadHardBound", "project/math/730_linear_144/1821_lookaheadhardbound/scene.py", "LookaheadHardBound"),
    Video(1822, "ProdigyHardBound", "project/math/730_linear_144/1822_prodigyhardbound/scene.py", "ProdigyHardBound"),
    Video(1823, "ScheduleFreeHardBound", "project/math/730_linear_144/1823_schedulefreehardbound/scene.py", "ScheduleFreeHardBound"),
    Video(1824, "内心類似フォイエル弧比", "project/math/731_geometry_144/1824_in_sym_feuer_arc/scene.py", "InSymFeuerArc"),
    Video(1825, "傍心類似フォイエル弧比", "project/math/731_geometry_144/1825_ex_sym_feuer_arc/scene.py", "ExSymFeuerArc"),
    Video(1826, "外心類似フォイエル弧比", "project/math/731_geometry_144/1826_o_sym_feuer_arc/scene.py", "OSymFeuerArc"),
    Video(1827, "一様半径被覆", "project/math/732_probability_142/1827_uniform_radius_covering/scene.py", "UniformRadiusCovering"),
    Video(1828, "一様半径パッキング", "project/math/732_probability_142/1828_uniform_radius_packing/scene.py", "UniformRadiusPacking"),
    Video(1829, "二分ヒープ細分", "project/math/733_combinatorics_141/1829_binheap_refine/scene.py", "BinHeapRefine"),
)

VIDEOS_1830_1841: tuple[Video, ...] = (
    Video(1830, "相対ログ自己交対", "project/math/734_analysis_145/1830_rel_log_self_int/scene.py", "RelLogSelfInt"),
    Video(1831, "ログ交多項式対", "project/math/734_analysis_145/1831_log_int_poly_pair/scene.py", "LogIntPolyPair"),
    Video(1832, "相対ログ交多項式対", "project/math/734_analysis_145/1832_rel_log_int_poly/scene.py", "RelLogIntPoly"),
    Video(1833, "AdamWHardBound", "project/math/735_linear_145/1833_adamwhardbound/scene.py", "AdamWHardBound"),
    Video(1834, "LionSoftBoundClip", "project/math/735_linear_145/1834_lionsoftboundclip/scene.py", "LionSoftBoundClip"),
    Video(1835, "SophiaSoftBoundClip", "project/math/735_linear_145/1835_sophiasoftboundclip/scene.py", "SophiaSoftBoundClip"),
    Video(1836, "垂心類似フォイエル弧比", "project/math/736_geometry_145/1836_h_sym_feuer_arc/scene.py", "HSymFeuerArc"),
    Video(1837, "重心類似フォイエル弧比", "project/math/736_geometry_145/1837_g_sym_feuer_arc/scene.py", "GSymFeuerArc"),
    Video(1838, "九点類似フォイエル弧比", "project/math/736_geometry_145/1838_n_sym_feuer_arc/scene.py", "NSymFeuerArc"),
    Video(1839, "局所一様被覆", "project/math/737_probability_143/1839_local_uniform_covering/scene.py", "LocalUniformCovering"),
    Video(1840, "局所一様パッキング", "project/math/737_probability_143/1840_local_uniform_packing/scene.py", "LocalUniformPacking"),
    Video(1841, "三分木細分", "project/math/738_combinatorics_142/1841_ternary_tree_refine/scene.py", "TernaryTreeRefine"),
)

VIDEOS_1842_1853: tuple[Video, ...] = (
    Video(1842, "ログ数値類対", "project/math/739_analysis_146/1842_log_num_class_pair/scene.py", "LogNumClassPair"),
    Video(1843, "相対ログ数値類対", "project/math/739_analysis_146/1843_rel_log_num_class/scene.py", "RelLogNumClass"),
    Video(1844, "ログピカール対", "project/math/739_analysis_146/1844_log_picard_pair/scene.py", "LogPicardPair"),
    Video(1845, "ApolloSoftBound", "project/math/740_linear_146/1845_apollosoftbound/scene.py", "ApolloSoftBound"),
    Video(1846, "MuonHardBound", "project/math/740_linear_146/1846_muonhardbound/scene.py", "MuonHardBound"),
    Video(1847, "SamSoftHardBound", "project/math/740_linear_146/1847_samsofthardbound/scene.py", "SamSoftHardBound"),
    Video(1848, "内心フォイエル中心比", "project/math/741_geometry_146/1848_in_feuer_center/scene.py", "InFeuerCenter"),
    Video(1849, "傍心フォイエル中心比", "project/math/741_geometry_146/1849_ex_feuer_center/scene.py", "ExFeuerCenter"),
    Video(1850, "外心フォイエル中心比", "project/math/741_geometry_146/1850_o_feuer_center/scene.py", "OFeuerCenter"),
    Video(1851, "経験一様被覆", "project/math/742_probability_144/1851_emp_uniform_covering/scene.py", "EmpUniformCovering"),
    Video(1852, "経験一様パッキング", "project/math/742_probability_144/1852_emp_uniform_packing/scene.py", "EmpUniformPacking"),
    Video(1853, "平面増加木細分", "project/math/743_combinatorics_143/1853_plane_inc_tree_refine/scene.py", "PlaneIncTreeRefine"),
)

VIDEOS_1854_1865: tuple[Video, ...] = (
    Video(1854, "相対ログピカール対", "project/math/744_analysis_147/1854_rel_log_picard/scene.py", "RelLogPicard"),
    Video(1855, "ログネロンセベリ対", "project/math/744_analysis_147/1855_log_ns_pair/scene.py", "LogNsPair"),
    Video(1856, "相対ログネロンセベリ対", "project/math/744_analysis_147/1856_rel_log_ns/scene.py", "RelLogNs"),
    Video(1857, "LARSHardBound", "project/math/745_linear_147/1857_larshardbound/scene.py", "LARSHardBound"),
    Video(1858, "AdaFactorHardBound", "project/math/745_linear_147/1858_adafactorhardbound/scene.py", "AdaFactorHardBound"),
    Video(1859, "NAdamBoundSoftClip", "project/math/745_linear_147/1859_nadamboundsoftclip/scene.py", "NAdamBoundSoftClip"),
    Video(1860, "垂心フォイエル中心比", "project/math/746_geometry_147/1860_h_feuer_center/scene.py", "HFeuerCenter"),
    Video(1861, "重心フォイエル中心比", "project/math/746_geometry_147/1861_g_feuer_center/scene.py", "GFeuerCenter"),
    Video(1862, "九点フォイエル中心比", "project/math/746_geometry_147/1862_n_feuer_center/scene.py", "NFeuerCenter"),
    Video(1863, "スケール一様エントロピー", "project/math/747_probability_145/1863_scale_uniform_entropy/scene.py", "ScaleUniformEntropy"),
    Video(1864, "半径一様複雑度", "project/math/747_probability_145/1864_radius_uniform_comp/scene.py", "RadiusUniformComp"),
    Video(1865, "順序森細分", "project/math/748_combinatorics_144/1865_ordered_forest_refine/scene.py", "OrderedForestRefine"),
)

VIDEOS_1866_1877: tuple[Video, ...] = (
    Video(1866, "ログ有理対", "project/math/749_analysis_148/1866_log_rational_pair/scene.py", "LogRationalPair"),
    Video(1867, "相対ログ有理対", "project/math/749_analysis_148/1867_rel_log_rational/scene.py", "RelLogRational"),
    Video(1868, "ログ双有理対", "project/math/749_analysis_148/1868_log_birational_pair/scene.py", "LogBirationalPair"),
    Video(1869, "RMSBoundClip", "project/math/750_linear_148/1869_rmsboundclip/scene.py", "RMSBoundClip"),
    Video(1870, "LAMBSoftBound", "project/math/750_linear_148/1870_lambsoftbound/scene.py", "LAMBSoftBound"),
    Video(1871, "LookaheadSoftBound", "project/math/750_linear_148/1871_lookaheadsoftbound/scene.py", "LookaheadSoftBound"),
    Video(1872, "内心類似フォイエル中心比", "project/math/751_geometry_148/1872_in_sym_feuer_center/scene.py", "InSymFeuerCenter"),
    Video(1873, "傍心類似フォイエル中心比", "project/math/751_geometry_148/1873_ex_sym_feuer_center/scene.py", "ExSymFeuerCenter"),
    Video(1874, "外心類似フォイエル中心比", "project/math/751_geometry_148/1874_o_sym_feuer_center/scene.py", "OSymFeuerCenter"),
    Video(1875, "局所スケール被覆", "project/math/752_probability_146/1875_local_scale_covering/scene.py", "LocalScaleCovering"),
    Video(1876, "局所スケールパッキング", "project/math/752_probability_146/1876_local_scale_packing/scene.py", "LocalScalePacking"),
    Video(1877, "根つき増加木細分", "project/math/753_combinatorics_145/1877_rooted_inc_tree_refine/scene.py", "RootedIncTreeRefine"),
)

VIDEOS_1878_1889: tuple[Video, ...] = (
    Video(1878, "相対ログ双有理対", "project/math/754_analysis_149/1878_rel_log_birational/scene.py", "RelLogBirational"),
    Video(1879, "ログ射影対", "project/math/754_analysis_149/1879_log_proj_pair/scene.py", "LogProjPair"),
    Video(1880, "相対ログ射影対", "project/math/754_analysis_149/1880_rel_log_proj/scene.py", "RelLogProj"),
    Video(1881, "ProdigyBoundClip", "project/math/755_linear_149/1881_prodigyboundclip/scene.py", "ProdigyBoundClip"),
    Video(1882, "ScheduleFreeBoundHard", "project/math/755_linear_149/1882_schedulefreeboundhard/scene.py", "ScheduleFreeBoundHard"),
    Video(1883, "AdamWBoundClip", "project/math/755_linear_149/1883_adamwboundclip/scene.py", "AdamWBoundClip"),
    Video(1884, "垂心類似フォイエル中心比", "project/math/756_geometry_149/1884_h_sym_feuer_center/scene.py", "HSymFeuerCenter"),
    Video(1885, "重心類似フォイエル中心比", "project/math/756_geometry_149/1885_g_sym_feuer_center/scene.py", "GSymFeuerCenter"),
    Video(1886, "九点類似フォイエル中心比", "project/math/756_geometry_149/1886_n_sym_feuer_center/scene.py", "NSymFeuerCenter"),
    Video(1887, "経験スケール被覆", "project/math/757_probability_147/1887_emp_scale_covering/scene.py", "EmpScaleCovering"),
    Video(1888, "経験スケールパッキング", "project/math/757_probability_147/1888_emp_scale_packing/scene.py", "EmpScalePacking"),
    Video(1889, "ラベル森細分", "project/math/758_combinatorics_146/1889_labeled_forest_refine/scene.py", "LabeledForestRefine"),
)

VIDEOS_1890_1901: tuple[Video, ...] = (
    Video(1890, "ログファノ対", "project/math/759_analysis_150/1890_log_fano_pair/scene.py", "LogFanoPair"),
    Video(1891, "相対ログファノ対", "project/math/759_analysis_150/1891_rel_log_fano/scene.py", "RelLogFano"),
    Video(1892, "ログアルバネーゼ対", "project/math/759_analysis_150/1892_log_albanese_pair/scene.py", "LogAlbanesePair"),
    Video(1893, "LionWSoftBound", "project/math/760_linear_150/1893_lionwsoftbound/scene.py", "LionWSoftBound"),
    Video(1894, "SophiaWSoftBound", "project/math/760_linear_150/1894_sophiawsoftbound/scene.py", "SophiaWSoftBound"),
    Video(1895, "ApolloBoundClip", "project/math/760_linear_150/1895_apolloboundclip/scene.py", "ApolloBoundClip"),
    Video(1896, "内心フォイエル半径比", "project/math/761_geometry_150/1896_in_feuer_radius/scene.py", "InFeuerRadius"),
    Video(1897, "傍心フォイエル半径比", "project/math/761_geometry_150/1897_ex_feuer_radius/scene.py", "ExFeuerRadius"),
    Video(1898, "外心フォイエル半径比", "project/math/761_geometry_150/1898_o_feuer_radius/scene.py", "OFeuerRadius"),
    Video(1899, "一様スケール被覆", "project/math/762_probability_148/1899_uniform_scale_covering/scene.py", "UniformScaleCovering"),
    Video(1900, "一様スケールパッキング", "project/math/762_probability_148/1900_uniform_scale_packing/scene.py", "UniformScalePacking"),
    Video(1901, "ケイリー森細分", "project/math/763_combinatorics_147/1901_cayley_forest_refine/scene.py", "CayleyForestRefine"),
)

VIDEOS_1902_1913: tuple[Video, ...] = (
    Video(1902, "相対ログアルバネーゼ対", "project/math/764_analysis_151/1902_rel_log_albanese/scene.py", "RelLogAlbanese"),
    Video(1903, "ログクレモナ対", "project/math/764_analysis_151/1903_log_cremona_pair/scene.py", "LogCremonaPair"),
    Video(1904, "相対ログクレモナ対", "project/math/764_analysis_151/1904_rel_log_cremona/scene.py", "RelLogCremona"),
    Video(1905, "MuonBoundSoftClip", "project/math/765_linear_151/1905_muonboundsoftclip/scene.py", "MuonBoundSoftClip"),
    Video(1906, "SamBoundClip", "project/math/765_linear_151/1906_samboundclip/scene.py", "SamBoundClip"),
    Video(1907, "AdaFactorBoundClip", "project/math/765_linear_151/1907_adafactorboundclip/scene.py", "AdaFactorBoundClip"),
    Video(1908, "垂心フォイエル半径比", "project/math/766_geometry_151/1908_h_feuer_radius/scene.py", "HFeuerRadius"),
    Video(1909, "重心フォイエル半径比", "project/math/766_geometry_151/1909_g_feuer_radius/scene.py", "GFeuerRadius"),
    Video(1910, "九点フォイエル半径比", "project/math/766_geometry_151/1910_n_feuer_radius/scene.py", "NFeuerRadius"),
    Video(1911, "経験スケールエントロピー", "project/math/767_probability_149/1911_emp_scale_entropy/scene.py", "EmpScaleEntropy"),
    Video(1912, "半径スケール複雑度", "project/math/767_probability_149/1912_radius_scale_comp/scene.py", "RadiusScaleComp"),
    Video(1913, "三分ヒープ細分", "project/math/768_combinatorics_148/1913_ternary_heap_refine/scene.py", "TernaryHeapRefine"),
)

VIDEOS_1914_1925: tuple[Video, ...] = (
    Video(1914, "ログカラビ対", "project/math/769_analysis_152/1914_log_calabi_pair/scene.py", "LogCalabiPair"),
    Video(1915, "相対ログカラビ対", "project/math/769_analysis_152/1915_rel_log_calabi/scene.py", "RelLogCalabi"),
    Video(1916, "ログカラビヤウ対", "project/math/769_analysis_152/1916_log_cy_pair/scene.py", "LogCyPair"),
    Video(1917, "NAdamBoundClip", "project/math/770_linear_152/1917_nadamboundclip/scene.py", "NAdamBoundClip"),
    Video(1918, "LARSBoundClip", "project/math/770_linear_152/1918_larsboundclip/scene.py", "LARSBoundClip"),
    Video(1919, "LionWBoundHard", "project/math/770_linear_152/1919_lionwboundhard/scene.py", "LionWBoundHard"),
    Video(1920, "内心類似フォイエル半径比", "project/math/771_geometry_152/1920_in_sym_feuer_radius/scene.py", "InSymFeuerRadius"),
    Video(1921, "傍心類似フォイエル半径比", "project/math/771_geometry_152/1921_ex_sym_feuer_radius/scene.py", "ExSymFeuerRadius"),
    Video(1922, "外心類似フォイエル半径比", "project/math/771_geometry_152/1922_o_sym_feuer_radius/scene.py", "OSymFeuerRadius"),
    Video(1923, "標本スケール被覆", "project/math/772_probability_150/1923_sample_scale_covering/scene.py", "SampleScaleCovering"),
    Video(1924, "標本スケールパッキング", "project/math/772_probability_150/1924_sample_scale_packing/scene.py", "SampleScalePacking"),
    Video(1925, "平面三分木細分", "project/math/773_combinatorics_149/1925_plane_ternary_refine/scene.py", "PlaneTernaryRefine"),
)

VIDEOS_1926_1937: tuple[Video, ...] = (
    Video(1926, "相対ログカラビヤウ対", "project/math/774_analysis_153/1926_rel_log_cy/scene.py", "RelLogCy"),
    Video(1927, "ログ一般型対", "project/math/774_analysis_153/1927_log_general_type/scene.py", "LogGeneralType"),
    Video(1928, "相対ログ一般型対", "project/math/774_analysis_153/1928_rel_log_general_type/scene.py", "RelLogGeneralType"),
    Video(1929, "SophiaWBoundHard", "project/math/775_linear_153/1929_sophiawboundhard/scene.py", "SophiaWBoundHard"),
    Video(1930, "LookaheadBoundClip", "project/math/775_linear_153/1930_lookaheadboundclip/scene.py", "LookaheadBoundClip"),
    Video(1931, "ProdigySoftBoundClip", "project/math/775_linear_153/1931_prodigysoftboundclip/scene.py", "ProdigySoftBoundClip"),
    Video(1932, "垂心類似フォイエル半径比", "project/math/776_geometry_153/1932_h_sym_feuer_radius/scene.py", "HSymFeuerRadius"),
    Video(1933, "重心類似フォイエル半径比", "project/math/776_geometry_153/1933_g_sym_feuer_radius/scene.py", "GSymFeuerRadius"),
    Video(1934, "九点類似フォイエル半径比", "project/math/776_geometry_153/1934_n_sym_feuer_radius/scene.py", "NSymFeuerRadius"),
    Video(1935, "局所スケールエントロピー再訪", "project/math/777_probability_151/1935_local_scale_entropy_rev/scene.py", "LocalScaleEntropyRev"),
    Video(1936, "一様スケールエントロピー再訪", "project/math/777_probability_151/1936_uniform_scale_entropy_rev/scene.py", "UniformScaleEntropyRev"),
    Video(1937, "増加ヒープ細分", "project/math/778_combinatorics_150/1937_inc_heap_refine/scene.py", "IncHeapRefine"),
)

VIDEOS_1938_1949: tuple[Video, ...] = (
    Video(1938, "ログ小平対", "project/math/779_analysis_154/1938_log_kodaira_pair/scene.py", "LogKodairaPair"),
    Video(1939, "相対ログ小平対", "project/math/779_analysis_154/1939_rel_log_kodaira/scene.py", "RelLogKodaira"),
    Video(1940, "ログ飯高ファイバー対", "project/math/779_analysis_154/1940_log_iitaka_fiber/scene.py", "LogIitakaFiber"),
    Video(1941, "RMSSoftBoundClip", "project/math/780_linear_154/1941_rmssoftboundclip/scene.py", "RMSSoftBoundClip"),
    Video(1942, "LAMBBoundClip", "project/math/780_linear_154/1942_lambboundclip/scene.py", "LAMBBoundClip"),
    Video(1943, "AdamWSoftBoundClip", "project/math/780_linear_154/1943_adamwsoftboundclip/scene.py", "AdamWSoftBoundClip"),
    Video(1944, "内心九点弦比", "project/math/781_geometry_154/1944_in_nine_chord/scene.py", "InNineChord"),
    Video(1945, "傍心九点弦比", "project/math/781_geometry_154/1945_ex_nine_chord/scene.py", "ExNineChord"),
    Video(1946, "外心九点弦比", "project/math/781_geometry_154/1946_o_nine_chord/scene.py", "ONineChord"),
    Video(1947, "データ半径エントロピー", "project/math/782_probability_152/1947_data_radius_entropy/scene.py", "DataRadiusEntropy"),
    Video(1948, "標本半径複雑度", "project/math/782_probability_152/1948_sample_radius_comp/scene.py", "SampleRadiusComp"),
    Video(1949, "減少森細分", "project/math/783_combinatorics_151/1949_dec_forest_refine/scene.py", "DecForestRefine"),
)

VIDEOS_1950_1961: tuple[Video, ...] = (
    Video(1950, "相対ログ飯高ファイバー対", "project/math/784_analysis_155/1950_rel_log_iitaka_fiber/scene.py", "RelLogIitakaFiber"),
    Video(1951, "ログ随伴対", "project/math/784_analysis_155/1951_log_adjoint_pair/scene.py", "LogAdjointPair"),
    Video(1952, "相対ログ随伴対", "project/math/784_analysis_155/1952_rel_log_adjoint/scene.py", "RelLogAdjoint"),
    Video(1953, "ScheduleFreeSoftBound", "project/math/785_linear_155/1953_schedulefreesoftbound/scene.py", "ScheduleFreeSoftBound"),
    Video(1954, "ApolloHardBound", "project/math/785_linear_155/1954_apollohardbound/scene.py", "ApolloHardBound"),
    Video(1955, "MuonSoftHardBound", "project/math/785_linear_155/1955_muonsofthardbound/scene.py", "MuonSoftHardBound"),
    Video(1956, "垂心九点弦比", "project/math/786_geometry_155/1956_h_nine_chord/scene.py", "HNineChord"),
    Video(1957, "重心九点弦比", "project/math/786_geometry_155/1957_g_nine_chord/scene.py", "GNineChord"),
    Video(1958, "九点弦長比", "project/math/786_geometry_155/1958_n_nine_chord/scene.py", "NNineChord"),
    Video(1959, "局所標本スケール被覆", "project/math/787_probability_153/1959_local_sample_scale_cov/scene.py", "LocalSampleScaleCov"),
    Video(1960, "局所標本スケールパッキング", "project/math/787_probability_153/1960_local_sample_scale_pack/scene.py", "LocalSampleScalePack"),
    Video(1961, "根つき三分木細分", "project/math/788_combinatorics_152/1961_rooted_ternary_refine/scene.py", "RootedTernaryRefine"),
)

VIDEOS_1962_1973: tuple[Video, ...] = (
    Video(1962, "ログ随伴豊富対", "project/math/789_analysis_156/1962_log_adj_ample/scene.py", "LogAdjAmple"),
    Video(1963, "相対ログ随伴豊富対", "project/math/789_analysis_156/1963_rel_log_adj_ample/scene.py", "RelLogAdjAmple"),
    Video(1964, "ログ随伴ネフ対", "project/math/789_analysis_156/1964_log_adj_nef/scene.py", "LogAdjNef"),
    Video(1965, "SamSoftBoundClip", "project/math/790_linear_156/1965_samsoftboundclip/scene.py", "SamSoftBoundClip"),
    Video(1966, "NAdamSoftBoundClip", "project/math/790_linear_156/1966_nadamsoftboundclip/scene.py", "NAdamSoftBoundClip"),
    Video(1967, "LARSSoftBound", "project/math/790_linear_156/1967_larssoftbound/scene.py", "LARSSoftBound"),
    Video(1968, "内心類似九点弦比", "project/math/791_geometry_156/1968_in_sym_nine_chord/scene.py", "InSymNineChord"),
    Video(1969, "傍心類似九点弦比", "project/math/791_geometry_156/1969_ex_sym_nine_chord/scene.py", "ExSymNineChord"),
    Video(1970, "外心類似九点弦比", "project/math/791_geometry_156/1970_o_sym_nine_chord/scene.py", "OSymNineChord"),
    Video(1971, "経験一様スケール被覆", "project/math/792_probability_154/1971_emp_unif_scale_cov/scene.py", "EmpUnifScaleCov"),
    Video(1972, "経験一様スケールパッキング", "project/math/792_probability_154/1972_emp_unif_scale_pack/scene.py", "EmpUnifScalePack"),
    Video(1973, "ラベル三分木細分", "project/math/793_combinatorics_153/1973_labeled_ternary_refine/scene.py", "LabeledTernaryRefine"),
)

VIDEOS_1974_1985: tuple[Video, ...] = (
    Video(1974, "相対ログ随伴ネフ対", "project/math/794_analysis_157/1974_rel_log_adj_nef/scene.py", "RelLogAdjNef"),
    Video(1975, "ログ随伴ビッグ対", "project/math/794_analysis_157/1975_log_adj_big/scene.py", "LogAdjBig"),
    Video(1976, "相対ログ随伴ビッグ対", "project/math/794_analysis_157/1976_rel_log_adj_big/scene.py", "RelLogAdjBig"),
    Video(1977, "LionWBoundClip", "project/math/795_linear_157/1977_lionwboundclip/scene.py", "LionWBoundClip"),
    Video(1978, "SophiaWBoundClip", "project/math/795_linear_157/1978_sophiawboundclip/scene.py", "SophiaWBoundClip"),
    Video(1979, "ApolloSoftBoundClip", "project/math/795_linear_157/1979_apollosoftboundclip/scene.py", "ApolloSoftBoundClip"),
    Video(1980, "垂心類似九点弦比", "project/math/796_geometry_157/1980_h_sym_nine_chord/scene.py", "HSymNineChord"),
    Video(1981, "重心類似九点弦比", "project/math/796_geometry_157/1981_g_sym_nine_chord/scene.py", "GSymNineChord"),
    Video(1982, "九点類似弦比", "project/math/796_geometry_157/1982_n_sym_nine_chord/scene.py", "NSymNineChord"),
    Video(1983, "局所一様スケール被覆", "project/math/797_probability_155/1983_local_unif_scale_cov/scene.py", "LocalUnifScaleCov"),
    Video(1984, "局所一様スケールパッキング", "project/math/797_probability_155/1984_local_unif_scale_pack/scene.py", "LocalUnifScalePack"),
    Video(1985, "順序三分木細分", "project/math/798_combinatorics_154/1985_ordered_ternary_refine/scene.py", "OrderedTernaryRefine"),
)

VIDEOS_1986_1997: tuple[Video, ...] = (
    Video(1986, "ログ随伴擬有効対", "project/math/799_analysis_158/1986_log_adj_psef/scene.py", "LogAdjPsef"),
    Video(1987, "相対ログ随伴擬有効対", "project/math/799_analysis_158/1987_rel_log_adj_psef/scene.py", "RelLogAdjPsef"),
    Video(1988, "ログ随伴移動対", "project/math/799_analysis_158/1988_log_adj_movable/scene.py", "LogAdjMovable"),
    Video(1989, "MuonHardBoundClip", "project/math/800_linear_158/1989_muonhardboundclip/scene.py", "MuonHardBoundClip"),
    Video(1990, "SamHardBoundClip", "project/math/800_linear_158/1990_samhardboundclip/scene.py", "SamHardBoundClip"),
    Video(1991, "AdaFactorSoftBoundClip", "project/math/800_linear_158/1991_adafactorsoftboundclip/scene.py", "AdaFactorSoftBoundClip"),
    Video(1992, "内心九点弧比", "project/math/801_geometry_158/1992_in_nine_arc/scene.py", "InNineArc"),
    Video(1993, "傍心九点弧比", "project/math/801_geometry_158/1993_ex_nine_arc/scene.py", "ExNineArc"),
    Video(1994, "外心九点弧比", "project/math/801_geometry_158/1994_o_nine_arc/scene.py", "ONineArc"),
    Video(1995, "一様標本スケール被覆", "project/math/802_probability_156/1995_unif_sample_scale_cov/scene.py", "UnifSampleScaleCov"),
    Video(1996, "一様標本スケールパッキング", "project/math/802_probability_156/1996_unif_sample_scale_pack/scene.py", "UnifSampleScalePack"),
    Video(1997, "平面増加森細分", "project/math/803_combinatorics_155/1997_plane_inc_forest_refine/scene.py", "PlaneIncForestRefine"),
)

VIDEOS_1998_2009: tuple[Video, ...] = (
    Video(1998, "相対ログ随伴移動対", "project/math/804_analysis_159/1998_rel_log_adj_mov/scene.py", "RelLogAdjMov"),
    Video(1999, "ログ随伴正値対", "project/math/804_analysis_159/1999_log_adj_pos/scene.py", "LogAdjPos"),
    Video(2000, "相対ログ随伴正値対", "project/math/804_analysis_159/2000_rel_log_adj_pos/scene.py", "RelLogAdjPos"),
    Video(2001, "NAdamHardBoundClip", "project/math/805_linear_159/2001_nadamhardboundclip/scene.py", "NAdamHardBoundClip"),
    Video(2002, "LARSHardBoundClip", "project/math/805_linear_159/2002_larshardboundclip/scene.py", "LARSHardBoundClip"),
    Video(2003, "LAMBSoftBoundClip", "project/math/805_linear_159/2003_lambsoftboundclip/scene.py", "LAMBSoftBoundClip"),
    Video(2004, "垂心九点弧比", "project/math/806_geometry_159/2004_h_nine_arc/scene.py", "HNineArc"),
    Video(2005, "重心九点弧比", "project/math/806_geometry_159/2005_g_nine_arc/scene.py", "GNineArc"),
    Video(2006, "九点円弧比", "project/math/806_geometry_159/2006_n_nine_arc/scene.py", "NNineArc"),
    Video(2007, "半径データ複雑度", "project/math/807_probability_157/2007_radius_data_comp/scene.py", "RadiusDataComp"),
    Video(2008, "スケール一様被覆再訪", "project/math/807_probability_157/2008_scale_unif_cov_rev/scene.py", "ScaleUnifCovRev"),
    Video(2009, "ケイリー三分木細分", "project/math/808_combinatorics_156/2009_cayley_ternary_refine/scene.py", "CayleyTernaryRefine"),
)

VIDEOS_2010_2021: tuple[Video, ...] = (
    Video(2010, "ログ随伴体積対", "project/math/809_analysis_160/2010_log_adj_vol/scene.py", "LogAdjVol"),
    Video(2011, "相対ログ随伴体積対", "project/math/809_analysis_160/2011_rel_log_adj_vol/scene.py", "RelLogAdjVol"),
    Video(2012, "ログ随伴数値次元対", "project/math/809_analysis_160/2012_log_adj_num_dim/scene.py", "LogAdjNumDim"),
    Video(2013, "RMSHardBoundClip", "project/math/810_linear_160/2013_rmshardboundclip/scene.py", "RMSHardBoundClip"),
    Video(2014, "LookaheadSoftBoundClip", "project/math/810_linear_160/2014_lookaheadsoftboundclip/scene.py", "LookaheadSoftBoundClip"),
    Video(2015, "ProdigyHardBoundClip", "project/math/810_linear_160/2015_prodigyhardboundclip/scene.py", "ProdigyHardBoundClip"),
    Video(2016, "内心類似九点弧比", "project/math/811_geometry_160/2016_in_sym_nine_arc/scene.py", "InSymNineArc"),
    Video(2017, "傍心類似九点弧比", "project/math/811_geometry_160/2017_ex_sym_nine_arc/scene.py", "ExSymNineArc"),
    Video(2018, "外心類似九点弧比", "project/math/811_geometry_160/2018_o_sym_nine_arc/scene.py", "OSymNineArc"),
    Video(2019, "局所データ半径被覆", "project/math/812_probability_158/2019_local_data_radius_cov/scene.py", "LocalDataRadiusCov"),
    Video(2020, "局所データ半径パッキング", "project/math/812_probability_158/2020_local_data_radius_pack/scene.py", "LocalDataRadiusPack"),
    Video(2021, "根つき増加森細分", "project/math/813_combinatorics_157/2021_rooted_inc_forest/scene.py", "RootedIncForest"),
)

VIDEOS_2022_2033: tuple[Video, ...] = (
    Video(2022, "相対ログ随伴数値次元対", "project/math/814_analysis_161/2022_rel_log_adj_num_dim/scene.py", "RelLogAdjNumDim"),
    Video(2023, "ログ随伴飯高対", "project/math/814_analysis_161/2023_log_adj_iitaka/scene.py", "LogAdjIitaka"),
    Video(2024, "相対ログ随伴飯高対", "project/math/814_analysis_161/2024_rel_log_adj_iitaka/scene.py", "RelLogAdjIitaka"),
    Video(2025, "ScheduleFreeHardBoundClip", "project/math/815_linear_161/2025_schedulefreehardboundclip/scene.py", "ScheduleFreeHardBoundClip"),
    Video(2026, "AdamWHardBoundClip", "project/math/815_linear_161/2026_adamwhardboundclip/scene.py", "AdamWHardBoundClip"),
    Video(2027, "LionSoftBoundHard", "project/math/815_linear_161/2027_lionsoftboundhard/scene.py", "LionSoftBoundHard"),
    Video(2028, "垂心類似九点弧比", "project/math/816_geometry_161/2028_h_sym_nine_arc/scene.py", "HSymNineArc"),
    Video(2029, "重心類似九点弧比", "project/math/816_geometry_161/2029_g_sym_nine_arc/scene.py", "GSymNineArc"),
    Video(2030, "九点類似弧比", "project/math/816_geometry_161/2030_n_sym_nine_arc/scene.py", "NSymNineArc"),
    Video(2031, "経験局所スケール被覆", "project/math/817_probability_159/2031_emp_local_scale_cov/scene.py", "EmpLocalScaleCov"),
    Video(2032, "経験局所スケールパッキング", "project/math/817_probability_159/2032_emp_local_scale_pack/scene.py", "EmpLocalScalePack"),
    Video(2033, "ラベル増加木細分", "project/math/818_combinatorics_158/2033_labeled_inc_tree/scene.py", "LabeledIncTree"),
)

VIDEOS_2034_2045: tuple[Video, ...] = (
    Video(2034, "ログ随伴フリップ対", "project/math/819_analysis_162/2034_log_adj_flip/scene.py", "LogAdjFlip"),
    Video(2035, "相対ログ随伴フリップ対", "project/math/819_analysis_162/2035_rel_log_adj_flip/scene.py", "RelLogAdjFlip"),
    Video(2036, "ログ随伴フロップ対", "project/math/819_analysis_162/2036_log_adj_flop/scene.py", "LogAdjFlop"),
    Video(2037, "SophiaSoftBoundHard", "project/math/820_linear_162/2037_sophiasoftboundhard/scene.py", "SophiaSoftBoundHard"),
    Video(2038, "ApolloHardBoundClip", "project/math/820_linear_162/2038_apollohardboundclip/scene.py", "ApolloHardBoundClip"),
    Video(2039, "MuonSoftBoundHard", "project/math/820_linear_162/2039_muonsoftboundhard/scene.py", "MuonSoftBoundHard"),
    Video(2040, "内心九点中心弦比", "project/math/821_geometry_162/2040_in_nine_center_chord/scene.py", "InNineCenterChord"),
    Video(2041, "傍心九点中心弦比", "project/math/821_geometry_162/2041_ex_nine_center_chord/scene.py", "ExNineCenterChord"),
    Video(2042, "外心九点中心弦比", "project/math/821_geometry_162/2042_o_nine_center_chord/scene.py", "ONineCenterChord"),
    Video(2043, "一様データ半径被覆", "project/math/822_probability_160/2043_unif_data_radius_cov/scene.py", "UnifDataRadiusCov"),
    Video(2044, "一様データ半径パッキング", "project/math/822_probability_160/2044_unif_data_radius_pack/scene.py", "UnifDataRadiusPack"),
    Video(2045, "三分増加木細分", "project/math/823_combinatorics_159/2045_ternary_inc_tree/scene.py", "TernaryIncTree"),
)

VIDEOS_2046_2057: tuple[Video, ...] = (
    Video(2046, "相対ログ随伴フロップ対", "project/math/824_analysis_163/2046_rel_log_adj_flop/scene.py", "RelLogAdjFlop"),
    Video(2047, "ログ随伴収縮対", "project/math/824_analysis_163/2047_log_adj_contraction/scene.py", "LogAdjContraction"),
    Video(2048, "相対ログ随伴収縮対", "project/math/824_analysis_163/2048_rel_log_adj_contraction/scene.py", "RelLogAdjContraction"),
    Video(2049, "RMSSoftBoundHard", "project/math/825_linear_163/2049_rmssoftboundhard/scene.py", "RMSSoftBoundHard"),
    Video(2050, "LookaheadHardBoundClip", "project/math/825_linear_163/2050_lookaheadhardboundclip/scene.py", "LookaheadHardBoundClip"),
    Video(2051, "ProdigySoftBoundHard", "project/math/825_linear_163/2051_prodigysoftboundhard/scene.py", "ProdigySoftBoundHard"),
    Video(2052, "垂心九点中心弦比", "project/math/826_geometry_163/2052_h_nine_center_chord/scene.py", "HNineCenterChord"),
    Video(2053, "重心九点中心弦比", "project/math/826_geometry_163/2053_g_nine_center_chord/scene.py", "GNineCenterChord"),
    Video(2054, "九点中心弦比", "project/math/826_geometry_163/2054_nine_center_chord/scene.py", "NineCenterChord"),
    Video(2055, "局所経験半径被覆", "project/math/827_probability_161/2055_local_emp_radius_cov/scene.py", "LocalEmpRadiusCov"),
    Video(2056, "局所経験半径パッキング", "project/math/827_probability_161/2056_local_emp_radius_pack/scene.py", "LocalEmpRadiusPack"),
    Video(2057, "二分増加森細分", "project/math/828_combinatorics_160/2057_binary_inc_forest/scene.py", "BinaryIncForest"),
)

VIDEOS_2058_2069: tuple[Video, ...] = (
    Video(2058, "ログ随伴終端対", "project/math/829_analysis_164/2058_log_adj_terminal/scene.py", "LogAdjTerminal"),
    Video(2059, "相対ログ随伴終端対", "project/math/829_analysis_164/2059_rel_log_adj_terminal/scene.py", "RelLogAdjTerminal"),
    Video(2060, "ログ随伴極小対", "project/math/829_analysis_164/2060_log_adj_minimal/scene.py", "LogAdjMinimal"),
    Video(2061, "ScheduleFreeSoftBoundHard", "project/math/830_linear_164/2061_schedulefreesoftboundhard/scene.py", "ScheduleFreeSoftBoundHard"),
    Video(2062, "AdamWSoftBoundHard", "project/math/830_linear_164/2062_adamwsoftboundhard/scene.py", "AdamWSoftBoundHard"),
    Video(2063, "LionHardBoundClip", "project/math/830_linear_164/2063_lionhardboundclip/scene.py", "LionHardBoundClip"),
    Video(2064, "内心九点弦弧比", "project/math/831_geometry_164/2064_in_nine_chord_arc/scene.py", "InNineChordArc"),
    Video(2065, "傍心九点弦弧比", "project/math/831_geometry_164/2065_ex_nine_chord_arc/scene.py", "ExNineChordArc"),
    Video(2066, "外心九点弦弧比", "project/math/831_geometry_164/2066_o_nine_chord_arc/scene.py", "ONineChordArc"),
    Video(2067, "一様局所スケール被覆", "project/math/832_probability_162/2067_unif_local_scale_cov/scene.py", "UnifLocalScaleCov"),
    Video(2068, "一様局所スケールパッキング", "project/math/832_probability_162/2068_unif_local_scale_pack/scene.py", "UnifLocalScalePack"),
    Video(2069, "根つきラベル増加木細分", "project/math/833_combinatorics_161/2069_rooted_labeled_inc_tree/scene.py", "RootedLabeledIncTree"),
)

VIDEOS_2070_2081: tuple[Video, ...] = (
    Video(2070, "相対ログ随伴極小対", "project/math/834_analysis_165/2070_rel_log_adj_minimal/scene.py", "RelLogAdjMinimal"),
    Video(2071, "ログ随伴終局対", "project/math/834_analysis_165/2071_log_adj_final/scene.py", "LogAdjFinal"),
    Video(2072, "相対ログ随伴終局対", "project/math/834_analysis_165/2072_rel_log_adj_final/scene.py", "RelLogAdjFinal"),
    Video(2073, "SophiaHardBoundClip", "project/math/835_linear_165/2073_sophiahardboundclip/scene.py", "SophiaHardBoundClip"),
    Video(2074, "ApolloSoftBoundHard", "project/math/835_linear_165/2074_apollosoftboundhard/scene.py", "ApolloSoftBoundHard"),
    Video(2075, "MuonHardSoftBound", "project/math/835_linear_165/2075_muonhardsoftbound/scene.py", "MuonHardSoftBound"),
    Video(2076, "垂心九点弦弧比", "project/math/836_geometry_165/2076_h_nine_chord_arc/scene.py", "HNineChordArc"),
    Video(2077, "重心九点弦弧比", "project/math/836_geometry_165/2077_g_nine_chord_arc/scene.py", "GNineChordArc"),
    Video(2078, "九点弦弧比", "project/math/836_geometry_165/2078_nine_chord_arc/scene.py", "NineChordArc"),
    Video(2079, "経験データ半径被覆", "project/math/837_probability_163/2079_emp_data_radius_cov/scene.py", "EmpDataRadiusCov"),
    Video(2080, "経験データ半径パッキング", "project/math/837_probability_163/2080_emp_data_radius_pack/scene.py", "EmpDataRadiusPack"),
    Video(2081, "ケイリー増加森細分", "project/math/838_combinatorics_162/2081_cayley_inc_forest/scene.py", "CayleyIncForest"),
)

VIDEOS_2082_2093: tuple[Video, ...] = (
    Video(2082, "ログ随伴標準対", "project/math/839_analysis_166/2082_log_adj_canonical/scene.py", "LogAdjCanonical"),
    Video(2083, "相対ログ随伴標準対", "project/math/839_analysis_166/2083_rel_log_adj_canonical/scene.py", "RelLogAdjCanonical"),
    Video(2084, "ログ随伴正則対", "project/math/839_analysis_166/2084_log_adj_regular/scene.py", "LogAdjRegular"),
    Video(2085, "RMSClipHardBound", "project/math/840_linear_166/2085_rmscliphardbound/scene.py", "RMSClipHardBound"),
    Video(2086, "LookaheadSoftBoundHard", "project/math/840_linear_166/2086_lookaheadsoftboundhard/scene.py", "LookaheadSoftBoundHard"),
    Video(2087, "ProdigyHardSoftBound", "project/math/840_linear_166/2087_prodigyhardsoftbound/scene.py", "ProdigyHardSoftBound"),
    Video(2088, "内心九点弧弦比", "project/math/841_geometry_166/2088_in_nine_arc_chord/scene.py", "InNineArcChord"),
    Video(2089, "傍心九点弧弦比", "project/math/841_geometry_166/2089_ex_nine_arc_chord/scene.py", "ExNineArcChord"),
    Video(2090, "外心九点弧弦比", "project/math/841_geometry_166/2090_o_nine_arc_chord/scene.py", "ONineArcChord"),
    Video(2091, "局所一様半径被覆", "project/math/842_probability_164/2091_local_unif_radius_cov/scene.py", "LocalUnifRadiusCov"),
    Video(2092, "局所一様半径パッキング", "project/math/842_probability_164/2092_local_unif_radius_pack/scene.py", "LocalUnifRadiusPack"),
    Video(2093, "三分増加森細分", "project/math/843_combinatorics_163/2093_ternary_inc_forest/scene.py", "TernaryIncForest"),
)

VIDEOS_2094_2105: tuple[Video, ...] = (
    Video(2094, "相対ログ随伴正則対", "project/math/844_analysis_167/2094_rel_log_adj_regular/scene.py", "RelLogAdjRegular"),
    Video(2095, "ログ随伴平滑対", "project/math/844_analysis_167/2095_log_adj_smooth/scene.py", "LogAdjSmooth"),
    Video(2096, "相対ログ随伴平滑対", "project/math/844_analysis_167/2096_rel_log_adj_smooth/scene.py", "RelLogAdjSmooth"),
    Video(2097, "ScheduleFreeHardSoftBound", "project/math/845_linear_167/2097_schedulefreehardsoftbound/scene.py", "ScheduleFreeHardSoftBound"),
    Video(2098, "AdamWHardSoftBound", "project/math/845_linear_167/2098_adamwhardsoftbound/scene.py", "AdamWHardSoftBound"),
    Video(2099, "LionClipSoftBound", "project/math/845_linear_167/2099_lionclipsoftbound/scene.py", "LionClipSoftBound"),
    Video(2100, "垂心九点弧弦比", "project/math/846_geometry_167/2100_h_nine_arc_chord/scene.py", "HNineArcChord"),
    Video(2101, "重心九点弧弦比", "project/math/846_geometry_167/2101_g_nine_arc_chord/scene.py", "GNineArcChord"),
    Video(2102, "九点弧弦比", "project/math/846_geometry_167/2102_nine_arc_chord/scene.py", "NineArcChord"),
    Video(2103, "経験一様半径被覆", "project/math/847_probability_165/2103_emp_unif_radius_cov/scene.py", "EmpUnifRadiusCov"),
    Video(2104, "経験一様半径パッキング", "project/math/847_probability_165/2104_emp_unif_radius_pack/scene.py", "EmpUnifRadiusPack"),
    Video(2105, "ラベル増加森細分", "project/math/848_combinatorics_164/2105_labeled_inc_forest/scene.py", "LabeledIncForest"),
)

VIDEOS_2106_2117: tuple[Video, ...] = (
    Video(2106, "ログ随伴準正則対", "project/math/849_analysis_168/2106_log_adj_semiregular/scene.py", "LogAdjSemiregular"),
    Video(2107, "相対ログ随伴準正則対", "project/math/849_analysis_168/2107_rel_log_adj_semiregular/scene.py", "RelLogAdjSemiregular"),
    Video(2108, "ログ随伴準平滑対", "project/math/849_analysis_168/2108_log_adj_semismooth/scene.py", "LogAdjSemismooth"),
    Video(2109, "SophiaClipSoftBound", "project/math/850_linear_168/2109_sophiaclipsoftbound/scene.py", "SophiaClipSoftBound"),
    Video(2110, "ApolloHardSoftBound", "project/math/850_linear_168/2110_apollohardsoftbound/scene.py", "ApolloHardSoftBound"),
    Video(2111, "MuonBoundSoftHard", "project/math/850_linear_168/2111_muonboundsofthard/scene.py", "MuonBoundSoftHard"),
    Video(2112, "内心類似九点中心弧比", "project/math/851_geometry_168/2112_in_sym_nine_center_arc/scene.py", "InSymNineCenterArc"),
    Video(2113, "傍心類似九点中心弧比", "project/math/851_geometry_168/2113_ex_sym_nine_center_arc/scene.py", "ExSymNineCenterArc"),
    Video(2114, "外心類似九点中心弧比", "project/math/851_geometry_168/2114_o_sym_nine_center_arc/scene.py", "OSymNineCenterArc"),
    Video(2115, "一様経験半径被覆", "project/math/852_probability_166/2115_unif_emp_radius_cov/scene.py", "UnifEmpRadiusCov"),
    Video(2116, "一様経験半径パッキング", "project/math/852_probability_166/2116_unif_emp_radius_pack/scene.py", "UnifEmpRadiusPack"),
    Video(2117, "無根増加森細分", "project/math/853_combinatorics_165/2117_unrooted_inc_forest/scene.py", "UnrootedIncForest"),
)

VIDEOS_2118_2129: tuple[Video, ...] = (
    Video(2118, "相対ログ随伴準平滑対", "project/math/854_analysis_169/2118_rel_log_adj_semismooth/scene.py", "RelLogAdjSemismooth"),
    Video(2119, "ログ随伴純粋対", "project/math/854_analysis_169/2119_log_adj_pure/scene.py", "LogAdjPure"),
    Video(2120, "相対ログ随伴純粋対", "project/math/854_analysis_169/2120_rel_log_adj_pure/scene.py", "RelLogAdjPure"),
    Video(2121, "RMSBoundSoftHard", "project/math/855_linear_169/2121_rmsboundsofthard/scene.py", "RMSBoundSoftHard"),
    Video(2122, "LookaheadClipHardBound", "project/math/855_linear_169/2122_lookaheadcliphardbound/scene.py", "LookaheadClipHardBound"),
    Video(2123, "ProdigyClipSoftBound", "project/math/855_linear_169/2123_prodigyclipsoftbound/scene.py", "ProdigyClipSoftBound"),
    Video(2124, "垂心類似九点中心弧比", "project/math/856_geometry_169/2124_h_sym_nine_center_arc/scene.py", "HSymNineCenterArc"),
    Video(2125, "重心類似九点中心弧比", "project/math/856_geometry_169/2125_g_sym_nine_center_arc/scene.py", "GSymNineCenterArc"),
    Video(2126, "九点類似中心弧比", "project/math/856_geometry_169/2126_n_sym_nine_center_arc/scene.py", "NSymNineCenterArc"),
    Video(2127, "局所データスケール被覆", "project/math/857_probability_167/2127_local_data_scale_cov/scene.py", "LocalDataScaleCov"),
    Video(2128, "局所データスケールパッキング", "project/math/857_probability_167/2128_local_data_scale_pack/scene.py", "LocalDataScalePack"),
    Video(2129, "有向増加森細分", "project/math/858_combinatorics_166/2129_directed_inc_forest/scene.py", "DirectedIncForest"),
)

VIDEOS_2130_2141: tuple[Video, ...] = (
    Video(2130, "ログ随伴純正則対", "project/math/859_analysis_170/2130_log_adj_pure_regular/scene.py", "LogAdjPureRegular"),
    Video(2131, "相対ログ随伴純正則対", "project/math/859_analysis_170/2131_rel_log_adj_pure_regular/scene.py", "RelLogAdjPureRegular"),
    Video(2132, "ログ随伴純平滑対", "project/math/859_analysis_170/2132_log_adj_pure_smooth/scene.py", "LogAdjPureSmooth"),
    Video(2133, "ScheduleFreeClipSoftBound", "project/math/860_linear_170/2133_schedulefreeclipsoftbound/scene.py", "ScheduleFreeClipSoftBound"),
    Video(2134, "AdamWClipSoftBound", "project/math/860_linear_170/2134_adamwclipsoftbound/scene.py", "AdamWClipSoftBound"),
    Video(2135, "LionBoundSoftHard", "project/math/860_linear_170/2135_lionboundsofthard/scene.py", "LionBoundSoftHard"),
    Video(2136, "内心九点弦半径比", "project/math/861_geometry_170/2136_in_nine_chord_radius/scene.py", "InNineChordRadius"),
    Video(2137, "傍心九点弦半径比", "project/math/861_geometry_170/2137_ex_nine_chord_radius/scene.py", "ExNineChordRadius"),
    Video(2138, "外心九点弦半径比", "project/math/861_geometry_170/2138_o_nine_chord_radius/scene.py", "ONineChordRadius"),
    Video(2139, "経験局所半径被覆", "project/math/862_probability_168/2139_emp_local_radius_cov/scene.py", "EmpLocalRadiusCov"),
    Video(2140, "経験局所半径パッキング", "project/math/862_probability_168/2140_emp_local_radius_pack/scene.py", "EmpLocalRadiusPack"),
    Video(2141, "平面根つき増加森細分", "project/math/863_combinatorics_167/2141_planar_rooted_inc_forest/scene.py", "PlanarRootedIncForest"),
)

VIDEOS_2142_2153: tuple[Video, ...] = (
    Video(2142, "相対ログ随伴純平滑対", "project/math/864_analysis_171/2142_rel_log_adj_pure_smooth/scene.py", "RelLogAdjPureSmooth"),
    Video(2143, "ログ随伴準終端対", "project/math/864_analysis_171/2143_log_adj_semiterminal/scene.py", "LogAdjSemiterminal"),
    Video(2144, "相対ログ随伴準終端対", "project/math/864_analysis_171/2144_rel_log_adj_semiterminal/scene.py", "RelLogAdjSemiterminal"),
    Video(2145, "SophiaBoundSoftHard", "project/math/865_linear_171/2145_sophiaboundsofthard/scene.py", "SophiaBoundSoftHard"),
    Video(2146, "ApolloClipSoftBound", "project/math/865_linear_171/2146_apolloclipsoftbound/scene.py", "ApolloClipSoftBound"),
    Video(2147, "MuonClipSoftBound", "project/math/865_linear_171/2147_muonclipsoftbound/scene.py", "MuonClipSoftBound"),
    Video(2148, "垂心九点弦半径比", "project/math/866_geometry_171/2148_h_nine_chord_radius/scene.py", "HNineChordRadius"),
    Video(2149, "重心九点弦半径比", "project/math/866_geometry_171/2149_g_nine_chord_radius/scene.py", "GNineChordRadius"),
    Video(2150, "九点弦半径比", "project/math/866_geometry_171/2150_nine_chord_radius/scene.py", "NineChordRadius"),
    Video(2151, "一様データスケール被覆", "project/math/867_probability_169/2151_unif_data_scale_cov/scene.py", "UnifDataScaleCov"),
    Video(2152, "一様データスケールパッキング", "project/math/867_probability_169/2152_unif_data_scale_pack/scene.py", "UnifDataScalePack"),
    Video(2153, "増加林細分", "project/math/868_combinatorics_168/2153_inc_grove/scene.py", "IncGrove"),
)

VIDEOS_2154_2165: tuple[Video, ...] = (
    Video(2154, "ログ随伴準正対", "project/math/869_analysis_172/2154_log_adj_semipositive/scene.py", "LogAdjSemipositive"),
    Video(2155, "相対ログ随伴準正対", "project/math/869_analysis_172/2155_rel_log_adj_semipositive/scene.py", "RelLogAdjSemipositive"),
    Video(2156, "ログ随伴強終端対", "project/math/869_analysis_172/2156_log_adj_strong_terminal/scene.py", "LogAdjStrongTerminal"),
    Video(2157, "RMSHardSoftBound", "project/math/870_linear_172/2157_rmshardsoftbound/scene.py", "RMSHardSoftBound"),
    Video(2158, "LookaheadBoundSoftHard", "project/math/870_linear_172/2158_lookaheadboundsofthard/scene.py", "LookaheadBoundSoftHard"),
    Video(2159, "ProdigyBoundSoftHard", "project/math/870_linear_172/2159_prodigyboundsofthard/scene.py", "ProdigyBoundSoftHard"),
    Video(2160, "内心九点弧半径比", "project/math/871_geometry_172/2160_in_nine_arc_radius/scene.py", "InNineArcRadius"),
    Video(2161, "傍心九点弧半径比", "project/math/871_geometry_172/2161_ex_nine_arc_radius/scene.py", "ExNineArcRadius"),
    Video(2162, "外心九点弧半径比", "project/math/871_geometry_172/2162_o_nine_arc_radius/scene.py", "ONineArcRadius"),
    Video(2163, "局所経験スケール被覆", "project/math/872_probability_170/2163_local_emp_scale_cov/scene.py", "LocalEmpScaleCov"),
    Video(2164, "局所経験スケールパッキング", "project/math/872_probability_170/2164_local_emp_scale_pack/scene.py", "LocalEmpScalePack"),
    Video(2165, "二分増加林細分", "project/math/873_combinatorics_169/2165_binary_inc_grove/scene.py", "BinaryIncGrove"),
)

VIDEOS_2166_2177: tuple[Video, ...] = (
    Video(2166, "相対ログ随伴強終端対", "project/math/874_analysis_173/2166_rel_log_adj_strong_terminal/scene.py", "RelLogAdjStrongTerminal"),
    Video(2167, "ログ随伴弱終端対", "project/math/874_analysis_173/2167_log_adj_weak_terminal/scene.py", "LogAdjWeakTerminal"),
    Video(2168, "相対ログ随伴弱終端対", "project/math/874_analysis_173/2168_rel_log_adj_weak_terminal/scene.py", "RelLogAdjWeakTerminal"),
    Video(2169, "ScheduleFreeBoundSoftHard", "project/math/875_linear_173/2169_schedulefreeboundsofthard/scene.py", "ScheduleFreeBoundSoftHard"),
    Video(2170, "AdamWBoundSoftHard", "project/math/875_linear_173/2170_adamwboundsofthard/scene.py", "AdamWBoundSoftHard"),
    Video(2171, "LionClipHardBound", "project/math/875_linear_173/2171_lioncliphardbound/scene.py", "LionClipHardBound"),
    Video(2172, "垂心九点弧半径比", "project/math/876_geometry_173/2172_h_nine_arc_radius/scene.py", "HNineArcRadius"),
    Video(2173, "重心九点弧半径比", "project/math/876_geometry_173/2173_g_nine_arc_radius/scene.py", "GNineArcRadius"),
    Video(2174, "九点弧半径比", "project/math/876_geometry_173/2174_nine_arc_radius/scene.py", "NineArcRadius"),
    Video(2175, "経験データスケール被覆", "project/math/877_probability_171/2175_emp_data_scale_cov/scene.py", "EmpDataScaleCov"),
    Video(2176, "経験データスケールパッキング", "project/math/877_probability_171/2176_emp_data_scale_pack/scene.py", "EmpDataScalePack"),
    Video(2177, "三分増加林細分", "project/math/878_combinatorics_170/2177_ternary_inc_grove/scene.py", "TernaryIncGrove"),
)

VIDEOS_2178_2189: tuple[Video, ...] = (
    Video(2178, "ログ随伴強正則対", "project/math/879_analysis_174/2178_log_adj_strong_regular/scene.py", "LogAdjStrongRegular"),
    Video(2179, "相対ログ随伴強正則対", "project/math/879_analysis_174/2179_rel_log_adj_strong_regular/scene.py", "RelLogAdjStrongRegular"),
    Video(2180, "ログ随伴弱正則対", "project/math/879_analysis_174/2180_log_adj_weak_regular/scene.py", "LogAdjWeakRegular"),
    Video(2181, "SophiaClipHardBound", "project/math/880_linear_174/2181_sophiacliphardbound/scene.py", "SophiaClipHardBound"),
    Video(2182, "ApolloBoundSoftHard", "project/math/880_linear_174/2182_apolloboundsofthard/scene.py", "ApolloBoundSoftHard"),
    Video(2183, "MuonBoundHardSoft", "project/math/880_linear_174/2183_muonboundhardsoft/scene.py", "MuonBoundHardSoft"),
    Video(2184, "内心類似九点弦弧比", "project/math/881_geometry_174/2184_in_sym_nine_chord_arc/scene.py", "InSymNineChordArc"),
    Video(2185, "傍心類似九点弦弧比", "project/math/881_geometry_174/2185_ex_sym_nine_chord_arc/scene.py", "ExSymNineChordArc"),
    Video(2186, "外心類似九点弦弧比", "project/math/881_geometry_174/2186_o_sym_nine_chord_arc/scene.py", "OSymNineChordArc"),
    Video(2187, "一様経験スケール被覆", "project/math/882_probability_172/2187_unif_emp_scale_cov/scene.py", "UnifEmpScaleCov"),
    Video(2188, "一様経験スケールパッキング", "project/math/882_probability_172/2188_unif_emp_scale_pack/scene.py", "UnifEmpScalePack"),
    Video(2189, "ラベル増加林細分", "project/math/883_combinatorics_171/2189_labeled_inc_grove/scene.py", "LabeledIncGrove"),
)

VIDEOS_2190_2201: tuple[Video, ...] = (
    Video(2190, "相対ログ随伴弱正則対", "project/math/884_analysis_175/2190_rel_log_adj_weak_regular/scene.py", "RelLogAdjWeakRegular"),
    Video(2191, "ログ随伴強平滑対", "project/math/884_analysis_175/2191_log_adj_strong_smooth/scene.py", "LogAdjStrongSmooth"),
    Video(2192, "相対ログ随伴強平滑対", "project/math/884_analysis_175/2192_rel_log_adj_strong_smooth/scene.py", "RelLogAdjStrongSmooth"),
    Video(2193, "RMSClipSoftBound", "project/math/885_linear_175/2193_rmsclipsoftbound/scene.py", "RMSClipSoftBound"),
    Video(2194, "LookaheadClipSoftBound", "project/math/885_linear_175/2194_lookaheadclipsoftbound/scene.py", "LookaheadClipSoftBound"),
    Video(2195, "ProdigyClipHardBound", "project/math/885_linear_175/2195_prodigycliphardbound/scene.py", "ProdigyClipHardBound"),
    Video(2196, "垂心類似九点弦弧比", "project/math/886_geometry_175/2196_h_sym_nine_chord_arc/scene.py", "HSymNineChordArc"),
    Video(2197, "重心類似九点弦弧比", "project/math/886_geometry_175/2197_g_sym_nine_chord_arc/scene.py", "GSymNineChordArc"),
    Video(2198, "九点類似弦弧比", "project/math/886_geometry_175/2198_n_sym_nine_chord_arc/scene.py", "NSymNineChordArc"),
    Video(2199, "局所一様データ被覆", "project/math/887_probability_173/2199_local_unif_data_cov/scene.py", "LocalUnifDataCov"),
    Video(2200, "局所一様データパッキング", "project/math/887_probability_173/2200_local_unif_data_pack/scene.py", "LocalUnifDataPack"),
    Video(2201, "根つき増加林細分", "project/math/888_combinatorics_172/2201_rooted_inc_grove/scene.py", "RootedIncGrove"),
)

VIDEOS_2202_2213: tuple[Video, ...] = (
    Video(2202, "ログ随伴弱平滑対", "project/math/889_analysis_176/2202_log_adj_weak_smooth/scene.py", "LogAdjWeakSmooth"),
    Video(2203, "相対ログ随伴弱平滑対", "project/math/889_analysis_176/2203_rel_log_adj_weak_smooth/scene.py", "RelLogAdjWeakSmooth"),
    Video(2204, "ログ随伴準標準対", "project/math/889_analysis_176/2204_log_adj_semiclassical/scene.py", "LogAdjSemiclassical"),
    Video(2205, "ScheduleFreeClipHardBound", "project/math/890_linear_176/2205_schedulefreecliphardbound/scene.py", "ScheduleFreeClipHardBound"),
    Video(2206, "AdamWClipHardBound", "project/math/890_linear_176/2206_adamwcliphardbound/scene.py", "AdamWClipHardBound"),
    Video(2207, "LionHardSoftBound", "project/math/890_linear_176/2207_lionhardsoftbound/scene.py", "LionHardSoftBound"),
    Video(2208, "内心九点中心弧比", "project/math/891_geometry_176/2208_in_nine_center_arc/scene.py", "InNineCenterArc"),
    Video(2209, "傍心九点中心弧比", "project/math/891_geometry_176/2209_ex_nine_center_arc/scene.py", "ExNineCenterArc"),
    Video(2210, "外心九点中心弧比", "project/math/891_geometry_176/2210_o_nine_center_arc/scene.py", "ONineCenterArc"),
    Video(2211, "経験一様データ被覆", "project/math/892_probability_174/2211_emp_unif_data_cov/scene.py", "EmpUnifDataCov"),
    Video(2212, "経験一様データパッキング", "project/math/892_probability_174/2212_emp_unif_data_pack/scene.py", "EmpUnifDataPack"),
    Video(2213, "無根増加林細分", "project/math/893_combinatorics_173/2213_unrooted_inc_grove/scene.py", "UnrootedIncGrove"),
)

VIDEOS_2214_2225: tuple[Video, ...] = (
    Video(2214, "相対ログ随伴準標準対", "project/math/894_analysis_177/2214_rel_log_adj_semiclassical/scene.py", "RelLogAdjSemiclassical"),
    Video(2215, "ログ随伴強標準対", "project/math/894_analysis_177/2215_log_adj_strong_canonical/scene.py", "LogAdjStrongCanonical"),
    Video(2216, "相対ログ随伴強標準対", "project/math/894_analysis_177/2216_rel_log_adj_strong_canonical/scene.py", "RelLogAdjStrongCanonical"),
    Video(2217, "SophiaHardSoftBound", "project/math/895_linear_177/2217_sophiahardsoftbound/scene.py", "SophiaHardSoftBound"),
    Video(2218, "ApolloClipHardBound", "project/math/895_linear_177/2218_apollocliphardbound/scene.py", "ApolloClipHardBound"),
    Video(2219, "MuonClipHardBound", "project/math/895_linear_177/2219_muoncliphardbound/scene.py", "MuonClipHardBound"),
    Video(2220, "垂心九点中心弧比", "project/math/896_geometry_177/2220_h_nine_center_arc/scene.py", "HNineCenterArc"),
    Video(2221, "重心九点中心弧比", "project/math/896_geometry_177/2221_g_nine_center_arc/scene.py", "GNineCenterArc"),
    Video(2222, "九点中心弧比", "project/math/896_geometry_177/2222_nine_center_arc/scene.py", "NineCenterArc"),
    Video(2223, "一様局所半径被覆", "project/math/897_probability_175/2223_unif_local_radius_cov/scene.py", "UnifLocalRadiusCov"),
    Video(2224, "一様局所半径パッキング", "project/math/897_probability_175/2224_unif_local_radius_pack/scene.py", "UnifLocalRadiusPack"),
    Video(2225, "有向増加林細分", "project/math/898_combinatorics_174/2225_directed_inc_grove/scene.py", "DirectedIncGrove"),
)

VIDEOS_2226_2237: tuple[Video, ...] = (
    Video(2226, "ログ随伴弱標準対", "project/math/899_analysis_178/2226_log_adj_weak_canonical/scene.py", "LogAdjWeakCanonical"),
    Video(2227, "相対ログ随伴弱標準対", "project/math/899_analysis_178/2227_rel_log_adj_weak_canonical/scene.py", "RelLogAdjWeakCanonical"),
    Video(2228, "ログ随伴準極小対", "project/math/899_analysis_178/2228_log_adj_semiminimal/scene.py", "LogAdjSemiminimal"),
    Video(2229, "RMSBoundHardSoft", "project/math/900_linear_178/2229_rmsboundhardsoft/scene.py", "RMSBoundHardSoft"),
    Video(2230, "LookaheadHardSoftBound", "project/math/900_linear_178/2230_lookaheadhardsoftbound/scene.py", "LookaheadHardSoftBound"),
    Video(2231, "ProdigySoftHardBound", "project/math/900_linear_178/2231_prodigysofthardbound/scene.py", "ProdigySoftHardBound"),
    Video(2232, "内心類似九点弧弦比", "project/math/901_geometry_178/2232_in_sym_nine_arc_chord/scene.py", "InSymNineArcChord"),
    Video(2233, "傍心類似九点弧弦比", "project/math/901_geometry_178/2233_ex_sym_nine_arc_chord/scene.py", "ExSymNineArcChord"),
    Video(2234, "外心類似九点弧弦比", "project/math/901_geometry_178/2234_o_sym_nine_arc_chord/scene.py", "OSymNineArcChord"),
    Video(2235, "局所スケールデータ被覆", "project/math/902_probability_176/2235_local_scale_data_cov/scene.py", "LocalScaleDataCov"),
    Video(2236, "局所スケールデータパッキング", "project/math/902_probability_176/2236_local_scale_data_pack/scene.py", "LocalScaleDataPack"),
    Video(2237, "平面増加林細分", "project/math/903_combinatorics_175/2237_planar_inc_grove/scene.py", "PlanarIncGrove"),
)

VIDEOS_2238_2249: tuple[Video, ...] = (
    Video(2238, "相対ログ随伴準極小対", "project/math/904_analysis_179/2238_rel_log_adj_semiminimal/scene.py", "RelLogAdjSemiminimal"),
    Video(2239, "ログ随伴準終局対", "project/math/904_analysis_179/2239_log_adj_semifinal/scene.py", "LogAdjSemifinal"),
    Video(2240, "相対ログ随伴準終局対", "project/math/904_analysis_179/2240_rel_log_adj_semifinal/scene.py", "RelLogAdjSemifinal"),
    Video(2241, "ScheduleFreeHardBoundSoft", "project/math/905_linear_179/2241_schedulefreehardboundsoft/scene.py", "ScheduleFreeHardBoundSoft"),
    Video(2242, "AdamWHardBoundSoft", "project/math/905_linear_179/2242_adamwhardboundsoft/scene.py", "AdamWHardBoundSoft"),
    Video(2243, "LionSoftHardBound", "project/math/905_linear_179/2243_lionsofthardbound/scene.py", "LionSoftHardBound"),
    Video(2244, "垂心類似九点弧弦比", "project/math/906_geometry_179/2244_h_sym_nine_arc_chord/scene.py", "HSymNineArcChord"),
    Video(2245, "重心類似九点弧弦比", "project/math/906_geometry_179/2245_g_sym_nine_arc_chord/scene.py", "GSymNineArcChord"),
    Video(2246, "九点類似弧弦比", "project/math/906_geometry_179/2246_n_sym_nine_arc_chord/scene.py", "NSymNineArcChord"),
    Video(2247, "経験スケールデータ被覆", "project/math/907_probability_177/2247_emp_scale_data_cov/scene.py", "EmpScaleDataCov"),
    Video(2248, "経験スケールデータパッキング", "project/math/907_probability_177/2248_emp_scale_data_pack/scene.py", "EmpScaleDataPack"),
    Video(2249, "ケイリー増加林細分", "project/math/908_combinatorics_176/2249_cayley_inc_grove/scene.py", "CayleyIncGrove"),
)

VIDEOS_2250_2261: tuple[Video, ...] = (
    Video(2250, "ログ随伴準フリップ対", "project/math/909_analysis_180/2250_log_adj_semiflip/scene.py", "LogAdjSemiflip"),
    Video(2251, "相対ログ随伴準フリップ対", "project/math/909_analysis_180/2251_rel_log_adj_semiflip/scene.py", "RelLogAdjSemiflip"),
    Video(2252, "ログ随伴準フロップ対", "project/math/909_analysis_180/2252_log_adj_semiflop/scene.py", "LogAdjSemiflop"),
    Video(2253, "SophiaSoftHardBound", "project/math/910_linear_180/2253_sophiasofthardbound/scene.py", "SophiaSoftHardBound"),
    Video(2254, "ApolloHardBoundSoft", "project/math/910_linear_180/2254_apollohardboundsoft/scene.py", "ApolloHardBoundSoft"),
    Video(2255, "MuonHardBoundSoft", "project/math/910_linear_180/2255_muonhardboundsoft/scene.py", "MuonHardBoundSoft"),
    Video(2256, "内心九点弧心比", "project/math/911_geometry_180/2256_in_nine_arc_center/scene.py", "InNineArcCenter"),
    Video(2257, "傍心九点弧心比", "project/math/911_geometry_180/2257_ex_nine_arc_center/scene.py", "ExNineArcCenter"),
    Video(2258, "外心九点弧心比", "project/math/911_geometry_180/2258_o_nine_arc_center/scene.py", "ONineArcCenter"),
    Video(2259, "一様スケールデータ被覆", "project/math/912_probability_178/2259_unif_scale_data_cov/scene.py", "UnifScaleDataCov"),
    Video(2260, "一様スケールデータパッキング", "project/math/912_probability_178/2260_unif_scale_data_pack/scene.py", "UnifScaleDataPack"),
    Video(2261, "増加林根細分", "project/math/913_combinatorics_177/2261_inc_grove_root/scene.py", "IncGroveRoot"),
)

VIDEOS_2262_2273: tuple[Video, ...] = (
    Video(2262, "相対ログ随伴準フロップ対", "project/math/914_analysis_181/2262_rel_log_adj_semiflop/scene.py", "RelLogAdjSemiflop"),
    Video(2263, "ログ随伴準収縮対", "project/math/914_analysis_181/2263_log_adj_semicontraction/scene.py", "LogAdjSemicontraction"),
    Video(2264, "相対ログ随伴準収縮対", "project/math/914_analysis_181/2264_rel_log_adj_semicontraction/scene.py", "RelLogAdjSemicontraction"),
    Video(2265, "RMSSoftHardBound", "project/math/915_linear_181/2265_rmssofthardbound/scene.py", "RMSSoftHardBound"),
    Video(2266, "LookaheadSoftHardBound", "project/math/915_linear_181/2266_lookaheadsofthardbound/scene.py", "LookaheadSoftHardBound"),
    Video(2267, "ProdigyBoundHardSoft", "project/math/915_linear_181/2267_prodigyboundhardsoft/scene.py", "ProdigyBoundHardSoft"),
    Video(2268, "垂心九点弧心比", "project/math/916_geometry_181/2268_h_nine_arc_center/scene.py", "HNineArcCenter"),
    Video(2269, "重心九点弧心比", "project/math/916_geometry_181/2269_g_nine_arc_center/scene.py", "GNineArcCenter"),
    Video(2270, "九点弧心比", "project/math/916_geometry_181/2270_nine_arc_center/scene.py", "NineArcCenter"),
    Video(2271, "局所半径データ被覆", "project/math/917_probability_179/2271_local_radius_data_cov/scene.py", "LocalRadiusDataCov"),
    Video(2272, "局所半径データパッキング", "project/math/917_probability_179/2272_local_radius_data_pack/scene.py", "LocalRadiusDataPack"),
    Video(2273, "二分増加根林細分", "project/math/918_combinatorics_178/2273_binary_inc_root_grove/scene.py", "BinaryIncRootGrove"),
)

VIDEOS_2274_2285: tuple[Video, ...] = (
    Video(2274, "ログ随伴準移動対", "project/math/919_analysis_182/2274_log_adj_semimove/scene.py", "LogAdjSemimove"),
    Video(2275, "相対ログ随伴準移動対", "project/math/919_analysis_182/2275_rel_log_adj_semimove/scene.py", "RelLogAdjSemimove"),
    Video(2276, "ログ随伴準正値対", "project/math/919_analysis_182/2276_log_adj_semipositive_pair/scene.py", "LogAdjSemipositivePair"),
    Video(2277, "ScheduleFreeSoftHardBound", "project/math/920_linear_182/2277_schedulefreesofthardbound/scene.py", "ScheduleFreeSoftHardBound"),
    Video(2278, "AdamWSoftHardBound", "project/math/920_linear_182/2278_adamwsofthardbound/scene.py", "AdamWSoftHardBound"),
    Video(2279, "LionBoundHardSoft", "project/math/920_linear_182/2279_lionboundhardsoft/scene.py", "LionBoundHardSoft"),
    Video(2280, "内心九点弦心比", "project/math/921_geometry_182/2280_in_nine_chord_center/scene.py", "InNineChordCenter"),
    Video(2281, "傍心九点弦心比", "project/math/921_geometry_182/2281_ex_nine_chord_center/scene.py", "ExNineChordCenter"),
    Video(2282, "外心九点弦心比", "project/math/921_geometry_182/2282_o_nine_chord_center/scene.py", "ONineChordCenter"),
    Video(2283, "経験半径データ被覆", "project/math/922_probability_180/2283_emp_radius_data_cov/scene.py", "EmpRadiusDataCov"),
    Video(2284, "経験半径データパッキング", "project/math/922_probability_180/2284_emp_radius_data_pack/scene.py", "EmpRadiusDataPack"),
    Video(2285, "三分増加根林細分", "project/math/923_combinatorics_179/2285_ternary_inc_root_grove/scene.py", "TernaryIncRootGrove"),
)

VIDEOS_2286_2297: tuple[Video, ...] = (
    Video(2286, "相対ログ随伴準正値対", "project/math/924_analysis_183/2286_rel_log_adj_semipositive_pair/scene.py", "RelLogAdjSemipositivePair"),
    Video(2287, "ログ随伴準体積対", "project/math/924_analysis_183/2287_log_adj_semivolume/scene.py", "LogAdjSemivolume"),
    Video(2288, "相対ログ随伴準体積対", "project/math/924_analysis_183/2288_rel_log_adj_semivolume/scene.py", "RelLogAdjSemivolume"),
    Video(2289, "SophiaBoundHardSoft", "project/math/925_linear_183/2289_sophiaboundhardsoft/scene.py", "SophiaBoundHardSoft"),
    Video(2290, "ApolloSoftHardBound", "project/math/925_linear_183/2290_apollosofthardbound/scene.py", "ApolloSoftHardBound"),
    Video(2291, "MuonClipBoundHard", "project/math/925_linear_183/2291_muonclipboundhard/scene.py", "MuonClipBoundHard"),
    Video(2292, "垂心九点弦心比", "project/math/926_geometry_183/2292_h_nine_chord_center/scene.py", "HNineChordCenter"),
    Video(2293, "重心九点弦心比", "project/math/926_geometry_183/2293_g_nine_chord_center/scene.py", "GNineChordCenter"),
    Video(2294, "九点弦心比", "project/math/926_geometry_183/2294_nine_chord_center/scene.py", "NineChordCenter"),
    Video(2295, "一様半径データ被覆", "project/math/927_probability_181/2295_unif_radius_data_cov/scene.py", "UnifRadiusDataCov"),
    Video(2296, "一様半径データパッキング", "project/math/927_probability_181/2296_unif_radius_data_pack/scene.py", "UnifRadiusDataPack"),
    Video(2297, "ラベル増加根林細分", "project/math/928_combinatorics_180/2297_labeled_inc_root_grove/scene.py", "LabeledIncRootGrove"),
)
