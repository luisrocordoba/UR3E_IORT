import socket
import threading
import urx
import time
# Choosing Nickname
nickname = "Robot"

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client.connect(("192.168.100.21", 50000))
client.connect(("4.tcp.ngrok.io", 17936))

# Listening to Server and Sending Nickname
def receive():
	while True:
		try:
			# Receive Message From Server
			# If 'NICK' Send Nickname
			message = client.recv(1024).decode('ascii')
			unido=message.split()
			if message == 'NICK':
				client.send(nickname.encode('ascii'))
			else:
				try:
					resultado=eleccion(message)
					mensaje='Robot:{}'.format(resultado)
					client.send(mensaje.encode('ascii'))
				except Exception as e:
					print(message)
		except Exception as e:
			print(f"Se generó una excepción: {e}")
			# Close Connection When Error
			print("An error occured!")
			client.close()
			break

def eleccion(message):
	if message=="posicion":
		resultado=posicion()
	elif message=="movimiento":
		resultado=movlineal()
	return resultado

def posicion():
	rob = urx.Robot("192.168.1.102")
	rob.set_tcp((0, 0,  0.150, 0, 0, 0))
	rob.set_payload(1.040,(0, 0, 0))
	pose=rob.getl()
	rob.close()
	return str(pose)

def movlineal():
	rob = urx.Robot("192.168.1.102")
	rob.set_tcp((0, 0,  0.150, 0, 0, 0)) 
	rob.set_payload(1.040,(0, 0, 0))
	pose=rob.getl()
	pose[0]+=0.05
	rob.movel(pose,0.05,0.05,wait=False)
	time.sleep(15)
	pose2=rob.getl()
	rob.close()
	resultado="Movimiento listo"
	return resultado
# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()