from unittest import expectedFailure

import pytest
from pyexpat.errors import messages
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Locators.BiilPayPageLocators import BillPayPageLocators
from Pages.LoginPage import LoginPage
from Pages.BillPayPage import BillPayPage

from Utils.FileHelper import read_csv

test_data = read_csv("Data/BillPayPageData.csv")

@pytest.mark.parametrize((
    "payee_name", "address", "city", "state", "zip_code", "phone",
    "account_number", "verify_account_number", "amount", "from_account", "expected"
), test_data)
def test_bill_pay(payee_name, address, city, state, zip_code, phone,
                  account_number, verify_account_number, amount, from_account, expected, driver):

    login_page = LoginPage(driver)
    login_page.login("shyam2", "shyam")

    bill_pay_page = BillPayPage(driver)
    bill_pay_page.load()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(BillPayPageLocators.bill_pay_menu)
    ).click()

    bill_pay_page.enter_payee_information(payee_name, address, city, state, zip_code, phone)
    bill_pay_page.enter_account_information(account_number, verify_account_number, amount, from_account)
    bill_pay_page.send_payment()

    if expected=="success":
        message=bill_pay_page.has_success_message()
        assert message== True ,f"This is the message shown {message}"
    elif expected=="account_mismatch_error":
        messages=bill_pay_page.has_verify_account_mismatch_error()
        assert messages== True ,f"This is the message shown {messages}"
    elif expected=="failure":
        message=bill_pay_page.has_amount_error()
        assert message== False ,f"This is the message shown {message}"
    elif expected=="negative_amount_error":
        message=bill_pay_page.has_negative_amount_error()
        assert message== True ,f"This is the message shown {message}"
    else:
        print("Other errors")
        assert False
    #
    #
    # # Enhanced logic to detect outcome:
    # if bill_pay_page.has_verify_account_mismatch_error():
    #     result = "failure"
    # elif bill_pay_page.has_negative_amount_error():
    #     result = "failure"
    # elif bill_pay_page.has_amount_error():
    #     result = "failure"
    # elif bill_pay_page.has_success_message():
    #     result = "success"
    # else:
    #     result = "failure"
    #
    # assert result == expected