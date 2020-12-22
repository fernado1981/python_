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


@then('User must succesfully login to the Dashboard page')
def Dashboard(context):
    text = context.web.get_text("//h1[contains(text(),'Dashboard')]")
    assert text == "Dashboard"
    context.web.close()
