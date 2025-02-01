import unittest
from app import create_app, db
from app.models import User

class ModelsTestCase(unittest.TestCase):
    def setUp(self):
        """Set up test client and application context"""
        self.app = create_app()

        with self.app.app_context():
            db.create_all()  # Create tables before each test

    def tearDown(self):
        """Clean up database"""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()  # Drop tables after each test

    def test_create_user(self):
        """Ensure user creation works"""
        with self.app.app_context():  # Ensure database operations are inside app context
            user = User(username="testuser", email="test@example.com", password="hashedpass")
            db.session.add(user)
            db.session.commit()

            fetched_user = User.query.filter_by(username="testuser").first()
            self.assertIsNotNone(fetched_user)
            self.assertEqual(fetched_user.email, "test@example.com")

if __name__ == '__main__':
    unittest.main()
