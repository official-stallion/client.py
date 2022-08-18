from parser import *
from network import Network
from message import newMessage



class Client:
    def __init__(self, url):
        url = self.__parse_url__(url=url)
        self.__net = Network(url[0], url[1])
        self.__handlers = {}
        
        self.__readDataFromServer()
    
    def __parse_url__(self, url):
        return url.rsplit(':', 1)

    def __readDataFromServer__(self):
        while True:
            message = self.__net.read()
            message = jsonDecode(pickleDecode(message))
            if message['type'] == 'normal':
                data = pickleDecode(message['data'])
                self.__handlers['topic'](data)
    
    def Publish(self, topic, data):
        bytes = pickleEncode(jsonEncode(newMessage(topic=topic, data=data)))
        self.__net.write(bytes)

    def Subscribe(self, topic, handler):
        self.__handlers[topic] = handler

        bytes = pickleEncode(jsonEncode(newMessage(type="subscribe", topic=topic)))
        self.__net.write(bytes)

    def Unsubscribe(self, topic):
        self.__handlers.pop(topic)

        bytes = pickleEncode(jsonEncode(newMessage(type="unsubscribe", topic=topic)))
        self.__net.write(bytes)
