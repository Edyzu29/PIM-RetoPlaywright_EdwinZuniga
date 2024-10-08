from playwright.sync_api import Page
from pages.locatores import *
from utils import *
import time

class PIMPage:
    def __init__(self, page: Page):
        self.page = page

        self.button_pim = page.locator(button_pim_field)
        self.button_add_worker = page.locator(button_add_employee_field)

        self.employee_middle = page.locator(employee_middle_field)
        self.employee_name = page.locator(employee_name_field)
        self.employee_last = page.locator(employee_last_field)
        self.employee_id = page.locator(employee_id_field)

        self.employee_username = page.locator(username_field)
        self.employee_password = page.locator(password_field)
        self.employee_confirmp = page.locator(confirm_password_field)

        self.button_save = page.locator(button_save_add_field)
        self.button_cancel = page.locator(button_cancel_add_field)
        self.switch_details = page.locator(switch_details_field)
        
        self.status_1_employee = page.locator(status_bullet_1_field)
        self.status_2_employee = page.locator(status_bullet_2_field)

        self.search_for_id = page.locator(search_field)
        self.button_search = page.locator(button_search_field)
        self.button_reset = page.locator(button_reset_field)

        self.result_search = page.locator(result_field)

        self.successfully_creation = page.locator(create_successful_field)

        self.msg_id_exist = page.locator(msg_alert_field)

    def pim_page(self):
        self.button_pim.click()
        self.button_add_worker.click()

    def add_employee(self, fname,mname, lname, id_employee):

        self.employee_name.fill(fname)
        self.employee_middle.fill(mname)
        self.employee_last.fill(lname)
        self.employee_id.fill(id_employee)

    def add_employee_details(self, status = True, uname = "" , password = ""):

        self.switch_details.click()

        self.employee_username.fill(uname)
        self.employee_password.fill(password)
        self.employee_confirmp.fill(password)

        if status:
            self.status_1_employee.click()

        else:
            self.status_2_employee.click()

    def save_cancel_employee(self, save = True):

        if save:
            self.button_save.click()
        
        else:
            self.button_cancel.click()

    def searh_employee(self, id_employee, action = True):
        
        self.button_pim.wait_for(state="visible", timeout=5000)
        self.button_pim.click()

        self.search_for_id.wait_for(state="visible", timeout=5000)
        self.search_for_id.fill(id_employee)

        if action:
            self.button_search.click()

        else:
            self.button_reset.click()

    def check_search(self):

        id_result = self.result_search.text_content()
        return id_result
        
    def check_creation(self):

        time.sleep(10)
        employee_name = self.successfully_creation.text_content()

        employee_name_particion = employee_name.split()

        return employee_name_particion[0], employee_name_particion[-1]
    
    def msg_alert_id(self):

        time.sleep(4)
        while self.msg_id_exist.is_visible():
            self.employee_id.clear()
            id_employee = id_genetaror()
            self.employee_id.fill(id_employee)
            time.sleep(4)