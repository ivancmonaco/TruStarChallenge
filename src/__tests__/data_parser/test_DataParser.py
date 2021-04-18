import unittest
from typing import Dict, Any
from data_parser.Extractor import Extractor
from data_parser.DataParser import DataParser
from __tests__.__mocks__.MockExtractor import MockExtractor

data = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
}


class TestDataParser(unittest.TestCase):
    def test_parse(self):
        parser = DataParser(data, MockExtractor())
        keys = ["a", "c", "e"]
        response = parser.parse(keys)
        expect = {"a": data["a"], "c": data["c"]}
        self.assertEqual(response, expect, "It should return a key-value dict.")

    def test_parse_empty_keys(self):
        parser = DataParser(data, MockExtractor())
        response = parser.parse([])
        expect = {}
        self.assertEqual(response, expect, "It should return an empty dict")

    def test_parse_empty_data(self):
        data = {}
        parser = DataParser(data, MockExtractor())
        keys = ["a", "c", "e"]
        response = parser.parse(keys)
        expect = {}
        self.assertEqual(response, expect, "It should return an empty dict")
