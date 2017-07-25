# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 08:40:11 2017

@author: 29907
"""

import re 
#name_regex=re.compile('bb\\(\\\\a|aa)')
#a=mo.group()
#print(name_regex)
#print(a)

name_regex=re.compile(r'First Name:.*Last Name:.*')
mo=name_regex.findall('First Name:ffLast Name:LL')

names_regex=re.compile(r'Agent (\w)\w*')
a=names_regex.sub(r'\1CC','Agent Xiaobai told Agent Xiaomiao is double agent.')
print(a)