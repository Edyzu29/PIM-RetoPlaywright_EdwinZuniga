from faker import Faker
import secrets
import string

# Crear una instancia de Faker
fake = Faker('es_ES')  

def name_rng() -> str:
    return fake.name()

def user_rng() -> str:
    return fake.user_name()

def password_rng(long = 8) -> str:
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(caracteres) for i in range(long))