'''
Author: Steven Tong
Date: 2019-03-14 12:52:08
LastEditTime: 2021-03-14 13:18:24
LastEditors: Please set LastEditors
Description:This is an example to get the HTML page name on the server
'''
#!/usr/bin/python
#coding=utf-8

#urllib2是python自带的模块，在python3.x中被改为urllib.request
import urllib.request
import re

num = 1081

while (num < 1296):   
    # this number you need kown
    urlname='http://www.sina.com.cn/docs/tmp/neg'+str(num)+'.html'  
    # this URL is traget 
    page = urllib.request.urlopen(urlname)
    print(urlname)
    html = page.read().decode('utf-8')
    # Python3 findall  use bytes datatype
    # or html=urllib.urlopen(url).read()
    title=re.findall('<title>(.+)</title>',html)
    print (title)
    num = num + 1