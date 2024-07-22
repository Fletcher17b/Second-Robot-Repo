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

robot = DriveBase(green_motor,blue_motor,68.8,185)

RADIO_ENGRANAJE_MAYOR = 5
DIAMETRO_RUEDA_MM = 56


def girar_90_grados(radio_robot, radio_rueda, right_motor, left_motor,cuarto_de_circunferencia, velocidad = 100):
    right_motor.reset_angle(0)
    left_motor.reset_angle(0)

    # Calcula la distancia que cada rueda debe recorrer para girar 90 grados
    circunferencia_robot = 2 * pi * radio_robot
    distancia_giro_90 = circunferencia_robot / cuarto_de_circunferencia  # 90 grados es un cuarto de la circunferencia
    
    # Calcula los grados que debe girar cada motor para recorrer la distancia_giro_90
    circunferencia_rueda = 2 * 3.14159 * radio_rueda
    grados_giro_motor = (distancia_giro_90 / circunferencia_rueda) * 360  # Convertir a grados
    
    # Inicializa los motores para el giro
    right_motor.run_angle(velocidad, grados_giro_motor, wait=False)
    left_motor.run_angle(-velocidad, grados_giro_motor, wait=True)  # Gira en la dirección opuesta
# =========================================

def movimiento_recto(motor_b, motor_c, distancia):

    desired = 0
    motor_b.reset_angle(0)
    motor_c.reset_angle(0)
    kinteger = 0.001
    kproportional = 0.3
    kderivate = 0.2
    target_angle = ( distancia / (13.5716) ) *360
    print(target_angle)
    integral = 0
    speed = 100
    print("Start: ")
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
