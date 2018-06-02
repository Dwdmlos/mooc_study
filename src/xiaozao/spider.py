# -*- coding: utf-8 -*-
import urllib.request, urllib.parse
from bs4 import BeautifulSoup
import re

page_urls = ['https://www.xiaozao.org/job/internship?inside=0&pn='+str(num) for num in range(1, 16)]
job_urls = set()
result_url = dict()

def output_html(datas):
        fout = open('output1.html', 'w', encoding = 'utf-8')
        
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')#加入表格标签
        for k, v in datas.items():
            fout.write('<tr>')#行的开始标签
            fout.write('<td>%s</td>'%k)#单元格的标签
            fout.write('<td>%s</td>'%v)
            fout.write('</tr>')
            
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        fout.close()


for web in page_urls:
    connection = urllib.request.urlopen(web)
    html = connection.read().decode()
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a', href = re.compile(r'/job/[0-9]+'))
    for link in links:
        new_url = link['href']
        new_full_url=urllib.parse.urljoin('https://www.xiaozao.org/job/46171',new_url)
        job_urls.add(new_full_url)
        
for url in job_urls:
    connection = urllib.request.urlopen(url)
    html = connection.read().decode()
    soup = BeautifulSoup(html, 'html.parser')
    jd = soup.find('p').get_text()
    if '应届生' in jd or '应届毕业生' in jd or '18届' in jd:
        result_url[url] = '\n' + soup.find('h2').get_text() +'============================='+ jd +'\n'

output_html(result_url)
        
    
    
    
