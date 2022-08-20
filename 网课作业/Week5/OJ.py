def Splist(dim,astr):
    if dim==1:
        resultlist=[[astr,astr,astr],[astr,' '*len(astr),astr],[astr,astr,astr]]
        return resultlist
    else:
        templist=Splist(dim-1,astr)
        newlist=[]
        for i in range(3**(dim-1)):
            newlist.append(templist[i]+templist[i]+templist[i])
        Nonelist=[]
        for i in range(3**(dim-1)):
            Nonelist.append(' '*len(astr))
        for i in range(3**(dim-1)):
            newlist.append(templist[i]+Nonelist+templist[i])
        for i in range(3**(dim-1)):
            newlist.append(templist[i]+templist[i]+templist[i])
        return newlist
def draw(alist):
    for i in range(len(alist)):
        for j in range(len(alist)):
            print(alist[i][j],end='')
        print('')
N=int(input())
astr=input()
dim=-1
while N!=0:
    dim=dim+1
    N=N//3
drawlist=Splist(dim,astr)
draw(drawlist)
        
        

