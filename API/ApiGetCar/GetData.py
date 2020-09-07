from API.ApiGetCar.DataApi import DataApi
from API.Generic.hook import ApiCRUD


class GetData(ApiCRUD):

    def __init__(self):
        self.data = DataApi.data
        self.dataUrl = DataApi.data['url']
        self.search = DataApi.data['searchWord']

    def TakeData(self):
        for c, v in self.ApiGet(self.dataUrl).items():
            if c == self.search:
                #print(type(self.data))
                self.data['data'] = {True: v}

    def ShowData(self):
        print(self.data)
