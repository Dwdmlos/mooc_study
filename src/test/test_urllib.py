# -*- coding:utf-8 -*-
import urllib.request
from http import cookiejar
url = 'https://www.baidu.com'

print('Method1')
response1 = urllib.request.urlopen(url)
print(response1.getcode())
print(len(response1.read()))

print('method2')
request = urllib.request.Request(url)
request.add_header('user-agent', 'Mozilla/5.0')
response2 = urllib.request.urlopen(request)
print(response2.getcode())
print(len(response2.read()))

print("第三种方法")
cj = cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
response3 = urllib.request.urlopen(url)
print(response3.getcode())
#print(len(response3.read()))
print(cj)#打印cookie
print(response3.read().decode())