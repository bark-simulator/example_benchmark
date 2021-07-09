py_library(
    name = "mcts_config",
    srcs = ["mcts_config.py"],
    data = [
        "@bark_project//bark/python_wrapper:core.so",
    ],
    imports = ["../python/"],
    visibility = ["//visibility:public"],
    deps = [
        ":mcts_behavior_config_reader",
        "@bark_project//bark/runtime",
        "@bark_project//bark/runtime/scenario/scenario_generation",
    ],
)

py_library(
    name = "mcts_behavior_config_reader",
    srcs = [
        "mcts_behavior_config_reader.py",
    ],
    data = [
        "@bark_project//bark/python_wrapper:core.so",
    ],
    imports = ["../python/"],
    visibility = ["//visibility:public"],
    deps = [
        "@bark_project//bark/runtime",
        "@bark_project//bark/runtime/scenario/scenario_generation",
        "//src/traffic_rules:traffic_rules"
    ],
)

py_test(
    name = "mcts_config_test",
    srcs = ["mcts_config_test.py"],
    data = [
        "//src/database:database",
        "//src/mcts_config/params:mcts_params",
        "@bark_project//bark/python_wrapper:core.so",
    ],
    imports = ["../python/"],
    deps = [
        ":mcts_config",
        "@bark_project//bark/runtime",
        "@bark_project//bark/runtime/scenario/scenario_generation",
        "@bark_project//bark/runtime/scenario/scenario_generation/config_readers",
    ],
)
