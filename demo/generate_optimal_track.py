import numpy as np


def generateOptimalTrack():
    """
    Generates the layout of an optimal track for racing simulations.

    The track is defined by the positions of various colored cones, which include blue, yellow, and orange cones.
    These cones represent the boundaries and key points on the track. The function also calculates the starting
    position and orientation for a car.

    Returns:
        tuple of list: A tuple containing two lists.
                       The first list contains the starting position and orientation of the car.
                       The second list contains arrays of the positions of orange small cones, orange big cones,
                       yellow cones, and blue cones, respectively.
    """

    # Define positions of blue cones on the track
    blue_cones = np.array(
        [[0.0, 15.0], [-0.5804185646014384, 17.91796117178381], [-2.233310793452575, 20.391689206547426],
         [-4.70703882821619, 22.044581435398563], [-7.624999999999999, 22.625], [-10.542961171783809, 22.044581435398563],
         [-13.016689206547424, 20.391689206547426], [-14.669581435398563, 17.91796117178381], [-15.25, 15.000000000000002],
         [-14.669581435398563, 12.082038828216191], [-13.016689206547426, 9.608310793452576],
         [-10.542961171783814, 7.95541856460144], [-7.625000000000002, 7.375], [-4.707038828216189, 7.955418564601439],
         [-2.233310793452577, 9.608310793452574], [-0.5804185646014401, 12.082038828216186],
         [6.5589885311209155, 5.183779967067581], [10.624999999999998, 4.375], [14.691011468879081, 5.183779967067579],
         [18.138009550107064, 7.4869904498929305], [20.44122003293242, 10.933988531120914], [21.25, 15.0],
         [20.44122003293242, 19.06601146887908], [18.138009550107068, 22.513009550107068],
         [14.69101146887908, 24.81622003293242], [10.625, 25.625], [6.558988531120922, 24.81622003293242],
         [4.722066274166729, 23.834364630714546], [4.7220662741667265, 6.165635369285457]])

    # Define positions of yellow cones on the track
    yellow_cones = np.array(
        [[18.25, 15.0], [17.669581435398563, 17.91796117178381], [16.016689206547426, 20.391689206547426],
         [13.54296117178381, 22.044581435398563], [10.625, 22.625], [7.7070388282161915, 22.044581435398563],
         [5.233310793452576, 20.391689206547426], [3.5804185646014384, 17.91796117178381], [3.0, 15.000000000000002],
         [3.5804185646014375, 12.082038828216191], [5.233310793452574, 9.608310793452576],
         [7.707038828216186, 7.95541856460144], [10.624999999999998, 7.375], [13.542961171783812, 7.955418564601439],
         [16.016689206547422, 9.608310793452574], [17.66958143539856, 12.082038828216186],
         [-3.558988531120921, 24.81622003293242], [-7.624999999999999, 25.625], [-11.69101146887908, 24.81622003293242],
         [-15.138009550107068, 22.513009550107068], [-17.44122003293242, 19.06601146887908], [-18.25, 15.000000000000002],
         [-17.44122003293242, 10.933988531120923], [-15.13800955010707, 7.486990449892933],
         [-11.691011468879084, 5.183779967067581], [-7.625000000000002, 4.375], [-3.558988531120919, 5.183779967067579],
         [-1.7220662741667256, 23.834364630714543], [-1.72206627416673, 6.165635369285454]])

    # Define positions of big orange cones
    orange_big_cones = np.array([[0.0, 14.5], [0.0, 15.5], [3.0, 14.5], [3.0, 15.5]])

    # Define positions of small orange cones
    orange_small_cones = np.array(
        [[0.0, 0.0], [3.0, 0.0], [0.0, 5.0], [3.0, 5.0], [0.0, 40.0], [1.0, 40.0], [2.0, 40.0], [3.0, 40.0], [0.0, 37.0],
         [0.0, 34.0], [0.0, 31.0], [0.0, 28.0], [0.0, 25.0], [3.0, 37.0], [3.0, 34.0], [3.0, 31.0], [3.0, 28.0],
         [3.0, 25.0]])

    # Shift the track by offest
    offset = np.array([1.5, 15])
    orange_small_cones = orange_small_cones - offset
    orange_big_cones = orange_big_cones - offset
    yellow_cones = yellow_cones - offset
    blue_cones = blue_cones - offset

    # Define the starting position and orientation of the car
    start_car = [np.array([0.0,0.0]),np.array([0.0,1.0])]

    return start_car, [orange_small_cones, orange_big_cones, yellow_cones, blue_cones]