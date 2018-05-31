# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, 'html.parser')

print('获取所有的链接')
links = soup.find_all('a')
for link in links:
    print(link['href'], link.name, link.get_text())
    
print('获取Lacie的URL')
link1 = soup.find('a', href=re.compile(r'lacie'))
print(link1['href'])


print('获取P段落文字')
paras = soup.find_all('p', class_="title")
for para in paras:
    print(para.get_text())
