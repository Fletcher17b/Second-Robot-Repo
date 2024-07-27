# =============================================================================
# LIBRERIAS BOILERPLATE
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
# =============================================================================

#estas dos variabls globales deben ser ajustadas individualmente,
#en el contexto de alguan variable,

# increAmentar DIAMETRO_RUEDA si el robot avanza demasiado
# decrecer DIAMETRO_RUEDA si el robot no avanza lo suficiente

# incrementar ENVERGADURA si el robot no gira lo suficiente
# decrecer ENVERGADURA si el robot gira demasiado

DIAMETRO_RUEDA=56
ENVERGADURA=214

import definitions as df

def movimientoRecto(distance):
    df.robot.straight(distance)
    return



def girar(angle):
    """
    Girar el robot en un angulo determinado, angulo negativo gira a la derecha y positivo a la izquierda
    """ 

    wait(350)
    df.robot.turn(angle)
    df.robot.stop()
    return


#alinearse al inicio, distance=-70

