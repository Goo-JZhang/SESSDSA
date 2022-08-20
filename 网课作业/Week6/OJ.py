def findWays(expr):
    #做计算
    def doMath(op,op1,op2):
        if op=='*':
            return op1*op2
        elif op=='+':
            return op1+op2
        elif op=='-':
            return op1-op2
        else:
            print("说好的只有*+-呢QAQ,这明明是",op)
    #做搜索
    def gongjuren(numlist,oplist):
        if len(oplist)==0:
            return [numlist[0]]
        else:
            resultlist=[]
            for i in range(len(oplist)):
                rearlist=gongjuren(numlist[i+1:],oplist[i+1:])#选位置i的地方切成两份，分别计算结果的可能值
                frontlist=gongjuren(numlist[0:i+1:1],oplist[0:i:1])
                for j in frontlist:
                    for k in rearlist:
                        resultlist.append(doMath(oplist[i],j,k))
            resultlist=list(set(resultlist))
            resultlist.sort()
            return resultlist
# 用于将字符串转为数字与运算符
    nums, ops = [], []
    num = 0
    for c in expr:
        if '0' <= c <= '9':
            num = num * 10 + ord(c) - 48
        else:
            ops.append(c)
            nums.append(num)
            num = 0
    else:
        nums.append(num)
    resultlist=gongjuren(nums,ops)
    result=''
    for i in range(len(resultlist)-1):
        result=result+str(resultlist[i])+','
    result=result+str(resultlist[-1])
    return result
 
expr=input()
print(findWays(expr))