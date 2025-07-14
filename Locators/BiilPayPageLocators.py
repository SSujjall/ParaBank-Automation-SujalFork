from selenium.webdriver.common.by import By

class BillPayPageLocators:
    url = "https://parabank.parasoft.com/parabank/billpay.htm"

    bill_pay_menu = (By.LINK_TEXT, 'Bill Pay')

    # Payee Information
    payee_name_input = (By.NAME, 'payee.name')
    payee_address_input = (By.NAME, 'payee.address.street')
    payee_city_input = (By.NAME, 'payee.address.city')
    payee_state_input = (By.NAME, 'payee.address.state')
    payee_zip_code_input = (By.NAME, 'payee.address.zipCode')
    payee_phone_input = (By.NAME, 'payee.phoneNumber')

    # Account Information
    account_number_input = (By.NAME, 'payee.accountNumber')
    verify_account_number_input = (By.NAME, 'verifyAccount')
    amount_input = (By.NAME, 'amount')
    from_account_input = (By.NAME, 'fromAccountId')

    # Buttons
    send_payment_button = (By.XPATH, "//input[@value='Send Payment']")

    # Success Message
    success_message = (By.CLASS_NAME, 'title')

    # Validation messages for "Verify Account #"
    verify_account_empty_error = (By.ID, 'validationModel-verifyAccount-empty')
    verify_account_invalid_error = (By.ID, 'validationModel-verifyAccount-invalid')
    verify_account_mismatch_error = (By.CLASS_NAME, 'error')
    verify_amount_error = (By.ID,'validationModel-amount-invalid')
