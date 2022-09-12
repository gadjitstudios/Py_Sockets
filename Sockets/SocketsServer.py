import socket

HOST = XXX.XXX.XXX.XXX
PORT = XXXXX

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    connection, address = s.accept()
    with connection:
        print('Connected to', address)
        while True:
            data = connection.recv(1024)
            if not data:
                break
            connection.sendall(data)
