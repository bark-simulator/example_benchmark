# Copyright (c) 2021 fortiss GmbH
#
# Authors: Julian Bernhard, Klemens Esterle, Patrick Hart and
# Tobias Kessler
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.

import time
import logging

from bark.runtime.commons.parameters import ParameterServer
from bark.runtime.viewer.matplotlib_viewer import MPViewer
from bark.runtime.viewer.video_renderer import VideoRenderer
from bark.runtime.scenario.scenario_generation.config_with_ease import \
    ConfigWithEase
from bark.core.models.behavior import *
from bark.runtime.runtime import Runtime

from src.mcts_config.mcts_config import create_mcts_configurations
from src.common.custom_lane_corridor_config import DeterministicLaneCorridorConfig


# SetVerboseLevel(5)
logging.getLogger().setLevel(logging.INFO)

params = ParameterServer()

params_mobil = ParameterServer(
    filename="src/mcts_config/params/mobil.json", log_if_default=True)

behaviors_tested, params_dict = create_mcts_configurations(
    "src/mcts_config/params/", [50], ['sa_mcts'])

# configure both lanes of the highway. the right lane has one controlled agent
left_lane = DeterministicLaneCorridorConfig(params=params,
                                            lane_corridor_id=0,
                                            road_ids=[0, 1],
                                            behavior_model=BehaviorMobilRuleBased(
                                                params_mobil),
                                            s_start=[15, 35],
                                            vel_start=10)
right_lane = DeterministicLaneCorridorConfig(params=params,
                                             lane_corridor_id=1,
                                             road_ids=[0, 1],
                                             controlled_ids=True,
                                             behavior_model=behaviors_tested["sa_mcts_50"],
                                             s_start=[15],
                                             vel_start=12)

map_path = "src/database/maps/merging_long_v01.xodr"

scenarios = \
    ConfigWithEase(num_scenarios=1,
                   map_file_name=map_path,
                   random_seed=0,
                   params=params,
                   lane_corridor_configs=[left_lane, right_lane])

# viewer
params_viewer = ParameterServer(
    filename="src/viewer_config/params/mp_viewer_params.json", log_if_default=True)
viewer = MPViewer(params=params_viewer)

sim_step_time = params["simulation"]["step_time",
                                     "Step-time used in simulation",
                                     0.25]
sim_real_time_factor = params["simulation"]["real_time_factor",
                                            "execution in real-time or faster",
                                            1.]

video_renderer = VideoRenderer(renderer=viewer,
                               world_step_time=sim_step_time,
                               fig_path="/tmp/video")

env = Runtime(step_time=sim_step_time,
                    viewer=video_renderer,
                    scenario_generator=scenarios,
                    render=True)

n_steps = 4
env.reset()
# step scenario n_steps times
for step in range(0, n_steps):
    env.step()
    time.sleep(sim_step_time/sim_real_time_factor)

video_renderer.export_video(filename="/tmp/video", remove_image_dir=False)
