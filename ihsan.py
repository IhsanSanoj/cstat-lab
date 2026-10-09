import pandas as pd

df = pd.read_csv("/home/mec/Downloads/population_murder_rate.csv")

print("Mean:")
print(df.mean(numeric_only=True))

print("Median:")
print(df.median(numeric_only=True))

print("Variance:")
print(df.var(numeric_only=True))
