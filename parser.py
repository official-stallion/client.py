import json



"""
Encode.

converts an object to json.

@param object: interface
@return str: json object
"""
def Encode(object) -> str:
    return json.dumps(object.__dict__)


"""
Decode.

converts a json object to Message type.

@param object: json string
@return Message: converted message
"""
def Decode(object) -> dict:
    return json.loads(object)
