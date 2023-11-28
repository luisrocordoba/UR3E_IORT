import socket

HOST = "192.168.100.44"
PORT = 50000
#myip.is
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send(f"Hello World".encode("utf-8"))
print(socket.recv(1024).decode('utf-8'))