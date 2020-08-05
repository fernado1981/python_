from selenium import webdriver


class Accionista:
    driver = webdriver.Chrome()

    def __init__(self, url, text):
        self.url = url
        self.link = text

    def openUrl(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def clickLink(self):
        self.driver.find_element_by_link_text(self.link).click()
        print(self.driver.title)
        print(self.driver.current_url)

    def tearDown(self):
        self.driver.quit()
