# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 07:41:27 2017

@author: 29907
"""

#lucky.py - Open several google search results.

import sys,requests,webbrowser,bs4

if len(sys.argv)<2:               #判断输入是否正确         
    print('Input error')
    
print('Gooling')                 #在下载goole页面时显示文本
res=requests.get('http://google.com/search?q='+' '.join(sys.argv[1:]))
res.raise_for_status()

#取出前五个搜索结果
soup=bs4.BeautifulSoup(res.text)
links=soup.select('h3 a')       #在浏览器中打开链接
number_open=min(5,len(links))
for i in range(number_open):
    webbrowser.open(links[i].get('href'))
