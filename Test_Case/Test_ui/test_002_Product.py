import time
import pytest
from PageObjects.ProductPage import ProductPage
from Utilities.CustomLogger import LogGen
from Utilities.ReadEnv import ReadEnvvalue
from .basetest import BaseTest
from PageObjects.LoginPage import LoginPage

@pytest.mark.usefixtures("user_auth")
class Test_ProductList(BaseTest):
    username = ReadEnvvalue.get_username()
    password = ReadEnvvalue.get_password()
    logger = LogGen.loggen()

    def test_product_filters(self):
        lp = LoginPage(self.driver)
        lp.Login_direct(self.username, self.password)
        self.logger.info("************** Test Login successful ********* ")
        loginvisible = lp.successfully_loin_message()
        time.sleep(2)
        assert loginvisible == True, "Failed: Dashboard page not displayed after login"

        pp = ProductPage(self.driver)
        
        # self.logger.info("********** Starting validation for Z to A ***************")
        # pp.filters_by_value("ztoa")
        
        # actual_names = pp.get_product_names()
        # assert len(actual_names) > 0, "Failed: No product names found on UI (List is empty)"
        
        # expected_names = sorted(actual_names, reverse=True)
        # assert actual_names == expected_names, "Failed: ZtoA sorting logic failed on UI!"
        # self.logger.info("ZtoA Filter validated successfully!")

        # self.logger.info("************* Starting validation for High to Low *********")
        # pp.filters_by_value("high_to_low")
        
        # actual_prices = pp.get_product_prices()
        # assert len(actual_prices) > 0, "Failed: No product prices found on UI (List is empty)"
        
        # expected_prices = sorted(actual_prices, reverse=True)
        # assert actual_prices == expected_prices, "Failed: High to Low price sorting failed on UI!"
        # self.logger.info("✅ High to Low Filter validated successfully!")
        
        self.logger.info("*********ADD TO CART PRODUCT FROM HERE ************")
        pp.click_add_to_cart_first_item()

        is_removevisible = pp.remove_btn_visible()
        self.logger.info("********Remove Button are visible check start *********")
        assert is_removevisible == True, "Faield: Remove Button Are Not Visible"
        self.logger.info("*********Add to cart sucessfully done ********")




    