#SE IMPORTAN LIBRERIAS
import urx
import time
#SE REALIZA CONEXIÓN CON EL ROBOT
rob = urx.Robot("192.168.1.102")
rob.set_tcp((0, 0,  0.150, 0, 0, 0)) #Definimos la ubicación del EF montado al robot
rob.set_payload(1.040,(0, 0, 0))

#SE OBTIENE LA POSICIÓN DEL ROBOT PARA MODIFICARLA
pose=rob.getl()
print(pose)
pose[0]+=0.05

#SE DEFINEN VELOCIDAD Y ACELERACIÓN
a=0.05 #aceleración para movimiento
v=0.05  #velocidad para movimiento

#SE EJECUTA UN MOVIMIENTO LINEAL
rob.movel(pose,acc=a,vel=v,wait=False)

#SE PAUSA EL PROGRAMA PARA QUE EL ROBOT PUEDA TERMINAR SU MOVIMIENTO
time.sleep(15)

#SE OBTIENE LA NUEVA POSICIÓN
pose2=rob.getl()
print(pose2)
rob.close()