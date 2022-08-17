import pickle

from message import Message



"""
Encode.

converts an object to json.

@param object: interface
@return str: json object
"""
def Encode(object) -> str:
    return pickle.dumps(object)


"""
Decode.

converts a json object to Message type.

@param object: json string
@return Message: converted message
"""
def Decode(object) -> Message:
    return pickle.loads(object)
