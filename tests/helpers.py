import random
import string

def generate_email():
        random_digits = random.randint(100, 999)
        return f"nelli_malyutina_12_{random_digits}@yandex.ru"
def generate_password(length=6):
        characters = string.ascii_letters + string.digits
        return ''.join(random.sample(characters, length))
def generate_wrong_password(length=4):
        characters = string.ascii_letters + string.digits
        return ''.join(random.sample(characters, length))
def generate_name(length=5):
        characters = string.ascii_letters
        return ''.join(random.sample(characters, length))