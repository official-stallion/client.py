from parser import *
from network import Network
from message import newMessage



class Client:
    def __init__(self):
        self.__net = Network("127.0.0.1", "7025")
        self.__handlers = {}
        self.__readDataFromServer()

    def __readDataFromServer(self):
        pass
    
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
