import pytest
from selenium import webdriver
from Utilities.ReadEnv import ReadEnvvalue

#SETUP BROWSER: Browser open
@pytest.fixture(scope="class", autouse=True) # Class level scope aur automatic execution
def setup_browser(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-features=PasswordLeakDetection")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    #Password leak credeantails
    prefs = {
        "profile.password_manager_leak_detection": False,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    #Browser khulte hi automatic direct .env se URL nikal kar khol dega
    url = ReadEnvvalue.get_base_url()
    driver.get(url)

    # Driver ko test class ke sath attach karna taaki self.driver kaam kare
    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    print("\n[BROWSER CLOSE] Destroying Driver Context ---")
    driver.quit()


#USER AUTH (FRESH URL): Yeh tumhaara safai-karamchari fixture hai
@pytest.fixture(scope="function") # autouse NAHI hai, manually mark karenge jahan zaroorat hogi
def user_auth(request):
    if hasattr(request.cls, 'driver'):
        url = ReadEnvvalue.get_base_url()
        request.cls.driver.delete_all_cookies() 
        request.cls.driver.get(url)               