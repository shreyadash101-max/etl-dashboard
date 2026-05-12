import pandas as pd
import logging

logger = logging.getLogger(__name__)

def transform(df):
    """Clean and validate data"""

    logger.info("Starting transformation")

    # 1. Standardize column names
    df.columns = [col.lower() for col in df.columns]

    # 2. Remove missing values
    df = df.dropna()
    logger.info(f"Rows after removing nulls: {len(df)}")

    # 3. Convert date column
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # 4. Remove invalid dates
    if 'date' in df.columns:
        df = df.dropna(subset=['date'])

    # 5. 
    if 'sales' in df.columns:
        df['sales_category'] = df['sales'].apply(
            lambda x: 'High' if x > 100 else 'Low'
        )

    return df