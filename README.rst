# Stallion Python SDK

Client SDK for **Stallion** message broker.

## How to use?
### Client
Create a client:
```python
from client import Client

c = Client(url="localhost:9090")
```

### Publish
```python
c.Publish("book", {'author': "Amirhossein", 'name': "Stallion"})
```

### Subscribe
```python
def handler(data):
    print(data)

c.Subscribe("book", handler)
```

### Unsubscribe
```python
c.Unsubscribe("book")
```
