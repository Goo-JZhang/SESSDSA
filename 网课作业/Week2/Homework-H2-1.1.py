#change the number of index
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
alist=[random.randint(10000,99999) for p in range(10**8)]
for i in range(0,10**8,5*(10**5)):
    timef=timeit.Timer("alist[{:d}]".format(i),"from __main__ import alist")
    timelist.append(timef.timeit(number=10000000))
result=calcsth(timelist)
print(result[0],result[1])
x=range(0,10**8,5*(10**5))
y=timelist
plt.scatter(x, timelist, s=5,c='b')
plt.ylabel("Time(s)")
plt.xlabel("The length of list")
plt.show()