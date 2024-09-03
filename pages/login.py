from playwright.sync_api import Page
from pages.locatores import *

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator(username_login_field)
        self.password_input = page.locator(password_login_field)
        self.login_button = page.locator(button_login_field)

    def login(self, username_input, password_input):
        self.username_input.fill(username_input)
        self.password_input.fill(password_input)
        self.login_button.click()