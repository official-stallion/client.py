import base64
import pickle
from parser import Decode, Encode
from message import Message


m = Message("subscribe")
m.setTopic("My topic")
m.setData("Data")

res = Encode(m)

print(res)

dec = Decode(res)

obj = pickle.loads(base64.b64decode(dec['data']))
print(obj)