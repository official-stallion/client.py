import re
from parser import JsonDecode, JsonEncode
from message import Message


m = Message("subscribe")
m.setTopic("My topic")

res = JsonEncode(m)

print(res)

print(JsonDecode(res))
