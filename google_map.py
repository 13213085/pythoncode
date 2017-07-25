# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 09:48:36 2017

@author: 29907
"""
#google_map.py - Lauches a map in the browser using an address from the command line 
#or clipboard

import sys,webbrowser,pyperclip

if len(sys.argv)>1:
    #Get address from comand line
    address=' '.join(sys.argv[1:])
    
    #Get address from clipboard
else:
    address=pyperclip.paste()
    
#Get URL
url='https://www.google.com/maps/place/'+address
webbrowser.open(url)    