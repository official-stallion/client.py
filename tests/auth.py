from stallion.client import Client



"""
creating a handler.
"""
def handler(data):
    print(data)


if __name__ == "__main__":
    # create client
    c = Client(url="st://root:Pa$$word@localhost:9090")

    # subscribe over a topic
    c.Subscribe("book", handler)

    # publish messages over a topic
    c.Publish("book", {'author': "Amirhossein", 'name': "Stallion"})

    # unsubscribe
    c.Unsubscribe("book")
