import string
import requests
from bs4 import BeautifulSoup

class MedlineScraper:

    def __init__(self):
        self.base_url = "https://medlineplus.gov/druginfo"
        self.drug_links = set()

    def get_categories(self):
        letters = string.ascii_uppercase
        result = list(map(lambda letter: self.base_url + "/drug_{}a.html".format(letter), letters))
        result.append("https://medlineplus.gov/druginfo/drug_00.html")
        return result

    def get_source(self, url):
        r = requests.get(url)
        if r.status_code == 200:
            return BeautifulSoup(r.content, "lxml")
        return False

    def get_all_drug_links(self, source):
        drug_elements = source.find("ul", attrs={"id": "index"}).find_all("li")
        drug_links = list(map(lambda drug: self.base_url + drug.find("a").get("href").replace(".", "", 1), drug_elements))
        return set(drug_links)

    def find_all_drug_links(self):
        categories = self.get_categories()
        for category_link in categories:
            category_source = self.get_source(category_link)
            self.drug_links.union(self.get_all_drug_links(category_source))
        return self.drug_links

if __name__ == "__main__":
    scraper = MedlineScraper()
    source = scraper.get_source("https://medlineplus.gov/druginfo/drug_Aa.html")
    print(scraper.get_all_drug_links(source))


