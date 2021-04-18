from typing import List
from repository_navigation.RepositoryFileManager import (
    RepositoryFileManager,
    RepositoryFileManagerResult,
)


class MockRepositoryFileManager(RepositoryFileManager):
    def __init__(self):
        pass

    def list(
        self, owner: str, repo: str, path: str
    ) -> List[RepositoryFileManagerResult]:
        return [
            {"isFile": False, "name": f"{owner}/{repo}{path}/folder"},
            {"isFile": True, "name": f"{owner}/{repo}{path}/file"},
        ]

    def getFile(self, owner: str, repo: str, path: str) -> str:
        return f"{owner}/{repo}{path}"
