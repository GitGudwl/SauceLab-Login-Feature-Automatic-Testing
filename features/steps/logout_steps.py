from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import open_browser, close_browser, go_to_login_page, login
from homepage import HomePageFactory

@given(u'I am logged in and on the dashboard page with "{username}" username and "{pwd}" password')
def step_impl(context, username, pwd):
    go_to_login_page(context)
    context.login_page.enter_username(username)
    context.login_page.enter_password(pwd)
    context.login_page.click_login()
    products_header = context.login_page.driver.find_element(By.CLASS_NAME, "title")
    assert products_header.text == "Products"
    
    # Initialize HomePageFactory and store it in the context
    context.home_page = HomePageFactory(context.login_page.driver)

@when(u'I press the logout button')
def step_impl(context):
    # Use HomePageFactory methods to interact with the page
    context.home_page.click_burger_menu_button()
    context.home_page.click_logout_link()

@then(u'I should be navigated back to the login page')
def step_impl(context):
    login_button = context.login_page.driver.find_element(By.ID, "login-button")
    assert login_button.get_attribute("name") == "login-button"
    assert login_button.get_attribute("value") == "Login"