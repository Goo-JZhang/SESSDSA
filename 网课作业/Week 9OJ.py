class BinaryTree():
    def __init__(self,item):
        self.val=item
        self.right=None
        self.left=None
        self.father=None
    def getRight(self):
        return self.right
    def getLeft(self):
        return self.left
    def getVal(self):
        return self.val
    def getFather(self):
        return self.father
    def setVal(self,item=None):
        self.val=item
    def setRight(self,rightree):
        self.right=rightree
        if rightree!=None:
            rightree.father=self
    def setLeft(self,leftree):
        self.left=leftree
        if leftree!=None:
            leftree.father=self

def seq2tree(seq):
    if len(seq)==0 or seq[0]==None:
        return None
    else:
        root=BinaryTree(seq[0])
        exi=[[root]]
        i,n=1,1#i,i,n are separatedly order and exi
        while i<len(seq):
            j=0
            lay=[]
            while j<2*len(exi[n-1]):
                if i>=len(seq):
                    return root
                elif seq[i]==None:
                    pass
                elif j%2==0:
                    exi[n-1][j//2].setLeft(BinaryTree(seq[i]))
                    lay.append(exi[n-1][j//2].getLeft())
                else:
                    exi[n-1][j//2].setRight(BinaryTree(seq[i]))
                    lay.append(exi[n-1][j//2].getRight())
                i=i+1
                j=j+1
            exi.append(lay)
            n=n+1
        return root
            
 
def inorderTree(root):
    if root==None:
        return []
    else:
        return inorderTree(root.getLeft())+[root.getVal()]+inorderTree(root.getRight())

def fanzhuan(root):
    if root==None:
        pass
    else:
        l=fanzhuan(root.getLeft())
        r=fanzhuan(root.getRight())
        root.setRight(l)
        root.setLeft(r)
    return root

def postTree(alist):
    if alist==[]:
        return []
    else:
        i,t=1,[]
        while i<len(alist):
            t=t+postTree(alist[i])
            i=i+1
        t=t+[alist[0]]
        return t

