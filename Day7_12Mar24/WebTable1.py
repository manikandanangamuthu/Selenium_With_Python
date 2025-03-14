from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
r_options = Options()
r_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=r_options,)

#========================================================================================
driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

# 1) Number of Rows & Columns

NoOfRows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))

NoOfColumn=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]//th"))

print("Number Of Rows",NoOfRows)  # Count Number of Rows

print("Number Of Columns",NoOfColumn)  # Count Number of Columns

# 2)Read specific Row & Column data    # Master In Selenium

data= driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[1]").text

print(data) # Master In Selenium

# 3) Read all rows and columns

All_Rows_Columns=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr/td"))
print(All_Rows_Columns)  # 24

print("No Of Rows and Columns...................")

for r in range(2,NoOfRows+1):
    for c in range(1,NoOfColumn+1):

        All_Rows_Columns = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(All_Rows_Columns,end='  ')
    print()

    # 4) Read the data based on conditions

    print("========================================")

    for r in range(2,NoOfRows+1):
        authorName= driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
        if authorName=="Mukesh":
           BookName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[1]").text
           Price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]").text
           print(BookName," ",authorName," ",Price)








