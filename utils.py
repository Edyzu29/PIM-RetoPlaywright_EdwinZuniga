from faker import Faker
import secrets
import string
import random

# Crear una instancia de Faker
fake = Faker('es_ES')  

def name_rng() -> tuple:
    fake = Faker()
    full_name = fake.name()

    name_parts = full_name.split()

    first_name = name_parts[0]
    last_name = name_parts[-1]

    middle_name = name_parts[1]

    username = first_name[:1] + last_name.lower() + str(random.randint(0,99))
    
    return first_name, last_name, middle_name,username

def password_rng(long = 8) -> str:

    caracteres = string.ascii_letters + string.digits + string.punctuation + string.ascii_letters.upper()
    password = ''.join(secrets.choice(caracteres) for i in range(long))

    password += password + str(random.randint(0,99))

    return password

def id_genetaror() -> str:

    id_raw = random.randint(0,1000)
    id_full = f'{id_raw:04}'

    return id_full