import socket
import threading
import urx
# Choosing Nickname
nickname = "Robot"

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.100.21", 50000))

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
					resultado=lectura(message)
					print("Ya voy papa")
					mensaje='Robot:{}'.format(resultado)
					client.send(mensaje.encode('ascii'))
				except Exception as e:
					print(f"Se generó una excepción: {e}")
					print(message)
		except Exception as e:
			print(f"Se generó una excepción: {e}")
			# Close Connection When Error
			print("An error occured!")
			client.close()
			break


def lectura(message):
	if message=="1":
		rob = urx.Robot("192.168.1.102")
		rob.set_tcp((0, 0,  0.150, 0, 0, 0))
		rob.set_payload(1.040,(0, 0, 0))
		pose=rob.getl()
	return str(pose)

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()
