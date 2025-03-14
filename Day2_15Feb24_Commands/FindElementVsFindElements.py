from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

r_options = Options()
r_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=r_options)

driver.get("https://demo.nopcommerce.com")

driver.maximize_window()

#============================================================
#1. Locator matching with single webelement
# find_element  - Return single webelement

#element=driver.find_element(By.XPATH, "//input[@type='text']")
#element.send_keys("Shoes")
#============================================================


#============================================================
#2. Locator matching with multiple webelements
#find_lements - Return multiple webelements

#element=driver.find_element((By.XPATH,"//div[@class='footer']//a"))

#print(element.text)

#======================================================================
#3. Element not available then throw NoSuchElementException

#login_element=driver.find_element(By.LINK_TEXT,"Log ")
#login_element.click()

#=========================================================================


# Findelements - Return multiple webElements

# 1) Locator matching with single webElement

#element=driver.find_elements(By.XPATH, "//input[@type='text']")

#print(len(element)) #1
#element[0].send_keys("Apple")

#===================================================================

# 1) Locator matching with Multiple webElement
#element=driver.find_elements(By.XPATH, "//div[@class='footer']//a")

#print(len(element)) #23
#print(element[0].text) # Sitemap

#for ele in element:
 #   print(ele.text)

#==================================================================

#3) Element Not Available
element=driver.find_elements(By.LINK_TEXT,"Log")

print("element return value",len(element))