#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from aux_file import girar_90_grados
import math

ev3 = EV3Brick()


green_motor = Motor(Port.A)
motor_c = green_motor
blue_motor = Motor(Port.D)
motor_b = blue_motor
crane_motor = Motor(Port.B)
claw_motor = Motor(Port.C)

gyro_sensor = GyroSensor(Port.S2)
LineSensor_left = ColorSensor(Port.S1)
LineSensor_right = ColorSensor(Port.S4)

DIAMETRO_RUEDA_MM = 68.8;
robot = DriveBase(green_motor,blue_motor,DIAMETRO_RUEDA_MM,185)

initial_angle=0

#########
#funciones'

def unstuck():
    
    crane_motor.run_until_stalled(100, then=Stop.HOLD, duty_limit=10) 
    

def initialize_claw():
    crane_motor.reset_angle
    crane_motor.run_target(speed=100, target_angle=85)
    #claw_motor.run_until_stalled(speed=-100,then=Stop.BRAKE)
    initial_angle=claw_motor.angle()
    print("Claw angle: ",initial_angle)

def grab():
    claw_motor.run(-100)
    print("SI paso\n")
    crane_motor.run_time(speed=50, time=700, then=Stop.HOLD, wait=True)
    
def drop_ontop():
    print("1")
    claw_motor.run_until_stalled(100, then=Stop.HOLD, duty_limit=30)
    crane_motor.stalled()
    print("2")
    robot.drive(speed=94,turn_rate=0)
    wait(6000)
    robot.stop()
    print("3")
    
    drop()

# =========================================
# Retrocede el robot para alinearse
def initialAlign():
    time = 1000;
    robot.drive(speed=-100, turn_rate=0)
    wait(time)
    robot.stop()

# =========================================
# Funcion para girar (no probada aun)
def rotateInPlace(angle):
    robot.turn(angle, Stop.hold, True);

# =========================================
# Funcion para avanzar cierta cantidad de cm
def moveForward(cm):
    # Me dicen que los motores estan invertidos asi que:
    robot.straight(cm * 10, Stop.hold, True);
    # Multiplicado por 10 pq la funcion agarra mm

# =========================================
# Segunda funcion de movimiento recto
def moveForward2(cm):
    # La logica de aca es que el robot avance cierta cantidad de cm
    # basado en la cantidad de revoluciones que tiene que hacer

    # Calculamos la cantidad de revoluciones que tiene que hacer
    # Una revolución es 360 grados y mueve una cantidad de diametro * pi
    # Entonces hacemos la regla de 3:
    revolutions = (360 * cm) / ((DIAMETRO_RUEDA_MM / 10) * math.PI) # Como el diametro esta en mm lo dividimos entre 10

    green_motor.reset_angle(0);
    blue_motor.reset_angle(0);

    green_motor.run_angle(100, revolutions, Stop.hold, True);
    blue_motor.run_angle(100, revolutions, Stop.hold, True);

    print("Angulos de los motores: ", green_motor.angle(), ", ", blue_motor.angle());

# =========================================

def drop():
    claw_motor.run_angle(speed=-100, rotation_angle=-100, wait=True)
    crane_motor.stalled()


def turn_left(angle):
    

    stopAngle=gyro_sensor.angle()
    print("stopangle= ",stopAngle)
    while True:
        print(gyro_sensor.angle())
        green_motor.run(-100)
        blue_motor.run(100)
        current_angle = gyro_sensor.angle()
        if current_angle <= stopAngle - angle:
            robot.stop()
            stopAngle = gyro_sensor.angle()
            break
    print(gyro_sensor.angle())  


def turn_right(angle):
    
    stopAngle =gyro_sensor.angle()
    print(stopAngle)
    while True:
        green_motor.run(100)
        blue_motor.run(-100)
        current_angle = gyro_sensor.angle()
        if current_angle >= stopAngle + angle:
            robot.stop()
            stopAngle = gyro_sensor.angle()
            break
    print(gyro_sensor.angle())  

def thingy_we_were_working_before():
    unstuck()
    initialize_claw()
    print("robot angle:",gyro_sensor.angle())
    robot.drive(speed=-94,turn_rate=0)
    wait(1400)
    robot.stop()
    wait(1000)
    robot.drive(speed=94,turn_rate=0)
    wait(1700)
    robot.stop()
    wait(100)
    stopAngle = gyro_sensor.angle()
    wait(1000)
#-------------------
    print("First turn")
    print("stopAngle:",stopAngle)
    while True:
        green_motor.run(100)
        blue_motor.run(-100)
        current_angle = gyro_sensor.angle()
        if current_angle >= stopAngle + 87:
            robot.stop()
            stopAngle = gyro_sensor.angle()
            break
    print("gyro: ", gyro_sensor.angle())    

    wait(1000)
