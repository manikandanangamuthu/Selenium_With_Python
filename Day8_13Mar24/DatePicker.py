from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

r_options = Options()
r_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=r_options)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()


driver.switch_to.frame(0)


# 1) Directly send date to through send keys
#driver.find_element(By.ID,"datepicker").send_keys("05/07/1997") # mm/dd/yyyy

# Expected Result
year="2025"
month="May"
date="07"


# Select date picker

driver.find_element(By.ID,"datepicker").click()

while True:
    Mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    Yr=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if Mon==month and Yr==year:
        break;
    else:
      driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()

# Date Select

dates=driver.find_elements(By.XPATH,"//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")

for ele in dates:
    if ele.text==date:
        ele.click()
        break

