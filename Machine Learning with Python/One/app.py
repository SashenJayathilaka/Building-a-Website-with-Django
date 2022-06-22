import pandas as pd
df = pd.read_csv('vgsales.csv')

print(df.shape)

print(df.describe())

print(df.values)