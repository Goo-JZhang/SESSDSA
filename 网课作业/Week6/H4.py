def dpMuseumThief(treasureList, maxWeight):
    #外部记录，避免重复计算
    resultList=[[0,[]]]*(maxWeight+1)
    #找重复，可能有重量和价值一样的不同宝物
    def YinLiuZhiZhu(alist,item):
        count=0
        for i in alist:
            if i==item:
                count+=1
            else:
                pass
        return count
    #宝物按重量-价值排序
    def treasureSort(atreasureList):
        for i in range(len(atreasureList)):
            for j in range(i,len(atreasureList)):
                if atreasureList[j]['w']<atreasureList[i]['w']:
                    atreasureList[i],atreasureList[j]=atreasureList[j],atreasureList[i]
                elif atreasureList[j]['w']==atreasureList[i]['w']:
                    if atreasureList[j]['v']<atreasureList[i]['v']:
                        atreasureList[i],atreasureList[j]=atreasureList[j],atreasureList[i]
                else:
                    pass
        return atreasureList
    treasureList=treasureSort(treasureList)
    #开始找
    for i in range(maxWeight+1):
        temp_Max=0
        for j in treasureList:
            if j['w']>i:
                break#宝物重量大于负重就跳出，因为之前已经排过序了
            else:
                num1=YinLiuZhiZhu(resultList[i-j['w']][1],j)
                num2=YinLiuZhiZhu(treasureList,j)
                if num1<num2:#j能被拿走，因为它存在并且还没被拿走
                    tempV,tempL=resultList[i-j['w']]
                    if tempV+j['v']>temp_Max:
                        temp_Max=tempV+j['v']
                        resultList[i]=[temp_Max,tempL+[j]]
                    else:
                        pass
                else:
                    pass
    maxValue,choosenList=resultList[maxWeight]
    return maxValue, choosenList

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
        scoreList[i][0][1]=scoreList[i-1][0][1]+['delete',original[i-1]]#original前i位到target前0位
    for j in range(1,m+1):
        scoreList[0][j][0]=j*oplist['insert']
        scoreList[0][j][1]=scoreList[0][j-1][1]+['insert',target[j-1]]#original前0位变成target前j位
    for i in range(1,n+1):
        for j in range(1,m+1):
            substitute=oplist['copy'] if original[i-1]==target[j-1] else oplist['delete']+oplist['insert']
            substitute_score=substitute+scoreList[i-1][j-1][0]
            delete_score=oplist['delete']+scoreList[i-1][j][0]
            insert_score=oplist['insert']+scoreList[i][j-1][0]
            if substitute_score<=delete_score and substitute_score<=insert_score:
                scoreList[i][j][0]=substitute_score
                if original[i-1]==target[j-1]:
                    scoreList[i][j][1]=scoreList[i-1][j-1][1]+['copy',target[j-1]]
                else:
                    scoreList[i][j][1]=scoreList[i-1][j-1][1]+['delete',original[i-1]]+['insert',target[j-1]]
            elif delete_score<=substitute_score and delete_score<=insert_score:
                scoreList[i][j][0]=delete_score
                scoreList[i][j][1]=scoreList[i-1][j][1]+['delete',original[i-1]]
            elif insert_score<=substitute_score and insert_score<=delete_score:
                scoreList[i][j][0]=insert_score
                scoreList[i][j][1]=scoreList[i][j-1][1]+['insert',target[j-1]]
    score,operations=scoreList[n][m]
    return score, operations
