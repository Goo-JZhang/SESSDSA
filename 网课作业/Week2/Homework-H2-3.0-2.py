#change the length of dict
import random
import timeit
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
def calcsth(datalist):
    avr=sum(datalist)/len(datalist)
    sqr=np.sqrt(sum([(i-avr)**2 for i in datalist])/len(datalist))
    return [avr,sqr]
adict={}
timelist=[]
def testfunc(testdict,v):
    del testdict[0]
    testdict[0]=v
for i in range(10**5):
    adict[i]=random.randint(1000,9999)
for i in range(0,10**7,5*(10**4)):
    for p in range(5*(10**4)):
        adict[p]=random.randint(1000,9999)
    v=random.randint(1000,9999)
    timef=timeit.Timer("testfunc(adict,v)","from __main__ import testfunc,adict,v")
    zero=timeit.Timer("adict[0]=v","from __main__ import adict,v")
    timelist.append(timef.timeit(number=2000000)-zero.timeit(number=2000000))
x=range(0,10**7,5*(10**4))
result=calcsth(timelist)
print(result[0],result[1])
plt.scatter(x, timelist, s=5,c='b')
plt.ylabel("Time(s)")
plt.xlabel("The length of dict")
plt.show()