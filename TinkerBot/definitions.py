#!/usr/bin/env pybricks-micropython
# =============================================================================
# LIBRERIAS BOILERPLATE
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
# =============================================================================

from math import pi, degrees

ev3 = EV3Brick()

green_motor = Motor(Port.C)
motor_c = green_motor
blue_motor = Motor(Port.D)
motor_b = blue_motor
grua_motor = Motor(Port.B)
claw_motor = Motor(Port.A)

# c Y d > RUEDAS
# C > Green
# D > Blue
# B > GRUA
# a | CLAW

DIAMETRO_RUEDA_MM = 43.2
ENVERGADURA = 165

#axle-width conocido como envergadura
#original 185, con lo que mas gira preciso 214, 29mm offset de lo que deberia
robot = DriveBase(green_motor,blue_motor,DIAMETRO_RUEDA_MM,ENVERGADURA)