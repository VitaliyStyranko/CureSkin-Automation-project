from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


@given('Open Collections page')
def open_page(context):
    context.app.collections_page.open_collections_page()


@when('Click on a {product_id} collection link')
def click_product_link(context, product_id):
    context.app.collections_page.click_product_clt_link()


@then('Verify the user is taken to the products page')
def user_taken_to_product_page(context):
    context.driver.wait.until(EC.url_contains("https://shop.cureskin.com/collections/body"))
    print('Current window:', context.driver.current_window_handle)