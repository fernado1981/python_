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
            
[Api_Post](API_post.md) | [diccionario](diccionario.md) | [set_conjuntos](set_conjunto.md) | [lista_array](lista_Array.md) | [Selenium](selenium.md)