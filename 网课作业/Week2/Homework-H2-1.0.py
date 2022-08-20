#change the length of the list
import random
import timeit
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
def calcsth(datalist):
    avr=sum(datalist)/len(datalist)
    sqr=np.sqrt(sum([(i-avr)**2 for i in datalist])/len(datalist))
    return [avr,sqr]
timelist=[]
alist=[random.randint(10000,99999) for i in range(10**6)]
for i in range(10**6,10**8,5*(10**5)):
    for p in range(5*(10**5)):
        alist.append(random.randint(10000,99999))
    timef=timeit.Timer("alist[0]","from __main__ import alist")
    timelist.append(timef.timeit(number=10000000))
result=calcsth(timelist)
print(result[0],result[1])
x=range(10**6,10**8,5*(10**5))
print(len(x))
y=timelist
plt.scatter(x, timelist, s=5,c='b')
plt.ylabel("Time(s)")
plt.xlabel("The length of list")
plt.show()