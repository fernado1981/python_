from selenium.webdriver import Chrome


class openlink:
    listaNews = []
    Chrome(executable_path="/usr/local/bin/chromedriver")
    driver = Chrome()
    count = 0

    def __init__(self, lista):
        self.listaNews = lista

    def obtUrl(self, periodico):
        print(periodico)
        for i in range(len(self.listaNews)):
            for c, v in self.listaNews[i].items():
                if c == periodico:
                    return v

    def opneUrl(self, urlList):
        self.driver.get(urlList)

    def searchWord(self, word):
        element = self.driver.find_element_by_xpath("//*[contains(.,' ')]")
        lista = element.text.split(' ')

        for i in lista:
            i.split('\n')
            if word in i:
                self.count = self.count + 1
        print("se ha encontrado: ", self.count, " palabras que coniciden con: ", word)

    def clicktab(self, word):
        self.driver.find_element_by_partial_link_text(word).click()

    def tearDown(self):
        self.driver.quit()
