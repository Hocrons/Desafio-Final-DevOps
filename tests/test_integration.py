import unittest
from app import app

class IntegrationTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_status_and_json(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertIsInstance(data, dict)
        self.assertIn('message', data)

    def test_login_returns_token(self):
        resp = self.client.post('/login', json={"username": "test", "password": "test"})
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertIn('access_token', data)

if __name__ == '__main__':
    unittest.main()
