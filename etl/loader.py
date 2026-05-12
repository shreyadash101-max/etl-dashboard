import sqlite3

def extract(file_path):
    """Reads CSV file and returns DataFrame."""
    ...

def load(df):
    conn = sqlite3.connect('data/etl.db')
    df.to_sql('data', conn, if_exists='replace', index=False)
    conn.close()