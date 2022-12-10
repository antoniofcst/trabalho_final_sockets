client.py

import socket #biblioteca padrão no python 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #definindo um objeto socket 
s.connect((socket.gethostname(), 1234))

msg = s.recv(1024)
print(msg.decode("utf-8"))