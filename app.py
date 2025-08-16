from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

portfolio = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_stock', methods=['POST'])
def add_stock():
    symbol = request.form['symbol'].upper()
    shares = int(request.form['shares'])
    price = float(request.form['price'])
    
    portfolio.append({
        'symbol': symbol,
        'shares': shares,
        'price': price,
        'total': round(shares * price, 2)
    })
    
    return redirect(url_for('show_portfolio'))

@app.route('/portfolio')
def show_portfolio():
    total_value = sum(stock['total'] for stock in portfolio)
    return render_template('portfolio.html', portfolio=portfolio, total_value=round(total_value, 2))

if __name__ == '__main__':
    app.run(debug=True)
