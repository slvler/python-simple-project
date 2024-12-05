#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


CHROME_DRIVER_PATH = "#"
CHROME_BINARY_PATH = "#"

options = Options()
options.binary_location = CHROME_BINARY_PATH

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=options)

driver.get("https://www.imdb.com")

print("current_url", driver.current_url)
print("title", driver.title)

WAIT_ELEMENT = 3
XPATH_VALUE = '//*[@id="imdbHeader"]'
x = WebDriverWait(driver, WAIT_ELEMENT).until(EC.presence_of_element_located((By.XPATH, XPATH_VALUE)))
outerHTML = x.get_attribute('outerHTML')
print(outerHTML)

# driver.close()
# driver.quit()
