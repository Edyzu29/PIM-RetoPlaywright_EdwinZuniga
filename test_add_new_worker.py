from playwright.sync_api import sync_playwright
from pages.login import *
from pages.PIM import *
from data import *
import time

class Orange_testing:

    def __init__(self) -> None:
        self.fname, self.lname, self.mname, self.uname = name_rng()
        self.id_employee = id_genetaror()
        self.password_employee = password_rng()
        self.pause = 2

    #Pruebas de valores
    def username_5to40_caracteres(self, valor_prueba):

        with sync_playwright() as pw:

            try:

                browser = pw.chromium.launch(headless=False)
                driver = browser.new_page()

                login_page = LoginPage(driver)
                pim_page = PIMPage(driver)

                driver.goto(url_login)
                login_page.login(username_input=username, password_input=password)

                long_user = random.randint(5,40)
                uname_test = "a" * long_user

                pim_page.pim_page()
                pim_page.add_employee(fname=self.fname, mname= self.mname, lname=self.lname, id_employee=self.id_employee)
                time.sleep(self.pause)
                pim_page.msg_alert_id()
                time.sleep(self.pause)
                pim_page.add_employee_details(uname=uname_test, password=self.password_employee)
                time.sleep(self.pause)
                pim_page.save_cancel_employee()
                result_name, result_last = pim_page.check_creation()

                successfull_creation = ((self.fname==result_name)and(self.lname==result_last))

                assert successfull_creation, f'La cuenta del trabajador: la cuenta detallada del trabajador: \"{self.fname} {self.lname}\" no ha sido creadacon un username de {long_user} caracteres'

                print(f"Prueba de valores  {valor_prueba} Pasada: la cuenta detallada del empleado: \"{self.fname} {self.lname}\" ha sido creada con un username de {long_user} caracteres")

            except AssertionError as error:

                print(f"Prueba de valores  {valor_prueba} no Pasada: {error}")

            finally: 

                driver.close()

    def username_less_2_caracteres(self, valor_prueba):

        with sync_playwright() as pw:

            try:

                browser = pw.chromium.launch(headless=False)
                driver = browser.new_page()

                login_page = LoginPage(driver)
                pim_page = PIMPage(driver)

                driver.goto(url_login)
                login_page.login(username_input=username, password_input=password)

                a:str
                long_user = random.randint(0,4)
                uname_test = "a" * long_user

                pim_page.pim_page()
                pim_page.add_employee(fname=self.fname, mname= self.mname, lname=self.lname, id_employee=self.id_employee)
                time.sleep(self.pause)
                pim_page.msg_alert_id()
                time.sleep(self.pause)
                pim_page.add_employee_details(uname=uname_test, password=self.password_employee)
                time.sleep(self.pause)
                pim_page.save_cancel_employee()
                result_name, result_last = pim_page.check_creation()

                successfull_creation = ((self.fname==result_name)and(self.lname==result_last))

                if successfull_creation:

                    error = f'La cuenta del trabajador: la cuenta detallada del trabajador: \"{self.fname} {self.lname}\" ha sido creadacon un username de {long_user} caracteres'
                    print(f"Prueba de valores  {valor_prueba} Pasada: {error}")

            except Exception as e:

                print(f"Prueba de valores  {valor_prueba} no Pasada: la cuenta detallada del empleado: \"{self.fname} {self.lname}\" no ha sido creada con un username de {long_user} caracteres")

            finally: 

                driver.close()

    def username_more_40_caracteres(self, valor_prueba):

        with sync_playwright() as pw:

            try:

                browser = pw.chromium.launch(headless=False)
                driver = browser.new_page()

                login_page = LoginPage(driver)
                pim_page = PIMPage(driver)

                driver.goto(url_login)
                login_page.login(username_input=username, password_input=password)

                a:str
                long_user = random.randint(10,40)
                uname_test = "a" * long_user

                pim_page.pim_page()
                pim_page.add_employee(fname=self.fname, mname= self.mname, lname=self.lname, id_employee=self.id_employee)
                time.sleep(self.pause)
                pim_page.msg_alert_id()
                time.sleep(self.pause)
                pim_page.add_employee_details(uname=uname_test, password=self.password_employee)
                time.sleep(self.pause)
                pim_page.save_cancel_employee()
                result_name, result_last = pim_page.check_creation()

                successfull_creation = ((self.fname==result_name)and(self.lname==result_last))

                if successfull_creation:
                    error = f'La cuenta del trabajador: la cuenta detallada del trabajador: \"{self.fname} {self.lname}\" ha sido creadacon un username de {long_user} caracteres'
                    print(f"Prueba de valores  {valor_prueba} Pasada: {error}")

            except Exception as e:

                print(f"Prueba de valores  {valor_prueba} no Pasada: la cuenta detallada del empleado: \"{self.fname} {self.lname}\" no ha sido creada con un username de {long_user} caracteres")

            finally: 

                driver.close()

    def username_only_numbers_caracteres(self, valor_prueba):

        with sync_playwright() as pw:

            try:

                browser = pw.chromium.launch(headless=False)
                driver = browser.new_page()

                login_page = LoginPage(driver)
                pim_page = PIMPage(driver)

                driver.goto(url_login)
                login_page.login(username_input=username, password_input=password)

                long_user = random.randint(0,1000)
                uname_test =  str(long_user)

                pim_page.pim_page()
                pim_page.add_employee(fname=self.fname, mname= self.mname, lname=self.lname, id_employee=self.id_employee)
                time.sleep(self.pause)
                pim_page.msg_alert_id()
                time.sleep(self.pause)
                pim_page.add_employee_details(uname=uname_test, password=self.password_employee)
                time.sleep(self.pause)
                pim_page.save_cancel_employee()
                result_name, result_last = pim_page.check_creation()

                successfull_creation = ((self.fname==result_name)and(self.lname==result_last))

                if successfull_creation:
                    error = f'La cuenta del trabajador: la cuenta detallada del trabajador: \"{self.fname} {self.lname}\" ha sido creadacon un username con solo numeros {long_user}'

                    print(f"Prueba de valores  {valor_prueba} Pasada: {error}")

            except Exception as e:

                print(f"Prueba de valores  {valor_prueba} no Pasada: la cuenta detallada del empleado: \"{self.fname} {self.lname}\" no ha sido creada con un username con solo numeros {long_user}")

            finally: 

                driver.close()

    def username_random_space(self, valor_prueba):

        with sync_playwright() as pw:

            try:

                browser = pw.chromium.launch(headless=False)
                driver = browser.new_page()

                login_page = LoginPage(driver)
                pim_page = PIMPage(driver)

                driver.goto(url_login)
                login_page.login(username_input=username, password_input=password)

                uname_test =  add_random_space(self.uname)

                pim_page.pim_page()
                pim_page.add_employee(fname=self.fname, mname= self.mname, lname=self.lname, id_employee=self.id_employee)
                time.sleep(self.pause)
                pim_page.msg_alert_id()
                time.sleep(self.pause)
                pim_page.add_employee_details(uname=uname_test, password=self.password_employee)
                time.sleep(self.pause)
                pim_page.save_cancel_employee()
                result_name, result_last = pim_page.check_creation()

                successfull_creation = ((self.fname==result_name)and(self.lname==result_last))

                if successfull_creation: 

                    error = f'La cuenta del trabajador: la cuenta detallada del trabajador: \"{self.fname} {self.lname}\" ha sido creadacon un username con epacio {uname_test}'

                    print(f"Prueba de valores  {valor_prueba} Pasada: {error}")

            except Exception as e:

                print(f"Prueba de valores  {valor_prueba} no Pasada: la cuenta detallada del empleado: \"{self.fname} {self.lname}\" no ha sido creada con un username con epacio {uname_test}")

            finally: 

                driver.close()

    def username_special_caracter(self, valor_prueba):

        with sync_playwright() as pw:

            try:

                browser = pw.chromium.launch(headless=False)
                driver = browser.new_page()

                login_page = LoginPage(driver)
                pim_page = PIMPage(driver)

                driver.goto(url_login)
                login_page.login(username_input=username, password_input=password)

                uname_test =  self.uname + "ñ"

                pim_page.pim_page()
                pim_page.add_employee(fname=self.fname, mname= self.mname, lname=self.lname, id_employee=self.id_employee)
                time.sleep(self.pause)
                pim_page.msg_alert_id()
                time.sleep(self.pause)
                pim_page.add_employee_details(uname=uname_test, password=self.password_employee)
                time.sleep(self.pause)
                pim_page.save_cancel_employee()
                result_name, result_last = pim_page.check_creation()

                successfull_creation = ((self.fname==result_name)and(self.lname==result_last))

                if successfull_creation:
                    
                    error = f'La cuenta del trabajador: la cuenta detallada del trabajador: \"{self.fname} {self.lname}\" ha sido creadacon un username con un caracter especial {uname_test}'

                    print(f"Prueba de valores  {valor_prueba} Pasada: {error}")

            except Exception as e:

                print(f"Prueba de valores  {valor_prueba} no Pasada: la cuenta detallada del empleado: \"{self.fname} {self.lname}\" no ha sido creada con un username con un caracter especial {uname_test}")

            finally: 

                driver.close()

    def username_with_dot(self, valor_prueba):

        with sync_playwright() as pw:

            try:

                browser = pw.chromium.launch(headless=False)
                driver = browser.new_page()

                login_page = LoginPage(driver)
                pim_page = PIMPage(driver)

                driver.goto(url_login)
                login_page.login(username_input=username, password_input=password)

                uname_test =  self.uname + "."

                pim_page.pim_page()
                pim_page.add_employee(fname=self.fname, mname= self.mname, lname=self.lname, id_employee=self.id_employee)
                time.sleep(self.pause)
                pim_page.msg_alert_id()
                time.sleep(self.pause)
                pim_page.add_employee_details(uname=uname_test, password=self.password_employee)
                time.sleep(self.pause)
                pim_page.save_cancel_employee()
                result_name, result_last = pim_page.check_creation()

                successfull_creation = ((self.fname==result_name)and(self.lname==result_last))

                if successfull_creation:
                    error = f'La cuenta del trabajador: la cuenta detallada del trabajador: \"{self.fname} {self.lname}\" ha sido creadacon un username con un \".\" {uname_test}'

                    print(f"Prueba de valores  {valor_prueba} Pasada: {error}")

            except Exception as e:

                print(f"Prueba de valores  {valor_prueba} no Pasada: la cuenta detallada del empleado: \"{self.fname} {self.lname}\" no ha sido creada con un username con un \".\" {uname_test}")

            finally: 

                driver.close()

    def username_with_coma(self, valor_prueba):

        with sync_playwright() as pw:

            try:

                browser = pw.chromium.launch(headless=False)
                driver = browser.new_page()

                login_page = LoginPage(driver)
                pim_page = PIMPage(driver)

                driver.goto(url_login)
                login_page.login(username_input=username, password_input=password)

                uname_test =  self.uname + ","

                pim_page.pim_page()
                pim_page.add_employee(fname=self.fname, mname= self.mname, lname=self.lname, id_employee=self.id_employee)
                time.sleep(self.pause)
                pim_page.msg_alert_id()
                time.sleep(self.pause)
                pim_page.add_employee_details(uname=uname_test, password=self.password_employee)
                time.sleep(self.pause)
                pim_page.save_cancel_employee()
                result_name, result_last = pim_page.check_creation()

                successfull_creation = ((self.fname==result_name)and(self.lname==result_last))

                if successfull_creation:

                    error = f'La cuenta del trabajador: la cuenta detallada del trabajador: \"{self.fname} {self.lname}\" ha sido creadacon un username con un \",\" {uname_test}'

                    print(f"Prueba de valores  {valor_prueba} Pasada: {error}")

            except Exception as e:

                print(f"Prueba de valores  {valor_prueba} no Pasada: la cuenta detallada del empleado: \"{self.fname} {self.lname}\" no ha sido creada con un username con un \",\" {uname_test}")

            finally: 

                driver.close()

    def username_with_dash(self, valor_prueba):

        with sync_playwright() as pw:

            try:

                browser = pw.chromium.launch(headless=False)
                driver = browser.new_page()

                login_page = LoginPage(driver)
                pim_page = PIMPage(driver)

                driver.goto(url_login)
                login_page.login(username_input=username, password_input=password)

                uname_test =  self.uname + "-"

                pim_page.pim_page()
                pim_page.add_employee(fname=self.fname, mname= self.mname, lname=self.lname, id_employee=self.id_employee)
                time.sleep(self.pause)
                pim_page.msg_alert_id()
                time.sleep(self.pause)
                pim_page.add_employee_details(uname=uname_test, password=self.password_employee)
                time.sleep(self.pause)
                pim_page.save_cancel_employee()
                result_name, result_last = pim_page.check_creation()

                successfull_creation = ((self.fname==result_name)and(self.lname==result_last))

                if successfull_creation:
                    error = f'La cuenta del trabajador: la cuenta detallada del trabajador: \"{self.fname} {self.lname}\" ha sido creadacon un username con un \"-\" {uname_test}'

                    print(f"Prueba de valores  {valor_prueba} Pasada: {error}")

            except Exception as e:

                 print(f"Prueba de valores  {valor_prueba} no Pasada: la cuenta detallada del empleado: \"{self.fname} {self.lname}\" no ha sido creada con un username con un \"-\" {uname_test}")


            finally: 

                driver.close()

    def username_empty(self, valor_prueba):

        with sync_playwright() as pw:

            try:

                browser = pw.chromium.launch(headless=False)
                driver = browser.new_page()

                login_page = LoginPage(driver)
                pim_page = PIMPage(driver)

                driver.goto(url_login)
                login_page.login(username_input=username, password_input=password)

                uname_test =  ""

                pim_page.pim_page()
                pim_page.add_employee(fname=self.fname, mname= self.mname, lname=self.lname, id_employee=self.id_employee)
                time.sleep(self.pause)
                pim_page.msg_alert_id()
                time.sleep(self.pause)
                pim_page.add_employee_details(uname=uname_test, password=self.password_employee)
                time.sleep(self.pause)
                pim_page.save_cancel_employee()
                result_name, result_last = pim_page.check_creation()

                successfull_creation = ((self.fname==result_name)and(self.lname==result_last))

                if successfull_creation:
                    error = f'La cuenta del trabajador: la cuenta detallada del trabajador: \"{self.fname} {self.lname}\" ha sido creadacon un username con un \"\" {uname_test}'

                    print(f"Prueba de valores  {valor_prueba} Pasada: {error}")

            except Exception as e:

                print(f"Prueba de valores  {valor_prueba} no Pasada: la cuenta detallada del empleado: \"{self.fname} {self.lname}\" no ha sido creada con un username con un \"\" {uname_test}")

            finally: 

                driver.close()

    #Prueba de casos
    def creat_new_employee_details(self, caso_prueba : int):

        with sync_playwright() as pw:

            try:

                browser = pw.chromium.launch(headless=False)
                driver = browser.new_page()

                login_page = LoginPage(driver)
                pim_page = PIMPage(driver)

                driver.goto(url_login)
                login_page.login(username_input=username, password_input=password)

                pim_page.pim_page()
                pim_page.add_employee(fname=self.fname, mname= self.mname, lname=self.lname, id_employee=self.id_employee)
                time.sleep(self.pause)
                pim_page.msg_alert_id()
                time.sleep(self.pause)
                pim_page.add_employee_details(uname=self.uname, password=self.password_employee)
                time.sleep(self.pause)
                pim_page.save_cancel_employee()
                result_name, result_last = pim_page.check_creation()

                successfull_creation = ((self.fname==result_name)and(self.lname==result_last))

                assert successfull_creation, f'La cuenta del trabajador: la cuenta detallada del trabajador: \"{self.fname} {self.lname}\" no ha sido creada'

                print(f"Caso de Prueba {caso_prueba} Pasada: la cuenta detallada del empleado: \"{self.fname} {self.lname}\" ha sido creada")

            except AssertionError as error:

                print(f"Caso de Prueba {caso_prueba} no Pasada: {error}")

            finally: 

                driver.close()

    def cheack_id_employee(self, caso_prueba : int):

        with sync_playwright() as pw:

            try:

                browser = pw.chromium.launch(headless=False)
                driver = browser.new_page()

                login_page = LoginPage(driver)
                pim_page = PIMPage(driver)

                driver.goto(url_login)
                login_page.login(username_input=username, password_input=password)

                pim_page.pim_page()
                time.sleep(self.pause)
                pim_page.searh_employee(id_employee=self.id_employee)
                time.sleep(self.pause)
                result = pim_page.check_search()

                assert result == self.id_employee, f'No existe un trabajador con el id: {self.id_employee}'

                print(f"Caso de Prueba {caso_prueba} Pasada: el Empleado con el id {self.id_employee} si existe")

            except AssertionError as error:

                print(f"Caso de Prueba {caso_prueba} no Pasada: {error}")

            finally: 

                driver.close()

    def creat_new_employee_simple(self, caso_prueba : int):

        fname, lname, mname, uname = name_rng()
        id_employee = id_genetaror()

        with sync_playwright() as pw:

            try:

                browser = pw.chromium.launch(headless=False)
                driver = browser.new_page()

                login_page = LoginPage(driver)
                pim_page = PIMPage(driver)

                driver.goto(url_login)
                login_page.login(username_input=username, password_input=password)

                pim_page.pim_page()
                pim_page.add_employee(fname=fname, mname= mname, lname=lname, id_employee=id_employee)
                time.sleep(self.pause)
                pim_page.msg_alert_id()
                time.sleep(self.pause)
                pim_page.save_cancel_employee()
                result_name, result_last = pim_page.check_creation()

                successfull_creation = ((fname==result_name)and(lname==result_last))

                assert successfull_creation, f'La cuenta del trabajador: la cuenta simple del trabajador: {fname} {lname} no ha sido creada'

                print(f"Caso de Prueba {caso_prueba} Pasada: la cuenta simple del empleado: \"{fname} {lname}\" ha sido creada")

            except AssertionError as error:

                print(f"Caso de Prueba {caso_prueba} no Pasada: {error}")

            finally: 

                driver.close()
