import requests
# We need to install requests package through file -->> settings -->> Projectintrepreter
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

r_options = Options()
r_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=r_options)

driver.get("http://www.deadlinkcity.com/")

driver.maximize_window()

links=driver.find_elements(By.TAG_NAME,'a')
count=0

for link in links:
    URL=link.get_attribute('href')
    try:
     req=requests.head(URL)
    except:
         None
    if req.status_code>=400:
        print(URL, "Is Broken Link")
        count+=1
    else:
        print(URL, "Is valid Links")
print ("Total length of the Links ", count)

