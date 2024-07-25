#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor
from pybricks.parameters import Port    
from pybricks.tools import wait
from pybricks.hubs import EV3Brick
#Esto no fue posible de modularizar, por lo que se tuvo que hacer en el main
#Sin embargo, el hecho de que las funciones no se puedan modularizar, hace que entonces
#sea más claro cuando hay reset.angle o reset

#estos no precisa direccion y gears uwu :3
e1 = Motor(Port.C)
e2 = Motor(Port.D)
ev3 = EV3Brick()

import funcionesDesplazamiento as fd
import funcionesGarraYElevador as ge
import definitions as df

# Description: Trayectoria de TinkerBot

ge.cerrar_hasta_top()

#para atras acomodarse 1 
fd.movimientoRecto(-200)

#df.robot.reset()

#para adelante acomodarse 1

ge.abrir_garra()

fd.movimientoRecto(335)

ge.cerrar_hasta_top()

ge.moverElevadorGrua(True,90)

fd.movimientoRecto(125)

df.ev3.speaker.beep()
wait(500)
df.robot.stop()
e1.reset_angle(0)
e2.reset_angle(0)

df.robot.reset()

#aqui iria un cerrar

fd.girar(91)

fd.movimientoRecto(420)

df.ev3.speaker.beep()
wait(500)
ge.moverElevadorGrua(True,240)
fd.girar(-30)

fd.girar(30)

df.ev3.speaker.beep()
wait(500)
fd.movimientoRecto(-10)

fd.girar(86)

wait(200)
fd.movimientoRecto(90)

ge.moverElevadorGrua(False,180)
ge.abrir_garra()

wait(500)
ge.moverElevadorGrua(False,140)
fd.movimientoRecto(10)
ge.moverElevadorGrua(True,70)
ge.cerrar_hasta_top()

ge.moverElevadorGrua(True,90)
fd.girar(105)
fd.movimientoRecto(1500)