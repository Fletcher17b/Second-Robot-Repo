#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()



green_motor = Motor(Port.A)
blue_motor = Motor(Port.D)
crane_motor = Motor(Port.B)
claw_motor = Motor(Port.C)

gyro_sensor = GyroSensor(Port.S2)
LineSensor_left = ColorSensor(Port.S1)
LineSensor_right = ColorSensor(Port.S3)

robot = DriveBase(green_motor,blue_motor,68.8,185)

initial_angle=0

#########
#funciones'

def unstuck():
    crane_motor.run_until_stalled(-100, then=Stop.HOLD, duty_limit=100)
    crane_motor.reset_angle(0)
    crane_motor.run_until_stalled(100, then=Stop.HOLD, duty_limit=34) 
    

def initialize_claw():
    claw_motor.run_until_stalled(speed=100,then=Stop.BRAKE)
    initial_angle=claw_motor.angle()
    print("Claw angle: ",initial_angle)

def grab():
    claw_motor.run_until_stalled(20)
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

def drop():
    claw_motor.run_angle(speed=100, rotation_angle=-100, wait=True)
    crane_motor.stalled()

def turn_(direction, angle):
    a =100
    b =-100
    if direction==1:
        a = a*-1
        b= b*-1
    


    print(stopAngle)
    while True:
        green_motor.run(100)
        blue_motor.run(-100)
        current_angle = gyro_sensor.angle()
        if current_angle >= stopAngle + 87:
            robot.stop()
            stopAngle = gyro_sensor.angle()
            break
    print(gyro_sensor.angle())  


try:
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
    claw_motor.run_angle(speed=130,rotation_angle=initial_angle-85)
    robot.drive(speed=94,turn_rate=0)
    wait(1570)
    robot.stop()
    wait(1100)
    grab() 
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
    wait(1300)
    robot.stop()

    while True:
        green_motor.run(100)
        blue_motor.run(-100)
        current_angle = gyro_sensor.angle()
        if current_angle >= stopAngle + 92:
            robot.stop()
            stopAngle = gyro_sensor.angle()
            break
    
    robot.drive(speed=70,turn_rate=0)
    wait(2000)
    robot.stop()
    wait(100) 
    crane_motor.run_time(speed=-50, time=50, then=Stop.HOLD, wait=True)
    drop()
    wait(1000)
    exit()



except:
    print
