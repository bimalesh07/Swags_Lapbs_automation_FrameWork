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
        self.logger.info("**************Test Login are successfully ********* ")
        loginvisible = lp.successfully_loin_message()
        time.sleep(2)
        assert loginvisible==True, "Faield: not show the after Login Page"

        pp = ProductPage(self.driver)
        pp.filters_by_value("ztoa")
        time.sleep(2)

        actual_product = pp.ValidatedFilters()
        self.logger.info("************Product get Successfully **************")

        expected_product = sorted(actual_product, reverse=True)
        self.logger.info("************products sorted sucessfully*******")

        assert actual_product == expected_product , "Faield: Not the get write product"
        self.logger.info("********Filltera are sucessfully Done ************")
        




        





