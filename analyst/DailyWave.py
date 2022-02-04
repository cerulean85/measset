from datetime import datetime, timedelta
import os
import pandas as pd
import FinanceDataReader as fdr
#pd.set_option("display.max_columns", None)
#pd.set_option("display.max_rows", None)

if not os.path.exists("df_nasdaq.csv"):
    df_nasdaq = fdr.StockListing("NASDAQ")
    df_nasdaq.to_csv("df_nasdaq.csv")
else: 
    df_nasdaq = pd.read_csv("df_nasdaq.csv")

now = datetime.now()
weekday = now.weekday()
if weekday == 5 or weekday == 6:
    now = now - timedelta(days=(weekday-4))

if weekday == 0 and now.hour < 9:
    now = now - timedelta(days=(3))

now = str(now).split(' ')[0]
print(now)

# https://financedata.github.io/posts/finance-data-reader-users-guide.html
wants = [
    "USD/KRW", "EUR/KRW",
    "AAPL", "ADBE", "KO", 
    "ETH/KRW",
    "DJI", "IXIC", "US500", "KS11"]
for want in wants:
    df = fdr.DataReader(want, now, now)  
    print(df)

# print(애플주가)
# print(코카콜라주가)
# print(어도비주가)
# print(달러환율)
# print(유로화환율)
# print(미국채권수익률)
# print(금시세)
# print(이더리움시세)
# print(날씨)
# print(코스피지수)
# print(다우지수)
# print(나스닥지수)
# print(S&P500지수)
