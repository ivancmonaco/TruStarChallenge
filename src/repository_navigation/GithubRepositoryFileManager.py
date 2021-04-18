from typing import List
from repository_navigation.RepositoryFileManager import (
    RepositoryFileManager,
    RepositoryFileManagerResult,
)
import requests


class GithubRepositoryFileManager(RepositoryFileManager):
    """File Manager Class, capable of navigating through a GitHub repository"""

    # TODO Add Caching Layer

    def __init__(self):
        pass

    def list(
        self, owner: str, repo: str, path: str = ""
    ) -> List[RepositoryFileManagerResult]:
        """
        Returns a representation of the given GitHub repo.

        #Parameters
        #   owner: a GitHub repository owner ( user | org )
        #   repo: a GitHub repo name associated to the owner
        #   path: a path from the root of the repository.

        #Returns
        #   A list of the folders and files represented as objects.
        """
        response = requests.get(
            f"https://api.github.com/repos/{owner}/{repo}/contents{path}"
        )
        if not response.ok:
            raise Exception(response.text)
        return list(
            map(
                lambda x: {"isFile": x["download_url"] is not None, "name": x["name"]},
                response.json(),
            )
        )

    def getFile(self, owner: str, repo: str, path: str) -> str:
        """
        Get a file hosted in a GitHub repository

        #Parameters
        #   owner: a GitHub repository owner ( user | org )
        #   repo: a GitHub repo name associated to the owner
        #   path: a path from the root of the repository.

        #Returns
        #   A string or None if file is not found
        """
        response = requests.get(
            f"https://raw.githubusercontent.com/{owner}/{repo}/master{path}"
        )
        if not response.ok:
            raise Exception(response.text)
        return response.text
