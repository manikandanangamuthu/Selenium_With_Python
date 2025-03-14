import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

# Set up Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('--ignore-certificate-errors')

# Launch Chrome browser
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://192.168.198.242:8280/ExaminationPortalWeb/logout.jsp')
driver.maximize_window()

# Log in
driver.find_element(By.XPATH, "//*[@id='username']").send_keys("Superadmin")
driver.find_element(By.XPATH, "//*[@id='password']").send_keys("abcd@1234")
driver.find_element(By.XPATH, "//*[@class='btncaption input-donebtn']").click()

# Navigate to Data Transfer > Pull Results
driver.find_element(By.LINK_TEXT, "Data Transfer").click()
driver.find_element(By.LINK_TEXT, "Pull Results").click()

# Get dropdowns

time.sleep(5)
examDate = Select(driver.find_element(By.XPATH, "//*[@name='resultDate']"))
time.sleep(5)
examBatch = Select(driver.find_element(By.XPATH, "//*[@name='resultTime']"))
time.sleep(5)
testCenter = Select(driver.find_element(By.XPATH, "//*[@id='testCenterId']"))

# Iterate through exam dates
for i in range(1, len(examDate.options)):
    try:
        examDate.select_by_index(i)

        # Iterate through batches
        for j in range(1, len(examBatch.options)):
            try:
                examBatch.select_by_index(j)

                # Iterate through test centers
                for k in range(1, len(testCenter.options)):
                    try:
                        testCenter.select_by_index(k)

                        # Click the Pull Results button
                        submit_button = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, "//*[@id='resultImportBtnId']"))
                        )
                        submit_button.click()

                        # Wait for the error message to appear
                        error_message = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.TAG_NAME, "strong"))
                        )
                        print(f"Error Message: {error_message.text}")

                    except StaleElementReferenceException:
                        testCenter = Select(driver.find_element(By.XPATH, "//*[@id='testCenterId']"))
                        testCenter.select_by_index(k)

            except StaleElementReferenceException:
                examBatch = Select(driver.find_element(By.XPATH, "//*[@name='resultTime']"))
                examBatch.select_by_index(j)

    except StaleElementReferenceException:
        examDate = Select(driver.find_element(By.XPATH, "//*[@name='resultDate']"))
        examDate.select_by_index(i)

driver.quit()
