class BinaryTree():
    def __init__(self,item=None):
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
    def insertRight(self,rightree):
        if self.right==None:
            self.right=BinaryTree(rightree)
            self.right.father=self
        else:
            t=BinaryTree(rightree)
            t.father=self
            t.right=self.right
            self.right=t
            t.right.father=t
    def insertLeft(self,leftree):
        if self.left==None:
            self.left=BinaryTree(leftree)
            self.left.father=self
        else:
            t=BinaryTree(leftree)
            t.father=self
            t.left=self.left
            self.left=t
            t.left.father=t
    def ListType(self):
        left=self.left.ListType() if self.left!=None else []
        right=self.right.ListType() if self.right!=None else []
        return [self.val,left,right]
    def __str__(self):
        return str(self.ListType())
    def height(self):
        def find(root,n=0):
            if root==None:
                return [n]
            else:
                return find(root.left,n+1)+find(root.right,n+1)
        return max(find(self))

def buildTree():
    atree=BinaryTree('a')
    atree.insertLeft('b')
    atree.getLeft().insertRight('d')
    atree.insertRight('c')
    atree.getRight().insertLeft('e')
    atree.getRight().insertRight('f')
    return atree
print(buildTree())
print(buildTree().height())
print(BinaryTree().height())

