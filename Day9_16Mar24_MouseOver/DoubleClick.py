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

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick")

driver.maximize_window()

driver.switch_to.frame("iframeResult")
button=driver.find_element(By.XPATH,"//button[@ondblclick='myFunction()']")

Act=ActionChains(driver)

Act.double_click(button).perform()