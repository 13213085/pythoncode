# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 09:31:51 2017

@author: 29907
"""
import re
def strip_regex(text,sub=None):
    if sub==None:
        regex=re.compile(r'^\s+')
        print(text)
        print(regex)
        text=regex.sub(r'',text)
        return text
    else:
        regex=re.compile(sub)
        text=regex.sub('',text)
        return text
text=strip_regex('111  ddd','111')
print(text)