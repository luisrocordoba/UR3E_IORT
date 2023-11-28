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
					resultado=suma(message)
					mensaje='Robot:{}'.format(resultado)
					client.send(mensaje.encode('ascii'))
				except:
					print(message)
		except Exception as e:
			print(f"Se generó una excepción: {e}")
			# Close Connection When Error
			print("An error occured!")
			client.close()
			break


def suma(message):
	arreglo = message.split(",")
	resultado= int(arreglo[0])+int(arreglo[1])
	return str(resultado)

def resta(a,b):
	return str(a-b)

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

