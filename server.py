import socket
import select

HEADER_LENGHT = 10
IP = "127.0.0.1"
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))
server_socket.listen()

socket_list = [server_socket]

client = {}

def receive_message(cliente_socket):
    try:
        message_header = cliente_socket.recv(HEADER_LENGHT)

        if not len(message_header):
            return False

        message_length = int(message_header.decode("utf-8").strip())
        return {"header": message_header, "data": cliente_socket.recv(message_length)}


    except:
        return False

while True:
    read_sockets, _, exception_sockets = select.select(socket_list, [], socket_list)

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()

            user = receive_message(client_socket)
            if user is False:
                continue

            socket_list.append(client_socket)

            client[client_socket] = user

            print(f"Accepted new connection from {client_address[0]}:{client_address[1]} username:{user['data'].decode('utf-8')}")

        else:
            message = receive_message(notified_socket)

            if message is False:
                print(f"Closed connection from {client[notified_socket]['data'].decode('utf-8')}")
                socket_list.remove(notified_socket)
                del client[notified_socket]
                continue

            user = client[notified_socket]
            print(f"Received message from {user['data'].decode['utf-8']}: {message['data'].decode['utf-8']}")

            for client_socket in client:
                if client_socket != notified_socket:
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

    for notified_socket in exception_sockets:
        socket_list.remove(notified_socket)
        del client[notified_socket]
