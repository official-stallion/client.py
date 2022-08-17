import imp
import json

from message import Message



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

@param object: json dictionary
@return Message: converted message
"""
def JsonDecode(ocject) -> Message:
    m = Message(object['type'])
    m.setTopic(object['topic'])
    m.setData(object['data'])
