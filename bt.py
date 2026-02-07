import pandas as pd
import numpy as np

df = pd.read_csv("bank_transactions.csv")

# print(df.head())

df["date"] = pd.to_datetime(df["date"])
errors = []
if df["amount"].min() < 0:
    errors.append("invalid amount")
if df.duplicated("transaction_id").any():
    errors.append("duplicate transaction id")
if df["balance"].min() < 0:
    errors.append("invalid balance")
if errors:
    print("Data validation Failed")

    for i in errors:
        print("-",i)

else:
    print("Data validation Success")

# daily_summary=df.set_index("date").resample("D")["amount"].sum()
# print("Daily summary")
# print(daily_summary)
# Monthly_summary=df.set_index("date").resample("ME")["amount"].mean()
# print("Monthly summary")
# print(Monthly_summary)



suspicious_transactions=df[df["amount"]>8000]
suspicious_transactions_count = len(suspicious_transactions)

print("Suspicious transactions")
print(suspicious_transactions_count)  

suspicious_transactions.to_csv("suspicious_transactions.csv",index=False)

