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
