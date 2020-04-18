import bs4

from selenium import webdriver

import sys
import time
import os


# getWFSlot('https://www.amazon.com/gp/buy/shipoptionselect/handlers/display.html?hasWorkingJavascript=1')


def getWFSlot(productUrl):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }

    driver = webdriver.Chrome()
    driver.get(productUrl)           
    html = driver.page_source
    soup = bs4.BeautifulSoup(html)
    time.sleep(60)


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
    os.system('C:\espeak\eSpeak\command_line\espeak.exe "Slots for delivery opened!"')
    time.sleep(600)

getWFSlot('https://shop.shipt.com/checkout')


