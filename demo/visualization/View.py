import matplotlib as matplotlib
from matplotlib import pyplot as plt

class View:
    """
    A graphical representation of a car's environment in a 2D space.

    This class uses Matplotlib to create a dynamic plot that can display the position and path of a car, as well as the location of various cones.

    Attributes:
        cones (list): A list of matplotlib scatter objects representing different types of cones.
        car_arrow (matplotlib.lines.Line2D): A Line2D object representing the car's position and direction.
        path (matplotlib.lines.Line2D): A Line2D object representing the car's path.
    """

    def __init__(self):
        """
        Initializes the View object and sets up the Matplotlib plot.
        """
        matplotlib.use('TkAgg')

        plt.ion()
        fig, ax = plt.subplots()
        plt.axis('equal')

        # Define the plot boundaries
        x_min, x_max = -40, 40
        y_min, y_max = -40, 40
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)

        # Initialize scatter objects for different types of cones and path elements
        self.cones = [ax.scatter([], [], c=color, s=10) for color in ['black', 'blue', 'yellow', 'orange', 'orange']]
        self.car_arrow, = ax.plot([], [], c="black")
        self.path, = ax.plot([], [], c="gray")

    def updateCones(self, unknown_cones=None, blue_cones=None, yellow_cones=None, orange_small_cones=None, orange_big_cones=None):
        """
        Updates the positions of the cones on the plot.

        Args:
            unknown_cones (numpy.array): Coordinates for unknown cones.
            blue_cones (numpy.array): Coordinates for blue cones.
            yellow_cones (numpy.array): Coordinates for yellow cones.
            orange_small_cones (numpy.array): Coordinates for small orange cones.
            orange_big_cones (numpy.array): Coordinates for big orange cones.
        """
        if unknown_cones is not None:
            self.cones[0].set_offsets(unknown_cones)
        if blue_cones is not None:
            self.cones[1].set_offsets(blue_cones)
        if yellow_cones is not None:
            self.cones[2].set_offsets(yellow_cones)
        if orange_small_cones is not None:
            self.cones[3].set_offsets(orange_small_cones)
        if orange_big_cones is not None:
            self.cones[4].set_offsets(orange_big_cones)
        self.draw()

    def updateCar(self, position, direction):
        """
        Updates the car's position on the plot.

        Args:
            position (numpy.array): The car's position.
            direction (numpy.array): The car's direction.
        """

        self.car_arrow.set_data([position[0], position[0] + direction[0]], [position[1], position[1] + direction[1]])
        self.draw()

    def updatePath(self, path):
        """
        Updates the car's path on the plot.

        Args:
            path (numpy.array): An array of coordinates representing the car's path.
        """
        self.path.set_data(path[:,0], path[:,1])
        self.draw()

    def draw(self):
        """
        Redraws the plot with the updated positions of the car, cones, and path.
        """
        plt.draw()
        plt.pause(0.1)
