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
