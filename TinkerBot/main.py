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
sensorColor3 = ColorSensor(Port.S3)

robot_speaker = ev3.speaker

import funcionesDesplazamiento as fd
import funcionesGarraYElevador as ge
import definitions as df

# Función para reproducir una canción
def play_song():
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

def alternate_start():
    fd.movimientoRecto(-200)
    fd.movimientoRecto(200)

    fd.girar(-90)
    fd.movimientoRecto(350)

    fd.girar(90)
    fd.movimientoRecto(550)

    fd.girar(-90)
    fd.movimientoRecto(750)
    # Hacemos un bucle de tanteo hasta que encontramos rojo (de la pista inicial)
    while(sensorColor1.color() != Color.RED and sensorColor2.color() != Color.RED):
        fd.movimientoRecto(-5)
    
    # Cuando lo encontremos nos alineamos contra la pared
    fd.girar(-90)
    fd.movimientoRecto(-200)



    fd.girar(-45)
    while(sensorColor1.color() != Color.RED and sensorColor2.color() != Color.RED):
        fd.movimientoRecto(10)

    fd.girar(123)
    fd.movimientoRecto(-130)
    fd.girar(-90)

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
    fd.movimientoRecto(-100) # El robot se mueve hacia atrás para alinearse con la pared

    # =========================================
    # Fase 1.2: Primer Escombro (Amarillo)
    # =========================================

    # Abrir la garra para agarrar el escombro
    ge.abrir_garra()

    # Movernos hacia adelante para agarrar el escombro
    fd.movimientoRecto(350) # El robot se mueve 35cm hacia adelante

    # Cerrar la garra para agarrar el escombro amarillo
    ge.cerrar_hasta_top()

    # Subimos el elevador para evitar fricción con el suelo
    ge.moverElevadorGrua(True,90)

    # Movemos el robot hacia adelante para alinearnos con la primera pipa
    fd.movimientoRecto(105) # El robot se mueve 8cm hacia adelante

    wait(500) # Esperamos medio segundo para marcar el final de la fase

    # =========================================
    # Fase 1.3: Levantar la pipa
    # =========================================

    # Giramos el robot 90 grados a la derecha
    fd.girar(90)

    # Movemos el robot hacia adelante para alinearnos con la pipa
    fd.movimientoRecto(415) # El robot se mueve 41cm hacia adelante

    wait(250) # Esperamos un cuarto de segundo para asegurar que el robot ya se movio adelante

    # Levantamos la pipa con la grua
    ge.moverElevadorGrua(True,240)

    # Giramos para terminar de levantar la grua
    fd.girar(-30) # Giramos 30 grados a la izquierda
    fd.girar(30) # Reseteamos el angulo

    # =========================================
    # Fase 1.4: Apilar escombro amarillo
    # =========================================

    # Giramos hacia el escombro
    fd.girar(87)

    # Avanzamos hacia el escombro gris para posicionarnos
    fd.movimientoRecto(87)

    # Bajamos la grua para dejar el escombro amarillo ligeramente
    ge.moverElevadorGrua(False,140)

    # Abrimos la garra y depositamos el escombro
    ge.abrir_garra()
    wait(1000) # Esperamos 1s mientras se abre la garra

    # Bajamos la grua para agarrar ambos escombros
    ge.moverElevadorGrua(False,180)

    # Nos movemos hacia adelante para alinear los dos escombros
    fd.movimientoRecto(30)

    ge.moverElevadorGrua(True,90)

    # Cerramos la garra hasta que no se pueda
    ge.cerrar_hasta_top()

    # =========================================
    # Fase 1.5: Depositar los escombros
    # =========================================

    # Nos movemos hacia atras para preparar el recorrido
    fd.movimientoRecto(-100)

    # Hacemos un ligero movimiento para evitar chocar contra la pipa
    fd.girar(-45) # Giramos 45 grados a la izquierda
    
    fd.movimientoRecto(-50) # Nos movemos 5cm hacia atras
    fd.girar(-46) # Giramos 48 grados a la izquierda (para completar el giro)

    # Ahora nos movemos hacia el centro del tablero
    fd.movimientoRecto(-900) # Nos movemos 90cm para atras

    # Giramos para alinearnos con la linea superior
    fd.girar(-90)

    # Nos movemos hacia la linea
    fd.movimientoRecto(300)

    # Estando alineados con la linea superior, la recorremos y avanzamos
    # hasta llegar al espacio de los escombros
    fd.girar(-90)
    fd.movimientoRecto(950) # Nos movemos hacia adelante 80cm

    # Nos giramos hacia el basurero y depositamos los escombros
    fd.girar(77)
    fd.movimientoRecto(200) # Movemos 8cm contra el basurero

    ge.abrir_garra() # Abrimos la garra
    wait(500)

    ge.moverElevadorGrua(False,280) # Bajamos la grua para depositar los escombros
    fd.movimientoRecto(-200) # Deshacemos los 8cm que nos movimos
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
    fd.girar(-45)
    while(sensorColor1.color() != Color.RED and sensorColor2.color() != Color.RED):
        fd.movimientoRecto(10)

    fd.girar(123)
    fd.movimientoRecto(-130)
    fd.girar(-90)
    fd.movimientoRecto(-150)

    #acomodado chatel

    ge.cerrar_hasta_top()
    ge.abrir_garra()
    fd.movimientoRecto(340)
    ge.cerrar_hasta_top()

    wait(500)
    #despues de agarrar escombro pequeno 2

    fd.movimientoRecto(415)
    fd.movimientoRecto(120)
    fd.girar(30)
    fd.movimientoRecto(50)
    fd.girar(-30)
    fd.movimientoRecto(-100)

    fd.girar(-15)

    fd.movimientoRecto(-900)
    fd.movimientoRecto(30)

    fd.girar(90)

    fd.movimientoRecto(500)
    ge.abrir_garra()

    fd.movimientoRecto(-250)

    # Hacemos un bucle de tanteo hasta que encontramos rojo (de la pista inicial)
    while(sensorColor1.color() != Color.RED and sensorColor2.color() != Color.RED):
        fd.movimientoRecto(-5)
    
    # Cuando lo encontremos nos alineamos contra la pared
    fd.girar(-90)
    fd.movimientoRecto(-40)

    fd.girar(-45)
    while(sensorColor1.color() != Color.RED and sensorColor2.color() != Color.RED):
        fd.movimientoRecto(5)

    fd.girar(123)
    fd.movimientoRecto(-130)
    fd.girar(-90)
    fd.movimientoRecto(-200)

    # =========================================
    # Fase 1.3: Levantar la pipa
    # =========================================

    fd.movimientoRecto(305)
    fd.girar(90)

    ge.cerrar_hasta_top()
    fd.movimientoRecto(500)

    # Levantamos la pipa con la grua
    ge.moverElevadorGrua(True,330)

    # Giramos para terminar de levantar la grua
    fd.girar(-30) # Giramos 30 grados a la izquierda
    fd.girar(30) # Reseteamos el angulo
    
    fd.movimientoRecto(-250)
    fd.girar(-90)
    fd.movimientoRecto(-150)

    fd.girar(90)
    while(sensorColor1.color() != Color.RED and sensorColor2.color() != Color.RED):
        fd.movimientoRecto(-5)

    fd.girar(-90)
    fd.movimientoRecto(-200)

    ge.moverElevadorGrua(False,330)

    wait(500)

