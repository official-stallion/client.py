<h1 align="center">
Stallion Python SDK
</h1>

<p align="center">
<img src="https://img.shields.io/badge/Python-3.21-blue?style=for-the-badge&logo=python" alt="go version" />
<img src="https://img.shields.io/badge/Version-1.1-2255DD?style=for-the-badge&logo=none" alt="version" /><br />
<img src="https://img.shields.io/badge/MacOS-black?style=for-the-badge&logo=apple" alt="version" />
<img src="https://img.shields.io/badge/Linux-white?style=for-the-badge&logo=linux" alt="version" />
<img src="https://img.shields.io/badge/Windows-blue?style=for-the-badge&logo=windows" alt="version" />
</p>

Client SDK for **Stallion** message broker.

## How to use?
Python install:
```shell
pip install stallion-python-sdk
```

### Client
Create a client:
```python
from stallion_python_sdk import Client

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
