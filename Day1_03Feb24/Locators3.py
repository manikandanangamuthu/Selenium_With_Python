from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

r_options = Options()
r_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=r_options)


driver.get("https://letcode.in/signup")
driver.maximize_window()

#---------------------------------------------------

#CSS Selectors Tag&ID

#driver.find_element(By.CSS_SELECTOR, "input#name").clear()

#driver.find_element(By.CSS_SELECTOR, "input#name").send_keys("Manikandan")

#driver.find_element(By.CSS_SELECTOR, "#name").clear()

#driver.find_element(By.CSS_SELECTOR, "input#name").send_keys("Mani")

#---------------------------------------------------

# CSS Selectors Tag&Class

#driver.find_element(By.CSS_SELECTOR,"input.input ng-pristine ng-invalid ng-touched").clear()
#driver.find_element(By.CSS_SELECTOR,"input.input ng-pristine ng-invalid ng-touched").send_keys("mani@gmail.com")

# The above 2 lines get no such elements error. So solution for above Css selector only enter first word of class name # refere blow line code
#driver.find_element(By.CSS_SELECTOR,"input.input").clear()
#driver.find_element(By.CSS_SELECTOR,"input.input").send_keys("mani")

#driver.find_element(By.CSS_SELECTOR,"button.button").click()

#-------------------------------------------------------

# CSS Selectors Tag & Attribute

driver.find_element(By.CSS_SELECTOR,"input[placeholder=Enter valid email address]").clear()

driver.find_element(By.CSS_SELECTOR,"input[placeholder=Enter valid email address]").send_keys("mani@nseit.com")