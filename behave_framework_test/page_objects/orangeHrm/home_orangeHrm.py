from page_objects.orangeHrm.locators_orangeHrm import homeorangeHrm


class home(homeorangeHrm):

    def __init__(self):
        self.username = self.locators["id_username"]
        self.password = self.locators["id_password"]
        self.error_msn = self.locators["xpath_message_error"]
        self.logo = self.locators["xpath_logo"]
        self.btn_login = self.locators["id_btn_login"]

    def simple_login_home(self, context, user, pwd):
        userName = context.web.find_by_id_displayed(self.username)
        password = context.web.find_by_id_displayed(self.password)
        if userName is True and password is True:
            context.web.find_by_id(self.username).send_keys(user)
            context.web.find_by_id(self.password).send_keys(pwd)
            return True
        return False

    def table_login_home(self, context, name, pwd):
        for row in context.table:
            context.temp_name = row['name']
            context.temp_password = row['pwd']
            userName = context.web.find_by_id_displayed("txtUsername")
            password = context.web.find_by_id_displayed("txtPassword")
            if userName is True and password is True:
                context.web.find_by_id("txtUsername").send_keys(context.temp_name)
                context.web.find_by_id("txtPassword").send_keys(context.temp_password)
                return True
            return False

    def example_login_home(self, context, user, pwd):
        context.temp_name = user
        context.temp_password = pwd
        userName = context.web.find_by_id_displayed(self.username)
        password = context.web.find_by_id_displayed(self.password)
        if userName is True and password is True:
            context.web.find_by_id(self.username).send_keys(context.temp_name)
            context.web.find_by_id(self.password).send_keys(context.temp_password)
            return True
        return False

    def invalid_login(self, context):
        message = context.web.get_text_xpath(self.error_msn)
        if message == "Invalid credentials":
            return True
        return False

    def view_logo(self, context):
        logo = context.web.find_by_xpath_displayed(self.logo)
        return logo

    def submit_bottom(self, context):
        context.web.find_by_id(self.btn_login).click()
