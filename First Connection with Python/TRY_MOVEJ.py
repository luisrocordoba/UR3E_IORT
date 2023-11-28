#SE IMPÓRTAN LIBRERIAS
import urx
import time
import math

#SE REALIZA CONEXIÓN CON EL ROBOT
rob = urx.Robot("192.168.1.102")
rob.set_tcp((0, 0,  0.150, 0, 0, 0)) #Definimos la ubicación del EF montado al robot
rob.set_payload(1.040,(0, 0, 0))
# SE OBTIENE POSICIÓN INICIAL
pose=rob.getl()
print(pose)

#COORDENADAS DE HOME PARA EL ROBOT
home_joints=[math.radians(0),math.radians(-90),math.radians(-90),math.radians(-90),math.radians(90),0]
#SE DEFINEN VELOCIDAD Y ACELERACIÓN
a=0.3 #aceleración para movimiento
v=0.4  #velocidad para movimiento
#Método de movimiento por juntas a cierta acel. y vel.
rob.movej(home_joints,acc=a,vel=v,wait=False) 
time.sleep(5) #SE PAUSA EL PROGRAMA PARA QUE EL ROBOT PUEDA TERMINAR SU MOVIMIENTO
# SE OBTIENE POSICIÓN FINAL
pose=rob.getl()
print(pose)
rob.close()