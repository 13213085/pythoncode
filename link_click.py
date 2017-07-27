# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 11:43:15 2017

@author: 29907
"""

from selenium import webdriver
import time
import Thread
driver=webdriver.Edge()
driver.get('http://inventwithpython.com')
link_ele=driver.find_element_by_link_text('Read It Online')
type(link_ele)
Thread.sleep(5000)
link_ele.click()
