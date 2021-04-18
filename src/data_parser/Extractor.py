from typing import Any


class Extractor:
    """Abstract and base class for Extractor-type classes"""

    def __init__(self):
        raise Exception("Abstract Class. Cannot be instanciated.")

    def get(self, data: Any, key: str) -> Any:
        raise Exception("Method not implemented")
