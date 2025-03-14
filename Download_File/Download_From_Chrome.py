
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
r_options = Options()
r_options.add_experimental_option('detach', True)

# Set download preferences
prefs = {
    "download.default_directory": "C:/Users/05444/Desktop/seleniumDownloadFiles",
    "download.prompt_for_download": False,
    "directory_upgrade": True,
    "safebrowsing.enabled": True,
    "safebrowsing.disable_download_protection": True,
    "profile.default_content_setting_values.automatic_downloads": 1
}
r_options.add_experimental_option("prefs", prefs)
r_options.add_argument("--no-sandbox")
r_options.add_argument("--disable-dev-shm-usage")
r_options.add_argument("--disable-gpu")
r_options.add_argument("--disable-software-rasterizer")

# Add preferences to ChromeOptions
r_options.add_experimental_option("prefs", prefs)

# Initialize the Chrome driver
driver = webdriver.Chrome(options=r_options)


driver.get("https://192.168.198.242:8180/OESWeb//admin/DashBoard.jsp")

driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='details-button']").click()
driver.find_element(By.XPATH,"//a[@id='proceed-link']").click()

driver.find_element(By.NAME,"username").send_keys("nseitadmin")
driver.find_element(By.NAME,"password").send_keys("nseit@1234")
driver.find_element(By.NAME,"Submit").click()

driver.find_element(By.LINK_TEXT,"Customer QB Management").click()
driver.implicitly_wait(5)
driver.find_element(By.LINK_TEXT,"Generate Question Bank").click()

# GenQBDropDownList=Select(driver.find_element(By.ID,"selectModule"))
# GenQBDropDownList.select_by_visible_text("Dove - ENG")
driver.implicitly_wait(5)
QBDrop=driver.find_element(By.ID,"selectModule")

GenQB=Select(QBDrop)

#Select by visible
GenQB.select_by_visible_text("Dove - ENG")
driver.implicitly_wait(5)

QbIdDrop=driver.find_element(By.ID,"selectQBIdr") # Question Bank Identifier

IdSelectDrop=Select(QbIdDrop)

IdSelectDrop.select_by_index(1)  # Question Bank identifier selected
driver.implicitly_wait(5)
driver.find_element(By.NAME,"encryptionKey").clear()
driver.find_element(By.NAME,"encryptionKey").send_keys("aaaaaaaaaa")
driver.implicitly_wait(5)
driver.find_element(By.NAME,"confEncryptionKey").clear()
driver.find_element(By.NAME,"confEncryptionKey").send_keys("aaaaaaaaaa")
driver.implicitly_wait(5)
driver.find_element(By.NAME,"zippwd").clear()
driver.find_element(By.NAME,"zippwd").send_keys("abcd@1234")

driver.implicitly_wait(5)
driver.find_element(By.NAME,"zippwd2").clear()
driver.find_element(By.NAME,"zippwd2").send_keys("abcd@1234")
driver.implicitly_wait(5)
driver.find_element(By.ID,"btnSubmit").click()








