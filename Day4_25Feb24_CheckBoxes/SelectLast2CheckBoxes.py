from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

r_options = Options()
r_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=r_options)

# select last 2 checkboxes

driver.get("https://www.techlistic.com/p/selenium-practice-form.html")

driver.maximize_window()

checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")

print(len(checkboxes))  # Total length of the checkboxes -> 5

for i in range(len(checkboxes)-2, len(checkboxes)):   # range (5-2, 5)  range (3,5)
    checkboxes[i].click()
