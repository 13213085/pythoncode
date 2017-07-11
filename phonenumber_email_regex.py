# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 09:17:22 2017

@author: 29907
"""

import re
import pyperclip
#build phonenumber and email regex
phonenumber_regex=re.compile(r'''(
                             (\d{3}|\(\d{3}\))?                   #area code
                             (\s|-|\.)?                           #separator
                             (\d{3})                              #firt 3 digits
                             (\s|-|\.)                            #separator
                             (\d{4})                              #last 4 didits
                             (\s|-|\.)                            #separator
                             (\s*(ext|x|ext.)\s*(\d{2,5}))?       #extension
                             )''',re.VERBOSE)
email_regex=re.compile(r'''(
                       [a-zA-Z0-9._%+-]+                          #username
                       @                                          #@ symbol
                       [a-zA-Z0-9.-]+                             #domain name
                       (\.[a-zA-Z]{2,4})                          #dot something
                       )''',re.VERBOSE)
                            
                             
#copy clipboard content
text=str(pyperclip.paste())
matches=[]

#find phonenumber and email
for groups in phonenumber_regex.findall():
    phonenumber='-'.join(groups[1],groups[3],groups[5])          #link phonenumber with regular style
    if groups[8]!=' ':
        phonenumber+=' x'+groups[8]
        matches.append(phonenumber)
for groups in email_regex.findall():
    email=groups[0]
    matches.append(email)

#show match result    
if len(matches)!=0:
    pyperclip.copy('\n'.join(matches))
    print('copied to clipboard.')
    print('\n'.join(matches))
else:
    print('No phonenumber or email found.')
                           