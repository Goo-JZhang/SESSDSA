import timeit
import random
import time
from hashlib import md5
def todict(aNode):#格式转化，输入为None或者TreeNode
    if aNode==None:
        return ""
    else:
        akey,aval=str(aNode.key),str(aNode.val)
        if isinstance(aNode.key,str):
            akey='\''+aNode.key+'\''
        if isinstance(aNode.val,str):
            aval='\''+aNode.val+'\''
        return akey+': '+aval



class TreeNode():
    def __init__(self,key,val=None):
        self.key=key
        self.val=val
        self.hash=hash(key)
        self.height=1
        self.right=None
        self.left=None
        self.parent=None
    def getRight(self):
        return self.right
    def getLeft(self):
        return self.left
    def isRightChild(self):#判断是否是右子树
        if self.parent!=None:
            if self.parent.right==self:
                return True
            else:
                return False
        else:
            return False
    def isLeftChild(self):#判断是否是左子树
        if self.parent!=None:
            if self.parent.left==self:
                return True
            else:
                return False
        else:
            return False
    def hasRight(self):
        if self.right==None:
            return False
        else:
            return True
    def hasLeft(self):
        if self.left==None:
            return False
        else:
            return True
    def hasBothChild(self):
        return self.hasRight() and self.hasLeft()
    def hasNoChild(self):
        return (not self.hasRight()) and (not self.hasLeft())
    def __iter__(self):
        if self!=None:
            if self.hasLeft():
                for node in self.left:
                    yield node
            yield self
            if self.hasRight():
                for node in self.right:
                    yield node
        else:
            return None

