from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

r_options = Options()
r_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=r_options)

driver.get("https://www.techlistic.com/p/selenium-practice-form.html")

driver.maximize_window()

checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.clear()