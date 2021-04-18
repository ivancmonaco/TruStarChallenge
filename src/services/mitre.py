from typing import List, Dict, Any
from data_parser.DataParser import DataParser
from threading import Thread
from data_parser.JSONStringExtractor import JSONStringExtractor
from repository_navigation.RepositoryNavigator import RepositoryNavigator
from repository_navigation.GithubRepositoryFileManager import (
    GithubRepositoryFileManager,
)


def getMalwareRecords(path: str, keys: List[str]) -> List[Dict[str, Any]]:
    """Returns an object with the found key-values of all the JSON files found in the path given,
    taking the mitre/cti repository as root"""

    owner = "mitre"
    repo = "cti"

    repository = RepositoryNavigator(owner, repo, GithubRepositoryFileManager())

    files = repository.listRepository(path)
    files = list(filter(lambda f: f["isFile"] == True, files))
    files = list(filter(lambda f: ".json" in f["name"], files))

    threads: List[Thread] = []
    response: List[Dict[str, Any]] = []

    def parseFile(filename: str):
        file_content = repository.getFileFromRepository(f"{path}/{filename}")
        parser = DataParser(file_content, JSONStringExtractor())
        response.append(parser.parse(keys))

    for f in files:
        filename = f["name"]
        t = Thread(target=parseFile, args=(filename,))
        threads.append(t)

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    return response
