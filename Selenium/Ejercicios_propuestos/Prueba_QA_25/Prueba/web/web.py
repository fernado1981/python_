from Prueba.dts.web_telefonica.web_telefonica import web_telefonica


class web(web_telefonica):

    def __init__(self):
        self.driver = self.dt_web_telefonica['driver']
        self.data = self.dt_web_telefonica

    def open_browser(self):
        self.driver.get(self.data['telefonioca'])
        self.driver.implicitly_wait(5)

    def cookies(self):
        self.driver.find_element_by_css_selector(self.data['cookie']).click()
        self.driver.implicitly_wait(5)

    def takeval(self):
        data = []
        for val in self.driver.find_elements_by_xpath('.//a'):
            data.append(val.get_attribute('href'))
        self.driver.implicitly_wait(10)

    def acciones(self):
        self.driver.find_element_by_xpath(self.data['acciones']).click()
        self.driver.implicitly_wait(5)

    def euroland(self):
        self.driver.maximize_window()
        frame = self.driver.find_element_by_id(self.data['frame'])
        self.driver.switch_to.frame(frame)

        self.driver.implicitly_wait(5)

    def nyse(self):
        self.driver.find_element_by_xpath(self.data['NYSE']).click()

    def valny(self):
        for val in self.driver.find_elements_by_css_selector(self.data['valNY']):
            print(val.text)

    def close(self):
        self.driver.quit()
