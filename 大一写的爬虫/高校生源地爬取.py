import requests
from bs4 import BeautifulSoup

r=requests.get('https://www.zjut.cc/article-270519-1.html')
t=r.text
r.encoding=r.apparent_encoding
s=BeautifulSoup(t,features="html.parser")


# 寻找网页
ls1=s.findAll('div',attrs={'class':'container'})
ls2=ls1[1].findAll('p',attrs={'class':'col-sm-6'})

urls=[]
for i in ls2:
    ur=i.find('a').get('href')
    urls.append(ur)


c=0
#遍历网页列表
for url in urls:
    rr = requests.get(url)
    tt = rr.text
    rr.encoding = rr.apparent_encoding
    ss = BeautifulSoup(tt, features="html.parser")

#统计人数
    lsl = ss.findAll('td')
    n = 0
    i = 0
    a = 1
    while i <= len(lsl) - 5:
        i = 2 + (a - 1) * 5
        a = a + 1
        try:
            n = n + eval(lsl[i].string)
        except TypeError:
            continue
    print(lsl[0].string,n)
    c=c+1
print(c)


#
