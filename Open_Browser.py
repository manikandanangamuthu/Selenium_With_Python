from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

r_options = Options()
r_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=r_options)

# Open the URL
driver.get("https://letcode.in/signup")

#Maximize the window
driver.maximize_window()

# # First time Sign UP Code
driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Manikandan")
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("manikandana998@gmail.com")
driver.find_element(By.XPATH, "//input[@id='pass']").send_keys("abcd@1234")
driver.find_element(By.XPATH, "//input[@id='agree']").click()
driver.find_element(By.XPATH, value="//button[contains(text(),'SIGN UP')]").click()






#-------------------------------------------------------------------------------------------------------
# After Sign Up to do login from next time

#driver.find_element(By.XPATH, "//*[text()='Log in']").click()
#driver.find_element(By.XPATH, "//input[@placeholder='Enter registered email']").send_keys("manikandana998@gmail.com")
#driver.find_element(By.XPATH, "//input[@placeholder='Enter password']").send_keys("abcd@1234")
#driver.find_element(By.LINK_TEXT("New Course!")).click()
#driver.find_element(By.XPATH, value="//Button[text()='LOGIN']").click()


#---------------------------------------------------------------------------------------------------------


# Take new Course

#driver.find_element(By.LINK_TEXT("New Course!")).click()







