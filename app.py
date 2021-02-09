from flask import Flask, render_template, jsonify, url_for
from binance.client import Client
from datetime import datetime, timedelta
import config
from binance.enums import *

client = Client(config.API_KEY, config.API_SECRET)

app = Flask(__name__)

@app.route('/')
def index():
    title = 'Trading Bot!'
    info = client.get_account()
    balance = info['balances']
    list_of_balance = [[i['asset'], i['free'], i['locked']] for i in info['balances'] if float(i['free'])>0.]
    return render_template('index.html', title = title, my_balance=list_of_balance)

@app.route('/buy')
def buy():
    return 'buy'

@app.route('/sell')
def sell():
    return 'sell'

@app.route('/setting')
def setting():
    return 'setting'


@app.route('/history')
def history():
    candels = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1HOUR, "19 Dec, 2020", '{:%d %B, %Y}'.format(datetime.today() + timedelta(days=1))) # , "1 Jan, 2017", "6 Dec, 2020"

    list_canel = []
    for i in candels:
        points = {
            'time': i[0]/1000,
            'open': i[1],
            'high': i[2],
            'low': i[3],
            'close': i[4]
        }
        list_canel.append(points)


    return jsonify(list_canel)


if __name__ == '__main__':
    app.run(debug=True)