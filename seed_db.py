import pandas as pd
from app import create_app, db

app = create_app()
with app.app_context():
    df = pd.read_csv('titanic.csv')
    df.to_sql('titanic', db.engine, if_exists='replace', index=False)