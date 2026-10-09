
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("river_temperature.csv")

print("Dataset:")
print(df.head())

river = df[df["Site"] == "Swale at Catterick Bridge"]

print("\nFiltered records:")
print(river)

print("\nMean temperature:")
print(river["Temperature"].mean())

print("\nMedian dissolved oxygen:")
print(river["Dissolved_Oxygen"].median())

river["Temperature"].hist()

plt.title("River Temperature Histogram")
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.show()

