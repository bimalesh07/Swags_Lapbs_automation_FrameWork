import pytest
from selenium import webdriver
from Utilities.ReadEnv import ReadEnvvalue
import os

@pytest.fixture(scope="class", autouse=True) 
def setup_browser(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-features=PasswordLeakDetection")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    
    prefs = {
        "profile.password_manager_leak_detection": False,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    url = ReadEnvvalue.get_base_url()
    driver.get(url)

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    print("\n[BROWSER CLOSE] Destroying Driver Context ---")
    driver.quit()


@pytest.fixture(scope="function") 
def user_auth(request):
    if hasattr(request.cls, 'driver'):
        url = ReadEnvvalue.get_base_url()
        
        print("\n[RESET] Deleting cookies and opening fresh URL...")
        request.cls.driver.delete_all_cookies() 
        request.cls.driver.get(url)             
        
    yield 


#in html report we remove some extra details 
def pytest_configure(config):
    if hasattr(config, '_metadata'):
        if 'JAVA_HOME' in config._metadata:
            del config._metadata['JAVA_HOME']
        if 'Packages' in config._metadata:
            del config._metadata['Packages']
        if 'Platform' in config._metadata:
            del config._metadata['Platform']
        if 'Plugins' in config._metadata:
            del config._metadata['Plugins']


# #Screenshot setup 
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
    
#     #if test fail
#     if rep.when == "call" and rep.failed:
#         driver = getattr(item.obj, "self", None)
#         if driver and hasattr(driver, "driver"):
#             web_driver = driver.driver
            
#             #folders exsits then 
#             if not os.path.exists("ScreenShots"):
#                 os.makedirs("ScreenShots")
            
#             #save in file
#             file_path = f"ScreenShots/{item.name}.png"
            
#             # Screenshot save command
#             web_driver.save_screenshot(file_path)
            
#             # attach in html repost
#             if not hasattr(rep, "extra"):
#                 rep.extra = []
#             pytest_html = item.config.pluginmanager.getplugin("html")
#             if pytest_html:
#                 rep.extra.append(pytest_html.extras.image(file_path))