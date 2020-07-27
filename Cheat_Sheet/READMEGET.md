[Principal](../README.md)<br/>
[Api_Post](READMEPOST.md) | [Api_Get](READMEGET.md)  | [Tuplas](READMETupleSet.md) | [Listas](READMELIST.md) | | [Diccionarios](READMEDIC.md) | [Selenium](../Selenium/README.md)
#API_Get:

    import requests<br/>

    url = "http://demo5977139.mockable.io/qa-cdco/exercises/cars_01"<br/>
    response = requests.get(url)<br/>
    print(response.status_code)<br/>
    response = response.json()<br/>
    print(response)<br/>
    sospechoso = []<br/>

    for c, v in response.items():<br/>
        if c == "suspicious_car":<br/>
            sospechoso = c, v<br/>
            sospechoso = list(sospechoso)<br/>
            print(sospechoso)<br/>
            