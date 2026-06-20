import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Utilities.CustomLogger import LogGen
from selenium.webdriver.support.ui import WebDriverWait

class ProductPage:
    logger = LogGen.loggen()
    filters_xpath = "//select[@class='product_sort_container']"
    ztoa ="//select[@class='product_sort_container']/option[@value='za']"
    low_to_high = "//select[@class='product_sort_container']/option[@value='lohi']"
    hight_to_low = "//select[@class='product_sort_container']/option[@value='hilo']"

    allprodcuts = "//div[@class='inventory_item_name']"


    def __init__(self, driver):
        self.driver = driver
        self.wait =  WebDriverWait(driver, 10)
        self.logger = LogGen.loggen()
    

    def filters_by_value(self, choice):
        self.logger.info("***********Navigate The Fillters bnt *****************")
        navigate_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.filters_xpath)))
        self.driver.execute_script("arguments[0].click();", navigate_btn)
        time.sleep(2)
        self.logger.info("*****************Succuessfully Click Fillters Btn*********")
        time.sleep(2)
        self.logger.info("********* Enters Fillters value start from here ***********")
    
        if choice == "ztoa":
           fillters_btn = self.ztoa

        elif choice == "low low high":
            fillters_btn = self.low_to_high

        elif choice == "high_to_low":
            fillters_btn = self.hight_to_low
        
        else :
            raise ValueError (f"Invalid Sorting Stiring Choice, {choice}")
        
        fillters_btn_search = self.wait.until(EC.element_to_be_clickable((By.XPATH, fillters_btn)))
        self.driver.execute_script("arguments[0].click();", fillters_btn_search)
        self.logger.info(f"Fillters are update to seraching sorting by update by value, {choice}")



    def ValidatedFilters(self):
        self.logger.info("*********Chekcing The Fillters Of Work or not *********************")
        try:
            products_list = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.allprodcuts)))
            return [product.text for product in products_list]
        
        except Exception as e:
            self.logger.info(f"******Products are not Visible in this page ,{e}")
            return []




        

        