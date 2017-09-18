from behave import *

from page_objects.register_page import RegisterPage


@when("I click register button")
def open_register(context):
    RegisterPage(context.driver).open_register()
