import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.CustomLogger import LogGen


class CheckOutPage:
    cart_btn_xapth = "//a[@id='shoping_cart_link']"
    Checkout_xpath = "//button[@id='Checkout']"
    logger = LogGen.loggen()


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    
    def Checkout_funcality(self):
        self.logger.info("*************Checking ChekCartButootn Working Or not ********")
        try:
         checkout_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.cart_btn_xapth)))
         checkout_btn.click()

        except Exception as e:
           self.logger.error(f"Try cart is not workign so we now clicking the with js clicked")
           checkout_btn = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.cart_btn_xapth)))
           self.driver.executes_script(['arguments[0].click();', checkout_btn])
        self.logger.info("Add to Cart Button are successfully Done")
        time.sleep(2)
    

    def Visibilty_of_Checkout(self):
       self.logger.info("*********Checking The CheckOut are Visible or not ")
       try:
            is_visible_checkout = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.Checkout_xpath)))
            is_visible_checkout.is_displayed()
            return True
       
       except Exception as e:
          self.logger.info(f"**********Checkout are not visible***********:{e}")
          return False
    
       
          
    
       
           
        