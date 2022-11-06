from behave import *
from selenium import webdriver
import time


@given(u'User is able to launch browsers')
def launch_browser(context):
    context.driver = webdriver.Chrome(R"C:\Users\Sai kumar\PycharmProjects\pythonProject2\pythonProject\pythonProject\pythonProject\pythonProject\Pharmeasy\drivers\chromedriver.exe")
    context.driver.get(R"https://pharmeasy.in/")
    context.driver.maximize_window()
    time.sleep(2)

@when(u'User is able to click on health_care module')
def click_on_healthcare(context):
    context.driver.find_element("xpath", '(//a[@class="c-iWbDBM c-iWbDBM-ifUuzgR-css"])[3]').click()
    time.sleep(2)

@then(u'User is  able to click on Covid essentials')
def click_on_covid_essential(context):
    context.driver.find_element("xpath", '//h2[text()="Covid Essentials"]').click()
    time.sleep(2)

@then(u'User is able to click on Covid Test Kits')
def click_on_covid_kits(context):
    context.driver.find_element("xpath", '//div[text()="Covid Test Kits"]').click()
    time.sleep(2)

@then(u'User is able to click on popularity')
def click_on_popularity(context):
    context.driver.find_element("xpath", '//div[text()="Popularity"]').click()
    time.sleep(2)

@then(u'User is able to select a product according its popularity')
def select_popularity(context):
    context.driver.find_element("xpath", '//li[@data-value="price:0"]').click()
    time.sleep(2)

@then(u'User is able to filter the product according to its brand')
def filter_brand(context):
    context.driver.find_element("xpath", '//input[@class="Input_input__3uBA4 FilterSection_filterInput__34-62"]').click()
    time.sleep(2)

@then(u'User should be able to select and choose price range')
def price_range(context):
    context.driver.find_element("xpath", '//div[text()="200 - 299"]').click()
    time.sleep(2)

@then(u'User should be able to select product')
def select_product(context):
    context.driver.find_element("xpath", '//div[text()="Coviself Covid Self Test Kit"]').click()
    time.sleep(2)

@then(u'User should be able add the product to cart')
def add_to_cart(context):
    context.driver.find_element("xpath", '//button[text()="Add To Cart"]').click()
    time.sleep(2)

@then(u'User should be able to select Qty of items to be added to cart')
def qty_of_items(context):
    context.driver.find_element("xpath", '//li[@data-value="9"]').click()
    time.sleep(2)

@then(u'User should be to click on view cart')
def view_cart(context):
    context.driver.find_element("xpath", '//span[text()="View Cart"]').click()
    time.sleep(2)

@then(u'User is able to add the delivery address')
def address(context):
    context.driver.find_element("xpath", "//span[text()='Add Delivery Address']").click()
    time.sleep(2)

@when(u'User enter valid phone "{number}" in phone number text field')
def enter_num(context,number):
    context.driver.find_element('id', 'mobileNoInput').send_keys(number)

    time.sleep(2)

@then(u'User should be able to click on send otp')
def enter_otp(context):
    context.driver.find_element('id', "mobileNoSubmitBtn").click()
    time.sleep(30)

@then(u'User should be able to click on submit otp')
def click_sub(context):
    context.driver.find_element('id', 'otpSubmitBtn').click()

@then(u'close browser')
def close_browser(context):
   context.driver.close()








