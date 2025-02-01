import pandas as pd
from app import create_app, db
from app.models import TitanicData

# Create the app
app = create_app()

# Load the Titanic dataset
data = pd.read_csv('titanic.csv')

# Replace NaN values in the 'Age' column with a default value (e.g., 0)
data['Age'] = data['Age'].fillna(0)

# Replace NaN values in the 'Cabin' and 'Embarked' columns with a default value (e.g., 'Unknown')
data['Cabin'] = data['Cabin'].fillna('Unknown')
data['Embarked'] = data['Embarked'].fillna('Unknown')

# Seed the database
with app.app_context():
    for index, row in data.iterrows():
        passenger = TitanicData(
            PassengerId=row['PassengerId'],
            Survived=row['Survived'],
            Pclass=row['Pclass'],
            Name=row['Name'],
            Sex=row['Sex'],
            Age=row['Age'],
            SibSp=row['SibSp'],
            Parch=row['Parch'],
            Ticket=row['Ticket'],
            Fare=row['Fare'],
            Cabin=row['Cabin'],
            Embarked=row['Embarked']
        )
        db.session.add(passenger)
    db.session.commit()
    print("Database seeded successfully!")