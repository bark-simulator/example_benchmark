py_test(
    name = "run_benchmark",
    srcs = ["run_benchmark.py"],
    data = [
        "//src/database:database",
        "//src/mcts_config/params:mcts_params",
        "//src/viewer_config/params:viewer_params",
        "@bark_project//bark/python_wrapper:core.so",
    ],
    imports = ["../python/"],
    deps = [
        "//src/mcts_config",
        "//src/traffic_rules:traffic_rules",
        "@bark_project//bark/benchmark:benchmark_runner",
        "@bark_project//bark/benchmark:benchmark_runner_mp",
        "@bark_project//bark/benchmark:benchmark_analyzer",
        "@bark_project//bark/runtime/scenario/scenario_generation:scenario_generation",
        "@benchmark_database//load:benchmark_database",
        "@benchmark_database//serialization:database_serializer",
    ],
)

py_test(
  name = "scenario_tuning",
  srcs = ["scenario_tuning.py"],
  data = ["@bark_project//bark:generate_core",
          "//src/database:database",
          "//src/mcts_config/params:mcts_params",
          "//src/viewer_config/params:viewer_params",
          ],
  imports = ['../python/'],
  deps = ["//src/traffic_rules:traffic_rules",
          "@bark_project//bark/benchmark:benchmark_runner",
          "@bark_project//bark/benchmark:benchmark_runner_mp",
          "@bark_project//bark/benchmark:benchmark_analyzer",
          "@bark_project//bark/runtime/scenario/scenario_generation:scenario_generation",
          "@benchmark_database//load:benchmark_database",
          "@benchmark_database//serialization:database_serializer",
          ],
)

py_test(
  name = "merging_test_specific",
  srcs = ["merging_test_specific.py"],
  data = [
          '@bark_project//bark:generate_core',
          "//src/mcts_config/params:mcts_params",
          "//src/viewer_config/params:viewer_params",
          "//src/database:database"],
  imports = ['../python/'],
  deps = ["@bark_project//bark/runtime/commons:parameters",
          "@bark_project//bark/runtime/commons:xodr_parser",
          "@bark_project//bark/runtime/viewer:matplotlib_viewer",
          "@bark_project//bark/runtime/scenario/scenario_generation:scenario_generation",
          "@bark_project//bark/runtime:runtime",
          "//src/mcts_config",
          "//src/common:custom_lane_corridor_config"],
)

py_test(
  name = "merging_test_random",
  srcs = ["merging_test_random.py"],
  data = [
          '@bark_project//bark:generate_core',
          "//src/mcts_config/params:mcts_params",
          "//src/viewer_config/params:viewer_params",
          "//src/database:database"],
  imports = ['../python/'],
  deps = ["@bark_project//bark/runtime/commons:parameters",
          "@bark_project//bark/runtime/commons:xodr_parser",
          "@bark_project//bark/runtime/viewer:matplotlib_viewer",
          "@bark_project//bark/runtime/scenario/scenario_generation:scenario_generation",
          "@bark_project//bark/runtime:runtime",
          "//src/mcts_config",
          "//src/common:custom_lane_corridor_config"],
)
