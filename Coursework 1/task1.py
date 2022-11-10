#Task 1

# Initialising timeseries and robot parameters
t = [0.0, 2.0, 4.0, 6.0, 8.0, 10.0]
robots = [(3,15), (6.5,10), (1,30)]


# Initialise results dictionary
timeseries = {}
_i = 0
while _i < len(t):
    value = t[_i]
    timeseries[value] = [0] * len(robots) 
    _i += 1
#print(timeseries)
# We now have a dictionary with the time values as keys and a list of zeros as values. 
# The length of the list is equal to the number of robots.

# For each robot, compute values
for robot_index in range(len(robots)):
    robot = robots[robot_index]
    # Collects relevant robot parameters from the list of tuples 'robots'

    angular_velocity = robot[0]
    # Collects the wheel angular velocity from the tuple 'robot' (first value in the tuple)
    wheel_diameter_centimeters = robot[1]
    # Collects the wheel diameter from the tuple 'robot' (second value in the tuple)
    linear_velocity = (wheel_diameter_centimeters / 200) * angular_velocity
    # Calculates the linear velocity from the wheel diameter and angular velocity 

    for index, time in enumerate(t):
        timeseries[time][robot_index] = round((linear_velocity * time * 60), 3)
        # Calculates the distance travelled by the robot at each time step and rounds to 3 decimal places
        # This value of the distance travelled is then added to the list of zeros in the dictionary 'timeseries' at the index of the robot


# This section prints the data in a table format
print ("{:<8} {:<10} {:<10} {:<10}".format('Time (minutes)','Robot 1 Position (cm)','Robot 2 Position (cm)','Robot 3 Position (cm)'))
for time, distances in timeseries.items():
    distance1, distance2, distance3 = distances
    print ("{:<15} {:<20} {:<20} {:<20}".format(time, distance1, distance2, distance3))
# This section collects the total distance travelled by each robot and therefore
# the distance between the nearest and furthest robot

# This collects the last value from the list of distances for each robot
distances_travelled = [timeseries[t[-1]][i] for i in range(len(robots))]
# This calculates the difference between the furthest and nearest robot
gap = max(distances_travelled) - min(distances_travelled)
print (f"The gap between the furthest and the nearest robot is {gap} centimeters.")

