from behave import *
from utils import open_browser, close_browser, go_to_login_page, login
from selenium.webdriver.common.by import By

@given('I am on the login page')
def step_impl(context):
    go_to_login_page(context)
    login_button = context.login_page.driver.find_element(By.ID, "login-button")
    assert login_button.get_attribute("name") == "login-button"
    assert login_button.get_attribute("value") == "Login"

@when('I fill in "username" with "{username}"')
def step_impl(context, username):
    context.login_page.enter_username(username)

@when('I fill in "Password" with "{pwd}"')
def step_impl(context,pwd):
    context.login_page.enter_password(pwd)

@when('I press "Login"')
def step_impl(context):
    context.login_page.click_login()

@then('I should see "{message_type}" with this "{message}"')
def step_impl(context, message_type, message):
    if message_type == 'positive':
        products_header = context.login_page.driver.find_element(By.CLASS_NAME, "title")
        assert products_header.text == message

    elif message_type == 'negative':
        error_message = context.login_page.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
        assert error_message.text == message
        

@when(u'I fill in "username" with ""')
def step_impl(context):
    pass


@when(u'I fill in "Password" with ""')
def step_impl(context):
    pass