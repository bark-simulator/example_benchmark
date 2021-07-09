# Copyright (c) 2021 fortiss GmbH
#
# Authors: Julian Bernhard, Klemens Esterle, Patrick Hart and
# Tobias Kessler
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.

import logging

from bark.core.world.evaluation.ltl import *

NOT_AVAILABLE = "Not available, please contact Klemens Esterle: esterle@fortiss.org"


def get_traffic_rule_evaluator_params(rule_name):
    if rule_name == "safe_distance":
        rule = {"type": "EvaluatorLTL",
                "params": {"ltl_formula": "G sd_front",
                           "label_functions": [SafeDistanceLabelFunction("sd_front", False, 1.0, 1.0, -7.84, -7.84, True, 4, False, 2.0, False)]}}

    elif rule_name == "zip_merge":
        logging.raiseExceptions(NOT_AVAILABLE)

    elif rule_name == "right_overtake":
        logging.raiseExceptions(NOT_AVAILABLE)

    elif rule_name == "safe_lane_change":
        logging.raiseExceptions(NOT_AVAILABLE)

    elif rule_name == "safe_lane_change_assumption":
        logging.raiseExceptions(NOT_AVAILABLE)

    elif rule_name == "being_overtaken":
        logging.raiseExceptions(NOT_AVAILABLE)

    elif rule_name == "being_overtaken_assumption":
        logging.raiseExceptions(NOT_AVAILABLE)

    elif rule_name == "speed_advantage_overtaking":
        logging.raiseExceptions(NOT_AVAILABLE)

    elif rule_name == "no_stopping":
        logging.raiseExceptions(NOT_AVAILABLE)

    elif rule_name == "no_stopping_assumption":
        logging.raiseExceptions(NOT_AVAILABLE)

    elif rule_name == "maximum_speed_limit":
        logging.raiseExceptions(NOT_AVAILABLE)

    elif rule_name == "inside_rightmost_lane":
        logging.raiseExceptions(NOT_AVAILABLE)

    elif rule_name == "inside_rightmost_lane_assumption":
        logging.raiseExceptions(NOT_AVAILABLE)
    else:
        logging.error("rule has not been defined")

    return rule


def get_traffic_rule_evaluator_bark(eval_agent_id, rule_name, location, use_frac_param_from_world):
    evaluator_params = get_traffic_rule_evaluator_params(
        rule_name, location, use_frac_param_from_world)
    evaluator_bark = eval(
        "{}(agent_id=eval_agent_id, **evaluator_params['params'])".format(evaluator_params["type"]))
    return evaluator_bark
