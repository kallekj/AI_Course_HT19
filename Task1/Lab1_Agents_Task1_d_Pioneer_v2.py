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

# Get all handlers for ultrasonic sensors
viable_sensors = []
for i in range(1,17):
    viable_sensors.append(vrep.simxGetObjectHandle(robot.clientID, "Pioneer_p3dx_ultrasonicSensor{}".format(i),vrep.simx_opmode_oneshot_wait))
    #viable_sensors.append("Pioneer_p3dx_ultrasonicSensor{}".format(i))


##########################
#   STACK FOR MOVEMENT   #
##########################
movementStack = []

def peek_stack(stack):
    if stack:
        return stack[-1]

#########################################    
#   Functions to control the robot      #
#########################################

def follow_wall():
            
    # if (right_sensors["sensor8"] + right_sensors["sensor9"] / 2) > 0.5:
    #     error = right_sensors["sensor8"] + right_sensors["sensor9"] / 2
    #     if error == float('inf'):
    #         error = 1
    #     World.setMotorSpeeds(dict(speedLeft=3*(error * 0.7), speedRight=1.5))
    # elif right_sensors["sensor8"] > right_sensors["sensor9"]:
    #     error = right_sensors["sensor8"] - right_sensors["sensor9"]
    #     if error == float('inf'):
    #         error = 1
    #     print("Error in Right: {}".format(error))
    #     World.setMotorSpeeds(dict(speedLeft=3*(error*0.5), speedRight=-3*(error*0.5)))


    # print((front_sensors["sensor4"] + front_sensors["sensor5"]) / 2 > 0.5)
    # if right_sensors["sensor8"] > right_sensors["sensor9"]:

    #     print((right_sensors["sensor8"], right_sensors["sensor9"]))  
    #     error = right_sensors["sensor8"] - right_sensors["sensor9"]
    #     if error == float('inf'):
    #         error = 1
    #     print("Error in Right: {}".format(error))
    #     World.setMotorSpeeds(dict(speedLeft=1*(error*0.5), speedRight=-3*(error*0.5)))   

    # elif right_sensors["sensor9"] > right_sensors["sensor8"]:
    #     print((right_sensors["sensor9"], right_sensors["sensor8"])) 
    #     error = right_sensors["sensor9"] - right_sensors["sensor8"]
    #     if error == float('inf'):
    #         error = 1
    #     print("Error in Right: {}".format(error))
    #     World.setMotorSpeeds(dict(speedLeft=-3*(error*0.5), speedRight=3*(error*0.5)))
    # else:
    #     World.setMotorSpeeds(dict(speedLeft=3, speedRight=3))

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
        if ((round(right_sensors["sensor8"] - right_sensors["sensor9"],2) < 0) or (right_sensors["sensor8"] > 0.5 and right_sensors["sensor9"] > 0.5) and front_sensors["sensor3"] > 0.4):
            print("Follow Wall, left: {}".format(0.1 + abs(error)))
            World.setMotorSpeeds(dict(speedLeft=0, speedRight=0.1 + abs(error)))   
        elif front_sensors["sensor3"] > 0.4 and round(right_sensors["sensor8"] - right_sensors["sensor9"],2) > 0:
            print("Follow Wall, right{}".format(1 + abs(error)*3))
            World.setMotorSpeeds(dict(speedLeft=1 + abs(error)*3, speedRight=0))
        else:
            print("Follow Wall, forward")
            #print("1.2: {}".format(1 - (1.2-front_sensors["sensor3"])*2))
            print("left={}   right={}".format(1 - (1-front_sensors["sensor3"])*2, 1 + (1-front_sensors["sensor3"])*2))
            World.setMotorSpeeds(dict(speedLeft=1 - (1-front_sensors["sensor3"])*2 , speedRight=1 + (1-front_sensors["sensor3"])*2))


def go_forward():
    World.setMotorSpeeds(dict(speedLeft=3, speedRight=3))

