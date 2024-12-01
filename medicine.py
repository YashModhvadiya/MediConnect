from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def links(user):
    file_path = "C:\\Users\\Yash\\OneDrive\\Desktop\\main\\User\\Initializing\\medicine.txt"
    fp = open(file_path, "r")
    mediciene = fp.readlines()
    fp.close()

    medicine_names = []
    for item in mediciene:
        if "|" in item:
            name = item.split("|")[0].strip()
            medicine_names.append(name)
    l = ""
    for items in medicine_names:
        l = l + items+ "\n"
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.netmeds.com/catalogsearch/result/"+items+"/all")
        time.sleep(5)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        href_ = soup.find_all(class_="ais-InfiniteHits-item")
        i = 0
        for paragraph in href_:
            category_name_element = paragraph.find('a', class_='category_name')
            if category_name_element and (i<3):
                href_value = category_name_element['href']
                l = l + "https://www.netmeds.com" + href_value + "\n"
                i = i + 1
            else:
                break
        driver.quit()
        l = l +"\n\n"
    return l

# links("meghal")


# l = links(file_path)
# print(l)