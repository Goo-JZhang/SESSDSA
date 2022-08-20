def dpWordEdit(original, target, oplist):
    score = 0
    operations = []
    n=len(original)
    m=len(target)
    scoreList=[[[0,[]] for j in range(m+1)] for i in range(n+1)]
    #二维数组初始化，scoreList[i][j]记录original前i位target前j位变成的最小分数和操作步骤
    #注意不能直接scoreList=[[[0,[]]*(m+1)]*(n+1)]，这样的话是copy的地址，改数就炸了
    for i in range(1,n+1):
        scoreList[i][0][0]=i*oplist['delete']
        scoreList[i][0][1]=scoreList[i-1][0][1]+['delete '+original[i-1]]#original前i位到target前0位
    for j in range(1,m+1):
        scoreList[0][j][0]=j*oplist['insert']
        scoreList[0][j][1]=scoreList[0][j-1][1]+['insert '+target[j-1]]#original前0位变成target前j位
    for i in range(1,n+1):
        for j in range(1,m+1):
            substitute=oplist['copy'] if original[i-1]==target[j-1] else oplist['delete']+oplist['insert']
            substitute_score=substitute+scoreList[i-1][j-1][0]
            delete_score=oplist['delete']+scoreList[i-1][j][0]
            insert_score=oplist['insert']+scoreList[i][j-1][0]
            if substitute_score<=delete_score and substitute_score<=insert_score:
                scoreList[i][j][0]=substitute_score
                if original[i-1]==target[j-1]:
                    scoreList[i][j][1]=scoreList[i-1][j-1][1]+['copy'+target[j-1]]
                else:
                    scoreList[i][j][1]=scoreList[i-1][j-1][1]+['delete '+original[i-1]]+['insert '+target[j-1]]
            elif delete_score<=substitute_score and delete_score<=insert_score:
                scoreList[i][j][0]=delete_score
                scoreList[i][j][1]=scoreList[i-1][j][1]+['delete '+original[i-1]]
            elif insert_score<=substitute_score and insert_score<=delete_score:
                scoreList[i][j][0]=insert_score
                scoreList[i][j][1]=scoreList[i][j-1][1]+['insert '+target[j-1]]
    score,operations=scoreList[n][m]
    return score, operations

print(dpWordEdit('SUOISL','S',{'copy': 18, 'delete': 10, 'insert': 18}))
# 操作所对应的分数可调整
# oplist = {'copy':5, 'delete':20, 'insert':20}
# 70
# ['delete c', 'delete a', 'copy n', 'copy e', 'insert w']
# 60
# ['copy s', 'insert l', 'delete h', 'copy e', 'copy e', 'copy p']
# 185
# ['copy a', 'copy l', 'insert l', 'insert i', 'copy g', 'insert a', 'insert t', 'copy o', 'copy r', 'delete i', 'delete t', 'delete h', 'delete m']
# 205
# ['insert r', 'delete d', 'copy e', 'insert l', 'insert e', 'insert a', 'insert s', 'insert e', 'delete b', 'delete u', 'delete g']
# 200
# ['insert s', 'insert n', 'delete d', 'copy i', 'copy f', 'copy f', 'copy i', 'insert n', 'insert g', 'delete c', 'delete u', 'delete l', 'delete t']
# 220
# ['insert f', 'delete d', 'delete i', 'copy r', 'insert a', 'insert m', 'copy e', 'insert w', 'delete c', 'delete t', 'copy o', 'copy r', 'insert k', 'delete y']
# 235
# ['insert t', 'delete w', 'delete o', 'delete n', 'delete d', 'copy e', 'copy r', 'insert r', 'insert i', 'copy f', 'insert i', 'insert c', 'delete u', 'delete l']
#
# oplist = {'copy':5, 'delete':10, 'insert':15}
# 45
# ['delete c', 'delete a', 'copy n', 'copy e', 'insert w']
# 45
# ['copy s', 'insert l', 'delete h', 'copy e', 'copy e', 'copy p']
# 125
# ['copy a', 'copy l', 'insert l', 'insert i', 'copy g', 'insert a', 'insert t', 'copy o', 'copy r', 'delete i', 'delete t', 'delete h', 'delete m']
# 135
# ['insert r', 'delete d', 'copy e', 'insert l', 'insert e', 'insert a', 'insert s', 'insert e', 'delete b', 'delete u', 'delete g']
# 130
# ['insert s', 'insert n', 'delete d', 'copy i', 'copy f', 'copy f', 'copy i', 'insert n', 'insert g', 'delete c', 'delete u', 'delete l', 'delete t']
# 145
# ['insert f', 'delete d', 'delete i', 'copy r', 'insert a', 'insert m', 'copy e', 'insert w', 'delete c', 'delete t', 'copy o', 'copy r', 'insert k', 'delete y']
# 150
# ['insert t', 'delete w', 'delete o', 'delete n', 'delete d', 'copy e', 'copy r', 'insert r', 'insert i', 'copy f', 'insert i', 'insert c', 'delete u', 'delete l']
#
# oplist = {'copy':10, 'delete':25, 'insert':20}
# 90
# ['delete c', 'delete a', 'copy n', 'copy e', 'insert w']
# 85
# ['copy s', 'insert l', 'delete h', 'copy e', 'copy e', 'copy p']
# 230
# ['copy a', 'copy l', 'insert l', 'insert i', 'copy g', 'insert a', 'insert t', 'copy o', 'copy r', 'delete i', 'delete t', 'delete h', 'delete m']
# 230
# ['insert r', 'delete d', 'copy e', 'insert l', 'insert e', 'insert a', 'insert s', 'insert e', 'delete b', 'delete u', 'delete g']
# 245
# ['insert s', 'insert n', 'delete d', 'copy i', 'copy f', 'copy f', 'copy i', 'insert n', 'insert g', 'delete c', 'delete u', 'delete l', 'delete t']
# 265
# ['insert f', 'delete d', 'delete i', 'copy r', 'insert a', 'insert m', 'copy e', 'insert w', 'delete c', 'delete t', 'copy o', 'copy r', 'insert k', 'delete y']
# 280
# ['insert t', 'delete w', 'delete o', 'delete n', 'delete d', 'copy e', 'copy r', 'insert r', 'insert i', 'copy f', 'insert i', 'insert c', 'delete u', 'delete l']