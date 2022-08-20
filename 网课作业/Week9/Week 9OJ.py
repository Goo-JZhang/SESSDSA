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
        rightree.father=self
    def setLeft(self,leftree):
        self.left=leftree
        leftree.father=self
    def inorder(self):
        if self.right==None:
            return [self.val]
        else:
            return inorder(self.left)+[self.father.val]+inorder(self.right)

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
        return inorderTree(root.left)+[root.val]+inorderTree(root.right)

lst = eval(input())
tree = seq2tree(lst)
inorder = inorderTree(tree)
print(*inorder) # 请自行确定打印方式