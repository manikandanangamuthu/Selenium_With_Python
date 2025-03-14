
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

r_options = Options()
r_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=r_options)

driver.get("https://192.168.198.242:8180/OESWeb//admin/DashBoard.jsp")

driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='details-button']").click()
driver.find_element(By.XPATH,"//a[@id='proceed-link']").click()

driver.find_element(By.NAME,"username").send_keys("nseitadmin")
driver.find_element(By.NAME,"password").send_keys("nseit@1234")
driver.find_element(By.NAME,"Submit").click()

driver.find_element(By.LINK_TEXT,"Upload Management").click() #Now select Upload Management
driver.implicitly_wait(5)
driver.find_element(By.LINK_TEXT,"Upload Exam Logo").click() # Now select Upload Exam Logo
driver.implicitly_wait(5)
driver.find_element(By.ID,"cmpName").clear() # Clear the company name text box
driver.implicitly_wait(5)
driver.find_element(By.ID,"cmpName").send_keys("NSEIT") # Now enter new in the text box
driver.implicitly_wait(5)
driver.find_element(By.ID,"logoFile").send_keys("D://Manikandan//Capture001.png")
#driver.implicitly_wait(10)
#driver.close()