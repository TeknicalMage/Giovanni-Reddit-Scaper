import pickle
import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import select
from selenium.webdriver.support.ui import Select

import random
import os


def access():
    chrome_options = Options()
    chrome_options.add_argument("--log-level=3")


    driver = webdriver.Chrome(chrome_options=chrome_options)
    

    site_access = "https://www.reddit.com/r/CointestOfficial/new/"

    #Splits
    controversial_view = site_access + "controversial"
    #

    driver.get(site_access)
    print('We are on ' + site_access)
    time.sleep(2)


    #searchbar = driver.find_element_by_xpath('//*[@id="gh-ac"]')
    #searchbutton = driver.find_element_by_xpath('//*[@id="gh-btn"]')

    #fillertext = "tire 205/55r16"
    #searchbar.send_keys(fillertext)
    time.sleep(0.2)
    #searchbutton.click()
    time.sleep(0.2)
    print('Type something')
    wack = input()
    print(wack)

    #driver.get(controversial_view)

    #driver.find_elements_by_xpath('//*[@data-testid="post-container"]')

    nifty = []

    time.sleep(3)
    

    val = 0
    for val in range(10):
        time.sleep(1.5)
        print(driver.find_elements_by_xpath('//a[@data-click-id="body"]')[val].get_attribute('href'))


    time.sleep(1000)


    #select = Select(driver.find_element_by_xpath("//*[@name='userDate']"))
    #select.select_by_value('2015')



    


    time.sleep(30000)


        

        


access()

