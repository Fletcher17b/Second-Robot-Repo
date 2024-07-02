#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from aux_file import girar_90_grados

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

robot = DriveBase(green_motor,blue_motor,68.8,185)

initial_angle=0

#########
#funciones'

def unstuck():
<<<<<<< Updated upstream
    
    crane_motor.run_until_stalled(100, then=Stop.HOLD, duty_limit=10) 
    
=======
    crane_motor.run_until_stalled(100, then=Stop.HOLD, duty_limit=41) 
    crane_motor.run_time(speed=90, time=160)
>>>>>>> Stashed changes

def initialize_claw():
    claw_motor.run_until_stalled(speed=-100,then=Stop.BRAKE)
    initial_angle=claw_motor.angle()
    print("Claw angle: ",initial_angle)

def grab():
<<<<<<< Updated upstream
    claw_motor.run(-100)
    print("SI paso\n")
    crane_motor.run_time(speed=50, time=700, then=Stop.HOLD, wait=True)
=======
    claw_motor.run_until_stalled(100)
    crane_motor.run_time(speed=100, time=500, then=Stop.HOLD, wait=True)
>>>>>>> Stashed changes
    
def drop_ontop():
    print("1")
    claw_motor.run_until_stalled(100, then=Stop.HOLD, duty_limit=41)
    crane_motor.stalled()
    print("2")
    robot.drive(speed=94,turn_rate=0)
    wait(6000)
    robot.stop()
    print("3")
    
    drop()

def drop():
<<<<<<< Updated upstream
    claw_motor.run_angle(speed=-100, rotation_angle=-100, wait=True)
=======
    claw_motor.run_angle(speed=100, rotation_angle=-90, wait=True)
>>>>>>> Stashed changes
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


<<<<<<< Updated upstream
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
=======
try:
    
   # PID()
>>>>>>> Stashed changes
    unstuck()
    initialize_claw()
    grab()
    print("robot angle:",gyro_sensor.angle())
    robot.drive(speed=-94,turn_rate=0)
    wait(1200)
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
    wait(2700)
    robot.stop()
    print("stopAngle: ",stopAngle)
    print("gyro angle: ",gyro_sensor.angle())

    while True:
        green_motor.run(100)
        blue_motor.run(-100)
        current_angle = gyro_sensor.angle()
        if current_angle >= stopAngle +88:
            robot.stop()
            stopAngle = gyro_sensor.angle()
            break
    wait(5000)
#------------------------
    print("Aproaching first block")
<<<<<<< Updated upstream
    claw_motor.run_angle(speed=-100,rotation_angle=initial_angle-85)
    robot.drive(speed=94,turn_rate=0)
    wait(1300)
    robot.stop()
    wait(1100)

    crane_motor.run_until_stalled(speed=-40)    
    grab()
    
    crane_motor.run_angle(speed=60,rotation_angle=60)


=======
    
    claw_motor.run_angle(speed=100,rotation_angle=initial_angle-85)
    robot.drive(speed=94,turn_rate=0)
    wait(1500)
    robot.stop()
    wait(1000)
    grab() 
>>>>>>> Stashed changes
    print(gyro_sensor.angle())
    robot.drive(speed=-94,turn_rate=0)
    wait(1800)
    robot.stop()
    
    print(gyro_sensor.angle())


#-------------------------
    while True:
        green_motor.run(-100)
        blue_motor.run(100)
        current_angle = gyro_sensor.angle()
        if current_angle <= stopAngle -87:
            robot.stop()
            stopAngle = gyro_sensor.angle()
            break
     
<<<<<<< Updated upstream
    robot.drive(speed=70,turn_rate=0)
    wait(1650)
=======
    robot.drive(speed=94,turn_rate=0)
    wait(1000)
>>>>>>> Stashed changes
    robot.stop()
    

    while True:
        green_motor.run(100)
        blue_motor.run(-100)
        current_angle = gyro_sensor.angle()
<<<<<<< Updated upstream
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
   initialize_claw()
   moviemiento_recto(motor_b=green_motor,motor_c=blue_motor,distancia=18)
   girar_90_grados(radio_robot=16.9,radio_rueda=6.88,right_motor=blue_motor,left_motor=green_motor,cuarto_de_circunferencia=4,velocidad=100)
   moviemiento_recto(motor_b=green_motor,motor_c=blue_motor,distancia=33)

   claw_motor.run_angle(speed=50,rotation_angle=initial_angle+85)
   crane_motor.stop()
   claw_motor.run_until_stalled(speed=-100)
   
   crane_motor.run_angle(speed=50,rotation_angle=20)

 #  girar_90_grados(radio_robot=16.9,radio_rueda=6.88,right_motor=blue_motor,left_motor=green_motor,cuarto_de_circunferencia=4,velocidad=100)
   moviemiento_recto(motor_b=green_motor,motor_c=blue_motor,distancia=17)
=======
        if current_angle >= stopAngle + 85:
            robot.stop()
            stopAngle = gyro_sensor.angle()
            break
    robot.drive(speed=94,turn_rate=0)
    wait(2100)
    robot.stop()
    wait(1000)
    drop()
>>>>>>> Stashed changes







try:
    crane_motor.run_angle(speed=50,rotation_angle=60)
    first_phase()
except:
    print("no")
