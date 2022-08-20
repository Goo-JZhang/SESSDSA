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
p=0
for i in range(10**7):
    adict[i]=random.randint(1000,9999)
for i in range(200):
    v=random.randint(0,10**7-1)
    timef=timeit.Timer("p=adict[v]","from __main__ import adict,v")
    zero=timeit.Timer("v","from __main__ import v")
    t=timef.timeit(number=10000000)-zero.timeit(number=10000000)
    timelist.append(t)
result=calcsth(timelist)
print(result[0],result[1])
x=range(200)
y=timelist
plt.scatter(x, timelist, s=5,c='b')
plt.ylabel("Time(s)")
plt.xlabel("The length of dict")
plt.show()