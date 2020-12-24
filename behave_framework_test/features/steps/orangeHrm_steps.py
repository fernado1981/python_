from behave import when, then


@when('the user verify the title page "{titlePage}"')
def title_page(context, titlePage):
    title = context.web.get_title()
    assert title == titlePage


@then('verify that the logo present on page')
def verifyLogo(context):
    logo = context.web.find_by_xpath_displayed("//div[@id='divLogo']//img")
    assert logo is True


# Login
@when('Enter username "{user}" and password "{pwd}"')
def login(context, user, pwd):
    userName = context.web.find_by_id_displayed("txtUsername")
    password = context.web.find_by_id_displayed("txtPassword")
    if userName is True and password is True:
        context.web.find_by_id("txtUsername").send_keys(user)
        context.web.find_by_id("txtPassword").send_keys(pwd)


# login table with header
@when('put username "{name}" and password "{pwd}"')
def login_table(context, name, pwd):
    for row in context.table:
        context.temp_name = row['name']
        context.temp_password = row['pwd']
        userName = context.web.find_by_id_displayed("txtUsername")
        password = context.web.find_by_id_displayed("txtPassword")
        if userName is True and password is True:
            context.web.find_by_id("txtUsername").send_keys(context.temp_name)
            context.web.find_by_id("txtPassword").send_keys(context.temp_password)


# login outline valid
@when('insert username "{name}" and password "{pwd}"')
def login_outline(context, name, pwd):
    context.temp_name = name
    context.temp_password = pwd
    userName = context.web.find_by_id_displayed("txtUsername")
    password = context.web.find_by_id_displayed("txtPassword")
    if userName is True and password is True:
        context.web.find_by_id("txtUsername").send_keys(context.temp_name)
        context.web.find_by_id("txtPassword").send_keys(context.temp_password)


# finish valid login
@then('User must succesfully login to the Dashboard page')
def Dashboard(context):
    text = context.web.get_text_xpath("(//h1[contains(text(),'Dashboard')])")
    if text == "Dashboard":
        assert True


# finish invalid login
@then('User must unsuccesfully login to the Dashboard page')
def Dashboard(context):
    message = context.web.get_text_xpath("//span[@id='spanMessage']")
    if message == "Invalid credentials":
        assert True
