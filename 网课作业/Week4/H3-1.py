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
mylist=[0,3]
print(mylist[2:3:3])