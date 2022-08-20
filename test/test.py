from time import sleep
from stallionSdk import Client



"""
creating a handler.
"""
def handler(data):
    print(data)


if __name__ == "__main__":
    # create client
    c = Client(url="localhost:9090")

    sleep(1)

    # subscribe over a topic
    c.Subscribe("book", handler)

    sleep(1)

    # publish messages over a topic
    c.Publish("book", {'author': "Amirhossein", 'name': "Stallion"})

    # unsubscribe
    c.Unsubscribe("book")
