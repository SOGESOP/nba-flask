# imports the csv into the database

import pandas as pd
df = pd.read_csv('2021.csv')
df.columns = [c.lower() for c in df.columns] # PostgreSQL doesn't like capitals or spaces

from sqlalchemy import create_engine
engine = create_engine('postgresql://theodore:pierre@localhost:5432/nba')

df.to_sql("players", engine)