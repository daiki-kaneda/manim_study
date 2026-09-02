# アルゴリズム 200本 ディレクトリ計画

ルート: `project/curriculum_algorithm_200/`

パス: `project/curriculum_algorithm_200/D{章2桁}_{章スラッグ}/{番号3桁}_{レッスンスラッグ}/`

## 命名規則

既存の短尺シリーズ `project/math/{章番号}_{章スラッグ}/{本番号}_{レッスンスラッグ}/` に合わせ、**章フォルダの下に本フォルダ**を置く。

- ディレクトリ名は **ASCII 小文字 + 数字 + アンダースコア** のみ（日本語は使わない）。
- スラッグは英語の短い名詞句（32文字以内）。シリーズ内で重複しない。
- 本番号は ROADMAP の `#` と一致する **3桁ゼロ埋め**。
- 各本フォルダには、実装時に `storyboard.md` と `scene.py` を置く（この計画ではまだ作らない）。

このファイルは計画表である。空ディレクトリの一括作成は次の作業とする。

## 章フォルダ

| コード | フォルダ | 内容 | 本番号 |
|---|---|---|---|
| D01 | `D01_complexity/` | 導入・計算量 | #1–#10 |
| D02 | `D02_data_structures/` | 基本データ構造 | #11–#24 |
| D03 | `D03_advanced_ds/` | 高度なデータ構造 | #25–#34 |
| D04 | `D04_sorting/` | ソートアルゴリズム | #35–#46 |
| D05 | `D05_search/` | 探索アルゴリズム | #47–#56 |
| D06 | `D06_divide_and_conquer/` | 再帰・分割統治法 | #57–#66 |
| D07 | `D07_graphs/` | グラフ理論の基礎 | #67–#76 |
| D08 | `D08_shortest_paths/` | 最短路・最小全域木 | #77–#88 |
| D09 | `D09_advanced_graphs/` | 高度なグラフアルゴリズム | #89–#100 |
| D10 | `D10_dp/` | 動的計画法 | #101–#114 |
| D11 | `D11_greedy/` | 貪欲法・設計技法 | #115–#124 |
| D12 | `D12_strings/` | 文字列アルゴリズム | #125–#136 |
| D13 | `D13_number_theory/` | 数論アルゴリズム | #137–#146 |
| D14 | `D14_computational_geometry/` | 計算幾何学 | #147–#156 |
| D15 | `D15_complexity_theory/` | NP完全性・計算複雑性 | #157–#166 |
| D16 | `D16_randomized/` | ランダム化アルゴリズム | #167–#174 |
| D17 | `D17_parallel/` | 並列・分散アルゴリズム | #175–#182 |
| D18 | `D18_ml_algorithms/` | 機械学習の基礎アルゴリズム | #183–#192 |
| D19 | `D19_game_theory/` | オンライン・ゲーム理論 | #193–#196 |
| D20 | `D20_wrap_up/` | 総合演習・まとめ | #197–#200 |

## 本フォルダ（200）

