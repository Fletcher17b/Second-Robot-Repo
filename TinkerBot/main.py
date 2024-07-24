#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor
from pybricks.parameters import Port    
from pybricks.tools import wait
from pybricks.hubs import EV3Brick
#Esto no fue posible de modularizar, por lo que se tuvo que hacer en el main
#Sin embargo, el hecho de que las funciones no se puedan modularizar, hace que entonces
#sea más claro cuando hay reset.angle o reset
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

fd.movimientoRecto(325)

ge.cerrar_hasta_top()

wait(2000)
df.robot.stop()
e1.reset_angle(0)
e2.reset_angle(0)

df.robot.reset()

#aqui iria un cerrar

fd.girar(90)

fd.movimientoRecto(420)