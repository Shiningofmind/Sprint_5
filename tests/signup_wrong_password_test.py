from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from helpers import generate_email, generate_name, generate_wrong_password
from urls import UrlsList
from locators import TestLocators
class TestSingWrongPassword:
    def test_sing_wrong_password(self, driver):
        name = generate_name()
        mail = generate_email()
        wrong_password = generate_wrong_password()
        driver.get(UrlsList.main_page)
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(UrlsList.main_page))
        driver.find_element(By.XPATH, TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(UrlsList.authorization))
        driver.find_element(By.XPATH, TestLocators.REGISTER_TEXT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(UrlsList.registration))
        driver.find_element(By.XPATH, TestLocators.INPUT_NAME).send_keys(name)
        driver.find_element(By.XPATH, TestLocators.INPUT_EMAIL).send_keys(mail)
        driver.find_element(By.XPATH, TestLocators.INPUT_PASS).send_keys(wrong_password)
        driver.find_element(By.XPATH, TestLocators.REGISTER_BUTTON).click()
        assert driver.find_element(By.XPATH, TestLocators.ERROR_PASS_SELECT).text == 'Некорректный пароль'
