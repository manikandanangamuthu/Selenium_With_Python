

# Test Case

#1. Open Web browser (Chrome/firefox/edge)
#2. Open URL : https://opensource-demo.orangehrmlive.com/
#3. Enter Username : Admin
#4. Enter Password : abcd@1234
#5. Click on Login
#6. Capture the title of the home page (Actual tile )
#7. Verify title of the page ()
#8. Close browser

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#r_options = Options()
#r_options.add_experimental_option('detach', True)
#driver: WebDriver = webdriver.Chrome(options=r_options)
driver=webdriver.Chrome()
driver.get("https://letcode.in/")
driver.maximize_window()

driver.find_element(By.XPATH, "//*[text()='Log in']").click()
driver.find_element(By.XPATH, "//input[@placeholder='Enter registered email']").clear()
driver.find_element(By.XPATH, "//input[@placeholder='Enter registered email']").send_keys("manikandana998@gmail.com")
driver.find_element(By.XPATH, "//input[@placeholder='Enter password']").clear()
driver.find_element(By.XPATH, "//input[@placeholder='Enter password']").send_keys("abcd@1234")
#driver.find_element(By.LINK_TEXT("New Course!")).click()
driver.find_element(By.XPATH, value="//Button[text()='LOGIN']").click()

act_title=driver.title
exp_title="LetCode with Koushik"

if act_title==exp_title:
     print("Login Test Case Pass!")
else:
     print("Login Test Case Fail..")
driver.close()












#WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//input[@name='username']"))).send_keys('Admin')

#WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//input[@name='password']"))).send_keys('admin123')


#WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//*[text()='Login']"))).clcik()