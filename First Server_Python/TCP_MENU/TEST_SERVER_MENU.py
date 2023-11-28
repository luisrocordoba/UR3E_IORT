import socket
import threading

# Connection Data
host = "192.168.100.44"
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
			message_decoded=message.decode('ascii')
			user=message_decoded.split(":")
			if user[0]=="user1":
				ordenes(user[1])
				respuesta("Enviado")
			elif user[0]=="menu":
				respuesta(user[1])
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