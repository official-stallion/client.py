import threading

from parser import *
from network import Network
from message import newMessage



"""
Client class.

manages to handler stallion clients.
"""
class Client:
    """
    constructor.

    @param url: stallion server
    """
    def __init__(self, url):
        url = self.__parse_url__(url=url)
        print(f'url: {url[0]}:{url[1]}')

        self.__net = Network(url[0], int(url[1]))
        self.__handlers = {}

        # starting the message reading
        threading.Thread(target=self.__read_data_from_server__).start()
    
    """
    parse_url.

    converts url into host and port.

    @param url: input url
    """
    def __parse_url__(self, url):
        return url.rsplit(':', 1)

    """
    read_data_from_server.

    manages to read input data from stallion server.
    """
    def __read_data_from_server__(self):
        print("start reading from server ...")
        while True:
            message = self.__net.read()
            message = jsonDecode(pickleDecode(message))
            if message['type'] == 'normal':
                data = pickleDecode(message['data'])
                self.__handlers['topic'](data)
    
    """
    Publish data over a topic.
    """
    def Publish(self, topic, data):
        bytes = bytesEncode(jsonEncode(newMessage(topic=topic, data=data)))
        self.__net.write(bytes)

    """
    Subscribe over a topic.
    """
    def Subscribe(self, topic, handler):
        self.__handlers[topic] = handler

        bytes = bytesEncode(jsonEncode(newMessage(type="subscribe", topic=topic)))
        self.__net.write(bytes)

    """
    Unsubscribe from a topic.
    """
    def Unsubscribe(self, topic):
        self.__handlers.pop(topic)

        bytes = bytesEncode(jsonEncode(newMessage(type="unsubscribe", topic=topic)))
        self.__net.write(bytes)
