#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor
from pybricks.parameters import Port    

#Esto no fue posible de modularizar, por lo que se tuvo que hacer en el main
#Sin embargo, el hecho de que las funciones no se puedan modularizar, hace que entonces
#sea más claro cuando hay reset.angle o reset
e1 = Motor(Port.C)
e2 = Motor(Port.D)


import funcionesDesplazamiento as fd
import funcionesGarraYElevador as ge
import definitions as df

# Description: Trayectoria de TinkerBot

#para atras acomodarse 1 

fd.movimientoRecto(-200)

#df.robot.reset()

#para adelante acomodarse 1
fd.movimientoRecto(235)

df.robot.stop()

e1.reset_angle(0)
e2.reset_angle(0)

df.robot.reset()

fd.girar(90)

ge.abrir_garra()

fd.movimientoRecto(270)

ge.cerrar_garra()
ge.cerrar_garra()

fd.movimientoRecto(245)

fd.girar(15)

fd.movimientoRecto(15)

ge.moverElevadorGrua(True,360)

ge.abrir_garra()
fd.girar(-20)

df.wait(200)

fd.girar(20)
ge.moverElevadorGrua(False,360)