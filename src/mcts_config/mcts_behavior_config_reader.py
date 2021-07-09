# Copyright (c) 2021 fortiss GmbH
#
# Authors: Julian Bernhard, Klemens Esterle, Patrick Hart and
# Tobias Kessler
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.

from bark.core.models.behavior import *
from src.traffic_rules.rule_generation import make_rule_monitors, make_labels
from bark.core.world.prediction import PredictionSettings
from bark.core.models.dynamic import SingleTrackModel
from bark.runtime.commons.parameters import ParameterServer
from bark.runtime.commons import ModelJsonConversion

prim_param_server = []


def mcts_behavior_from_config(param_server, ego_id=None, iterations=None):
    if iterations:
        param_server["BehaviorRulesMcts"]["MaxNumIterations"] = iterations

    # LABELS
    label_params = param_server["BehaviorRulesMcts"]["Labels",
                                                     "Definition of labels, required for the rules", []]
    # The collision label is always required for terminal state assessment!
    label_params.append(
        {"type": "CollisionEgoLabelFunction", "label_str": "collision_ego"})
    labels = make_labels(label_params)

    # RULES
    rules = make_rule_monitors(
        param_server["BehaviorRulesMcts"]["Rules"]["common", "Rules valid for all agents incl. ego", []])

    # DYNAMIC MODEL
    dynamic_model = SingleTrackModel(param_server)

    # PREDICTION SETTING
    prediction_settings = prediction_settings_from_config(
        param_server["BehaviorRulesMcts"], dynamic_model)

    behavior = BehaviorRulesMctsUct(
        param_server, prediction_settings, labels, rules, {})
    return behavior


def prediction_settings_from_config(param_server, dynamic_model):
    model_converter = ModelJsonConversion()
    # EGO BEHAVIOR MODEL
    ego_model = mp_macro_actions_from_config(
        param_server["PredictionSettings"]["EgoModelParams"])

    # OTHER AGENTS MODEL
    default_behavior_name = param_server["PredictionSettings"]["DefaultModelName",
                                                               "", "BehaviorMobilRuleBased"]
    default_behavior_params = param_server["PredictionSettings"]["DefaultModelParams"]
    if isinstance(default_behavior_params, dict):
        default_behavior_params = ParameterServer(
            log_if_default=True, json=default_behavior_params)
        param_server["PredictionSettings"]["DefaultModel"] = default_behavior_params
    if default_behavior_name == "None":
        default_model = None
    else:
        try:
            default_model = model_converter.convert_model(
                default_behavior_name, default_behavior_params)
        except:
            raise ValueError("Could not retrieve default_model")
    prediction_settings = PredictionSettings(
        ego_model, default_model, None, [])
    return prediction_settings


def mp_macro_actions_from_config(param_server):
    primitives = primitives_from_config(
        param_server["BehaviorMPMacroActions"]["Primitives"])
    model = BehaviorMPMacroActions(param_server, primitives)
    return model


def primitives_from_config(primitives):
    prim = []
    for param_prim_object in primitives:
        prim_dict = param_prim_object.ConvertToDict()
        prim_params = list(prim_dict.items())[0]
        prim_type = prim_params[0]
        param_server = ParameterServer(
            json=prim_params[1], log_if_default=True)
        prim_param_server.append(param_server)
        prim_dict[prim_type] = param_server
        prim.append(eval("{}(param_server)".format(prim_type)))
    return prim
