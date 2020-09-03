from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class DataWeb:
    data = {
        # driver
        'driver': webdriver.Chrome(),
        # Get open browser url
        'google': 'http://www.google.es',
        # by name search input google
        'igoogle': 'q',
        # send keys enter url by seacrh in google
        'telefonicaUrl': 'https://wwww.telefonica.com/es',
        # xpath search the first position and click
        'first': "//div[@id='search']//div[@class='g']",
        'link': './/a',
        'tag': 'href',
        'Nyse': "//a[contains(.,'NYSE')]",
        # css_selector cookies
        'cookie': '.cc-cookies .cc-cookie-accept',
        'valNy': '.Tab_Active .last',
        # by_link_name seacrh Acciones and click
        'acciones': 'Accionistas e inversores',
        # by id change to frame
        'iframe': 'euroland-ticker-es',
    }

    def __init__(self):
        self.datas = self.data
        self.driver = DataWeb.data['driver']

    def openBrowser(self):
        self.driver.get(self.datas['google'])

    def search(self):
        input = self.driver.find_element_by_name(self.datas['igoogle'])
        input.send_keys(self.datas['telefonicaUrl'] + Keys.ENTER)
        self.driver.implicitly_wait(10)

    def fristOption(self):
        first = self.driver.find_elements_by_xpath(self.datas['first'])[0]
        first.find_element_by_xpath(self.datas['link']).click()
        self.driver.implicitly_wait(10)

    def cookie(self):
        cookie = self.driver.find_element_by_css_selector(self.data['cookie'])
        cookie.click()

    def takeTag(self):
        count = 0
        for val in self.driver.find_elements_by_xpath('.//a'):
            self.data[count] = val.get_attribute(self.data['tag'])
            count += 1
        self.driver.implicitly_wait(20)

    def acciones(self):
        acciones = self.driver.find_element_by_link_text(self.data['acciones'])
        acciones.click()
        self.driver.implicitly_wait(10)

    def vlaNy(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        iframe = self.driver.find_element_by_id(self.data['iframe'])
        self.driver.switch_to.frame(iframe)
        nyse = self.driver.find_element_by_xpath(self.data['Nyse'])
        nyse.click()
        self.driver.implicitly_wait(5)

        for val in self.driver.find_elements_by_css_selector(self.data['valNy']):
            print(val.text)

        self.driver.implicitly_wait(10)

    def quit(self):
        self.driver.quit()
