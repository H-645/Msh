from flask import Flask, jsonify
from gold_data import get_gold_price

app = Flask(__name__)

@app.route('/')
def home():
    return "مرحباً بك في Chicha AI!"

@app.route('/gold-price')
def gold_price():
    price = get_gold_price()
    return jsonify({'gold_price': price})

if __name__ == '__main__':
    app.run(debug=True)
