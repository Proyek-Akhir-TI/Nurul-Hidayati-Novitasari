# %%
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# %%
#Link Digimap
for page_num in range(1, 10): 
        main_link = 'https://www.tokopedia.com/search?st=product&q='
        key="kain batik banyuwangi"

path = 'D:/chromedriver.exe'
s = Service(path)
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service=s, options=options)
driver.maximize_window()

driver.get(main_link+key)
wait = WebDriverWait(driver, 200)



driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
content = driver.page_source

#Bs4
soup = BeautifulSoup(content,"html.parser")

name, price, images, productLink =[],[],[],[]       

for i in soup.find_all('div', class_="css-svipq6"):
        name.append(i.text)
for i in soup.find_all('div', class_='css-1ksb19c'):
        price.append(i.text)
for img in soup.findAll('img'):
    images.append(img.get('src'))
for a in soup.find_all('a', href=True):
       productLink.append(a['href'])

#save data
listCols = ['name', 'price','images','productLink']
dict_data = dict(zip(listCols,
                    (name,
                    price,
                    images,
                    productLink)
))

# %%
import json
with open('tokopedia.json','w') as fp:
    json.dump(dict_data, fp)

