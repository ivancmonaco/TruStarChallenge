import unittest
from typing import Dict, Any
from unittest.mock import MagicMock
from repository_navigation.GithubRepositoryFileManager import (
    GithubRepositoryFileManager,
)
import requests
import json
from __tests__.__mocks__.MockHTTPResponse import MockHTTPResponse


repo_structure = [
    {
        "download_url": "http0...",
        "name": "file_0.json",
    },
    {
        "download_url": "http1...",
        "name": "file_1.json",
    },
    {
        "download_url": "http2...",
        "name": "file_2.json",
    },
    {
        "download_url": None,
        "name": "folder",
    },
]


class TestGithubRepositoryFileManager(unittest.TestCase):
    def test_list_dir_successful(self):
        mock_response = MockHTTPResponse(200, json.dumps(repo_structure))
        requests.get = MagicMock(return_value=mock_response)
        file_manager = GithubRepositoryFileManager()
        response = file_manager.list("", "", "")
        expect = [
            {"isFile": True, "name": "file_0.json"},
            {"isFile": True, "name": "file_1.json"},
            {"isFile": True, "name": "file_2.json"},
            {"isFile": False, "name": "folder"},
        ]
        self.assertEqual(
            response, expect, "It should return a file manager result dict type"
        )

    def test_list_empty_dir_successful(self):
        mock_response = MockHTTPResponse(200, json.dumps({}))
        requests.get = MagicMock(return_value=mock_response)
        file_manager = GithubRepositoryFileManager()
        response = file_manager.list("", "", "")
        expect = []
        self.assertEqual(response, expect, "It should return en empty dict.")

    def test_list_dir_not_found(self):
        mock_response = MockHTTPResponse(404, json.dumps({}))
        requests.get = MagicMock(return_value=mock_response)
        file_manager = GithubRepositoryFileManager()
        with self.assertRaises(Exception):
            file_manager.list("", "", "")

    def test_list_call_with_args(self):
        args = ("owner", "repo", "/path")
        mock_response = MockHTTPResponse(200, json.dumps({}))
        requests.get = MagicMock(return_value=mock_response)
        file_manager = GithubRepositoryFileManager()
        response = file_manager.list(*args)
        expected_url = (
            f"https://api.github.com/repos/{args[0]}/{args[1]}/contents{args[2]}"
        )
        requests.get.assert_called_with(expected_url)

    def test_get_file_successful(self):
        file_ = {"name": "filename"}
        mock_response = MockHTTPResponse(200, json.dumps(file_))
        requests.get = MagicMock(return_value=mock_response)
        file_manager = GithubRepositoryFileManager()
        response = file_manager.getFile("", "", "")
        expect = json.dumps(file_)
        self.assertEqual(
            response, expect, "It should return file content in txt format"
        )

    def test_get_file_not_found(self):
        mock_response = MockHTTPResponse(404, json.dumps({}))
        requests.get = MagicMock(return_value=mock_response)
        file_manager = GithubRepositoryFileManager()
        with self.assertRaises(Exception):
            file_manager.getFile("", "", "")

    def test_get_file_call_with_args(self):
        args = ("owner", "repo", "/path")
        mock_response = MockHTTPResponse(200, json.dumps({}))
        requests.get = MagicMock(return_value=mock_response)
        file_manager = GithubRepositoryFileManager()
        response = file_manager.getFile(*args)
        expected_url = (
            f"https://raw.githubusercontent.com/{args[0]}/{args[1]}/master{args[2]}"
        )
        requests.get.assert_called_with(expected_url)
