from playwright.sync_api import sync_playwright
from pages.login import *
from pages.PIM import *
from data import *
import time

def test_add_new_worker():

    with sync_playwright() as pw:

        browser = pw.chromium.launch(headless=False)
        driver = browser.new_page()

        login_page = LoginPage(driver)
        pim_page = PIMPage(driver)

        driver.goto(url_login)
        login_page.login(username_input=username, password_input=password)

        fname, lname, mname, uname = name_rng()
        id_employee = id_genetaror()
        
        password_employee = password_rng()

        pim_page.pim_page()
        pim_page.add_employee(fname=fname, mname= mname, lname=lname, id_employee=id_employee)
        time.sleep(4)
        pim_page.add_employee_details(uname=uname, password=password_employee)
        time.sleep(4)
        pim_page.save_cancel_employee()
        time.sleep(4)
        pim_page.searh_employee(id_employee=id_employee)
        time.sleep(4)
        pim_page.check_search(id_employee=id_employee)
        time.sleep(4)

        driver.close()
        
test_add_new_worker()