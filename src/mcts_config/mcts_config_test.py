# Copyright (c) 2021 fortiss GmbH
#
# Authors: Julian Bernhard, Klemens Esterle, Patrick Hart and
# Tobias Kessler
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.

import unittest
import pickle

from src.mcts_config.mcts_config import dump_mcts_default_params, \
    create_mcts_configurations
from src.traffic_rules.rule_generation import make_rule_monitors


def pickle_unpickle(object):
    d = pickle.dumps(object)
    return pickle.loads(d)


class MctsConfigTests(unittest.TestCase):
    def test_dump_defaults(self):
        dump_mcts_default_params("/tmp/")

    def test_create_config_dict(self):
        config_dict, params = create_mcts_configurations(
            "src/mcts_config/params/", [200])
        for config_name, behavior in config_dict.items():
            print(config_name, behavior)
            unpickled = pickle_unpickle(behavior)
            print(unpickled)
            print("##############")

    def test_rules(self):
        it = 200
        config_dict, params = create_mcts_configurations(
            "src/mcts_config/params/", [it])
        variant_name = list(config_dict.keys())[0]
        print(params[variant_name]["BehaviorRulesMcts"]["Rules"]["common"])
        rules = make_rule_monitors(params[variant_name]
                                   ["BehaviorRulesMcts"]["Rules"]["common"])


if __name__ == '__main__':
    unittest.main()
