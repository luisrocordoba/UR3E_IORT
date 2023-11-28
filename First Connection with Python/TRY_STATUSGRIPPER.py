import urx 
import time
import socket

#Socket setings
HOST="192.168.1.102" #replace by the IP address of the UR robot
PORT=63352 #PORT used by robotiq gripper


def status_gripper():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		s.sendall(b'GET STA\n')
		data = s.recv(2**10)
		print(data)
        #return status

def activate_gripper():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		print("ACTIVAR GRIPPER")
		s.connect((HOST, PORT))
		s.sendall(b'SET ACT 1\n')


rob = urx.Robot("192.168.1.102")
print("ROBOT CONECTADO")

rob.set_tcp((0, 0,  0.150, 0, 0, 0)) #Definimos la ubicación del EF montado al robot
rob.set_payload(1.040,(-0.001, -0.002, 0.055)) #Definimos la masa del EF
status_gripper()
time.sleep(5)
activate_gripper()
time.sleep(5)
status_gripper()
rob.close()