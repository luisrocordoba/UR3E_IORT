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
		
def open_gripper():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		print("ABRIR GRIPPER")
		#open the socket
		s.connect((HOST, PORT))
		s.sendall(b'SET POS 0\n')
		

def status_gripper():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		s.sendall(b'GET STA\n')
		data = s.recv(2**10)
		return data

def POS_gripper():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		s.sendall(b'GET POS\n')
		data = s.recv(2**10)
		return data
        

def activate_gripper():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		print("ACTIVAR GRIPPER")
		s.connect((HOST, PORT))
		s.sendall(b'SET ACT 1\n')

def GTO_gripper():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		print("ACTIVAR GRIPPER")
		s.connect((HOST, PORT))
		s.sendall(b'GET PRE\n')
		data = s.recv(2**10)
		return data

def terminate_gripper():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		print("APAGAR GRIPPER")
		s.connect((HOST, PORT))
		s.sendall(b'SET ACT 0\n')

def set_force_gripper():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		s.sendall(b'SET FOR 25\n')

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
		
def stat_speed_gripper():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		s.sendall(b'GET SPE\n')
		data = s.recv(2**10)
		print(data)