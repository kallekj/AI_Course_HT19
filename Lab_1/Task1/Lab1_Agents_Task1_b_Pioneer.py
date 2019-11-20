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
    
    if simulationTime<4000:
        motorSpeed = dict(speedLeft=0, speedRight=0)
    elif simulationTime<9500:
        motorSpeed = dict(speedLeft=2, speedRight=2)
    elif simulationTime<10900:
        motorSpeed = dict(speedLeft=-2, speedRight=2)
    elif simulationTime<17000:
        motorSpeed = dict(speedLeft=3, speedRight=3)
        #print ("Trying to collect a block...",World.collectNearestBlock())
        #print ("BTW, nearest energy block is at:",World.getSensorReading("energySensor"))
    elif simulationTime<18000:
        motorSpeed = dict(speedLeft=0, speedRight=0)
    elif simulationTime<23900:
        motorSpeed = dict(speedLeft=-3, speedRight=-3)
    elif simulationTime<25300:
        motorSpeed = dict(speedLeft=2, speedRight=-2)
    elif simulationTime<27300:
        motorSpeed = dict(speedLeft=2, speedRight=2)
    elif simulationTime<28300:
        motorSpeed = dict(speedLeft=0, speedRight=0)
    elif simulationTime<31200:
        motorSpeed = dict(speedLeft=2, speedRight=-2)
    elif simulationTime<35500:
        motorSpeed = dict(speedLeft=4, speedRight=4)
    elif simulationTime<36850:
        motorSpeed = dict(speedLeft=2, speedRight=-2)
    elif simulationTime<44000:
        motorSpeed = dict(speedLeft=4, speedRight=4)
    else:
        motorSpeed = dict(speedLeft=0, speedRight=0)

        
    ########################################
    # Action Phase: Assign speed to wheels #
    ########################################

    # assign speed to the wheels
    World.setMotorSpeeds(motorSpeed)
    #  try to collect energy block (will fail if not within range)
    if simulationTime%1000==0 and [motorSpeed['speedLeft'], motorSpeed['speedRight']] == [0,0]:
        print ("Trying to collect a block...",World.collectNearestBlock())
    