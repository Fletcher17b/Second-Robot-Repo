#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from math import pi
from aux_file import girar_90_grados,movimiento_recto

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

LAST_CLAW_ANGLE = 0
RADIO_ENGRANAJE_MAYOR = 5
DIAMETRO_RUEDA_MM = 56

robot = DriveBase(green_motor,blue_motor,DIAMETRO_RUEDA_MM,185)

initial_angle=0

#########
#funciones'

#=================
def grab():
    print()
    #deberia de haber codigo aqui

# =========================================
# Retrocede el robot para alinearse
def initialAlign():
    time = 1000
    robot.drive(speed=-100, turn_rate=0)
    wait(time)
    robot.stop()

# =========================================
# Funcion para girar (no probada aun)
def rotateInPlace(angle):
    robot.turn(angle, Stop.hold, True)

# =========================================
# Funcion para avanzar cierta cantidad de cm
def moveForward(cm):
    # Me dicen que los motores estan invertidos asi que:
    robot.straight(cm * 10)
    # Multiplicado por 10 pq la funcion agarra mm

# =========================================
# Segunda funcion de movimiento recto
def moveForward2(cm):
    # La logica de aca es que el robot avance cierta cantidad de cm
    # basado en la cantidad de revoluciones que tiene que hacer

    # Calculamos la cantidad de revoluciones que tiene que hacer
    # Una revolución es 360 grados y mueve una cantidad de diametro * pi
    # Entonces hacemos la regla de 3:
    revolutions = (360 * cm) / ((DIAMETRO_RUEDA_MM / 10) * pi) # Como el diametro esta en mm lo dividimos entre 10

    green_motor.reset_angle(0)
    blue_motor.reset_angle(0)

    green_motor.run_angle(100, revolutions, Stop.HOLD, False)
    blue_motor.run_angle(100, revolutions, Stop.HOLD, True)

    print("Angulos de los motores: ", green_motor.angle(), ", ", blue_motor.angle())

# =========================================
def avanzar(distancia_cm, velocidad):

    tiempo_ms = abs((distancia_cm / velocidad) * 1000)
    robot.drive(velocidad, 0)
    wait(tiempo_ms)
    robot.stop()

# =========================================

def drop():
    claw_motor.run_angle(speed=-100, rotation_angle=-100, wait=True)
    grua_motor.stalled()
# =========================================

def cerrar_hasta_top():
   claw_motor.run_until_stalled
   print("banana con quevedo")


# =========================================
def cerrar_garra():
    claw_motor.run(speed=-100)
    wait(2000)
# =========================================
def abrir_garra():
    claw_motor.stop()
    claw_motor.run_target(speed=200, target_angle=LAST_CLAW_ANGLE,wait=True)

#pueden usar run_until_stall para resetear el mecanismo de ascensor 
# =========================================
def bajar_garra():
    #grua_motor.run_angle(speed=200,rotation_angle=-360)
    grua_motor.run_until_stalled(speed=-100, duty_limit=50)
# =========================================
def subir_garra():
    #grua_motor.run_angle(speed=200,rotation_angle=360)
    grua_motor.run_until_stalled(speed=100)
# =========================================
def initialize_claw():
    LAST_CLAW_ANGLE = claw_motor.run_until_stalled(-200, then=Stop.HOLD, duty_limit=40)
    print("LAST_CLAW_ANGLE: ",LAST_CLAW_ANGLE)
# =========================================
def first_phase():

   initialize_claw()
   cerrar_garra()
   subir_garra()
   bajar_garra()
   print("si paso")
   abrir_garra()
   #bajar_garra() 


   wait(2000)
   # subirUnBloque()
   #movimiento_recto(motor_b=blue_motor,motor_c=green_motor,distancia=30)

# =========================================    
def subirUnBloque():
    grua_motor.run_angle(speed=200,rotation_angle=245)


# =========================================
def test_phase():
    #movimiento_recto(motor_b=motor_b,motor_c=motor_c, distancia=27)
    girar_90_grados(radio_robot=7.35,radio_rueda=2.16,right_motor=green_motor,left_motor=blue_motor,cuarto_de_circunferencia=4,velocidad=100)


# =========================================


first_phase()

ev3.speaker.beep(4)
print("FUNCIONA")
