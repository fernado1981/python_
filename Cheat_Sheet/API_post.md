# API_Post:

import requests<br/>

url = "https://jsonplaceholder.typicode.com/posts"<br/>
data = {"Nombre": "Fer", "Edad": 39}<br/>
response = requests.post(url, data, stream=True)<br/>
print(response.status_code)<br/>
response = response.json()<br/>
print(response)<br/>

