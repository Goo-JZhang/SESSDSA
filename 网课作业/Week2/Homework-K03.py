#K03实验1-insert()
import random
import timeit
alist=[random.randint(1000,9999) for i in range(10**5)]
timelist=[]
for i in range(10**5,10**6+1,10**5):
    alist=[random.randint(1000,9999) for i in range(i)]
    testlist=alist
    timef1=timeit.Timer("testlist.insert(0,2333)","from __main__ import testlist")
    timef2=timeit.Timer("testlist.append(2333)","from __main__ import testlist")
    print(timef1.timeit(number=1000),timef2.timeit(number=1000))



