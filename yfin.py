import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

ticker=input("enter the stock symbol: ")
df=yf.download(ticker,start="2020-01-01",end="2025-12-31")
print(df.head())