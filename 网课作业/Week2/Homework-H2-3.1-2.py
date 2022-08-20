#change key
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
def testfunc(testdict,r,v):
    del testdict[r]
    testdict[r]=v
for i in range(10**7):
    adict[i]=random.randint(1000,9999)
for i in range(200):
    v=random.randint(1000,9999)
    r=random.randint(0,1)
    timef=timeit.Timer("testfunc(adict,r,v)","from __main__ import adict,testfunc,r,v")
    zero=timeit.Timer("adict[r]=v","from __main__ import testfunc,adict,v,r")
    timelist.append(timef.timeit(number=2000000)-zero.timeit(number=2000000))
x=range(200)
result=calcsth(timelist)
print(result[0],result[1])
y=timelist
plt.scatter(x, timelist, s=5,c='b')
plt.ylabel("Time(s)")
plt.xlabel("The length of dict")
plt.show()