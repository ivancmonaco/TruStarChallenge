from flask import request
from server.app import app
from typing import List, Dict, Any
import json
from services.mitre import getMalwareRecords


@app.route("/mitre", methods=["POST"])
def mitrePostRoute():

    data: Dict[str, Any] = json.loads(request.data or json.dumps({}))
    keys: List[str] = data.get("keys", [])
    path: str = data.get("path", "/")

    response = getMalwareRecords(path, keys)

    return json.dumps({"data": response})
