from POO.Generic.DriverBrowser import DriverBrowser


class hook(DriverBrowser):
    driver = DriverBrowser.driver

    def openBrowser(self, url='http://wwww.google.es'):
        self.driver.get(url)

    def quitDriver(self):
        self.driver.quit()
