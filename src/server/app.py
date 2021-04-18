import sys
import os
from flask import Flask

app = Flask(__name__)


def startServer(dev: bool = False):
    if not dev:
        return app
    app.run(
        host=os.environ.get("HOST", "localhost"),
        port=os.environ.get("PORT", 4000),
        debug=dev,
    )
