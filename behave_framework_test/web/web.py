from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Web(object):
    __TIMEOUT = 10

    def __init__(self, web_driver):
        super().__init__()
        self._web_driver_wait = WebDriverWait(web_driver, Web.__TIMEOUT)
        self._web_driver = web_driver

    def open(self, url):
        self._web_driver.get(url)

    def maximize(self):
        self._web_driver.maximize_window()

    def close(self):
        self._web_driver.quit()

    def get_url(self):
        return self._web_driver.current_url

    def get_title(self):
        return self._web_driver.title

    def get_text_xpath(self, xpath):
        return self._web_driver_wait.until(EC.presence_of_element_located((By.XPATH, xpath))).text

    def find_by_xpath(self, xpath):
        return self._web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def find_by_xpath_displayed(self, xpath):
        return self._web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath))).is_displayed()

    def finds_by_xpath_displayed(self, xpath):
        return self._web_driver_wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

    def find_by_id(self, id_value):
        return self._web_driver_wait.until(EC.visibility_of_element_located((By.ID, id_value)))

    def find_by_id_displayed(self, id_value):
        return self._web_driver_wait.until(EC.presence_of_element_located((By.ID, id_value))).is_displayed()
