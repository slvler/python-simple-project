from bs4 import BeautifulSoup
import requests



headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}

url = "https://www.amazon.com.tr/HyperX-Pulsefire-Haste-Siyah-K%C4%B1rm%C4%B1z%C4%B1-Mouse/dp/B09QX54293?ref_=Oct_DLandingS_D_42212d44_7"


req = requests.get(url, headers=headers)


soup = BeautifulSoup(req.content, "html.parser")

#title = soup.find('span', attrs={'id': 'productTitle'}).get_text().strip()

#price = soup.find('span', attrs={'class': 'a-price-whole'}).get_text().strip()

#price_fraction = soup.find('span', attrs={'class': 'a-price-fraction'}).get_text().strip()

#print(title)
#print(price + '' + price_fraction)


brand = soup.find('a', attrs={'id': 'bylineInfo'})

print(brand.get_text().strip().replace('Marka: ', ''))

# tch_name = soup.find_all("th", attrs={'class':'a-color-secondary a-size-base prodDetSectionEntry'})
# tch_value = soup.find_all("td", attrs={'class':'a-size-base prodDetAttrValue'})
#
#
# list1 = []
# list2 = []
#
#
# for i in  tch_name:
#     list1.append(i.get_text().strip())
#
# for i in tch_value:
#     list2.append(i.get_text().strip().replace('\u200e', ''))
#
#
#
# #print(list1)
# #print(list2)
#
# dist1 = dict(zip(list1, list2))
#
# print(dist1)