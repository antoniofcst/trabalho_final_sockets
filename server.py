server.py

import socket #biblioteca padrão no python 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #definindo um objeto socket 
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
	clientsocket, address = s.accept()
	print(f"Conexão a partir de {address} foi estabelecida!")
	clientsocket.send(bytes("Bem-vindos ao server!", "utf-8"))
	