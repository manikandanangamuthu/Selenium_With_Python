import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

r_options = Options()
r_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=r_options)

driver.get("https://demo.nopcommerce.com")

driver.maximize_window()

time.sleep(5)  # Python Command for wait and load # 5 Means seconds

driver.find_element(By.LINK_TEXT,"nopCommerce").click()