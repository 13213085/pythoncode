# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 08:52:43 2017

@author: 29907
"""
import re 
code=input()
code_regex1=re.compile(r'[A-Z]')
code_regex2=re.compile(r'[a-z]')
code_regex3=re.compile(r'\d')
if len(code)<8:
    print(2)
try:
    mo1=code_regex1.search(code)
    mo2=code_regex2.search(code)
    mo3=code_regex3.search(code)
    print('1')
    print(mo1)
    print(mo2)
    print(mo3)
except:
    print(2)