| # | タイトル | パス |
|---|---|---|
| 1 | アルゴリズムとは何か | `D01_complexity/001_what_is_an_algorithm/` |
| 2 | 計算量とビッグO記法 | `D01_complexity/002_big_o/` |
| 3 | 時間計算量と空間計算量 | `D01_complexity/003_time_space_complexity/` |
| 4 | 最良・最悪・平均計算量 | `D01_complexity/004_best_worst_average/` |
| 5 | 漸近記法（Ω, Θ）の使い分け | `D01_complexity/005_omega_theta/` |
| 6 | 再帰と計算量の関係 | `D01_complexity/006_recursion_complexity/` |
| 7 | 再帰木による計算量の見積もり | `D01_complexity/007_recursion_tree/` |
| 8 | マスター定理 | `D01_complexity/008_master_theorem/` |
| 9 | 償却解析（amortized analysis）の考え方 | `D01_complexity/009_amortized_analysis/` |
| 10 | P と NP の入門 | `D01_complexity/010_p_vs_np_intro/` |
| 11 | 配列とリスト | `D02_data_structures/011_arrays_lists/` |
| 12 | 連結リスト（単方向・双方向） | `D02_data_structures/012_linked_lists/` |
| 13 | スタック | `D02_data_structures/013_stack/` |
| 14 | キュー | `D02_data_structures/014_queue/` |
| 15 | デック（両端キュー） | `D02_data_structures/015_deque/` |
| 16 | 木構造の基本 | `D02_data_structures/016_trees/` |
| 17 | 二分探索木 | `D02_data_structures/017_bst/` |
| 18 | 平衡二分探索木（AVL木の直感） | `D02_data_structures/018_avl/` |
| 19 | 赤黒木の直感 | `D02_data_structures/019_red_black_tree/` |
| 20 | ヒープと優先度付きキュー | `D02_data_structures/020_heap_priority_queue/` |
| 21 | 二項ヒープ・フィボナッチヒープの直感 | `D02_data_structures/021_binomial_fibonacci_heap/` |
| 22 | ハッシュテーブル | `D02_data_structures/022_hash_table/` |
| 23 | Union-Find（素集合データ構造） | `D02_data_structures/023_union_find/` |
| 24 | セグメント木 | `D02_data_structures/024_segment_tree/` |
| 25 | Fenwick木（Binary Indexed Tree） | `D03_advanced_ds/025_fenwick_tree/` |
| 26 | 平方分割（区間クエリの高速化） | `D03_advanced_ds/026_sqrt_decomposition/` |
| 27 | トライ木（Trie） | `D03_advanced_ds/027_trie/` |
| 28 | スキップリスト | `D03_advanced_ds/028_skip_list/` |
| 29 | レンジツリー | `D03_advanced_ds/029_range_tree/` |
| 30 | パーシステントデータ構造の考え方 | `D03_advanced_ds/030_persistent_ds/` |
| 31 | スパーステーブル | `D03_advanced_ds/031_sparse_table/` |
| 32 | LCAのためのオイラー路+セグメント木 | `D03_advanced_ds/032_lca_euler_segtree/` |
| 33 | Sqrt Decompositionの応用 | `D03_advanced_ds/033_sqrt_decomposition_apps/` |
| 34 | データ構造の総合演習 | `D03_advanced_ds/034_ds_comprehensive/` |
| 35 | バブルソート | `D04_sorting/035_bubble_sort/` |
| 36 | 選択ソート | `D04_sorting/036_selection_sort/` |
| 37 | 挿入ソート | `D04_sorting/037_insertion_sort/` |
| 38 | マージソート | `D04_sorting/038_merge_sort/` |
| 39 | クイックソート | `D04_sorting/039_quick_sort/` |
| 40 | ヒープソート | `D04_sorting/040_heap_sort/` |
| 41 | 計数ソート | `D04_sorting/041_counting_sort/` |
| 42 | バケットソート | `D04_sorting/042_bucket_sort/` |
| 43 | 基数ソート | `D04_sorting/043_radix_sort/` |
| 44 | シェルソート | `D04_sorting/044_shell_sort/` |
| 45 | 外部ソートの考え方 | `D04_sorting/045_external_sort/` |
| 46 | ソートアルゴリズムの比較と安定性 | `D04_sorting/046_sort_comparison/` |
| 47 | 線形探索 | `D05_search/047_linear_search/` |
| 48 | 二分探索 | `D05_search/048_binary_search/` |
| 49 | 二分探索の応用（境界探索・下限/上限） | `D05_search/049_binary_search_bounds/` |
| 50 | 三分探索 | `D05_search/050_ternary_search/` |
| 51 | 幅優先探索（BFS） | `D05_search/051_bfs/` |
| 52 | 深さ優先探索（DFS） | `D05_search/052_dfs/` |
| 53 | 反復深化探索 | `D05_search/053_iterative_deepening/` |
| 54 | A*探索アルゴリズム | `D05_search/054_a_star/` |
| 55 | 双方向探索 | `D05_search/055_bidirectional_search/` |
| 56 | ジャンプ探索・補間探索 | `D05_search/056_jump_interpolation_search/` |
| 57 | 再帰の基本と再帰木 | `D06_divide_and_conquer/057_recursion_basics/` |
| 58 | 分割統治法の考え方 | `D06_divide_and_conquer/058_divide_and_conquer/` |
| 59 | 累乗の高速計算（繰り返し二乗法） | `D06_divide_and_conquer/059_binary_exponentiation/` |
| 60 | 最大部分配列問題（分割統治法） | `D06_divide_and_conquer/060_max_subarray/` |
| 61 | クイックセレクト | `D06_divide_and_conquer/061_quickselect/` |
| 62 | 二分探索とメモ化の融合 | `D06_divide_and_conquer/062_binary_search_memo/` |
| 63 | ストラッセンの行列積アルゴリズム入門 | `D06_divide_and_conquer/063_strassen/` |
| 64 | 高速フーリエ変換（FFT）による多項式乗算 | `D06_divide_and_conquer/064_fft_polynomial/` |
| 65 | 分割統治法による最近点対問題 | `D06_divide_and_conquer/065_closest_pair/` |
| 66 | マンハッタン距離の最近点対 | `D06_divide_and_conquer/066_manhattan_closest_pair/` |
| 67 | グラフの表現方法（隣接行列・隣接リスト） | `D07_graphs/067_graph_representation/` |
| 68 | グラフの種類（有向・無向・重み付き） | `D07_graphs/068_graph_types/` |
| 69 | 連結性と連結成分 | `D07_graphs/069_connectivity/` |
| 70 | 木とグラフの関係 | `D07_graphs/070_trees_and_graphs/` |
| 71 | グラフの走査（BFS/DFSの応用） | `D07_graphs/071_graph_traversal/` |
| 72 | トポロジカルソート | `D07_graphs/072_topological_sort/` |
| 73 | オイラー路とハミルトン路 | `D07_graphs/073_euler_hamilton/` |
| 74 | 二部グラフ判定 | `D07_graphs/074_bipartite_check/` |
| 75 | グラフの彩色問題の入門 | `D07_graphs/075_graph_coloring/` |
| 76 | 平面グラフとオイラーの公式 | `D07_graphs/076_planar_euler/` |
| 77 | ダイクストラ法（最短路問題） | `D08_shortest_paths/077_dijkstra/` |
| 78 | ベルマン・フォード法 | `D08_shortest_paths/078_bellman_ford/` |
| 79 | フロイド・ワーシャル法 | `D08_shortest_paths/079_floyd_warshall/` |
| 80 | ジョンソンのアルゴリズム | `D08_shortest_paths/080_johnson/` |
| 81 | 0-1 BFS | `D08_shortest_paths/081_zero_one_bfs/` |
| 82 | プリム法（最小全域木） | `D08_shortest_paths/082_prim/` |
| 83 | クラスカル法（最小全域木） | `D08_shortest_paths/083_kruskal/` |
| 84 | ボルフカ法（最小全域木） | `D08_shortest_paths/084_boruvka/` |
| 85 | 最小全域木の応用問題 | `D08_shortest_paths/085_mst_applications/` |
| 86 | 負辺のある最短路問題 | `D08_shortest_paths/086_negative_edges/` |
| 87 | k番目の最短路 | `D08_shortest_paths/087_kth_shortest/` |
| 88 | 最短路問題の総合演習 | `D08_shortest_paths/088_shortest_path_comprehensive/` |
| 89 | 強連結成分分解（Tarjanのアルゴリズム） | `D09_advanced_graphs/089_tarjan_scc/` |
| 90 | 強連結成分分解（Kosarajuのアルゴリズム） | `D09_advanced_graphs/090_kosaraju/` |
| 91 | 木の直径 | `D09_advanced_graphs/091_tree_diameter/` |
| 92 | LCA（最小共通祖先） | `D09_advanced_graphs/092_lca/` |
| 93 | オイラーツアーテクニック | `D09_advanced_graphs/093_euler_tour/` |
| 94 | 最大流問題とフォード・ファルカーソン法 | `D09_advanced_graphs/094_ford_fulkerson/` |
| 95 | エドモンズ・カープ法 | `D09_advanced_graphs/095_edmonds_karp/` |
| 96 | 最小カット問題 | `D09_advanced_graphs/096_min_cut/` |
| 97 | 二部マッチング | `D09_advanced_graphs/097_bipartite_matching/` |
| 98 | ホップクロフト・カープ法 | `D09_advanced_graphs/098_hopcroft_karp/` |
| 99 | 一般グラフの最大マッチング入門 | `D09_advanced_graphs/099_general_matching/` |
| 100 | 最小費用流問題 | `D09_advanced_graphs/100_min_cost_flow/` |
| 101 | 動的計画法の基本的な考え方 | `D10_dp/101_dp_intro/` |
| 102 | フィボナッチ数列と記憶化 | `D10_dp/102_fibonacci_memo/` |
| 103 | ナップサック問題（0-1） | `D10_dp/103_knapsack_01/` |
| 104 | ナップサック問題（個数無制限） | `D10_dp/104_knapsack_unbounded/` |
| 105 | 最長共通部分列（LCS） | `D10_dp/105_lcs/` |
| 106 | 最長増加部分列（LIS） | `D10_dp/106_lis/` |
| 107 | 編集距離 | `D10_dp/107_edit_distance/` |
| 108 | 区間DP | `D10_dp/108_interval_dp/` |
| 109 | 木DP | `D10_dp/109_tree_dp/` |
| 110 | ビットDP | `D10_dp/110_bit_dp/` |
| 111 | 桁DP | `D10_dp/111_digit_dp/` |
| 112 | 巡回セールスマン問題とDP | `D10_dp/112_tsp_dp/` |
| 113 | 期待値DP | `D10_dp/113_expected_dp/` |
| 114 | 動的計画法の総合演習 | `D10_dp/114_dp_comprehensive/` |
| 115 | 貪欲法の考え方 | `D11_greedy/115_greedy/` |
| 116 | 区間スケジューリング問題 | `D11_greedy/116_interval_scheduling/` |
| 117 | ハフマン符号 | `D11_greedy/117_huffman/` |
| 118 | バックトラッキング法 | `D11_greedy/118_backtracking/` |
| 119 | 分枝限定法 | `D11_greedy/119_branch_and_bound/` |
| 120 | 局所探索法 | `D11_greedy/120_local_search/` |
| 121 | 焼きなまし法の直感 | `D11_greedy/121_simulated_annealing/` |
| 122 | 答えで二分探索する最適化テクニック | `D11_greedy/122_binary_search_on_answer/` |
| 123 | 平衡二分探索木を用いた設計例 | `D11_greedy/123_balanced_bst_design/` |
| 124 | 貪欲法とDPの使い分け | `D11_greedy/124_greedy_vs_dp/` |
| 125 | 文字列マッチングの基礎（力任せ法） | `D12_strings/125_naive_string_match/` |
| 126 | KMP法 | `D12_strings/126_kmp/` |
| 127 | ラビン・カープ法 | `D12_strings/127_rabin_karp/` |
| 128 | Zアルゴリズム | `D12_strings/128_z_algorithm/` |
| 129 | 接尾辞配列の基礎 | `D12_strings/129_suffix_array/` |
| 130 | 接尾辞配列の構築（SA-IS等の直感） | `D12_strings/130_sa_is/` |
| 131 | LCP配列 | `D12_strings/131_lcp_array/` |
| 132 | 接尾辞木の基礎 | `D12_strings/132_suffix_tree/` |
| 133 | Aho-Corasick法（複数パターン照合） | `D12_strings/133_aho_corasick/` |
| 134 | マナカーのアルゴリズム（最長回文） | `D12_strings/134_manacher/` |
| 135 | ローリングハッシュの応用 | `D12_strings/135_rolling_hash/` |
| 136 | 文字列アルゴリズムの総合演習 | `D12_strings/136_strings_comprehensive/` |
| 137 | エラトステネスの篩 | `D13_number_theory/137_sieve_of_eratosthenes/` |
| 138 | セグメント篩 | `D13_number_theory/138_segmented_sieve/` |
| 139 | 拡張ユークリッドの互除法 | `D13_number_theory/139_extended_euclidean/` |
| 140 | モジュラー逆元 | `D13_number_theory/140_modular_inverse/` |
| 141 | 高速な冪乗剰余計算 | `D13_number_theory/141_modular_exponentiation/` |
| 142 | 素数判定（フェルマーテスト・ミラー–ラビン法） | `D13_number_theory/142_primality_tests/` |
| 143 | 中国剰余定理のアルゴリズム的実装 | `D13_number_theory/143_crt_algorithm/` |
| 144 | 離散対数問題の入門 | `D13_number_theory/144_discrete_log/` |
| 145 | RSA暗号の仕組みの基礎 | `D13_number_theory/145_rsa_basics/` |
| 146 | 数論変換（NTT）の直感 | `D13_number_theory/146_ntt/` |
| 147 | 点と線分の位置関係 | `D14_computational_geometry/147_point_segment/` |
| 148 | 凸包（Convex Hull）アルゴリズム | `D14_computational_geometry/148_convex_hull/` |
| 149 | 線分交差判定 | `D14_computational_geometry/149_segment_intersection/` |
| 150 | 多角形の面積計算 | `D14_computational_geometry/150_polygon_area/` |
| 151 | 走査線アルゴリズムの考え方 | `D14_computational_geometry/151_sweep_line/` |
| 152 | 最近点対問題（幾何的アプローチ） | `D14_computational_geometry/152_closest_pair_geom/` |
| 153 | ボロノイ図の基礎 | `D14_computational_geometry/153_voronoi/` |
| 154 | ドロネー三角形分割の基礎 | `D14_computational_geometry/154_delaunay/` |
| 155 | 半平面交差 | `D14_computational_geometry/155_halfplane_intersection/` |
| 156 | 計算幾何学の総合演習 | `D14_computational_geometry/156_geom_comprehensive/` |
| 157 | 決定問題とクラスP | `D15_complexity_theory/157_decision_problems_p/` |
| 158 | クラスNPと検証可能性 | `D15_complexity_theory/158_class_np/` |
| 159 | NP完全性の定義 | `D15_complexity_theory/159_np_completeness/` |
| 160 | 帰着（リダクション）の考え方 | `D15_complexity_theory/160_reductions/` |
| 161 | SAT問題とクックの定理 | `D15_complexity_theory/161_sat_cook/` |
| 162 | 巡回セールスマン問題のNP完全性 | `D15_complexity_theory/162_tsp_np_complete/` |
| 163 | 頂点被覆問題・独立集合問題 | `D15_complexity_theory/163_vertex_cover_independent/` |
| 164 | 近似アルゴリズムの考え方 | `D15_complexity_theory/164_approximation/` |
| 165 | PTAS（多項式時間近似スキーム）の直感 | `D15_complexity_theory/165_ptas/` |
| 166 | 計算複雑性クラスの階層（PSPACE等） | `D15_complexity_theory/166_complexity_hierarchy/` |
| 167 | 乱択アルゴリズムの考え方 | `D16_randomized/167_randomized_algo/` |
| 168 | モンテカルロ法とラスベガス法 | `D16_randomized/168_monte_carlo_las_vegas/` |
| 169 | 乱択クイックソートの解析 | `D16_randomized/169_randomized_quicksort/` |
| 170 | スキップリストの確率的解析 | `D16_randomized/170_skip_list_analysis/` |
| 171 | ハッシュ法における確率的解析 | `D16_randomized/171_hashing_analysis/` |
| 172 | ブルームフィルタ | `D16_randomized/172_bloom_filter/` |
| 173 | オンラインアルゴリズムと競合比の考え方 | `D16_randomized/173_competitive_ratio/` |
| 174 | ランダム化アルゴリズムの総合演習 | `D16_randomized/174_randomized_comprehensive/` |
| 175 | 並列計算モデルの基礎 | `D17_parallel/175_parallel_models/` |
| 176 | 並列ソートアルゴリズム | `D17_parallel/176_parallel_sort/` |
| 177 | 分散アルゴリズムの基礎（リーダー選出） | `D17_parallel/177_leader_election/` |
| 178 | MapReduceの考え方 | `D17_parallel/178_mapreduce/` |
| 179 | 並列プレフィックス和 | `D17_parallel/179_parallel_prefix/` |
| 180 | キャッシュ効率とアルゴリズム設計 | `D17_parallel/180_cache_efficient/` |
| 181 | SIMDとアルゴリズムの高速化 | `D17_parallel/181_simd/` |
| 182 | 並列アルゴリズムの総合演習 | `D17_parallel/182_parallel_comprehensive/` |
| 183 | k-means法（クラスタリング） | `D18_ml_algorithms/183_kmeans/` |
| 184 | k近傍法（k-NN） | `D18_ml_algorithms/184_knn/` |
| 185 | 決定木アルゴリズムの基礎 | `D18_ml_algorithms/185_decision_trees/` |
| 186 | 勾配降下法の基礎 | `D18_ml_algorithms/186_gradient_descent/` |
| 187 | 線形回帰の最適化アルゴリズム | `D18_ml_algorithms/187_linear_regression_opt/` |
| 188 | 主成分分析（PCA）の計算アルゴリズム | `D18_ml_algorithms/188_pca/` |
| 189 | ページランクアルゴリズム | `D18_ml_algorithms/189_pagerank/` |
| 190 | レコメンデーションアルゴリズムの基礎 | `D18_ml_algorithms/190_recommendation/` |
| 191 | A/Bテストと多腕バンディット問題 | `D18_ml_algorithms/191_multiarmed_bandit/` |
| 192 | ニューラルネットワークの誤差逆伝播法の基礎 | `D18_ml_algorithms/192_backpropagation/` |
| 193 | 競売アルゴリズムの基礎 | `D19_game_theory/193_auction_algo/` |
| 194 | ゲーム木探索（ミニマックス法） | `D19_game_theory/194_minimax/` |
| 195 | アルファベータ枝刈り | `D19_game_theory/195_alpha_beta/` |
| 196 | ナッシュ均衡と計算アルゴリズムの基礎 | `D19_game_theory/196_nash_equilibrium/` |
| 197 | アルゴリズム設計技法の比較まとめ | `D20_wrap_up/197_design_techniques_review/` |
| 198 | 計算量のチートシート的総復習 | `D20_wrap_up/198_complexity_cheatsheet/` |
| 199 | 競技プログラミングにおけるアルゴリズム選択の指針 | `D20_wrap_up/199_competitive_programming_choice/` |
| 200 | P対NP問題と今後のアルゴリズム研究の展望 | `D20_wrap_up/200_p_vs_np_outlook/` |
