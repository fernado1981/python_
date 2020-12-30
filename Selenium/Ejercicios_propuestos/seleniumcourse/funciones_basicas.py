from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class funciones_basicas:

    def __init__(self):
        self.driver = webdriver.Firefox()

    def open_browser_title(self, url="http://www.google.es", title=False):
        if title is False:
            self.driver.get(url)
            return "pass"
        else:
            self.driver.get(url)
            title = WebDriverWait(self.driver, 20).until(EC.title_contains("Google"))
            return title

    def show_title(self, title):
        print(title)
        if title is True:
            print("Passed")
        else:
            print("Failed")

    def nav_doc(self):
        doc = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@class='nav-item'][normalize-space()='Documentation']")))
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
        self.driver.find_element_by_css_selector("[name='q'").send_keys(element, Keys.ENTER)

    def bbcMundo(self):
        self.driver.get("https://www.bbc.com/mundo")
        count_h1 = 0
        count_h2 = 0
        count_h3 = 0

        for ele_h1 in self.driver.find_elements_by_tag_name("H1"):
            count_h1 += 1
        print("Hay elementos de tipo H1: ", count_h1)

        print("\n Elementos H2: \n")
        for ele_h2 in self.driver.find_elements_by_tag_name("H2"):
            count_h2 += 1
            if count_h2 <= 3:
                print(count_h2, "", ele_h2.text)
        print("Hay elementos de tipo H2: ", count_h2)

        print("\n Elementos H3: \n")
        for ele_h3 in self.driver.find_elements_by_tag_name("H3"):
            count_h3 += 1
            if count_h3 <= 3:
                print(count_h3, "", ele_h3.text)
        print("Hay elementos de tipo H3 ", count_h3)

    def bbcmundolistas(self):
        count = 0
        for ele_li in self.driver.find_elements_by_tag_name("li"):
            print(ele_li.text)
            count += 1
        print("hay ", count, " li")

    def acepted_cookie(self):
        self.driver.find_element_by_xpath("//button[normalize-space()='Aceptar todas']").click()

    def send_keys(self, email="test@test.com", pwd="holamundo"):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='email']")))
        input_email = self.driver.find_element_by_xpath("//input[@id='email']")
        input_email.send_keys(email)

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='pass']")))
        input_pass = self.driver.find_element_by_xpath("//input[@id='pass']")
        input_pass.send_keys(pwd)

        self.driver.find_element_by_xpath("//button[normalize-space()='Entrar']").click()

    def show_link(self):
        count = 0
        print("cantidad de parrafos")
        for ele_parrafo in self.driver.find_elements_by_tag_name("a"):
            count += 1
            print(ele_parrafo.text)
        print("hay ", count, " parrafos")

    def show_div(self):
        count = 0
        print("cantidad de div's")
        for i in self.driver.find_elements_by_tag_name("div"):
            count += 1
        print("cantidad de div's: ", count)

    def show_button(self):
        count = 0
        print("cantidad de botones")
        for i in self.driver.find_elements_by_tag_name("button"):
            print(i.text)
            count += 1
        print("cantidad de botones: ", count)

    def max_window(self):
        self.driver.maximize_window()

    def refres_screen(self):
        self.driver.refresh()

    def go_forward(self):
        print("voy adelante")
        self.driver.forward()

    def go_back(self):
        print("voy atrás")
        self.driver.back()

    def quit_driver(self):
        self.driver.quit()
