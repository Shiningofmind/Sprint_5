from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from data import User
from urls import UrlsList
from locators import TestLocators

class TestSinginMainPage:
    def test_singin_mainpage_button(self, driver):
        mail = User.my_email
        password = User.my_password
        driver.get(UrlsList.main_page)
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(UrlsList.main_page))
        driver.find_element(By.XPATH, TestLocators.ENTER_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(UrlsList.authorization))
        driver.find_element(By.XPATH, TestLocators.INPUT_EMAIL).send_keys(mail)
        driver.find_element(By.XPATH, TestLocators.INPUT_PASS).send_keys(password)
        driver.find_element(By.XPATH, TestLocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(UrlsList.main_page))
        driver.find_element(By.XPATH, TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(UrlsList.profile))
        assert driver.current_url == UrlsList.profile

class TestSinginLogin:
    def test_singin_login(self, driver):
        mail = User.my_email
        password = User.my_password
        driver.get(UrlsList.authorization)
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(UrlsList.authorization))
        driver.find_element(By.XPATH, TestLocators.INPUT_EMAIL).send_keys(mail)
        driver.find_element(By.XPATH, TestLocators.INPUT_PASS).send_keys(password)
        driver.find_element(By.XPATH, TestLocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(UrlsList.main_page))
        driver.find_element(By.XPATH, TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(UrlsList.profile))
        assert driver.current_url == UrlsList.profile

class TestSinginRegister:
    def test_singin_register(self, driver):
        mail = User.my_email
        password = User.my_password
        driver.get(UrlsList.registration)
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(UrlsList.registration))
        driver.find_element(By.XPATH, TestLocators.ENTER_TEXT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(UrlsList.authorization))
        driver.find_element(By.XPATH, TestLocators.INPUT_EMAIL).send_keys(mail)
        driver.find_element(By.XPATH, TestLocators.INPUT_PASS).send_keys(password)
        driver.find_element(By.XPATH, TestLocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(UrlsList.main_page))
        driver.find_element(By.XPATH, TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(UrlsList.profile))
        assert driver.current_url == UrlsList.profile

class TestSinginForgotPassword:
    def test_singin_forgot_password(self, driver):
        mail = User.my_email
        password = User.my_password
        driver.get(UrlsList.recovery_pass)
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(UrlsList.recovery_pass))
        driver.find_element(By.XPATH, TestLocators.ENTER_TEXT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(UrlsList.authorization))
        driver.find_element(By.XPATH, TestLocators.INPUT_EMAIL).send_keys(mail)
        driver.find_element(By.XPATH, TestLocators.INPUT_PASS).send_keys(password)
        driver.find_element(By.XPATH, TestLocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(UrlsList.main_page))
        driver.find_element(By.XPATH, TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(UrlsList.profile))
        assert driver.current_url == UrlsList.profile














