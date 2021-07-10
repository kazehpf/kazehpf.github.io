d={}
with open('E:\\桌面\\成理文2.txt','w',encoding='utf-8') as f1:
    with open('E:\\桌面\\成理文.txt','r',encoding='utf-8') as f2:
        ls=f2.readlines()
        for s in ls:
            ls1=s.split()
            if ls1[0]=='年份':
                continue
            else:
                d[ls1[1]]=d.get(ls1[1],0)+eval(ls1[-1])
    for i in d:
        f1.write(i+':'+str(d[i])+'\n')



