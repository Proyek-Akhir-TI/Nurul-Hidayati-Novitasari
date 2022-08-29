from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv
from time import sleep

path = 'D:/chromedriver.exe'
s = Service(path)
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# chrome_options.add_argument('disable-notifications')
# chrome_options.add_argument('--disable-infobars')
# chrome_options.add_argument('start-maximized')

# chrome_options.add_experimental_option("prefs", {
#     "profile.default_content_setting_values.notifications": 2
# })


def get_url(search_term):
    """Generate an url from the search term"""
    template = "https://www.tokopedia.com/search?st=product&q={}"
    search_term = search_term.replace(' ', '+')

    # add term query to url
    url = template.format(search_term)

    # add page query placeholder
    url += '&page={}'

    return url





def main(search_term):
    # invoke the webdriver
    driver = webdriver.Chrome(service=s, options=options)
    rows = []
    url = get_url(search_term)

    for page in range(0, 3):
        driver.get(url.format(page))
        WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "css-1wc186l e110g5pc0")))
        driver.execute_script("""
        var scroll = document.body.scrollHeight / 10;
        var i = 0;
        function scrollit(i) {
           window.scrollBy({top: scroll, left: 0, behavior: 'smooth'});
           i++;
           if (i < 10) {
            setTimeout(scrollit, 500, i);
            }
        }
        scrollit(i);
        """)
        sleep(5)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', {'class': 'pcv3__container css-gfx8z3'}):
            name = item.find('div', {'class': 'css-svipq6'})
            if name is not None:
                name = name.text.strip()
            else:
                name = ''

            price = item.find('div', {'class': 'css-1u1z2kp'})
            if price is not None:
                price = text.strip()
            print([name, price])
            rows.append([name, price])

    with open('shopee_item_list.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Product Description', 'Price'])
        writer.writerows(rows)
        
        