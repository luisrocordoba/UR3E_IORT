import urx 
import math
import time
import sys
import socket
from urx import urrtmon
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


if sys.version_info[0] < 3: 
    input = raw_input
    
#Definimos un método de espera para activar movimiento
def wait():
    if do_wait:
        print("Click enter para continuar")
        input()

#Programa principal
if __name__ == '__main__':
	do_wait = True
	if len(sys.argv) > 1:
		do_wait = False
    #--------------CONEXIÓN DEL ROBOT------------------
	print("Conectandose a robot...")
	#rob = urx.Robot("192.168.1.102", use_rt=True, urFirm=5.13) #Se crea al objeto robot y se conecta a la IP del UR3
	rob = urx.Robot("192.168.1.102")
	print("**Robot 1 conectado**")
	
	#-----------PCH Y CARGA-------------------
	rob.set_tcp((0, 0,  0.150, 0, 0, 0)) #Definimos la ubicación del EF montado al robot
	rob.set_payload(1.040,(0, 0, 0))
	#rob.set_payload(1.040,(-0.001, -0.002, 0.055)) #Definimos la masa del EF
	
	#Imprimimos la ubicación del TCP en el espacio (Cinemática Directa del robot)
	#rob.x, rob.y, rob.z regresa las posiciones en m, se convierten a mm para compararlos con PolyScope
	print("\nEfector final respecto a la base")
	print('Posicion de EF en x ' ,rob.x*1000) 
	print('Posicion de EF en y ' ,rob.y*1000)
	print('Posicion de EF en z ' ,rob.z*1000)
	time.sleep(0.2)
	
	try:
		home_joints=[math.radians(0),math.radians(-90),math.radians(-90),math.radians(-90),math.radians(90),0]
		a=0.3 #aceleración para movimiento
		v=0.5 #velocidad para movimiento
		print("\nMover robot a configuración 'home'...")
		time.sleep(2)
		wait()
		print("Moviéndose")
		rob.movej(home_joints,a,v,wait=False) #Método de movimiento por juntas a cierta acel. y vel.
		time.sleep(10)
		pose=rob.getl()
		print(pose)
		#j_current = rob.get_joint_current()
		#print(j_current)
		

       
		

		
	finally: 
		rob.close() #Desconexión del robot
		print("\nFin del programa")