from binance.client import Client
import config
import numpy as np
import pandas as pd
import csv

client = Client(config.API_KEY, config.API_SECRET)

# prices = client.get_all_tickers()


# for price in prices:
#     print(price)

# candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)

# df_for_csv = []
# for candel in candles:
#     df_for_csv.append(candel)

# df = pd.DataFrame(df_for_csv)
# print(df.head())
# print(df.shape)
# print(len(candles))

klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_5MINUTE, "1 Jan, 2017", "6 Dec, 2020")

df_for_csv = []
for kline in klines:
    df_for_csv.append(kline)

df = pd.DataFrame(df_for_csv)
print(df.head())
print(df.shape)