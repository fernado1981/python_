class dashboard_orangeHrm:
    locators = {
        "xpath_dashboard_header": "//h1[contains(text(),'Dashboard')]",
    }

    def __init__(self):
        self.dashboardheader = self.locators["xpath_dashboard_header"]

    def dashboard_header(self, context):
        text = context.web.get_text_xpath(self.dashboardheader)
        if text == "Dashboard":
            return True
        return False
