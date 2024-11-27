from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from urls import UrlsList
from locators import TestLocators

def test_constructor_buns(driver):
    driver.get(UrlsList.main_page)
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(UrlsList.main_page))
    driver.find_element(By.XPATH, TestLocators.SAUCES_TEXT_BUTTON).click()
    driver.find_element(By.XPATH, TestLocators.BUNS_TEXT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(UrlsList.main_page))
    assert driver.find_element(By.XPATH, TestLocators.BUNS_TEXT).text == 'Булки'

def test_constructor_sauces(driver):
    driver.get(UrlsList.main_page)
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(UrlsList.main_page))
    driver.find_element(By.XPATH, TestLocators.SAUCES_TEXT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(UrlsList.main_page))
    assert driver.find_element(By.XPATH, TestLocators.SAUCES_TEXT).text == 'Соусы'

def test_constructor_fillings(driver):
    driver.get(UrlsList.main_page)
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(UrlsList.main_page))
    driver.find_element(By.XPATH, TestLocators.FILLINGS_TEXT).click()
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(UrlsList.main_page))
    assert driver.find_element(By.XPATH, TestLocators.FILLINGS_TEXT).text == 'Начинки'




