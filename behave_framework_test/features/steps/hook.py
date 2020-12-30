from behave import given, when

from page_objects.orangeHrm.home_orangeHrm import home


@given('the user is on the search page "{page}"')
def user_on_search_page(context, page):
    if page == "orangehrmlive":
        context.web.open('http://opensource-demo.orangehrmlive.com/')
    if page == "blazedemo":
        context.web.open("http://blazedemo.com/")


@when('Click on login button')
def submitLoginForm(context):
    submit = home()
    submit.submit_bottom(context)
