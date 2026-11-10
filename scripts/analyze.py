import pandas as pd

df = pd.read_excel("data/fruit_size_data.xlsx")

print("\nFirst 5 rows:")
print(df.head())

print("\nColumn Names:")
print(df.columns)

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSummary Statistics:")
print(df.describe())

print("\nAverage Actual Size:")
print(df["size_in_mm-actual"].mean())

print("\nMaximum Actual Size:")
print(df["size_in_mm_actual"].max())

print("\nMinimum Actual Size:")
print(df["size_in_mm_actual"].min())

print("\nAverage Estimated Mass:")
print(df["estimated_mass"].mean())

print("\nAverage Size By Header ID:")

print(df.groupby("header_id")["size_in_mm_actual"].mean().short_values(ascending=False))