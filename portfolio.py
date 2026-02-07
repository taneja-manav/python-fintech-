import pandas as pd 
import numpy as np 

df = pd.read_csv("Updated_Portfolio_Management.csv")

print(df.head())

market_return = df['NSE_Return']
stock_return = df.drop(columns = ["Date","NSE_Return"])

trading_days = 252
avg_daily_return = stock_return.mean()
annual_return = np.round((avg_daily_return * trading_days)*100,2)
print(annual_return)

