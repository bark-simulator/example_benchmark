# Copyright (c) 2021 fortiss GmbH
#
# Authors: Julian Bernhard, Klemens Esterle, Patrick Hart and
# Tobias Kessler
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.

import logging
import sys
from bark.core.ltl import RuleMonitor
from bark.core.world.evaluation.ltl import *


def make_rule_monitors(rule_params):
    rules = []
    for rule_param_srv in rule_params:
        rules.append(RuleMonitor(rule_param_srv["formula", "Traffic rules described using LTL"],
                                 rule_param_srv["weight",
                                                "Penalty for violating the rule.", 0.0],
                                 rule_param_srv[
            "priority", "Index of the entry in the reward vector to add penalty.", 0]))

    return rules


def dump_rules(rules):
    rule_str = ""
    for agent in rules.keys():
        rule_str = rule_str + "Agent ID: {}".format(agent)
        for rule in rules[agent]:
            rule_str = rule_str + "\n{}".format(str(rule))
        rule_str = rule_str + "\n\n"
    return rule_str


def make_SafeDistanceLabelFunction(params):
    label_str = params["label_str"]
    to_rear = params["to_rear"]
    delta_ego = params["delta_ego"]
    delta_others = params["delta_others"]
    a_e = params["a_e"]
    a_o = params["a_o"]
    consider_crossing_corridors = params["consider_crossing_corridors"]
    max_agents_for_crossing = params["max_agents_for_crossing"]
    use_frac_param_from_world = params["use_frac_param_from_world"]
    lateral_difference_threshold = params["lateral_difference_threshold"]
    check_lateral_dist = params["check_lateral_dist"]
    return SafeDistanceLabelFunction(label_str, to_rear, delta_ego, delta_others, a_e, a_o, consider_crossing_corridors, max_agents_for_crossing, use_frac_param_from_world, lateral_difference_threshold, check_lateral_dist)

def make_CollisionEgoLabelFunction(params):
    label_str = params["label_str"]
    return CollisionEgoLabelFunction(label_str)

def _make_default_label(evaluator_name, params):
    label_str = params["label_str"]
    return eval("{}(label_str)".format(evaluator_name))


def make_labels(label_params):
    labels = []
    for label in label_params:
        try:
            labels.append(eval("make_{}(label)".format(label["type"])))
        except Exception as e:
            logging.error("Error during label creation: {}".format(e))
            try:
                labels.append(_make_default_label(label["type"], label))
            except Exception as e:
                logging.error("Error during label creation: {}".format(e))
                sys.exit(1)
    return labels
