server.py

import socket #biblioteca padrão no python 
# criar um soquete INET, STREAMing
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #definindo um objeto socket 
# vincularndo o socket a um host 
s.bind((socket.gethostname(), 1234))
# tornando um socket de servidor
s.listen(5)

while True:
	clientsocket, address = s.accept()
	print(f"Conexão a partir de {address} foi estabelecida!")
	clientsocket.send(bytes("Bem-vindos ao server!", "utf-8"))
