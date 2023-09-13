#--------------------IMPORT--------------------#
import json

#--------------------CLASS--------------------#
"""
Subclass, json.JSONEncoder
"""
class JSONEncoder(json.JSONEncoder):
    def default(self, default_object):
        name = type(default_object).__name__
        try:
            encoder_function = getattr(self, f"encode_{name}")
        except AttributeError:
            return super().default(default_object)
        else:
            encoded = encoder_function(default_object)
            encoded["__extended_json_type__"] = name
            return encoded

    def encode_complex(self, encode_complex_object):
        return {"real": encode_complex_object.real, "imag": encode_complex_object.imag}

    def encode_range(self, encode_range_object):
        return {"start": encode_range_object.start, "stop": encode_range_object.stop, "step": encode_range_object.step}

"""
Subclass, json.JSONDecoder
"""
class JSONDecoder(json.JSONDecoder):
    def __init__(self, **kwargs):
        kwargs["object_hook"] = self.object_hook
        super().__init__(**kwargs)

    def object_hook(self, hook_object):
        try:
            name = hook_object["__extended_json_type__"]
            decode = getattr(self, f"decode_{name}")
        except (KeyError, AttributeError):
            return hook_object
        else:
            return decode(hook_object)

    def decode_complex(self, decode_complex_object):
        return complex(decode_complex_object["real"], decode_complex_object["imag"])

    def decode_range(self, decode_range_object):
        return range(decode_range_object["start"], decode_range_object["stop"], decode_range_object["step"])

#--------------------FUNCTION--------------------#
"""
Function named dumps that serves as a wrapper around the json.dumps function
"""
def dumps(dumps_object):
    return json.dumps(dumps_object, cls=JSONEncoder)

"""
A function named loads that serves as a wrapper around the json.loads function
"""
def loads(loads_object):
    return json.loads(loads_object, cls=JSONDecoder)