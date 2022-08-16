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
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection = s.connect((host, port))

    def read():
        pass

    def write():
        pass
