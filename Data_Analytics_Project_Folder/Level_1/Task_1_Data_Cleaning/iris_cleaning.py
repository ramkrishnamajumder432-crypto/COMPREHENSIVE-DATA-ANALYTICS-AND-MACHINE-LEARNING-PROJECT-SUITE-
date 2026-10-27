
import pandas as pd

df = pd.read_csv("1) iris.csv")

print(df.head())

print(df.isnull().sum())

df = df.drop_duplicates()

df.columns = df.columns.str.lower().str.strip()

print(df.info())

cleaned_file = "cleaned_iris.csv"
df.to_csv(cleaned_file, index=False)

print("Cleaned dataset saved successfully")