#------------------------
    print("2")
    
    robot.drive(speed=94,turn_rate=0)
    print("OMGGGGG")
    wait(2200)
    print(LineSensor_right.reflection())
    while LineSensor_right.color() != Color.RED:
        robot.drive(speed=20,turn_rate=0)
        wait(100)
        print("Left: ", LineSensor_left.reflection())
        print("Right: ", LineSensor_right.reflection())
    robot.stop()
    print("stopAngle: ",stopAngle)
    print("gyro angle: ",gyro_sensor.angle())
    wait(100)
    robot.drive(speed=-94,turn_rate=0)
    wait(90)
    robot.stop()
    while True:
        green_motor.run(100)
        blue_motor.run(-100)
        current_angle = gyro_sensor.angle()
        if current_angle >= stopAngle + 85:
            robot.stop()
            stopAngle = gyro_sensor.angle()
            break
    wait(1000)
    
#------------------------
    print("Aproaching first block")
    claw_motor.run_angle(speed=-100,rotation_angle=initial_angle-85)
    robot.drive(speed=94,turn_rate=0)
    wait(1300)
    robot.stop()
    wait(1100)

    crane_motor.run_until_stalled(speed=-40)    
    grab()
    
    crane_motor.run_angle(speed=60,rotation_angle=60)


    print(gyro_sensor.angle())
    robot.drive(speed=-94,turn_rate=0)
    wait(1800)
    robot.stop()
    
    print(gyro_sensor.angle())

    
#-------------------------
    while True:
        green_motor.run(-70)
        blue_motor.run(70)
        current_angle = gyro_sensor.angle()
        if current_angle <= stopAngle -87:
            robot.stop()
            stopAngle = gyro_sensor.angle()
            break
     
    robot.drive(speed=70,turn_rate=0)
    wait(1650)
    robot.stop()
    

    while True:
        green_motor.run(100)
        blue_motor.run(-100)
        current_angle = gyro_sensor.angle()
        if current_angle >= stopAngle + 87:
            robot.stop()
            stopAngle = gyro_sensor.angle()
            break
    print("1")
    robot.drive(speed=70,turn_rate=0)
    wait(20108)
   
    print("2")
    crane_motor.run_time(speed=-50, time=50, then=Stop.HOLD, wait=True)
    drop()
    wait(1000)


def moviemiento_recto(motor_b, motor_c, distancia):

    desired = 0
    motor_b.reset_angle(0)
    motor_c.reset_angle(0)
    ki = 0.001
    kp = 0.3
    kd = 0.2
    target_angle = ( distancia / (21.6) ) *360
    print(target_angle)
    integral = 0
    speed = 10
    while motor_b.angle() < target_angle:
        # print(motor_b.angle(), motor_c.angle())
        actual = abs(motor_b.angle()) - abs(motor_c.angle())

        error = desired - actual
        integral = integral + error
        derivative = error - actual
        correcion = (error*kp) + (integral*ki) + (derivative*kd)

        motor_b.run(speed + correcion)
        motor_c.run(speed - correcion)

        if speed < 140: 
            speed += 10
    motor_b.stop()
    motor_c.stop()
 

def first_phase():
   initialAlign() # Retrocede el robot para alinearse
   initialize_claw()
   moviemiento_recto(motor_b=green_motor,motor_c=blue_motor,distancia=17.8)
   girar_90_grados(radio_robot=16.9,radio_rueda=6.88,right_motor=blue_motor,left_motor=green_motor,cuarto_de_circunferencia=4,velocidad=100)
   moviemiento_recto(motor_b=green_motor,motor_c=blue_motor,distancia=33)

   claw_motor.run_angle(speed=50,rotation_angle=initial_angle+85)
   crane_motor.stop()
   claw_motor.run_until_stalled(speed=-100)
   crane_motor.run_target(speed=50, target_angle=30)
   
   crane_motor.run_angle(speed=50,rotation_angle=20)

 #  girar_90_grados(radio_robot=16.9,radio_rueda=6.88,right_motor=blue_motor,left_motor=green_motor,cuarto_de_circunferencia=4,velocidad=100)
   moviemiento_recto(motor_b=green_motor,motor_c=blue_motor,distancia=18)
   girar_90_grados(radio_robot=16.9,radio_rueda=6.88,right_motor=blue_motor,left_motor=green_motor,cuarto_de_circunferencia=-20,velocidad=100)

   crane_motor.run_target(speed=25, target_angle=90)
   girar_90_grados(radio_robot=16.9,radio_rueda=6.88,right_motor=blue_motor,left_motor=green_motor,cuarto_de_circunferencia=15.4,velocidad=50)
   claw_motor.run_angle(speed=50,rotation_angle=initial_angle+130)




try:
    crane_motor.run_angle(speed=50,rotation_angle=60)
    first_phase()
except:
    print("no")
