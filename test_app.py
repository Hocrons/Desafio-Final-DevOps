import unittest
import json
from app import app

class ApiTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        """Teste da rota /"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data["message"], "API is running")

    def test_items(self):
        """Teste da rota /items"""
        response = self.app.get('/items')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn("items", data)
        self.assertIsInstance(data["items"], list)

    def test_login(self):
        """Teste do login JWT"""
        response = self.app.post('/login')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn("access_token", data)
        self.assertIsInstance(data["access_token"], str)

    def test_protected_without_token(self):
        """Teste da rota protegida sem token"""
        response = self.app.get('/protected')
        self.assertEqual(response.status_code, 401)

    def test_protected_with_token(self):
        """Teste da rota protegida com token válido"""
        login_resp = self.app.post('/login')
        token = json.loads(login_resp.data)["access_token"]

        response = self.app.get(
            '/protected',
            headers={"Authorization": f"Bearer {token}"}
        )

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data["message"], "Protected route")


if __name__ == '__main__':
    unittest.main()

