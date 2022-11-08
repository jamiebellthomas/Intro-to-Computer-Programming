#Task 3

def air_temperature_calculator(x, y, rad:list, rad_temp, air_temp):
    """This function calculates the temperature of the air at a given point in the room.
    given the coordinates of the point, the coordinates of the radiator, the radiator temperature and the air temperature."""
    temperature = air_temp + ((rad_temp - air_temp) / (1 + (x - rad[0])**2 + (y - rad[1])**2)**0.5)
    return temperature

def coord_list_calculator(no_of_x_points, no_of_y_points, room_dimensions):
    """This function calculates the seperate x & y coordinates of the points in the room for which temperatures are to be calculated."""
    x_point_coordinates = []
    y_point_coordinates = []
    # These lists will contain the x and y coordinates of the points in the room for which temperatures are to be calculated.
    x_step = room_dimensions[0] / (no_of_x_points-1)
    y_step = room_dimensions[1] / (no_of_y_points-1)
    # These variables are the distance between each x and y coordinate.
    # The -1 is to ensure that the last point is at the edge of the room.
    for i in range(no_of_x_points):
        x_point_coordinates.append(round(i * x_step, 6))
        # This loop calculates the x coordinates of the points in the room for which temperatures are to be calculated.
    for i in range(no_of_y_points):
        y_point_coordinates.append(round(i * y_step, 6))
        # This loop calculates the y coordinates of the points in the room for which temperatures are to be calculated.
    return x_point_coordinates, y_point_coordinates



def point_temp_calculator(x_coord_list, y_coord_list,radiator_coordinates,rad_temp, air_temp):
    """This function calculates the temperature of the air at each point in the room."""
    temperature_list = []
    for i in x_coord_list:
        for j in y_coord_list:
            point_temp = round(air_temperature_calculator(i, j, radiator_coordinates, rad_temp, air_temp),6)
            temperature_list.append(point_temp) 
            # These loops calculate the temperature of the air at each point in the room.
            # The outer loop runs through the x coordinates and the inner loop runs through the y coordinates at each x coordinate, working out the temperature at each point.
            # The temperature of each point is then added to the temperature_list.   
    return temperature_list

def mean_temperature_calculator(temperature_list):
    """This function calculates the mean temperature of the room."""
    mean_temp = round(sum(temperature_list) / len(temperature_list), 3)
    return mean_temp

def required_radiator_temperature_calculator(mean_temp, rad_temp, required_average_room_temp,x_point_coordinates, y_point_coordinates,radiator_coordinates, air_temp):
    """This function calculates the required radiator temperature in order to achieve a certain average room temperature.
    It does this by calculating the mean temperature of the room for a given radiator temperature, and if the mean temperature is less than the required average room temperature,
    the radiator temperature is increased by 0.1 degrees and the mean temperature is recalculated. 
    This process is repeated until the mean temperature is greater than or equal to the required average room temperature."""
    while mean_temp<required_average_room_temp:
        rad_temp += 0.1
        mean_temp = mean_temperature_calculator(point_temp_calculator(x_point_coordinates, y_point_coordinates,radiator_coordinates,rad_temp,air_temp))
        # This loop increases the radiator temperature by 0.1 degrees until the mean temperature of the room is greater than or equal to the required average room temperature.
    required_rad_temp = rad_temp
    return (round(required_rad_temp,1))

