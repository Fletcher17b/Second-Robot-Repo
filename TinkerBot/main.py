#!/usr/bin/env pybricks-micropython

# =============================================================================
# LIBRERIAS BOILERPLATE
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from math import pi, degrees
import funciones_desplazamiento as fd
import funciones_garra as fg

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

DIAMETRO_RUEDA_MM = 56

#axle-width conocido como envergadura
#original 185, con lo que mas gira preciso 214, 29mm offset de lo que deberia
robot = DriveBase(green_motor,blue_motor,DIAMETRO_RUEDA_MM,214)

initial_angle=0

#########
#funciones'


# =========================================
def first_phase():

   
   fg.initialize_claw()
   fg.cerrar_garra()
   fg.subir_garra()
   fg.bajar_garra()
   print("si paso")
   fg.abrir_garra()
   #bajar_garra() 


   wait(2000)
   # subirUnBloque()
   #movimiento_recto(motor_b=blue_motor,motor_c=green_motor,distancia=30)

# =========================================    

# =========================================
# Función de Andrés también en test-phase, veáse girarEnRadianes.py

def girarEnRadianes(angle):
    # https://docs.pybricks.com/en/stable/robotics.html#measuring en caso que no gire bien :(


    controlGirar = True
    if controlGirar == True:
        robot.turn(angle)



        #If your robot turns not far enough, increase the axle_track value slightly.
        #robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

        #If your robot turns too far, decrease the axle_track value slightly.


    return
# =========================================

# =========================================
def test_phase():
    


    fg.moverElevadorGrua(True,120)

    angle_radians = 1/2*pi
    angle = degrees(angle_radians)
    for i in range(16):
        girarEnRadianes(angle)


def test_phase2():
    fg.cerrar_garra()
    wait(5000)
    fg.subir_garra_cantidad(250)
    fd.movimiento_recto(motor_b=motor_b,motor_c=motor_c,distancia=6.2)
    fg.bajar_garra_cantidad(50)
    wait(500)
    fg.abrir_garra()
    fg.bajar_garra_cantidad(200)
    


test_phase2()

ev3.speaker.beep(4)
print("FUNCIONA")