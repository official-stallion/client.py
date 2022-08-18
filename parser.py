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
    return base64.b64encode(bytesEncode(object=object)).decode('ascii')


"""
pickleDecode.

converts bytes to any object.

@param bytes: string of bytes
@return interface
"""
def pickleDecode(bytes):
    return bytesDecode(bytes=base64.b64decode(bytes))


"""
bytesEncode.

convert object to array of bytes.
"""
def bytesEncode(object):
    return base64.b64encode(pickle.dumps(object))


"""
bytesDecode.

convert array of bytes to an object.
"""
def bytesDecode(bytes):
    return pickle.loads(bytes)
