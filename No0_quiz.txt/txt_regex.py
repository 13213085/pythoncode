# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 09:50:06 2017

@author: 29907
"""
#txt_regex -Look up all matched text in text file.

import re,os

#Open all text file.
file_list=os.listdir('.')
txt_list=[]
for file in file_list:
    print(file)
    if file[-3:]=='txt':
        txt_list.append(file)

match_regex=re.compile(r'A$')
for file in txt_list:
    text_file=open(file)
    text_list=text_file.readlines()
    for line in text_list:
        if match_regex.search(line)!=None:
            print(line)
    text_file.close()
            
            