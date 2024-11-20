import random
import string
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
def generate_email():
    random_digits = random.randint(100, 999)
    return f"nelli_malyutina_12_{random_digits}@yandex.ru"
def generate_password(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.sample(characters, length))
email = generate_email()
password = generate_password()
driver.get('https://stellarburgers.nomoreparties.site/')
driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys("Nelli")
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(email)
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input").send_keys(password)
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click()
sleep(2)
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys(email)
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(password)
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click()
sleep(2)
driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
sleep(5)
driver.quit()