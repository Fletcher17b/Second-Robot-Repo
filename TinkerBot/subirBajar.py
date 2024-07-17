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
GRUA_MAXIMO = 360; # GRUA_MAXIMO es el maximo de grados al que puede llegar la garra

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