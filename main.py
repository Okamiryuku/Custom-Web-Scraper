import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import csv


URL = "https://steamdb.info/"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-CA,en-US;q=0.7,en;q=0.3"
}

FILE_NAME = 'steam_mpg_data.csv'


def soup_scraping(web_url):
    response = requests.get(url=web_url, headers=HEADERS)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    all_price_elements = soup.find_all(name="div", class_="property-address")
    all_prices = [price.get_text().split("+")[0] for price in all_price_elements]

    all_link_elements = soup.find_all(name="a", class_="property-link")
    return data


def selenium_scraping():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(URL)

    sleep(2)

    mpg_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    mpg_button.click()

    sleep(2)

    all_time_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    all_time_button.click()

    sleep(2)

    web_url = driver.current_url

    return web_url


web_url = selenium_scraping()

data = soup_scraping(web_url=web_url)


# Specify the file name


# Writing to the CSV file
with open(FILE_NAME, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
