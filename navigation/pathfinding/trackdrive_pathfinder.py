from navigation.pathfinding.pathfinder import Pathfinder


class TrackdrivePathfinder(Pathfinder):
    def generatePath(self, car_position, car_direction, cones, points = 10):
        raise NotImplementedError