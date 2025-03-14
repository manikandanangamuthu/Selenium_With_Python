import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

r_options = Options()
r_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=r_options)

driver.get("https://www.worldometers.info/geography/flags-of-the-world/")

driver.maximize_window()

# Scroll down by pixel

#driver.execute_script("window.scrollBy(0,3000)","")
#value=driver.execute_script("return window.pageYOffset;")
#print ("Number of pixel moved:", value)

# Scroll down the page till element visible

flag=driver.find_element(By.XPATH,"//img[@src='/img/flags/small/tn_vm-flag.gif']")

#driver.execute_script("arguments[0].scrollIntoView();",flag)
#value=driver.execute_script("return window.pageYOffset;")
#print ("Number of pixel moved:", value)

# Scroll down page till end of the page

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)") # moving till end of the page
value=driver.execute_script("return window.pageYOffset;")
print ("Number of pixel moved:", value)

time.sleep(5)

driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")  # Comeback the same place
value=driver.execute_script("return window.pageYOffset;")
print ("Number of pixel moved:", value)