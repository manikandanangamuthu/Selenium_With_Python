from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

r_options = Options()
r_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=r_options)

driver.get("https://excelr.in/")
driver.maximize_window()

#=============================================================================

#Find out List of Webelements
slider=driver.find_elements(By.CLASS_NAME,"recommended-single")

print(len(slider)) # total  37 sliders available

links=driver.find_elements(By.TAG_NAME,"a")

print(len(links)) # Total 92 links are available

