class Node():
    def __init__(self,val):
        self.val=val
        self.parent=None
        self.right=None
        self.left=None
        self.searched="No"

class BT():
    def __init__(self):
        self.root=None
    def _put(self,val,cNode):
        if val<cNode.val:
            if cNode.left==None:
                cNode.left=Node(val)
                cNode.left.parent=cNode
            else:
                self._put(val,cNode.left)
        else:
            if cNode.right==None:
                cNode.right=Node(val)
                cNode.right.parent=cNode
            else:
                self._put(val,cNode.right)
    def put(self,val):
        if self.root==None:
            self.root=Node(val)
        else:
            self._put(val,self.root)

resultList=[]

def findRoute(aNode,nowRoute):#保证aNode!=None
    global resultList
    if aNode!=None:
        nowRoute+=str(aNode.val)
        if aNode.left==None and aNode.right==None:
            resultList.append(nowRoute)
        else:
            nowRoute+='->'
            findRoute(aNode.left,nowRoute)
            findRoute(aNode.right,nowRoute)

aTree=BT()
inList=list(map(int,input().split()))
for i in inList:
    aTree.put(i)

findRoute(aTree.root,'')
for route in resultList:
    print(route)

'''
HouseList=list(map(int,input().split(' ')))
N=len(HouseList)
Val=[0 for p in range(N+1)]
Val[1]=HouseList[0]
for i in range(2,N+1):
    Val[i]=max(Val[i-2]+HouseList[i-1],Val[i-1])
print(Val[-1])
'''