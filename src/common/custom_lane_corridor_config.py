# Copyright (c) 2021 fortiss GmbH
#
# Authors: Julian Bernhard, Klemens Esterle, Patrick Hart and
# Tobias Kessler
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.

import logging

from bark.core.world.opendrive import XodrDrivingDirection
from bark.core.world.goal_definition import GoalDefinitionPolygon
from bark.runtime.scenario.scenario_generation.config_with_ease import LaneCorridorConfig
from bark.core.geometry import *


class CustomLaneCorridorConfig(LaneCorridorConfig):
    def __init__(self,
                 params=None,
                 **kwargs):
        super(CustomLaneCorridorConfig, self).__init__(params, **kwargs)

    def goal(self, world):
        # settings are valid for merging map
        road_corr = world.map.GetRoadCorridor(
            self._road_ids, XodrDrivingDirection.forward)
        lane_corr = self._road_corridor.lane_corridors[0]
        goal_polygon = Polygon2d([0, 0, 0], [
                                 Point2d(-10, -10), Point2d(-10, 10), Point2d(10, 10), Point2d(10, -10)])
        goal_point = GetPointAtS(
            lane_corr.center_line, lane_corr.center_line.Length()*0.45)
        goal_polygon = goal_polygon.Translate(goal_point)
        return GoalDefinitionPolygon(goal_polygon)


class DeterministicLaneCorridorConfig(CustomLaneCorridorConfig):
    def __init__(self,
                 params=None,
                 **kwargs):
        super(DeterministicLaneCorridorConfig, self).__init__(params, **kwargs)
        self._s_start = kwargs.pop("s_start", [30])
        self._vel_start = kwargs.pop("vel_start", [10])
        if not isinstance(self._s_start, list):
            raise ValueError("start types must be of type list.")

    def position(self, world):
        """
        returns position based on start 
        """
        if self._road_corridor == None:
            world.map.GenerateRoadCorridor(
                self._road_ids, XodrDrivingDirection.forward)
            self._road_corridor = world.map.GetRoadCorridor(
                self._road_ids, XodrDrivingDirection.forward)
        if self._road_corridor is None:
            return None
        if self._lane_corridor is not None:
            lane_corr = self._lane_corridor
        else:
            lane_corr = self._road_corridor.lane_corridors[self._lane_corridor_id]
        if lane_corr is None:
            return None
        centerline = lane_corr.center_line

        if len(self._s_start) == 0:
            logging.info(
                "no more agents to spawn. If this message is created more than one \
                    time, then the scenario has been tried to be created more than \
                        once -> ERROR")
            return None

        self._current_s = self._s_start.pop(0)
        xy_point = GetPointAtS(centerline, self._current_s)
        angle = GetTangentAngleAtS(centerline, self._current_s)

        logging.info("Creating agent at x={}, y={}, theta={}".format(
            xy_point.x(), xy_point.y(), angle))
        return (xy_point.x(), xy_point.y(), angle)

    def velocity(self):
        return self._vel_start
