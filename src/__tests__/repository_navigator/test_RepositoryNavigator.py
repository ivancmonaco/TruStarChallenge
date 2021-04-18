import unittest
from typing import Dict, Any, List
from repository_navigation.RepositoryFileManager import (
    RepositoryFileManager,
    RepositoryFileManagerResult,
)
from repository_navigation.RepositoryNavigator import RepositoryNavigator
from __tests__.__mocks__.MockRepositoryFileManager import MockRepositoryFileManager


class TestRepositoryNavigator(unittest.TestCase):
    def test_list_dir(self):
        navigator = RepositoryNavigator("owner", "repo", MockRepositoryFileManager())
        response = navigator.listRepository("/path")
        expect = [
            {"isFile": False, "name": "owner/repo/path/folder"},
            {"isFile": True, "name": "owner/repo/path/file"},
        ]
        self.assertEqual(
            response,
            expect,
            "It should should return an array with all the folders and files from the repository",
        )

    def test_get_file(self):
        navigator = RepositoryNavigator("owner", "repo", MockRepositoryFileManager())
        response = navigator.getFileFromRepository("/folder/file")
        expect = "owner/repo/folder/file"
        self.assertEqual(response, expect)
