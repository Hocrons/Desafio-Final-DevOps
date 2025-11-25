import unittest
from app import app

class BehaviorTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_protected_requires_token(self):
        resp = self.client.get('/protected')
        self.assertEqual(resp.status_code, 401)

    def test_protected_with_token(self):
        login = self.client.post('/login', json={"username": "test", "password": "test"})
        token = login.get_json().get('access_token')
        self.assertIsNotNone(token)

        resp = self.client.get('/protected', headers={"Authorization": f"Bearer {token}"})
        self.assertIn(resp.status_code, (200, 201))

if __name__ == '__main__':
    unittest.main()
