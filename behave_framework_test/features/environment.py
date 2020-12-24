from behave.fixture import use_fixture_by_tag

from web.factory import get_web


# def before_all(context):
#   web = get_web(context.config.userdata['browser'])
#  context.web = web

def before_scenario(context, test):
    web = get_web(context.config.userdata['browser'])
    context.web = web


def after_scenario(context, test):
    context.web.close()
