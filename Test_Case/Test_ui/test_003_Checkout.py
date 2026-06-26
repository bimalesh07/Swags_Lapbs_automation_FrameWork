import time
import pytest
from PageObjects.CheckOut import CheckOutPage
from PageObjects.LoginPage import LoginPage
from PageObjects.ProductPage import ProductPage
from .basetest import BaseTest
from Utilities.CustomLogger import LogGen
from Utilities.ReadEnv import ReadEnvvalue

@pytest.mark.usefixtures("user_auth")
class Test_CheckCart(BaseTest):
    logger = LogGen.loggen()
    username = ReadEnvvalue.get_username()
    password = ReadEnvvalue.get_password()

    def test_checkout(self):
        self.logger.info("********* Start Checkout Test ************")

        #step 1: Login Flow
        lp = LoginPage(self.driver)
        self.logger.info("******** Login Process Started ***********")
        lp.Login_direct(self.username, self.password)
        is_login = lp.successfully_loin_message()
        assert is_login ==True, "Failed: Login failed, Dashboard not displayed"
        self.logger.info("******* Login Successfully Done *********")

        # Add Product to Cart
        self.logger.info("******** Adding Pehla Product to Cart ********")
        pp = ProductPage(self.driver)
        pp.click_add_to_cart_first_item()
        
        time.sleep(3)
        
        # Verify Product is Added
        is_visible_remove = pp.remove_btn_visible()
        assert is_visible_remove is True, "Failed: Remove button is not visible after click"
        self.logger.info("*** PRODUCT ADDED TO CART SUCCESSFULLY ****")

        # Checkout Page Flow
        self.logger.info("****** Starting Checkout Functionality *******")
        Cp = CheckOutPage(self.driver)
        Cp.Checkout_funcality()
        
        #confrim chekout
        is_visible = Cp.Visibilty_of_Checkout()
        assert is_visible is True, "Failed: Checkout Your Information Page is not visible"
        self.logger.info("******* Checkout Navigation Successfully Verified! **********")

        self.logger.info("********Addign adress and confrim Orders *********")
        Cp.address_value("Rahul", "sharma", "11092")
        Cp.click_finsih_orders()

        self.logger.info("********Finsih orders  button ***********")

        is_ordered_placed_confrim = Cp.order_completed_confirm()
        expected_message = "Thank you for your order!"
        assert is_ordered_placed_confrim == expected_message , "Faield: Not showing Than you your Orers"

        self.logger.info("Completed this all project")
