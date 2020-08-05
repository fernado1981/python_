from selenium import webdriver


class respuesta5:
    driver = webdriver.Chrome()

    def __init__(self, urlTelefonica, bag, values, iframe):
        self.bag = bag
        self.values = values
        self.iframe = iframe
        self.url = urlTelefonica

    def opnUrl(self):
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)

    def obtValueNyse(self):
        self.driver.maximize_window()
        ifm = self.driver.find_element_by_id(self.iframe)
        self.driver.switch_to.frame(ifm)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text(self.bag).click()

        for val in self.driver.find_elements_by_css_selector(self.values):
            print(val.text)
