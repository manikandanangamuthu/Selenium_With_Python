from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

r_options = Options()
r_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=r_options)

driver.get("https://demo.nopcommerce.com/")

driver.maximize_window()

# Click on Links

#driver.find_element(By.LINK_TEXT,"Digital downloads").click()

#driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()

# Find Number of links in the page

#Total_links=driver.find_elements(By.TAG_NAME,"a")
Total_links=driver.find_elements(By.XPATH,'//a')

print("Total number of Links :", len(Total_links))

# Print all the links

for link in Total_links:
    print(link.text)