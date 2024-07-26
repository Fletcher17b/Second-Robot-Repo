#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor
from pybricks.parameters import Port    
from pybricks.tools import wait
from pybricks.hubs import EV3Brick

import threading
#Esto no fue posible de modularizar, por lo que se tuvo que hacer en el main
#Sin embargo, el hecho de que las funciones no se puedan modularizar, hace que entonces
#sea más claro cuando hay reset.angle o reset

#estos no precisa direccion y gears uwu :3
e1 = Motor(Port.C)
e2 = Motor(Port.D)
ev3 = EV3Brick()

robot_speaker = ev3.speaker

import funcionesDesplazamiento as fd
import funcionesGarraYElevador as ge
import definitions as df

# Función para reproducir una canción
def play_song():

    while(True): 
        robot_speaker.beep(500, 214)
        wait(214)

        robot_speaker.beep(500, 214)
        robot_speaker.beep(420, 214)

        wait(214)
        robot_speaker.beep(500, 214)

        wait(214)
        robot_speaker.beep(500, 214)

        wait(214)
        robot_speaker.beep(472, 214)

        wait(214)
        robot_speaker.beep(375, 214)

        robot_speaker.beep(749, 214)

        wait(107)
        robot_speaker.beep(749, 214)

        wait(107)
        robot_speaker.beep(630, 214)

        robot_speaker.beep(500, 214)
        wait(214)

        robot_speaker.beep(500, 214)
        robot_speaker.beep(420, 214)

        wait(214)
        robot_speaker.beep(500, 214)

        wait(214)
        robot_speaker.beep(500, 214)

        wait(214)
        robot_speaker.beep(472, 214)

        wait(214)
        robot_speaker.beep(375, 214)

        robot_speaker.beep(667, 214)

        wait(107)
        robot_speaker.beep(667, 214)

        wait(107)
        robot_speaker.beep(630, 214)

# Description: Trayectoria de TinkerBot

def first_phase(): 

    print(df.robot.settings())
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

    fd.movimientoRecto(420)

    wait(500)
    ge.moverElevadorGrua(True,240)
    fd.girar(-30)

    fd.girar(30)


    fd.movimientoRecto(-10)

    fd.girar(86)

    fd.movimientoRecto(90)

    ge.moverElevadorGrua(False,160)
    ge.abrir_garra()
    wait(1000)

    ge.moverElevadorGrua(False,140)
    fd.movimientoRecto(15)
    ge.moverElevadorGrua(True,50)
    ge.cerrar_hasta_top()

    ge.moverElevadorGrua(True,90)

    fd.movimientoRecto(-65)
    fd.girar(-90)

    fd.movimientoRecto(-900)
    fd.girar(-90)

    fd.movimientoRecto(350)
    fd.girar(-90)

    fd.movimientoRecto(800)
    fd.girar(-25)

    ge.moverElevadorGrua(False,70)
    fd.movimientoRecto(120)

    ge.moverElevadorGrua(True,245)
    fd.girar(-30)

    fd.girar(30)
    fd.girar(90)
    fd.girar(25)

    fd.movimientoRecto(150)
    ge.moverElevadorGrua(False,280)
    ge.abrir_garra()

    

#thread1 = threading.Thread(target=play_super_mario)
#thread2 = threading.Thread(target=first_phase)

#thread1.start()
#thread2.start()

first_phase()