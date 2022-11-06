import datetime
import pytest
from Library.read_excel import ReadExcel
from POM.health_care import Helath_care
from Library.config import Config


class TestRegisterPage:
    read_xl = ReadExcel()
    data = read_xl.read_data(Config.SHEET_NAME_DATA_PATH)
    @pytest.mark.parametrize("number, fname, pcode, flat, address", data)
    def test_valid_credentil(self, number, fname, pcode, flat, address, init_driver):
        driver = init_driver

        try:
            obj = Helath_care(init_driver)
            obj.click_health_care()
            obj.click_on_covid_essential()
            obj.click_on_covid_testkits()
            obj.click_on_popularity()
            obj.select_popularity()
            obj.filter_product()
            obj.select_price_range()
            obj.click_on_product()
            obj.click_on_add_to_cart()
            obj.qty_of_items()
            obj.click_on_view_cart()
            obj.click_on_add_delivery_address()
            obj.mobile_number(number)
            obj.send_otp()
            obj.click_on_submit()
            obj.click_on_name(fname)
            obj.zipcode(pcode)
            obj.select_flat(flat)
            obj.select_ship_address(address)
            obj.select_type_of_address()
            obj.click_on_save()
            obj.click_on_proceed_to_buy()
            obj.click_payment_mode()


        except BaseException as error_msg:
            td = datetime.datetime.now()
            name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
            driver.save_screenshot(Config.SCREENSHOT_PATH + name)
            raise error_msg