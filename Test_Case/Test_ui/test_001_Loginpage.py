import time
from .basetest import BaseTest
from PageObjects.LoginPage import LoginPage
from Utilities.CustomLogger import LogGen
from Utilities.ReadEnv import ReadEnvvalue
import pytest

@pytest.mark.usefixtures("user_auth")
class Test_login(BaseTest):
    username = ReadEnvvalue.get_username()
    password = ReadEnvvalue.get_password()
    logger = LogGen.loggen()

    def test_login(self):
        self.logger.info("************User Loin are Sucessfully ***********")
        lp = LoginPage(self.driver)
        lp.Login_direct(self.username, self.password)
        
        self.logger.info("******After Login sucessfully message ****")
        logo_visible = lp.successfully_loin_message()
        time.sleep(2)
        assert logo_visible == True , "Faield: Some Things Error not visible "
    





    



