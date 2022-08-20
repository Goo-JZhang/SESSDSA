class Stack(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
class Queue(object):
    def __init__(self):
        self.items=[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def is_Empty(self):
        return self.items==[]
    def size(self):
        return len(self.items)
    def dequeue(self):
        return self.items.pop()
class Node(object):
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
def calculate(astring):
    #一个计算函数
    def doMath(op,op1,op2):
        if op=='+':
            return op1+op2
        elif op=='-':
            return op1-op2
        elif op=='*':
            return op1*op2
        elif op=='/':
            return op1/op2
        elif op=='^':
            return op1**op2
    #一个优先级字典
    priority={'+':0,'-':0,'*':1,'/':1,'^':2,'(':-1}
    midlist=astring.split(' ')#一个挖掉空格的列表
    opStak=Stack()#操作栈
    numStak=Stack()#数栈
    for i in midlist:
        #考虑有括号的情况
        if i=='(':
            opStak.push(i)
        elif i==')':
            while opStak.peek()!='(':
                op2=float(numStak.pop())
                op1=float(numStak.pop())
                op=opStak.pop()
                numStak.push(doMath(op,op1,op2))
            opStak.pop()
        #操作符入栈
        elif i in "+-*/^":
            if opStak.isEmpty():
                opStak.push(i)
            #根据优先级计算
            else: 
                #防止空栈peek报错，同时在i入栈前处理掉前面的高级和同级运算
                while not opStak.isEmpty() and priority[i]<=priority[opStak.peek()]:
                    op2=float(numStak.pop())
                    op1=float(numStak.pop())
                    op=opStak.pop()
                    numStak.push(doMath(op,op1,op2))
                opStak.push(i)
        #操作数入栈
        else:
            numStak.push(i)
    #剩下的东西继续算
    while not opStak.isEmpty():
        op2=float(numStak.pop())
        op1=float(numStak.pop())
        op=opStak.pop()
        numStak.push(doMath(op,op1,op2))
    return float(numStak.pop())
#print(calculate(input()))
def radix_sort(mylist):
    maxcount=1
    output=mylist
    Qm=Queue()
    Qbasic=[]
    #获得一个队列列表比较方便
    for i in range(10):
        Qbasic.append(Queue())
    #获得最高位位数
    for i in mylist:
        count=1
        while i!=0:
            i=i//10
            count=count+1
        if maxcount<count:
            maxcount=count
    #开始排序
    for i in range(maxcount):
        for p in output:
            Qbasic[(p//(10**i))%10].enqueue(p)
        for j in range(10):
            while not Qbasic[j].is_Empty():
                Qm.enqueue(Qbasic[j].dequeue())
        for p in range(len(mylist)):
            output[p]=Qm.dequeue()
    return output
def HTMLMatch(astring):
    #获得tag
    def get_tag(astring):
        alist=[]
        temp=''
        rangle=0
        for i in astring:
            #找到<
            if i=='<':
                rangle=True
            if rangle and i not in "<>":
                temp=temp+i
            if i=='>':
                alist.append(temp)
                temp=''
                rangle=False
        return alist
    mStak=Stack()
    taglist=get_tag(astring)
    #开始匹配
    for i in taglist:
        if mStak.isEmpty():
            mStak.push(i)
        elif i=='/'+mStak.peek():#xxx和/xxx匹配
            mStak.pop()
        else:
            mStak.push(i)
    return mStak.isEmpty()
#print(HTMLMatch(input()))
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
            #把切片的start和stop换成从0开始数的序号，然后取和0，1,...,self.length的交集
            #先变成从0计数的序号
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
        if other==None or not isinstance(other,DoublyLinkedList):
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
    def __iter__(self):
        self.current=self.head
        return self
    def __next__(self):
        if self.current==None:
            raise StopIteration
        else:
            temp=self.current
            self.current=self.current.getNext()
            return temp.getData()
