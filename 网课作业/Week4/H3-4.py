class Node():
    def __init__(self, initdata=None):
        self.data = initdata
        self.next = None
        self.prev = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def getPrev(self):
        return self.prev
    def setData(self, newdata):
        self.data = newdata
    def setNext(self, newnext):
        self.next = newnext
    def setPrev(self, newprev):
        self.prev = newprev

class LinkStack():
    def __init__(self):
        self.head=None
        self.length=0
    def isEmpty(self):
        return self.head==None
    def size(self):
        return self.length
    def push(self,item):
        if self.head==None:#没有就创建
            self.head=Node(item)
        else:
            temp=Node(item)
            temp.setNext(self.head)
            self.head=temp
        self.length=self.length+1
    def peek(self):
        return self.head.getData()
    def pop(self):
        temp=self.head.getData()
        self.head=self.head.getNext()
        self.length=self.length-1
        return temp

class LinkQueue():
    def __init__(self):
        self.head=None
        self.rear=None
        self.length=0
    def size(self):
        return self.length
    def isEmpty(self):
        return self.head==None
    def enqueue(self,item):
        #空集加元素时加在头部
        if self.head==None:
            self.head=Node(item)
        #两个元素时，创建尾巴，避免enqueue时要从头遍历一遍
        elif self.rear==None:
            self.rear=Node(item)
            self.head.setNext(self.rear)
            self.rear.setPrev(self.head)
        else:#接尾巴
            temp=Node(item)
            temp.setPrev(self.rear)
            self.rear.setNext(temp)
            self.rear=temp
        self.length=self.length+1
    def dequeue(self):
        if self.length==0:
            return None
        else:
            head=self.head.getData()
            if self.length==1:
                self.head=None 
            elif self.length==2:
                self.head=self.rear
                self.head.setPrev(None)
                self.rear=None
            else:
                self.head=self.head.getNext()
                self.head.setPrev(None)
            self.length=self.length-1
            return head



# 检验
print("======== 4-Link Stack & Link Queue ========")
q = LinkQueue()
q.enqueue(13)
print(q.isEmpty())
q.enqueue(0)
print(q.size())
print(q.dequeue())
print(q.isEmpty())
q.enqueue(15)
print(q.size())
print(q.dequeue())
print(q.isEmpty())
print(q.dequeue())
print(q.isEmpty())
q.enqueue(18)
print(q.size())
print(q.enqueue(15))
print(q.isEmpty())
q.enqueue(7)
print(q.size())
q.enqueue(18)
print(q.size())
q.enqueue(10)
print(q.isEmpty())



import matplotlib.pyplot as plt
from numpy import *
x=linspace(-2,2)   #设置自变量的取值范围为[-2,2]，
y1=2*x+1
y2=x**2
 
plt.figure()      #声明第一张图片
plt.plot(x,y1)    #制图
 
plt.figure()  #声明第二张图片
plt.plot(x,y2,color='red',linestyle='--') #设置函数线的颜色和线的样式
 
plt.show()    #显示上面所绘制的所有图片