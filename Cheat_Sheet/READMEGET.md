[Principal](../README.md)<br/>
[Api_Post](READMEPOST.md) | [Api_Get](READMEGET.md)  | [Tuplas](READMETupleSet.md) | [Listas](READMELIST.md) | [Diccionarios](READMEDIC.md) | [Selenium](../Selenium/README.md)<br/>
# API_Get:


 from pip._vendor import requests <br/>
 class ApiPrueba:<br/>
    url = "http://demo5977139.mockable.io/qa-cdco/exercises/cars_01"<br/>
    sospechoso = 'suspicious_car'<br/>
    lista = []<br/>
    response = requests.get(url)<br/>
    if response.status_code == 200:<br/>
        response = response.json()<br/>
        for c, v in response.items():<br/>
            if c == sospechoso:<br/>
                lista.append(c)<br/>
                lista.append(v)<br/>
   print(lista)<br/>       
