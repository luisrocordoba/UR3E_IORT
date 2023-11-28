import socket
import threading

# Choosing Nickname
nickname = "menu"

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.100.44", 50000))

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
					mensaje='menu:{}'.format(resultado)
					client.send(mensaje.encode('ascii'))
				except:
					print(message)
		except Exception as e:
			print(f"Se generó una excepción: {e}")
			# Close Connection When Error
			print("An error occured!")
			client.close()
			break


def eleccion(message):
	arreglo=message.split(",")
	if arreglo[0]=="suma":
		resultado=suma(arreglo[1],arreglo[2])
	elif arreglo[0]=="resta":
		resultado = resta(arreglo[1],arreglo[2])
	return resultado

def suma(a,b):
	resultado= int(a)+int(b)
	return str(resultado)

def resta(a,b):
	resultado= int(a)-int(b)
	return str(resultado)

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()