import requests

response = requests.get('https://finnhub.io/api/v1/stock/candle?symbol=IBM&resolution=D&from=1546383599&to=1577833199')
if response.status_code == 200:
    response = response.json()

    for c, v in response.items():
        print(c,v)
