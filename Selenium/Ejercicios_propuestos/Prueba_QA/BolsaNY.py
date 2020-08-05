from selenium import webdriver


class BolsaNY:
    driver = webdriver.Chrome()

    def __init__(self, url, test_link, iframid, value):
        self.iframeid = iframid
        self.url = url
        self.text_link = test_link
        self.value = value

    def openUrl(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def iframeBolsa(self):
        iframe = self.driver.find_element_by_id(self.iframeid)
        self.driver.switch_to.frame(iframe)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text(self.text_link).click()

    def obtNYBolsa(self):
        for valor in self.driver.find_elements_by_css_selector(self.value):
            print(valor.text)

    def tearDown(self):
        self.driver.quit()
