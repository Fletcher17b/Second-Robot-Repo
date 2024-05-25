#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time

def line_follower(distancia):
    LineSensor_left = ColorSensor(Port.S1)
    LineSensor_right = ColorSensor(Port.S3)

    luz_negra = 15 
    speed = 100 
    kp = 0.01

    starTime = time.time()
    #tiempo = speed/distancia
    tiempo = distancia/speed
    timeW = time.time()




    