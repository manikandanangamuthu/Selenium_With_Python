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

driver.get("https://65.2.59.146:8373/OESWeb/Login/loginPage.jsp")

driver.maximize_window()

driver.find_element(By.XPATH,"//button[@id='details-button']").click()
driver.find_element(By.ID,"proceed-link").click()
driver.find_element(By.NAME,"username").send_keys("nseitadmin")
driver.find_element(By.NAME,"password").send_keys("nseit@1234")
driver.find_element(By.NAME,"Submit").click()


# Upload Management -->> TestCenter -->> Upload TestCenter

management=driver.find_element(By.LINK_TEXT,"Candidate Management")

admit=driver.find_element(By.LINK_TEXT,"Admit Card")

gen_admitcard=driver.find_element(By.LINK_TEXT,"Generate Admit Card")

# MouseHover

Act=ActionChains(driver)

Act.move_to_element(management).move_to_element(admit).move_to_element(gen_admitcard).click().perform()

