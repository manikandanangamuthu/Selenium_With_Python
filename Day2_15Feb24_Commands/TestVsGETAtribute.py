from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

r_options = Options()
r_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=r_options)

driver.get("https://demo.nopcommerce.com")

driver.maximize_window()

#search=driver.find_element(By.XPATH,"//input[@type='text']")

#search.clear()
#search.send_keys("Apple")

#print("Results of Text:", search.text)
#print("Results of get_Attribute:", search.get_attribute('id'))

#=====================================================================

search=driver.find_element(By.LINK_TEXT,"Search")

print("Results of Text:",search.text)
print("Result of get_Attribute:",search.get_attribute('type'))
