from behave import given, when, then
from selenium.webdriver.common.by import By


SUBSCRIBE_TO_EMAIL = (By.XPATH, "//div[@class='footer-block__newsletter']//h2[@class='footer-block__heading']")
CONTACT_INFO = (By.XPATH, "//div[@class='footer-block grid__item']//h2[@class='footer-block__heading']")

@given('Open main page')
def open_page(context):
    context.app.main_page.open_main()


@then('Verify Subscribe to email visible in the footer')
def verify_Subscribe_to_email(context):
    actual_text = context.driver.find_element(*SUBSCRIBE_TO_EMAIL).text
    expected_text = "Subscribe to email"
    assert expected_text == actual_text, \
        f'Expected: {expected_text}, but got: {actual_text}'


@then('Verify Contact Info is visible in the footer')
def verify_contact_info(context):
    actual_text = context.driver.find_element(*CONTACT_INFO).text
    expected_text = "Contact Info"
    assert expected_text == actual_text, \
        f'Expected: {expected_text}, but got: {actual_text}'
