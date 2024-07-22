from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from math import pi

ev3 = EV3Brick()


green_motor = Motor(Port.C)
motor_c = green_motor
blue_motor = Motor(Port.D)
motor_b = blue_motor
grua_motor = Motor(Port.B)
claw_motor = Motor(Port.A)

robot = DriveBase(green_motor,blue_motor,68.8,185)
initial_angle=0
# =========================================
# Definimos variables globales para el movimiento de la grua   
MOVIMIENTO_TOTAL = 0; # MOVIMIENTO_TOTAL lleva record de cuanto se ha movido la garra
GRUA_MAXIMO = 360 # GRUA_MAXIMO es el maximo de grados al que puede llegar la garra
BLOQUE_ALTURA = 280 # BLOQUE_ALTURA es la altura de un solo bloque

MOVIMIENTO_TOTAL = 0; # MOVIMIENTO_TOTAL lleva record de cuanto se ha movido la garra
GRUA_MAXIMO = 360; # GRUA_MAXIMO es el maximo de grados al que puede llegar la garra

LAST_CLAW_ANGLE = 0
# =========================================
# Funciones de ayuda para subir y bajar la garra
def bajar_garra_cantidad(cantidad):
    # Bajar la garra la cantidad de grados que se pide (grados negativos)
    grua_motor.run_angle(speed=200,rotation_angle=-cantidad)

def subir_garra_cantidad(cantidad):
    # Subir la garra la cantidad de grados que se pide (grados positivos)
    grua_motor.run_angle(speed=200,rotation_angle=cantidad)

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
    
#===========

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
