from playwright.sync_api import sync_playwright
from pages.login import *
from data import *
import time

def test_add_new_worker():

    with sync_playwright() as pw:

        browser = pw.chromium.launch(headless=False)
        driver = browser.new_page()
        login_page = LoginPage(driver)
        driver.goto(url_login)
        login_page.login(username_input=username, password_input=password)

        #driver.close()
        time.sleep(5)

test_add_new_worker()