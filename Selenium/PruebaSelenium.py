import re
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class PruebaSelenium:
    list = []
    listNYSE = []
    WebElement = ''
    Chrome(executable_path='/usr/local/bin/chromedriver')
    driver = Chrome()

    def __init__(self, url):
        self.WebElement = url

    def AbrirUrl(self):
        self.driver.get(self.WebElement)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def ObtenerTitleUrl(self):
        dic = {self.driver.title: self.driver.current_url}
        for c, v in dic.items():
            print("Title: ", c, " Url: ", v)
            assert c == "Google"
        self.driver.implicitly_wait(10)

    def searchTelefonica(self):
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("telefonica")
        search_box.send_keys(Keys.ENTER)
        phone = self.driver.find_element(By.CSS_SELECTOR, "a[href='https://www.telefonica.com/es/']")
        phone.click()

        self.driver.implicitly_wait(10)

    def searchElements(self):
        for element in self.driver.find_elements_by_xpath("//a"):
            elements = self.driver.find_elements(By.CSS_SELECTOR, "a[href='https://www.telefonica.com']")

        for i in elements:
            self.list.append(i)

        for i in self.list:
            print(i)

        self.driver.implicitly_wait(10)

    def Accionistas(self):
        Accionista = self.driver.find_element(By.LINK_TEXT, "Accionistas e inversores")
        Accionista.click()
        self.driver.implicitly_wait(10)
        print("Tengo: ", self.driver.title)
        self.driver.implicitly_wait(10)

    def NYSE_Values(self):
        # Almacena el elemento web
        iframe = self.driver.find_element(By.CSS_SELECTOR, ".EurolandTool")
        # Cambia el foco al iframe
        self.driver.switch_to.frame(iframe)
        # Ahora podemos hacer clic en el botón
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.LINK_TEXT, 'NYSE').click()
        self.driver.implicitly_wait(10)
        for i in self.driver.find_elements_by_xpath("/html/body/div/div[2]/div/div[2]"):
            self.listNYSE.append(i)

        for i in self.listNYSE:
            print(i)

    def tearDown(self):
        self.driver.quit()
