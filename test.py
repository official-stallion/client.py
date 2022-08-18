from time import sleep
from client import Client



def handler(data):
    print(data)


if __name__ == "__main__":
    c = Client(url="localhost:9090")
    c.Subscribe("book", handler)

    sleep(2)

    c.Publish("book", "new book")
    sleep(2)
    
