import requests
from selenium.webdriver import Chrome


class paper:
    periodicos = {}
    WebElement = ''
    Chrome(executable_path='/usr/local/bin/chromedriver')
    driver = Chrome()

    def __init__(self, news, url):
        self.periodicos = news
        self.WebElement = url

    def urlNews(self, data):
        for c, v in self.periodicos.items():
            if data in c:
                return self.periodicos[c]['url']
            else:
                pass

    def openUrl(self, url):
        self.driver.get(url)

    def ApiGet(self):
        response = requests.get(self.WebElement)
        print(response.status_code)
        response = response.json()
        print(response)

    def ApiPost(self, data):
        response = requests.post(self.WebElement, data, stream=True)
        print(response.status_code)
        response = response.json()
        print(response)

    def ApiPut(self, data):
        response = requests.put(self.WebElement, data, stream=True)
        print(response.status_code)
        response = response.json()
        print(response)

    def ApiDel(self):
        response = requests.delete(self.WebElement, stream=True)
        print(response.status_code)
        response = response.json()
        print(response)

    def quitDriver(self):
        self.driver.quit()
