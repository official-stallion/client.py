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
        try:
            self.__connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__connection.connect((host, port))
        except:
            print("connection failed")

    """
    read method.
    """
    def read(self):
        return self.__connection.recv(2048)

    """
    write method.
    """
    def write(self, data):
        self.__connection.send(data.encode())
