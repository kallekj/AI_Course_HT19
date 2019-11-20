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
import random

# connect to the server
robot = World.init()
# print important parts of the robot
print(sorted(robot.keys()))

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
    
    speedLeft = random.uniform(-4.0, 4.0)
    speedRight = random.uniform(-4.0, 4.0)
    simTime = random.randint(1000, 5000)
    print("speedLeft={} \t speedRight={} \t durationSimTime={}".format(speedLeft, speedRight, simTime))
  
    ########################################
    # Action Phase: Assign speed to wheels #
    ########################################

    World.execute(dict(speedLeft=speedLeft, speedRight=speedRight), simTime, -1)

    # assign speed to the wheels
    # World.setMotorSpeeds(motorSpeed)
    #  try to collect energy block (will fail if not within range)
    if simulationTime%10000==0:
        print ("Trying to collect a block...",World.collectNearestBlock())
    