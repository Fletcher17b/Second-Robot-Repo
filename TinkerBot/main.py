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

claw_sensor = ColorSensor(Port.S4)

LineSensor_left = ColorSensor(Port.S1)
LineSensor_right = ColorSensor(Port.S3)

robot = DriveBase(green_motor,blue_motor,34,150)

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


def grab():
#
    claw_motor.run_until_stalled(100)
    wait(1000)
    crane_motor.run_time(speed=100, time=1000, then=Stop.HOLD, wait=True)
    print("done")
    

def drop():
    claw_motor.run_until_stalled(100, then=Stop.HOLD, duty_limit=41)
    crane_motor.run_angle(speed=100, rotation_angle=-40)
    crane_motor.stalled()
#    claw_motor.run_angle(speed=100, rotation_angle=40, wait=False)
#    claw_motor.run_angle(speed=100, rotation_angle=40, then=Stop.HOLD, wait=False)
#    crane_motor.run_angle(speed=1000, rotation_angle=1500, then=Stop.HOLD, wait=True)

print("done")
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
    # wait(1000)
    # drop()
    # wait(1000)
    unstuck()
    wait(1000)
    claw_motor.run_angle(speed=100, rotation_angle=-60, wait=True)
    wait(1000)
    grab() 
    # wait(2000)
    # initial_moveset(1)



except:
    print
