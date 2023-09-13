#--------------------IMPORT--------------------#
"""
Import the test unit (which is similar to JUnit).
Import the jsonapi to test its functionality, specifically dumps and loads.
"""
import unittest
from jsonapi import dumps, loads

#--------------------CLASS--------------------#
class TestJSONAPI(unittest.TestCase):
    """
    Encode complex number (1 and 2, based on 1 + 2j from class example).
    Encodes testNumbers and dumps the data, checks if value is true from encoded.
    """
    def test_encode_complex(self):
        test_numbers = {"complex_number": complex(1, 2)}
        encoded = dumps(test_numbers)
        self.assertTrue('"__extended_json_type__": "complex"', encoded)

    """
    Decode complex number (1 and 2, based on 1 + 2j from class example).
    Decode testNumbersEncoded and loads the data, checks if the instance exists.
    """
    def test_decode_complex(self):
        test_numbers_encoded = '{"complex_number": {"__extended_json_type__": "complex", "real": 1.0, "imag": 2.0}}'
        decode = loads(test_numbers_encoded)
        self.assertIsInstance(decode["complex_number"], complex)

    """
    Encode a range of numbers given three arguments (start, stop, step).
    Encode range_data and dumps the data, checks if the expression contains the arguments from encoded. 
    """
    def test_encode_range(self):
        range_date = {"range_data": range(7, 700, 14)}
        encoded = dumps(range_date)
        self.assertTrue('"__extended_json_type__": "range"', encoded)

    """
    Decode a range of numbers given three arguments (start, stop, step).
    Decode range_data and dumps the data, checks if the expression contains the arguments from encoded.
    """
    def test_decode_range(self):
        test_numbers_encoded = '{"range_data": {"__extended_json_type__": "range", "start": 7, "stop": 700, "step": 14}}'
        decoded = loads(test_numbers_encoded)
        self.assertIsInstance(decoded["range_data"], range)

#I am not sure this is the correct way to test, modeled this after java testing since this is similar to intelliJ.