def dpWordEdit(original, target, oplist):
    memory={(0,0):[0,[]]}
    n,m=len(original),len(target)
    for i in range(1,n+1):
        memory[(i,0)]=[oplist['delete']*i,[('delete '+original[k]) for k in range(i)]]
    for j in range(1,m+1):
        memory[(0,j)]=[oplist['insert']*i,[('insert '+target[k]) for k in range(j)]]
    def dpWE(i,j):#ori前i位到tgt前j位
        if (i,j) in memory:
            return memory[(i,j)][:]
        else:
            delete=dpWE(i-1,j)
            delete[0],delete[1]=delete[0]+oplist['delete'],delete[1]+['delete '+original[i-1]]
            insert=dpWE(i,j-1)
            insert[0],insert[1]=insert[0]+oplist['insert'],insert[1]+['insert '+target[j-1]]
            copy=dpWE(i-1,j-1)
            copy[0],copy[1]=copy[0]+oplist['copy'],copy[1]+['copy '+original[i-1]]
            if original[i-1]==target[j-1]:
                memory[(i,j)]=min(copy,delete,insert,key=lambda x:x[0])
            else:
                memory[(i,j)]=min(delete,insert,key=lambda x:x[0])
            return memory[(i,j)][:]
    dpWE(n,m)
    return memory[(n,m)][0],memory[(n,m)][1]

# 检验
print("========= 2 单词最小编辑距离问题 =========")
oplist = {'copy': 5, 'delete': 20, 'insert': 20}
originalWords = [
    "cane", "sheep", "algorithm", "debug", "difficult", "directory",
    "wonderful"
]
targetWords = [
    "new", "sleep", "alligator", "release", "sniffing", "framework", "terrific"
]
for i in range(len(originalWords)):
    score, operations = dpWordEdit(originalWords[i], targetWords[i], oplist)
    print(score)
    print(operations)