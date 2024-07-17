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
 