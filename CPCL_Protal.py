from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

r_options = Options()
r_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=r_options)

driver.get("http://182.74.138.195:8934/TNCPCL/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,"a[href='../TNCPCL/instructions.jsp']").click()

driver.find_element(By.ID,"checkbox").click()
driver.find_element(By.ID,"continue").click()

driver.find_element(By.NAME,"candidateName").clear()
driver.find_element(By.NAME,"candidateName").send_keys("MANIKANDAN")

driver.find_element(By.XPATH, "//option[normalize-space()='Indian']").click()

driver.find_element(By.XPATH,"(//option[@value='10'])").click()

driver.find_element(By.XPATH,"//option[@value='473']").click()
