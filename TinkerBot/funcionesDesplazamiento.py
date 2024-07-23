
#estas dos variabls globales deben ser ajustadas individualmente,
#en el contexto de alguan variable,

# incrementar DIAMETRO_RUEDA si el robot avanza demasiado
# decrecer DIAMETRO_RUEDA si el robot no avanza lo suficiente

# incrementar ENVERGADURA si el robot no gira lo suficiente
# decrecer ENVERGADURA si el robot gira demasiado


DIAMETRO_RUEDA=56
ENVERGADURA=214

green_motor=Motor(Port.C)
blue_motor=Motor(Port.D)

robot = DriveBase(green_motor,blue_motor,DIAMETRO_RUEDA,ENVERGADURA)


def movimientoRecto(distance):
    robot.straight(distance)
    robot.stop()
    return

def girar(angle):
    robot.turn(angle)
    robot.stop()
    return


#alinearse al inicio, distance=-70

