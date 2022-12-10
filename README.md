<h1 align="center">
Stallion Python SDK
</h1>

<br />

<p align="center">
<img src="https://img.shields.io/badge/Python-3.21-blue?style=for-the-badge&logo=python" alt="go version" />
<img src="https://img.shields.io/badge/Version-1.2.1-2255DD?style=for-the-badge&logo=github" alt="version" /><br />
<img src="https://img.shields.io/badge/MacOS-black?style=for-the-badge&logo=apple" alt="version" />
<img src="https://img.shields.io/badge/Linux-white?style=for-the-badge&logo=linux" alt="version" />
<img src="https://img.shields.io/badge/Windows-blue?style=for-the-badge&logo=windows" alt="version" /><br /><br />
Client SDK for Stallion message broker
</p>

## How to use?
Python install:
```shell
pip install stallion-python-sdk
```

### Client
Create a client:
```python
# importing Client module
from stallion import Client

# creating a client
# with given stallion server url
c = Client(url="st://localhost:9090")
```

### Publish
```python
# publish an object on a topic
c.Publish("book", {'author': "Amirhossein", 'name': "Stallion"})
```

### Subscribe
```python
# creating a handler
# any published object will be given to this handler as data
def handler(data):
    print(f'{data['author']}: {data['name']})

# subscribe over a topic with given handler
c.Subscribe("book", handler)
```

### Unsubscribe
```python
# unsubscribe from a topic
c.Unsubscribe("book")
```