class mydict():
    def __init__(self):
        self.root=None
        self.size=0
    def getRoot(self):
        return self.root
    def _updateHeight(self,cNode):
        #由于我们更新节点时只对该节点的母树有影响，所以每次只需更新妈节点的高度
        if cNode==None:#对空点当然不能更新高度
            raise SyntaxError
        else:#树高为max(cNode.right.height+1,cNode.left.height+1),避免None Type has no attribute height,采用分段写法
            if cNode.hasNoChild():
                cNode.height=1
            elif cNode.hasBothChild():
                cNode.height=max(cNode.right.height+1,cNode.left.height+1)
            elif cNode.hasRight():
                cNode.height=cNode.right.height+1
            else:
                cNode.height=cNode.left.height+1
    def _RotateRight(self,cNode):
        #cNode不能为None,cNode是被更新的节点（被实际插入或者删除的）,并且可以右旋,即cNode,cNode.left均不为None
        if cNode.isRightChild():#cNode是右子节点
            cNode.parent.right=cNode.left
        elif cNode.isLeftChild():#cNode是左子节点
            cNode.parent.left=cNode.left
        else:
            self.root=cNode.left
        cNode.left.parent=cNode.parent
        cNode.parent=cNode.left
        cNode.left=cNode.parent.right
        cNode.parent.right=cNode
        if cNode.left==None:
            pass
        else:
            cNode.left.parent=cNode
        self._updateHeight(cNode)
        self._updateHeight(cNode.parent)
    def _RotateLeft(self,cNode):#同理瞎写
        if cNode.isRightChild():
            cNode.parent.right=cNode.right
        elif cNode.isLeftChild():
            cNode.parent.left=cNode.right
        else:
            self.root=cNode.right
        cNode.right.parent=cNode.parent
        cNode.parent=cNode.right
        cNode.right=cNode.parent.left
        cNode.parent.left=cNode
        if cNode.right==None:
            pass
        else:
            cNode.right.parent=cNode
        self._updateHeight(cNode)
        self._updateHeight(cNode.parent)
    def _updateBalance(self,cNode):
        #我们是在AVL树上平衡的，故只需要考虑平衡因子在-2~2的情况
        #cNode为被改变的节点，可以从被put,del的节点往上一直跑到root
        if cNode==None:#结束条件
            return None
        else:
            self._updateHeight(cNode)#子树节点高度和平衡已经做好了，但是母树不一定
            #通常情况，cNode有两个子树
            if cNode.hasBothChild():
                L,R=cNode.left.height,cNode.right.height
                #初始化各树高度
                if L-R>1:#左重
                    LL,LR=0,0
                    if cNode.left.hasLeft():
                        LL=cNode.left.left.height
                    if cNode.left.hasRight():
                        LR=cNode.left.right.height
                    #左子树的左右子树高度，None为0
                    if LL-LR>-1:#左左情况，旋转一次即可
                        self._RotateRight(cNode)
                    else:#这种情况为LL-LR=-1,因为cNode.left已经被处理为平衡树了,即使取LL最小为0,也有LR=1,cNode.left.right不是None
                        #cNode.left.right子树和cNode.left.left相对高度只能为(0,0)和(0,-1)，保证旋转后是AVL
                        self._RotateLeft(cNode.left)
                        self._RotateRight(cNode)
                elif L-R<-1:#右重
                    RR,RL=0,0
                    if cNode.right.hasRight():
                        RR=cNode.right.right.height
                    if cNode.right.hasLeft():
                        RL=cNode.right.left.height
                    if RR-RL>-1:
                        self._RotateLeft(cNode)
                    else:
                        self._RotateRight(cNode.right)
                        self._RotateLeft(cNode)
            else:
                if cNode.hasLeft():#只有左子树
                    if cNode.left.height>1:
                        if cNode.left.hasRight():
                            self._RotateLeft(cNode.left)
                            self._RotateRight(cNode)
                        else:
                            self._RotateRight(cNode)
                elif cNode.hasRight():#只有右子树
                    if cNode.right.height>1:
                        if cNode.right.hasLeft():
                            self._RotateRight(cNode.right)
                            self._RotateLeft(cNode)
                        else:
                            self._RotateLeft(cNode)
                else:#无子树，爬
                    pass
        self._updateBalance(cNode.parent)#对于旋转过的树，其实要上升两次才会有操作
    def _put(self,key,val,cNode):
        if hash(key)<cNode.hash:
            if cNode.hasLeft():
                return self._put(key,val,cNode.left)
            else:
                cNode.left=TreeNode(key,val)
                cNode.left.parent=cNode
                self.size=self.size+1
                return cNode
        elif hash(key)>cNode.hash:
            if cNode.hasRight():
                return self._put(key,val,cNode.right)
            else:
                cNode.right=TreeNode(key,val)
                cNode.right.parent=cNode
                self.size=self.size+1
                return cNode
        else:#散列冲突
            if cNode.hasRight():#如果有右子树
                if cNode.right.hash==hash(key):#右子树的根节点也有散列冲突
                    return self._put(key,val,cNode.right)
                else:
                    if cNode.hasLeft():#无论左子节点是否有散列冲突，都要在左子树找
                            return self._put(key,val,cNode.left)
                    else:
                        cNode.left=TreeNode(key,val)
                        cNode.left.parent=cNode
                        self.size=self.size+1
                        return cNode
            else:
                cNode.right=TreeNode(key,val)
                cNode.right.parent=cNode
                self.size=self.size+1
                return cNode
    def put(self,key,val):
        if self.root==None:
            self.root=TreeNode(key,val)
            self.size=1
        else:
            findNode=self._get(key,self.root)#散列冲突情况下查找方式和put里的方式不一样的
            if findNode!=None:#如果找到了，直接替换值
                findNode.val=val
            else:#如果没找到，就按_put的查找方式找一个地方放节点
                cNode=self._put(key,val,self.root)
                self._updateHeight(cNode)
                self._updateBalance(cNode.parent)
    def __setitem__(self,key,val):
        self.put(key,val)
    def _get(self,key,cNode):
        if cNode==None:
            return None
        else:
            if hash(key)<cNode.hash:
                return self._get(key,cNode.left)
            elif hash(key)>cNode.hash:
                return self._get(key,cNode.right)
            else:
                if key==cNode.key:
                    return cNode
                else:
                    leftfind=self._get(key,cNode.left)
                    rightfind=self._get(key,cNode.right)
                    if leftfind!=None:
                        return leftfind
                    else:
                        return rightfind#如果是空那就还是空
    def get(self,key):
        aNode=self._get(key,self.root)
        if aNode!=None:
            return aNode.val
        else:
            raise KeyError("你键爆了")
    def __getitem__(self,key):
        return self.get(key)
    def _find(self,key,cNode):
        if cNode==None:
            return False
        else:
            if hash(key)<cNode.hash:
                return self._find(key,cNode.left)
            elif hash(key)>cNode.hash:
                return self._find(key,cNode.right)
            else:
                if key==cNode.key:
                    return True
                else:
                    return self._find(key,cNode.right) or self._find(key,cNode.left)#往两边找散列冲突
    def find(self,key):
        return self._find(key,self.root)
    def __contains__(self,key):
        return self.find(key)
    def __len__(self):
        return self.size
    def clear(self):
        self.root=None
        self.size=0
    def _findMin(self,cNode):#向右找继承者
        if cNode.hasRight():
            return self._findMin(cNode.right)
        else:
            return cNode
    def _findSuccessor(self,cNode):
        return self._findMin(cNode.left)
    def delete(self,key):
        aNode=self._get(key,self.root)
        if aNode==None:
            raise KeyError("你键爆了")
        else:
            if aNode.hasNoChild():
                if aNode.isLeftChild():
                    aNode.parent.left=None
                    self.size=self.size-1
                    self._updateBalance(aNode.parent)
                elif aNode.isRightChild():
                    aNode.parent.right=None
                    self.size=self.size-1
                    self._updateBalance(aNode.parent)
                else:#就是孤立根节点
                    self.root=None
                    self.size=0
            elif aNode.hasLeft():#有左子树，不如暴力直接找继承者
                target=self._findSuccessor(aNode)
                if target.parent==aNode:#继承者就是妈节点   
                    aNode.key,aNode.hash,aNode.val=target.key,target.hash,target.val
                    aNode.left=target.left
                    if target.left!=None:
                        target.left.parent=aNode
                else:
                    aNode.key,aNode.hash,aNode.val=target.key,target.hash,target.val
                    target.parent.right=target.left
                    if target.left!=None:
                        target.left.parent=target.parent
                self.size=self.size-1
                self._updateBalance(target.parent)
            else:#只有右子树
                if aNode.parent==None:#为根节点
                    self.root=aNode.right
                    self.size=self.size-1
                    aNode.right.parent=None#不需要平衡
                else:
                    if aNode.isLeftChild():
                        aNode.parent.left=aNode.right
                        aNode.right.parent=aNode.parent
                    else:
                        aNode.parent.right=aNode.right
                        aNode.right.parent=aNode.parent
                    self.size=self.size-1
                    self._updateBalance(aNode.parent)
    def __delitem__(self,key):
        self.delete(key)
    def _keys(self,cNode):
        if cNode==None:
            return []
        else:
            return self._keys(cNode.left)+[cNode.key]+self._keys(cNode.right)
    def _values(self,cNode):
        if cNode==None:
            return []
        else:
            return self._values(cNode.left)+[cNode.val]+self._values(cNode.right)
    def keys(self):
        return self._keys(self.root)
    def values(self):
        return self._values(self.root)

    def __iter__(self):
        for node in self.root:
            yield node.key
    def __str__(self):
        s=""
        Head=True
        if self.root!=None:#如果在头部的话前面没有逗号和空格
            for Node in self.root:
                if Node!=None:
                    if Head:
                        s+=todict(Node)
                        Head=False
                    else:
                        s+=", "+todict(Node)
        return "{"+s+"}"
    __repr__ = __str__

md={'6': '6', '8': 3, 4.0: 3, 5: '6', 9: 3, '1': 4.0}
print(type(4.0)==type(4))