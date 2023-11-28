import socket
import threading

# Connection Data
host = "localhost"
port = 50000

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Lists For Clients and Their Nicknames
clients = []
nicknames = []

# Sending Messages To All Connected Clients
def broadcast(message):
	for client in clients:
		client.send(message)

def ordenes(orden):
	clients[0].send(orden.encode('ascii'))

def respuesta(orden):
	clients[1].send(orden.encode('ascii'))

# Handling Messages From Clients
def handle(client):
	while True:
		try:
            # Broadcasting Messages
			message = client.recv(1024)
			intento=message.decode('ascii')
			usuario=intento.split(":")
			if usuario[0]=="luis":
				ordenes(usuario[1])
				#print("aqui1",usuario[1])
				respuesta("Enviado")
			elif usuario[0]=="Robot":
				#print("aqui2",usuario[1])
				respuesta(usuario[1])
			else:
				pass
			#broadcast(message)
		except:
			# Removing And Closing Clients
			index = clients.index(client)
			clients.remove(client)
			client.close()
			nickname = nicknames[index]
			broadcast('{} left!'.format(nickname).encode('ascii'))
			nicknames.remove(nickname)
			break

def receive():
	while True:
        # Accept Connection
		client, address = server.accept()
		print("Connected with {}".format(str(address)))

        # Request And Store Nickname
		client.send('NICK'.encode('ascii'))
		nickname = client.recv(1024).decode('ascii')
		nicknames.append(nickname)
		clients.append(client)

        # Print And Broadcast Nickname
		print("Nickname is {}".format(nickname))
		broadcast("{} joined!".format(nickname).encode('ascii'))
		client.send('Connected to server!'.encode('ascii'))

        # Start Handling Thread For Client
		thread = threading.Thread(target=handle, args=(client,))
		thread.start()

receive()