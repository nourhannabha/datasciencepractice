import pandas as pd

df = pd.read_json('News_Category_Dataset_v3.csv', lines=True)

print(df)

print(df.head())

print(df.info())

print(df.describe())

print(df.isnull().sum())

duplicates = df.duplicated()
print("Duplicate rows")
print(df[duplicates])


df_no_duplicates = df.drop_duplicates()
print("DataFrame without duplicates")
print(df_no_duplicates)

print(duplicates.sum())

duplicates = df.duplicated()
print("Duplicate rows")
print(duplicates)
