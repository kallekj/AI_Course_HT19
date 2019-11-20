# Make sure to have the server side running in V-REP:
# in a child script of a V-REP scene, add following command
# to be executed just once, at simulation start:
#
# simExtRemoteApiStart(19999)
# then start simulation, and run this program.
#
# IMPORTANT: for each successful call to simxStart, there
# should be a corresponding call to simxFinish at the end!
import Lab1_Agents_Task1_World as World
import vrep, math, random

# connect to the server
robot = World.init()
# print important parts of the robot
print(sorted(robot.keys()))

targetDistance = 0.5

# Get all handlers for ultrasonic sensors
viable_sensors = []
for i in range(1,17):
    viable_sensors.append(vrep.simxGetObjectHandle(robot.clientID, "Pioneer_p3dx_ultrasonicSensor{}".format(i),vrep.simx_opmode_oneshot_wait))
    #viable_sensors.append("Pioneer_p3dx_ultrasonicSensor{}".format(i))

#########################################    
#   Functions to control the robot      #
#########################################

def follow_wall():

    ######################
    #                    #
    #      3 4 5 6       #
    #       #####        #
    #       ##^## 8      #
    #       ##|## 9      #
    #       #####        #
    #                    #
    ######################
    followWall = True

    dist_to_energy = World.getSensorReading("energySensor")['distance']
    stuckCounter2 = 0
    while followWall:
        stuckCounter2 += 1

        if stuckCounter2 > 300:
            print("Unstuck!! c2")
            stuckCounter2 = 0
            break

        right_sensors = dict(sensor8=round(read_sensor(8), 6), sensor9=round(read_sensor(9), 6))
        front_sensors = dict(sensor3=round(read_sensor(3), 2), sensor4=round(read_sensor(4), 2), sensor5=round(read_sensor(5), 2), sensor6=round(read_sensor(6), 2))

        if (World.getSensorReading("energySensor")['distance'] + 0.3 < dist_to_energy) or (World.getSensorReading("energySensor")['distance'] < 0.5):
            followWall = False
            break
        
        error = right_sensors["sensor8"] - right_sensors["sensor9"]
        distance = ((right_sensors["sensor8"] + right_sensors["sensor9"]) / 2) - targetDistance
        regulator = distance + error*1.7

        if check_wall() == False:
            World.setMotorSpeeds(dict(speedLeft=(1+min(regulator,0))*3, speedRight=(1-max(0, regulator))*3))
        else:
            World.setMotorSpeeds(dict(speedLeft=-2, speedRight=2))
            

def go_forward():
    World.setMotorSpeeds(dict(speedLeft=2, speedRight=2))

def point_to_energy(right_sensors, front_sensors):
    
    theDirection = round(World.getSensorReading("energySensor")['direction'], 1)
    
    if theDirection < 0:
        rotateDir = dict(speedLeft=theDirection, speedRight=-theDirection) #Right
        World.setMotorSpeeds(rotateDir)
    elif theDirection >0:
        rotateDir = dict(speedLeft=theDirection, speedRight=-theDirection) #Left
        World.setMotorSpeeds(rotateDir)
    else:
        if check_wall() == False:
            go_forward()
        else:
            rotateDir = dict(speedLeft= 2 - (2.2 - front_sensors["sensor6"]), speedRight= 2 + (2.2 - front_sensors["sensor3"]))
            World.setMotorSpeeds(rotateDir)
        

def try_collect_energy():
    World.STOP()
    if World.getSensorReading("energySensor")['distance'] < 0.5:
        print ("Trying to collect a block...",World.collectNearestBlock())
        return True
    else:
        return False

def read_sensor(sensorID):
    
    ############################################
    # getObstacleDist() is from Task1_World.py #
    ############################################
    def getObstacleDist(sensorHandler_):
        # Get raw sensor readings using API
        rawSR = vrep.simxReadProximitySensor(robot.clientID, sensorHandler_, vrep.simx_opmode_oneshot_wait)
        #print(rawSR)
        # Calculate Euclidean distance
        if rawSR[1]: # if true, obstacle is within detection range, return distance to obstacle
            return math.sqrt(rawSR[2][0]*rawSR[2][0] + rawSR[2][1]*rawSR[2][1] + rawSR[2][2]*rawSR[2][2])
        else: # if false, obstacle out of detection range, return inf.
            return 1

    return getObstacleDist(viable_sensors[sensorID][1])
    

def check_wall():
    front_sensors = dict(sensor3=read_sensor(3), sensor6=read_sensor(6))
    
    if not (front_sensors["sensor3"] > 0.2 and front_sensors["sensor6"] > 0.2):
        if try_collect_energy():
            return False
        else:
            return True
    else:
        return False

            
stuckCounter = 0
pickupTime = 0
while robot: # main Control loop
    
    #######################################################
    # Perception Phase: Get information about environment #
    #######################################################
    simulationTime = World.getSimulationTime()

    right_sensors = dict(sensor8=round(read_sensor(8), 2), sensor9=round(read_sensor(9), 2))
    front_sensors = dict(sensor3=round(read_sensor(3), 2), sensor4=round(read_sensor(4), 2), sensor5=round(read_sensor(5), 2), sensor6=round(read_sensor(6), 2))
    
    ##############################################
    # Reasoning: figure out which action to take #
    ##############################################

    pickupTime += 1
    if pickupTime > 100:
        print("Unstuck!!")
        speedLeft = random.uniform(-4.0, 0)
        speedRight = random.uniform(-4.0, 0)
        World.execute(dict(speedLeft=speedLeft, speedRight=speedRight), 5000 ,-1)
        pickupTime = 0

    if front_sensors["sensor3"] < targetDistance and front_sensors["sensor6"] < targetDistance or front_sensors["sensor4"] < targetDistance and front_sensors["sensor5"] < targetDistance:
        stuckCounter += 1
        World.setMotorSpeeds(dict(speedLeft=0, speedRight=0))

        if stuckCounter > 10:
            stuckCounter = 0
            follow_wall()
            
    
    if try_collect_energy():
        pickupTime = 0
    else:
        point_to_energy(right_sensors, front_sensors)

