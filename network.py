import socket 



"""
Network manages the client requests over TCP connection.
"""
class Network:
    """
    class constructor.
    @param host: server url
    @param port: server port
    """
    def __init__(self, host, port):
        self.__connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))

    """
    read method.
    """
    def read(self):
        return self.__connection.recv(1024)

    """
    write method.
    """
    def write(self, data):
        self.__connection.sendall(data)
