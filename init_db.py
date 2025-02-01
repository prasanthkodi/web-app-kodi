from app import create_app, db
from app.models import User, TitanicData  # Import your models

# Create the app
app = create_app()

# Create the database tables
with app.app_context():
    db.create_all()
    print("Database tables created successfully!")