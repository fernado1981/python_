[Principal](../README.md)<br/>
[Api_Post](READMEPOST.md) | [Api_Get](READMEGET.md)  | [Tuplas](READMETupleSet.md) | [Listas](READMELIST.md) | [Diccionarios](READMEDIC.md) | [Selenium](../Selenium/README.md)<br/>
# API_Get:

    import requests<br/>

    url = "http://demo5977139.mockable.io/qa-cdco/exercises/cars_01"<br/>
    sospechoso = 'cat'<br/>
    lista=[]
    response = requests.get(url)<br/>
    if response.status_code == 200:<br/>
        response = response.json()<br/>
        for c, v in response.items():<br/>
            if c == sospechoso:<br/>
                lista.append({c,v})<br/>
                print(lista)<br/>
            