def point_to_energy(right_sensors, front_sensors):
    # print("point_to_energy()")
    # energyDirection = World.getSensorReading("energySensor")['direction']
    # robotDirection = World.robotDirection()
    
    # print("energy dir {}".format(energyDirection))
    # print("robot dir {}".format(robotDirection))

    # error = abs(robotDirection - energyDirection)
    # print("Rotate Right with error {}".format(error))
    # #if robotDirection < energyDirection:
    # rotateDir = dict(speedLeft=2*(error * 0.5), speedRight=-2*(error*0.5)) #Right
    # # else:
    # #     error = robotDirection - energyDirection
    # #     print("Rotate Left with error {}".format(error))
    # #     rotateDir = dict(speedLeft=-2*(error*0.5), speedRight=2*(error*0.5)) #Left
    
    # if error > 0.05:
    #     World.setMotorSpeeds(rotateDir)
    #     return True
    # else:
    #     World.setMotorSpeeds(dict(speedLeft=0, speedRight=0))
    #     return False


    # if not (robotDirection - energyDirection > -0.1 and robotDirection - energyDirection < 0.1):
    #     World.setMotorSpeeds(rotateDir)
    
        #trimming = False
        #break

    """energyDirection = round(World.getSensorReading("energySensor")['direction'], 1)
    #print("Point to energy")
    if energyDirection < 0:
        World.setMotorSpeeds(dict(speedLeft=energyDirection, speedRight=-energyDirection))
    elif energyDirection > 0:
        World.setMotorSpeeds(dict(speedLeft=energyDirection, speedRight=-energyDirection))
    else:
        if front_sensors["sensor3"] > 0.2 and front_sensors["sensor6"] > 0.2:
            go_forward()
        else:
            World.setMotorSpeeds(dict(speedLeft= 2 - (2.2 - front_sensors["sensor6"]), speedRight= 2 - (2.2 - front_sensors["sensor3"])))
    """

    
    theDirection = round(World.getSensorReading("energySensor")['direction'], 1)
    
    if theDirection > 0:
        rotateDir = dict(speedLeft=-1*theDirection, speedRight=1*theDirection) #Right
        World.setMotorSpeeds(rotateDir)
    elif theDirection < 0:
        rotateDir = dict(speedLeft=1*theDirection, speedRight=-1*theDirection) #Left
        World.setMotorSpeeds(rotateDir)
    else:
        print(check_wall())
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

def reverseMovement():
    latestMovement = movementStack.pop()
    nextToLastMovement = peek_stack(movementStack)

    inverseMovement = dict(speedLeft=latestMovement[0]["speedLeft"]*(-1), speedRight=latestMovement[0]["speedRight"]*(-1))
    print(nextToLastMovement[1], type(nextToLastMovement[1]))
    timeDelta = latestMovement[1] - nextToLastMovement[1]

    World.execute(inverseMovement, timeDelta, -1)

# def checkBoundary(limit):
#     sonarLeft = World.getSensorReading("ultraSonicSensorLeft")
#     sonarRight = World.getSensorReading("ultraSonicSensorRight")

#     if sonarLeft < limit and sonarRight < limit:
        
#         # latestMovement = movementStack.pop()
#         # nextToLastMovement = peek_stack(latestMovement)

#         # inverseMovement = dict(speedLeft=latestMovement[0]["speedLeft"]*(-1), speedRight=latestMovement[0]["speedRight"]*(-1))
#         # timeDelta = latestMovement[1] - nextToLastMovement[1]

#         # World.execute(inverseMovement, timeDelta, -1)
#         print("Too close!!")


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
    print("check_wall()")
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

    # while point_to_energy():
    #     pass

    # if try_collect_energy() == False:
    pickupTime += 1
    if pickupTime > 100:
        print("Unstuck!!")
        speedLeft = random.uniform(-4.0, 0)
        speedRight = random.uniform(-4.0, 0)
        World.execute(dict(speedLeft=speedLeft, speedRight=speedRight), 5000 ,-1)
        pickupTime = 0

    if front_sensors["sensor3"] < 0.3 and front_sensors["sensor6"] < 0.3 or front_sensors["sensor4"] < 0.3 and front_sensors["sensor5"] < 0.3:
        stuckCounter += 1
        World.setMotorSpeeds(dict(speedLeft=0, speedRight=0))
        #print("Stuck Counter: {}".format(stuckCounter))
        if stuckCounter > 10:
            stuckCounter = 0
            follow_wall()
            
    
    if try_collect_energy():
        pickupTime = 0
    else:
        point_to_energy(right_sensors, front_sensors)


    # while check_wall() == False:
    #     go_forward()
    #     if try_collect_energy() == False:
    #         dist_to_energy = World.getSensorReading("energySensor")['distance']
    #         print(World.getSensorReading("energySensor")['distance'] >= dist_to_energy)
    #         while World.getSensorReading("energySensor")['distance'] >= dist_to_energy:
    #             follow_wall()
    # dist_to_energy = float('inf')

    #
    #point_to_energy()
    #follow_wall()
    #############
    # Execution #
    #############
