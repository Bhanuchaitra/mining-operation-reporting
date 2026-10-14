import pandas as pd

data = pd.read_csv("data/production_data.csv")

print("Mining Production Report")
print(data)

print("\nTotal production:")
print(data["production_tonnes"].sum())

print("\nAverage daily production:")
print(data["production_tonnes"].mean())
