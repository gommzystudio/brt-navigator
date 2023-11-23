from typing import List

import numpy as np


class Conesorter:
    def sortCones(self, yellow_cones: np.ndarray, blue_cones: np.ndarray, unknown_cones: np.ndarray):
        """
        Sorts the cones into related groups.

        Args:
            yellow_cones (numpy.ndarray): Coordinates for yellow cones.
            blue_cones (numpy.ndarray): Coordinates for blue cones.
            unknown_cones (numpy.ndarray): Coordinates for unknown cones.

        Returns:
        """
        groups = []
        groups.append(yellow_cones)
        groups.append(blue_cones)
        groups.append(unknown_cones)
        return groups