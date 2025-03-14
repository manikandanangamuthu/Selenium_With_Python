from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

r_options = Options()
r_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=r_options)

# Open the URL
driver.get("https://text-compare.com/")

#Maximize the window
driver.maximize_window()


input1=driver.find_element(By.ID,"inputText1")
input2=driver.find_element(By.ID,"inputText2")

input1.send_keys("Hello Manikandan!")

Act=ActionChains(driver)

# First select all --->> CRL+A -->> select the text

# Act.key_down(Keys.CONTROL)
# Act.send_keys("a")
# Act.key_up(Keys.CONTROL)
# Act.perform()

# Above lines can add as a single line
Act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

# Copy the Text -->> CRL+C
#
# Act.key_down(Keys.CONTROL)
# Act.send_keys("c")
# Act.key_up(Keys.CONTROL)
# Act.perform()
Act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# Navigate to tab 2 Second input tab
#
# Act.send_keys(Keys.TAB)
# Act.perform()

Act.send_keys(Keys.TAB).perform()

# Paste The copy the text

# Act.key_down(Keys.CONTROL)
# Act.send_keys("v")
# Act.key_up(Keys.CONTROL)
# Act.perform()

Act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
