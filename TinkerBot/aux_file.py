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


green_motor = Motor(Port.A)
blue_motor = Motor(Port.D)
crane_motor = Motor(Port.B)
claw_motor = Motor(Port.C)

gyro_sensor = GyroSensor(Port.S2)
LineSensor_left = ColorSensor(Port.S1)
LineSensor_right = ColorSensor(Port.S4)

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


# 1 es derecho 2 es izquierdo

#def PID():
#    target_path = 45
#    Kp = 0.5
 #   speed = 50
#
 #   while True:
  #      if  (LineSensor_right < target_path) or (LineSensor_left > target_path):
   #          var1 = Kp*(LineSensor_right.reflection()-target_path)
    #         blue_motor.run(SpeedPercent(var1))
     ##
      #  if  (LineSensor_left < target_path) or (LineSensor_right > target_path):
       #      var2 = Kp*(LineSensor_left.reflection()-target_path)
        #     blue_motor.run(SpeedPercent(20))
         #    green_motor.run(SpeedPercent(var2))
#
  #      else:
 #            print()
   #          robot.drive(SpeedPercent(20))