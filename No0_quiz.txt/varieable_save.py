# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 09:29:48 2017

@author: 29907
"""

import shelve
import pprint
cats={'Kate':3,';Hary':2}
shelf_file=shelve.open('mydata')
shelf_file['cats']=cats
shelf_file.close()
shelf_file=shelve.open('mydata')
b=list(shelf_file.keys())
a=shelf_file['cats']
shelf_file.close()

cats={'Kate':3,';Hary':2}
pprint.pformat(cats)
file_object=open('my.py','w')
file_object.write('cats='+pprint.pformat(cats)+'\n')
file_object.close()

import my
d=my.cats