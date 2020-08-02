from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys


class Testlinkedin:
    Chrome(executable_path='/usr/local/bin/chromedriver')
    driver = Chrome()
    iniciar_sesion_link = '.nrgt .mslg .sld .cNifBc .r .l'
    out = '.display-flex .nav-container .nav-item--profile .nav-item__content'
    salir = "//*[@id='ember38']"
    submit = "button[type='submit']"
    inputGoogle = "input[name='q']"
    username_input = '#username'
    password_input = '#password'

    def __init__(self, Url, User, Passwd):
        self.url = Url
        self.user = User
        self.passwd = Passwd

    def searchUrl(self):
        self.driver.get(self.url)
        assert self.driver.title == "Google", "Houston we've got a problem"
        element = self.driver.find_element_by_css_selector(self.inputGoogle)
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
        linkedin = self.driver.find_element_by_css_selector(self.submit)
        linkedin.click()
        assert self.driver.title == "LinkedIn", "Houston we've got a problem"

    def logout(self):
        linkedin = self.driver.find_element_by_css_selector(self.out)
        linkedin.click()
        self.driver.implicitly_wait(10)
        linkedin = self.driver.find_element_by_xpath(self.salir)
        linkedin.click()
        assert self.driver.title == "LinkedIn: inicio de sesión o registro", "Houston we've got a problem"

    def quitdriver(self):
        self.driver.quit()
