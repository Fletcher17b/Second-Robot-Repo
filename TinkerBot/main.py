#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import Aux_file


ev3 = EV3Brick()

green_motor = Motor(Port.A)
blue_motor = Motor(Port.D)
crane_motor = Motor(Port.B)
claw_motor = Motor(Port.C)

claw_sensor = ColorSensor(Port.S3)
gyro_sensor = GyroSensor(Port.S2)
LineSensor_left = ColorSensor(Port.S1)
LineSensor_right = ColorSensor(Port.S4)

robot = DriveBase(green_motor,blue_motor,68.8,185)

initial_angle=0

#########
#funciones'

def advance_1():
    robot.straight(distance=20,then= Stop.HOLD,wait=False)

def turn_right(angle):
    robot.curve(120,angle,then=Stop, wait=False)

def turn_left(angle):
    angle = angle*-1
    robot.curve(120,angle,then=Stop, wait=False)

def unstuck():
    crane_motor.run_until_stalled(100, then=Stop.HOLD, duty_limit=41) 
    crane_motor.run_time(speed=90, time=200)


 
def initialize_claw():
    claw_motor.run_until_stalled(speed=100,then=Stop.BRAKE)
    initial_angle=claw_motor.angle()
    print("Claw angle: ")
    print(initial_angle)



def grab():
#
    claw_motor.run_until_stalled(100)
    claw_motor.run(speed=700)
    crane_motor.run_time(speed=100, time=500, then=Stop.HOLD, wait=True)
    
def drop_ontop():
    print("1")
    claw_motor.run_until_stalled(100, then=Stop.HOLD, duty_limit=41)
 #   crane_motor.run_angle(speed=100, rotation_angle=-40)
    crane_motor.stalled()
    print("2")
    robot.drive(speed=94,turn_rate=0)
    wait(6000)
    robot.stop()
    print("3")
    
    drop()

def drop():
    claw_motor.run_angle(speed=100, rotation_angle=-90, wait=True)
 #   crane_motor.run_angle(speed=100, rotation_angle=-40)
    crane_motor.stalled()

#    claw_motor.run_angle(speed=100, rotation_angle=40, wait=False)
#    claw_motor.run_angle(speed=100, rotation_angle=40, then=Stop.HOLD, wait=False)
#    crane_motor.run_angle(speed=1000, rotation_angle=1500, then=Stop.HOLD, wait=True)


# claw angle range is 45 degrees to open and close 


def initial_moveset(start_type):
    robot.robot.straight(distance=-200,then= Stop.HOLD,wait=False)
    robot.robot.straight(distance=400,then= Stop.HOLD,wait=False)

    if (start_type==1): 
        turn_right(90)
    else: 
        turn_left(90)



    

try:
    # claw_motor.run_angle(speed=100, rotation_angle=90, wait=True)
    # drop()
    # wait(1000)
    unstuck()
    initialize_claw()


    robot.drive(speed=-94,turn_rate=0)
    wait(1000)
    robot.stop()
    wait(1000)
    robot.drive(speed=94,turn_rate=0)
    wait(1700)
    robot.stop()
    wait(100)

#-------------------
    print("Second turn")
    green_motor.run_time(speed=90,time=2200,wait=False)
    blue_motor.run_time(speed=-90,time=3000,wait=True)
    print("advance")

#------------------------
    print("Third Phase")
    robot.drive(speed=94,turn_rate=0)
    wait(3000)
    robot.stop()
    print("turning 2")
    green_motor.run_time(speed=90,time=2250,wait=False)
    print("turning 2")
    blue_motor.run_time(speed=-90,time=3000,wait=True)

#------------------------
    claw_motor.run_angle(speed=100,rotation_angle=initial_angle-85)
    robot.drive(speed=94,turn_rate=0)
    wait(1750)
    print("a4")
    robot.stop()
    print("a5")
    wait(1000)
    grab() 

#    robot.drive(speed=-94,turn_rate=0)
#    wait(1750)
#    robot.stop()


#    wait(1000)
#    claw_motor.run_angle(speed=100, rotation_angle=-40, wait=True)
#    wait(1000)
#    
#    grab() 
#    print("Grab exits")
    
#    drop_ontop()
#    print("Drop EXITS")

    # wait(2000)
    # initial_moveset(1)



except:
    print
