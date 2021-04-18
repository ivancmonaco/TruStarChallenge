from typing import Any, List, Dict

from data_parser.Extractor import Extractor


class DataParser:
    """Parser class to serialize and extract information from generic data"""

    def __init__(self, data: Any, extractor: Extractor):
        """
        Constructor method

        #Parameters
        #   data: Any piece of data ( eg. a JSON object)
        #   extractor: An instance of an Extractor class

        """
        self._data = data
        self._extractor = extractor

    def parse(self, keys: List[str]):
        """
        Parse the data from a list of keys

        #Parameters
        #   keys: A list of strings, which represents keys passed to
                  the extractor
        #Returns
        #   An key - value object, with the given data for each key.
        """
        values = {}
        for key in keys:
            value = self._extractor.get(self._data, key)
            if value:
                values[key] = value
        return values
