from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class valueNY:

    driver = webdriver.Chrome()

    def __init__(self, data):
        self.datos = data

    def openUrl(self):
        self.driver.get(self.datos['UrlGoogle'])
        input=self.driver.find_element_by_name(self.datos['InputGoogleName'])
        input.send_keys(self.datos['Urltel'])
        input.send_keys(Keys.ENTER)

    def firstOption(self):
        First = self.driver.find_elements_by_xpath(self.datos['FirsOptionXpath'])[0]
        First.find_element_by_xpath('.//a').click()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def AceptBannerterms(self):
        self.driver.find_element_by_css_selector(self.datos['acepterms']).click()

    def Acciones(self):
        self.driver.find_element_by_link_text(self.datos['AccionistasLinkText']).click()

    def valueNY(self):
        iframe = self.driver.find_element_by_id(self.datos['iframe'])
        self.driver.switch_to.frame(iframe)

        self.driver.find_element_by_link_text(self.datos['NYSElinktext']).click()

        self.driver.implicitly_wait(10)

        for val in self.driver.find_elements_by_css_selector(self.datos['valueNY']):
            print(val.text)

    def TearDown(self):
        self.driver.quit()







