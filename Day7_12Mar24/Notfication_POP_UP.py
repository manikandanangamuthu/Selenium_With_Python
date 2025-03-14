from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
ops=webdriver.ChromeOptions()

ops.add_argument("--disable-notifications")
r_options = Options()
r_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=r_options,)
driver=webdriver.Chrome(options=ops)
#========================================================================================
driver.get("https://whatmylocation.com")

driver.maximize_window()