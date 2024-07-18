#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from math import pi, degrees
from aux_file import girar_90_grados,movimiento_recto
from subirBajar import moverElevadorGrua
from subirBajar import moverElevadorGrua

ev3 = EV3Brick()


green_motor = Motor(Port.C)
motor_c = green_motor
blue_motor = Motor(Port.D)
motor_b = blue_motor
grua_motor = Motor(Port.B)
claw_motor = Motor(Port.A)

# c Y d > RUEDAS
# C > Green
# D > Blue
# B > GRUA
# a | CLAW

LAST_CLAW_ANGLE = 0
RADIO_ENGRANAJE_MAYOR = 5
DIAMETRO_RUEDA_MM = 56

robot = DriveBase(green_motor,blue_motor,DIAMETRO_RUEDA_MM,185)

initial_angle=0

#########
#funciones'

#=================
def grab():
    print()
    #deberia de haber codigo aqui

# =========================================
# Retrocede el robot para alinearse
def initialAlign():
    time = 1000
    robot.drive(speed=-100, turn_rate=0)
    wait(time)
    robot.stop()

# =========================================
# Funcion para girar (no probada aun)
def rotateInPlace(angle):
    robot.turn(angle, Stop.hold, True)

# =========================================
# Funcion para avanzar cierta cantidad de cm
def moveForward(cm):
    # Me dicen que los motores estan invertidos asi que:
    robot.straight(cm * 10)
    # Multiplicado por 10 pq la funcion agarra mm

# =========================================
# Segunda funcion de movimiento recto
def moveForward2(cm):
    # La logica de aca es que el robot avance cierta cantidad de cm
    # basado en la cantidad de revoluciones que tiene que hacer

    # Calculamos la cantidad de revoluciones que tiene que hacer
    # Una revolución es 360 grados y mueve una cantidad de diametro * pi
    # Entonces hacemos la regla de 3:
    revolutions = (360 * cm) / ((DIAMETRO_RUEDA_MM / 10) * pi) # Como el diametro esta en mm lo dividimos entre 10

    green_motor.reset_angle(0)
    blue_motor.reset_angle(0)

    green_motor.run_angle(100, revolutions, Stop.HOLD, False)
    blue_motor.run_angle(100, revolutions, Stop.HOLD, True)

    print("Angulos de los motores: ", green_motor.angle(), ", ", blue_motor.angle())

# =========================================
def avanzar(distancia_cm, velocidad):

    tiempo_ms = abs((distancia_cm / velocidad) * 1000)
    robot.drive(velocidad, 0)
    wait(tiempo_ms)
    robot.stop()

# =========================================

def drop():
    claw_motor.run_angle(speed=-100, rotation_angle=-100, wait=True)
    grua_motor.stalled()
# =========================================

def cerrar_hasta_top():
   claw_motor.run_until_stalled
   print("banana con quevedo")


# =========================================
def cerrar_garra():
    claw_motor.run(speed=-100)
    wait(500)
    wait(500)
# =========================================
def abrir_garra():
    claw_motor.stop()
    claw_motor.run_target(speed=200, target_angle=180,wait=True)
    claw_motor.run_target(speed=200, target_angle=180,wait=True)

#pueden usar run_until_stall para resetear el mecanismo de ascensor 
# =========================================
def bajar_garra():
    #grua_motor.run_angle(speed=200,rotation_angle=-360)
    grua_motor.run_until_stalled(speed=-100, duty_limit=50)
# =========================================
def subir_garra():
    #grua_motor.run_angle(speed=200,rotation_angle=360)
    grua_motor.run_until_stalled(speed=100)
# =========================================
def initialize_claw():
    LAST_CLAW_ANGLE = claw_motor.run_until_stalled(-200, then=Stop.HOLD, duty_limit=40)
    print("LAST_CLAW_ANGLE: ",LAST_CLAW_ANGLE)
    abrir_garra()
    abrir_garra()
# =========================================
def first_phase():

   initialize_claw()
   cerrar_garra()
   subir_garra()
   bajar_garra()
   print("si paso")
   abrir_garra()
   #bajar_garra() 


   wait(2000)
   # subirUnBloque()
   #movimiento_recto(motor_b=blue_motor,motor_c=green_motor,distancia=30)

# =========================================    
def subirUnBloque():
    grua_motor.run_angle(speed=200,rotation_angle=245)



# =========================================

# =========================================
# Funciones de ayuda para subir y bajar la garra
def bajar_garra_cantidad(cantidad):
    # Bajar la garra la cantidad de grados que se pide (grados negativos)
    grua_motor.run_angle(speed=200,rotation_angle=-cantidad)

