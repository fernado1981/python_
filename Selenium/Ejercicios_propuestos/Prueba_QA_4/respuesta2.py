import requests




class respuesta2:
    lista = []
    response = ''

    def __init__(self, url, sospechoso):
        self.url = url
        self.sospechosos = sospechoso

    def ApiGet(self):
        try:
            self.response = requests.get(self.url)
            if self.response.status_code == 200:
                self.response = self.response.json()
        except:
            print("Error")


    def obtData(self):
        print(self.response)
        try:
            for c, v in self.response.items():
                if c == self.sospechosos:
                    self.lista.append(c)
                    self.lista.append(v)
            print(self.lista)
        except:
            print("Error")
