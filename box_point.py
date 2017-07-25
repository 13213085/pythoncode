# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 08:25:45 2017

@author: 29907
"""

def box_point(symbol,width,height):
    if len(symbol)!=1:
        raise Exception('Symbol must be a single character string.')
    if width<=2:
        raise Exception('Width must be greater than 2.')
    if height<=2:
        raise Exception('Height must be greater than 2.')
        
    print(symbol*width)
    for i in range(height-2):
        print(symbol+' '*(width-2)+symbol)
    print(symbol*width)
    
for symbol,width,height in (('*',3,4),('0',4,23),('3',1,2),('11',3,3)):
    try:
        box_point(symbol,width,height)
    except Exception as err:
        print('An exception happened: '+str(err))