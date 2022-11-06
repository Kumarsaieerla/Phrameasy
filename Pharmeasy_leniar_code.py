from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
path = R"C:\Users\Sai kumar\PycharmProjects\pythonProject2\pythonProject\pythonProject\pythonProject\htmldup\htmldup1\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.maximize_window()
driver.implicitly_wait(20)
file_path = R"https://pharmeasy.in/"
driver.get(file_path)

driver.find_element("xpath", '(//a[@class="c-iWbDBM c-iWbDBM-ifUuzgR-css"])[3]').click()

driver.find_element("xpath", '//h2[text()="Covid Essentials"]').click()

driver.find_element("xpath", '//div[text()="Covid Test Kits"]').click()


driver.find_element("xpath", '//div[text()="Popularity"]').click()

driver.find_element("xpath", '//li[@data-value="price:0"]').click()

driver.find_element("xpath", '//input[@class="Input_input__3uBA4 FilterSection_filterInput__34-62"]').click()

driver.find_element("xpath", '//div[text()="200 - 299"]').click()

driver.find_element("xpath", '//div[text()="Coviself Covid Self Test Kit"]').click()

driver.find_element("xpath", '//button[text()="Add To Cart"]').click()

driver.find_element("xpath", '//li[@data-value="9"]').click()


driver.find_element("xpath", '//span[text()="View Cart"]').click()


driver.find_element("xpath", "//span[text()='Add Delivery Address']").click()

driver.find_element('id', 'mobileNoInput').send_keys("8639461234")


driver.find_element('id', "mobileNoSubmitBtn").click()
time.sleep(30)
handles = driver.window_handles
print(handles)

driver.find_element("name",'name').send_keys("E.Saikuamar")

driver.find_element("xpath", '//input[@name="ship-zip"]').send_keys("507166")

driver.find_element("xpath", '//input[@name="flat"]').send_keys("Khammam 1-92")

driver.find_element("xpath", '//input[@name="ship-address"]').send_keys("gandhinagar-khammam")

driver.find_element("xpath", '(//label[@class="ErAsG"])[1]').click()

driver.execute_script("arguments[0].click()", driver.find_element("xpath",'//button[text()="Save & Continue"]')).click()

driver.find_element("xpath",'//span[text()="Proceed To Buy"]').click()

driver.find_element("xpath",'//div[text()="Cash on Delivery"]').click()

#driver.execute_script("arguments[0].click()", driver.find_element("xpath",'//span[text()="Place Order"]')).click()


driver.close()









