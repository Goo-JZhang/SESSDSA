#定义类和方法
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
            i=i/10
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
#print(radix_sort(eval(input())))