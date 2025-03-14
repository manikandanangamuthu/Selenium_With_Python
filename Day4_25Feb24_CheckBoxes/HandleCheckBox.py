import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

r_options = Options()
r_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=r_options)
#=========================================================================================
driver.get("https://total-qa.com/checkbox-example/")

driver.maximize_window()
checkboxes=driver.find_elements(By.XPATH,"//input[@name='chk']")

print(len(checkboxes)) # length of the checkboxes are total 7

 #Check all checkboxes using approach 1 & 2

# Approach 1

#for i in range (len(checkboxes)):
#    checkboxes[i].click()

# Approach 2
for checkbox in checkboxes:
   checkbox.click()
