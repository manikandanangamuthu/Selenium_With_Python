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

min_Slider=driver.find_element(By.XPATH,"//span[@tabindex='0']")

Act=ActionChains(driver)

print("Location Slider Before Moveing")

print(min_Slider.location)  #{'x': 762, 'y': 1087}

Act.drag_and_drop_by_offset(min_Slider,100,0).perform()

print("Location Slider After Moveing ")

print(min_Slider.location)


