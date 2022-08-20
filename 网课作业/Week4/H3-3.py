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
