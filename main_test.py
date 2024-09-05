from test_add_new_worker import *

Challenge_ntt = Orange_testing()
print("#############Pruebas de Valores###################")
Challenge_ntt.username_5to40_caracteres(1)
Challenge_ntt.username_less_2_caracteres(2)
Challenge_ntt.username_more_40_caracteres(3)
Challenge_ntt.username_only_numbers_caracteres(4)
Challenge_ntt.username_random_space(5)
Challenge_ntt.username_special_caracter(6)
Challenge_ntt.username_with_dot(7)
Challenge_ntt.username_with_coma(8)
Challenge_ntt.username_with_dash(9)
Challenge_ntt.username_empty(10)

print("##################Casos de Prueba##################")
Challenge_ntt.creat_new_employee_details(5)
Challenge_ntt.cheack_id_employee(6)
Challenge_ntt.creat_new_employee_simple(7)