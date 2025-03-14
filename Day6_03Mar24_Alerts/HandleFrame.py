import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

r_options = Options()
r_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=r_options)

# driver.get("https://the-internet.herokuapp.com/basic_auth") # normal url passing

driver.get("https://demo.automationtesting.in/Frames.html")

driver.maximize_window()

# Single Frame  ====================================================
#driver.switch_to.frame("SingleFrame")
#driver.find_element(By.XPATH,"/html[1]/body[1]/section[1]/div[1]/div[1]/div[1]/input[1]").send_keys("Manikandan")

#====================================================================

# Multiple Frames

driver.find_element(By.LINK_TEXT,"Iframe with in an Iframe").click()


OuterFrame=driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")

driver.switch_to.frame(OuterFrame)

InnerFrame=driver.find_element(By.XPATH,"//iframe[@src='SingleFrame.html']")

driver.switch_to.frame(InnerFrame)

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Hello!")

driver.switch_to.parent_frame()  # Directly switch to parent frame (Outerframe)