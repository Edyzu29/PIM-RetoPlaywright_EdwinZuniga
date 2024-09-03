from playwright.sync_api import Page
from pages.locatores import *

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.button_admin = page.locator(button_admin_field)
        self.button_add_worker = page.locator(button_add_worker_field)

    def admin_page(self):
        self.button_admin.click()
        self.button_add_worker.click()