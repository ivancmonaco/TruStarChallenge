import unittest
from unittest.mock import patch, MagicMock
from server.app import app
import json


class TestMitreRoute(unittest.TestCase):
    @patch("routes.mitre.getMalwareRecords", return_value=[{"id": 1}])
    def test_post(self, getMalwareRecords):
        with app.test_client() as client:
            path = "/path"
            keys = ["id"]
            rv = client.post(
                "/mitre",
                data=json.dumps(dict(path=path, keys=keys)),
                content_type="application/json",
            )
            expected_args = (path, keys)
            expected_status_code = 200
            expected_response = {"data": [{"id": 1}]}
            getMalwareRecords.assert_called_with(*expected_args)
            self.assertEqual(rv.status_code, expected_status_code)
            self.assertEqual(json.loads(rv.get_data()), expected_response)

    @patch("routes.mitre.getMalwareRecords", return_value=[])
    def test_post_no_path(self, getMalwareRecords):
        with app.test_client() as client:
            keys = ["id"]
            rv = client.post(
                "/mitre",
                data=json.dumps(dict(keys=keys)),
                content_type="application/json",
            )
            expected_args = ("/", keys)
            expected_status_code = 200
            expected_response = {"data": []}
            getMalwareRecords.assert_called_with(*expected_args)
            self.assertEqual(rv.status_code, expected_status_code)
            self.assertEqual(json.loads(rv.get_data()), expected_response)

    @patch("routes.mitre.getMalwareRecords", return_value=[])
    def test_post_no_keys(self, getMalwareRecords):
        with app.test_client() as client:
            path = "/path"
            rv = client.post(
                "/mitre",
                data=json.dumps(dict(path=path)),
                content_type="application/json",
            )
            expected_args = (path, [])
            expected_status_code = 200
            expected_response = {"data": []}
            getMalwareRecords.assert_called_with(*expected_args)
            self.assertEqual(rv.status_code, expected_status_code)
            self.assertEqual(json.loads(rv.get_data()), expected_response)

    @patch("routes.mitre.getMalwareRecords", return_value=[])
    def test_post_no_content(self, getMalwareRecords):
        with app.test_client() as client:
            rv = client.post("/mitre")
            expected_args = ("/", [])
            expected_status_code = 200
            expected_response = {"data": []}
            getMalwareRecords.assert_called_with(*expected_args)
            self.assertEqual(rv.status_code, expected_status_code)
            self.assertEqual(json.loads(rv.get_data()), expected_response)

    def test_get(self):
        with app.test_client() as client:
            rv = client.get("/mitre")
            expected_status_code = 405
            self.assertEqual(rv.status_code, expected_status_code)

    def test_put(self):
        with app.test_client() as client:
            rv = client.put("/mitre")
            expected_status_code = 405
            self.assertEqual(rv.status_code, expected_status_code)

    def test_delete(self):
        with app.test_client() as client:
            rv = client.delete("/mitre")
            expected_status_code = 405
            self.assertEqual(rv.status_code, expected_status_code)
