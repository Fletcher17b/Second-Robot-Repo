#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from math import pi

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

def movimiento_recto(motor_b, motor_c, distancia):

    desired = 0
    motor_b.reset_angle(0)
    motor_c.reset_angle(0)
    kinteger = 0.001
    kproportional = 0.3
    kderivate = 0.2
    target_angle = ( distancia / (21.6) ) *360
    print(target_angle)
    integral = 0
    speed = 100
    while motor_b.angle() < target_angle:
        print(motor_b.angle(), motor_c.angle())
        actual = abs(motor_b.angle()) - abs(motor_c.angle())

        error = desired - actual
        integral = integral + error
        derivative = error - actual
        correcion = (error*kproportional) + (integral*kinteger) + (derivative*kderivate)

        motor_b.run(speed + correcion) 
        motor_c.run(speed - correcion)

        if speed < 150: 
           speed += 10
    motor_b.stop()
    motor_c.stop()
 
# =========================================

def drop():
    claw_motor.run_angle(speed=-100, rotation_angle=-100, wait=True)
    grua_motor.stalled()

def cerrar_hasta_top():
   #djfndnf
   print("banana con quevedo")

def cerrar_garra():
    claw_motor.run_target(speed=200, target_angle=-360,wait=False)
    wait(2000)

def abrir_garra():
    claw_motor.run_target(speed=200, target_angle=LAST_CLAW_ANGLE,wait=True)

#pueden usar run_until_stall para resetear el mecanismo de ascensor 

def bajar_garra():
    grua_motor.run_angle(speed=200,rotation_angle=-360)

def subir_garra():
    grua_motor.run_angle(speed=200,rotation_angle=360)

def initialize_claw():
    LAST_CLAW_ANGLE = claw_motor.run_until_stalled(-200, then=Stop.HOLD, duty_limit=40)
    print("LAST_CLAW_ANGLE: ",LAST_CLAW_ANGLE)

def first_phase():

   initialize_claw()
   claw_motor.run(-200)
   subir_garra()
   grua_motor.run_until_stalled(speed=100)
   grua_motor.run_angle(speed=200,rotation_angle=-350)
   print("si paso")
   claw_motor.stop()
   abrir_garra()
   #bajar_garra()
   


   wait(2000)
   # subirUnBloque()
   #movimiento_recto(motor_b=blue_motor,motor_c=green_motor,distancia=30)

    
def subirUnBloque():
    grua_motor.run_angle(speed=200,rotation_angle=245)


# =========================================
def test_phase():
    moveForward(10)

def avanzar(distancia_cm, velocidad):

    tiempo_ms = abs((distancia_cm / velocidad) * 1000)
    robot.drive(velocidad, 0)
    wait(tiempo_ms)
    robot.stop()


first_phase()

ev3.speaker.beep(4)
print("FUNCIONA")
