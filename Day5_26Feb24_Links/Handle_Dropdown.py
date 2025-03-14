import time

from select import select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

r_options = Options()
r_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=r_options)

#time.sleep(20)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()


#drop_list=driver.find_elements(By.XPATH,"//select[@id='country']")

drop_country=Select(driver.find_elements(By.XPATH,"//select[@id='country']"))


# Select one option from the dropdown list
drop_country.select_by_visible_text("France")
