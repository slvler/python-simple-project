from bs4 import BeautifulSoup
import requests
from enum import Enum
class URL:
    class Status(Enum):
        BASE_URL = "https://www.amazon.com.tr/"

r = requests.get('https://www.amazon.com.tr/gp/bestsellers/home/13511265031')

soup = BeautifulSoup(r.content,'lxml')
product = soup.find_all('div', attrs={"class":"a-column a-span12 a-text-center _cDEzb_grid-column_2hIsc"})

for item in product:
    i = item.find_all("a", attrs={"class":"a-link-normal aok-block"})
    for x in i:
        text = URL.Status.BASE_URL.value + x.get('href')
        print(text)


