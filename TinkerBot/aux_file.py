#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from math import pi

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


