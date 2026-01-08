import socket
from config.settings import HOST, PORT
from socket_.router import handle_request


def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)

    print(f"Server ishga tushdi: http://{HOST}:{PORT}")

    while True:
        client_socket, addr = s.accept()
        request = client_socket.recv(8192)
        response = handle_request(request)

        client_socket.sendall(response.encode())
        client_socket.close()
