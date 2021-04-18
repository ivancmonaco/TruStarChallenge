#!/usr/bin/env python3
import re
from data_parser.Extractor import Extractor
from typing import Any, Dict, List, Union


class JSONExtractor(Extractor):
    """Extractor class capable of parsing JSON objects"""

    def __init__(self):
        return

    def get(self, data: Any, key: str) -> Any:
        """
        Returns the given value associated with a key
        from a JSON object, in a key - value format.

        #Parameters
        #   data: A JSON object
        #   key: A string key

        #Returns
        #   Any value or None if key is invalid
        """
        return self._get(data, key)

    def _get(self, data: Dict[str, Any], key: str) -> Dict[str, Any]:
        keys = key.split(".")
        key = keys[0]
        value = self._getValue(data, key)
        if len(keys) == 1:
            return value
        return self._get(value, ".".join(keys[1:]))

    def _parseArray(self, array: List[Any], idxs: List[int]) -> Any:
        if len(idxs) == 0:
            return array
        idx = idxs[0]
        if len(idxs) == 1:
            try:
                return array[int(idx)]
            except IndexError:
                return None
        return self._parseArray(array[int(idx)], idxs[1:])

    def _getValue(self, data: Dict[str, Any], key: str) -> Any:
        if type(data) is not dict:
            return None
        idxs = re.findall("\[(.*?)\]", key)
        key = key.replace("".join(map(lambda x: f"[{x}]", idxs)), "")
        value = data.get(key, None)
        if type(value) is list:
            try:
                return self._parseArray(value, list(map(lambda i: int(i), idxs)))
            except ValueError:
                return None
        return value
