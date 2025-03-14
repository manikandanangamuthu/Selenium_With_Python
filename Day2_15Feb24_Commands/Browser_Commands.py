import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

r_options = Options()
r_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=r_options)

driver.get("https://demo.nopcommerce.com")

driver.maximize_window()

#==============================================================

driver.find_element(By.LINK_TEXT,"nopCommerce").click()

time.sleep(60)

# driver.close()  # Close single browser window ( Where driver focused)

driver.quit()  # Close multiple browser windows(This will kill process)
