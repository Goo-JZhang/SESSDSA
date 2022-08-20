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
p=0
for i in range(5*(10**5)):
    adict[i]=random.randint(1000,9999)
for i in range(10**6,10**8,5*(10**5)):
    for j in range(i-5*(10**5),i):
        adict[j]=random.randint(1000,9999)
    timef=timeit.Timer("p=adict[0]","from __main__ import adict")
    timelist.append(timef.timeit(number=10000000))
result=calcsth(timelist)
print(result[0],result[1])
x=range(10**6,10**8,5*(10**5))
y=timelist
plt.scatter(x, timelist, s=5,c='b')
plt.ylabel("Time(s)")
plt.xlabel("The length of dict")
plt.show()