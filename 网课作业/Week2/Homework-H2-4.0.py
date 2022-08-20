import random
import timeit
import numpy as np
import matplotlib.pyplot as plt
import copy
from scipy.optimize import curve_fit
def testfunc(testlist,model_list):
    testlist.sort()
    testlist=model_list.copy()
def calcsth(x_list,datalist):
    avr_d=sum(datalist)/len(datalist)
    sqr_d=np.sqrt(sum([(i-avr_d)**2 for i in datalist])/len(datalist))
    avr_x=sum(x_list)/len(x_list)
    sqr_x=np.sqrt(sum([(i-avr_x)**2 for i in x_list])/len(x_list))
    avr_xd=sum((x_list[i]*datalist[i]-avr_d*avr_x) for i in range(len(datalist)))/len(datalist)
    return [avr_d,sqr_d,avr_x,sqr_x,avr_xd]
timelist=[]
for i in range(10**3,10**5,5*(10**2)):
    print(i/10**5)
    alist=[random.randint(10000,99999) for p in range(i)]
    mlist=alist.copy()
    timef=timeit.Timer("testfunc(alist,mlist)","from __main__ import testfunc,alist,mlist")
    zero=timeit.Timer("alist=mlist.copy()","from __main__ import alist,mlist")
    timelist.append(timef.timeit(number=1000)-zero.timeit(number=1000))
x=range(10**3,10**5,5*(10**2))
y=timelist
y_c=[]
x_c=[]
for i in range(198):
    y_c.append(y[i]/x[i])
    x_c.append(np.log(x[i]))
result_o=calcsth(x,y)
b_o=result_o[4]/(result_o[3]**2)
a_o=result_o[0]-result_o[2]*b_o
r_o=result_o[4]/(result_o[1]*result_o[3])
print(b_o,a_o,r_o)
result_c=calcsth(x_c,y_c)
b_c=result_c[4]/(result_c[3]**2)
a_c=result_c[0]-result_c[2]*b_c
r_c=result_c[4]/(result_c[1]*result_c[3])
print(b_c,a_c,r_c)
plt.plot(x,a_c+b_c*np.log(x),'r--')
plt.scatter(x, y_c, s=5,c='b')
#plt.plot(x,a_o+b_o*x,'r--')
#plt.plot(x_c,a_c+b_c*x_c,'r--')
plt.ylabel("Time(s)/len(list)")
plt.xlabel("The length of list")
plt.show()