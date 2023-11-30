import re
from Library.read_excel import ReadExcel
from Library.config import Config
import time


class Helath_care:

    read_xl = ReadExcel()
    reg_locators = read_xl.read_locaters(Config.SHEET_NAME_LOCATER_PATH)

    def __init__(self, driver):
        self.driver = driver

    def click_health_care(self):
        locator = self.reg_locators["click_health_care"]
        self.driver.find_element(*locator).click()
        time.sleep(2)


    def click_on_covid_essential(self):
        locator = self.reg_locators["click_on_covid_essential"]
        self.driver.find_element(*locator).click()
        time.sleep(2)


    def click_on_covid_testkits(self):
        locator = self.reg_locators["click_on_covid_testkits"]
        self.driver.find_element(*locator).click()
        time.sleep(2)



    def click_on_popularity(self):
        locator = self.reg_locators["click_on_popularity"]
        self.driver.find_element(*locator).click()
        time.sleep(2)


    def select_popularity(self):
        locator = self.reg_locators["select_popularity"]
        self.driver.find_element(*locator).click()
        time.sleep(2)


    def filter_product(self):
        locator = self.reg_locators["filter_product"]
        self.driver.find_element(*locator).click()
        time.sleep(2)


    def select_price_range(self):
        locator = self.reg_locators["select_price_range"]
        self.driver.find_element(*locator).click()
        time.sleep(2)


    def click_on_product(self):
        locator = self.reg_locators["click_on_product"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def click_on_add_to_cart(self):
        locator = self.reg_locators["click_on_add_to_cart"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def qty_of_items(self):
        locator = self.reg_locators["qty_of_items"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def click_on_view_cart(self):
        locator = self.reg_locators["click_on_view_cart"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def click_on_add_delivery_address(self):
        locator = self.reg_locators["click_on_add_delivery_address"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def mobile_number(self,number):
        if isinstance(number,float):
            number = str(int(number))
        assert len(number) == 10
        locator = self.reg_locators["mobile_number"]
        self.driver.find_element(*locator).send_keys(number)
        time.sleep(2)


    def send_otp(self):
        locator = self.reg_locators["send_otp"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def click_on_submit(self):
        locator = self.reg_locators["click_on_submit"]
        self.driver.find_element(*locator).click()
        time.sleep(30)
        handles = self.driver.window_handles
        print(handles)

    def click_on_name(self,fname):
        locator = self.reg_locators["click_on_name"]
        self.driver.find_element(*locator).send_keys(fname)
        time.sleep(2)

    def zipcode(self, pcode):
        locator = self.reg_locators["zipcode"]
        self.driver.find_element(*locator).send_keys(pcode)


    def select_flat(self,flat):
        locator = self.reg_locators["select_flat"]
        self.driver.find_element(*locator).send_keys(flat)

    def select_ship_address(self,address):
        locator = self.reg_locators["click_on_ship_address"]
        self.driver.find_element(*locator).send_keys(address)

    def select_type_of_address(self):
        locator = self.reg_locators["select_type_of_address"]
        self.driver.find_element(*locator).click()

    def click_on_save(self):
        locator = self.reg_locators["click_on_save"]
        self.driver.exicute_script("arguments[0].click"),self.driver.find_element(*locator).click()
        self.driver.close()

    #
    # def click_on_proceed_to_buy(self):
    #     locator = self.reg_locators["click_on_proceed_to_buy"]
    #     self.driver.exicute_script("arguments[0].click"),self.driver.find_element(*locator).click()
    #
    # def click_payment_mode(self):
    #     locator = self.reg_locators["select_payment_mode"]
    #     self.driver.exicute_script("arguments[0].click"),self.driver.find_element(*locator).click()
    #     self.driver.close()



#123757684
