# Py-Rc4
Simple implementation of [RC4](https://en.wikipedia.org/wiki/RC4)

## Setup

Install the library:
```
pip install git+https://github.com/itasahobby/py-rc4.git
```

## Basic sample
```python
from rc4 import Rc4

rc4_client = Rc4(key=bytearray.fromhex("deadbeef"))
rc4_server = Rc4(key=bytearray.fromhex("deadbeef"))

rc4_server.decrypt(rc4_client.encrypt("sample text".encode())).decode()
```
