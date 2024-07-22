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

# while True:
#     print("Left: ", LineSensor_left.color())
#     print("Right: ", LineSensor_right.color())
#     wait(1000)

# crane_motor.run_until_stalled(-100, then=Stop.HOLD, duty_limit=100)
# crane_motor.reset_angle(0)
# crane_motor.run_until_stalled(100, then=Stop.HOLD, duty_limit=40)
claw_motor.run_until_stalled(100, then=Stop.HOLD, duty_limit=40)
claw_motor.run_until_stalled(-30, then=Stop.HOLD, duty_limit=40)
crane_motor.run(-50)
wait(500)
crane_motor.stop()
# claw_motor.run_until_stalled(30)
# crane_motor.run_until_stalled(100, then=Stop.HOLD, duty_limit=70)
# wait(1000)
# claw_motor.run_until_stalled(-30, then=Stop.HOLD, duty_limit=40)

