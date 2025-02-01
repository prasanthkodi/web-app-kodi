from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

class TitanicData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    PassengerId = db.Column(db.Integer, nullable=False)
    Survived = db.Column(db.Integer, nullable=False)
    Pclass = db.Column(db.Integer, nullable=False)
    Name = db.Column(db.String(100), nullable=False)
    Sex = db.Column(db.String(10), nullable=False)
    Age = db.Column(db.Float, nullable=True)  # Allow NULL values
    SibSp = db.Column(db.Integer, nullable=False)
    Parch = db.Column(db.Integer, nullable=False)
    Ticket = db.Column(db.String(20), nullable=False)
    Fare = db.Column(db.Float, nullable=False)
    Cabin = db.Column(db.String(20), nullable=True)  # Allow NULL values
    Embarked = db.Column(db.String(1), nullable=True)  # Allow NULL values

    def __repr__(self):
        return f"TitanicData('{self.PassengerId}', '{self.Name}', '{self.Age}', '{self.Survived}')"