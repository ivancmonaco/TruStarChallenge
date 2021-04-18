from server.app import startServer
from routes import *


def start():
    return startServer()


if __name__ == "__main__":
    startServer(True)
