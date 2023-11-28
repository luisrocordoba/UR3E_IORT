import urx 
import time
import socket

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



rob = urx.Robot("192.168.1.102")
print("ROBOT CONECTADO")

rob.set_tcp((0, 0,  0.150, 0, 0, 0)) #Definimos la ubicación del EF montado al robot
rob.set_payload(1.040,(-0.001, -0.002, 0.055)) #Definimos la masa del EF

close_gripper()
time.sleep(5)
open_gripper()


rob.close()