from time import sleep
from client import Client



def handler(data):
    print(data)


if __name__ == "__main__":
    c = Client(url="localhost:9090")
    sleep(1)
    c.Subscribe("book", handler)
    sleep(1)
    c.Publish("book", {'a': 'a', 'b': 'b'})
    # c.Publish("book", "new book")
