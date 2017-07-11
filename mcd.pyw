# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 11:53:14 2017

@author: 29907
"""

#mcd.pyw - Save and loads pieces of text to the clipboard.
#Usage: py.exe mcd.pyw save <keyword> -Save clipboard to keyword.
#       py.exe mcd.pyw <keyword> -Loads keyword to clipboard.
#       py.exe mcd.pyw list - Loads all keywords to clipboard.
#       py.exe mcd.pyw delete <keyword> -Delete keyword 
#       py.exe mcd.pyw delete -Delete all keywords
import shelve, pyperclip, sys

mcd_shelf=shelve.open('mcd')

if len(sys.argv)==3 and sys.argv[1].lower()=='save':
    mcd_shelf[sys.argv[2]]=pyperclip.paste()
elif len(sys.argv)==3 and sys.argv[1].lower()=='delete':
    del mcd_shelf[sys.argv[2]]
elif len(sys.argv)==2: 
    if sys.argv[1].lower()=='list':
        pyperclip.copy(str(list(mcd_shelf.keys())))
    elif sys.argv[1] in list(mcd_shelf.keys()):
         pyperclip.copy(mcd_shelf[sys.argv[1]])
    elif sys.argv[1].lower()=='delete':
         for key in mcd_shelf.keys():
             del mcd_shelf[key]
    
mcd_shelf.close()