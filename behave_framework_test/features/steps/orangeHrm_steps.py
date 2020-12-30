from behave import when, then

from page_objects.orangeHrm.home_orangeHrm import home
from page_objects.orangeHrm.dashboard_orangeHrm import dashboard_orangeHrm


@when('the user verify the title page "{titlePage}"')
def title_page(context, titlePage):
    title = context.web.get_title()
    assert title == titlePage


@then('verify that the logo present on page')
def verifyLogo(context):
    logo = home()
    result = logo.view_logo(context)
    assert result is True


# Login
@when('Enter username "{user}" and password "{pwd}"')
def login(context, user, pwd):
    login = home()
    result = login.simple_login_home(context, user, pwd)
    assert result is True


# login table with header
@when('put username "{name}" and password "{pwd}"')
def login_table(context, name, pwd):
    login = home()
    result = login.table_login_home(context, name, pwd)
    assert result is True


# login outline valid
@when('insert username "{user}" and password "{pwd}"')
def login_outline(context, user, pwd):
    login = home()
    result = login.example_login_home(context, user, pwd)
    assert result is True


# finish valid login
@then('User must succesfully login to the Dashboard page')
def Dashboard(context):
    Dashboard = dashboard_orangeHrm()
    dashboard = Dashboard.dashboard_header(context)
    assert dashboard is True


# finish invalid login
@then('User must unsuccesfully login to the Dashboard page')
def login_error(context):
    login = home()
    result = login.invalid_login(context)
    assert result is True
