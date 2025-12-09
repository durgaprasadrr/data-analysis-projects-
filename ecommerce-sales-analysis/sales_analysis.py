import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_dataset.csv")

# Revenue column
df["revenue"] = df["quantity"] * df["price"]

print("First 5 rows:")
print(df.head())

# Monthly Revenue
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.to_period("M")

monthly_rev = df.groupby("month")["revenue"].sum()
print("\nMonthly Revenue:")
print(monthly_rev)

# Plot
monthly_rev.plot(kind="bar")
plt.title("Monthly Revenue Trend")
plt.ylabel("Revenue")
plt.xlabel("Month")
plt.tight_layout()
plt.savefig("monthly_revenue.png")
