from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

class HomePageFactory:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_burger_menu_button(self):
        burger_menu_button = self.driver.find_element(By.ID, "react-burger-menu-btn")
        burger_menu_button.click()

    def click_logout_link(self):
        wait = WebDriverWait(self.driver, 10)
        logout_link = wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
        logout_link.click()
