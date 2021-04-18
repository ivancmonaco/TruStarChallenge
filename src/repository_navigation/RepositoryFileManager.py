from typing import List, TypedDict

RepositoryFileManagerResult = TypedDict(
    "RepositoryFileManagerResult", {"isFile": bool, "name": str}
)


class RepositoryFileManager:
    """Abstract and base class for Repository File Manager-type classes"""

    def __init__(self):
        raise Exception("Abstract Class. Cannot be instantiated.")

    def list(
        self, owner: str, repo: str, path: str
    ) -> List[RepositoryFileManagerResult]:
        raise Exception("Method not implemented.")

    def getFile(self, owner: str, repo: str, path: str) -> str:
        raise Exception("Method not implemented")
