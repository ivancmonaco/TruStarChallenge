import re
from typing import Any
from data_parser.JSONExtractor import JSONExtractor
import json


class JSONStringExtractor(JSONExtractor):
    """Extractor class capable of parsing stringified JSON objects"""

    def __init__(self):
        return

    def get(self, data: Any, key: str):
        """
        Returns the given value associated with a key
        from a stringified JSON object.

        #Parameters
        #   data: A stringified JSON object
        #   key: A string key

        #Returns
        #   Any value or None if key is invalid
        """
        return super().get(json.loads(data), key)
