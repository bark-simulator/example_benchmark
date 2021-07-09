# Copyright (c) 2021 fortiss GmbH
#
# Authors: Julian Bernhard, Klemens Esterle, Patrick Hart and
# Tobias Kessler
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.

import os

from bark.runtime.commons.parameters import ParameterServer
from src.mcts_config.mcts_behavior_config_reader import \
    mcts_behavior_from_config


def dump_mcts_default_params(dir):
    params = ParameterServer()
    sa_mcts_behavior = mcts_behavior_from_config(params)

    params.Save(filename=os.path.join(dir, "sa_mcts.json"))
    params.Save(filename=os.path.join(dir, "sa_mcts_default_description.json"),
                print_description=True)


def create_mcts_configurations(param_directory, iterations, variants=None):
    common_params_fname = 'common.json'
    params_dict = {}
    configuration_dict = {}
    for root, dirs, files in os.walk(param_directory):
        for file in files:
            base = os.path.basename(file)
            (configuration_name, ext) = os.path.splitext(base)
            if ext == '.json' and base != common_params_fname:
                print(configuration_name)
                if ((variants is None) or (configuration_name in variants)):
                    for it in iterations:
                        full_config_name = "{}_{}".format(
                            configuration_name, it)
                        params = ParameterServer(filename=os.path.join(
                            root, file), log_if_default=True)
                        action_set_params = ParameterServer(filename=os.path.join(param_directory, common_params_fname),
                                                            log_if_default=True)
                        params.AppendParamServer(action_set_params)
                        behavior = mcts_behavior_from_config(
                            params, iterations=(it))
                        configuration_dict[full_config_name] = behavior
                        params_dict[full_config_name] = params
    return configuration_dict, params_dict
