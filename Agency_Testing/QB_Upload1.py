
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

r_options = Options()
r_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=r_options)

#driver.get("https://65.2.59.146:8373/OESWeb/Login/loginPage.jsp")

driver.get("https://192.168.198.242:8280/ExaminationPortalWeb/logout.jsp")

driver.maximize_window()