def subir_garra_cantidad(cantidad):
    # Subir la garra la cantidad de grados que se pide (grados positivos)
    grua_motor.run_angle(speed=200,rotation_angle=cantidad)

# =========================================
# Definimos variables globales para el movimiento de la garra
MOVIMIENTO_TOTAL = 0; # MOVIMIENTO_TOTAL lleva record de cuanto se ha movido la garra
GRUA_MAXIMO = 360 # GRUA_MAXIMO es el maximo de grados al que puede llegar la garra
BLOQUE_ALTURA = 280 # BLOQUE_ALTURA es la altura de un solo bloque

# =========================================
# Funcion para mover el elevador
def moverElevadorGrua(direccion, cantidad):
    global MOVIMIENTO_TOTAL, GRUA_MAXIMO

    # Imprimimos para debuggear
    print("moverElevadorGrua(): Se ha pedido que la garra se mueva: ",cantidad)
    print("moverElevadorGrua(): La garra se movera hacia: ",direccion)

    # La variable movimiento procesado es para que no se baje o suba mas de lo que se puede
    movimiento_procesado = 0

    # La direccion es un booleano, si es true subimos la garra y si es false la bajamos!!!
    if direccion == True:

        # Se comprueba si se puede subir la cantidad de grados que se pide
        if MOVIMIENTO_TOTAL + cantidad > GRUA_MAXIMO:
            # Si no se puede usamos esta logica para subir lo que se pueda:
            movimiento_procesado = GRUA_MAXIMO - MOVIMIENTO_TOTAL

            # Por ejemplo, si MOVIMIENTO_TOTAL = 340 y cantidad = 90, entonces no se puede subir mas
            # Entonces subimos lo que nos queda para llegar al maximo

            # Imprimimos para debuggear:
            print("moverElevadorGrua(): No se puede subir la cantidad de " + str(cantidad))
            print("moverElevadorGrua(): Se subira la cantidad de " + str(movimiento_procesado))
        else:
            # Si se puede, entonces subimos la garra por la cantidad que se pide
            movimiento_procesado = cantidad

        # Subimos la garra de acuerdo al movimiento procesado y lo añadimos al MOVIMIENTO_TOTAL
        subir_garra_cantidad(movimiento_procesado)
        MOVIMIENTO_TOTAL += movimiento_procesado

        return
    
    else:
        
        # Se comprueba si se puede bajar la cantidad de grados que se pide
        if MOVIMIENTO_TOTAL - cantidad < 0:

            # Si no se puede usamos esta logica para bajar lo que se pueda:
            movimiento_procesado = MOVIMIENTO_TOTAL

            # Por ejemplo, si MOVIMIENTO_TOTAL = 30 y cantidad = 90, entonces no se puede bajar mas
            # Entonces bajamos lo que queda de MOVIMIENTO_TOTAL (30) y no los 90 que se piden

            # Imprimimos para debuggear:
            print("moverElevadorGrua(): No se puede subir la cantidad de " + str(cantidad))
            print("moverElevadorGrua(): Se subira la cantidad de " + str(movimiento_procesado))
        else:
            # Si se puede, entonces bajamos la garra por la cantidad que se pide
            movimiento_procesado = cantidad
        
        # Bajamos la garra por el movimiento procesado y lo restamos al MOVIMIENTO_TOTAL
        bajar_garra_cantidad(movimiento_procesado)
        MOVIMIENTO_TOTAL -= movimiento_procesado

        return

# =========================================


# =========================================

# =========================================
# Funciones de ayuda para subir y bajar la garra
def bajar_garra_cantidad(cantidad):
    # Bajar la garra la cantidad de grados que se pide (grados negativos)
    grua_motor.run_angle(speed=200,rotation_angle=-cantidad)

def subir_garra_cantidad(cantidad):
    # Subir la garra la cantidad de grados que se pide (grados positivos)
    grua_motor.run_angle(speed=200,rotation_angle=cantidad)

# =========================================
# Definimos variables globales para el movimiento de la garra
MOVIMIENTO_TOTAL = 0; # MOVIMIENTO_TOTAL lleva record de cuanto se ha movido la garra
GRUA_MAXIMO = 360 # GRUA_MAXIMO es el maximo de grados al que puede llegar la garra
BLOQUE_ALTURA = 280 # BLOQUE_ALTURA es la altura de un solo bloque

