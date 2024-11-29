from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from helpers import generate_email, generate_name, generate_password
from urls import UrlsList
from locators import TestLocators
class TestSingup:
    def test_singup(self, driver):
        name = generate_name()
        mail = generate_email()
        password = generate_password()
        driver.get(UrlsList.main_page)
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(UrlsList.main_page))
        driver.find_element(By.XPATH, TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(UrlsList.authorization))
        driver.find_element(By.XPATH, TestLocators.REGISTER_TEXT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(UrlsList.registration))
        driver.find_element(By.XPATH, TestLocators.INPUT_NAME).send_keys(name)
        driver.find_element(By.XPATH, TestLocators.INPUT_EMAIL).send_keys(mail)
        driver.find_element(By.XPATH, TestLocators.INPUT_PASS).send_keys(password)
        driver.find_element(By.XPATH, TestLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(UrlsList.authorization))
        driver.find_element(By.XPATH, TestLocators.INPUT_EMAIL).send_keys(mail)
        driver.find_element(By.XPATH, TestLocators.INPUT_PASS).send_keys(password)
        driver.find_element(By.XPATH, TestLocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(UrlsList.main_page))
        driver.find_element(By.XPATH, TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(UrlsList.profile))
        assert driver.current_url == UrlsList.profile