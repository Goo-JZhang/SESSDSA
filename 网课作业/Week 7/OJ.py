def findMain(alist):
    n=len(alist)
    num=0
    resultlist=[]
    for i in range(n):
        count=0
        found=True
        while count<i and found:
            if int(alist[i])<int(alist[count]):
                found=False
            count=count+1
        count=count+1
        while count<n and found:
            if int(alist[i])>int(alist[count]):
                found=False
            count=count+1
        if found:
            num=num+1
            resultlist.append(alist[i])
    return num,resultlist

def firstBadVersion(n):
    first=1
    last=n
    while last-first>1:
        mid=(last+first)//2
        if isBadVersion(mid):
            last=mid
        else:
            first=mid
    if isBadVersion(first):
        return first
    else:
        return last

def MergeSort(blist):
    alist=blist[:]
    def MS(alist,step):
        #进啥回啥
        if len(alist)<=step:
            return alist
        #比较
        elif len(alist)<=2*step:
            resultlist=[]
            i,j=0,step
            while i<step and j<len(alist):
                if alist[j]<alist[i]:
                    resultlist.append(alist[j])
                    j=j+1
                else:
                    resultlist.append(alist[i])
                    i=i+1
            if i==step:
                resultlist=resultlist+alist[j:]
            else:
                resultlist=resultlist+alist[i:step]
            return resultlist
        else:
            return MS(alist[:2*step],step)+MS(alist[2*step:],step)
    i=1
    resultlist=[alist]
    while i<len(alist):
        alist=MS(alist,i)
        i=2*i
        resultlist.append(alist)
    return resultlist

def InsertSort(blist):
    alist=blist[:]
    def IS(blist,index):
        alist=blist[:]
        if len(alist)<2:
            return alist
        else:
            if alist[index]<alist[index-1]:
                target=alist.pop(index)
                for i in range(index):
                    if alist[i]>target:
                        alist.insert(i,target)
                        break
        return alist
    i=1
    resultlist=[alist]
    while i<len(blist):
        alist=IS(alist,i)
        resultlist.append(alist)
        i=i+1
    return resultlist

def op(alist):
    if alist==[]:
        return ''
    else:
        result=str(alist[0])
        for i in range(1,len(alist)):
            result=result+' '+str(alist[i])
        return result
blist=list(map(int,input().split(' ')))
tlist=list(map(int,input().split(' ')))
M=MergeSort(blist)
I=InsertSort(blist)
found=False
iM=0
iI=0
Stype=''
while iM<len(M) and not found:
    if tlist==M[iM]:
        found=True
        Stype='Merge Sort'
    iM=iM+1
while iI<len(I) and not found:
    if tlist==I[iI]:
        found=True
        Stype='Insertion Sort'
    iI=iI+1
print(Stype)
if Stype=='Merge Sort':
    print(op(M[iM]))
else:
    print(op(I[iI]))    