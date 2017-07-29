# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 10:01:28 2017

@author: 29907
"""

#2048_game.py -- Auto play 2048 game

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Open 2048 game website
browser=webdriver.Opera()
browser.get('http://gabrielecirulli.github.io/2048/')

html_ele=browser.find_element_by_class_name('container')     #Select html element

for i in range(1000):
    if i%4==0:
        html_ele.send_keys(Keys.UP)
    if i%4==1:
        html_ele.send_keys(Keys.RIGHT)
    if i%4==2:
        html_ele.send_keys(Keys.DOWN)
    if i%4==3:
        html_ele.send_keyd(Keys.LEFT)
