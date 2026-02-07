import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("financial_time_series.csv")
df["date"] = pd.to_datetime(df["date"])

# # Calculate weekly average before resetting index
weekly_average = df.set_index("date").resample("W")["amount"].mean()

# Fix: reset_index() and strftime()
weekly_df = weekly_average.reset_index()
weekly_df["Month"] = weekly_df["date"].dt.strftime("%b")
weekly_df["week"] = ((weekly_df["date"].dt.day-1)//7)+1
weekly_df["week_label"] = weekly_df["Month"] + " week " + weekly_df["week"].astype(str)

print(weekly_df[["week_label", "amount"]])

# Monthly_total=df.set_index("date").resample("ME")["amount"].sum()
# Monthly_df=Monthly_total.reset_index()
# Monthly_df["Month"]=Monthly_df["date"].dt.strftime("%b")
# Monthly_df["Month_label"]=Monthly_df["Month"]


# print(Monthly_df[["Month_label","amount"]])

plt.figure(figsize=(10,4))
plt.plot(weekly_df["week_label"],weekly_df["amount"])
plt.title("Weekly Average Amount")
plt.xlabel("Week")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

