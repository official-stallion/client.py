from parser import JsonDecode, JsonEncode, PickleDecode
from message import Message


m = Message("subscribe")
m.setTopic("My topic")
m.setData("Data")

res = JsonEncode(m)

print(res)

dec = JsonDecode(res)

obj = PickleDecode(dec['data'])
print(obj)