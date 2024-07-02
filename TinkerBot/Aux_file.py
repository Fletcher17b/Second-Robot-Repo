#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from ev3dev2.motor import SpeedPercent

ev3 = EV3Brick()


green_motor = Motor(Port.A)
blue_motor = Motor(Port.D)
crane_motor = Motor(Port.B)
claw_motor = Motor(Port.C)

gyro_sensor = GyroSensor(Port.S2)
LineSensor_left = ColorSensor(Port.S1)
LineSensor_right = ColorSensor(Port.S3)

robot = DriveBase(green_motor,blue_motor,68.8,185)

# 1 es derecho 2 es izquierdo

def PID():
    target_path = 45
    Kp = 0.5
    speed = 50

    while True:
        if  (LineSensor_right < target_path) or (LineSensor_left > target_path):
             var1 = Kp*(LineSensor_right.reflection()-target_path)
             blue_motor.run(SpeedPercent(var1))
             green_motor.run(SpeedPercent(20))

        if  (LineSensor_left < target_path) or (LineSensor_right > target_path):
             var2 = Kp*(LineSensor_left.reflection()-target_path)
             blue_motor.run(SpeedPercent(20))
             green_motor.run(SpeedPercent(var2))

        else:
             print()
             robot.drive(SpeedPercent(20))