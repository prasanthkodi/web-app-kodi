import unittest
from app import create_app

class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        """Set up a test client before each test"""
        self.app = create_app().test_client()

    def test_home_page(self):
        """Ensure the home page loads successfully"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
