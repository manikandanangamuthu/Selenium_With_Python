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



driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

driver.maximize_window()

rightclick=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
#time.sleep(10)
Act=ActionChains(driver)
Act.context_click(rightclick).perform()
time.sleep(5)
driver.find_element(By.XPATH,"//span[normalize-space()='Copy']").click()
time.sleep(5)
driver.switch_to.alert.accept()
time.sleep(5)
driver.quit()