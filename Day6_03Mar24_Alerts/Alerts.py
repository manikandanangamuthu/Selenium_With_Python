import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

r_options = Options()
r_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=r_options)
#========================================================================================
#driver.get("https://demo.automationtesting.in/Alerts.html")

#driver.maximize_window()


#driver.find_element(By.XPATH,"//button[@class='btn btn-danger']").click()
#myalert=driver.switch_to.alert

#print(myalert.text)   # Capture text message

#myalert.accept()  # Ok button we are clicking
#========================================================================================

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
driver.maximize_window()


driver.find_element(By.NAME,"alert").click()

time.sleep(5)
myalert=driver.switch_to.alert

print(myalert.text)

myalert.dismiss()


