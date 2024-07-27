#!/usr/bin/env pybricks-micropython
# =============================================================================
# LIBRERIAS BOILERPLATE
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
#usar un cvs para anotar las cosas??? DataLog?
from pybricks.robotics import DriveBase
# =============================================================================

import definitions as df

#########################
#   Grua definiciones   #
#########################

engranajes_grua = [[20,12],[20,12]]
perfi_tolerancia_grua = 11
direccion = Direction.CLOCKWISE
reiniciar_angulo = True

#grua_motor = Motor(Port.B,direccion,engranajes_grua,reiniciar_angulo,perfil_tolerancia_grua)
#grua_motor = Motor(Port.B,positive_direction=Direction.CLOCKWISE,gears=[[20,12],[20,12]],reset_angle=True,profile=11)
grua_motor = Motor(Port.B)

MOVIMIENTO_TOTAL = 0
GRUA_MAXIMO = 360
BLOQUE_ALTURA = 280

# que implicacion tienen esos 80 grados de diferencia entre GRUA_MAXIMO y BLOQUE_ALTURA


#los engranajes, son dos de 20 conectados directo al motor grande, de los cuales
#se les transfiere el torque a unos de 12

#profile por defecto de tolerancia, 11
#un perfil mas bajo, da mas precision pero movimientos mas chisporroteados (chiripiorca, erratico)
#un perfil mas alto, da menos precision pero movimientos mas mantequillosos (smooth)

###########################
# Garra definiciones #
###########################

LAST_CLAW_ANGLE = 0
perfil_tolerancia_garra = 11

engranajes_garra = [8,40]
#el engranaje chiquitito de 8 esta conectado directo al motor, le pasa la fuerza al de 40,
#que le pasa con un eje de 90 a los dos de 16 que abren/cierran la garra

#completé la definición
claw_motor = Motor(Port.A,Direction.CLOCKWISE,gears=engranajes_garra)

#############################################
# funciones de garra y elevador #
#############################################

def bajarGarra(cantidad):
    #es decir, a bajara a una velocidad de 200 grados por segundo, la cantidad
    #de grados
    grua_motor.run_angle(speed=200,rotation_angle=-cantidad)

def subirGarra(cantidad):
    grua_motor.run_angle(speed=200,rotation_angle=cantidad)

def moverElevadorGrua(direccion, cantidad):
    global MOVIMIENTO_TOTAL, GRUA_MAXIMO

    #prints para debug
    print("moverElevadorGrua(): Se ha pedido que la garra se mueva: ", cantidad)
    print("moverElevadorGrua(): La garra se va a mover hacia: ", direccion)
    #direccion CLOCKWISE, a favor de las agujas del reloj, positiva
    #direccion ANTICLOCKWISE, en contra de las agujas del reloj, negativa

    #para no bajar o subir mas de lo posible
    movimiento_procesado = 0
    
    #en el codigo de Mario la direccion lo toma como un booleano de una vez, pero usando los metodos del
    #pybricks se puede pasar mejor direccion 

    
    # si subir, y aun no alcanza el maximo lo solicitado a subir:
    if direccion == True:
        # y si ya sobrepaso el maximo posible para subir
        if MOVIMIENTO_TOTAL + cantidad > GRUA_MAXIMO:
            # entonces se sube lo posible ajustando movimiento_procesado
            movimiento_procesado = GRUA_MAXIMO - MOVIMIENTO_TOTAL
        
            #prints para debug
            print ("moverElevadorGrua(): No se puede subir la cantidad de " + str(cantidad))
            print("moverElevadorGrua(): Se subira la cantidad de " + str(movimiento_procesado))
        else:
            # se puede, simple
            movimiento_procesado = cantidad

        # se sube dicho movimiento_procesado, y se va conteando al MOVIMIENTO_TOTAL
        subirGarra(movimiento_procesado)
        MOVIMIENTO_TOTAL += movimiento_procesado

        return

    else:

        # comprobar si se puede bajar la cantidad de grados solicitada
        if MOVIMIENTO_TOTAL - cantidad < 0:

            # si no, para bajar lo posible
            movimiento_procesado = MOVIMIENTO_TOTAL

            # prints para debug
            print("moverElevadorGrua(): No se puede subir la cantidad de " + str(cantidad))
            print("moverElevadorGrua(): Se subira la cantidad de " + str(movimiento_procesado))
        else:
            # si se puede, entonces simple
            movimiento_procesado = cantidad

        # se baja dicho movimiento_procesado, y se va conteando al MOVIMIENTO_TOTAL
        bajarGarra(movimiento_procesado)
        MOVIMIENTO_TOTAL -= movimiento_procesado

        return
    

# =========================================

def drop():
    claw_motor.run_angle(speed=-100, rotation_angle=-100, wait=True)
    grua_motor.stalled()
# =========================================

def cerrar_hasta_muerte():
    claw_motor.run_until_stalled(speed=-100, duty_limit=100)
    print("cerrar_hasta_muerte(): Se ha llegado al duty limit")
    print("naranja con anuel")

def cerrar_hasta_top():
   claw_motor.run_until_stalled(speed=-100,duty_limit=40)
   print("cerrar_hasta_top(): Se ha llegado al duty limit")
   print("banana con quevedo")

# =========================================
def cerrar_garra():
    claw_motor.run(speed=-200)
    #muerto el wait de cerrar garra
# =========================================
def abrir_garra():
    #habian dos run targets, y wait era True
    claw_motor.run_target(speed=200, target_angle=-30,wait=False)

def abrir_garra_ang(angulo):
    claw_motor.run_target(speed=200, target_angle=-angulo,wait=False)

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
    """
    Inicializa la garra a una posición conocida.
    
    Returns:
        None
    
    Arguments:
        None
    """
    LAST_CLAW_ANGLE = claw_motor.run_until_stalled(-200, then=Stop.HOLD, duty_limit=40)
    print("LAST_CLAW_ANGLE: ",LAST_CLAW_ANGLE)
    abrir_garra()
    abrir_garra()

def subirUnBloque():
    grua_motor.run_angle(speed=200,rotation_angle=245)