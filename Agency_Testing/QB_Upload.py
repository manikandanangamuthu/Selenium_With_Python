import time
from argparse import Action
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

r_options = Options()
r_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=r_options)

driver.get("https://192.168.158.89:8180/OESWeb//admin/DashBoard.jsp")

driver.maximize_window()

driver.find_element(By.XPATH,"//*[@id='details-button']").click()
driver.find_element(By.XPATH,"//a[@id='proceed-link']").click()

driver.find_element(By.NAME,"username").send_keys("nseitadmin")
driver.find_element(By.NAME,"password").send_keys("nseit@1234")
driver.find_element(By.NAME,"Submit").click()

#Now select Upload Management




#=====================================================================
#
# driver.find_element(By.LINK_TEXT,"Customer QB Management").click()
# time.sleep(5)
# driver.find_element(By.LINK_TEXT,"Upload Question Bank").click()
# time.sleep(5)
# dropdown = Select(driver.find_element(By.NAME,"ModuleId"))
# time.sleep(2)
# moduleName="New Module 1"
# optionGlobal=dropdown.options
# #dropdown1 = driver.find_element_by_id("ModuleId")
# print(optionGlobal)
# for option in optionGlobal:
#     print("....")
#     print(optionGlobal)
#     # Check if the option text starts with "IIBF Demo"
#     if option.text.startswith(moduleName):
#         dropdown.select_by_visible_text(option.text)
#         new_string = option.text.replace(" ", "").replace("-", "")
#         split_string = option.text.split('-')
#         driver.find_element(By.ID, "qbankName").send_keys(new_string+"_15MAR")
#         driver.find_element(By.ID, "qBankFileName").send_keys("C://Users//05444//Desktop//QB//"+moduleName+"//"+split_string[1].strip()+".zip")
#         message = driver.find_element(By.ID, "uploadBtn").click()
#
#
#
#
#
