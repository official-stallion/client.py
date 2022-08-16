import json



"""
JsonEncode.

converts an object to json.

@param object: interface
@return str: json object
"""
def JsonEncode(object) -> str:
    return json.dumps(object.__dict__)