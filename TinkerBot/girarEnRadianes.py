# Controlar que la funcion gire por la derecha con un true y que este predeterminado, 
# si no sabes como hacerlo en python me escribes aqui. Controlar el angulo que vas a girar pasandole el angulo. 
# Refierete a la funcion de alexander moverRad(). 

# En comparación al codigo de elbolo, éste deja pasar un ángulo arbitrario en radianes,
# además, utiliza la DriveBase entera en vez de los Motores individualmente
# posiblemente sean necesarias correcciones, hacia la derecha, a favor de las agujas del reloj, es negativo? 

from main import pi, robot, DriveBase, Stop, wait, turn, Motor
import math



def girarEnRadianes(angle_radians):
    # robot = DriveBase(green_motor,blue_motor,68.8,185)
    # robot = class DriveBase(left_motor, right_motor, wheel_diameter, axle_track)
    # https://docs.pybricks.com/en/stable/robotics.html#measuring en caso que no gire bien :(

    controlGirar = True

    angle = math.degrees(angle_radians)

    if controlGirar == True:
        robot.turn(angle, Stop.HOLD, wait=True)



    # angulo_final_del_motor_d = right_motor.angle()
    #     angulo_final_del_motor_i = left_motor.angle()
        
    #     print("####################################### Primer giro #######################################")
    #     print("El motor debe de girar: ", grados_giro_motor, " El motor ha girado derecho: ", angulo_final_del_motor_d, " El motor ha girado izquierdo: ", angulo_final_del_motor_i)
    #     print("####################################### Final primer Giro #######################################")
        
    #     # Esta es la nueva parte agregada, para corregir el giro de los motores al finalizar.
    
    #     if right_motor != grados_giro_motor or left_motor != grados_giro_motor:
            
    #         correccion_derecha = grados_giro_motor - right_motor.angle()
    #         correccion_izquierda = grados_giro_motor - left_motor.angle()
    
    #         right_motor.reset_angle(0)
    #         left_motor.reset_angle(0)
    
    #         right_motor.run_angle(50, correccion_derecha, wait=False)
    #         left_motor.run_angle(-50, correccion_izquierda, wait=True)
    
    #         # Actualiza los angulos finales de los motores  
    #         angulo_final_del_motor_d += correccion_derecha
    #         angulo_final_del_motor_i += correccion_izquierda    
    
    #     print("####################################### Giro Corregido #######################################")
    #     print("El motor debe de girar: ", grados_giro_motor, " El motor ha girado derecho: ", angulo_final_del_motor_d, " El motor ha girado izquierdo: ", angulo_final_del_motor_i)
    #     print("####################################### Final de giro corregido #######################################")
    






