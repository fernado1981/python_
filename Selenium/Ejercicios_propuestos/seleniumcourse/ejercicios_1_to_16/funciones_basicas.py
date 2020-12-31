from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class funciones_basicas:
    count = 0
    count_h1 = 0
    count_h2 = 0
    count_h3 = 0
    lista_divs_header = {
        "h1": count_h1,
        "h2": count_h2,
        "h3": count_h3
    }

    locator = {
        "xpath_cookie_netflix": "//div[@id='cookie-disclosure'] // div[@class ='cta-btn-container']//*[contains(text(),'Aceptar')]",
        "xpath_init_sesion": "//*[contains(text(),'Iniciar sesión')]",
        "xpath_documentacion": "//a[@class='nav-item'][normalize-space()='Documentation']",
        "input_google": "[name='q']",
        "input_email_facebook": "//input[@id='email']",
        "input_pass_facebook": "//input[@id='pass']",
        "submit_entrar_facebook": "//button[normalize-space()='Entrar']",
        "acepted_cookie_facebook": "//button[@type='submit'][2]"
    }

    def __init__(self):
        self.driver = webdriver.Firefox()

    def open_browser_title(self, url="http://www.google.es", title=False):
        if title is False:
            self.driver.get(url)
            return "pass"
        elif title is True:
            self.driver.get(url)
            title = self.driver.title
            return title
        elif title is None:
            self.driver.get(url)
            title = WebDriverWait(self.driver, 20).until(EC.title_contains("Google"))
            return title

    def show_title(self, title):
        if title:
            print("Passed")
        else:
            print("Failed")

    def nav_doc(self):
        doc = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.locator["xpath_documentacion"])))
        doc.click()

    def get_windows_size_test(self):
        dimensiones = self.driver.get_window_size()
        for c, v in dimensiones.items():
            print(c, v)
        self.driver.set_window_size(1024, 768)

    def set_windows_size_test(self, width=0, height=0):
        self.driver.set_window_size(width, height)
        dimensiones = self.driver.get_window_size()
        for c, v in dimensiones.items():
            if c == "width" and v == 1024:
                print(c, v)
            if c == "height" and v == 768:
                print(c, v)

    def search_in_google(self, element="Welement"):
        print("tengo", element)
        self.driver.find_element_by_css_selector(self.locator["input_google"]).send_keys(element, Keys.ENTER)

    def acepted_cookie(self):
        self.driver.find_element_by_xpath(self.locator["acepted_cookie_facebook"]).click()

    def send_keys(self, email="test@test.com", pwd="holamundo"):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.locator["input_email_facebook"])))
        input_email = self.driver.find_element_by_xpath(self.locator["input_email_facebook"])
        input_email.send_keys(email)

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.locator["input_pass_facebook"])))
        input_pass = self.driver.find_element_by_xpath(self.locator["input_pass_facebook"])
        input_pass.send_keys(pwd)

        self.driver.find_element_by_xpath(self.locator["submit_entrar_facebook"]).click()

    def selecionar(self):
        for ele_h1 in self.driver.find_elements_by_tag_name("H1"):
            self.count_h1 += 1
            self.lista_divs_header["h1"] = self.count_h1
        print("Hay elementos de tipo H1: ", self.lista_divs_header["h1"])

        for ele_h2 in self.driver.find_elements_by_tag_name("H2"):
            self.count_h2 += 1
            self.lista_divs_header["h2"] = self.count_h2
        print("Hay elementos de tipo H2: ", self.lista_divs_header["h2"])

        for ele_h3 in self.driver.find_elements_by_tag_name("H3"):
            self.count_h3 += 1
            self.lista_divs_header["h3"] = self.count_h3
        print("Hay elementos de tipo H3 ", self.lista_divs_header["h3"])

        print("el que más veces se muestra es: ",
              list(self.lista_divs_header.keys())[
                  list(self.lista_divs_header.values()).index(max(self.lista_divs_header.values()))])

    def show_tag(self, div=False, button=False, input=False, link=False, listas=False):
        if div is True:
            for i in self.driver.find_elements_by_tag_name("div"):
                self.count += 1
            print("cantidad de div's: ", self.count)
        elif button is True:
            for i in self.driver.find_elements_by_tag_name("button"):
                # print(i.text)
                self.count += 1
            print("cantidad de botones: ", self.count)
        elif input is True:
            for i in self.driver.find_elements_by_tag_name("input"):
                # print(i.text)
                self.count += 1
            print("cantidad de input: ", self.count)
        elif link is True:
            for ele_parrafo in self.driver.find_elements_by_tag_name("a"):
                self.count += 1
                # print(ele_parrafo.text)
                self.lista_divs_header["link"] = self.count
            print("hay ", self.count, " links")
        elif listas is True:
            for ele_li in self.driver.find_elements_by_tag_name("li"):
                # print(ele_li.text)
                self.count += 1
                self.lista_divs_header["lista"] = self.count
            print("hay ", self.count, " li")

    def show_repeticiones(self):
        print(self.lista_divs_header)
        print("el que más veces se muestra es: ",
              list(self.lista_divs_header.keys())[
                  list(self.lista_divs_header.values()).index(max(self.lista_divs_header.values()))], " con: ",
              max(self.lista_divs_header.values()))

    def max_window(self):
        self.driver.maximize_window()

    def refres_screen(self):
        self.driver.refresh()

    def go_forward(self):
        self.driver.forward()

    def go_back(self):
        self.driver.back()

    def accept_cookie(self):
        self.driver.find_element_by_xpath(self.locator["xpath_cookie_netflix"]).click()

    def iniciar_sesion_btn(self):
        initsesion = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.locator["xpath_init_sesion"])))
        print(initsesion.text)
        if initsesion != "":
            initsesion.click()
        else:
            print("error")

    def quit_driver(self):
        self.driver.quit()
