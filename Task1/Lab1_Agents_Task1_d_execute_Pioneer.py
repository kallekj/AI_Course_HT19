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

# connect to the server
robot = World.init()
# print important parts of the robot
print(sorted(robot.keys()))

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

def trimDirection():
    trimming = True
    theDirection = World.getSensorReading("energySensor")['direction']
    World.execute(dict(speedLeft=1, speedRight=-1), 2, -1)
    movementStack.append([dict(speedLeft=1, speedRight=-1), 2])

    if abs(theDirection - World.getSensorReading("energySensor")['direction']) < theDirection:
        rotateDir = dict(speedLeft=1, speedRight=-1) #Right
    else:
        rotateDir = dict(speedLeft=-1, speedRight=1) #Left
    while trimming:
        theDirection = World.getSensorReading("energySensor")['direction']
        if not (theDirection > -0.2 and theDirection < 0.2):
            World.execute(rotateDir, 50, -1)
            movementStack.append([rotateDir, 50])
        else:
            World.execute(rotateDir, 50, -1)
            movementStack.append([rotateDir, 50])
            trimming = False
            break
    
def goForwardsNTicks(ticks):
    World.execute(dict(speedLeft=3, speedRight=3), ticks, -1)
    movementStack.append([dict(speedLeft=3, speedRight=3), ticks])

def goForward():
    World.setMotorSpeeds(dict(speedLeft=3, speedRight=3))
    movementStack.append([dict(speedLeft=3, speedRight=3), World.getSimulationTime()])

def trySuck():
    if World.getSensorReading("energySensor")['distance'] < 0.5:
        print ("Trying to collect a block...",World.collectNearestBlock())

def reverseMovement():

    latestMovement = movementStack.pop()
    
    inverseMovement = dict(speedLeft=latestMovement[0]["speedLeft"]*(-1), speedRight=latestMovement[0]["speedRight"]*(-1))

    World.execute(inverseMovement, latestMovement[1], -1)


motorSpeed = dict(speedLeft=0, speedRight=0)    

while robot: # main Control loop
    
    #######################################################
    # Perception Phase: Get information about environment #
    #######################################################
    simulationTime = World.getSimulationTime()
    if simulationTime%1000==0:
        # print some useful info, but not too often
        print ('Time:',simulationTime,\
               'ultraSonicSensorLeft:',World.getSensorReading("ultraSonicSensorLeft"),\
               "ultraSonicSensorRight:", World.getSensorReading("ultraSonicSensorRight"))

    
    ##############################################
    # Reasoning: figure out which action to take #
    ##############################################

    #goForwardsNTicks(1000)
    
    #checkBoundary(0.4)
    
    # if simulationTime < 3000:
    #     goForward()
    #     trySuck()
    #     if simulationTime%100 == 0:
    #         trimDirection()
    # elif simulationTime < 5000:
    #     reverseMovement()
    # else:
    #     World.setMotorSpeeds(dict(spedLeft=0, speedRight=0))
    
    # if simulationTime < 20000:
    #     goForwardsNTicks(200)
    #     trySuck()
    #     if simulationTime%100 == 0:
    #             trimDirection()
    # else:
    #     reverseMovement()


    

    #trySuck()

