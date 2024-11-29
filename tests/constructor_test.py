from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from urls import UrlsList
from locators import TestLocators

class TestConstructorPage:

    def test_constructor_buns(self, driver):
        driver.get(UrlsList.main_page)
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(UrlsList.main_page))
        driver.find_element(By.XPATH, TestLocators.SAUCES_TEXT_BUTTON).click()
        driver.find_element(By.XPATH, TestLocators.BUNS_TEXT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(UrlsList.main_page))
        assert driver.find_element(By.XPATH, TestLocators.BUNS_TEXT_SELECT).text == 'Булки'

    def test_constructor_sauces(self, driver):
        driver.get(UrlsList.main_page)
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(UrlsList.main_page))
        driver.find_element(By.XPATH, TestLocators.SAUCES_TEXT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(UrlsList.main_page))
        assert driver.find_element(By.XPATH, TestLocators.SAUCES_TEXT_SELECT).text == 'Соусы'

    def test_constructor_fillings(self, driver):
        driver.get(UrlsList.main_page)
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(UrlsList.main_page))
        driver.find_element(By.XPATH, TestLocators.FILLINGS_TEXT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(UrlsList.main_page))
        assert driver.find_element(By.XPATH, TestLocators.FILLINGS_TEXT_SELECT).text == 'Начинки'
