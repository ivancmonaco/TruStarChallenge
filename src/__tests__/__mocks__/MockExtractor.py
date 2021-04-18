from typing import Any
from data_parser.Extractor import Extractor


class MockExtractor(Extractor):
    def __init__(self):
        pass

    def get(self, data: Any, key: str) -> Any:
        return data.get(key, None)
