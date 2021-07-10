import requests
from bs4 import BeautifulSoup

r=requests.get('https://www.zjut.cc/article-58477-4.html')
t=r.text
r.encoding=r.apparent_encoding
s=BeautifulSoup(t,features="html.parser")


# 寻找网页
ls1=s.findAll('div',attrs={'class':'container'})
ls2=ls1[1].findAll('p',attrs={'class':'col-sm-6'})
print(ls2)
urls=[]
for i in ls2:
    ur=i.find('a').get('href')
    urls.append(ur)
print(urls)


c=0
#遍历网页列表
for i in range(3,25):
    rr = requests.get(urls[i])
    tt = rr.text
    rr.encoding = rr.apparent_encoding
    ss = BeautifulSoup(tt, features="html.parser")
    lsl = ss.findAll('tbody')

    for tb in lsl:
        lsls = tb.findAll('td')

        n = 0
        i = 0
        a = 1
        while i <= len(lsls) - 9 - 8:
            i = 13 + (a - 1) * 8
            a = a + 1
            try:
                n = n + eval(lsls[i].string)
            except TypeError:
                continue
        print(lsls[9].string, n)

        c=c+1
print(c)