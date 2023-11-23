import matplotlib as matplotlib
from matplotlib import pyplot as plt

class Plot:
    """
    A graphical representation of a car's environment in a 2D space.

    This class uses Matplotlib to create a plot that can display the position and path of a car, as well as the location of various cones.
    """

    def __init__(self, car_position, car_direction, unknown_cones=None, blue_cones=None, yellow_cones=None, orange_small_cones=None, orange_big_cones=None, path=None):
        """
        Initializes the View object and sets up the Matplotlib plot.
        """
        plt.axis('equal')

        # Plot the cones
        if unknown_cones is not None:
            plt.scatter(unknown_cones[:, 0], unknown_cones[:, 1], c='black', s=10)
        if blue_cones is not None:
            plt.scatter(blue_cones[:, 0], blue_cones[:, 1], c='blue', s=10)
        if yellow_cones is not None:
            plt.scatter(yellow_cones[:, 0], yellow_cones[:, 1], c='yellow', s=10)
        if orange_small_cones is not None:
            plt.scatter(orange_small_cones[:, 0], orange_small_cones[:, 1], c='orange', s=10)
        if orange_big_cones is not None:
            plt.scatter(orange_big_cones[:, 0], orange_big_cones[:, 1], c='orange', s=10)

        # Plot the car
        car_dir_length = 1.0
        plt.arrow(car_position[0], car_position[1], car_dir_length * car_direction[0], car_dir_length * car_direction[1], head_width=0.5, head_length=0.7, fc='black', ec='black')

        # Plot the path
        if path is not None:
            plt.plot(path[:, 1], path[:, 2], c='green', linewidth=2)

        # Draw the plot
        plt.show()

