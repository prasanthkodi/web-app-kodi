import unittest
from app import create_app, db
from app.models import User
from werkzeug.security import generate_password_hash

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        """Set up test client and application context"""
        self.app = create_app()
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()  # Create tables before each test

    def tearDown(self):
        """Clean up database"""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()  # Drop tables after each test

    def test_login_page_loads(self):
        """Ensure the login page loads correctly"""
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_user_authentication(self):
        """Test user authentication"""
        with self.app.app_context():  # Ensure database operations are inside app context
            hashed_password = generate_password_hash("password123")
            user = User(username="testuser", email="test@example.com", password=hashed_password)
            db.session.add(user)
            db.session.commit()

            response = self.client.post('/login', data={
                "username": "testuser",
                "password": "password123"
            }, follow_redirects=True)

            self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
