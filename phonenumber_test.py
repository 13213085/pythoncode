# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 18:46:47 2017

@author: 29907
"""

import re
phonenumber_regex=re.compile(r'(\(\d\d\d\)) (\d\d\d?-\d\d\d\d)')
phonenumber_regex2=re.compile(r'(\(\d{3}\))-\d{3}-\d{4}?')
phonenumber_regex3=re.compile('\(\\(\\d\{3\}\\)\)-\\d\{3\}-\\d\{4\}')
mo=phonenumber_regex.search('my phone number is (555) 65-3433?')
a=mo.group()
print(phonenumber_regex2)

Ha_regex=re.compile(r'(Ha)+')
mo=Ha_regex.search('HaHaHaHa')
a=mo.group()

phonenumber_regex=re.compile(r'^(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo=phonenumber_regex.findall('415-555-9999,123')
print(phonenumber_regex)