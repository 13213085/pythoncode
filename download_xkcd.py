# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 08:48:37 2017

@author: 29907
"""

#download_xkcd.py - Downloads every every single XKCD comic.

import requests,os, bs4

url='http://xkcd.com'          #Intialize url
os.makedirs('xkcd',exist_ok=True)       #Build folder which saves xkcd comic

while not url.endswith('#'):
    #Download the page
    print('Downloading page %s...'%(url))
    res=requests.get(url)
    res.raise_for_status()
    
    soup=bs4.BeautifulSoup(res.text)
    
    #Find the url of the comic
    comic_ele=soup.select('#comic img')
    if len(comic_ele)==0:
        print('Could\'t find comic element')
    else:
        print(comic_ele[0].get('src'))
        comic_url='https:'+comic_ele[0].get('src')    #Get the url of comic image.
        
        #Download the page of the comic image
        res=requests.get(comic_url)
        res.raise_for_status()
        
        #Save image file to xkcd folder
        comic_file=open(os.path.join('xkcd',os.path.basename(comic_url)),'wb')
        for chunk in res.iter_content(100000):
            comic_file.write(chunk)
        comic_file.close()
        
    #Get the url of next comic page
    pref_link=soup.select('a[rel="prev"]')[0]
    url='https://xkcd.com'+pref_link.get('href')

print('Done') 
