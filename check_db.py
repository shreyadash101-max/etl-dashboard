import sqlite3
import pandas as pd

conn = sqlite3.connect('data/etl.db')

df = pd.read_sql('SELECT * FROM data', conn)

print(df)

conn.close()