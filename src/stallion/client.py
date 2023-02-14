import threading
from time import sleep

from stallion.stringparser import *
from stallion.network import Network
from stallion.message import newMessage



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
            message = jsonDecode(message.decode('utf-8'))
            if message['type'] == 1:
                data = pickleDecode(message['data'])
                self.__handlers[message['topic']](data)
    
    """
    Publish data over a topic.
    """
    def Publish(self, topic, data):
        self.__net.write(jsonEncode(newMessage(topic=topic, data=data)))

        sleep(0.001)

    """
    Subscribe over a topic.
    """
    def Subscribe(self, topic, handler):
        self.__handlers[topic] = handler
        self.__net.write(jsonEncode(newMessage(type=2, topic=topic)))
        
        sleep(0.001)

    """
    Unsubscribe from a topic.
    """
    def Unsubscribe(self, topic):
        self.__handlers.pop(topic)
        self.__net.write(jsonEncode(newMessage(type=3, topic=topic)))

        sleep(0.001)
