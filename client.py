import imp
from parser import *
from network import Network



class Client:
    def __init__(self):
        self.net = Network("127.0.0.1", "7025")
