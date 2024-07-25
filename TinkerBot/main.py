#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor
from pybricks.parameters import Port    
from pybricks.tools import wait
from pybricks.hubs import EV3Brick

import threading
#Esto no fue posible de modularizar, por lo que se tuvo que hacer en el main
#Sin embargo, el hecho de que las funciones no se puedan modularizar, hace que entonces
#sea más claro cuando hay reset.angle o reset
e1 = Motor(Port.C)
e2 = Motor(Port.D)
ev3 = EV3Brick()

import funcionesDesplazamiento as fd
import funcionesGarraYElevador as ge
import definitions as df

def play_song():
    while(True): 
        df.ev3.speaker.beep(500, 214)
        wait(214)

        df.ev3.speaker.beep(500, 214)
        df.ev3.speaker.beep(420, 214)

        wait(214)
        df.ev3.speaker.beep(500, 214)

        wait(214)
        df.ev3.speaker.beep(500, 214)

        wait(214)
        df.ev3.speaker.beep(472, 214)

        wait(214)
        df.ev3.speaker.beep(375, 214)

        df.ev3.speaker.beep(749, 214)

        wait(107)
        df.ev3.speaker.beep(749, 214)

        wait(107)
        df.ev3.speaker.beep(630, 214)

        df.ev3.speaker.beep(500, 214)
        wait(214)

        df.ev3.speaker.beep(500, 214)
        df.ev3.speaker.beep(420, 214)

        wait(214)
        df.ev3.speaker.beep(500, 214)

        wait(214)
        df.ev3.speaker.beep(500, 214)

        wait(214)
        df.ev3.speaker.beep(472, 214)

        wait(214)
        df.ev3.speaker.beep(375, 214)

        df.ev3.speaker.beep(667, 214)

        wait(107)
        df.ev3.speaker.beep(667, 214)

        wait(107)
        df.ev3.speaker.beep(630, 214)

# Description: Trayectoria de TinkerBot

def main(): 

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

    wait(500)
    df.robot.stop()
    e1.reset_angle(0)
    e2.reset_angle(0)

    df.robot.reset()

    #aqui iria un cerrar

    fd.girar(91)

    fd.movimientoRecto(410)

    wait(500)
    ge.moverElevadorGrua(True,240)
    fd.girar(-30)

    fd.girar(30)


    fd.movimientoRecto(-10)

    fd.girar(86)

    fd.movimientoRecto(90)

    ge.moverElevadorGrua(False,180)
    ge.abrir_garra()
    wait(500)

    ge.moverElevadorGrua(False,140)
    fd.movimientoRecto(10)
    ge.moverElevadorGrua(True,70)
    ge.cerrar_hasta_top()

    ge.moverElevadorGrua(True,90)

    fd.movimientoRecto(-60)
    fd.girar(-89)

    fd.movimientoRecto(-20000)
    fd.girar(-89)

    fd.movimientoRecto(200)

thread1 = threading.Thread(target=play_song)
thread2 = threading.Thread(target=main)

thread1.start()
thread2.start()