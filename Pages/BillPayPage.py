from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from Locators.BiilPayPageLocators import BillPayPageLocators


class BillPayPage:
    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(BillPayPageLocators.url)

    def fill_input(self, locator, value):
        try:
            field = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            )
            field.clear()
            field.send_keys(value)
        except TimeoutException:
            print(f"[Input Error] Cannot interact with: {locator}")

    def enter_payee_information(self, name, address, city, state, zip_code, phone):
        self.fill_input(BillPayPageLocators.payee_name_input, name)
        self.fill_input(BillPayPageLocators.payee_address_input, address)
        self.fill_input(BillPayPageLocators.payee_city_input, city)
        self.fill_input(BillPayPageLocators.payee_state_input, state)
        self.fill_input(BillPayPageLocators.payee_zip_code_input, zip_code)
        self.fill_input(BillPayPageLocators.payee_phone_input, phone)

    def enter_account_information(self, acc_no, verify_acc, amount, from_acc):
        self.fill_input(BillPayPageLocators.account_number_input, acc_no)
        self.fill_input(BillPayPageLocators.verify_account_number_input, verify_acc)
        self.fill_input(BillPayPageLocators.amount_input, amount)
        try:
            from_acc_field = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(BillPayPageLocators.from_account_input)
            )
            from_acc_field.send_keys(from_acc)
        except TimeoutException:
            print("[From Account Error] Cannot select from account.")

    def send_payment(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(BillPayPageLocators.send_payment_button)
            ).click()
        except TimeoutException:
            print("[Send Payment Error] Button not found or clickable.")

    def has_success_message(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(BillPayPageLocators.success_message)
            )
            return True
        except TimeoutException:
            return False

    def has_verify_account_mismatch_error(self):
        try:
            element = self.driver.find_element(By.ID, "validationModel-verifyAccount-mismatch")
            return element.is_displayed()
        except Exception:
            return False
    def has_amount_error(self):
        try:
            element = self.driver.find_element(By.ID, "verify_amount_error")
            return element.is_displayed()
        except Exception:
            return False


    def has_negative_amount_error(self):
        try:
            element = self.driver.find_element(By.ID, "validationModel-amount-negative")
            return element.is_displayed()
        except Exception:
            return False


