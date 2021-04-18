from typing import List, Dict, Any, List
from repository_navigation.RepositoryFileManager import (
    RepositoryFileManager,
    RepositoryFileManagerResult,
)
from data_parser.DataParser import DataParser
from data_parser.JSONStringExtractor import JSONStringExtractor
import requests


class RepositoryNavigator:
    """Class capable of navigating through any git-based repository"""

    def __init__(self, owner: str, repo: str, file_manager: RepositoryFileManager):
        """
        Constructor method

        #Parameters
        #   owner: a git repository user
        #   repo: a git repository name
        #   file_manager: A RepositoryFileManager instance

        """
        self._owner = owner
        self._repo = repo
        self._file_manager = file_manager

    def listRepository(self, path: str) -> List[RepositoryFileManagerResult]:
        """
        Returns a representation of the given repository.

        #Parameters
        #   path: a path from the root of the repository.

        #Returns
        #   A list of the folders and files represented as objects.
        """
        return self._file_manager.list(self._owner, self._repo, path)

    def getFileFromRepository(self, path: str) -> str:
        """
        Get a file hosted in the given repository

        #Parameters
        #   path: a path from the root of the repository.

        #Returns
        #   A string or None if file is not found
        """
        return self._file_manager.getFile(self._owner, self._repo, path)
