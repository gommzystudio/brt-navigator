import unittest

from demo.generate_optimal_track import generateOptimalTrack
from demo.visualization.plot import Plot
from navigation.conesorting.conesorter import Conesorter


class ConesorterTest(unittest.TestCase):
    def testSorting(self):
        car, cones = generateOptimalTrack()
        Plot(car[0], car[1], yellow_cones=cones[2], blue_cones=cones[3])

        groups = Conesorter().sortCones(cones[2], cones[3], [])
        groupcount = groups.__len__()

        self.assertEqual(4, groupcount) # Because a skidpad has 2 circles, there should be 4 groups of cones


if __name__ == '__main__':
    unittest.main()
