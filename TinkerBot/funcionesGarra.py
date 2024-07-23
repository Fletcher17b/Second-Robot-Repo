
engranajes_grua = [[20,12],[20,12]]
perfil_tolerancia_grua = 11
direccion = Direction.CLOCKWISE
reiniciar_angulo = False

grua_motor = Motor(Port.B,direccion,engranajes_grua,reiniciar_angulo,perfil_tolerancia_grua)



#los engranajes, son dos de 20 conectados directo al motor grande, de los cuales
#se les transfiere el torque a unos de 12

#profile por defecto de tolerancia, 11
#un perfil mas bajo, da mas precision pero movimientos mas chisporroteados (chiripiorca, erratico)
#un perfil mas alto, da menos precision pero movimientos mas mantequillosos (smooth)

claw_motor = Motor(Port.A)

MOVIMIENTO_TOTAL = 0
GRUA_MAXIMO = 360
BLOQUE_ALTURA = 280

#pregunta, que implican esos 80 de diferencia entre GRUA_MAXIMO, BLOQUE_ALTURA

LAST_CLAW_ANGLE = 0

def bajarGarra(cantidad):
    #es decir, a bajara a una velocidad de 200 grados por segundo, la cantidad
    #de grados
    grua_motor.run_angle(speed=200,rotation_angle=-cantidad)

def subirGarra(cantidad):
    grua_motor.run_angle(speed=200,rotation_angle=cantidad)
