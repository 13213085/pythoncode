# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 11:56:53 2017

@author: 29907
"""

#remove_not_exist -change name of file 

import os,shutil,re

def remove_not_exist(folder):
    
    
    #Creat file regex
    filename_regex=re.compile(r'^No\d_quiz.txt$')
    
    #Get filename list
    filenames=os.listdir(folder)
    for filename in filenames:
        if filename_regex.search(filename)==None:
            filenames.remove(filename)
    filenames.sort()
    #Rename filename
    for i in range(len(filenames)):
  
        new_filename='No%s_quiz.txt'%(i)
 #       shutil.move(filename,new_filename)

os.chdir('F:/pythoncode')
filenames=os.listdir('F:/pythoncode')
filenames.sort()
remove_not_exist('F:/pythoncode')
shutil.move('No1_quiz.txt','No1_quiz.txt')