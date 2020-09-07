import requests


class ApiCRUD:
    response = ''

    def ApiGet(self, rute=''):
        self.response = requests.get(rute)
        if self.response.status_code == 200:
            if self.response is None or self.response == '':
                self.response = 'I got a null or empty string value for data in a file'
            else:
                self.response = self.response.json()
            return self.response
        else:
            return "error"

    def ApiPost(self, rute='', data=''):
        self.response = requests.post(rute, data, stream=True)
        if self.response.status_code == 200:
            self.response = self.response.json()
            return self.response
