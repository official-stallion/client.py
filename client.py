import imp
from parser import *
from network import Network



class Client:
    def __init__(self):
        self.net = Network("127.0.0.1", "7025")
    
    def Publish(self, topic, data):
        pass

    def Subscribe(self, topic, handler):
        pass

    def Unsubscribe(self, topic):
        pass
