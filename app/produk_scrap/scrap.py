from itertools import product
from wsgiref import headers
import requests
from bs4 import BeautifulSoup
import lxml


url = "https://www.tokopedia.com/search?st=product&q=batik%20banyuwangi&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&navsource="

# def get_link_product(url):
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "Accept-Language" : "en,in",
}
r = requests.get(url, headers=headers)
# soup = BeautifulSoup(url,"lxml")
# allProducts = soup.findAll(class_="pcv3__container css-gfx8z3")
# for product in allProducts:
#     name = product.find(class_="css-svipq6").getText()
#     name = name.strip()
#     price = product.find(class_="css-1ksb19c").getText()
#     img = product.find('img')
#     img = img['src']
#     productLink = product.find('a')
#     productLink = productLink["href"][7:]
        
#     print (name, price, productLink, img)
soup = BeautifulSoup(r.text, "lxml")
allProducts = soup.findAll(class_="pcv3__container css-gfx8z3")
number = 0
for product in allProducts:
    name = product.find(class_="css-svipq6")
    if name is not None:
        number += 1
        print("Product number %d:" % number)
        print("Name : " + name.text)
        productLink = product.find('a')
        print("Link : " + productLink["href"][7:])
        img = product.find('img')
        print("Image : " + img["src"])
        price = product.find(class_="css-1ksb19c")
        print("Price " + price.text)
        
        print(name, productLink, img, price)
    # soup = BeautifulSoup(url,"lxml")
    # allProducts = soup.findAll(class_="pcv3__container css-gfx8z3")
    # for product in allProducts:
    #     name = product.find(class_="css-svipq6").getText()
    #     name = name.strip()
    #     price = product.find(class_="css-1ksb19c").getText()
    #     img = product.find('img')
    #     img = img['src']
    #     productLink = product.find('a')
    #     productLink = productLink["href"][7:]
        
    # print (name, price, productLink, img)
    
#     print(get_link_product(url))






    
