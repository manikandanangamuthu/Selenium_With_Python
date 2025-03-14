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



driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

source_ele=driver.find_element(By.ID,"draggable")

traget_ele=driver.find_element(By.ID,"droppable")

Act=ActionChains(driver)

Act.drag_and_drop(source_ele,traget_ele).perform()