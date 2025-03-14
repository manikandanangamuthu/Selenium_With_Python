from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

r_options = Options()
r_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=r_options)

driver.get("https://demo.nopcommerce.com")

driver.maximize_window()  #window maximize
#===================================================================================
# is_displayed  is_enabled

searchBox=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")

print("Display Status:", searchBox.is_displayed())
print("Display Status:", searchBox.is_enabled())

#===========================================================================================

# is_selected   Before selecting redio button

rd_pollOptions=driver.find_element(By.XPATH,"//input[@id='pollanswers-1']")

print("Display Status:",rd_pollOptions.is_selected())

driver.find_element(By.XPATH,"//input[@id='pollanswers-1']").click()

print("Display Status:",rd_pollOptions.is_selected())

