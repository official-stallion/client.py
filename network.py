import socket 

HOST = "127.0.0.1"
PORT = 7025

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
    connection.connect((HOST, PORT))
    connection.sendall(b"message")

