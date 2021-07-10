import requests
from bs4 import BeautifulSoup

r=requests.get('https://www.zjut.cc/article-320676-1.html')
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
# 遍历网页列表并写入文件
with open('川农生源地来源.txt','w',encoding='utf-8') as f:
    f.write('NAME'+', '+'四川农业大学'+'\n')
    for i in range(0,31):
        try:
            rr = requests.get(urls[i])
            tt = rr.text
            rr.encoding = rr.apparent_encoding
            ss = BeautifulSoup(tt, features="html.parser")

            lsl = ss.findAll('tbody')
            name=ls2[i].string
            for tb in lsl:
                lsls = tb.findAll('td')

                n = 0
                j = 0
                a = 1
                while j <= len(lsls) - 8:
                    j = 15 + (a - 1) * 8
                    a = a + 1
                    try:
                        n = n + eval(lsls[j].string)
                    except TypeError:
                        continue
                f.write(ls2[i].string[6:]+', '+str(n)+'\n')


                c=c+1
                print('已写入{}条'.format(c))
        except SyntaxError:
            print('出错省份是{},在网页第{}页'.format(ls2[i].string[6:],c+1))
            continue
print('完成爬取，共{}条'.format(c))