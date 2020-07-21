from API.GetPrueba.Searchdata import Searchdata


class ApiPrueba:
     url = "http://demo5977139.mockable.io/qa-cdco/exercises/cars_01"
     data = 'suspicious_car'
     search = Searchdata(url, data)
     search.searchApiGet()
