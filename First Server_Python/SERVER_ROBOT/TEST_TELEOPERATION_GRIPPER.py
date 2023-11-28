import socket
import threading
import func_gripper
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
					resultado=eleccion(message)
					mensaje='Robot:{}'.format(resultado)
					client.send(mensaje.encode('ascii'))
				except Exception as e:
					#print(f"Se generó una excepción: {e}")
					print(message)
		except Exception as e:
			print(f"Se generó una excepción: {e}")
			# Close Connection When Error
			print("An error occured!")
			client.close()
			break

def eleccion(message):
	if message=="Activar":
		func_gripper.activate_gripper()
		resultado="Gripper Activado"
	elif message=="Estatus":
		resultado=func_gripper.status_gripper()
	elif message=="Abrir":
		func_gripper.open_gripper()
		resultado="Gripper Abierto"
	elif message=="Cerrar":
		func_gripper.close_gripper()
		resultado="Gripper Cerrado"
	return resultado


# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()