from selenium import webdriver
from web.web import Web


def browser_chrome(context, timeout=30, **kwargs):
    #Chrome
    browser = webdriver.Chrome()
    #Firefox
    #browser = webdriver.Firefox()
    web = Web(browser)
    context.web = web
    yield context.web
    browser.quit()
