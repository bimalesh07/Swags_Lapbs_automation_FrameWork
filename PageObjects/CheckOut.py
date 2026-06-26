import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.CustomLogger import LogGen

class CheckOutPage:
    cart_btn_xpath = "//a[@class='shopping_cart_link']"
    checkout_btn_xpath = "//button[@id='checkout']"
    first_name ="//input[@id='first-name']"
    last_name ="//input[@id='last-name']"
    zip_code = "//input[@id='postal-code']"
    continue_btn_xpath = "//input[@id='continue']"
    finish_btn_xpath = "//button[@id='finish']"
    visible_thanyou_xapth = "//h2[normalize-space()='Thank you for your order!']"

    logger = LogGen.loggen()

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def Checkout_funcality(self):
        self.logger.info("************* Navigating to Cart Page *********")
        
        try:
            cart_icon = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.cart_btn_xpath)))
            cart_icon.click()
            self.logger.info("Cart Icon clicked via Native UI")
        except Exception:
            self.logger.error(" Native cart click failed, using corrected JS Click")
            cart_icon_visible = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.cart_btn_xpath)))
          
            self.driver.execute_script("arguments[0].click();", cart_icon_visible)
        
        time.sleep(2) 
    
        self.logger.info("************* Clicking Checkout Button ************")
        try:
            checkout_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.checkout_btn_xpath)))
            checkout_btn.click()
            self.logger.info("Checkout Button clicked via Native UI")
        except Exception:
            checkout_btn_visible = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.checkout_btn_xpath)))
            self.driver.execute_script("arguments[0].click();", checkout_btn_visible)
            
        time.sleep(2)
    
    def address_value(self, first_names, last_names, zip_codes):
        self.logger.info("******Entering Informations ****************")
        fname = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.first_name)))
        fname.clear()
        fname.send_keys(first_names)
        self.logger.info("Firstname is added sucessfully")

        lname = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.last_name)))
        lname.clear()
        lname.send_keys(last_names)
        self.logger.info("Lastname is sucessfully added")

        zcode = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.zip_code)))
        zcode.clear()
        zcode.send_keys(zip_codes)
        self.logger.info("Zipcode sucssfully added")

        self.logger.info("**********COMPLAETED ADRESS SUCEESSFULLY **********")
        time.sleep(3)

        try:
            contune_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.continue_btn_xpath)))
            contune_btn.click()
            self.logger.info("Continue button clicked successfully via Native Selenium Click")
        except Exception as e:
            self.logger.warning(f"Native click failed due to: {e}. Switching to JavaScript click fallback.")
            contune_btn_js = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.continue_btn_xpath)))
            self.driver.execute_script("arguments[0].click();", contune_btn_js)
            self.logger.info("✅ Continue button clicked successfully via JavaScript Executor")
    

    def click_finsih_orders(self):
        self.logger.info("*************Clicking Finsih button to Completed orders *********")
        try:
            completed_btn = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.finish_btn_xpath)))
            completed_btn.click()
            self.logger.info("Order Finshed via naive ui click")
        
        except Exception as e:
            self.logger.info(f"Native finish Failed, switching to js click")
            finish_btn_js = self.wait.until(EC.visibility_of_element_located((By.XPATH, finish_btn_js)))
            self.driver.execute_script("arguments[0].click();", finish_btn_js)
        
        time.sleep(2)
    
        

    def Visibilty_of_Checkout(self):
        self.logger.info("********* Checking if Checkout Info Page is Displayed *********")
        try:
            is_visible_checkout = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='first-name']")))
            return is_visible_checkout.is_displayed()
        except Exception as e:
            self.logger.info(f"********** Checkout page not visible ***********:{e}")
            return False
    
    def order_completed_confirm(self):
        self.logger.info("********* Fetching Final Success Message Text *********")
        try:
            success_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.visible_thanyou_xapth)))
        
            actual_text = success_element.text.strip()
            self.logger.info(f"UI Text Found: '{actual_text}'")
            
            return actual_text
            
        except Exception as e:
            self.logger.error(f"Success message element not found: {e}")
            return ""