from binance.client import Client
import config
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import csv

client = Client(config.API_KEY, config.API_SECRET)

info = client.get_account()
# for i in info['balances']:
#     # print(i['loced'])
#     if float(i['free'])>0.:
#         print(i)

# list_of_balance = [[i['asset'], i['free'], i['locked']] for i in info['balances'] if float(i['free'])>0.]
# print(list_of_balance)

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




# candels = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_30MINUTE, "19 Dec, 2020", '{:%d %B, %Y}'.format(datetime.today() + timedelta(days=1))) # , "1 Jan, 2017", "6 Dec, 2020"

# list_canel = []
# for i in candels:
#     points = {
#         'time': i[0],
#         'open': i[1],
#         'high': i[2],
#         'low': i[3],
#         'close': i[4]
#     }
#     list_canel.append(points)

# print(list_canel[-1])


# Get dayly data
# candels = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2020", '{:%d %B, %Y}'.format(datetime.today() + timedelta(days=1))) # , "1 Jan, 2017", "6 Dec, 2020"

# csvfile = open('data/dayly.csv', 'w', newline='')
# candel_writer = csv.writer(csvfile, delimiter=',')

# for candel in candels:
#     candel[0] = datetime.utcfromtimestamp(int(candel[0]/1000)).strftime('%Y-%m-%d %H:%M:%S') 
#     candel_writer.writerow(candel)

# print(len(candels))
# csvfile.close()

# print('{:%d %B, %Y}'.format(datetime.today() + timedelta(days=1)))

# Get 15 min data
candels = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1HOUR, "1 Oct, 2020", '{:%d %B, %Y}'.format(datetime.today() + timedelta(days=1))) # , "1 Jan, 2017", "6 Dec, 2020"

csvfile = open('data/1hour_backtest.csv', 'w', newline='')
candel_writer = csv.writer(csvfile, delimiter=',')

for candel in candels:
    candel[0] = datetime.utcfromtimestamp(int(candel[0]/1000)).strftime('%Y-%m-%d %H:%M:%S') 
    candel_writer.writerow(candel)

print(len(candels))
csvfile.close()





