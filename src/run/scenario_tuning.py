# Copyright (c) 2021 fortiss GmbH
#
# Authors: Julian Bernhard, Klemens Esterle, Patrick Hart and
# Tobias Kessler
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.

import os
import pandas as pd
import logging
import sys

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

from bark.runtime.viewer.video_renderer import VideoRenderer
from bark.runtime.viewer.matplotlib_viewer import MPViewer
from bark.benchmark.benchmark_runner import BenchmarkResult, BenchmarkRunner
from bark.benchmark.benchmark_runner_mp import BenchmarkRunnerMP
from bark.runtime.commons.parameters import ParameterServer
from bark.core.commons import SetVerboseLevel
from bark.core.world.evaluation.ltl import *
from bark.core.models.behavior import BehaviorMobilRuleBased
from bark.benchmark.benchmark_analyzer import BenchmarkAnalyzer

from load.benchmark_database import BenchmarkDatabase
from serialization.database_serializer import DatabaseSerializer

from src.traffic_rules.traffic_rules_evaluators import *

# reduced max steps and scenarios for testing
max_steps = 160
test_steps = int(max_steps * 0.5 / 0.2)
test_scenarios = 0  # 2
num_scenarios = 5

try:
    params = ParameterServer(
        filename="src/viewer_config/params/mp_viewer_params.json", log_if_default=True)
except:
    logging.warning("Cannot find viewer params")

logging.info("Current Working Directory: {}".format(os.getcwd()))

if not os.path.exists("src/database"):
    print("changing directory")
    os.chdir("run_benchmark.runfiles/example_benchmark")

dbs = DatabaseSerializer(test_scenarios=test_scenarios,
                         test_world_steps=test_steps,
                         num_serialize_scenarios=num_scenarios)
dbs.process("src/database", filter_sets="**/*.json")
local_release_filename = dbs.release(version="2021_07_01")

# reload
db = BenchmarkDatabase(database_root=local_release_filename)

use_frac_param_from_world = False

evaluators = {"collision": "EvaluatorCollisionEgoAgent",
              "steps": "EvaluatorStepCount",
              "out_of_map": "EvaluatorDrivableArea",
              "safe_distance": get_traffic_rule_evaluator_params("safe_distance"),
              "goal_reached": "EvaluatorGoalReached",
              }
terminal_when = {"collision": lambda x: x,
                 "steps": lambda x: x > max_steps,
                 "goal_reached": lambda x: x,
                 "out_of_map": lambda x: x}

paramserver_mobil = ParameterServer(
    filename="src/mcts_config/params/mobil.json", log_if_default=True)
behaviors_tested = {"Mobil": BehaviorMobilRuleBased(paramserver_mobil)}

benchmark_runner = BenchmarkRunner(benchmark_database=db,
                                   evaluators=evaluators,
                                   terminal_when=terminal_when,
                                   behaviors=behaviors_tested,
                                   num_scenarios=num_scenarios,
                                   log_eval_avg_every=1)

viewer = MPViewer(params=params)
result = benchmark_runner.run(viewer, maintain_history=True)
