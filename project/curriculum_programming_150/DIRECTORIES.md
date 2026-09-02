# プログラミング 自己完結 150本 ディレクトリ計画

ルート: `project/curriculum_programming_150/`

パス: `project/curriculum_programming_150/{番号3桁}_{スラッグ}/`

章フォルダは置かない（視聴順の章ではない）。正本は `ROADMAP.md`。

## 命名規則

- ディレクトリ名は **ASCII 小文字 + 数字 + アンダースコア** のみ。
- スラッグは英語の短い名詞句（32文字以内）。シリーズ内で重複しない。
- 本番号は ROADMAP の `#` と一致する **3桁ゼロ埋め**。
- 各本フォルダには、実装時に `storyboard.md` と `scene.py` を置く（この計画ではまだ作らない）。
- 各動画は **必ず先に `storyboard.md` を書き、そのあと `scene.py` を実装する。**

このファイルは計画表である。空ディレクトリの一括作成は次の作業とする。

## 本フォルダ（150）

| # | スラッグ | パス |
|---|---|---|
| 1 | find_duplicate | `001_find_duplicate/` |
| 2 | two_sum | `002_two_sum/` |
| 3 | undo_stack | `003_undo_stack/` |
| 4 | print_queue | `004_print_queue/` |
| 5 | brackets_match | `005_brackets_match/` |
| 6 | binary_search_directory | `006_binary_search_directory/` |
| 7 | binary_search_on_answer | `007_binary_search_on_answer/` |
| 8 | sorting_lower_bound | `008_sorting_lower_bound/` |
| 9 | quicksort_random | `009_quicksort_random/` |
| 10 | mergesort_stable | `010_mergesort_stable/` |
| 11 | fisher_yates | `011_fisher_yates/` |
| 12 | reservoir_sampling | `012_reservoir_sampling/` |
| 13 | lru_cache | `013_lru_cache/` |
| 14 | trie_autocomplete | `014_trie_autocomplete/` |
| 15 | edit_distance | `015_edit_distance/` |
| 16 | diff_lcs | `016_diff_lcs/` |
| 17 | huffman | `017_huffman/` |
| 18 | bloom_filter | `018_bloom_filter/` |
| 19 | maze_bfs | `019_maze_bfs/` |
| 20 | n_queens_backtrack | `020_n_queens_backtrack/` |
| 21 | dijkstra | `021_dijkstra/` |
| 22 | astar | `022_astar/` |
| 23 | mst_kruskal | `023_mst_kruskal/` |
| 24 | course_order_topo | `024_course_order_topo/` |
| 25 | bipartite_matching | `025_bipartite_matching/` |
| 26 | maxflow_mincut | `026_maxflow_mincut/` |
| 27 | pagerank | `027_pagerank/` |
| 28 | interval_scheduling | `028_interval_scheduling/` |
| 29 | coin_change_dp | `029_coin_change_dp/` |
| 30 | knapsack | `030_knapsack/` |
| 31 | kadane | `031_kadane/` |
| 32 | lis | `032_lis/` |
| 33 | string_search_hash | `033_string_search_hash/` |
| 34 | fast_pow | `034_fast_pow/` |
| 35 | karatsuba | `035_karatsuba/` |
| 36 | hash_collisions | `036_hash_collisions/` |
| 37 | array_vs_linked_list | `037_array_vs_linked_list/` |
| 38 | heap_priority | `038_heap_priority/` |
| 39 | prefix_sums | `039_prefix_sums/` |
| 40 | closest_pair | `040_closest_pair/` |
| 41 | convex_hull | `041_convex_hull/` |
| 42 | voronoi | `042_voronoi/` |
| 43 | kmeans | `043_kmeans/` |
| 44 | gradient_descent | `044_gradient_descent/` |
| 45 | halting_problem | `045_halting_problem/` |
| 46 | np_reduction | `046_np_reduction/` |
| 47 | consistent_hashing | `047_consistent_hashing/` |
| 48 | git_dag | `048_git_dag/` |
| 49 | minimax | `049_minimax/` |
| 50 | b_tree_index | `050_b_tree_index/` |
| 51 | bst_imbalance | `051_bst_imbalance/` |
| 52 | avl_rotations | `052_avl_rotations/` |
| 53 | segment_tree | `053_segment_tree/` |
| 54 | fenwick_tree | `054_fenwick_tree/` |
| 55 | union_find_path_compression | `055_union_find_path_compression/` |
| 56 | queue_from_two_stacks | `056_queue_from_two_stacks/` |
| 57 | min_stack | `057_min_stack/` |
| 58 | deque_ring_buffer | `058_deque_ring_buffer/` |
| 59 | running_median_two_heaps | `059_running_median_two_heaps/` |
| 60 | sparse_array_representation | `060_sparse_array_representation/` |
| 61 | rotated_binary_search | `061_rotated_binary_search/` |
| 62 | ternary_search_unimodal | `062_ternary_search_unimodal/` |
| 63 | quickselect | `063_quickselect/` |
| 64 | median_of_two_sorted_arrays | `064_median_of_two_sorted_arrays/` |
| 65 | max_product_subarray | `065_max_product_subarray/` |
| 66 | tree_diameter | `066_tree_diameter/` |
| 67 | tree_isomorphism | `067_tree_isomorphism/` |
| 68 | expression_tree_parsing | `068_expression_tree_parsing/` |
| 69 | iterative_dfs | `069_iterative_dfs/` |
| 70 | tail_recursion_stack_overflow | `070_tail_recursion_stack_overflow/` |
| 71 | bellman_ford | `071_bellman_ford/` |
| 72 | floyd_warshall | `072_floyd_warshall/` |
| 73 | negative_cycle_detection | `073_negative_cycle_detection/` |
| 74 | articulation_points_bridges | `074_articulation_points_bridges/` |
| 75 | strongly_connected_components | `075_strongly_connected_components/` |
| 76 | multi_source_bfs | `076_multi_source_bfs/` |
| 77 | bidirectional_search | `077_bidirectional_search/` |
| 78 | lowest_common_ancestor | `078_lowest_common_ancestor/` |
| 79 | bipartite_check_coloring | `079_bipartite_check_coloring/` |
| 80 | cycle_detection_topo | `080_cycle_detection_topo/` |
| 81 | interval_dp_matrix_chain | `081_interval_dp_matrix_chain/` |
| 82 | tree_dp | `082_tree_dp/` |
| 83 | bitmask_dp_tsp | `083_bitmask_dp_tsp/` |
| 84 | digit_dp | `084_digit_dp/` |
| 85 | expected_value_dp | `085_expected_value_dp/` |
| 86 | longest_common_substring | `086_longest_common_substring/` |
| 87 | palindrome_dp | `087_palindrome_dp/` |
| 88 | memoization_vs_dp | `088_memoization_vs_dp/` |
| 89 | tsp_dp_bitmask | `089_tsp_dp_bitmask/` |
| 90 | rolling_array_dp | `090_rolling_array_dp/` |
| 91 | greedy_counterexample_matroid | `091_greedy_counterexample_matroid/` |
| 92 | deadline_scheduling | `092_deadline_scheduling/` |
| 93 | gas_station_greedy | `093_gas_station_greedy/` |
| 94 | simulated_annealing | `094_simulated_annealing/` |
| 95 | binary_search_answer_advanced | `095_binary_search_answer_advanced/` |
| 96 | multi_resource_scheduling | `096_multi_resource_scheduling/` |
| 97 | bin_packing_approx | `097_bin_packing_approx/` |
| 98 | online_algorithm_competitive_ratio | `098_online_algorithm_competitive_ratio/` |
| 99 | lfu_vs_lru | `099_lfu_vs_lru/` |
| 100 | pareto_multi_objective | `100_pareto_multi_objective/` |
| 101 | aho_corasick | `101_aho_corasick/` |
| 102 | manacher_palindrome | `102_manacher_palindrome/` |
| 103 | string_hash_similarity | `103_string_hash_similarity/` |
| 104 | suffix_array_lcp | `104_suffix_array_lcp/` |
| 105 | sliding_window | `105_sliding_window/` |
| 106 | kmp_preprocessing | `106_kmp_preprocessing/` |
| 107 | fuzzy_search_edit_distance | `107_fuzzy_search_edit_distance/` |
| 108 | run_length_lz77 | `108_run_length_lz77/` |
| 109 | suffix_tree_frequent_substring | `109_suffix_tree_frequent_substring/` |
| 110 | edit_distance_path_reconstruction | `110_edit_distance_path_reconstruction/` |
| 111 | primality_testing_miller_rabin | `111_primality_testing_miller_rabin/` |
| 112 | diffie_hellman_intuition | `112_diffie_hellman_intuition/` |
| 113 | rsa_one_way_intuition | `113_rsa_one_way_intuition/` |
| 114 | randomized_algorithm_design | `114_randomized_algorithm_design/` |
| 115 | hyperloglog_intuition | `115_hyperloglog_intuition/` |
| 116 | streaming_approximation | `116_streaming_approximation/` |
| 117 | statistical_test_on_dice | `117_statistical_test_on_dice/` |
| 118 | monte_carlo_tree_search | `118_monte_carlo_tree_search/` |
| 119 | pseudo_random_number_period | `119_pseudo_random_number_period/` |
| 120 | secret_sharing_intuition | `120_secret_sharing_intuition/` |
| 121 | race_condition_locks | `121_race_condition_locks/` |
| 122 | deadlock | `122_deadlock/` |
| 123 | load_balancing_hashing | `123_load_balancing_hashing/` |
| 124 | replication_fault_tolerance | `124_replication_fault_tolerance/` |
| 125 | logical_clocks_ordering | `125_logical_clocks_ordering/` |
| 126 | cache_invalidation | `126_cache_invalidation/` |
| 127 | mapreduce_divide_conquer | `127_mapreduce_divide_conquer/` |
| 128 | message_ordering_async | `128_message_ordering_async/` |
| 129 | backpressure_overload | `129_backpressure_overload/` |
| 130 | idempotent_operations | `130_idempotent_operations/` |
| 131 | expression_parsing_precedence | `131_expression_parsing_precedence/` |
| 132 | lexer_error_detection | `132_lexer_error_detection/` |
| 133 | regex_finite_automaton | `133_regex_finite_automaton/` |
| 134 | automata_limits_cfg | `134_automata_limits_cfg/` |
| 135 | stack_machine_cfg | `135_stack_machine_cfg/` |
| 136 | closures_and_functions | `136_closures_and_functions/` |
| 137 | call_stack_recursion_compile | `137_call_stack_recursion_compile/` |
| 138 | garbage_collection_reachability | `138_garbage_collection_reachability/` |
| 139 | type_checking_intuition | `139_type_checking_intuition/` |
| 140 | deterministic_replay_debugging | `140_deterministic_replay_debugging/` |
| 141 | k_nearest_neighbors | `141_k_nearest_neighbors/` |
| 142 | random_forest_voting | `142_random_forest_voting/` |
| 143 | naive_bayes_spam | `143_naive_bayes_spam/` |
| 144 | collaborative_filtering | `144_collaborative_filtering/` |
| 145 | convolution_intuition | `145_convolution_intuition/` |
| 146 | backpropagation_intuition | `146_backpropagation_intuition/` |
| 147 | reinforcement_learning_intro | `147_reinforcement_learning_intro/` |
| 148 | shannon_limit_intuition | `148_shannon_limit_intuition/` |
| 149 | measuring_algorithms_beyond_time | `149_measuring_algorithms_beyond_time/` |
| 150 | greedy_vs_dp_when_to_choose | `150_greedy_vs_dp_when_to_choose/` |
