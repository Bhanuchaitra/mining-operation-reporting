
import pandas as pd

# Load the practice dataset
df = pd.read_csv("data/production_data.csv")

# Calculate production achievement for each shift
df["production_achievement_pct"] = (
    df["actual_tonnes"] / df["planned_tonnes"] * 100
).round(2)

# Calculate downtime percentage for each shift
df["downtime_pct"] = (
    df["downtime_hours"] / df["scheduled_hours"] * 100
).round(2)

print("Production Reporting Analysis")
print("-----------------------------")

print("\nTotal planned tonnes:", df["planned_tonnes"].sum())
print("Total actual tonnes:", df["actual_tonnes"].sum())

achievement = (
    df["actual_tonnes"].sum() / df["planned_tonnes"].sum() * 100
)
print("Overall production achievement:", round(achievement, 2), "%")

downtime = (
    df["downtime_hours"].sum() / df["scheduled_hours"].sum() * 100
)
print("Overall downtime:", round(downtime, 2), "%")

print("\nShift-level results:")
print(df[[
    "date",
    "shift",
    "production_achievement_pct",
    "downtime_pct",
    "reporting_effort_hours"
]])

