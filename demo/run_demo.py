from time import sleep
import numpy as np

from demo.generate_optimal_track import generateOptimalTrack
from demo.visualization.view import View

view = View()

car,cones = generateOptimalTrack()
view.updateCones(orange_small_cones=cones[0], orange_big_cones=cones[1], yellow_cones=cones[2], blue_cones=cones[3])
view.updateCar(car[0],car[1])

sleep(5)