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



print(dpMuseumThief([{'w':1,'v':24},{'w':18,'v':8},{'w':1,'v':22}],3))
# 可有多种取法，以下只给出一种符合条件的宝物列表
# 29
# [{'w':2, 'v':3}, {'w':4, 'v':8}, {'w':5, 'v':8}, {'w':9, 'v':10}]
# 83
# [{'w': 1, 'v': 2}, {'w': 2, 'v': 3}, {'w': 4, 'v': 7}, {'w': 5, 'v': 8}, {'w': 6, 'v': 10}, {'w': 7, 'v': 12}, {'w': 8, 'v': 12}, {'w': 8, 'v': 13}, {'w': 9, 'v': 16}]
# 139
# [{'w': 1, 'v': 2}, {'w': 3, 'v': 5}, {'w': 4, 'v': 6}, {'w': 4, 'v': 7}, {'w': 6, 'v': 10}, {'w': 7, 'v': 12}, {'w': 8, 'v': 14}, {'w': 9, 'v': 15}, {'w': 9, 'v': 16}, {'w': 9, 'v': 17}, {'w': 10, 'v': 17}, {'w': 10, 'v': 18}]
# 164
# [{'w': 1, 'v': 2}, {'w': 3, 'v': 5}, {'w': 8, 'v': 13}, {'w': 9, 'v': 15}, {'w': 9, 'v': 16}, {'w': 10, 'v': 16}, {'w': 10, 'v': 17}, {'w': 11, 'v': 18}, {'w': 12, 'v': 19}, {'w': 13, 'v': 21}, {'w': 14, 'v': 22}]
# 246
# [{'w': 1, 'v': 2}, {'w': 3, 'v': 4}, {'w': 3, 'v': 5}, {'w': 9, 'v': 15}, {'w': 10, 'v': 17}, {'w': 11, 'v': 18}, {'w': 11, 'v': 19}, {'w': 12, 'v': 20}, {'w': 13, 'v': 21}, {'w': 14, 'v': 23}, {'w': 15, 'v': 24}, {'w': 15, 'v': 25}, {'w': 16, 'v': 26}, {'w': 17, 'v': 27}]
