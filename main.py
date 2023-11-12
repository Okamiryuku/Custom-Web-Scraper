from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import csv


URL ='https://steamdb.info/charts/?sort=peak'
FILE_NAME = 'steam_mpg_data.csv'


def selenium_scraping():
    data= []
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(URL)

    sleep(5)

    mpg_button = driver.find_element(By.XPATH, '//*[@id="table-apps_length"]/label/select/option[7]')
    mpg_button.click()

    sleep(5)

    # Locate the table element (adjust the XPath or other locator based on your HTML structure)
    table = driver.find_element(By.XPATH, '//*[@id="table-apps"]')

    # Get all the rows from the table
    rows = table.find_elements(By.TAG_NAME, "tr")

    # Iterate through rows and print data
    for row in rows:
        # Get all the cells in each row
        cells = row.find_elements(By.TAG_NAME, "td")

        # Extract and print data from each cell
        row_data = [cell.text for cell in cells]
        data.append(row_data)

    # Close the browser window
    driver.quit()
    return data


data = selenium_scraping()


with open(FILE_NAME, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f'CSV file "{FILE_NAME}" has been created.')
