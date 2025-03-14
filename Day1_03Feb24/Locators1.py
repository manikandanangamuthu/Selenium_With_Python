from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

r_options = Options()
r_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=r_options)

driver.get("https://demo.nopcommerce.com/")

driver.maximize_window()    #window maximize

# ----------  ID Selectors  -----------------
#driver.find_element(By.ID, "small-searchterms").clear()
#driver.find_element(By.ID, "small-searchterms").send_keys("Nokia Lumia 1020")

# -----------------------------------------------------------------------------------

# ----------- NAME Selectors --------------------

#driver.find_element(By.NAME, "q").clear()
#driver.find_element(By.NAME,"q").send_keys("HTC One Mini Blue")

#-------------------------------------------------------------------------------------

# ------ Link Text --------------------
#driver.find_element(By.LINK_TEXT, "Register").click()

#---------------------------------------------------------------------------------------
# ---------  Partial_Link_Text ---------------

driver.find_element(By.PARTIAL_LINK_TEXT, "Reg").click()

#-----------------------------------------------------------------------------------------

# ---------- CSS Selectors ------------------
driver.find_elements(By.CLASS_NAME,)
