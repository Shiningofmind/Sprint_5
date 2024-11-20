from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://stellarburgers.nomoreparties.site/login')
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys("nelli_malyutina_12_627@yandex.ru")
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys("9wDnfy")
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click()
sleep(2)
driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
driver.find_element(By.LINK_TEXT, "Конструктор").click()
sleep(5)
driver.quit()