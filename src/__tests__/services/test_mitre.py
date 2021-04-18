import unittest
import json
from unittest.mock import patch, MagicMock
from services.mitre import getMalwareRecords

mock_files = {
    "/attack-patterns/file1.json": {"id": 1, "content": "foo", "name": "zzz"},
    "/attack-patterns/file2.json": {"id": 2, "content": "bar", "name": "yyy"},
}

mock_repository = {
    "/attack-patterns": [
        {"isFile": False, "name": "folder"},
        {"isFile": True, "name": "file1.json"},
        {"isFile": True, "name": "file2.json"},
        {"isFile": True, "name": "file3.pdf"},
    ],
    "/other-folder": [],
}


class TestMitreService(unittest.TestCase):
    @patch(
        "repository_navigation.RepositoryNavigator.RepositoryNavigator.listRepository",
        side_effect=lambda p: mock_repository[p],
    )
    @patch(
        "repository_navigation.RepositoryNavigator.RepositoryNavigator.getFileFromRepository",
        side_effect=lambda n: json.dumps(mock_files[n]),
    )
    def test_get_malware_records(self, *args):
        response = getMalwareRecords(
            "/attack-patterns", ["id", "content", "other", "content.other"]
        )

        expected = [{"id": 1, "content": "foo"}, {"id": 2, "content": "bar"}]
        self.assertEqual(response, expected)
