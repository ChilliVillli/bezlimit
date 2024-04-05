import time
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent



ua = UserAgent()
headers = {'User-agent': ua.random}



def card_product(card):

    for i in card:
        return [i.text for i in card]


def get_location(url):

    session = requests.Session()
    session.headers.update(headers)
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[6]/div/div[2]/div/div[2]/div/div/div[2]/div/div/button').click()
    soup = BeautifulSoup(driver.page_source, 'lxml')
    card = soup.find_all('span', class_='bz-typography phone bz-typography-regular')
    return card


def reservetion(products, driver):

    for product in products:

        if len(products) == 1:
            driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/section/section/main/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/span/div/button').click()
            print(product)
        else:
            continue



def main():

    while True:
        cards = get_location(url='https://l.bezlimit.ru/store/480524?type=p&cubes=999333761')
        products = card_product(cards)

        if products == None:
            continue
        if products != None:
            reservetion(products)


if __name__ =='__main__':
    main()

