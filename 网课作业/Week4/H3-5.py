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

class DoublyLinkedList():
    def __init__(self,it=None):
        self.head=None
        self.rear=None
        self.length=0
        if it!=None:
            for d in it:
                self.append(d)
    def isEmpty(self):
        return self.head==None
    def add(self,item):#这里add在头上
        #空集加元素时加在头部
        if self.head==None:
            self.head=Node(item)
        #两个元素时，创建尾巴
        elif self.rear==None:
            temp=Node(item)
            self.rear=self.head
            self.head=temp
            self.head.setNext(self.rear)
            self.rear.setPrev(self.head)
        else:#放头部
            temp=Node(item)
            temp.setNext(self.head)
            self.head.setPrev(temp)
            self.head=temp
        self.length=self.length+1
    def search(self,item):
        current=self.head
        while current!=None:#找到空为止
            if current.getData()==item:
                return True
            current=current.getNext()
        return False
    def size(self):
        return self.length
    __len__=size
    def append(self,item):
        #空集加元素时加在头部
        if self.head==None:
            self.head=Node(item)
        #两个元素时，创建尾巴
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
    def remove(self,item):
        current=self.head
        previous=None
        found=False
        while not found:
            if current.getData()==item:
                found=True
            else:
                previous=current
                current=current.getNext()
        if found==False:
            return "Not Found"
        elif previous!=None:
            previous.setNext(current.getNext())
            self.length=self.length-1
        else:
            self.head=current.getNext()
            self.head.setPrev(None) 
            self.length=self.length-1 
    def index(self,item):
        current=self.head
        count=0
        found=False
        while not found:
            if current.getData()==item:
                return count
            else:
                current=current.getNext()
                count=count+1
        if found==False:
            return None
    def pop(self,num=-1):
        if num==-1 or num==self.length-1:
            temp=self.rear.getData()
            self.rear=self.rear.getPrev()
            self.rear.setNext(None)
            self.length=self.length-1
            return temp
        elif num==0:
            temp=self.head.getData()
            self.head=self.head.getNext()
            self.head.setPrev(None)
            self.length=self.length-1
            return temp
        elif num>0 and num < self.length-1:
            current=self.head
            previous=None
            for i in range(num):
                previous=current
                current=current.getNext()
            temp=current.getData()
            previous.setNext(current.getNext())
            self.length=self.length-1
            return temp
        else:
            return None
    def insert(self,num,item):
        if num==0:
            self.add(item)
        elif num>=self.length:
            self.append(item)
        else:
            current=self.head
            previous=None
            for i in range(num):
                previous=current
                current=current.getNext()
            temp=Node(item)
            temp.setNext(current)
            temp.setPrev(previous)
            current.setPrev(temp)
            previous.setNext(temp)
        self.length=self.length+1
    def delete(self,current):
        if current==self.head:
            self.head=self.head.getNext()
            self.head.setPrev(None)
        elif current.self.rear:
            self.rear=self.rear.getPrev()
            self.rear.setNext(None)
        else:
            tempN=current.getNext()
            tempP=current.getPrev()
            tempN.setPrev(tempP)
            tempP.setNext(tempN)
    def getTail(self):
        if self.length==1:
            return self.head
        else:
            return self.rear
    def getHead(self):
        return self.head
    def __getitem__(self,num):
        if isinstance(num,int):
            current=self.head
            for i in range(num):
                current=current.getNext()
            if current!=None:
                return current.getData()
            else:
                raise StopIteration
        elif isinstance(num,slice):
            start=0 if num.start==None else num.start
            step=1 if num.step==None else num.step
            stop=self.length if num.stop==None else num.stop
            #
            if start<0:
                start=start+self.length
            if stop<0:
                stop=stop+self.length
            #找交集
            start_eq=start
            stop_eq=stop
            if start_eq<stop_eq:
                #没有交集就变成0
                if (start<0 and stop<0) or (start>self.length and stop>self.length):
                    start=0
                    stop=0
                #有交集就取交集
                else:
                    if stop>self.length:
                        stop=self.length
                    if start<0:
                        start=0
            if start_eq>stop_eq:
                if (start<0 and stop<0) or (start>self.length and stop>self.length):
                    start=0
                    stop=0
                #有交集就取交集
                else:
                    if stop<0:
                        stop=-1
                    if start>self.length-1:
                        start=self.length-1
            print(start,stop)
            copylink=DoublyLinkedList()
            current=self.head
            for i in range(start):
                current=current.getNext()
            for i in range(start,stop,step):
                copylink.append(current.getData())
                if step>0:
                    for p in range(step):
                        if current==None:
                            break
                        current=current.getNext()
                else:
                    for p in range(-step):
                        if current==None:
                            break
                        current=current.getPrev()
            return copylink
    def __str__(self):
        alist=[]
        current=self.head
        while current!=None:
            alist.append(current.getData())
            current=current.getNext()
        return str(alist)
    __repr__=__str__
    def __eq__(self,other):
        if other==None or not isinstance(other,DoublyLinkedList()):
            return False
        if self.size()!=other.size():
            return False
        current1=self.head
        current2=other.getHead()
        flag=True
        for i in range(self.length):
            if current1.getData()==current2.getData() and flag:
                current1=current2.getNext()
                current2=current2.getNext()
            else:
                flag=False
                break
        return flag
    class Aiter():
        def __init__(self,my):
            self.base=my
            self.count=-1
        def __next__(self):
            if self.count<self.base.size()-1:
                self.count=self.count+1
                return self.base[self.count]
            else:
                raise StopIteration
    def __iter__(self):
        return self.Aiter(self)

# 检验
print("======== 5-DoublyLinkedList ========")
mylist = DoublyLinkedList()
for i in range(0, 20, 2):
    mylist.append(i)
mylist.add(3)
mylist.remove(6)
print(mylist)
print(mylist.getTail().getPrev().getData())  # 16
print(mylist.isEmpty())  # False
print(mylist.search(5))  # False
print(mylist.size())  # 10
print(mylist.index(2))  # 2
print(mylist.pop())  # 18
print(mylist.pop(2))  # 2
print(mylist)  # [3, 0, 4, 8, 10, 12, 14, 16]
mylist.insert(3, "10")
print(len(mylist))  # 9
print(mylist[4])  # 8
print(mylist[-3:1:2])  # ['10', 10, 14]
p=DoublyLinkedList(range(50))
k=[i for i in range(50)]
print("p:",p)
print("k:",k)
print("p_slice:",p[-60:95:5])
print("k_slice:",k[-60:95:5])


    
    
