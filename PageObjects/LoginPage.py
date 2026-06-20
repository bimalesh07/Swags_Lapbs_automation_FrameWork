import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.CustomLogger import LogGen


class LoginPage:
    username_path = "//input[@id='user-name']"
    password_path = "//input[@id='password']"

    login_path = "//input[@id='login-button']"
    errro_message_path ="//h3[normalize-space()='Epic sadface: Username is required']"
    password_wrong_message_xpath = "//h3[contains(text(),'Epic sadface: Username and password do not match a')]"

    swap_logo_confrim = "//div[@class='app_logo']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = LogGen.loggen()
    
    def Login_direct(self, username, password):
        self.logger.info("************Login page Opening ***************")
        username_feild = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.username_path)))
        username_feild.clear()
        username_feild.send_keys(username)
        self.logger.info("*********Username are enter **************************")

        password_feild = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.password_path)))
        password_feild.clear()
        password_feild.send_keys(password)
        self.logger.info("*********Password are Entner succeesfully******************")


        btn_click = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.login_path)))
        self.driver.execute_script("arguments[0].click();", btn_click)
        self.logger.info("**********Login Button are Click are suceessfully ******************")



    def invlid_loin(self):
        self.logger.info("******Here we Start Check Invalid login process")
        
    
    def successfully_loin_message(self):
        self.logger.info("********After Login Sucessmessage are ")
        try:
            self.logger.info("Watiin for the sucessmesaage")
            logo_text = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.swap_logo_confrim)))
            if logo_text.is_displayed():
                self.logger.info("This is a now visible ")
                return True
            else:
                return False
        
        except Exception as e:
            self.logger.info("******Logo are not Visible**************")
            return False
    
        







