from typing import Dict, Any
import json


class MockHTTPResponse:
    def __init__(self, status: int, text: str):
        self.status = status
        self.ok = self.status >= 200 and self.status < 400
        self.text = text

    def json(self) -> Dict[str, Any]:
        return json.loads(self.text)
