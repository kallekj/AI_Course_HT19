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

    
def trimDirection():
    trimming = True
    theDirection = World.getSensorReading("energySensor")['direction']
    World.execute(dict(speedLeft=1, speedRight=-1), 2, -1)
    
    if abs(theDirection - World.getSensorReading("energySensor")['direction']) < theDirection:
        rotateDir = dict(speedLeft=1, speedRight=-1) #Right
    else:
        rotateDir = dict(speedLeft=-1, speedRight=1) #Left
    while trimming:
        theDirection = World.getSensorReading("energySensor")['direction']
        if not (theDirection > -0.1 and theDirection < 0.1):
            World.setMotorSpeeds(rotateDir)
        else:
            World.setMotorSpeeds(rotateDir)
            trimming = False
            break
    
def goForwardsNTicks(ticks):
    World.execute(dict(speedLeft=3, speedRight=3), ticks, -1)

def trySuck():
    if World.getSensorReading("energySensor")['distance'] < 0.5:
        print ("Trying to collect a block...",World.collectNearestBlock())


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

    motorSpeed = dict(speedLeft=0, speedRight=0)
    
    ##############################################
    # Reasoning: figure out which action to take #
    ##############################################

    trimDirection()
    goForwardsNTicks(1000)
    trySuck()

