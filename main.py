import time
import sys
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent



ua = UserAgent()
headers = {'User-agent': ua.random}
flag = True


class web_driver():

    driver = webdriver.Chrome()
    clicken = driver.find_element
    options = webdriver.ChromeOptions()


def card_product(card):

    for i in card:
        return [i.text for i in card]


def get_location(url):

    web_driver.options.add_argument(headers)
    web_driver.driver.get(url)
    time.sleep(5)

    try:
        web_driver.clicken(By.XPATH, '/html/body/div[6]/div/div[2]/div/div[2]/div/div/div[2]/div/div/button').click()
        time.sleep(2)
        card = BeautifulSoup(web_driver.driver.page_source, 'lxml').find('div', class_='ant-row ant-row-space-between').find_all('span', class_='bz-typography phone bz-typography-regular')
        # card = soup.find_all('span', class_='bz-typography phone bz-typography-regular')
        return card

    except Exception:
        time.sleep(2)
        card = BeautifulSoup(web_driver.driver.page_source, 'lxml').find('div', class_='ant-row ant-row-space-between').find_all('span', class_='bz-typography phone bz-typography-regular')
        # card = soup.find_all('span', class_='bz-typography phone bz-typography-regular')
        return card


def reservetion(products):

    for product in products:
        if len(products) == 1:
            web_driver.clicken(By.XPATH, '//*[@id="root"]/div[2]/div/section/section/main/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/span/div/button/span').click()
            time.sleep(2)
            web_driver.clicken(By.XPATH, '/html/body/div[6]/div/div[2]/div/div[2]/div/div/div/form/div/div[5]/div/div/div/div/div/button/span').click()
            time.sleep(2)
            web_driver.driver.close()
            web_driver.driver.quit()
            sys.exit()
        else:
            continue


def search():

    while flag:
        cards = get_location(url='https://l.bezlimit.ru/store/480524?type=p&cubes=999333784')
        products = card_product(cards)

        if products == None:
            continue
        if products != None:
            reservetion(products)


search()

# if __name__ =='__main__':
#     main()

