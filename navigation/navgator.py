from typing import List

import numpy as np

from navigation.conesorting.conesorter import Conesorter
from navigation.pathfinding.pathfinder import Pathfinder


class Navigator:
    def __init__(self, conesorter: Conesorter, pathfinder: Pathfinder):
        """
        Creates a new Navigator

        :param conesorter: The conesorter to use
        :param pathfinder: The pathfinder to use
        """
        self.conesorter = conesorter
        self.pathfinder = pathfinder

    def step(self, car_position: np.ndarray, car_direction: np.ndarray, cones: List[np.ndarray]) -> np.ndarray:
        """
        Generates a new path from the given data

        :param car_position: The position of the car
        :param car_direction: The direction of the car
        :param cones: The cones

        :return: The new path as a list of points
        """
        cones = self.conesorter.sortCones(cones)
        return self.pathfinder.generatePath(car_position, car_direction, cones)
