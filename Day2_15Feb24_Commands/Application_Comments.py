from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

r_options = Options()
r_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=r_options)

driver.get("https://letcode.in/signup")

driver.maximize_window()    #window maximize

print(driver.title)

print(driver.current_url)

Actual_title="LetCode with Koushik"

expected_title=driver.title

print(expected_title)

if Actual_title==expected_title:
    print("Pass!")
else:
    print("Fail")

print(driver.page_source)
