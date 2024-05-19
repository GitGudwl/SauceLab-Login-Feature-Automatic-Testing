# utils.py
from selenium import webdriver
from login_page import LoginPage  # Importing the updated LoginPage class

def open_browser(context):
    context.browser = webdriver.Chrome()

def close_browser(context):
    context.browser.quit()

def go_to_login_page(context):
    context.browser.get("https://www.saucedemo.com")
    context.login_page = LoginPage(context.browser)  # Instantiate the LoginPage class

def login(context, username, password):
    context.login_page.enter_username(username)
    context.login_page.enter_password(password)
    context.login_page.click_login()
