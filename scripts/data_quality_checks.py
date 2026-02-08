import pandas as pd

df = pd.read_csv("data/raw/manufacturing_data.csv")

assert df.isnull().sum().sum() == 0
assert df.duplicated().sum() == 0
assert df["yield_percent"].between(0, 100).all()

print("All data quality checks passed.")
