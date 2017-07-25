# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 07:57:11 2017
@author: 29907
"""

#rename_date -Rename filenames with MM-DD-YYYY date format 
#to European DD-MM-YYYY

import os,re,shutil

#build American date regex
date_regex=re.compile(r'''^(.*)?           #all text before the date
                      ((0|1)?\d)-             #month
                      ((0|1|2|3)?\d)-              #day
                      (19|20\d\d)-         #year
                      (.*)?$               #all text after the date
                      '''
                      ,re.VERBOSE)

#Look over the directory
os.chdir('F:/pythoncode')
for foldername,subfolders,filenames in os.walk('F:/pythoncode'):
    for filename in filenames:
        mo=date_regex.search(filename)
        if mo!=None:
            
            #Get the different parts of filename
            before_part=mo.group(1)
            month_part=mo.group(2)
            day_part=mo.group(4)
            year_part=mo.group(6)
            after_part=mo.group(7)
            
            #Rename the file
            newname=before_part+day_part+'-'+month_part+'-'+year_part    #os.path.join(abs,newname)
            newname_path=foldername+'/'+newname
            oldname_path=foldername+'/'+filename
            print('Renaming %s to %s'%(oldname_path,newname_path))
            #shutil.move(oldname_path,newname_path) #uncomment aftering test