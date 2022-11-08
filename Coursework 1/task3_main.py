from task3_functions import *

# This section simply defines the parameters of the problem 
T_rad = 40.0 # Temperature of the radiator in degrees Celsius     
T_air = 5.0 # Temperature of the air in degrees Celsius
room_dimensions = [5,4] # Dimensions of the room in metres
radiator_coordinates = [2.5,0.0] # Coordinates of the radiator in metres 
no_of_x_points = 10 # Number of points in the x direction
no_of_y_points = 6 # Number of points in the y direction 
required_average_room_temp = 23.0 # Required average room temperature in degrees Celsius
degree_sign = u'\N{DEGREE SIGN}'

x_point_coordinates, y_point_coordinates = coord_list_calculator(no_of_x_points, no_of_y_points, room_dimensions) 
print("The x coordinates of the points in the room are: ", x_point_coordinates)
print("The y coordinates of the points in the room are: ", y_point_coordinates)
# This line calls the coord_list_calculator function to calculate the x and y coordinates of the points in the room for which temperatures are to be calculated
temperature_list = point_temp_calculator(x_point_coordinates, y_point_coordinates,radiator_coordinates,T_rad, T_air)
# This line calls the point_temp_calculator function to calculate the temperature of the air at each point in the room. The output is a list of temperatures at the points in the room.
initial_mean_temp = mean_temperature_calculator(temperature_list) 
# This line calls the mean_temperature_calculator function to calculate the mean temperature of the room. The output is a single number.
if initial_mean_temp < required_average_room_temp:
    required_rad_temp = required_radiator_temperature_calculator(initial_mean_temp, T_rad, required_average_room_temp,x_point_coordinates, y_point_coordinates,radiator_coordinates, T_air)
    print(f"The initial mean temperature is {initial_mean_temp}{degree_sign}C.")
    print(f"The required radiator temperature to reach an average temperature of {required_average_room_temp}{degree_sign}C is {required_rad_temp}{degree_sign}C.")  
else:
    print(f"The initial mean temperature is {initial_mean_temp}{degree_sign}C.")
    print("The initial radiator temperature is greater than or equal to required average room temperature.")

# This if clause compares the initial mean temperature to the required average room temperature. 
# If the initial mean temperature is less than the required average room temperature, the required radiator temperature is calculated and printed. 
# If the initial mean temperature is greater than or equal to the required average room temperature, the initial mean temperature is printed and 
# a message is printed to say that the initial radiator temperature is greater than or equal to the required average room temperature.
#print(sorted(temperature_list,key=float))
#print(len(temperature_list))