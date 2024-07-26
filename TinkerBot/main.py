#!/usr/bin/env pybricks-micropython

# =============================================================================
# LIBRERIAS BOILERPLATE
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
# =============================================================================

import threading
#Esto no fue posible de modularizar, por lo que se tuvo que hacer en el main
#Sin embargo, el hecho de que las funciones no se puedan modularizar, hace que entonces
#sea más claro cuando hay reset.angle o reset
e1 = Motor(Port.C)
e2 = Motor(Port.D)
ev3 = EV3Brick()

sensorColor1 = ColorSensor(Port.S1)
sensorColor2 = ColorSensor(Port.S4)

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

    # =========================================
    # Inicio de la trayectoria

    # Imprimir Settings del robot
    print(df.robot.settings())

    # =========================================
    # Fase 1.1: Alineación inicial
    # =========================================

    # El robot cierra la garra 
    ge.cerrar_hasta_top() # Cierra la garra hasta que ya no puede
    fd.movimientoRecto(-200) # El robot se mueve hacia atrás para alinearse con la pared

    # =========================================
    # Fase 1.2: Primer Escombro (Amarillo)
    # =========================================

    # Abrir la garra para agarrar el escombro
    ge.abrir_garra()

    # Movernos hacia adelante para agarrar el escombro
    fd.movimientoRecto(350) # El robot se mueve 35cm hacia adelante

    # Cerrar la garra para agarrar el escombro
    ge.cerrar_hasta_top()

    # Subimos el elevador para evitar fricción con el suelo
    ge.moverElevadorGrua(True,90)

    # Movemos el robot hacia adelante para alinearnos con la primera pipa
    fd.movimientoRecto(85) # El robot se mueve 8cm hacia adelante

    wait(500) # Esperamos medio segundo para marcar el final de la fase

    # =========================================
    # Fase 1.3: Levantar la pipa
    # =========================================

    # Giramos el robot 90 grados a la derecha
    fd.girar(90)

    # Movemos el robot hacia adelante para alinearnos con la pipa
    fd.movimientoRecto(420) # El robot se mueve 42cm hacia adelante

    wait(250) # Esperamos un cuarto de segundo para asegurar que el robot ya se movio adelante

    # Levantamos la pipa con la grua
    ge.moverElevadorGrua(True,240)

    # Giramos para terminar de levantar la grua
    fd.girar(-30) # Giramos 30 grados a la izquierda
    fd.girar(30) # Reseteamos el angulo

    # =========================================
    # Fase 1.4: Apilar escombro amarillo
    # =========================================

    # Retrocedemos 0.5cm para alinearnos contra el escombro gris
    fd.movimientoRecto(-5)

    # Giramos hacia el escombro
    fd.girar(90)

    # Avanzamos hacia el escombro gris para posicionarnos
    fd.movimientoRecto(75)

    # Bajamos la grua para dejar el escombro amarillo ligeramente
    ge.moverElevadorGrua(False,140)

    # Abrimos la garra y depositamos el escombro
    ge.abrir_garra()
    wait(1000) # Esperamos 1s mientras se abre la garra

    # Bajamos la grua para agarrar ambos escombros
    ge.moverElevadorGrua(False,180)

    # Nos movemos hacia adelante para alinear los dos escombros
    fd.movimientoRecto(50)

    # Cerramos la garra hasta que no se pueda
    ge.cerrar_hasta_top()

    # =========================================
    # Fase 1.5: Depositar los escombros
    # =========================================

    # Nos movemos hacia atras para preparar el recorrido
    fd.movimientoRecto(-80)

    # Hacemos un ligero movimiento para evitar chocar contra la pipa
    fd.girar(-45) # Giramos 45 grados a la izquierda
    fd.movimientoRecto(-50) # Nos movemos 5cm hacia atras
    fd.girar(-48) # Giramos 48 grados a la izquierda (para completar el giro)

    # Ahora nos movemos hacia el centro del tablero
    fd.movimientoRecto(-900) # Nos movemos 90cm para atras

    # Giramos para alinearnos con la linea superior
    fd.girar(-90)

    # Nos movemos hacia la linea
    fd.movimientoRecto(350)

    # Estando alineados con la linea superior, la recorremos y avanzamos
    # hasta llegar al espacio de los escombros
    fd.girar(-90)
    fd.movimientoRecto(800) # Nos movemos hacia adelante 80cm

    # Nos giramos hacia el basurero y depositamos los escombros
    fd.girar(90)
    fd.movimientoRecto(30) # Movemos 30cm contra el basurero

    ge.moverElevadorGrua(False,280) # Bajamos la grua para depositar los escombros
    ge.abrir_garra() # Abrimos la garra
    fd.movimientoRecto(-30) # Deshacemos los 30cm que nos movimos
    wait(1000)

    # =========================================
    # Fase 1.6: Alineación Final
    # =========================================

    # Vamos en contra a la pista inicial
    fd.girar(-90)

    # Hacemos un avance inicial
    fd.movimientoRecto(-150)

    # Hacemos un bucle de tanteo hasta que encontramos rojo (de la pista inicial)
    while(sensorColor1.color() != Color.RED and sensorColor2.color() != Color.RED):
        fd.movimientoRecto(-10)
    
    # Cuando lo encontremos nos alineamos contra la pared
    fd.girar(-90)
    fd.movimientoRecto(-200)

    
def second_phase():
    print("Empezando segunda fase")
#thread1 = threading.Thread(target=play_song)
#thread2 = threading.Thread(target=first_phase)

#thread1.start()
#thread2.start()

first_phase()