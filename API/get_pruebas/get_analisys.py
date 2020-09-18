import requests

url = "https://3000-cce3d78b-04e9-46e1-bdc8-00f4637a3aa0.ws-eu01.gitpod.io/watchlist"

payload = {}
headers = {}
response = requests.request("GET", url, headers=headers, data=payload)
resp = response.json()


for i in range(len(resp)):
    for c, v in resp[i].items():
        if c == 'user_id':
            print('wachtList_user_id:',v)
        if c == 'stocks':
            for i in range(len(v)):
                print("symbol: ",v[i]['symbol'])
                print("name: ",v[i]['name'])

