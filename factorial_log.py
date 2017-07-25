# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 09:17:38 2017
@author: 29907
"""

import logging
logging.basicConfig(level=logging.DEBUG,format=' filename: %(filename)s ')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' %(n))    
    total=1
    for i in range(n+1):
        total*=i
        logging.debug('i is '+str(i)+'total is '+str(total))
    logging.debug('End of factorial(%s)'%(n))
    return total
print(factorial(5))
logging.debug('End of program')