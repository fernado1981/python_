from API.GetPruebaCoches3.Searchdata import Searchdata


class ApiPrueba:
     #dada una url
     url = "http://demo5977139.mockable.io/qa-cdco/exercises/cars_03"
     #dado el datgo a buscar
     data = 'suspicious_interval'
     Matricula= '7692I'
     Intervalo = '9257I'
     #cereamos un objeti de tipo SearchData y le pasamos la url y el data al constructor
     search = Searchdata(url, data,Matricula,Intervalo)
     #invocamos el método searchApiGet de SeachData
     search.searchApiGet()
     search.showIntervalo()
