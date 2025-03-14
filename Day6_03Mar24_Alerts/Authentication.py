import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

r_options = Options()
r_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=r_options)

# driver.get("https://the-internet.herokuapp.com/basic_auth") # normal url passing

driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth") # username:password passed through url

# Syntax    http://username:password@test.com

driver.maximize_window()

