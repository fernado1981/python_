from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys


class linkedin:
    Chrome(executable_path='/usr/local/bin/chromedriver')
    driver = Chrome()
    iniciar_sesion_link = '.nrgt .mslg .sld .cNifBc .r .l'
    username_input = '#username'
    password_input = '#password'

    def __init__(self, Url, User, Passwd):
        self.url = Url
        self.user = User
        self.passwd = Passwd

    def serachUrl(self):
        self.driver.get(self.url)
        assert self.driver.title == "Google", "Houston we've got a problem"
        element = self.driver.find_element_by_css_selector("input[name='q']")
        element.send_keys('linkedin')
        element.send_keys(Keys.ENTER)
        linkedin = self.driver.find_element_by_css_selector(self.iniciar_sesion_link)
        linkedin.click()
        assert self.driver.title == "Iniciar sesión en LinkedIn | LinkedIn", "Houston we've got a problem"

    def initSesion(self):
        linkedin = self.driver.find_element_by_css_selector(self.username_input)
        linkedin.send_keys(self.user)
        linkedin = self.driver.find_element_by_css_selector(self.password_input)
        linkedin.send_keys(self.passwd)
        linkedin = self.driver.find_element_by_css_selector("button[type='submit']")
        linkedin.click()
        assert self.driver.title == "LinkedIn", "Houston we've got a problem"

    def quitdriver(self):
        self.driver.quit()
