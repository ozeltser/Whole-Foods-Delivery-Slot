import bs4

from selenium import webdriver

import sys
import time
import os


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
      print("refreshed")
      html = driver.page_source
      soup = bs4.BeautifulSoup(html)
      time.sleep(4)

      # slot_pattern = 'Next available'
      # try:
      #    next_slot_text = soup.find('h4', class_ ='ufss-slotgroup-heading-text a-text-normal').text
      #    if slot_pattern in next_slot_text:
      #       print('SLOTS OPEN!')
      #       os.system('C:\espeak\command_line\espeak.exe "Slots for delivery opened!"')
      #       no_open_slots = False
      #       time.sleep(1400)
      # except AttributeError:
      #    pass

      # try:
      #    slot_opened_text = "Not available"
      #    all_dates = soup.findAll("div", {"class": "ufss-date-select-toggle-text-availability"})
      #    for each_date in all_dates:
      #       if slot_opened_text not in each_date.text:
      #          print('SLOTS OPEN!')
      #          os.system('C:\espeak\command_line\espeak.exe "Slots for delivery opened!"')
      #          no_open_slots = False
      #          time.sleep(1400)
      # except AttributeError:
      #    pass

      try:
         no_open_slots = True
         no_slot_pattern = 'No more delivery windows available.'
         slot_pattern_all = soup.findAll('div', {"class": "title-4"})
         for each_no_pattern in slot_pattern_all:
            print(each_no_pattern.text)
            if each_no_pattern.text == no_slot_pattern :
               print("NO SLOTS!")
               no_open_slots = False
      # except AttributeError: 
      #       print('SLOTS OPEN!')
      #       os.system('C:\espeak\command_line\espeak.exe "Slots for delivery opened!"')
      #       no_open_slots = False
   
   os.system('C:\espeak\command_line\espeak.exe "Slots for delivery opened!"')

# getWFSlot('https://www.amazon.com/gp/buy/shipoptionselect/handlers/display.html?hasWorkingJavascript=1')
getWFSlot('https://shop.shipt.com/checkout')

def match(toMatch) : 
    print(toMatch)
    pattern = 'No more delivery windows available.'
    print(pattern)


