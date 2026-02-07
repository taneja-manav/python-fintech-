import yfinance as yf
import pandas as pd
import numpy as np

def get_stock(symbol):
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info
    
        company_name = info.get("longName",symbol)
        current_price = info.get("currentPrice")
        previous_close = info.get("previousClose")
        
        if current_price and previous_close:
            change = np.round(current_price - previous_close, 2)
            pct_change = np.round((change / previous_close) * 100, 2)
            daily_change = f"{change:+.2f} ({pct_change:+.2f}%)"
            
            print(f"\nCompany Name: {company_name}")
            print(f"Current Price: {current_price}")
            print(f"Previous Close: {previous_close}")
            print(f"Daily Change: {daily_change}")
            
            return {
                "company_name": company_name,
                "current_price": current_price,
                "previous_close": previous_close,
                "daily_change": daily_change
            }
    except Exception as e:
        print(f"Error fetching data: {e}")
    return None

print("Stock Analyser")
print("="*14)

while True:
    # Fixed the syntax error by using 'quit' instead of "quit"
    symbol = input("\nEnter stock symbol (or 'quit'):: ").strip().upper()

    if symbol == "QUIT":
        print("Exiting...")
        break
        
    print(f"Fetching data for {symbol}...")
    data = get_stock(symbol)
    
    if data:
        print("\n--- Final Summary ---")
        print(f"Symbol: {symbol}")
        print(f"Company: {data['company_name']}")
        print(f"Price: {data['current_price']}")
        print(f"Change: {data['daily_change']}")
    else:
        print("Could not retrieve data. Please check the symbol.")