import pandas as pd
import os

def extract(file_path):
    """Reads CSV file and returns DataFrame."""

    print("DEBUG: file_path =", file_path)

    if not file_path:
        raise ValueError("CSV_PATH is not set")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    df = pd.read_csv(file_path)

    print("DEBUG: Data loaded successfully")

    return df