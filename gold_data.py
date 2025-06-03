import requests

API_KEY = 'd0s8ip9r01qkkpltlsb0d0s8ip9r01qkkpltlsbg'

def get_gold_price():
    url = f'https://www.alphavantage.co/query?function=COMMODITY_EXCHANGE_RATE&from_symbol=XAU&to_symbol=USD&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    try:
        price = data['Realtime Commodity Exchange Rate']['5. Exchange Rate']
        return float(price)
    except KeyError:
        return None

price = get_gold_price()
if price:
    print(f"سعر الذهب الحالي: {price} دولار أمريكي")
else:
    print("تعذر جلب بيانات الذهب")
