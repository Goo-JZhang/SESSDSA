def findAnagrams(s, p):
    slist,plist=list(s),list(p)
    plist.sort()
    i,resultlist=0,[]
    while i<len(s)-len(p)+1:
        temp=slist[i:i+len(p)]
        temp.sort()
        if temp==plist:
            resultlist.append(i)
        i=i+1
    if resultlist==[] or len(p)==0:
        print('none')
    else:
        print(' '.join(map(str,resultlist)))
    return resultlist

def topKFrequent(nums, k):
    resultdict={}
    for num in nums:
        resultdict[num]=resultdict.get(num,0)+1
    result=sorted(resultdict.items(),key=lambda d:(-d[1],d[0]))[:k]
    print(' '.join(str(i[0]) for i in result))
    return result

def createHashTable(n):
    p=[2]
    i=3#找素数
    while p[-1]<n:
        j,mayprime=0,True
        while j<len(p) and mayprime:
            if i%p[j]==0:
                mayprime=False
            j=j+1
        if mayprime:
            p.append(i)
        i=i+1
    return [None for q in range(p[-1])]
 
def insertNumbers(table, nums):
    N=len(table)
    i,result=0,[]
    while i<len(nums):
        res=nums[i]%N
        q,Getplace=0,False
        while q<N and not Getplace:
            j=(res+q*q)%N
            if table[j]==None:
                table[j]=nums[i]
                Getplace=True
                result.append(str(j))
            else:
                if table[j]==nums[i]:
                    result.append(str(j))
                    Getplace=True
            q=q+1
        if not Getplace:
            result.append('-')
        i=i+1
    print(' '.join(result))
    return result

n = int(input())
nums = list(map(int, input().split()))
table = createHashTable(n)
insertNumbers(table, nums)