import unittest
from typing import Dict, Any
from data_parser.JSONExtractor import JSONExtractor

data = {
    "guid": "1234",
    "array": [0, 1, 2, 3, {"nested": [{"even_more_nested": 100}]}],
    "content": {
        "type": "text/html",
        "title": "Challenge 1",
        "entities": ["1.2.3.4", "wannacry", "malware.com"],
    },
    "score": 74,
    "time": 1574879179,
}


class TestJSONExtractor(unittest.TestCase):
    def test_get_existent_key(self):
        extractor = JSONExtractor()
        key = "guid"
        response = extractor.get(data, key)
        expect = data[key]
        self.assertEqual(
            response, expect, "It should return the associated value to the key."
        )

    def test_get_non_existent_key(self):
        extractor = JSONExtractor()
        key = "other"
        response = extractor.get(data, key)
        expect = None
        self.assertEqual(
            response, expect, "It should return None if the key doesnt exist."
        )

    def test_get_nested_existent_key(self):
        extractor = JSONExtractor()
        key = "content.type"
        response = extractor.get(data, key)
        expect = "text/html"
        self.assertEqual(
            response,
            expect,
            "It should return the associated value to the key, even if it is nested",
        )

    def test_get_nested_non_existent_key(self):
        extractor = JSONExtractor()
        key = "content.typo"
        response = extractor.get(data, key)
        expect = None
        self.assertEqual(
            response,
            expect,
            "It should return None if the key doesnt exists, even if it is nested and previous keys exist.",
        )

    def test_get_array_existent_key(self):
        extractor = JSONExtractor()
        key = "array[2]"
        expect = 2
        response = extractor.get(data, key)
        self.assertEqual(
            response,
            expect,
            "It should return the correct element of the of array associated with the key.",
        )

    def test_get_array_non_existent_key(self):
        extractor = JSONExtractor()
        key = "array[15]"
        expect = None
        response = extractor.get(data, key)
        self.assertEqual(
            response,
            expect,
            """
        It should return None if the index doesnt exists, 
        even if previous indexes exist.
        """,
        )

    def test_get_array_invalid_key(self):
        extractor = JSONExtractor()
        key = "array[a]"
        expect = None
        response = extractor.get(data, key)
        self.assertEqual(
            response,
            expect,
            """
        It should return None if the index is invalid, 
        even if previous indexes are not.
        """,
        )

    def test_get_valid_nested(self):
        extractor = JSONExtractor()
        key = "array[4].nested[0].even_more_nested"
        expect = 100
        response = extractor.get(data, key)
        self.assertEqual(
            response,
            expect,
            """
        It should return the correct value,
        associated with the key and index, 
        even if it is nested.
        """,
        )

    def test_get_nested_invalid_index(self):
        extractor = JSONExtractor()
        key = "array[4].nested[1].even_more_nested"
        expect = None
        response = extractor.get(data, key)
        self.assertEqual(
            response,
            expect,
            """
        It should return None if the index is invalid, 
        even if previous indexes  are not.
        """,
        )

    def test_get_nested_invalid_key(self):
        extractor = JSONExtractor()
        key = "array[4].nestod[0].even_more_nested"
        expect = None
        response = extractor.get(data, key)
        self.assertEqual(
            response,
            expect,
            """
        It should return None if the key is invalid, 
        even if previous keys are not.
        """,
        )
