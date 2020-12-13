from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    title = 'Trading Bot!'
    return render_template('index.html', title = title)

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