#change the number of index
import random
import timeit
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
def calcsth(x_list,datalist):
    avr_d=sum(datalist)/len(datalist)
    sqr_d=np.sqrt(sum([(i-avr_d)**2 for i in datalist])/len(datalist))
    avr_x=sum(x_list)/len(x_list)
    sqr_x=np.sqrt(sum([(i-avr_x)**2 for i in x_list])/len(x_list))
    avr_xd=sum((x_list[i]*datalist[i]-avr_d*avr_x) for i in range(len(datalist)))/len(datalist)
    return [avr_d,sqr_d,avr_x,sqr_x,avr_xd]
timelist=[]
alist=[random.randint(1000,9999) for i in range(10**7)]
for i in range(200):
    testlist=alist
    timef=timeit.Timer("del testlist[5*(10**4)*i]","from __main__ import testlist,i")
    timelist.append(timef.timeit(number=100))
x=range(0,10**7,5*(10**4))
y=timelist
plt.scatter(x, timelist, s=5,c='b')
result=calcsth(x,y)
b=result[4]/(result[3]**2)
a=result[0]-result[2]*b
r=result[4]/(result[1]*result[3])
print(b,a,r)
plt.plot(x,a+b*x,'r--')
plt.ylabel("Time(s)")
plt.xlabel("The length of list")
plt.show()