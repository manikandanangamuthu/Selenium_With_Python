import time
from telnetlib import EC

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

r_options = Options()
r_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=r_options)
wait=WebDriverWait(driver,10, poll_frequency=2, ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException])


driver.get("https://demo.nopcommerce.com")

driver.maximize_window()


click_nop=wait.until(EC.presence_of_element_located((By.LINK_TEXT,"nopCommerce")))
#click_nop=wait.until(EC.presence_of_element_located((By.LINK_TEXT,'nopCommerce')))
click_nop.click()
#driver.quit()

#driver.find_element(By.LINK_TEXT,"nopCommerce").click()