import requests
r = requests.get('https://finnhub.io/api/v1/stock/metric?symbol=AAPL&metric=all&token=')
print(r.json())