from time import sleep
from client import Client



def handler(data):
    print(data)


if __name__ == "__main__":
    c = Client(url="localhost:9090")
    c.Subscribe("book", handler)
    c.Publish("book", "new book")
    c.Publish("book", "new book")
