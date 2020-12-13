from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/buy')
def buy():
    return 'buy'

@app.route('/sell')
def sell():
    return 'sell'

@app.route('/setting')
def setting():
    return 'setting'

if __name__ == '__main__':
    app.run(debug=True)