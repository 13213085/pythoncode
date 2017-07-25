# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 09:39:57 2017

@author: 29907
"""

#backuptozip -Copies a entire folder to a ZIP file whose filename increments

import os,zipfile

def backuptozip(folder):
    
    folder=os.path.abspath(folder)
    
    #Find out the filename which does't exist
    num=1
    while True:
        filename=os.path.basename(folder)+'_'+str(num)+'.zip'
        if not os.path.exists(filename):
            break
        num=num+1
    #Creat zip file
    print('Creat %s file.'%(filename))
    copy_file=zipfile.ZipFile(filename,'w')
    
    #Walk the entire folder and add each folder to zip file
    for foldername,subfolders,filenames in os.walk(folder):
        print('Adding file in '+foldername)
        copy_file.write(foldername)
        for filename in filenames:
            new_base=os.path.basename(folder)+'_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue
            copy_file.write(os.path.join(foldername,filename))
    
    copy_file.close()
    print('Done')
    
backuptozip('F:/pythoncode')