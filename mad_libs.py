# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 08:42:17 2017

@author: 29907
"""

#mab_libs -Replace the vocabulary in the text file

import re

#Regex compile
vc_regex1=re.compile(r'ADJECTIVE')
vc_regex2=re.compile('NOUN')
vc_regex3=re.compile('ADVERB')
vc_regex4=re.compile('VERB')

#Enter replace word
print('Enter an abjective\n')
abjective_re=input()
print('Enter a noun\n')
noun_re=input()
print('Enter an adverb\n')
adverb_re=input()
print('Enter a verb\n')
verb_re=input()

#Look up and replace
object_file=open('num.txt')
text=object_file.read()
replace_text=vc_regex1.sub(abjective_re,text)
replace_text=vc_regex2.sub(noun_re,replace_text)
replace_text=vc_regex3.sub(adverb_re,replace_text)
replace_text=vc_regex4.sub(verb_re,replace_text)
object_file.close()

object_file=open('num.txt','w')
object_file.write(replace_text)
object_file.close()