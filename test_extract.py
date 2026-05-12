from etl.extractor import extract

df = extract('data/dummy_data.csv')

print(df.head())