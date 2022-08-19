import base64
import json
import pickle



"""
jsonEncode.

converts an object to json.

@param object: interface
@return str: json object
"""
def jsonEncode(object) -> str:
    return json.dumps(object.__dict__)


"""
jsonDecode.

converts a json object to Message type.

@param object: json string
@return Message: converted message
"""
def jsonDecode(string) -> dict:
    return json.loads(string)


"""
pickleEncode.

converts an object to string of bytes.

@param object: any interface
@return str: string of bytes
"""
def pickleEncode(object) -> str:
    return base64.b64encode(pickle.dumps(object)).decode('ascii')


"""
pickleDecode.

converts bytes to any object.

@param bytes: string of bytes
@return interface
"""
def pickleDecode(string):
    return pickle.loads(base64.b64decode(string))
