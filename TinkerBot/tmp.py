#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()

green_motor = Motor(Port.A)
blue_motor = Motor(Port.D)
crane_motor = Motor(Port.B)
claw_motor = Motor(Port.C)

sensor1 = ColorSensor(Port.S1)
sensor2 = ColorSensor(Port.S2)

def seguidorDeLineas():
    green_motor.run(25)
    blue_motor.run(25)

    kp = 0.5
    target_path = 45

    while True:
        if (sensor1.reflection() < target_path) or (sensor2.reflection() > target_path):
            green_motor.run(kp * (sensor1.reflection() - target_path))
            blue_motor.run(20)
        if (sensor2.reflection() < target_path) or (sensor1.reflection() > target_path):
            green_motor.run(20)
            blue_motor.run(kp * (sensor2.reflection() - target_path))
        else:
            green_motor.run(20)
            blue_motor.run(20)