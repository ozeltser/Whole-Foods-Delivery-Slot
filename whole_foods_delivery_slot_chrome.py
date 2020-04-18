import bs4

from selenium import webdriver

import sys
import time
import os


# getWFSlot('https://www.amazon.com/gp/buy/shipoptionselect/handlers/display.html?hasWorkingJavascript=1')


def getWFSlot(productUrl):
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    # }

    driver = webdriver.Chrome()
    driver.get(productUrl)           
    html = driver.page_source
    soup = bs4.BeautifulSoup(html, features="html.parser")
    time.sleep(10)


    # wait untill we get to proper checkout page_source
    while driver.current_url != productUrl:
        print('Current Url ' + driver.current_url)
        print('We are on the wrong page, waiting')
        time.sleep(10)

    driver.refresh()
    time.sleep(10)
    # html = driver.page_source
    # # soup.findAll('span', {"data-test": "Checkout-total"})
    # subtotal_pattern = soup.findAll('span')
    # for item in subtotal_pattern:
    #     print( item.attrs )
    # print(subtotal_pattern)


    no_open_slots = True
    while no_open_slots:
        driver.refresh()
        time.sleep(10)
        print("refreshed")
        html = driver.page_source
        soup = bs4.BeautifulSoup(html)
        

        no_open_slots = False
        no_slot_pattern = 'No more delivery windows available.'
        slot_pattern_all = soup.findAll('div', {"class": "title-4"})
        for each_no_pattern in slot_pattern_all:
           print(each_no_pattern.text)
           if each_no_pattern.text == no_slot_pattern:
              print("NO SLOTS!")
              no_open_slots = True
    os.system(r'C:\espeak\eSpeak\command_line\espeak.exe "Slots for delivery opened!"')
    time.sleep(6000)

getWFSlot('https://shop.shipt.com/checkout')


