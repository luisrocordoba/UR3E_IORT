import urx 
import math
import time
import sys
import socket
import numpy as np

#Socket setings
HOST="192.168.1.102" #replace by the IP address of the UR robot
PORT=63352 #PORT used by robotiq gripper

def close_gripper():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		print("CERRANDO GRIPPER")
		#open the socket
		s.connect((HOST, PORT))
		s.sendall(b'SET POS 255\n')
		#Gripper finger position is between 0 (Full open) and 255 (Full close)

def open_gripper():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		print("ABRIR GRIPPER")
		#open the socket
		s.connect((HOST, PORT))
		s.sendall(b'SET POS 0\n')
		#Gripper finger position is between 0 (Full open) and 255 (Full close)


def set_force_gripper():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		s.sendall(b'SET FOR 25\n')

if sys.version_info[0] < 3: 
    input = raw_input
    
#Definimos un método de espera para activar movimiento
def wait():
    if do_wait:
        print("Click enter para continuar")
        input()
		
def espera(rob):
	while 1:
		pose=rob.getl()
		pose_r=[round(x, 3) for x in pose]
		time.sleep(1)
		pose_2=rob.getl()
		pose_r2=[round(x, 3) for x in pose_2]
		if all(x == y for x, y in zip(pose_r, pose_r2)):
			break
	

