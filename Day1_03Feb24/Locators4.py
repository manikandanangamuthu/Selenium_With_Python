from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

r_options = Options()
r_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=r_options)


driver.get("https://letcode.in")
driver.maximize_window()

# -----------------------------------------------------------------------
#driver.get("https://letcode.in")
#driver.maximize_window()
# Absoulte / Full xpath
      # Ex : /html[1]/body[1]/app-root[1]/app-header[1]/nav[1]/div[1]/div[2]/div[2]/div[1]/div[1]/a[1]

#driver.find_element(By.XPATH,"/html[1]/body[1]/app-root[1]/app-header[1]/nav[1]/div[1]/div[2]/div[2]/div[1]/div[1]/a[1]").click()
# =======================================================

# Relative / Partial xpath
     # Ex: //a[normalize-space()='Sign up']
#driver.find_element(By.XPATH,"//a[normalize-space()='Sign up']").click()

  # -------------------------------------------------------------------------

   # Xpath path types
   #     OR
   #     AND
   #     CONTAINS()
   #     Staart_With()
   #     test()

   #=======================================================
#  OR
# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()
# driver.find_element(By.XPATH,"//button[@type='button' or @class='button-2 product-box-add-to-cart-button']").click()
   #=======================================================

# AND

