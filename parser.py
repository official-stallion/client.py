import base64
import json
import pickle



"""
JsonEncode.

converts an object to json.

@param object: interface
@return str: json object
"""
def JsonEncode(object) -> str:
    return json.dumps(object.__dict__)


"""
JsonDecode.

converts a json object to Message type.

@param object: json string
@return Message: converted message
"""
def JsonDecode(string) -> dict:
    return json.loads(string)


"""
PickleEncode.

converts an object to string of bytes.

@param object: any interface
@return str: string of bytes
"""
def PickleEncode(object) -> str:
    return base64.b64encode(pickle.dumps(object)).decode('ascii')


"""
PickleDecode.

converts bytes to any object.

@param bytes: string of bytes
@return interface
"""
def PickleDecode(bytes):
    return pickle.loads(base64.b64decode(bytes))