# =========================================
# Funcion para mover el elevador
def moverElevadorGrua(direccion, cantidad):
    global MOVIMIENTO_TOTAL, GRUA_MAXIMO

    # Imprimimos para debuggear
    print("moverElevadorGrua(): Se ha pedido que la garra se mueva: ",cantidad)
    print("moverElevadorGrua(): La garra se movera hacia: ",direccion)

    # La variable movimiento procesado es para que no se baje o suba mas de lo que se puede
    movimiento_procesado = 0

    # La direccion es un booleano, si es true subimos la garra y si es false la bajamos!!!
    if direccion == True:

        # Se comprueba si se puede subir la cantidad de grados que se pide
        if MOVIMIENTO_TOTAL + cantidad > GRUA_MAXIMO:
            # Si no se puede usamos esta logica para subir lo que se pueda:
            movimiento_procesado = GRUA_MAXIMO - MOVIMIENTO_TOTAL

            # Por ejemplo, si MOVIMIENTO_TOTAL = 340 y cantidad = 90, entonces no se puede subir mas
            # Entonces subimos lo que nos queda para llegar al maximo

            # Imprimimos para debuggear:
            print("moverElevadorGrua(): No se puede subir la cantidad de " + str(cantidad))
            print("moverElevadorGrua(): Se subira la cantidad de " + str(movimiento_procesado))
        else:
            # Si se puede, entonces subimos la garra por la cantidad que se pide
            movimiento_procesado = cantidad

        # Subimos la garra de acuerdo al movimiento procesado y lo añadimos al MOVIMIENTO_TOTAL
        subir_garra_cantidad(movimiento_procesado)
        MOVIMIENTO_TOTAL += movimiento_procesado

        return
    
    else:
        
        # Se comprueba si se puede bajar la cantidad de grados que se pide
        if MOVIMIENTO_TOTAL - cantidad < 0:

            # Si no se puede usamos esta logica para bajar lo que se pueda:
            movimiento_procesado = MOVIMIENTO_TOTAL

            # Por ejemplo, si MOVIMIENTO_TOTAL = 30 y cantidad = 90, entonces no se puede bajar mas
            # Entonces bajamos lo que queda de MOVIMIENTO_TOTAL (30) y no los 90 que se piden

            # Imprimimos para debuggear:
            print("moverElevadorGrua(): No se puede subir la cantidad de " + str(cantidad))
            print("moverElevadorGrua(): Se subira la cantidad de " + str(movimiento_procesado))
        else:
            # Si se puede, entonces bajamos la garra por la cantidad que se pide
            movimiento_procesado = cantidad
        
        # Bajamos la garra por el movimiento procesado y lo restamos al MOVIMIENTO_TOTAL
        bajar_garra_cantidad(movimiento_procesado)
        MOVIMIENTO_TOTAL -= movimiento_procesado

        return

# =========================================

# =========================================
def test_phase():
    girar_90_grados(9, (DIAMETRO_RUEDA_MM/2)/10, green_motor, blue_motor, 4)
    #cerrar_hasta_top()
    #cerrar_garra()
    #moverElevadorGrua(True, BLOQUE_ALTURA)
    #abrir_garra()
    #moverElevadorGrua(False, BLOQUE_ALTURA)
    girar_90_grados(9, (DIAMETRO_RUEDA_MM/2)/10, green_motor, blue_motor, 4)
    #cerrar_hasta_top()
    #cerrar_garra()
    #moverElevadorGrua(True, BLOQUE_ALTURA)
    #abrir_garra()
    #moverElevadorGrua(False, BLOQUE_ALTURA)
    #movimiento_recto(motor_b=motor_b,motor_c=motor_c, distancia=27)
    # girar_90_grados(radio_robot=7.35,radio_rueda=2.16,right_motor=green_motor,left_motor=blue_motor,cuarto_de_circunferencia=4,velocidad=100)
    angle_radians = 1/4*pi
    girarEnRadianes(angle_radians)




# =========================================
# Función de Andrés también en test-phase, veáse girarEnRadianes.py

def girarEnRadianes(angle_radians):
    # robot = DriveBase(green_motor,blue_motor,68.8,185)
    # robot = class DriveBase(left_motor, right_motor, wheel_diameter, axle_track)
    # https://docs.pybricks.com/en/stable/robotics.html#measuring en caso que no gire bien :(

    controlGirar = True

    angle = degrees(angle_radians)

    if controlGirar == True:
        robot.turn(angle, Stop.HOLD, wait=True)




first_phase()

ev3.speaker.beep(4)
print("FUNCIONA")
