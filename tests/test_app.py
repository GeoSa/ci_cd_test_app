import unittest
import app as tested_app


class FlaskTestApp(unittest.TestCase):
    def setUp(self) -> None:
        tested_app.app.config['TESTING'] = True
        self.app = tested_app.app.test_client()

    def test_get_hello_endpoint(self) -> None:
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello World!')

    def test_post_hello_endpoint(self) -> None:
        response = self.app.post('/')
        self.assertEqual(response.status_code, 405)

