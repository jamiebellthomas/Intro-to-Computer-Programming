#Task 1

# def distance_calculator(angular_velocity, wheel_diameter_centimeters):
#     """
#     This function calculates the distance travelled by a robot with a given angular velocity and wheel diameter.
#     The output is a list of distances travelled at each time in time list 't'.
#     """
#     linear_velocity = wheel_diameter_centimeters/200 * angular_velocity
#     distance = []
#     for time in t:
#         distance.append(round((linear_velocity * time * 60),3))
#     return distance

# This section calls the distance_calculator function for each robot
# Each robot variable is a list of distances travelled at each time in time list 't'  
# robot_parameters = [(3,15),(6.5,10),(1,30)]
# for robot in robot_parameters:
#     distance_calculator(robot[0],robot[1])
# robot1 = distance_calculator(3, 15)
# robot2 = distance_calculator(6.5, 10)
# robot3 = distance_calculator(1, 30)

# This section stores the all the data in a single dictionary where each time 
# is a key and the values are lists of distances travelled by each robot at that time
# timeseries = {}
# for count, value in enumerate(t):
#     timeseries[value] = [robot1[count], robot2[count], robot3[count]]

#
t = [0.0, 2.0, 4.0, 6.0, 8.0, 10.0]
robots = [(3,15), (6.5,10), (1,30)]


# Initialise timeseries
timeseries = {}

# for count, value in enumerate(t):
#     timeseries[value] = [0] * len(robots) # [0, 0, 0]

_i = 0
while _i < len(t):
    value = t[_i]
    timeseries[value] = [0] * len(robots) # [0, 0, 0]
    _i += 1


'''

[Initialise Variables -- get t and robots, _i = 0]
|
(_i < len(t)) -> [add line to timeseries] -> [_i++] -> *loop back*
|



'''

# For each robot, compute values
for robot_index in range(len(robots)):
    robot = robots[robot_index]

    wheel_diameter_centimeters = robot[0]
    angular_velocity = robot[1]
    linear_velocity = (wheel_diameter_centimeters / 200) * angular_velocity

    for index, time in enumerate(t):
        timeseries[time][robot_index] = round((linear_velocity * time * 60), 3)




# This section prints the data in a table format
print ("{:<8} {:<10} {:<10} {:<10}".format('Time (minutes)','Robot 1 Position (cm)','Robot 2 Position (cm)','Robot 3 Position (cm)'))
for time, distances in timeseries.items():
    distance1, distance2, distance3 = distances
    print ("{:<15} {:<20} {:<20} {:<20}".format(time, distance1, distance2, distance3))
# This section works out the total distance travelled by each robot and therefore
# the distance between the nearest and furthest robot
# distances_travelled = [timeseries[0][-1], timeseries[1][-1], max(robot3)]
distances_travelled = [timeseries[t[-1]][i] for i in range(len(robots))]
gap = max(distances_travelled) - min(distances_travelled)
print (f"The gap between the furthest and the nearest robot is {gap} centimeters.")

