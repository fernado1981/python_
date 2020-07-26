from API.Sospechoso.ApiGet_sospechoso import apiget_sospechoso


class get_suspicius:
    search = 'suspicious_car'
    url = 'http://demo5977139.mockable.io/qa-cdco/exercises/cars_01'

    api = apiget_sospechoso(url, search)
    api.getData()
    api.searchData()
    api.viewlist()
