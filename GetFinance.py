import requests

response = requests.get('https://finnhub.io/api/v1/quote?symbol=AAPL&token=bsrbhmf48v6tucpg28a0')
print(response.status_code)

if response.status_code == 200:
    response = response.json()

for c, v in response.items():
    print(c, v)
