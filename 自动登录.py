#coding=utf-8
import time
from selenium import webdriver
import time

from splinter import Browser

def splinter(url):
    browser = webdriver.Firefox()
    browser.get(url)
    #wait web element loading
    time.sleep(5)
    #fill in account and password
    browser.find_element_by_id('auto-id-1501856021089').send_keys("xieyutao01")
    browser.find_element_by_id(' auto-id-1501856021044').send_keys("xieyutao")
    #click the button of login
    browser.find_element_by_id('dologin').click()
    time.sleep(8)
    #close the window of brower
    browser.quit()

if __name__ == '__main__':
    websize3 ='http://www.126.com'
    splinter(websize3)