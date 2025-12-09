import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("covid_dataset.csv")
df["date"] = pd.to_datetime(df["date"])

print("Dataset Preview:")
print(df.head())

# Infection trend
plt.plot(df["date"], df["confirmed"])
plt.title("COVID-19 Infection Trend")
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("infection_trend.png")

# Recovery Rate
df["recovery_rate"] = df["recovered"] / df["confirmed"].replace(0, 1)
print("\nRecovery Rates:")
print(df[["date", "recovery_rate"]])
