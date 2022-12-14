from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Open Product Details {product_id} page')
def open_page(context, product_id):
    context.driver.get(f'https://shop.cureskin.com/products/{product_id}/')


@when('Click to add product to cart')
def add_to_cart(context):
    context.app.product_page.click_add_to_cart()


@when('Verify added to your cart confirmation is shown')
def verify_conf(context):
    context.app.product_page.verify_confirmation()


@then('Open cart page')
def click_on_btn(context):
    context.app.product_page.click_view_btn()


@then('Verify {expected_result} is in the cart')
def verify_correct_item(context, expected_result):
    context.app.product_page.verify_item(expected_result)
