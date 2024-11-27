from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from data import User
from urls import UrlsList
from locators import TestLocators

def test_transfer(driver):
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
    driver.find_element(By.XPATH, TestLocators.CONSTRUCTOR_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(UrlsList.main_page))
    assert driver.current_url == UrlsList.main_page