import urx 
import time
import socket

#Socket setings
HOST="192.168.1.102" #replace by the IP address of the UR robot
PORT=63352 #PORT used by robotiq gripper


def stat_speed_gripper():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		s.sendall(b'GET SPE\n')
		data = s.recv(2**10)
		print(data)
		
def set_speed_gripper():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		s.sendall(b'SET SPE 10\n')

def stat_force_gripper():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		s.sendall(b'GET FOR\n')
		data = s.recv(2**10)
		print(data)
		
def set_force_gripper():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		s.sendall(b'SET FOR 25\n')

rob = urx.Robot("192.168.1.102")
print("ROBOT CONECTADO")

rob.set_tcp((0, 0,  0.150, 0, 0, 0)) #Definimos la ubicación del EF montado al robot
rob.set_payload(1.040,(-0.001, -0.002, 0.055)) #Definimos la masa del EF

#Control y consulta de velocidad
stat_speed_gripper()
set_speed_gripper()
time.sleep(5)
stat_speed_gripper()
time.sleep(5)
#Control y consulta de fuerza
stat_force_gripper()
set_force_gripper()
time.sleep(5)
stat_force_gripper()

rob.close()