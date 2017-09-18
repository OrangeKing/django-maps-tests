from behave import *

from page_objects.register_page import RegisterPage


@given("app is open")
def check_app_open(context):
    pass


@when("I fill sign up form with generated credentials")
def fill_reg_form(context):
    RegisterPage(context.driver).fill_fields(
        context.username, context.password, context.email)


@when("I stop the music form playing in the background")
def stop_music(context):
    RegisterPage(context.driver).stop_music()


@then("I press submit button on sign up form")
def submit_reg(context):
    RegisterPage(context.driver).press_submit()