def third_phase():

    #estos hijueputas del otro grupo usan el rojo
    #asi nunca falla :(


    #subimos la grua un poquitito para reducir friccion
    ge.moverElevadorGrua(True,25)
    fd.movimientoRecto(145)
    #avanza hasta que, al girar, los sensores esten perpendiculares a las lineas blancas
    fd.girar(-90)

    #avanzamos ese poquitito para poner los sensores sobre el blanco iniciial
    fd.movimientoRecto(255)

    fd.girar(-90)

    fd.movimientoRecto(90)
    #a veces cierra DEMASIADO Fuerte
    ge.cerrar_garra()
    wait(300)

    ge.moverElevadorGrua(True,280)
    fd.movimientoRecto(-80)
    #retrocede para alinear con blancos
    fd.girar(90)


###LO QUE QUEREMOS; ES QUE SE "ENLLAVE" en esto
    if(sensorColor1.color() == Color.WHITE and sensorColor2.color() == Color.WHITE):
        fd.movimientoRecto(90)
        
        #la primera distancia paralela a los bloques antes del primero desde los sensores
        #registrando el color blanco por primera vez, hasta el medio del primer bloque
        #es de 8.5 cm,
        #de la mitad del primer bloque a la mitad del segundo y asi sucesivamente, son 9.5cm

        #considerando esa discrepancia de las distancias, 
        #if distancia recorrida, la separacion entre los bloques (14.25cm), entonces, girar 90,
        #y ejecutar funcion de bloques
    #EMILIO LEE ESTO TRABAJA HACE ALGO LOCO
        
    

    #avanza para agarrar primera roja


    #todo lo que esta abajo de esto debe ir comentado bien una vez se implemente lo que esta arriba
    ge.moverElevadorGrua(True,280)
    fd.girar(-90)

    #este avance fue mucho :(
    fd.movimientoRecto(40)

    #este bajar no me acuerdo para que era
    ge.moverElevadorGrua(False,60)


    #se detiene para bajar el primer bloque rojo sobre el segundo bloque rojo
    ge.grua_motor.stop()
    ge.claw_motor.stop()
    ge.abrir_garra()

    #baja para ponerlas ambas sobre el piso,
    #aqui necesitamos hacer que las jale un poco, y luego las empuje hacia adelante,
    #para levantarla el stack corrigiendo errores en el agarrado
    ge.moverElevadorGrua(False,280)
    ge.cerrar_garra()
    fd.movimientoRecto(-10)




    while(sensorColor1.color() != Color.BLACK and sensorColor2.color() != Color.BLACK):
        fd.movimientoRecto(-5)

    fd.girar(90)
    fd.movimientoRecto(40)
    fd.girar(-90)
    fd.movimientoRecto(115)

    ge.grua_motor.stop()
    ge.abrir_garra()

    #bajar para agarrar el primer amarillo
    ge.moverElevadorGrua(False,280)
    ge.cerrar_garra()
    ge.moverElevadorGrua(True,280)


third_phase()