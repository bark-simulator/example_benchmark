load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive", "http_file")

def example_benchmark_dependencies():
    _maybe(
        git_repository,
        name = "rule_monitor_project",
        commit = "187c125a18979214d638ca771dd86e7934932b94",
        remote = "https://github.com/bark-simulator/rule-monitoring.git",
    )

    _maybe(
        git_repository,
        name = "planner_rules_mcts",
        commit = "35b09a857d8c3f1c65e0ed80ee4df1b358e45bf4",
        remote = "https://github.com/bark-simulator/planner-rules-mcts.git",
    )

    _maybe(
        git_repository,
        name = "bark_project",
        commit = "4e33a66ec5dc6a936a71cad1bc0db1807a9b7cb6",
        remote = "https://github.com/bark-simulator/bark.git",
    )

def _maybe(repo_rule, name, **kwargs):
    if name not in native.existing_rules():
        repo_rule(name = name, **kwargs)
