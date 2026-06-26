import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select  
from Utilities.CustomLogger import LogGen

class ProductPage:
    logger = LogGen.loggen()
    filters_xpath = "//select[@class='product_sort_container']"
    allproducts_names_xpath = "//div[contains(@class, 'inventory_item_name')]"
    allproducts_prices_xpath = "//div[contains(@class, 'inventory_item_price')]"
    add_to_cart_xapth = "//button[@id='add-to-cart-sauce-labs-backpack']"
    remove_btn_path ="//button[@id='remove-sauce-labs-backpack']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def filters_by_value(self, choice):
        self.logger.info(f"*********** Selecting Filter Value: '{choice}' *****************")
        # Step 1: Dropdown element ke clickable hone ka wait karo
        dropdown_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.filters_xpath)))
        
        # Step 2: Element to  ui when we see 
        select = Select(dropdown_element)
        choice = choice.lower().strip()
        
        if choice == "ztoa":
            select.select_by_value("za")     
        elif choice == "low_to_high":
            select.select_by_value("lohi")  
        elif choice == "high_to_low":
            select.select_by_value("hilo")  
        else:
            raise ValueError(f"Invalid Sorting Choice Passed: {choice}")
            
        time.sleep(3)
        self.logger.info(f"Successfully selected filter: {choice}")

    def get_product_names(self):
        self.logger.info("********* Fetching Product Names from UI *********************")
        try:
            elements = self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, self.allproducts_names_xpath)))
            return [element.text for element in elements]
        
        except Exception as e:
            self.logger.info(f"Error fetching product names: {e}")
            return []

    def get_product_prices(self):
        self.logger.info("********* Fetching Product Prices from UI *********************")
        try:
            elements = self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, self.allproducts_prices_xpath)))
            # '$29.99' ko clean karke float decimal (29.99) mein convert kar rahe hain taaki math check ho sake
            return [float(element.text.replace('$', '').strip()) for element in elements]
        except Exception as e:
            self.logger.info(f"Error fetching product prices: {e}")
            return []
    
    def click_add_to_cart_first_item(self):
        self.logger.info("**************Clicking Add to Cart using JavaScript**************")
        try:
            add_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_xapth)))
            add_btn.click()
            self.logger.info("Clicked seccesssfully using Native selenium Click")

        except Exception as e:
            self.logger.info(f"Native clicked Faield due to exexption Switching to click javascript {e}")
            add_btn_visible = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.add_to_cart_xapth)))
            self.driver.execute_script("arguments[0].click();", add_btn_visible)
            self.logger.info("Clickeed suceesfully using JavaScript Exexutor Fallback")
        time.sleep(3)
    

    def remove_btn_visible(self):
        self.logger.info("********Remove btn Visible Checking ****************")
        try:
             remove_btn = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.remove_btn_path)))
             return remove_btn.is_displayed()
        except Exception as e:
            self.logger.info(f"Remove btn not visible:{e}")
            return False

    

        
