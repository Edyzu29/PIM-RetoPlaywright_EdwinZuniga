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

        pause = 2

        pim_page.pim_page()
        pim_page.add_employee(fname=fname, mname= mname, lname=lname, id_employee=id_employee)
        time.sleep(pause)
        pim_page.add_employee_details(uname=uname, password=password_employee)
        time.sleep(pause)
        pim_page.save_cancel_employee()
        time.sleep(pause)
        pim_page.searh_employee(id_employee=id_employee)
        time.sleep(pause)
        pim_page.check_search()
        time.sleep(pause)

        driver.close()


class Orange_testing:

    def __init__(self) -> None:
        self.fname, self.lname, self.mname, self.uname = name_rng()
        self.id_employee = id_genetaror()
        self.password_employee = password_rng()
        self.pause = 2

    #Pruebas de valores

    #Prueba de casos
    def creat_new_employee(self):

        with sync_playwright() as pw:


test_add_new_worker()