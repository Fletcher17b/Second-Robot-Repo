#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time 
from math import pi

ev3 = EV3Brick()

left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
crane_motor = Motor(Port.B)
claw_motor = Motor(Port.C)

claw_sensor = ColorSensor(Port.S3)
gyro_sensor = GyroSensor(Port.S2)
left_sensor = ColorSensor(Port.S1)
right_sensor = ColorSensor(Port.S4)

robot = DriveBase(left_motor,right_motor,68.8,185)

def line_follower(distancia=None):

    luz_negra = 15 #lo usaremos para hacer que el robot pare cuando ambos detecten menos de 15.
    speed = 140 #velocidad para los motores, 100mm/s
    kp = 0.09 #preguntar a alexander. 

    starTime = time.time()
    
    if distancia == None:
        condicional = False
    else:
        print("iniciando")
        condicional = True
    
    tiempo = (distancia*(18/7))/(68.8*pi)
    
    timeW = time.time()
    while True:
        #obtener valores de la luz
        timestamp = time.time()#obtener un timestamp
        left_light = left_sensor.reflection()
        right_light = right_sensor.reflection()
        
        #si ambos sensores estan en linea negra, entonces se acabo la linea y se detiene
        if time.time() - starTime  > 3 and left_light < 15 and right_light < 15:
            left_motor.brake()
            right_motor.brake()
            break
        
        if condicional and time.time() - starTime > tiempo:
            left_motor.brake()
            right_motor.brake()
            break
        #para calcular el error
        error = left_light - right_light
    
        #calcular ajuste proporcional. Control proporcional.
        turn = kp * error #propagacion del error. 
    
        #ajustar motores
        left_motor.run(speed + turn) #speed en grados/s. 200 grados por segundo
        right_motor.run(speed - turn)
        timeWFinal= time.time()
        print(timeWFinal-timeW)
        
    
        
    # df.to_csv("datos_Bolo.csv", index=False)