#Programa principal
if __name__ == '__main__':
	do_wait = True
	if len(sys.argv) > 1:
		do_wait = False
    #--------------CONEXIÓN DEL ROBOT------------------
	print("Conectandose a robot...")
	rob = urx.Robot("192.168.1.102") #Se crea al objeto robot y se conecta a la IP del UR3
	print("**Robot 1 conectado**")
	
	#-----------PCH Y CARGA-------------------
	rob.set_tcp((0, 0,  0.150, 0, 0, 0)) #Definimos la ubicación del EF montado al robot
	rob.set_payload(1.040,(-0.001, -0.002, 0.055)) #Definimos la masa del EF
	set_force_gripper()
	#Imprimimos la ubicación del TCP en el espacio (Cinemática Directa del robot)
	#rob.x, rob.y, rob.z regresa las posiciones en m, se convierten a mm para compararlos con PolyScope
	print("\nEfector final respecto a la base")
	print('Posicion de EF en x ' ,rob.x*1000) 
	print('Posicion de EF en y ' ,rob.y*1000)
	print('Posicion de EF en z ' ,rob.z*1000)
	time.sleep(0.2)
	
	try:
        #Se define un vector de posiciones para cada articulación (urx maneja radianes, por lo que se realiza la conversión)
        #------------------POSICION HOME------------------------
		home_joints=[math.radians(0),math.radians(-90),math.radians(-90),math.radians(-90),math.radians(90),0]
		
        #-----------VELOCIDAD ACELERACION------------

		a=0.3 #aceleración para movimiento
		v=0.4  #velocidad para movimiento
		print("\nMover robot a configuración 'home'...")
		print("Moviéndose")
		#pose=rob.getl()
		rob.movej(home_joints,acc=a,vel=v,wait=False) #Método de movimiento por juntas a cierta acel. y vel.
		open_gripper()
		espera(rob)
		print("Robot en 'home'")

		pose = rob.getl()
		print("Posicion x,y,z:", pose[0],pose[1],pose[2])
		print("Rotacion x,y,z:", pose[3],pose[4],pose[5])
		
        #PRIMER MOVIMIENTO
		print("\nPrimer Movimiento")
		print("Moviendose")
		new_joints=[math.radians(65.45),math.radians(-90),math.radians(-90),math.radians(-90),math.radians(90),math.radians(86)]
		rob.movej(new_joints,a,v,wait=False)
		espera(rob)
		pose1=rob.getl()
		print("Primera Posicion:")
		print("Posicion x,y,z:", pose1[0],pose1[1],pose1[2])
		print("Rotacion x,y,z:", pose1[3],pose1[4],pose1[5])

		
        #Segundo movimiento
		print("\nSegundo Movimiento")
		print("Moviendose")
		new_joints2=[math.radians(2.58),math.radians(-102.56),math.radians(-75.35),math.radians(-90),math.radians(87.23),math.radians(54.20)]
		rob.movej(new_joints2,a,v,wait=False)
		espera(rob)
		pose2=rob.getl()
		print("Segunda Posicion:")
		print("Posicion x,y,z:", pose2[0],pose2[1],pose2[2])
		print("Rotacion x,y,z:", pose2[3],pose2[4],pose2[5])

		
        #Tercer movimiento
		print("\nTercer Movimiento")
		pose2[2]-=0.092
		print("Moviendose")
		rob.movel(pose2,0.05,0.05,wait=False)
		espera(rob) 
		close_gripper()
		pose3=rob.getl()
		print("Tercera Posicion")
		print("Posicion x,y,z:", pose3[0],pose3[1],pose3[2])
		print("Rotacion x,y,z:", pose3[3],pose3[4],pose3[5])

		

		#Cuarto Movimiento
		print("\nCuarto Movimiento")
		pose3[2]+=0.092
		print("Moviendose")
		rob.movel(pose3,0.05,0.05,wait=False)
		espera(rob) 
		pose4=rob.getl()
		print("Cuarta Posicion")
		print("Posicion x,y,z:", pose4[0],pose4[1],pose4[2])
		print("Rotacion x,y,z:", pose4[3],pose4[4],pose4[5])


		#Quinto Movimiento
		print("\nQuinto Movimiento")
		print("Moviendose")
		new_joints3=[math.radians(-103.27),math.radians(-90.31),math.radians(-91.04),math.radians(-90.87),math.radians(90.78),math.radians(78.70)]
		rob.movej(new_joints3,a,v,wait=False)
		espera(rob)
		pose5=rob.getl()
		print("Quinta Posicion:")
		print("Posicion x,y,z:", pose5[0],pose5[1],pose5[2])
		print("Rotacion x,y,z:", pose5[3],pose5[4],pose5[5])


		#Sexto movimiento
		print("\nSexto Movimiento")
		pose5[2]-=0.054
		print("Moviendose")
		rob.movel(pose5,0.02,0.02,wait=False)
		espera(rob) 
		open_gripper()
		pose6=rob.getl()
		print("Sexta Posicion")
		print("Posicion x,y,z:", pose6[0],pose6[1],pose6[2])
		print("Rotacion x,y,z:", pose6[3],pose6[4],pose6[5])


		#Septimo movimiento
		print("\nSeptimo Movimiento")
		pose6[2]+=0.054
		print("Moviendose")
		rob.movel(pose6,0.05,0.05,wait=False)
		espera(rob) 
		pose7=rob.getl()
		print("Septima Posicion")
		print("Posicion x,y,z:", pose7[0],pose7[1],pose7[2])
		print("Rotacion x,y,z:", pose7[3],pose7[4],pose7[5])


		#Octavo Movimiento
		print("\nOctavo Movimiento")
		print("Moviendose")
		#new_joints4=[math.radians(-102.86),math.radians(-92.31),math.radians(-35.75),math.radians(-93.64),math.radians(90.78),math.radians(79.10)]
		new_joints4=[math.radians(-103.27),math.radians(-90.31),math.radians(-35.75),math.radians(-90.87),math.radians(90.78),math.radians(78.70)]
		rob.movej(new_joints4,a,v,wait=False)
		espera(rob)
		pose8=rob.getl()
		print("Octava Posicion:")
		print("Posicion x,y,z:", pose8[0],pose8[1],pose8[2])
		print("Rotacion x,y,z:", pose8[3],pose8[4],pose8[5])

		#Noveno Movimiento
		print("\nNoveno Movimiento")
		print("Moviendose")
		#new_joints5=[math.radians(-102.86),math.radians(-92.31),math.radians(-86.26),math.radians(-93.64),math.radians(90.78),math.radians(79.10)]
		new_joints5=[math.radians(-103.27),math.radians(-90.31),math.radians(-91.04),math.radians(-90.87),math.radians(90.78),math.radians(78.70)]
		rob.movej(new_joints5,a,v,wait=False)
		espera(rob)
		pose9=rob.getl()
		print("Novena Posicion:")
		print("Posicion x,y,z:", pose9[0],pose9[1],pose9[2])
		print("Rotacion x,y,z:", pose9[3],pose9[4],pose9[5])


		#Decimo movimiento
		print("\nDecimo Movimiento")
		pose9[2]-=0.054
		print("Moviendose")
		rob.movel(pose5,0.05,0.05,wait=False)
		espera(rob) 
		close_gripper()
		pose10=rob.getl()
		print("Decimo Posicion")
		print("Posicion x,y,z:", pose10[0],pose10[1],pose10[2])
		print("Rotacion x,y,z:", pose10[3],pose10[4],pose10[5])


		#Decimo Primer movimiento
		print("\nDecimo Primer Movimiento")
		pose10[2]+=0.054
		print("Moviendose")
		rob.movel(pose6,0.05,0.05,wait=False)
		espera(rob) 
		pose11=rob.getl()
		print("Decimo Primer Posicion")
		print("Posicion x,y,z:", pose11[0],pose11[1],pose11[2])
		print("Rotacion x,y,z:", pose11[3],pose11[4],pose11[5])


		#Decimo Segundo movimiento
		print("\nDecimo Segundo Movimiento")
		print("Moviendose")
		new_joints6=[math.radians(2.58),math.radians(-102.56),math.radians(-75.35),math.radians(-90),math.radians(87.23),math.radians(54.20)]
		rob.movej(new_joints6,a,v,wait=False)
		espera(rob)
		pose11=rob.getl()
		print("Decima Segunda Posicion:")
		print("Posicion x,y,z:", pose11[0],pose11[1],pose11[2])
		print("Rotacion x,y,z:", pose11[3],pose11[4],pose11[5])


		#Decimo Tercer movimiento
		print("\nDecimo Tercer Movimiento")
		pose11[2]-=0.088
		print("Moviendose")
		rob.movel(pose11,0.05,0.05,wait=False)
		espera(rob) 
		open_gripper()
		pose12=rob.getl()
		#punto3=rob.getl()
		print("Decimo Tercera Posicion")
		print("Posicion x,y,z:", pose12[0],pose12[1],pose12[2])
		print("Rotacion x,y,z:", pose12[3],pose12[4],pose12[5])


		#Decimo Cuarta movimiento
		print("\nDecimo Cuarto Movimiento")
		pose12[2]+=0.088
		print("Moviendose")
		rob.movel(pose12,0.05,0.05,wait=False)
		espera(rob) 
		pose13=rob.getl()
		print("Decimo Cuarta Posicion")
		print("Posicion x,y,z:", pose13[0],pose13[1],pose13[2])
		print("Rotacion x,y,z:", pose13[3],pose13[4],pose13[5])

	finally: 
		rob.close() #Desconexión del robot
		print("\nFin del programa")