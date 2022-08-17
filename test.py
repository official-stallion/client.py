from parser import Decode, Encode
from message import Message


m = Message("subscribe")
m.setTopic("My topic")
m.setData("Data")

res = Encode(m)

print(res)

print(Decode(res))
